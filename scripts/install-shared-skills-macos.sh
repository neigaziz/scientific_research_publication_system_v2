#!/bin/bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE="$PROJECT_ROOT/skills"
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"
BACKUP="$HOME/.agents/skills-backup-$(date +%Y%m%d-%H%M%S)"
BACKUP_CREATED=0
for skill_dir in "$SOURCE"/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  [ -f "$skill_dir/SKILL.md" ] || { echo "Skipping $name: SKILL.md missing"; continue; }
  if [ -e "$DEST/$name" ]; then
    if diff -qr "$skill_dir" "$DEST/$name" >/dev/null 2>&1; then echo "Already current: $name"; continue; fi
    if [ "$BACKUP_CREATED" -eq 0 ]; then mkdir -p "$BACKUP"; BACKUP_CREATED=1; fi
    cp -R "$DEST/$name" "$BACKUP/"; rm -rf "$DEST/$name"
    echo "Backed up old $name to $BACKUP"
  fi
  cp -R "$skill_dir" "$DEST/$name"; echo "Installed $name"
done
echo "Shared Skills installed to $DEST. Enable them in Chatbox Settings → Skills. Open the project root in OpenCode."
