# Chatbox AI setup — macOS

Chatbox Work Mode documents a tool-using loop with Skills, MCP, local code execution, Knowledge Base and Working Directory. Use a model that supports tool use. Skills are Agent Skills-compatible and Chatbox discovers `~/.agents/skills`; enable them in Settings → Skills. Custom MCP servers are in Settings → MCP; local stdio is desktop-only.

1. Extract this package to a stable path such as `~/Projects/scientific_research_publication_system_v2`.
2. Run `bash scripts/install-shared-skills-macos.sh` from the project root.
3. In Chatbox → Settings → Skills, verify and enable the 14 Skills. Restart Chatbox if needed.
4. Start a new chat in **Work Mode** before sending the first message (mode locks after the conversation starts).
5. Grant only this project folder as the chat's Working Directory.
6. Add `research-metadata` as a custom local stdio MCP server using `mcp-servers/CHATBOX_MCP_SETUP.md`, test/save it, then enable it in Work Mode.
7. Paste `CHATBOX_ORCHESTRATOR_PROMPT.md` or use this starter: "Act as the Scientific Research Orchestrator for this workspace. Read AGENTS.md, MASTER_ARCHITECTURE.md and the orchestrator routing and approval-gate files. Inspect available Skills/MCP tools and present a plan before performing scientific analysis."

## Platform boundary
Chatbox documentation describes Work Mode, Skills, MCP and iterative tool use; it does not document OpenCode-style named subagent/child-session definitions. Use OpenCode for full native multi-agent orchestration. Chatbox can still use the same Skills and MCP with sequential role handoffs in one Work Mode context.

## Computational caveat
Chatbox documents a Node.js/Bash sandbox and does not ship a Python scientific stack by default. Install and validate R, Python, BLUPF90, GCTA, PLINK, GATK and other research software separately on macOS; do not assume they exist in the Chatbox sandbox.