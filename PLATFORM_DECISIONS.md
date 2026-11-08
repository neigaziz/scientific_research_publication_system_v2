# Platform implementation decisions — v1.1.0

## OpenCode (primary multi-agent runtime)
The project contains one primary Research Orchestrator and four native OpenCode subagent profiles under `.opencode/agents/`. OpenCode supports agent profiles, subagent child sessions, reusable Skills and MCP servers. Project `opencode.json` selects `research-orchestrator` as the default and keeps the included metadata MCP disabled until setup.

## Chatbox AI (companion Work Mode client)
The project includes the same 14 Agent Skills, a Chatbox orchestrator prompt and MCP setup. Chatbox documents Work Mode tool loops, Skills, MCP, local code execution and a desktop Working Directory. Its published docs do not document OpenCode-style named subagents/child sessions; use sequential role handoffs inside one Work Mode context. OpenCode remains the native multi-agent runtime.

## Shared Skills
The installer copies all Skills to `~/.agents/skills`, a discovery location documented by both clients. OpenCode should be opened at this project root to load `.opencode/agents` and `opencode.json`. In Chatbox enable the discovered Skills in Settings → Skills.

## MCP
The included read-only `research-metadata` MCP server exposes Crossref, OpenAlex and PubMed metadata operations. It does not retrieve restricted full text, manage datasets, run statistical genetics software or submit manuscripts. The server starts disabled in OpenCode pending local setup; configure it as local stdio in Chatbox.

## Safety
MCP is disabled until explicitly configured. Shell/edit operations are approval-gated in OpenCode. In Chatbox use Smart Approval or Always Ask and grant only the research project directory. No API keys or personal email addresses are included.

## Compatibility
This configuration follows current OpenCode V2 documentation. Check `opencode --version` and current official docs before merging into a pre-existing global config. Do not overwrite `~/.config/opencode/opencode.json` blindly; this package uses project-level configuration.