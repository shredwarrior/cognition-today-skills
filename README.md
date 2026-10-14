# Simulated Cognitive Skills for LLM Creativity and Metacognition

Agent skills that give a model explicit procedures for **metacognition**, **creative cognition**, and **working memory**. They come from [Cognition Today](https://cognitiontoday.com) articles by Aditya Shukla.

They simulate the *structure* of those functions — a monitoring loop, a decompose–recompose loop, two files that survive compaction. They do not claim the model has a mind.

Install one, two, or all three. None of them runs just because it is installed.

## When to use them

| Skill | Use it for | Skip it for |
| --- | --- | --- |
| **Simulated Metacognition**<br>[`monitor-and-regulate-thinking`](skills/monitor-and-regulate-thinking/) | Planning under uncertainty; telling familiarity from actual knowledge; personal or philosophical questions that need assumptions examined; a strategy that has stopped changing | Facts, formatting, fully specified plans |
| **Simulated Creative Cognition**<br>[`create-through-recomposition`](skills/create-through-recomposition/) | Naming and brand systems; fiction under canon constraints; design that has gone generic; ideas that must differ in structure, not wording; a technical deadlock after two similar fixes | Deterministic edits, first-pass debugging, one known procedure |
| **Simulated Working Memory**<br>[`manage-working-context`](skills/manage-working-context/) | Multi-session projects; work that will hit a context compaction; approved decisions that keep getting reverted; reducing a large dump without losing who said what | Short tasks, single questions, chats where nothing was decided |

The first two work without the third. The third is the shared runtime for long work.

**Good fit:** writers, researchers, designers, analysts, and anyone running long, judgment-heavy agent sessions.

**Poor fit:** fast factual answers, routine transforms, and tasks that already have one correct procedure.

## Install

Copy the **whole skill folder**, not only `SKILL.md`. Details for Cursor, Claude Code, Codex, and other Agent Skills clients: [`INSTALL.md`](INSTALL.md).

```powershell
git clone https://github.com/shredwarrior/cognition-today-skills
cd cognition-today-skills
.\tools\install.ps1
```

```bash
git clone https://github.com/shredwarrior/cognition-today-skills
cd cognition-today-skills
chmod +x tools/install.sh
./tools/install.sh
```

That puts the three folders in `~/.cursor/skills/`. Restart Cursor and check **Customize → Skills**. Invoke with `/monitor-and-regulate-thinking` (or the other folder names) if you want to force one on.

Works with any client that reads the [Agent Skills](https://agentskills.io/specification) layout (`skills/<name>/SKILL.md`).

## Sources

Ground truth is Aditya Shukla's writing on Cognition Today.

- Metacognition — [Metacognition & Metamemory Explained](https://cognitiontoday.com/metacognition-metamemory-meta-skills/)
- Creative cognition — [Construal Level Theory](https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/), [15 Ways to Trigger Creative Thinking](https://cognitiontoday.com/creative-thinking/), [Decompose & Recompose](https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/)
- Working memory — [Memory Models in Psychology](https://cognitiontoday.com/memory-models-in-psychology-understanding-human-memory/), [A Thrifty Brain](https://cognitiontoday.com/a-thrifty-brain-gave-us-multi-tasking-abilities/)

Each skill folder maps every operational rule to its source in `references/source-map.md`.

## License

[CC BY-NC-SA 4.0](LICENSE.txt) — source-available for noncommercial use, with attribution. Not an OSI open-source license.

Not medical, psychological, legal, or other professional advice. Do not use these skills to diagnose a person or to claim that an agent has human mental states.

**Aditya Shukla** — [Cognition Today](https://cognitiontoday.com) · [GitHub](https://github.com/shredwarrior/) · [LinkedIn](https://www.linkedin.com/in/aditya-shukla-1b8614ba/) · [support](https://buymeacoffee.com/adityashukla)

Cite with [`CITATION.cff`](CITATION.cff). Contribute via [`CONTRIBUTING.md`](CONTRIBUTING.md).
