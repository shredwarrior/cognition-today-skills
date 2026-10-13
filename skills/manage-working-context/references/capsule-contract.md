# Source-intent capsule contract

The interface between any Cognition Today skill and this runtime. Load this when ingesting a capsule, returning one on resume, or making a new skill runtime-compatible.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [What a capsule is for](#what-a-capsule-is-for)
3. [Schema version 1](#schema-version-1)
4. [The layer-separation rule](#the-layer-separation-rule)
5. [What the runtime returns on resume](#what-the-runtime-returns-on-resume)
6. [Worked capsule: monitor-and-regulate-thinking](#worked-capsule-monitor-and-regulate-thinking)
7. [Worked capsule: create-through-recomposition](#worked-capsule-create-through-recomposition)
8. [Making a new skill runtime-compatible](#making-a-new-skill-runtime-compatible)
9. [Versioning policy](#versioning-policy)
10. [Capsule anti-patterns](#capsule-anti-patterns)

## Epistemic legend

`[S]` article source claim, `[M]` specified by Aditya Shukla in the master specification, `[D]` compiler design inference, `[A]` agent rule, `[V]` validation result.

## What a capsule is for

`[M]` A domain skill hands the runtime a source-intent capsule when it activates the runtime. The capsule carries what must survive compression, compaction, or a thread switch.

`[D]` The capsule is deliberately not a transcript. A transcript preserves words; a capsule preserves intent. After a compaction the question is never "what was said" but "what were we doing, what did the user already decide, what did we rule out, and what is next." Those five things are cheap to store and expensive to reconstruct.

`[A]` The capsule is a handoff format, not a storage format. Ingest it into `working-context.md` in the structure defined by `state-model.md`. Do not store raw capsules alongside the state files.

## Schema version 1

`[M]` The field list is specified. `[D]` The required-versus-optional split and the version field are compiler additions.

```yaml
capsule_version: 1

# Required. A capsule missing any of these is incomplete; say so on ingest.
objective: ""              # what finishing looks like
active_skill: ""           # the skill handing off, by exact skill name
active_operation: ""       # the operation_id currently running
next_action: ""            # the single next thing to do

# Required when non-empty. Omit the key entirely when there is nothing to say.
source_ids: []             # article URLs or other source identifiers in play
governing_source_claims: []  # claims from those sources governing the operation
design_inferences: []      # agent-side operationalizations, labeled as inferences
locked_constraints: []     # constraints that survive every iteration
approved_elements: []      # what the user has explicitly approved
completed_transformations: []  # work already done that must not be redone
rejected_approaches: []    # what was set aside, each with its reason
open_uncertainties: []     # unresolved questions and what would resolve them
raw_material: []           # pointers to unstructured bulk awaiting transformation, never the bulk itself
```

`[M]` Omit irrelevant empty arrays at runtime, but never merge source claims with design inferences.

`[A]` On ingest, check the four required fields. If one is missing, store what you were given and tell the calling skill which field is absent. Do not invent a plausible value for a missing objective or next action.

`[D]` `raw_material` is an optional field added under the minor-change rule; the version stays at 1 and callers that never send it are unaffected.

`[A]` A populated `raw_material` list means the caller is holding bulk it wants transformed. Run the transform operation in `state-model.md` before the ingest completes: structure, freeze into `memory-base.md`, then derive the active slice. Entries must be pointers. A capsule that carries the bulk itself instead of a pointer to it is malformed — store it, say so, and transform it anyway rather than writing it through.

## The layer-separation rule

`[M]` Preserve the distinction among source claim, design inference, agent rule, and validation result during compression or retrieval.

`[A]` This is the one rule that may never be relaxed for space. When compressing, you may shorten any individual entry. You may not merge `governing_source_claims` into `design_inferences`, drop the labels, or summarize both into a single "context" paragraph.

`[D]` The reason is that this is exactly what compression destroys first. A summarizer sees two lists of similar-looking sentences and merges them. Three turns later nobody can tell which constraints came from a published source, which came from the user, and which the agent inferred — which is the precise failure this repository exists to prevent.

`[A]` If a capsule arrives with the layers already merged, store it, flag it, and do not attempt to re-separate them by guessing.

## What the runtime returns on resume

`[A]` On resume, return the same shape you were given, plus one field the caller did not send:

```yaml
capsule_version: 1
retrieval_status: complete | partial | unavailable
missing: []                # named fields that could not be recovered
# ...all recovered capsule fields...
```

`[A]` `retrieval_status` is mandatory on return. `partial` requires a populated `missing` list.

`[A]` Never return `complete` for a reconstructed capsule. If you inferred a field rather than reading it, the status is `partial` and the field is named in `missing`. See `compaction-and-recovery.md`.

## Worked capsule: monitor-and-regulate-thinking

```yaml
capsule_version: 1
objective: Decide whether to rebuild the sync layer or patch it, with a defensible basis.
active_skill: monitor-and-regulate-thinking
active_operation: diagnose-retrieval-condition
source_ids:
  - https://cognitiontoday.com/metacognition-metamemory-meta-skills/#theories-of-metamemory
governing_source_claims:
  - Cue familiarity, accessibility, competition, and their interaction offer different accounts of memory judgments.
design_inferences:
  - Requiring one specific checkable detail discriminates a familiar label from retrieved knowledge.
locked_constraints:
  - The migration window is fixed to the March release.
  - No new external dependencies.
approved_elements:
  - The user accepted the phased-cutover framing on 2026-08-01.
completed_transformations:
  - Classified the throughput claim as retrieved-unverified and scheduled a benchmark.
rejected_approaches:
  - Full rewrite. Ruled out because the migration window cannot absorb it.
open_uncertainties:
  - Whether the reported p99 latency was measured under production load or in staging.
next_action: Verify the p99 measurement conditions before choosing between rebuild and patch.
```

## Worked capsule: create-through-recomposition

```yaml
capsule_version: 1
objective: Land a brand system that reads as precise rather than clinical.
active_skill: create-through-recomposition
active_operation: recompose-variants
source_ids:
  - https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#what-can-we-make-of-these-processes
governing_source_claims:
  - Modified decomposed units can be recomposed into a new entity that can itself be decomposed and iterated.
design_inferences:
  - Three variants spanning conservative, structural, and high-distance cover the useful range at low cost.
locked_constraints:
  - The wordmark is final and does not change.
  - Accent colour stays "#4be4ff".
approved_elements:
  - Round 3 grid system, approved by the user.
completed_transformations:
  - Exhausted cross-domain borrowing and chance configuration on the typography direction.
rejected_approaches:
  - Serif display face. The user rejected it twice as "academic".
open_uncertainties:
  - Whether the accent colour survives at small sizes on the dark surface.
next_action: Apply one lower-construal pass to variant B, testing the accent at 12px on dark.
```

## Making a new skill runtime-compatible

`[D]` This section is the reason the contract is versioned and skill-agnostic. Future Cognition Today skills plug in here without this runtime being modified.

A new skill becomes runtime-compatible by doing four things. None of them require a change to this package.

**1. Embed the coordination block.** Copy the `## Cognition Today cognitive-runtime coordination` section verbatim from any existing Cognition Today `SKILL.md`. Do not paraphrase it — the discovery rules and the non-activation defaults are load-bearing.

**2. Declare the coordination in `SKILL.md` only.** Not in `agents/openai.yaml`. The `dependencies.tools` schema is for tool dependencies and must not be used to declare a dependency on another skill.

**3. Emit a valid capsule.** Populate the four required fields. Map your skill's own state schema onto the capsule fields:

| Your skill has | Maps to |
| --- | --- |
| Whatever you call the goal | `objective` |
| Your current `operation_id` | `active_operation` |
| Anything the user approved or fixed | `locked_constraints`, `approved_elements` |
| Anything you tried and set aside | `rejected_approaches`, each with a reason |
| Claims from your source articles | `governing_source_claims`, with `source_ids` |
| Your own operationalizations | `design_inferences`, kept separate |
| Bulk you are holding and do not want to carry | `raw_material`, as pointers only |
| Your single next step | `next_action` |

If your skill has state with no capsule field, do not invent one. Put it in `completed_transformations` with a label, or leave it out. Extending the schema is a version change.

**4. Stay functional without the runtime.** A domain skill must complete normally when this runtime is absent, retaining the same fields in the current context without claiming persistence. A skill that breaks without the runtime has made a required dependency out of an optional one.

**Compatibility checklist**

- [ ] Coordination block embedded verbatim
- [ ] Runtime not declared in `agents/openai.yaml`
- [ ] Four required capsule fields populated on activation
- [ ] Source claims and design inferences emitted as separate lists
- [ ] Every rejected approach carries a reason
- [ ] Bulk handed over as pointers in `raw_material`, never inlined or pre-summarized
- [ ] A sanity check requested before compaction, hand-off, and 98% context
- [ ] The skill completes with the runtime absent
- [ ] The skill does not write to the state files directly

## Versioning policy

`[D]` Compiler decision.

- `capsule_version: 1` is the current contract.
- Adding an optional field is a minor change; the version stays at 1 and older callers keep working.
- Renaming a field, removing one, changing a required field, or changing the layer-separation rule increments the version.
- The runtime must accept any capsule version it declares support for, and must say so plainly when handed one it does not recognize rather than guessing at the mapping.
- Changes to this contract require approval under the change-control rule, because every future skill depends on it.

## Capsule anti-patterns

| Anti-pattern | Why it fails | Correction |
| --- | --- | --- |
| Transcript in a capsule | Costs the tokens compaction was meant to save | Store pointers; capsule holds intent |
| Merged claim and inference lists | Destroys provenance permanently | Keep two lists even when one has a single entry |
| Rejected approaches with no reasons | The same direction returns three rounds later | Every rejection carries its reason |
| Empty arrays for every unused field | Bloats every read | Omit the key entirely |
| Vague `next_action` | Resume produces a restart | One sentence, one action |
| Capsule sent on a short task | Overhead with no benefit | Activation requires a trigger, not availability |
| Domain reasoning in the capsule | The runtime starts to look authoritative about the domain | Capsule carries state, not judgments |
| Bulk inlined into `raw_material` | Reproduces the dump the transform exists to prevent | Pointers only; the runtime reads the material itself |
| Dump summarized by the caller before handover | Merges the epistemic layers before the runtime can preserve them | Hand over the pointer unsummarized and let the transform structure it |

`[V]` untested.
