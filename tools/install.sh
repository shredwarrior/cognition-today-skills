#!/usr/bin/env bash
# Copy Cognition Today skill folders into a client skills directory.
# Run from the repository root:
#   ./tools/install.sh
#   ./tools/install.sh --client cursor --scope user
#   ./tools/install.sh --skills monitor-and-regulate-thinking,create-through-recomposition

set -euo pipefail

CLIENT="cursor"
SCOPE="user"
SKILLS="monitor-and-regulate-thinking,create-through-recomposition,manage-working-context"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --client) CLIENT="$2"; shift 2 ;;
    --scope) SCOPE="$2"; shift 2 ;;
    --skills) SKILLS="$2"; shift 2 ;;
    -h|--help)
      echo "Usage: ./tools/install.sh [--client cursor|claude|codex|agents] [--scope user|project] [--skills name,name]"
      exit 0
      ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_ROOT="$ROOT/skills"

if [[ ! -f "$SKILLS_ROOT/monitor-and-regulate-thinking/SKILL.md" ]]; then
  echo "Run this script from a clone of cognition-today-skills." >&2
  exit 1
fi

case "${CLIENT}-${SCOPE}" in
  cursor-user) DEST="${HOME}/.cursor/skills" ;;
  cursor-project) DEST="${ROOT}/.cursor/skills" ;;
  claude-user) DEST="${HOME}/.claude/skills" ;;
  claude-project) DEST="${ROOT}/.claude/skills" ;;
  codex-user) DEST="${HOME}/.codex/skills" ;;
  codex-project) DEST="${ROOT}/.codex/skills" ;;
  agents-user) DEST="${HOME}/.agents/skills" ;;
  agents-project) DEST="${ROOT}/.agents/skills" ;;
  *) echo "Unsupported combination: --client $CLIENT --scope $SCOPE" >&2; exit 1 ;;
esac

mkdir -p "$DEST"

IFS=',' read -r -a NAMES <<< "$SKILLS"
for name in "${NAMES[@]}"; do
  name="$(echo "$name" | xargs)"
  source="$SKILLS_ROOT/$name"
  if [[ ! -f "$source/SKILL.md" ]]; then
    echo "Skill folder not found: $source" >&2
    exit 1
  fi
  rm -rf "$DEST/$name"
  cp -R "$source" "$DEST/"
  echo "Installed $name -> $DEST/$name"
done

echo
echo "Restart the client if the skills do not appear."
echo "In Cursor, check Customize -> Skills, then try /<skill-folder-name> in Agent chat."
