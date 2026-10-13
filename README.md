# Simulated Cognitive Skills for LLM Creativity and Metacognition

Cognitive-psychology frameworks by Aditya Shukla, compiled into auditable agent procedures.

> **Status: `v0.1.0-unpublished`. Not released.** All three skills are structurally complete and validated. None has been forward-tested. There are no benchmark results, and the sections below that would normally hold them say so plainly. See [Current status](#current-status).

## The problem

Models generate plausible work while quietly losing the thread. They confuse a familiar topic with retrieved knowledge. They repeat a strategy that has already failed, with more confidence each time. They converge on the first workable idea and call it a decision. Across a long session they overwrite the choices you already approved, and after a context compaction they cannot tell which constraints came from you and which they invented.

These are not knowledge failures. They are control failures — and prompting harder does not fix them, because the missing piece is a decision about *how* to proceed, not more effort at the current approach.

## What this is

Three skills that give an agent explicit procedures for the cognitive functions models most visibly lack: metacognition, creative cognition, and working memory.

The frameworks are not assembled from generic AI-era psychology content. They come from a body of published work by **Aditya Shukla** at [Cognition Today](https://cognitiontoday.com), and that body of work is the ground truth for this repository — the authority every operational rule is answerable to. You can trace any instruction back to the article claim that produced it.

**"Simulated" is the honest word, and it is load-bearing.** These skills do not give a model metacognition, imagination, or memory. They reproduce the *structure* of those functions as procedures a model can actually execute: a monitoring loop it must run, an operator it must select, a file it must write. The framework is authentic; the faculty is not claimed. Every package enforces that separation in its guardrails, and the evaluation rubrics penalize any output that blurs it.

| Skill | Simulates | What it does | When it fires |
| --- | --- | --- | --- |
| **Simulated Metacognition**<br>[`monitor-and-regulate-thinking`](skills/monitor-and-regulate-thinking/) | Metacognition and metamemory | Separates the task from a model of how the task is being approached, classifies what is known versus assumed versus merely familiar, then selects and applies one control operation | Planning under uncertainty, confidence calibration, personal or philosophical guidance, brainstorm phase decisions, reasoning that has stopped changing |
| **Simulated Creative Cognition**<br>[`create-through-recomposition`](skills/create-through-recomposition/) | Creative cognition and construal shifting | Decomposes an artifact into units, shifts construal or psychological distance, applies routed creative operators, and recomposes structural variants before converging | Explicit creative work, repeated aesthetic or narrative revision, open brainstorming, technical deadlock after two similar failed approaches |
| **Simulated Working Memory**<br>[`manage-working-context`](skills/manage-working-context/) | Working memory and consolidation | Preserves objective, locked constraints, approved decisions, rejected approaches, and source provenance across compaction, using a two-file state model | Long multi-thread sessions, expected compaction, thread switching, corpus reduction |

The folder names are the invocation identifiers; the bolded names are what the skills are. Both domain skills work fully without the runtime. None of the three activates just because it is installed.

The runtime is also the extension point. Future Cognition Today skills plug into it through a versioned source-intent capsule contract without the runtime being modified — see [`capsule-contract.md`](skills/manage-working-context/references/capsule-contract.md) for the schema and the compatibility checklist.

## Ideal use cases

These skills are for judgment-heavy work, not throughput. They add deliberation, which is exactly wrong for a task that already has a known procedure.

### Simulated Metacognition

Best when the hard part is not producing an answer but deciding whether the answer can be trusted, or how to proceed when the path is genuinely unclear.

- **Research and study.** Separating what you actually know from what merely feels familiar because you have read it three times. Fluency is not recall, and this is the skill built to catch that.
- **Planning under real uncertainty.** Surfacing which assumptions the plan depends on before committing to it, and naming what would have to be verified first.
- **Personal, philosophical, and reflective conversations.** Where you want your reasoning examined and alternatives held open rather than a confident verdict delivered.
- **Auditing a decision you keep circling.** The skill forces one control operation and a check on whether it changed anything.
- **Long analytical sessions that have gone flat**, where the model has started agreeing with its own earlier output instead of testing it.
- **Deciding whether to keep brainstorming.** Judging whether exploration is still producing new material or just producing volume.

### Simulated Creative Cognition

Best when the output is technically competent and creatively dead, and more instructions are not going to fix it.

- **Naming, positioning, and brand systems**, where the first ten options are recognizably the same option.
- **Fiction and narrative revision under constraint** — canon, voice, and established facts must survive the rewrite, so unstructured "be more creative" prompting is unusable.
- **Design and art direction stuck at generic.** Construal and distance shifts change which associations are reachable at all.
- **Concept work that needs structurally different options**, not synonyms. The skill's own test is whether variants differ in structure, not wording.
- **Technical deadlock after two similar fixes have failed.** At that point the problem representation is the likely fault, and the skill attacks the representation rather than attempting a third variation.

### Simulated Working Memory

Best when the work outlives the context window.

- **Multi-day or multi-session projects** resumed from a cold start, where the agent must state what it actually retained instead of reconstructing it plausibly.
- **Long agent runs that will hit a compaction** mid-task.
- **Iterative work where approved decisions keep getting silently reverted** several turns later.
- **Reducing a large corpus** into a working representation without losing which claim came from which source.
- **Parallel workstreams that bleed into each other**, where each needs its own preserved state.

### Who this is for

Writers, researchers, designers, analysts, and developers running long, judgment-heavy sessions with an agent — and anyone building agent systems who wants cognitive scaffolding with traceable provenance rather than prompt folklore.

### Where these will not help

Fast factual questions, deterministic transformations, formatting, routine edits, first-pass debugging, and fully specified tasks. All three skills are explicitly designed *not* to fire in those cases, and roughly a quarter of the evaluation corpus consists of negative prompts that check exactly that restraint.

## Installation

Copy **the whole skill folder**, not only `SKILL.md`. Full commands for Cursor, Claude Code, Codex, Windows, and macOS/Linux are in [`INSTALL.md`](INSTALL.md). The short version for Cursor on this machine:

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

That places the three folders in `~/.cursor/skills/` (`%USERPROFILE%\.cursor\skills\` on Windows). Restart Cursor and check **Customize → Skills**.

The two domain skills are independent of each other and of the runtime. Install one, two, or all three. Each package is self-contained: `SKILL.md`, `references/` loaded on demand, `agents/openai.yaml` for UI metadata, and `LICENSE.txt`. Nothing outside the folder is required at runtime.

Discovery of copied folders has been confirmed in Cursor at the documented path. Triggering, reference loading, and full workflows are still unverified — see [Current status](#current-status).

### Compatibility

| Client | Status |
| --- | --- |
| Any client supporting the Agent Skills format | Format-compatible, unverified |
| Codex | Untested |
| Claude Code | Untested |
| Cursor | Untested |

**Tested** means installation, discovery, triggering, reference loading, and at least one full workflow were verified. Nothing has earned that label yet.

"Model-agnostic" here means the capability is expressed in an open, model-neutral format. It does not mean behaviour will be identical across models. Trigger interpretation, instruction adherence, and output quality will vary.

## Before and after

*Not yet available.* Demonstrations require paired baseline and skill-assisted runs with recorded models, versions, costs, and judging method. None have been run. Fabricated examples would defeat the purpose of the repository.

The demonstration set to be produced first: familiarity versus actual knowledge; planning under uncertainty; narrative revision preserving canon; persistent technical deadlock; and a long creative project crossing a context compaction.

## Benchmark results

*Not yet available.* See [`benchmarks/`](benchmarks/) for the reporting template and [`evals/`](evals/) for the frozen-in-draft prompt sets and rubrics.

The evaluation design is published before the results deliberately: 40 prompts per domain skill split across positive, negative, boundary, and long-context classes, paired arms against an unmodified baseline, at least three model families, blind judging by two judges from different providers, and pre-registered pass gates. Any performance claim not backed by a filled run manifest and raw outputs in `benchmarks/` is unsupported.

## Provenance model

Every operational rule in this repository carries four separable layers:

| Layer | Example |
| --- | --- |
| **Source claim** | Object-level and meta-level cognition exchange information through monitoring and control |
| **Design inference** | Separating task state from a monitoring model may improve an agent's strategy selection |
| **Agent rule** | Identify the object task and the meta objective before regulating the process |
| **Validation result** | `untested` |

You can trace any instruction back to its origin. Open a package's `references/source-map.md`: each record names the operation, the exact source, the claim, the inference that bridged it to agent behaviour, the resulting rule, and its validation status.

Every record also declares who authored it:

| `layer` | Meaning | Can it be changed on engineering grounds? |
| --- | --- | --- |
| `source-grounded` | A cited Cognition Today article supplies the mechanism | No. Attribution and source URL must be retained |
| `author-specified` | Aditya Shukla specified it directly in the implementation specification. No article claims it, but it is not the compiler's invention | No. Under change control |
| `design-inference` | An engineering decision made while compiling the skill. No authority | Yes, freely |

The two-failure threshold before creativity may enter debugging is `design-inference` — an engineering guess, not psychology, and the map says so out loud. The two-file state model is `author-specified`. Neither is dressed up as a research finding.

Every `validation_status` in this build is `untested`. That will stay true until the evaluation set has been run.

## Ground truth

The authority for this repository is a specific body of published work: Aditya Shukla's writing on Cognition Today. These articles are not references consulted alongside other material — they are the ground truth. Where an article and an engineering convenience disagree, the article wins, and the disagreement is recorded rather than smoothed over.

Two things are worth keeping apart. The **authority of the sources** is settled: they are authored, published, dated, and citable. The **fidelity of this compilation to them** is not yet verified — the source notes were compiled from Aditya's implementation specification rather than read back against the articles themselves. That gap is mine, not the sources', and each package's `source-notes.md` carries a ledger of exactly which claims still need checking.

**Simulated Metacognition** — `monitor-and-regulate-thinking`

- [Metacognition & Metamemory Explained: Awareness, Reflection, Learning, and Mental health](https://cognitiontoday.com/metacognition-metamemory-meta-skills/)

**Simulated Creative Cognition** — `create-through-recomposition`

- [Creative Cognition: The Construal Level Theory & Psychological Distance](https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/)
- [15 Ways to Trigger the Brain's Creative Thinking Mode](https://cognitiontoday.com/creative-thinking/)
- [HOW Ideas come alive: Decompose & Recompose](https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/)

**Simulated Working Memory** — `manage-working-context`. Cited as motivation, not derivation. This package is predominantly author-specified rather than article-derived, and its article grounding is the weakest of the three. See its [`source-notes.md`](skills/manage-working-context/references/source-notes.md).

- [Memory Models in Psychology](https://cognitiontoday.com/memory-models-in-psychology-understanding-human-memory/)
- [A Thrifty Brain gave us Multi-tasking Abilities](https://cognitiontoday.com/a-thrifty-brain-gave-us-multi-tasking-abilities/)
- [Metacognition & Metamemory Explained](https://cognitiontoday.com/metacognition-metamemory-meta-skills/)

## Current status

| Item | State |
| --- | --- |
| All three skill packages | Complete, structurally validated |
| Structural validation in CI | Passing |
| Source maps | Complete, every record `untested` |
| Source notes | Compiled from the implementation specification; several sections await verification against the articles themselves |
| `manage-working-context` article grounding | Weakest of the three. Predominantly author-specified; all three articles unread |
| Evaluation prompts and rubrics | Written, unfrozen. 112 prompts, 4 rubrics |
| Private holdout set | Not written |
| Benchmark runs | None |
| Runtime state fixtures for recovery tests | Not written |
| Source visuals under `assets/` | None supplied; no diagram is bundled |
| Public release | Blocked. See [`BUILD-REPORT.md`](BUILD-REPORT.md) |

## Limitations

- **No performance evidence exists.** Every claim in this repository about what the skills do is a claim about their design, not their measured effect.
- **The source notes are second-hand.** They were compiled from the implementation specification rather than from the articles directly. Each `references/source-notes.md` carries a verification ledger marking which claims still need checking against the original text.
- **Trigger thresholds are guesses.** The two-failure gate, the three-variant default, and the three intensity levels are labeled design inferences because they are untested engineering choices.
- **The runtime has never written a state file.** Its formats, consolidation boundaries, and recovery behaviour are specified but have not been exercised once against a real session.
- **These are simulations, not faculties.** Nothing here gives software metacognition, memory, or creativity in the human sense. The frameworks supply the structure; the agent-side implementation is an explicit operational analogy and is documented as one throughout. That is what "simulated" means in the title, and it is not a hedge added late.

## License

Content is licensed [CC BY-NC-SA 4.0](LICENSE.txt). The accurate public label is **source-available for noncommercial use** — this is not an OSI-approved open source license. Free to use, adapt, and share with attribution under the same terms; commercial use and resale are prohibited.

Provided without warranty. These skills operationalize educational cognitive frameworks for agent workflows. They are not medical, psychological, legal, or other professional advice, and must not be used to diagnose a person or to claim that an agent possesses human mental states.

## Author

**Aditya Shukla** — writer and researcher at [Cognition Today](https://cognitiontoday.com), where the underlying frameworks were originally published.

- [GitHub](https://github.com/shredwarrior/)
- [LinkedIn](https://www.linkedin.com/in/aditya-shukla-1b8614ba/)
- [Miirae Core](https://miiraecore.com)

If this work is useful to you, [support Cognition Today](https://buymeacoffee.com/adityashukla).

To cite the repository or the underlying articles, see [`CITATION.cff`](CITATION.cff). To contribute, read [`CONTRIBUTING.md`](CONTRIBUTING.md) first — the provenance discipline is not optional.
