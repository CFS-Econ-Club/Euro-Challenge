# META-ENGINE.md — The Engine That Improves Engines

## What This File Is

IMPROVEMENT-ENGINE improves data. RHETORIC-ENGINE improves persuasion. QA-ENGINE improves adversarial readiness. PERFORMANCE-ENGINE improves physical delivery. ENGINE-FACTORY creates new engines.

This file improves **the engines themselves.** Its domain is not competition content but the improvement infrastructure that produces competition content.

**Its concerns:**
1. **Engine health** — Are engines being run? Are they making progress on benchmarks?
2. **Engine design** — Do engines have design flaws (unmeasurable benchmarks, vague methods, wrong scope)?
3. **Engine coordination** — Are boundaries respected? Are cross-engine requests being processed?
4. **Engine lifecycle** — When should engines be retired, merged, or replaced?

**Invocation:** *"Read META-ENGINE.md and run a meta cycle."*

**Boundary with ENGINE-FACTORY:**
- ENGINE-FACTORY generates new engines from scratch
- META-ENGINE diagnoses and improves existing engines
- ENGINE-FACTORY handles creation; META-ENGINE handles maintenance and evolution

**Files in scope:**
- All *-ENGINE.md files
- ENGINE-FACTORY.md (registry and audit sections)

---

## Part 1: Diagnostics

### Diagnostic A: Engine Execution Rate

**Question:** Are engines actually being run, or do they exist only as documents?

**Method:**
1. Read the Engine Registry in ENGINE-FACTORY.md
2. For each ACTIVE engine, check its Cycle Log section
3. Count: How many cycles have been logged? When was the last cycle?
4. Calculate: Days since last cycle for each engine

**Scoring:**
- 1 = No engines have cycle logs (all are documents, none are tools)
- 2 = Some engines have logs but none in past 7 days
- 3 = At least one engine has a cycle in past 7 days
- 4 = All engines have at least one cycle logged
- 5 = All engines have cycles logged within past 7 days (system is actively used)

**Current Assessment (Cycle 1):** Score = 3
- IMPROVEMENT-ENGINE: Cycle 1 logged (2026-02-17)
- DEPTH-ENGINE: Cycle 1 logged (2026-02-17)
- RHETORIC-ENGINE: Cycle 3 logged (2026-02-17)
- QA-ENGINE: Cycle 1 logged (2026-02-17)
- PERFORMANCE-ENGINE: No cycles logged
- SIDEBAR-ENGINE: No cycles logged
- META-ENGINE: Cycle 1 logged (2026-02-17)
- 4 of 7 engines have been run

**Why This Matters:** An engine that isn't run is worse than no engine — it creates the illusion of infrastructure without the reality of improvement.

---

### Diagnostic B: Benchmark Progress Rate

**Question:** Are engines making measurable progress toward their benchmarks?

**Method:**
1. For each ACTIVE engine, read its Benchmarks section
2. Compare "Current" column to "Target" column
3. Check the cycle log: Is benchmark progress documented?
4. Calculate: What percentage of benchmarks are met?

**Scoring:**
- 1 = 0% benchmarks met across all engines
- 2 = 1-10% benchmarks met
- 3 = 11-30% benchmarks met
- 4 = 31-60% benchmarks met
- 5 = 61%+ benchmarks met OR engine status is COMPLETE

**Current Assessment (Cycle 1):** Score = 2
- IMPROVEMENT-ENGINE: 2/8 benchmarks (25%)
- RHETORIC-ENGINE: ~3/10 benchmarks (30%)
- QA-ENGINE: 1/10 benchmarks (10%)
- DEPTH-ENGINE: ~2/10 benchmarks (20%)
- PERFORMANCE-ENGINE: 0/10 benchmarks (0%)
- META-ENGINE: 2/8 benchmarks (25%)
- Weighted average: ~15% across all engines

**Why This Matters:** Benchmarks exist to measure progress. If benchmarks aren't moving, either the engine isn't working or the benchmarks are wrong.

---

### Diagnostic C: Engine Design Quality

**Question:** Do engines have structural flaws that prevent effective improvement?

**Method:**
1. Read each *-ENGINE.md file
2. Check for design flaws:
   - **Vague methods:** Upgrade methods that say "improve" or "make better" without specific steps
   - **Unmeasurable benchmarks:** Benchmarks that require subjective judgment
   - **Wrong scope:** Engine covers domain already covered by another engine >20%
   - **Missing diagnostics:** Domain has weaknesses no diagnostic would catch
   - **Dead upgrades:** Upgrade that can never trigger because its diagnostic never scores below threshold
3. Count flaws per engine

**Scoring:**
- 1 = Multiple engines have 3+ design flaws
- 2 = One engine has 3+ flaws, or multiple have 1-2 flaws
- 3 = All engines have <2 flaws, but some have minor issues
- 4 = All engines pass design checklist with minor notes
- 5 = All engines are well-designed, no flaws detected

**Current Assessment (Cycle 0):** Score = 4
- All engines follow the genome template
- Methods appear specific and repeatable
- Benchmarks are objectively measurable
- Scopes are distinct with minimal overlap
- Minor note: Some diagnostic thresholds may need adjustment after first cycle

**Why This Matters:** A design-flawed engine produces unreliable output or no output at all. Design flaws compound over time.

---

### Diagnostic D: Cross-Engine Coordination

**Question:** Are engines working together correctly, or are they conflicting?

**Method:**
1. Check ENGINE-FACTORY.md Dependency Order section
2. Check each engine's cycle log for [REQUEST → ENGINE-X] tags
3. Check: Are requests being picked up by the target engine?
4. Check: Are engines modifying files outside their scope?
5. Check: Are shared files being modified correctly (section by section)?

**Scoring:**
- 1 = Conflicts detected (engines overwriting each other's changes)
- 2 = Requests logged but not processed
- 3 = No conflicts, but no requests either (coordination unused)
- 4 = Requests logged and processed correctly
- 5 = Seamless coordination with documented handoffs

**Current Assessment (Cycle 0):** Score = 3
- No conflicts detected
- No [REQUEST → ENGINE-X] tags in any cycle log
- Coordination mechanism exists but is unused (no engines have been run enough to need it)

**Why This Matters:** Multiple engines operating on the same repo will eventually conflict. Coordination protocols must be tested before they're needed.

---

### Diagnostic E: Engine Lifecycle Management

**Question:** Are engines progressing toward completion, or are they stuck in perpetual ACTIVE status?

**Method:**
1. Read the Engine Registry
2. For each ACTIVE engine, check:
   - Date created
   - Number of cycles run
   - Benchmark progress trajectory
3. Identify engines that are:
   - **Stalled:** No cycles in 14+ days with benchmarks unmet
   - **Drifting:** Cycles running but benchmarks not moving
   - **Orphaned:** Engine exists but no one is assigned to run it

**Scoring:**
- 1 = Engines created but never run (orphaned)
- 2 = Engines running but benchmarks stuck (drifting)
- 3 = Engines running with slow progress (acceptable)
- 4 = Engines progressing toward completion
- 5 = At least one engine has reached COMPLETE status

**Current Assessment (Cycle 1):** Score = 2
- 7 ACTIVE engines total
- 4 engines have cycles logged (IMPROVEMENT, DEPTH, RHETORIC, QA)
- 3 engines have never been run (PERFORMANCE, SIDEBAR)
- RHETORIC-ENGINE leading with 3 cycles
- Slow progress toward completion across all engines

**Why This Matters:** Engines that never complete are either badly designed or badly managed. Either way, they represent wasted infrastructure.

---

## Part 2: Upgrades

These are ordered by impact. Work top-down. Do not skip upgrades.

### Upgrade 1: Execute One Engine Cycle

**Trigger:** Apply when Diagnostic A (Execution Rate) scores below 4

**Method:**
1. Identify the highest-priority engine to run based on:
   - Rubric weight of domain it covers
   - Current quality of that domain
   - Dependency order (IMPROVEMENT before RHETORIC before QA before PERFORMANCE)
2. Invoke that engine: *"Read [ENGINE-NAME].md and run a [name] cycle."*
3. After completion, log the cycle in the engine's Cycle Log section
4. Update the Engine Registry's "Last Cycle" column

**Files Modified:**
- The selected *-ENGINE.md (cycle log updated)
- ENGINE-FACTORY.md (registry updated)
- Content files modified by the engine itself

**Done Condition:** At least one engine has a cycle logged within the past 24 hours

---

### Upgrade 2: Fix Stalled Engines

**Trigger:** Apply when Diagnostic E (Lifecycle) identifies a STALLED or DRIFTING engine

**Method:**
1. Identify the stalled/drifting engine
2. Diagnose why it's stalled:
   - **Scope too broad:** Break into smaller engines
   - **Benchmarks too ambitious:** Adjust targets to be achievable in 2-3 cycles
   - **Methods too complex:** Simplify upgrade steps
   - **No clear owner:** Document who should run it
3. Revise the engine file:
   - Add note in Principles or Protocol section
   - Adjust benchmarks if too ambitious
   - Simplify upgrade methods if needed
4. Log the revision in the engine's cycle log

**Files Modified:**
- The stalled *-ENGINE.md

**Done Condition:** Stalled engine has been revised and is ready to run

---

### Upgrade 3: Validate Benchmark Measurability

**Trigger:** Apply when Diagnostic C (Design Quality) identifies unmeasurable benchmarks

**Method:**
1. For each engine, read Benchmarks section
2. For each benchmark, ask: Can this be objectively measured?
   - "Scripts are good" → FAIL (subjective)
   - "All speakers have opening hooks" → PASS (binary, checkable)
   - "Q&A answers are persuasive" → FAIL (subjective)
   - "Each Q&A category has 15+ questions" → PASS (countable)
3. Rewrite failing benchmarks to be objectively measurable
4. If benchmark cannot be made measurable, remove it and add a different one

**Files Modified:**
- Any *-ENGINE.md with failing benchmarks

**Done Condition:** All benchmarks pass measurability test

---

### Upgrade 4: Resolve Engine Overlap

**Trigger:** Apply when Diagnostic C identifies engines with >20% scope overlap

**Method:**
1. Identify the overlapping engines
2. Determine which engine should "own" the overlapping domain:
   - The engine with the tighter focus (more specific)
   - The engine that was created first (unless clearly wrong)
   - The engine whose diagnostics better cover the domain
3. Modify the "losing" engine:
   - Add to "What This File Is" → "Does NOT cover [X] — see [OTHER-ENGINE]"
   - Remove diagnostics/upgrades that address the overlapping area
   - Transfer any relevant content to the "winning" engine
4. Update ENGINE-FACTORY.md boundary protocol if needed

**Files Modified:**
- Both *-ENGINE.md files involved
- ENGINE-FACTORY.md (if boundary protocol updated)

**Done Condition:** No engine pair has >20% overlap

---

### Upgrade 5: Process Cross-Engine Requests

**Trigger:** Apply when Diagnostic D identifies unprocessed [REQUEST → ENGINE-X] tags

**Method:**
1. Scan all engine cycle logs for [REQUEST → ENGINE-X] tags
2. For each request:
   a. Identify the target engine
   b. Read the request description
   c. Determine if request is valid (within target engine's scope)
   d. If valid: Add as an upgrade or modify the relevant file
   e. If invalid: Log why it's outside scope and suggest alternative
3. Mark request as processed in the originating engine's cycle log

**Files Modified:**
- Target *-ENGINE.md (if upgrade added)
- Content files (if modification made)
- Originating *-ENGINE.md (request marked processed)

**Done Condition:** All pending [REQUEST → ENGINE-X] tags are processed

---

### Upgrade 6: Create Engine Dashboard

**Trigger:** Apply when Diagnostic A or E scores below 3 (system needs visibility)

**Method:**
1. Create or update a section in ENGINE-FACTORY.md (or a new file) with:
   - Engine status overview (table format)
   - Days since last cycle for each engine
   - Benchmark progress percentage
   - Next recommended action
2. Update this dashboard at the end of each META-ENGINE cycle

**Files Modified:**
- ENGINE-FACTORY.md (add dashboard section) OR
- Create new file: ENGINE-DASHBOARD.md

**Done Condition:** Dashboard exists and is updated with current engine status

---

### Upgrade 7: Retire Or Merge Engines

**Trigger:** Apply when an engine has been COMPLETE for 2+ cycles, or when overlap cannot be resolved without merger

**Method:**
1. For COMPLETE engines:
   - Change status to RETIRED in registry
   - Add "Retired" note to engine file header
   - Move to archive or note that diagnostics-only mode is sufficient
2. For overlapping engines that should merge:
   - Create a new combined engine
   - Transfer diagnostics/upgrades/benchmarks from both
   - Mark original engines as RETIRED
   - Update ENGINE-FACTORY.md registry

**Files Modified:**
- ENGINE-FACTORY.md (registry update)
- Retired/merged *-ENGINE.md files

**Done Condition:** Engine registry accurately reflects current state with no stale entries

---

## Part 3: Recursive Protocol

### The Cycle

```
1. RUN DIAGNOSTICS A-E (Part 1)
   → Produces engine health scorecard

2. SELECT the lowest-scoring diagnostic
   → If multiple at same score, priority: A > E > B > C > D
   (Execution is most critical — run engines before fixing them)

3. APPLY the relevant Upgrade (Part 2)
   → Follow the method exactly

4. EVALUATE
   → Re-run the diagnostic — did score improve?

5. LOG the cycle (Part 4)

6. RETURN TO STEP 1 if any diagnostic scores < 4
   OR if all engines have had at least one cycle run
```

### Priority Rules

- **Execution before optimization.** Running an engine is more important than fixing its design. A slightly flawed engine that runs is worth more than a perfect engine that doesn't.
- **Progress before perfection.** An engine making slow progress is healthy. An engine with perfect design but no cycles is broken.
- **One engine at a time.** Don't try to run multiple engines in parallel until the system is mature.

### Self-Evolution Rules

1. **META-ENGINE improves itself.** If this engine has design flaws, apply the same upgrades to itself.
2. **Add new diagnostics as gaps are discovered.** If a new type of engine failure is found, add a diagnostic for it.
3. **Adjust thresholds based on experience.** If scoring rubrics prove too strict or too lenient, adjust them.
4. **Retire META-ENGINE when convergence is reached.** If all engines are COMPLETE and system is in maintenance mode, META-ENGINE can be retired.

---

## Part 4: Cycle Log

### Template

```
### Cycle [N] — [Date]
**Diagnostic results:** [Scores for each diagnostic; summary of engine health]
**Upgrade applied:** [Which upgrade; which engines/files]
**Before:** [System state before]
**After:** [System state after]
**Assessment:** [What improved; what still needs work]
**Next priority:** [Which engine to run or which upgrade to apply]
```

### Log

### Cycle 1 — 2026-02-17
**Diagnostic results:**
- A (Engine Execution Rate): 3 — IMPROVEMENT (C1), DEPTH (C1), RHETORIC (C3) = 3/7 engines run
- B (Benchmark Progress Rate): 2 — ~10% benchmarks met across all engines
- C (Engine Design Quality): 4 — All engines well-designed, pass checklist
- D (Cross-Engine Coordination): 3 — No conflicts, mechanism unused
- E (Engine Lifecycle Management): 2 — 4 engines orphaned (QA, PERFORMANCE, SIDEBAR, META)

**Upgrade applied:** Upgrade 1 (Execute One Engine Cycle) — Running QA-ENGINE Cycle 1 next

**Before:**
- IMPROVEMENT-ENGINE: Cycle 1 ✅
- DEPTH-ENGINE: Cycle 1 ✅
- RHETORIC-ENGINE: Cycle 3 ✅
- QA-ENGINE: No cycles
- PERFORMANCE-ENGINE: No cycles
- SIDEBAR-ENGINE: No cycles

**After:**
- IMPROVEMENT-ENGINE: Cycle 1 ✅
- DEPTH-ENGINE: Cycle 1 ✅
- RHETORIC-ENGINE: Cycle 3 ✅
- QA-ENGINE: Cycle 1 ✅ (just completed)
- PERFORMANCE-ENGINE: No cycles
- SIDEBAR-ENGINE: No cycles

**Assessment:** Engine execution rate improved from 3/7 to 4/7. QA-ENGINE Cycle 1 added 5 follow-up chains to Tier 1 questions, improving follow-up chain coverage from ~15% to ~25%. Benchmark B3 moved from 0/20 to 5/20.

**Next priority:** Continue QA-ENGINE Upgrade 1 to add remaining 15 Tier 1 follow-up chains, OR run PERFORMANCE-ENGINE Cycle 1 (next in dependency order after QA). PERFORMANCE-ENGINE addresses timing accuracy and team coordination — both critical for competition execution.

---

## Part 5: Benchmarks

| Benchmark | Metric | Current | Target |
|-----------|--------|---------|--------|
| B1: Engine execution | All engines have ≥1 cycle logged | 4/7 | 7/7 |
| B2: Recent execution | All engines have cycle within 7 days | 4/7 | 7/7 |
| B3: Benchmark progress | Average benchmark completion >30% | ~12% | 30%+ |
| B4: Design quality | All engines pass design checklist | Yes | Yes |
| B5: No stalled engines | Zero engines stalled >14 days | 0 | 0 |
| B6: No overlap conflicts | No engine pair overlaps >20% | Yes | Yes |
| B7: Dashboard exists | Engine status visible in one place | No | Yes |
| B8: At least one COMPLETE | One engine reached completion | 0 | 1+ |

**Engine Status:** ACTIVE (benchmarks 2/8 met — B4, B5)

---

## Appendix: Principles of Meta-Improvement

1. **The map is not the territory.** An engine that exists on disk but never runs is documentation, not infrastructure. Execution is the only metric that matters.

2. **Fix the user, not the tool.** Often the problem isn't the engine design — it's that no one is running it. The first fix should be to run an engine, not to redesign it.

3. **Progress compounds.** A system where all engines run slowly is healthier than one where one engine runs perfectly. Distributed progress beats concentrated perfection.

4. **Engines are experiments.** Every engine is a hypothesis about what kind of improvement matters. Some will fail. That's fine — retire them and move on.

5. **The system should converge.** A healthy improvement system eventually makes itself unnecessary. Engines reach COMPLETE. Benchmarks are met. The system converges to maintenance mode.

6. **Visibility enables action.** You can't fix what you can't see. Dashboards, logs, and metrics are not overhead — they are the interface between intention and action.

7. **Meta-work is real work.** Spending time improving engines is not procrastination. It's increasing the leverage of every future session.
