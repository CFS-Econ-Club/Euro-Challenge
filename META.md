# META.md — Self-Improving Cognitive Architecture

## What This File Is

This is not a task list. It is a **reasoning system** that any Claude Code instance can load to generate its own improvement tasks, evaluate its own work, and evolve the framework itself over time.

**Invocation:** *"Read META.md and run an improvement cycle on this repository."*

The system works at any stage — whether the repo is a skeleton, nearly finished, or being adapted for a different year/topic. It never "runs out" of things to do because it generates tasks from principles, not from a predefined list.

---

## Part 1: The Protocol

### 1.1 Boot Sequence

Every new Claude Code instance starts here:

```
1. Read this file (META.md) in its entirety
2. Read Part 5 (Active Hypotheses) — this is your starting orientation
3. Read the last 3 entries in Part 4 (Institutional Memory) — this is recent context
4. Run the Diagnostic Probes in Part 2 to assess current state
5. Enter the Operating Loop (§1.2)
```

### 1.2 Operating Loop

```
OBSERVE  →  What is the current state? (use lenses + probes from Part 2)
    ↓
ORIENT   →  What maturity stage is the repo in? (see §1.3)
    ↓         What do the active hypotheses say? (Part 5)
    ↓         What has been tried before? (Part 4)
    ↓
HYPOTHESIZE → What single change would most improve competition performance?
    ↓           (Write this hypothesis down BEFORE acting)
    ↓
ACT      →  Execute the improvement using reasoning patterns from Part 3
    ↓
EVALUATE →  Did the change achieve what you hypothesized?
    ↓         What surprised you?
    ↓         Did you discover a new weakness or a new principle?
    ↓
ADAPT    →  Update this file:
    ↓         - Revise Active Hypotheses (Part 5)
    ↓         - Append to Institutional Memory (Part 4)
    ↓         - Add/prune/revise Lenses or Patterns (Parts 2-3) if warranted
    ↓
(repeat until session ends)
```

Every cycle, the instance must modify this file. If you finish a session and META.md is unchanged, the system failed to learn.

### 1.3 Maturity Model

The system must assess which stage the repository is in. This determines what kind of work is most valuable. Don't do Stage 3 work on a Stage 1 repo.

| Stage | Name | Signature | Focus |
|-------|------|-----------|-------|
| 1 | **Foundation** | Missing files, empty sections, placeholder text, many `[VERIFY]` tags, no citations | Fill gaps, verify facts, build coverage |
| 2 | **Structure** | Most files exist and have content, but arguments are encyclopedic, not strategic; data exists but isn't woven into narrative | Strengthen arguments, add causal reasoning, connect files to each other |
| 3 | **Persuasion** | Arguments are sound, data is verified, but the presentation reads like a report, not a performance; Q&A answers are correct but not memorable | Sharpen rhetoric, add hooks and soundbites, tune for audience impact |
| 4 | **Resilience** | Narrative is strong and polished, but hasn't been stress-tested; counterarguments are shallow; no competitive analysis | Adversarial review, red-teaming, consistency audits, edge-case Q&A |
| 5 | **Mastery** | All previous layers are solid; marginal improvements are small | Creative differentiation, surprise depth, strategic framing to steer judge questions, meta-competitive positioning |

**How to assess stage:** Run diagnostic probes (§2.2). If >30% of probes for a stage fail, the repo is at or below that stage.

### 1.4 Self-Modification Rules

This file is designed to evolve. But evolution must be disciplined.

**When to ADD to this file:**
- You discovered a quality dimension (lens) that isn't captured in Part 2
- You developed a reasoning approach that worked well and is generalizable (new pattern for Part 3)
- You have a new hypothesis about what matters most (update Part 5)

**When to REMOVE from this file:**
- A lens has been tagged "unused" for 3+ consecutive cycles → remove it
- A reasoning pattern has been tried twice and produced no useful output → remove it
- An active hypothesis has been refuted by evidence → archive it to Part 4, remove from Part 5

**When to RESTRUCTURE this file:**
- Part 4 (Memory) exceeds 50 entries → summarize oldest entries into a "lessons learned" digest, delete the raw entries
- Any section of this file exceeds 100 lines → it's too detailed; compress to principles

**Invariant sections (never modify):**
- §1.1 (Boot Sequence)
- §1.2 (Operating Loop)
- §1.4 (Self-Modification Rules) — *except* by adding new rules, never removing existing ones

---

## Part 2: Quality Lenses

A lens is a **perspective from which to evaluate content**. Each lens asks a question, provides diagnostic probes to test it, and can be applied to any file.

Lenses are not a checklist. They are ways of seeing. Apply the ones that are most relevant to the current maturity stage and the file you're examining.

### How to use lenses

1. Pick 2-4 lenses most relevant to the current work
2. For each file you examine, ask the lens's core question
3. Run the diagnostic probes — they give you concrete, greppable signals
4. The gap between "what the lens expects" and "what exists" generates your specific tasks

### Seed Lenses

These are the initial lenses. Future instances should add, refine, or prune these.

---

**Lens: Truth**
- *Core question:* Can every factual claim in this file survive a hostile fact-check?
- *Probes:*
  - `Grep for "[VERIFY]", "approximately", "about", "roughly", "~"` — vagueness signals
  - For each quantitative claim: Is a specific source, date, and methodology cited?
  - Flip test: Search the web for the same statistic. Does our number match?
- *Stage relevance:* Stage 1-2 (critical), Stage 3+ (maintenance)
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Argument Resilience**
- *Core question:* If a skeptic read this file, what's the first thing they'd attack — and do we have a defense?
- *Probes:*
  - For each causal claim ("X leads to Y"): Is the mechanism explicit? Are confounders acknowledged?
  - For each policy claim: Are at least 3 counterarguments addressed?
  - Steel-man test: Can you construct a stronger version of the opposing view than what's in the file?
- *Stage relevance:* Stage 2-4 (critical)
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Narrative Momentum**
- *Core question:* If you read this file (or sequence of files) aloud, does the audience want to hear what comes next?
- *Probes:*
  - Does the first sentence create curiosity or state a boring fact?
  - Is there a clear "so what?" within the first paragraph?
  - Does each section end by setting up the next (not just stopping)?
  - Is there a single throughline you could state in one sentence?
- *Stage relevance:* Stage 3-5 (critical)
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Strategic Alignment**
- *Core question:* Does this content directly help us score points on the rubric?
- *Probes:*
  - Can you draw a direct line from this content to a specific rubric criterion and point value?
  - Is any content "interesting but not scoreable"? (candidate for cutting)
  - Does the emphasis within the file match the rubric weighting? (recommendations = 20%, so policy files should be strongest)
- *Stage relevance:* All stages
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Consistency**
- *Core question:* If you extracted every instance of a given fact from every file, would they all match?
- *Probes:*
  - Pick 5 key statistics (e.g., "€10 billion grid fund"). Grep the entire repo. Are all instances identical?
  - Do speaker scripts use the same framing as the research files they draw from?
  - Does the Q&A document's data match the policy documents' data?
- *Stage relevance:* Stage 2+ (important)
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Audience Model**
- *Core question:* Who is reading/hearing this, and does the content match their knowledge level, expectations, and decision-making criteria?
- *Probes:*
  - Judges are economists, business people, diplomats — does the language match? (Not too simplistic, not too jargony)
  - Would a judge who has seen 15 presentations today find anything surprising or fresh here?
  - Does the content answer the questions judges actually ask, or the questions we wish they'd ask?
- *Stage relevance:* Stage 3-5 (critical)
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Interconnection**
- *Core question:* Does this file exist in isolation, or does it draw from and feed into the rest of the repository?
- *Probes:*
  - Count cross-references to other files. Fewer than 3 = isolated.
  - For each claim, can you trace it to a research file, which traces to a data file, which traces to a primary source?
  - Would removing this file leave a visible gap in any other file?
- *Stage relevance:* Stage 2+ (important)
- *Added:* Cycle 0 (seed) | *Last useful:* —

**Lens: Diminishing Returns Detector**
- *Core question:* Is further improvement to this file the best use of time, or has it plateaued while other files remain weak?
- *Probes:*
  - Has this file been modified in the last 2 cycles? If yes, has the quality meaningfully changed?
  - Compare this file's quality score to the weakest file in the same rubric category. Difference > 2 = work on the weaker file instead.
  - If you deleted the least important 20% of this file, would the presentation suffer?
- *Stage relevance:* Stage 3+ (prevents over-polishing)
- *Added:* Cycle 0 (seed) | *Last useful:* —

---

## Part 3: Reasoning Patterns

A pattern is a **reusable cognitive strategy** for improving content. Unlike a task ("verify the GDP number"), a pattern is a way of thinking that generates tasks.

### How to use patterns

1. Based on your current maturity stage and the lens results, select 1-3 patterns
2. Apply the pattern to the highest-priority file(s)
3. The pattern will generate specific actions — execute them
4. After the session, note in Part 4 which patterns you used and whether they produced useful output

### Seed Patterns

---

**Pattern: Evidence Chain Tracing**
- *When to use:* Any file makes claims that need support
- *Method:*
  ```
  For each key claim in the file:
    1. What is the claim?
    2. What evidence supports it? (in this file or another)
    3. Where does that evidence come from? (primary source)
    4. Is the primary source accessible, current, and authoritative?
    5. If any link in the chain is broken → fix it or flag the claim as unsupported
  ```
- *Generates:* Verification tasks, citation improvements, claim removals
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: Perspective Rotation**
- *When to use:* A file feels "done" but you suspect it could be stronger
- *Method:*
  ```
  Read the file 4 times, each time as a different person:
    1. A skeptical economist judge who has heard 14 bad presentations today
    2. A competing team looking for weaknesses to exploit
    3. A team member who has to speak these words aloud under pressure
    4. A domain expert (Dutch climate policy researcher) who finds this surface-level
  After each read, note the strongest criticism that person would make.
  ```
- *Generates:* Specific weaknesses you wouldn't see from your default perspective
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: The Inversion**
- *When to use:* You're trying to improve something but aren't sure what "better" looks like
- *Method:*
  ```
  Instead of asking "how do I make this better?", ask:
    1. "What would make this WORSE?" (list 5 things)
    2. "Are any of those bad things currently present?" (often yes)
    3. "What is the OPPOSITE of each bad thing?" (this is your improvement direction)
  ```
- *Generates:* Non-obvious improvements by inverting failure modes
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: Compression Test**
- *When to use:* A file is long and you're not sure every part earns its place
- *Method:*
  ```
  1. Summarize the file in exactly 3 sentences
  2. For each section of the original file, ask: does this support one of my 3 sentences?
  3. If a section doesn't support any of the 3: it's either the wrong 3 sentences, or the section is padding
  4. Kill the padding. If the 3 sentences are wrong, rewrite them (this means you don't understand the file's purpose, which is itself a problem)
  ```
- *Generates:* Content cuts, structural clarity, purpose alignment
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: Gap Synthesis**
- *When to use:* All individual files seem adequate but the whole feels less than the sum of its parts
- *Method:*
  ```
  1. List the 10 most important claims in the entire repository
  2. For each pair of adjacent claims, ask: "Is the logical connection between these two claims explicit anywhere?"
  3. Missing connections = structural gaps
  4. Write the missing connective tissue (or add it to the relevant file)
  ```
- *Generates:* Transition text, bridging arguments, new files that synthesize across topics
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: Productive Destruction**
- *When to use:* A file has been incrementally improved multiple times but still feels mediocre — the structure itself may be wrong
- *Method:*
  ```
  1. Close the file. Ask: "If I were writing this from scratch to serve its purpose, what would I write?"
  2. Write a 10-line outline of the "from scratch" version
  3. Compare to the current file's structure
  4. If <50% overlap, the file should be rewritten, not patched
  5. Rewrite it. (Save the old version in a comment block at the bottom if you want a safety net)
  ```
- *Generates:* Complete rewrites of structurally flawed files
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: Surprise Depth**
- *When to use:* Stage 4-5, when the content is solid but undifferentiated from what any prepared team might say
- *Method:*
  ```
  1. Identify the 3 blandest sections of the presentation (the parts any team would say)
  2. For each, ask: "What does a genuine expert know about this that would surprise the judges?"
  3. Research that deeper layer (specific case studies, counterintuitive data, historical parallels, cutting-edge developments)
  4. Insert it — not as additional bulk, but as a replacement for the bland version
  ```
- *Generates:* Moments of unexpected depth that signal genuine understanding to judges
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

**Pattern: Future-Back Reasoning**
- *When to use:* Policy recommendations feel generic or insufficiently grounded
- *Method:*
  ```
  1. Start from the desired outcome (e.g., "grid congestion eliminated by 2031")
  2. Work backwards: What must be true in 2030? 2029? 2028? 2027?
  3. For each step: What specific action makes this happen? Who does it? What's the cost? What could go wrong?
  4. Compare this backward chain to what's currently in the policy file
  5. Fill any gaps in the chain
  ```
- *Generates:* More granular and credible implementation timelines
- *Added:* Cycle 0 (seed) | *Times used:* 0 | *Success rate:* —

---

## Part 4: Institutional Memory

This is the system's learning log. Every cycle appends an entry. This is how the system becomes smarter over time — future instances read this to understand what has been tried, what worked, and what the current state of understanding is.

### Entry Format

```
### Cycle [N] — [Date]
**Maturity assessment:** Stage [X]
**Lenses applied:** [list]
**Patterns used:** [list]
**Hypothesis:** "[What I believed would be the highest-impact improvement before starting]"
**Actions taken:** [What was actually done, briefly]
**Outcome:** [Did the hypothesis prove correct? What quality changed?]
**Surprises:** [What did I discover that I didn't expect?]
**Framework changes made:**
  - [Any additions/removals/revisions to Parts 2, 3, or 5 of this file]
**Recommendation to next instance:** [Plain-language advice]
```

### Log

### Cycle 1 — 2026-02-17
**Maturity assessment:** Stage 2-3 (Structure → Persuasion transition)
**Lenses applied:** Truth, Consistency, Strategic Alignment
**Patterns used:** Evidence Chain Tracing
**Hypothesis:** "Propagating the 4 flagged data corrections from verification tracker to all affected files would be the highest-impact improvement because inconsistent data directly undermines credibility."
**Actions taken:**
- Corrected Dutch carbon tax from €125-150/t to €78.67-87.90/t across 4 files (counterarguments-and-rebuttals.md, externalities-explainer.md, QUICK_REFERENCE.md, dutch-carbon-tax.md)
- Corrected grid wait time from "3-5 years" to "7-10 years" across 3 files (speaker-3-script.md, international-comparisons.md, netherlands-emissions-data.md)
- Corrected "75%+ renewable projects blocked" to "14,000+ projects (9 GW)" across 4 files (overview.md, speaker-3-script.md, speaker-4-script.md, brochure-content.md)
- Updated QUICK_REFERENCE.md and brochure-content.md with corrected macro data (ECB rate 2.00%, unemployment 6.2%/4.0%, GDP figures)
- Updated verification-tracker.md to reflect completed corrections
**Outcome:** Hypothesis confirmed. 11 files corrected with consistent data. Remaining: 54 [VERIFY] tags still present across 18 files for future cycles.
**Surprises:**
- The Q&A master document already had correct carbon tax data (€78.67-87.90/t) while other files didn't — indicates partial prior corrections
- The policy-1-grid-modernization.md was already updated with correct grid data (14,044 requests, 8-12 years), showing the corrections were done in research files but not propagated to presentation materials
- External linter updated speaker-3-script.md with more accurate emissions data (143 Mton, 37% reduction vs 1990) during this cycle — suggests ongoing external verification
**Framework changes made:**
- None to lenses or patterns (first cycle, seed framework adequate)
**Recommendation to next instance:**
- Focus on resolving remaining [VERIFY] tags (54 across 18 files) — most are in EU policy framework files
- Check if the emissions profile data (143 Mton vs 165 Mton discrepancy) needs propagation to other files
- Consider adding "Follow-up Chain" lens to Q&A preparation — H4 notes Q&A is wide but not deep

### Cycle 2 — 2026-02-17
**Maturity assessment:** Stage 2-3 (Structure → Persuasion transition)
**Lenses applied:** Truth, Consistency
**Patterns used:** Evidence Chain Tracing (with Jina MCP web verification)
**Hypothesis:** "Propagating the updated emissions data (143 Mton, 37% reduction) and resolving key [VERIFY] tags in EU policy files using web search would further strengthen data consistency."
**Actions taken:**
- Propagated emissions data (143 Mton, 37% reduction vs 1990) to QUICK_REFERENCE.md, netherlands-emissions-data.md, transition-sentences.md
- Used Jina MCP to verify EU policy data:
  - Netherlands RRF allocation: €5.4B total (€4.7B RRF + €734M REPowerEU) - updated nextgeneu-and-rrf.md
  - Netherlands JTF allocation: €623M (not €175M!) - updated just-transition-fund.md
  - Netherlands CAP allocation: €4.5-4.8B for 2023-27 (~€900M annually) - updated cap-reform.md
  - EU green bond market: €442B new issuance 2024, €2.22T total market - already verified in eu-taxonomy-green-bonds.md
**Outcome:** Hypothesis confirmed. Major finding: Netherlands JTF allocation was significantly understated (€175M → €623M), a 3.6x correction. This affects Policy 3 financing assumptions and should be propagated.
**Surprises:**
- JTF allocation was €623M, not €175M — a major discrepancy that affects policy financing calculations
- RRF green spending is 54.9% in Netherlands, not 38% — one of the most ambitious in EU
- The EU policy files had more [VERIFY] tags than core research files, indicating earlier verification focused on main documents
**Framework changes made:**
- None (pattern and lens set adequate)
**Recommendation to next instance:**
- Update financing-plan.md to reflect corrected JTF allocation (€623M available, not €175M)
- Update Policy 3 (green-skills.md) to reflect larger JTF resource base
- Continue resolving remaining [VERIFY] tags in EU policy files
- Consider timing test for speaker scripts (H5 still active)

---

### Cycle 3 — 2026-02-17
**Maturity assessment:** Stage 2-3 (Structure → Persuasion transition)
**Lenses applied:** Truth, Consistency, Strategic Alignment
**Patterns used:** Evidence Chain Tracing
**Hypothesis:** "Fixing the JTF funding discrepancy in policy-3-green-skills.md (€175M/€200M → €623M) would be the highest-impact improvement because inconsistent data undermines credibility during Q&A."
**Actions taken:**
- Fixed JTF funding in policy-3-green-skills.md:
  - Line 152: Changed financing table from €200M to €623M
  - Line 215: Changed "€175M for Dutch workforce transition" to "€623M"
- Verified remaining [VERIFY] tags: ~9 tags remain, mostly in research files (cbam.md, european-green-deal.md, fit-for-55.md, climate-act-and-agreement.md)
- Verified EU ETS carbon price: Current ~€72/tonne (within stated €60-75 range) - confirmed via web search
**Outcome:** Hypothesis confirmed. JTF funding discrepancy fixed. Data now consistent between financing-plan.md (€623M) and policy-3-green-skills.md (€623M).
**Surprises:**
- Anchor-questions.md is very comprehensive (20 questions with correct answers, common wrong answers, connections to topic) — H4 is actually adequately addressed
- Remaining [VERIFY] tags are primarily in research files, not in presentation-critical materials
**Framework changes made:**
- None
**Recommendation to next instance:**
- Address remaining ~9 [VERIFY] tags in EU policy research files (optional — they're not in presentation-critical files)
- H5 (speaker timing) still needs validation — scripts have time allocations but haven't been tested
- H6 (euro angle) could be strengthened in presentation materials

### Cycle 4 — 2026-02-19
**Maturity assessment:** Stage 3-4 (Persuasion → Resilience transition)
**Lenses applied:** Argument Resilience, Audience Model
**Patterns used:** Perspective Rotation, Future-Back Reasoning
**Hypothesis:** "Q&A performance is the biggest risk (20% of score). Creating adversarial depth via follow-up chains, nightmare questions, and coordinated team handoffs will instantly increase resilience against persistent judging."
**Actions taken:**
- Executed full QA-ENGINE.md cycle, hitting all Stage 1 benchmarks:
  - Created 6-level Q&A Master Document with 15 complete Follow-Up Chains.
  - Drafted top 10 Nightmare Questions reflecting actual weaknesses in our policy.
  - Revised all counterarguments into a Concession/Pivot/Defense format and scored them by Priority (1-25).
  - Doubled the `anchor-questions.md` bank from 20 to 40, injecting required Macro & EU concepts.
  - Authored a `team-qa-protocol.md` establishing Primary/Backup mechanics and the "I Don't Know" doctrine.
**Outcome:** Hypothesis confirmed. The team now has structural defense in depth. If a judge pursues a single line of questioning 3+ times, the backup speaker knows exactly how to respond without generating contradictory arguments.
**Surprises:**
- When drafting the Nightmare Questions, discovering that our true weakness is the *sequencing risk* (training workers before permits are approved) forced us to develop a much better defense (focusing on intermediate tech like batteries while waiting for main transmission lines). Advancing QA forced policy refinement.
**Framework changes made:**
- QA-ENGINE.md benchmarks updated (6/10 completed).
- Resolved H4 (Q&A prep) from Active to Superseded.
**Recommendation to next instance:**
- Practice logs (Upgrade 7 in QA-ENGINE) must be generated.
- Move towards PERFORMANCE-ENGINE.md to begin timing speaker scripts and testing the handoffs established in Q&A prep.
- H5 (speaker timing) and H6 (euro angle) remain unaddressed.

---

## Part 5: Active Hypotheses

These are the system's current best beliefs about what matters most. They are **mutable** — every cycle should confirm, refute, or refine them. They give a new instance immediate orientation without having to audit everything from scratch.

### Active Hypotheses (post-Cycle 4)

> **H1:** ~~The single highest-impact improvement is completing data verification (16 statistics still unverified) because unverified data undermines every layer built on top of it.~~ **SUPERSEDED** — Cycles 1-2 corrected major data issues. Emissions data propagated (143 Mton), EU policy data verified (RRF €5.4B, JTF €623M, CAP €4.5-4.8B). Remaining: ~40 [VERIFY] tags in EU policy files.

> **H2:** The reference library (10-reference-library/) being nearly empty means the team has no deep-reading material, which limits the depth of Q&A responses and "genuine understanding" signals to judges. **ACTIVE** — 8 documents now exist, but tier-2 and tier-3 could be expanded.

> **H3:** ~~The repository's biggest structural weakness is the absence of an explicit narrative arc — files are informational but not persuasive, and there is no document that states the story the team is trying to tell.~~ **REFUTED** — overview.md contains explicit "Narrative Arc" section. Narrative exists; may need refinement but not creation.

> **H4:** ~~Q&A preparation is wide (74 questions) but not deep — no follow-up chains, no anchor question prep, no adversarial stress-testing. Given Q&A is 20% of the score, this is underprepared relative to its point value.~~ **SUPERSEDED** — Cycle 4 resolved this through a full QA-ENGINE implementation, creating 15 follow-up chains, 40 anchor questions, and 10 prioritized adversarial nightmare questions. Remaining Q&A work is now pure practice.

> **H5:** Speaker scripts have not been pressure-tested against their time allocations. If they're over/under, the presentation scores suffer. **ACTIVE** — Still unaddressed.

> **H6:** The "single currency angle" — how euro membership specifically shapes Dutch climate policy — is the most likely area where judges will probe for genuine understanding vs. surface knowledge, and the current treatment is adequate but not compelling. **ACTIVE** — Present in policy files but could be strengthened in presentation materials.

> **H7:** The financing-plan.md and policy-3-green-skills.md understate available EU funding because JTF allocation was corrected from €175M to €623M — this affects policy feasibility calculations. **CONFIRMED** — Cycle 3 propagated €623M to both files. Data is now consistent.

### Hypothesis Status Key
- **ACTIVE** — Not yet tested or partially supported
- **CONFIRMED** — Evidence supports this; act on it
- **REFUTED** — Evidence contradicts this; stop acting on it
- **SUPERSEDED** — Replaced by a more precise hypothesis

All seed hypotheses are **ACTIVE** as of initial creation.

---

## Appendix: Principles for Self-Modification

These govern how the framework evolves. They are intentionally hard to change (see §1.4).

1. **The framework must remain usable in a single session.** If META.md exceeds ~500 lines, compress it. A framework nobody reads is worthless.

2. **Prefer principles over procedures.** A principle ("every claim must survive adversarial scrutiny") is infinitely reusable. A procedure ("verify the GDP number in file X") is single-use. Always try to extract the principle from the procedure.

3. **Learning requires surprise.** If a cycle produces no surprises, the instance either didn't look hard enough or the framework's lenses are too narrow. Add a new lens.

4. **Diminishing returns are real.** Track which lenses and patterns produce useful output. Prune the ones that don't. The system should get leaner and sharper, not fatter and vaguer.

5. **The goal is competition performance, not document perfection.** Every improvement should be traceable to a plausible increase in judge scores. "This makes the file more complete" is not sufficient justification. "This gives Speaker 3 a stronger defense against the obvious counterargument, which directly affects Q&A scoring" is.

6. **New instances are not bound by old instances' decisions.** The memory log is advisory, not authoritative. If a previous instance's approach seems wrong, say so in your log entry and change course.

7. **The framework should be transferable.** If this repository were forked for a different team, topic, or competition, the framework (Parts 1-3) should still work. Only Parts 4-5 are specific to the current project.
