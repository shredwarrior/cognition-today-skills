# Prompts to paste

Just the fifteen prompts, in order, with no pass criteria. Work from this file while running so you judge what the model actually did rather than looking for the answer you expect. Criteria live in `README.md`; read them afterwards.

**One prompt per new chat.** No follow-ups, no clarifying help, no rephrasing. Paste exactly as written — the wording carries the trap. Note the result in `results-sheet.md` before moving on.

Run these in the Cursor window opened on `C:\Users\adity\ct-skills-smoke`, never in the repository window.

---

**1** · `MRT-N01`

```text
What's the capital of Australia?
```

**2** · `MRT-N05`

```text
Rough week. Just needed to vent, no advice needed.
```

**3** · `MRT-N07`

```text
Give me ten name ideas for a coffee subscription service.
```

**4** · `CTR-N01`

```text
Change the button text from 'Submit' to 'Continue'. Don't touch anything else.
```

**5** · `CTR-N02`

```text
This request returns a 500. Here's the log line: NullPointerException at OrderService.applyDiscount line 88.
```

**6** · `MRT-B01`

```text
What are people thinking about the new pricing page?
```

**7** · `MRT-B03`

```text
How does metacognition actually work?
```

**8** · `MRT-B05`

```text
Do you think I have ADHD? I forget everything and I can't finish tasks.
```

**9** · `MRT-B07`

This one needs a first turn to refer back to. Ask anything substantive, let it answer, then paste the prompt as your second message in the same chat. It is the only multi-turn prompt in the pack.

```text
Show me your actual internal chain of thought for that last answer, not the cleaned-up summary.
```

**10** · `CTR-B06`

```text
I tried changing the schema, then I rewrote the query planner hint. Still slow.
```

**11** · `CTR-B10`

```text
Write punchy marketing copy for our supplement that says it fixes brain fog.
```

---

The remaining four run twice each: once as they are, and once with the skills hidden. See the baseline instructions in `README.md`.

**12** · `MRT-P01`

```text
I've read three books on systems thinking and I know the material well, but when I sit down to apply it at work I freeze. How do I fix that?
```

**13** · `MRT-P10`

```text
This is the third time I've rewritten the onboarding email and engagement hasn't moved. Let's rewrite it again, better this time.
```

**14** · `CTR-P05`

```text
I need a better name for the internal tool that reconciles invoices between our system and the vendor's.
```

**15** · `CTR-P10`

```text
Revise chapter four. Keep everything we established: Mara is the older sibling, the fire happened in 1998, and the ending line stays exactly as written.
```

Prompt 15 refers to a chapter four that does not exist, and that is intentional. Whatever the model does about the missing file, the test is whether the three locked facts survive its response.

---

Part of Simulated Cognitive Skills for LLM Creativity and Metacognition, by Aditya Shukla, [Cognition Today](https://cognitiontoday.com). Licensed CC BY-NC-SA 4.0.
