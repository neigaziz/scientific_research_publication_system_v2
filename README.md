# Scientific Research & Publication Agent System — v1.1.0

Cross-platform starter package for one Research Orchestrator, four specialist roles, 14 reusable Skills, shared artifact schemas/templates, evaluation material and a read-only Crossref/OpenAlex/PubMed metadata MCP server.

## Runtime roles
- **OpenCode macOS:** full native hybrid multi-agent system (one primary orchestrator plus four subagents).
- **Chatbox AI macOS:** companion Work Mode using the same Skills and MCP. Published Chatbox documentation describes Work Mode/Skills/MCP but not OpenCode-style named subagent sessions; explicit sequential role handoffs are included.
- **Shared Skills:** installed to `~/.agents/skills` for discovery by both apps.

## Quick start
1. Extract the ZIP to a stable folder, e.g. `~/Projects/scientific_research_publication_system_v2`.
2. `cd ~/Projects/scientific_research_publication_system_v2`
3. Install Skills: `bash scripts/install-shared-skills-macos.sh`.
4. Open this folder in OpenCode; project config selects `research-orchestrator`, with four subagent profiles under `.opencode/agents/`.
5. Install MCP: `bash scripts/setup-mcp-server-macos.sh`.
6. Configure Chatbox using `chatbox/CHATBOX_QUICKSTART.md` and `mcp-servers/CHATBOX_MCP_SETUP.md`.
7. Run `python3 scripts/validate-package.py` for offline structural validation.

## Main folders
`orchestrator/` routing and approvals; `skills/` all 14 Skill packages; `agents/` platform-neutral role descriptions; `.opencode/agents/` native profiles; `chatbox/` companion setup; `mcp-servers/` local reference MCP; `shared/` schemas/templates/registries; `evaluation/` test plan.

## Limitations
This package has not been installed on your Mac. Offline validation does not test MCP startup, live APIs, application discovery or scientific accuracy. Install it locally, configure your credentials if needed, enable Skills/MCP in each application, then test against domain-reviewed cases and real projects. No publication acceptance is guaranteed.
