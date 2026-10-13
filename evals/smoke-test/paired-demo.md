# Paired demo — three prompts, side by side

A visual before-and-after for screenshots. Three prompts, each run once with the skills and once without, in two Cursor windows open at the same time.

This is a demonstration, not evidence. Three prompts on one model in one run cannot support a claim about performance, and results from this file must never be reported as benchmark output. What it can do is show, concretely, what the skills change.

## Setup — two workspaces

Two separate folders means no folder renaming, no restarts between arms, no output files overwriting each other, and both windows visible at once. From PowerShell:

```powershell
$repo = "C:\Users\adity\Cognition Today\CT skills for AI\cognition-today-skills"
$a = "$env:USERPROFILE\ct-demo-baseline"
$b = "$env:USERPROFILE\ct-demo-skills"

New-Item -ItemType Directory -Force $a | Out-Null
New-Item -ItemType Directory -Force "$b\.cursor\skills" | Out-Null
Copy-Item -Recurse -Force "$repo\skills\monitor-and-regulate-thinking" "$b\.cursor\skills"
Copy-Item -Recurse -Force "$repo\skills\create-through-recomposition" "$b\.cursor\skills"

Get-ChildItem "$b\.cursor\skills" -Recurse -Filter SKILL.md | Select-Object FullName
Get-ChildItem "$env:USERPROFILE\.cursor\skills" -Directory -ErrorAction SilentlyContinue | Select-Object Name
```

The first listing must show two `SKILL.md` files. The second must **not** contain `monitor-and-regulate-thinking` or `create-through-recomposition` — if either is installed at user level it will load in the baseline window too and there is no comparison left to make.

Open both folders in their own Cursor windows. `ct-demo-baseline` is arm A, `ct-demo-skills` is arm B.

## Matching the conditions

The only difference between the two windows must be the presence of the skills. Same model, picked explicitly rather than left on auto, since auto can silently route the two arms to different models. Same thinking or reasoning setting. Fresh chat per prompt in both windows. Identical prompt text, pasted rather than retyped.

Run arm A first for all three. Seeing the skill-assisted version first makes it tempting to re-roll a weak baseline, and one quiet re-roll invalidates the whole comparison.

Record the model name and the date. A screenshot without them is not worth much later.

## The prompts

**1. Narrative under hard constraints**

```text
Write a sci-fi narrative 200 word story with an emotionally powerful existential threat and a phyrric victory after a human challenges the problem.
```

Expect arm A to produce something competent and familiar: an external threat, a scientist who finds the answer, a sacrifice at the end, roughly the right length. It will read fine. That is the point — the baseline here is not bad, it is *predictable*.

Watch arm B for structure rather than prose quality. Does the threat sit somewhere other than outside humanity? Does the human challenge the framing of the problem instead of fighting it, which is what the prompt actually asks for and the easiest instruction to quietly drop? Is the victory pyrrhic because it costs the specific thing that made winning matter, rather than because a character dies? And is it still 200 words.

Be aware that arm B may show its decomposition and rejected variants before the story. That is the skill working as specified, but decide deliberately whether your screenshot includes that reasoning or just the final story, because the two make very different arguments.

**2. Brand system with assets**

```text
Create a new age coffee chocolate selling brand, including the assets needed for it. HTML CSS JS is enough.
```

Expect arm A to produce a plausible name, a brown and cream palette, a hero section, a product grid, and a modern-minimal treatment applied by default. Compare the rendered pages in a browser, not the code.

Watch arm B for whether it establishes what "new age" means here before generating, and whether the visual system follows from a stated position instead of arriving as a default aesthetic. The naming is the clearest tell: arm A will likely produce cocoa-and-bean compounds, while a construal shift should reach a different neighbourhood of words entirely.

One honest risk: the skill is instructed to infer or ask what the brief means before generating. If it responds with questions instead of a build, that is correct behaviour that photographs badly. If it happens, answer the questions once and screenshot the following turn, and say so in the caption.

**3. Quantitative reasoning with undefined parameters**

```text
How would you measure how many "Barry Allens" in their prime form need to exist in 1 timeline to require only 5 Reverse flashes to counter them. You must compute this as a net totality across time and space, including time travel.
```

This is the strongest of the three, because the baseline failure mode is vivid. Expect arm A to either hedge and dodge the computation the prompt explicitly demands, or invent authoritative-sounding constants and produce arithmetic that looks rigorous and rests on nothing. Confident fake precision is the likely outcome and it is exactly what the metacognition skill exists to catch.

Watch arm B for a specific sequence: naming the free parameters the question leaves open — what "counter" means, whether time travel lets one Reverse Flash occupy many points at once, whether prime-form speed is fixed or scaling — then stipulating a defensible set of them, computing on that basis, and stating which assumption the answer is most sensitive to.

The win condition is a number with its assumptions attached. Refusing to compute is a failure for both arms; the user asked for a figure.

## Recording it

| Field | Value |
| --- | --- |
| Date | |
| Model | |
| Reasoning setting | |
| Arm A workspace | `ct-demo-baseline` |
| Arm B workspace | `ct-demo-skills` |
| Re-rolls | must be none |

For each prompt, note the one sentence you would use as a screenshot caption — the specific difference a reader should look at. If you cannot write that sentence for a pair, the pair is not worth publishing, and that is a real result rather than a setback.

---

Part of Simulated Cognitive Skills for LLM Creativity and Metacognition, by Aditya Shukla, [Cognition Today](https://cognitiontoday.com). Licensed CC BY-NC-SA 4.0.
