# Source notes: working context and attention

Attributed notes for the three supporting sources of this runtime.

## Contents

1. [Status of this file](#status-of-this-file)
2. [Why this package is different](#why-this-package-is-different)
3. [Memory Models in Psychology](#memory-models-in-psychology)
4. [A Thrifty Brain gave us Multi-tasking Abilities](#a-thrifty-brain-gave-us-multi-tasking-abilities)
5. [Metacognition & Metamemory Explained](#metacognition--metamemory-explained)
6. [The master specification as a source](#the-master-specification-as-a-source)
7. [Verification ledger](#verification-ledger)

## Status of this file

**This package has the weakest article grounding of the three in this repository. Read this section before citing it.**

For the two domain skills, the master implementation specification named the article headings and restated the claims that each agent rule depends on. For this runtime it did neither. Section 2 of the specification lists three supporting sources and says only that they govern `manage-working-context` and do not enlarge the substantive logic of the domain skills. No headings, no claims, no anchors.

None of the three articles was read during this build.

Consequently, almost nothing in this package is `source-grounded`. The state contract is `author-specified` — Aditya Shukla defined it directly in Section 5 of the specification. The rest is compiler design inference. The entries below record what structure the runtime borrows and what still has to be checked, not what the articles say.

## Why this package is different

The distinction matters for change control and for public claims.

| Layer | What it means here | How much of this package |
| --- | --- | --- |
| `source-grounded` | An article claim supports the mechanism | Very little, and all of it pending verification |
| `author-specified` | Aditya Shukla specified it in the master specification | The two-file model, the mutation invariant, the capsule fields, the discovery rules, the activation triggers |
| `design-inference` | The compiler decided it | File locations, formats, consolidation boundaries, degraded mode, recovery behaviour, capsule versioning, size targets |

Do not describe this runtime publicly as derived from cognitive science until the ledger below is resolved. It is currently an engineering contract with a psychological motivation, which is a different and more modest claim.

## Memory Models in Psychology

Source: Aditya Shukla, [Memory Models in Psychology](https://cognitiontoday.com/memory-models-in-psychology-understanding-human-memory/), Cognition Today.

**Structure borrowed.** The separation between a limited-capacity active store where material is currently being manipulated, and a durable store where stable material is retained, with movement between them that is not automatic.

**Where it is used.** The two-file model in `state-model.md`; the consolidation boundary; the size targets.

**Verification.** `pending`. The specification supplies no claim from this article. The two-file model does not derive from it in this build — the model is `author-specified` and this article is cited as its motivation. Reading the article may confirm the analogy, refine it, or show that a different model in the article fits better.

**Caveat that must survive any revision.** Whatever the article says about human memory, the agent-side implementation is two markdown files. No encoding, storage, retrieval, consolidation, decay, or interference in the psychological sense occurs. `state-model.md` prohibits the vocabulary.

## A Thrifty Brain gave us Multi-tasking Abilities

Source: Aditya Shukla, [A Thrifty Brain gave us Multi-tasking Abilities](https://cognitiontoday.com/a-thrifty-brain-gave-us-multi-tasking-abilities/), Cognition Today.

**Structure borrowed.** Cognitive economy: doing more within limited processing capacity by not reprocessing what has already been handled, and the costs incurred when attention switches between tasks.

**Where it is used.** The corpus-reduction rules and the thread-switching procedure in `compaction-and-recovery.md`; the rationale for storing pointers rather than paraphrases.

**Verification.** `pending`. The specification supplies no claim from this article, and the title implies an evolutionary argument about multi-tasking whose relationship to the switching-cost framing used here is unverified. Do not attribute the switching-cost rationale to this article until it has been read.

## Metacognition & Metamemory Explained

Source: Aditya Shukla, [Metacognition & Metamemory Explained: Awareness, Reflection, Learning, and Mental health](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today.

**Structure borrowed.** Judgments about whether and how something is known, made without completing retrieval. Applied here to a different object: judging whether a piece of state was actually read from a file or merely reconstructed.

**Where it is used.** The `retrieval_status` field in the capsule contract; the confabulated-recovery prohibition in `compaction-and-recovery.md`.

**Verification.** `spec-attributed` for the underlying claim that metamemory supports judgments about whether something is known without complete retrieval, which the specification does state in Section 6.12. The application of that structure to file retrieval rather than to knowledge is a compiler design inference and is labeled as one.

**Note.** This is the only one of the three sources that the specification restates anywhere, and it does so in the context of the metacognition skill rather than this runtime.

## The master specification as a source

Source: Aditya Shukla, *Cognition Today Deep Cognitive Skills: Master Implementation Specification*, version 1.1-draft, 2026-08-03. Unpublished.

This is not an article and has no public URL. It is cited in `source-map.md` as `master-specification#<section>` so that author-specified rules can be traced without being confused for published claims.

Specified in Section 5 and carried into this package unchanged:

- The two-file model, its functions, and its mutation policy.
- The invariant that both files are never updated in the same ordinary work step.
- The seven discovery and activation rules.
- The six runtime activation triggers.
- The nine source-intent capsule fields.
- The instruction to preserve the distinction among source claim, design inference, agent rule, and validation result during compression or retrieval.
- The ownership boundary: the runtime owns state; the domain skill does not mutate the files; the runtime does not reinterpret or broaden a domain skill.

Specified in Section 11:

- The four runtime states to test, and the capsule validation schema.

If this specification is published or revised, update these citations. Rules at `layer: author-specified` are under change control and may not be altered on engineering grounds alone.

## Verification ledger

| Item | Status | Blocking public claims? |
| --- | --- | --- |
| Memory Models in Psychology — active versus durable store | `pending` | Yes, for any claim that the two-file model is derived from memory research |
| Memory Models in Psychology — consolidation | `pending` | Yes |
| A Thrifty Brain — cognitive economy | `pending` | Yes |
| A Thrifty Brain — switching costs | `pending` | Yes, and the framing itself may not match the article |
| Metacognition & Metamemory — judgment without complete retrieval | `spec-attributed` | No |
| Master specification Section 5 — state contract | Author-specified, complete | No |
| Master specification Section 11 — test states and capsule schema | Author-specified, complete | No |

Resolve every `pending` row against the articles before the first public release. Until then, describe this runtime as an engineering state contract, not as a cognitive model.
