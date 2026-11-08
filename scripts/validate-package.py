#!/usr/bin/env python3
"""Offline structure/config/syntax validation; not an API or scientific accuracy test."""
from pathlib import Path
import json,re,ast,sys
ROOT=Path(__file__).resolve().parents[1]; errors=[]
skills=sorted((ROOT/'skills').glob('*/'))
if len(skills)!=14: errors.append(f'Expected 14 Skills; found {len(skills)}')
for d in skills:
    f=d/'SKILL.md'
    if not f.exists(): errors.append(f'Missing {f.relative_to(ROOT)}'); continue
    t=f.read_text(); m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
    if not m: errors.append(f'Invalid/missing frontmatter: {f.relative_to(ROOT)}'); continue
    name=re.search(r'^name:\s*(.+)$',m.group(1),re.M)
    if not name or name.group(1).strip()!=d.name: errors.append(f'name must match folder: {d.name}')
    for sd in ('workflows','references','tests'):
        if not (d/sd).is_dir(): errors.append(f'Missing {sd}/ in {d.name}')
required=['AGENTS.md','MASTER_ARCHITECTURE.md','README.md','orchestrator/routing-rules.md','orchestrator/workflow-management.md','orchestrator/approval-gates.md','opencode.json','chatbox/CHATBOX_ORCHESTRATOR_PROMPT.md','mcp-servers/research-metadata-mcp/pyproject.toml']
for rel in required:
    if not (ROOT/rel).exists(): errors.append('Missing '+rel)
try:
    cfg=json.loads((ROOT/'opencode.json').read_text())
    assert cfg.get('default_agent')=='research-orchestrator'
    assert cfg['mcp']['servers']['research-metadata']['disabled'] is True
except Exception as e: errors.append('OpenCode config validation failed: '+str(e))
for aid in ['research-orchestrator','research-intelligence','scientific-methods','computational-research','publication-review']:
    p=ROOT/'.opencode/agents'/f'{aid}.md'
    if not p.exists() or not p.read_text().startswith('---\n'): errors.append('Missing/invalid agent profile '+aid)
try: ast.parse((ROOT/'mcp-servers/research-metadata-mcp/research_metadata_mcp/server.py').read_text())
except Exception as e: errors.append('MCP Python syntax error: '+str(e))
if errors:
    print('VALIDATION FAILED'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('STRUCTURAL VALIDATION PASSED')
print(f'- {len(skills)}/14 Skills have matching folder names, SKILL.md frontmatter and support folders')
print('- 1 OpenCode primary orchestrator + 4 native subagent profiles present')
print('- OpenCode JSON config parses; metadata MCP is disabled pending installation')
print('- Python MCP server syntax parses')
print('- No live MCP startup/API tests or subject-matter accuracy benchmarks were run')
