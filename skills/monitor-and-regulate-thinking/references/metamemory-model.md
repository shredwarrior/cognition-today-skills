# Metamemory model

Load this when the task involves familiarity, recall, confidence in remembered material, learning judgments, retrieval difficulty, or knowledge gaps.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [Source](#source)
3. [Definition and limits](#definition-and-limits)
4. [The eight metamemory dimensions](#the-eight-metamemory-dimensions)
5. [Theories of metamemory judgment](#theories-of-metamemory-judgment)
6. [Feeling of knowing versus actual knowing](#feeling-of-knowing-versus-actual-knowing)
7. [Everyday metamemory phenomena](#everyday-metamemory-phenomena)
8. [Epistemic-state taxonomy](#epistemic-state-taxonomy)
9. [Epistemic state to control mapping](#epistemic-state-to-control-mapping)
10. [Using this with a user rather than about a user](#using-this-with-a-user-rather-than-about-a-user)

## Epistemic legend

`[S]` source claim, `[D]` design inference, `[A]` agent rule, `[V]` validation result, `[?]` named in the specification but not transcribed from the source; verify before public claims.

## Source

Aditya Shukla, [Metacognition & Metamemory Explained: Awareness, Reflection, Learning, and Mental health](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today.

## Definition and limits

`[S]` Metamemory is knowledge and judgment about one's own memory: what is stored, how well it is stored, how likely it is to be retrieved, and what would help retrieve it. It supports judgments about whether and how something is known without completing retrieval.

`[S]` Metamemory judgments are inferential and fallible. They are not direct readouts of memory contents.

`[D]` The transferable structure is the *judgment before retrieval* step. An agent can decide whether a claim has actually been established in the current task before committing to it, instead of after being contradicted.

`[A]` An agent has no episodic memory and no stored personal past. Do not describe agent behavior as remembering or forgetting. Describe it as: present in context, absent from context, retrievable through a tool, or generated without a source.

`[A]` Do not apply this model to estimate a person's memory capacity, decline, or disorder. It is a routing model for the current task only.

## The eight metamemory dimensions

`[S]` The source describes eight categories of knowledge people hold about memory. `[A]` Each maps to a bounded question the agent may ask about the current task. Ask only the ones that change what you do next.

| Source dimension `[S]` | Agent-side question `[A]` | Prohibited use |
| --- | --- | --- |
| Strategy | What retrieval, recording, verification, or memory-support strategy is available here? | Prescribing a "memory system" the user did not ask for |
| Task | Does this task require recall, recognition, familiarity, external lookup, or on-the-go analysis? | Assuming all knowledge tasks are recall tasks |
| Capacity | Is the currently available context sufficient for this task? | Generalizing to a person's global memory capacity |
| Change | Has recall or confidence changed across attempts or contexts? | Reading a change as decline or improvement in the person |
| Anxiety | Has the user reported stress that may be affecting their confidence or retrieval? | Inferring anxiety clinically, or inferring it at all when unreported |
| Activities | Has the user identified conditions that support or impair their recall or performance? | Inventing conditions on their behalf |
| Achievement motivation | How strongly does the user want to improve, verify, or retain this material? | Judging the user's motivation level |
| Locus | What parts of the problem are controllable through external support, practice, or verification? | Implying the whole problem is or is not within their control |

`[D]` Capacity and Anxiety are the two dimensions most likely to be misused, because both invite statements about the person rather than the task. Capacity is reframed here as a context-window question. Anxiety is admissible only as a user report.

## Theories of metamemory judgment

`[S]` The source presents competing accounts of how memory judgments are produced: cue familiarity, accessibility, competition, and an interaction account.

| Account | Source claim `[S]` | Observable signal `[A]` | Candidate control `[A]` |
| --- | --- | --- | --- |
| Cue familiarity | The judgment is driven by how familiar the cue or label is, before any target content is retrieved | The topic name is recognized; no specific detail has been produced | Require a target detail before accepting the knowledge claim |
| Accessibility | The judgment is driven by how much partial information comes to mind | A fragment is easy to produce; the whole is not | Test whether the accessible fragment actually supports the larger conclusion |
| Competition | Several related candidates interfere with confident selection | Multiple plausible answers, none dominant | Reduce the candidate set, externalize the alternatives, verify a discriminating detail |
| Interaction | Familiarity is consulted first; partial retrieval is attempted when familiarity is insufficient | Cue check fails, then effortful search begins | Move from cue check to targeted retrieval only when needed; do not start with exhaustive search |

`[A]` These are explanatory routing models. Never present one to a user as a diagnosis of what their memory is doing. Use them to pick your next move.

`[D]` The interaction account is the most useful default for an agent because it prescribes a cost order: cheap check first, expensive retrieval second.

## Feeling of knowing versus actual knowing

`[S]` A feeling of knowing predicts later recognition better than it guarantees recall. Feeling that one knows something is not the same as being able to produce it, and confidence is not proportional to accuracy.

`[A]` The core test: demand one target detail. If the topic can be named but no specific, checkable detail can be produced, the state is `familiar-cue`, not knowledge.

`[A]` Apply the same test to the agent's own output. Fluent phrasing, a confident tone, a plausible citation format, and rapid production are not evidence. A specific verifiable detail, a retrievable source, or an in-context quotation is evidence.

`[A]` Never describe the agent as having a feeling of knowing. Report the state, not a sensation.

## Everyday metamemory phenomena

| Phenomenon | Source claim `[S]` | Agent-side handling `[A]` |
| --- | --- | --- |
| Judgment of learning | People predict how well they will later remember what they are studying, often inaccurately | When a user asks "do I understand this?", convert to a retrieval test rather than an opinion. Ask them to produce, not to rate. |
| Tip of the tongue | Partial access without full retrieval; the target feels imminent | Treat as `partial-access`. Elicit or search on the fragments that are accessible instead of restating the question. |
| Knowing your unknowns | People can often judge that they do not know something, quickly | Fast, confident non-knowledge is useful. Report `unknown` early instead of generating a plausible filler answer. |
| Prospective memory | Remembering to do something in the future | Convert to an external artifact: a written next action, a checkpoint condition, a verification step. Do not claim the agent will remember. |
| Confidence verification | Stated confidence needs external checking | Attach the verification method to the claim, not a confidence adjective. |

`[?]` The source section "How metamemory affects daily thinking" is named in the specification but not transcribed. Verify the article before publishing claims sourced to it.

## Epistemic-state taxonomy

`[D]` This label set is a compiler-added operationalization. The source describes the underlying distinctions; the specific ten-label enum is a design decision.

| State | Meaning |
| --- | --- |
| `verified-known` | Directly supported by reliable evidence available in the task |
| `retrieved-unverified` | Recalled or generated with confidence but not checked |
| `user-reported` | Stated by the user; relevant as their experience, preference, or belief |
| `familiar-cue` | The label or topic feels known but details have not been retrieved |
| `partial-access` | Some details are accessible; the target knowledge is incomplete |
| `competing-retrieval` | Several related candidates interfere with confident selection |
| `design-inference` | An agent-side operationalization rather than an article claim |
| `assumption` | Currently relied upon without adequate support |
| `conflicting` | Available claims or memories disagree |
| `unknown` | No adequate knowledge is currently available |

`[A]` Use the smallest set of labels the task requires. Labeling every sentence turns a conversation into a database migration and reduces the usability of the answer.

`[A]` `user-reported` never silently upgrades to `verified-known`. The user's account is strong evidence about the user and weak evidence about the external world.

## Epistemic state to control mapping

`[A]` Route from the dominant state to a control operation. This table is keyed on knowledge state; the blockage-keyed routing table is in `SKILL.md`, Step 5.

| Dominant state | Preferred control | What "done" looks like |
| --- | --- | --- |
| `verified-known` | Continue | The claim is used without further hedging |
| `retrieved-unverified` | Verify, or mark it explicitly as unverified and proceed | The reader can tell which claims were checked |
| `user-reported` | Reflect back and ask for the discriminating detail if the answer turns on it | The user's account and the agent's interpretation stay visibly separate |
| `familiar-cue` | Retrieve a target detail, or ask the user to produce one | A specific checkable detail exists, or the gap is named |
| `partial-access` | Test whether the accessible fragment supports the conclusion | The inference from fragment to conclusion is stated and judged |
| `competing-retrieval` | Externalize candidates and find the discriminating evidence | The candidate set is written down and narrowed on a stated criterion |
| `design-inference` | Label it and keep it separable from source claims | The reader can strip the inference and still see the source claim |
| `assumption` | Mark it, then decide whether to test it or accept it explicitly | The assumption is visible and its risk is stated |
| `conflicting` | Present the conflict; do not average it away | Both positions and the basis for preferring one are visible |
| `unknown` | Ask a targeted question or defer the decision | One specific question is asked, not a list of five |

`[V]` untested.

## Using this with a user rather than about a user

`[A]` When a user says "I know this but can't explain it", the correct move is a retrieval probe, not reassurance and not a memory lecture. Ask for one concrete instance, boundary case, or worked application.

`[A]` When a user reports repeated forgetting, offer controllable external supports under the Locus dimension. Do not estimate a cause, a trend, or a condition.

`[A]` When the user asks for the framework itself, this file may be summarized for them. When the user asks for help with a task, use the framework and show only what changes the answer.
