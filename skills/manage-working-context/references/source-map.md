# Source map: manage-working-context

Every hard instruction in this package maps to a record below. A record grounds the instruction in a Cognition Today article, attributes it to Aditya Shukla's master specification, or declares it a compiler design inference with no authority.

Load this file only when provenance, adaptation, or source-intent preservation is needed. It is not required to execute the skill.

## Contents

1. [Schema](#schema)
2. [Records](#records)
3. [Coverage note](#coverage-note)

## Schema

```yaml
- operation_id: stable-operation-name
  layer: source-grounded | author-specified | design-inference
  source_id: article-url#heading | master-specification#section | none
  source_claim: what-the-source-asserts | none
  design_inference: why-it-is-being-applied-to-an-agent
  agent_rule: executable-runtime-instruction
  validation_status: untested-or-tested-result
```

`layer: source-grounded` means an article supplies the mechanism and the agent-side application is the inference. `layer: author-specified` means Aditya Shukla specified the rule directly in the master implementation specification; no article claims it, but it is not the compiler's invention and is under change control. `layer: design-inference` means the compiler decided it and it may be revised on engineering grounds.

This package is predominantly `author-specified`. See `source-notes.md` for why.

## Records

```yaml
- operation_id: maintain-two-file-state-model
  layer: author-specified
  source_id: master-specification#5-runtime-state-model
  source_claim: none
  design_inference: Separating a small mutable working representation from a durable ledger prevents both a ledger that churns on every step and an active representation that grows until it costs as much as the history it replaced.
  agent_rule: Maintain working-context.md as the short mutable representation and memory-base.md as the durable ledger. Do not introduce a third state file.
  validation_status: untested

- operation_id: enforce-mutation-invariant
  layer: author-specified
  source_id: master-specification#5-runtime-state-model
  source_claim: none
  design_inference: Writing both files in one step makes it impossible to audit whether the ledger recorded what the working context actually held. Sequencing the writes makes the freeze inspectable.
  agent_rule: Never update both state files in the same ordinary work step. Consolidation is two sequential operations, freeze then derive.
  validation_status: untested

- operation_id: activate-only-on-trigger
  layer: author-specified
  source_id: master-specification#5-runtime-discovery-and-activation
  source_claim: none
  design_inference: An always-on state manager adds tokens and latency to work that was already fine, and crowds out domain reasoning.
  agent_rule: Activate only when at least one runtime trigger holds. Presence in the registry is not activation. Never install, copy, or modify the runtime automatically, and never recursively scan arbitrary filesystem locations.
  validation_status: untested

- operation_id: ingest-source-intent-capsule
  layer: author-specified
  source_id: master-specification#5-common-cognition-today-runtime-contract
  source_claim: none
  design_inference: A capsule preserves intent rather than words, which is what a resume actually needs and what a transcript is too expensive to supply.
  agent_rule: Accept the specified capsule fields on activation, ingest them into working-context.md, and report any missing required field rather than inventing a value.
  validation_status: untested

- operation_id: preserve-epistemic-layers-through-compression
  layer: author-specified
  source_id: master-specification#5-common-cognition-today-runtime-contract
  source_claim: none
  design_inference: Compression merges similar-looking lists first. Once source claims and design inferences are merged, provenance cannot be reconstructed, which defeats the purpose of the whole repository.
  agent_rule: Preserve the distinction among source claim, design inference, agent rule, and validation result during compression and retrieval. Individual entries may be shortened; the lists may never be merged.
  validation_status: untested

- operation_id: respect-ownership-boundary
  layer: author-specified
  source_id: master-specification#5-runtime-state-model
  source_claim: none
  design_inference: A state layer that begins making domain judgments becomes an unreviewed second opinion competing with the skill that owns the decision.
  agent_rule: Own state only. Never select a domain operation, judge a candidate, edit a domain artifact, or reinterpret or broaden a domain skill. Domain skills do not mutate the state files unless the runtime delegates a documented operation.
  validation_status: untested

- operation_id: judge-retrieval-completeness
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#metamemory
  source_claim: Metamemory supports judgments about whether and how something is known without complete retrieval.
  design_inference: The same judgment applies to state rather than to knowledge. A model resuming a thread will fluently generate a plausible account of what was decided, and that output is indistinguishable in tone from a real recovery.
  agent_rule: Report retrieval_status as complete only when every returned field was read from a file. Name every inferred or absent field in missing. Never present a reconstructed field as a retrieved one.
  validation_status: untested

- operation_id: separate-active-and-durable-stores
  layer: source-grounded
  source_id: https://cognitiontoday.com/memory-models-in-psychology-understanding-human-memory/
  source_claim: Memory models distinguish a limited-capacity active store where material is currently manipulated from a durable store where stable material is retained, with movement between them that is not automatic.
  design_inference: The transferable structure is the separation and the non-automatic transfer, not the neuroscience. This article is cited as the motivation for the author-specified two-file model rather than as its derivation.
  agent_rule: Treat promotion from working context to ledger as an explicit operation at a named boundary, never as a side effect of ordinary work.
  validation_status: untested
  verification: pending-source-read

- operation_id: reduce-corpus-to-pointers
  layer: source-grounded
  source_id: https://cognitiontoday.com/a-thrifty-brain-gave-us-multi-tasking-abilities/
  source_claim: Cognitive economy involves doing more within limited processing capacity by not reprocessing material that has already been handled.
  design_inference: Storing a specific pointer plus the conclusion drawn from a source is cheaper and more faithful than storing a paraphrase, which costs tokens and loses the ability to re-check.
  agent_rule: Reduce a large corpus to specific re-openable pointers plus conclusions and their basis. Do not store paraphrases of examined material.
  validation_status: untested
  verification: pending-source-read

- operation_id: consolidate-at-explicit-boundaries
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Consolidating on a timer or on every turn costs two writes per step and grows a file that is read on every resume. Consolidating mid-operation freezes a half-finished transformation that later reads as a settled decision.
  agent_rule: Consolidate only at a named boundary — user approval, workstream completion, thread pause, expected compaction, close of an iteration round, or session end.
  validation_status: untested

- operation_id: resolve-state-location
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: The specification defines the two files but not their path. Project scope is correct because working context is project-specific, and a visible path is correct because state an agent writes about a user's work should not be hidden from them.
  agent_rule: Resolve the state root in order of user instruction, documented project location, then .cognition-today/ at the workspace root. Never write to the home directory. Tell the user the path on first creation and never overwrite existing state on initialization.
  validation_status: untested

- operation_id: operate-in-degraded-mode
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Many clients cannot write files. Most of the value is the discipline of naming objective, invariants, rejections, and next action in a fixed structure; the files make that durable but are not what makes it useful.
  agent_rule: When no filesystem is available, maintain the same field structure in the visible conversation, state once that nothing is persisted, and never claim a file was written or that state will survive the session.
  validation_status: untested

- operation_id: report-retrieval-failures-without-filling-gaps
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: A state system fails safely when it loses information and says so, and dangerously when it substitutes something plausible. The user cannot distinguish the two from the output.
  agent_rule: On any missing file, broken pointer, malformed record, or absent field, name the gap and proceed with it stated. Never substitute a similar file, reconstruct from conversation and call it recovered, or delete state to resolve an inconsistency.
  validation_status: untested

- operation_id: version-the-capsule-contract
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: The capsule is a public interface that future Cognition Today skills will depend on. Without a version, a field rename silently breaks every existing caller.
  agent_rule: Declare capsule_version. Accept declared versions, state plainly when handed an unrecognized one, and treat any required-field or layer-rule change as a version increment under change control.
  validation_status: untested

- operation_id: bound-state-file-size
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: A state system that grows without bound recreates the problem it was built to solve.
  agent_rule: Target under 100 lines for working-context.md and under 400 for memory-base.md. Compress older thread capsules rather than recent ones, and never compress away a locked constraint, an approved decision, or a failed approach.
  validation_status: untested
```

## Coverage note

Records at `layer: design-inference` carry no authority and may be changed freely on engineering grounds when adapting this runtime.

Records at `layer: author-specified` are Aditya Shukla's design decisions. They are under the change-control rule and may not be altered without approval, even though no article claims them.

Records at `layer: source-grounded` must retain their attribution and source URL. Two of the three carry `verification: pending-source-read`, meaning the source claim was inferred from the article's subject matter rather than read from the article. Resolve before publication.

Every `validation_status` is `untested`. No forward evaluation has been run against this build.
