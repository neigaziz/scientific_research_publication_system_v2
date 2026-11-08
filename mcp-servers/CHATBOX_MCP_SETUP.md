# Chatbox local MCP setup (macOS)

1. Run `bash scripts/setup-mcp-server-macos.sh`.
2. Chatbox desktop → Settings → MCP → add a custom **Local (stdio)** server.
3. Name: `research-metadata`.
4. Command: absolute path to `<project>/.venv/bin/python`.
5. Arguments: `-m` and `research_metadata_mcp` (separate args).
6. Set environment variables `CROSSREF_MAILTO` (your own email), optionally `OPENALEX_API_KEY` and `NCBI_API_KEY`.
7. Press **Test**, save after successful test, then enable in the Work Mode MCP panel.
8. Test with `health_check`, then `search_crossref_works`.

Official Chatbox guide: https://chatboxai.app/en/guide/work-mode/configuration. Custom local stdio servers are desktop-only according to the guide.