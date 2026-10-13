# Install the skills

Copy each skill **folder**, not just `SKILL.md`. A skill that cannot load its `references/` directory is incomplete.

License: [CC BY-NC-SA 4.0](LICENSE.txt). Source-available for noncommercial use. Attribution required.

The two domain skills work without the runtime. Install one, two, or all three.

| Skill folder | What you get |
| --- | --- |
| `skills/monitor-and-regulate-thinking` | Simulated Metacognition |
| `skills/create-through-recomposition` | Simulated Creative Cognition |
| `skills/manage-working-context` | Simulated Working Memory (optional runtime) |

After copying, restart the client if the skills do not appear. Cursor: **Customize → Skills**. Invoke explicitly with `/monitor-and-regulate-thinking` (or the other folder names) to confirm discovery.

---

## 1. Cursor — this machine, every project

Windows PowerShell:

```powershell
git clone https://github.com/shredwarrior/cognition-today-skills
cd cognition-today-skills
.\tools\install.ps1
```

That copies all three folders into `%USERPROFILE%\.cursor\skills\`. To install a subset:

```powershell
.\tools\install.ps1 -Skills monitor-and-regulate-thinking,create-through-recomposition
```

Manual copy, same destination:

```powershell
$dest = "$env:USERPROFILE\.cursor\skills"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Recurse -Force .\skills\monitor-and-regulate-thinking $dest
Copy-Item -Recurse -Force .\skills\create-through-recomposition $dest
Copy-Item -Recurse -Force .\skills\manage-working-context $dest
```

macOS / Linux:

```bash
git clone https://github.com/shredwarrior/cognition-today-skills
cd cognition-today-skills
chmod +x tools/install.sh
./tools/install.sh
```

## 2. Cursor — one project only

Copies into this repository's `.cursor/skills/`, so teammates who clone the project get the skills too.

```powershell
.\tools\install.ps1 -Scope project
```

```bash
./tools/install.sh --scope project
```

Open that project in Cursor. Confirm under Customize → Skills.

## 3. Cursor — import this GitHub repo as a plugin

If your Cursor build supports **Customize → From GitHub Repository**, paste:

```text
https://github.com/shredwarrior/cognition-today-skills
```

This repository includes `.cursor-plugin/marketplace.json` and `.cursor-plugin/plugin.json` so that import path can discover the three skills. If the UI does not list them, use the copy commands above — they are the reliable path.

## 4. Claude Code, Codex, or any Agent Skills client

The packages follow the [Agent Skills](https://agentskills.io/specification) layout (`skills/<name>/SKILL.md`).

| Client | User-level destination |
| --- | --- |
| Cursor | `~/.cursor/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Generic | `~/.agents/skills/` |

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

With GitHub CLI 2.8+ skill support:

```bash
gh skill install shredwarrior/cognition-today-skills --agent cursor --scope user
```

Replace `--agent cursor` with `claude-code`, `codex`, or omit it and follow the CLI prompt.

## 5. Confirm it worked

Each installed folder must contain all four of these:

```text
SKILL.md
LICENSE.txt
agents/openai.yaml
references/
```

If `references/` is missing, you copied a file instead of a folder. Delete the incomplete copy and run the installer again.

Skills do not run on every chat. The agent reads each `name` and `description` and decides relevance per turn. A factual question should not activate them. If you need to force a skill on, type `/` and pick the folder name.

## Uninstall

Delete the skill folder from the destination you copied it to. Restart the client.

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.cursor\skills\monitor-and-regulate-thinking"
Remove-Item -Recurse -Force "$env:USERPROFILE\.cursor\skills\create-through-recomposition"
Remove-Item -Recurse -Force "$env:USERPROFILE\.cursor\skills\manage-working-context"
```

---

Part of Simulated Cognitive Skills for LLM Creativity and Metacognition, by Aditya Shukla, [Cognition Today](https://cognitiontoday.com). Licensed CC BY-NC-SA 4.0.
