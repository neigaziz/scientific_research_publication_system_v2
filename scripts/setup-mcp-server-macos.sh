#!/bin/bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"
command -v python3 >/dev/null 2>&1 || { echo "python3 not found; install Python 3.10+" >&2; exit 1; }
python3 -c 'import sys; assert sys.version_info >= (3,10), "Python 3.10+ required"; print("Using",sys.version)'
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ./mcp-servers/research-metadata-mcp
python -m compileall -q ./mcp-servers/research-metadata-mcp/research_metadata_mcp
echo "Installed MCP server in $PROJECT_ROOT/.venv"
echo "Python executable: $PROJECT_ROOT/.venv/bin/python"
echo "Configure Chatbox using mcp-servers/CHATBOX_MCP_SETUP.md"
echo "For OpenCode, remove disabled:true from opencode.json after setup and set provider environment variables."
