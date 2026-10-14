# Install

Copy each skill **folder** (`SKILL.md`, `references/`, `agents/`, `LICENSE.txt`). Copying only `SKILL.md` will not work.

License: [CC BY-NC-SA 4.0](LICENSE.txt), noncommercial, attribution required.

| Folder | Skill |
| --- | --- |
| `skills/monitor-and-regulate-thinking` | Simulated Metacognition |
| `skills/create-through-recomposition` | Simulated Creative Cognition |
| `skills/manage-working-context` | Simulated Working Memory (optional) |

Install one, two, or all three. After copying, restart the client. In Cursor: **Customize → Skills**, or type `/` and the folder name.

## Cursor — every project on this machine

Windows:

```powershell
git clone https://github.com/shredwarrior/cognition-today-skills
cd cognition-today-skills
.\tools\install.ps1
```

Subset:

```powershell
.\tools\install.ps1 -Skills monitor-and-regulate-thinking,create-through-recomposition
```

macOS / Linux:

```bash
git clone https://github.com/shredwarrior/cognition-today-skills
cd cognition-today-skills
chmod +x tools/install.sh
./tools/install.sh
```

Destination: `~/.cursor/skills/` (`%USERPROFILE%\.cursor\skills\` on Windows).

## Cursor — this project only

```powershell
.\tools\install.ps1 -Scope project
```

```bash
./tools/install.sh --scope project
```

## Cursor plugin import

**Customize → From GitHub Repository:**

```text
https://github.com/shredwarrior/cognition-today-skills
```

If that UI does not list the skills, use the copy commands above.

## Claude Code, Codex, other Agent Skills clients

```powershell
.\tools\install.ps1 -Client claude
.\tools\install.ps1 -Client codex
.\tools\install.ps1 -Client agents
```

```bash
./tools/install.sh --client claude
./tools/install.sh --client codex
./tools/install.sh --client agents
```

| Client | User-level folder |
| --- | --- |
| Cursor | `~/.cursor/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Generic | `~/.agents/skills/` |

Or:

```bash
gh skill install shredwarrior/cognition-today-skills --agent cursor --scope user
```

## Uninstall

Delete the skill folder from the destination you copied it to, then restart the client.
