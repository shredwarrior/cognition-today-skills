# Source notes: metacognition and metamemory

Attributed notes for the single canonical source of this skill. Organized under the source's own section headings.

Source: Aditya Shukla, [Metacognition & Metamemory Explained: Awareness, Reflection, Learning, and Mental health](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today.

## Contents

1. [Status of this file](#status-of-this-file)
2. [What is metacognition?](#what-is-metacognition)
3. [Levels of metacognition](#levels-of-metacognition)
4. [Cognition vs. Metacognition](#cognition-vs-metacognition)
5. [Metamemory](#metamemory)
6. [Theories of metamemory](#theories-of-metamemory)
7. [How metamemory affects daily thinking](#how-metamemory-affects-daily-thinking)
8. [Meta-skills](#meta-skills)
9. [How metacognition, metamemory, and meta-skills affect us](#how-metacognition-metamemory-and-meta-skills-affect-us)
10. [Verification ledger](#verification-ledger)

## Status of this file

This build was compiled from the master implementation specification, which names the source headings and states the claims the agent rules depend on, but does not reproduce the article text. Each section below therefore records:

- **Relied-upon claim** — the source assertion the specification attributes to that section and that an agent rule currently depends on.
- **Verification** — `spec-attributed` where the claim comes from the specification's own restatement of the source, or `pending` where the specification names the section without supplying its content.

No section below is a quotation. Nothing here should be cited as the article's exact wording. Before public release, read the article and replace `pending` entries with attributed notes and, where useful, short quotations within fair-use limits.

## What is metacognition?

**Relied-upon claim.** Metacognition is thinking about thinking: it includes both awareness of one's own cognitive processes and the modification of those processes.

**Depends on it.** `regulate-thinking` in `source-map.md`; the requirement in `SKILL.md` that monitoring must terminate in an applied control operation.

**Verification.** `spec-attributed`. The specification asserts this claim of the section anchored at `#what-is-metacognition`.

## Levels of metacognition

**Relied-upon claim.** Metacognitive activity is layered rather than uniform; awareness, reflection, and regulation operate at different depths.

**Depends on it.** The Light / Standard / Persistent intensity selection in `SKILL.md`.

**Verification.** `pending`. The specification names this heading but does not transcribe the level scheme. The three-level intensity ladder in `SKILL.md` is a compiler-added design inference and is labeled as such in `source-map.md`; it is not presented as the source's own taxonomy.

## Cognition vs. Metacognition

**Relied-upon claim.** Object-level cognition and meta-level cognition exchange information: monitoring passes information upward from object to meta, and control passes information downward from meta to object.

**Depends on it.** `separate-object-and-meta-levels`; the entire loop structure in `metacognition-model.md` and `source-graph.yaml`.

**Verification.** `spec-attributed`. Anchored at `#cognition-vs-metacognition`.

**Caveat preserved.** The source describes human cognitive architecture. The agent-side two-level representation is an explicit operational analogy, not a claim that the model contains two systems.

## Metamemory

**Relied-upon claims.**

1. Metamemory is knowledge and judgment about one's own memory.
2. It supports judgments about whether and how something is known without completing retrieval.
3. The source describes eight categories of knowledge about memory: strategy, task, capacity, change, anxiety, activities, achievement motivation, and locus.
4. Feeling that one knows something is distinguishable from actually knowing it.

**Depends on it.** `classify-knowledge-state`; the eight-dimension table and the feeling-of-knowing test in `metamemory-model.md`.

**Verification.** `spec-attributed` for claims 1-3, anchored at `#metamemory`. Claim 4 is `spec-attributed` through the specification's repeated instruction not to treat familiarity as knowledge, but the article's exact framing of feeling-of-knowing is `pending`.

## Theories of metamemory

**Relied-upon claim.** Cue familiarity, accessibility, competition, and their interaction offer competing accounts of how memory judgments are produced.

**Depends on it.** `diagnose-retrieval-condition`; the four-account routing table in `metamemory-model.md`.

**Verification.** `spec-attributed`. Anchored at `#theories-of-metamemory`.

**Caveat preserved.** These are competing explanatory accounts, not a settled mechanism. The skill uses them to select a control action and is forbidden from presenting any of them to a user as a diagnosis.

## How metamemory affects daily thinking

**Relied-upon claim.** Metamemory phenomena — judgments of learning, tip-of-the-tongue states, recognizing one's own unknowns, prospective memory, and confidence verification — shape ordinary reasoning and study behavior.

**Depends on it.** The everyday-phenomena table in `metamemory-model.md`.

**Verification.** `pending`. The specification lists these phenomena as required reference content but does not transcribe the source's treatment of them. The agent-side handling column is a design inference throughout.

## Meta-skills

**Relied-upon claim.** Higher-order skills group into families including planning, evaluation, monitoring, strategizing, and execution.

**Depends on it.** The meta-skill family table in `metacognition-model.md`.

**Verification.** `spec-attributed` for the family list; `pending` for the source's definitions and examples of each family.

## How metacognition, metamemory, and meta-skills affect us

**Relied-upon claims.**

1. Metacognitive activity can serve an evaluative or rationalizing function as well as a controlling function.
2. The rationalizing function warrants caution: a post-hoc account can be persuasive without being accurate.
3. Human metacognitive judgments are accompanied by epistemic feelings, which are informative but fallible.

**Depends on it.** The evaluative-versus-controlling section and the epistemic-feelings prohibition in `metacognition-model.md`.

**Verification.** `spec-attributed` for the existence of the two functions and for the caution about rationalizing, both of which the specification requires be preserved as source caveats. `pending` for the article's mental-health discussion, which this skill deliberately does not operationalize.

**Boundary.** The source article discusses mental health. This skill does not. Diagnosis, therapy, and disorder inference are non-goals; see the guardrails in `SKILL.md`.

## Verification ledger

| Section | Status | Blocking public claims? |
| --- | --- | --- |
| What is metacognition? | `spec-attributed` | No |
| Levels of metacognition | `pending` | Yes, if the intensity ladder is ever attributed to the source |
| Cognition vs. Metacognition | `spec-attributed` | No |
| Metamemory | `spec-attributed` (claims 1-3) | No |
| Theories of metamemory | `spec-attributed` | No |
| How metamemory affects daily thinking | `pending` | Yes |
| Meta-skills | Partial | Yes, for per-family definitions |
| How metacognition, metamemory, and meta-skills affect us | `spec-attributed` (functions and caveat) | No |

Resolve every `pending` row against the article before the first public release.
