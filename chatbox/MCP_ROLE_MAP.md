# MCP role map

| Server | Skills | Purpose | Permission |
|---|---|---|---|
| `research-metadata` (included) | 02, 12, 14 | Crossref/OpenAlex/PubMed bibliographic metadata | Read-only |
| Full-text retrieval (optional) | 02, 10, 11 | Legally accessible full text | Respect access/licence limits |
| GitHub (optional) | 06, 08 | Version-controlled pipelines | Read-only by default; ask before write/push |
| Context7 (optional) | 06, 07 | Current software documentation | Read-only |

Enable only necessary, reviewed servers. Do not embed secrets in Skills or checked-in configuration.