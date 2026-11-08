# Research Metadata MCP Server

Read-only MCP server for Crossref, OpenAlex and PubMed bibliographic metadata. Tools: `health_check`, `search_crossref_works`, `get_crossref_work_by_doi`, `search_openalex_works`, `search_pubmed`. It cannot fetch restricted full text, modify databases, execute statistical analyses or submit manuscripts.

## Install
From project root: `bash scripts/setup-mcp-server-macos.sh`.

Optional environment variables: `CROSSREF_MAILTO` (your own contact email; recommended for Crossref), `OPENALEX_API_KEY` (recommended for larger workloads/cursor paging), and `NCBI_API_KEY` (optional). Keep secrets in the client's environment configuration or a local ignored environment file, never in source or Skills.

Metadata is not full-text evidence. Verify records against publisher records and inspect the paper to validate whether it supports a claim. This build has not been live-tested against remote APIs.
