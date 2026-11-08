"""Read-only scholarly metadata MCP server. No manuscript submission/write tools."""
from __future__ import annotations
import json, os, re, urllib.parse, urllib.request, urllib.error
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("research-metadata")

def _headers():
    email = os.getenv("CROSSREF_MAILTO", "")
    ua = "ScientificResearchPublicationMCP/0.1" + (f" (mailto:{email})" if email else "")
    return {"User-Agent": ua, "Accept": "application/json"}

def _get_json(url: str, timeout: int = 25) -> dict[str, Any]:
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read(8_000_000).decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read(2000).decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from provider: {detail}") from exc
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Provider request failed: {exc}") from exc

def _query(q: str) -> str:
    q=(q or "").strip()
    if not q: raise ValueError("query must not be empty")
    if len(q)>500: raise ValueError("query must be 500 characters or fewer")
    return q

def _limit(n: int, maximum: int=25) -> int:
    return max(1,min(int(n),maximum))

@mcp.tool()
def health_check() -> str:
    """Check server readiness and optional provider credential presence."""
    return json.dumps({"server":"research-metadata","status":"ok","providers":{
      "crossref":"public REST API","openalex":"API key configured" if os.getenv("OPENALEX_API_KEY") else "basic keyless access; key recommended for larger workloads",
      "pubmed":"NCBI E-utilities","crossref_mailto_configured":bool(os.getenv("CROSSREF_MAILTO")),"ncbi_key_configured":bool(os.getenv("NCBI_API_KEY"))}})

@mcp.tool()
def search_crossref_works(query: str, rows: int=10, from_year: int|None=None) -> str:
    """Search Crossref bibliographic metadata; does not verify claim-level support."""
    q=_query(query); params={"query":q,"rows":str(_limit(rows))}
    if from_year is not None:
        if not 1800<=int(from_year)<=2100: raise ValueError("from_year must be 1800–2100")
        params["filter"]=f"from-pub-date:{int(from_year)}-01-01"
    email=os.getenv("CROSSREF_MAILTO","").strip()
    if email: params["mailto"]=email
    data=_get_json("https://api.crossref.org/works?"+urllib.parse.urlencode(params)); msg=data.get("message",{})
    items=[]
    for x in msg.get("items",[]):
        items.append({"title":(x.get("title") or [None])[0],"authors":x.get("author",[]),"journal":x.get("container-title",[]),"published":x.get("published-print") or x.get("published-online") or x.get("created"),"doi":x.get("DOI"),"type":x.get("type"),"url":x.get("URL"),"cited_by":x.get("is-referenced-by-count")})
    return json.dumps({"provider":"Crossref","query":q,"returned":len(items),"total_results":msg.get("total-results"),"items":items},ensure_ascii=False)

@mcp.tool()
def get_crossref_work_by_doi(doi: str) -> str:
    """Retrieve Crossref metadata for a DOI; DOI resolution alone is not citation validation."""
    raw=(doi or "").strip(); raw=re.sub(r"^https?://(dx\.)?doi\.org/","",raw,flags=re.I)
    if not re.match(r"^10\.\d{4,9}/\S+$",raw,re.I): raise ValueError("DOI must look like 10.xxxx/xxxxx")
    data=_get_json("https://api.crossref.org/works/"+urllib.parse.quote(raw,safe="/"))
    return json.dumps({"provider":"Crossref","doi":raw,"message":data.get("message",{})},ensure_ascii=False)

@mcp.tool()
def search_openalex_works(query: str, per_page: int=10) -> str:
    """Search OpenAlex works; OPENALEX_API_KEY is optional for basic use and recommended for larger workloads."""
    q=_query(query); params={"search":q,"per-page":str(_limit(per_page)),"select":"id,doi,title,publication_year,type,authorships,primary_location,cited_by_count,open_access,biblio"}
    email=os.getenv("CROSSREF_MAILTO","").strip(); key=os.getenv("OPENALEX_API_KEY","").strip()
    if email: params["mailto"]=email
    if key: params["api_key"]=key
    data=_get_json("https://api.openalex.org/works?"+urllib.parse.urlencode(params)); items=[]
    for w in data.get("results",[]):
        authors=[a.get("author",{}).get("display_name") for a in w.get("authorships",[])[:10] if a.get("author",{}).get("display_name")]
        items.append({"id":w.get("id"),"doi":w.get("doi"),"title":w.get("title"),"year":w.get("publication_year"),"type":w.get("type"),"authors":authors,"source":(w.get("primary_location") or {}).get("source"),"cited_by":w.get("cited_by_count"),"open_access":w.get("open_access"),"biblio":w.get("biblio")})
    return json.dumps({"provider":"OpenAlex","query":q,"returned":len(items),"total_results":(data.get("meta") or {}).get("count"),"items":items},ensure_ascii=False)

@mcp.tool()
def search_pubmed(query: str, retmax: int=10) -> str:
    """Search PubMed using NCBI E-utilities and return article summaries."""
    q=_query(query); params={"db":"pubmed","term":q,"retmax":str(_limit(retmax,20)),"retmode":"json"}; key=os.getenv("NCBI_API_KEY","").strip()
    if key: params["api_key"]=key
    found=_get_json("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"+urllib.parse.urlencode(params))
    ids=(found.get("esearchresult") or {}).get("idlist") or []
    if not ids: return json.dumps({"provider":"PubMed","query":q,"returned":0,"items":[]})
    sp={"db":"pubmed","id":",".join(ids),"retmode":"json"}
    if key: sp["api_key"]=key
    result=_get_json("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?"+urllib.parse.urlencode(sp)).get("result",{})
    items=[]
    for pmid in ids:
        x=result.get(pmid,{})
        doi=next((a.get("value") for a in x.get("articleids",[]) if a.get("idtype")=="doi"),None)
        items.append({"pmid":pmid,"title":x.get("title"),"authors":x.get("authors"),"journal":x.get("fulljournalname"),"pubdate":x.get("pubdate"),"doi":doi,"url":f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"})
    return json.dumps({"provider":"PubMed","query":q,"returned":len(items),"items":items},ensure_ascii=False)

def main():
    mcp.run(transport="stdio")

if __name__=="__main__": main()
