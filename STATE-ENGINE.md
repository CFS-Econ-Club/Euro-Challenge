# STATE-ENGINE.md — Repository State Auditor & Action Router

## What This File Is

This engine serves as the **central connector** between META.md's reasoning system, ENGINE-FACTORY.md's infrastructure, and the actual repository content. It audits the current state of the entire improvement ecosystem and routes to the appropriate next action.

**Invocation:** *"Read STATE-ENGINE.md and run a state audit."*

**Scope:**
- **IN SCOPE:** All `*-ENGINE.md` files, `META.md`, `ENGINE-FACTORY.md`, key content files for assessment
- **OUT OF SCOPE:** Does not modify content files directly (that's for other engines)
- **FUNCTION:** Diagnose → Prioritize → Route → Log

**Why this engine exists:**
- META.md decides *what matters* but doesn't track engine execution
- ENGINE-FACTORY.md *creates* engines but doesn't monitor their usage
- Individual engines improve *content* but don't coordinate with each other
- STATE-ENGINE.md fills the gap: it asks "what's the actual state?" and "what should run next?"

---

## Part 1: Diagnostics

### Diagnostic A: Engine Execution Rate
**Question:** Are the engines being run, or is infrastructure sitting idle?

**Method:**
1. Read ENGINE-FACTORY.md Part 5 (Engine Registry)
2. For each engine, check:
   - Last Cycle column: has it ever been run?
   - Benchmarks Met column: is progress being made?
3. Score:
   - 5 = All ACTIVE engines have been run in last 2 weeks with progress
   - 4 = Most engines (4+) have been run, some progress
   - 3 = Some engines (2-3) have been run, mixed progress
   - 2 = Only 1 engine has been run, or no progress shown
   - 1 = No engines have been run despite infrastructure existing

**Current Assessment:** → [To be filled on first run]

**Why This Matters:** An engine that exists but isn't run is waste. The factory has generated 7+ engines—if they're not executing, the system is stalled.

---

### Diagnostic B: Benchmark Progress Velocity
**Question:** Are benchmarks moving toward completion, or is improvement stalled?

**Method:**
1. For each engine in registry, extract: Benchmarks Met / Total Benchmarks
2. Calculate aggregate completion rate across all engines
3. Compare to previous audit (if exists) — is rate increasing?
4. Score:
   - 5 = >75% benchmarks met across all engines
   - 4 = 50-75% benchmarks met
   - 3 = 25-50% benchmarks met
   - 2 = 10-25% benchmarks met
   - 1 = <10% benchmarks met

**Current Assessment:** → [To be filled on first run]

**Why This Matters:** Benchmarks are the only objective measure of improvement. If they're not moving, the engines aren't working.

---

### Diagnostic C: Repository Maturity Stage
**Question:** What stage is the repository actually in (Stage 1-5 per META.md)?

**Method:**
1. Run META.md diagnostic probes (Part 2):
   - Truth lens: Count remaining `[VERIFY]` tags
   - Consistency lens: Check 5 key statistics across files
   - Strategic Alignment: Check if emphasis matches rubric weights
2. Apply Maturity Model criteria (META.md §1.3):
   - Stage 1 (Foundation): Many empty sections, placeholders, unverified data
   - Stage 2 (Structure): Files exist but arguments are encyclopedic
   - Stage 3 (Persuasion): Arguments sound but lack performance polish
   - Stage 4 (Resilience): Strong but not stress-tested
   - Stage 5 (Mastery): All solid, marginal improvements only
3. Score: 1-5 corresponding to stage

**Current Assessment:** → [To be filled on first run]

**Why This Matters:** Stage determines what work is valuable. Don't do Stage 3 work on a Stage 1 repo.

---

### Diagnostic D: Hypothesis Currency
**Question:** Are META.md's active hypotheses still valid, or have they been superseded?

**Method:**
1. Read META.md Part 5 (Active Hypotheses)
2. For each hypothesis marked ACTIVE:
   - Check if actions have been taken that affect it
   - Verify if the stated weakness still exists
3. For each hypothesis marked CONFIRMED/REFUTED/SUPERSEDED:
   - Verify status is accurate based on recent changes
4. Score:
   - 5 = All hypotheses current, accurate, and driving action
   - 4 = Mostly current, 1-2 need updating
   - 3 = Several outdated, some driving wrong actions
   - 2 = Many outdated, system confused
   - 1 = Hypotheses completely disconnected from reality

**Current Assessment:** → [To be filled on first run]

**Why This Matters:** Hypotheses orient every Claude instance. If they're wrong, work goes in wrong directions.

---

### Diagnostic E: Critical Path Alignment
**Question:** Is current work aligned with the engine dependency order and competition timeline?

**Method:**
1. Check ENGINE-FACTORY.md Part 7 (Dependency Order):
   - DEPTH → IMPROVEMENT → RHETORIC → QA → PERFORMANCE
2. Compare to recent work: are we running engines in order?
3. Check competition date: April 27, 2026 (calculate weeks remaining)
4. Apply stage-appropriate timing:
   - Stage 1 (Foundation): Should be complete by ~10 weeks out
   - Stage 2 (Structure): Should be complete by ~6 weeks out
   - Stage 3 (Persuasion): Should be complete by ~4 weeks out
   - Stage 4 (Resilience): Should be complete by ~2 weeks out
   - Stage 5 (Mastery): Final 2 weeks only
5. Score:
   - 5 = Perfect alignment, on track
   - 4 = Slight misalignment but manageable
   - 3 = Running behind, need acceleration
   - 2 = Critical path broken, wrong engines running
   - 1 = Misaligned with timeline, risk of failure

**Current Assessment:** → [To be filled on first run]

**Why This Matters:** You can't rehearse weak content. Running PERFORMANCE-ENGINE on Stage 2 content is premature; running DEPTH at Stage 4 is too late.

---

## Part 2: Upgrades

### Upgrade 1: Run Highest-Priority Engine
**Trigger:** Any diagnostic scores below 3, OR competition timeline demands it

**Method:**
1. Review diagnostic scores (A-E)
2. Calculate priority score per engine:
   - DEPTH-ENGINE: Priority if Diagnostic C (Content Maturity) ≤ 2
   - IMPROVEMENT-ENGINE: Priority if Diagnostic C ≤ 3 AND `[VERIFY]` tags exist
   - RHETORIC-ENGINE: Priority if Diagnostic C ≥ 3 AND Diagnostic A shows it hasn't run
   - QA-ENGINE: Priority if Diagnostic C ≥ 3 AND competition < 4 weeks away
   - PERFORMANCE-ENGINE: Priority if competition < 3 weeks away
   - META-ENGINE: Priority if Diagnostic A ≤ 2 (engines not being run)
3. Select highest-priority engine
4. **ACTION:** Run that engine per its own protocol
5. **VERIFY:** Check that engine's benchmarks moved

**Files Modified:** None (this is a routing action)

**Done Condition:** Selected engine completes one full cycle

---

### Upgrade 2: Update Engine Registry
**Trigger:** After any engine runs, OR Diagnostic A/B show stale data

**Method:**
1. Read ENGINE-FACTORY.md Part 5 (Engine Registry)
2. For each engine that ran since last audit:
   - Update "Last Cycle" date
   - Update "Benchmarks Met" count
   - Update "Status" if changed (ACTIVE → COMPLETE, etc.)
3. Check for new coverage gaps (per Part 3 Coverage Audit)
4. **ACTION:** Edit ENGINE-FACTORY.md to reflect current state
5. **VERIFY:** Registry accurately reflects reality

**Files Modified:** ENGINE-FACTORY.md (Engine Registry table)

**Done Condition:** Registry updated with all changes since last audit

---

### Upgrade 3: Refresh META.md Hypotheses
**Trigger:** Diagnostic D scores below 4, OR significant work completed

**Method:**
1. Read META.md Part 5 (Active Hypotheses)
2. For each ACTIVE hypothesis:
   - Did recent actions address it? → Mark CONFIRMED if evidence supports
   - Was it contradicted? → Mark REFUTED
   - Was it replaced by more precise version? → Mark SUPERSEDED
3. Look for new weaknesses/gaps not captured in existing hypotheses
4. Write new hypothesis for the highest-urgency gap
5. **ACTION:** Edit META.md Part 5 with updated statuses and new hypotheses
6. **VERIFY:** Hypotheses now accurately orient next work

**Files Modified:** META.md (Active Hypotheses section)

**Done Condition:** All hypotheses current, at least one ACTIVE hypothesis driving next actions

---

### Upgrade 4: Propagate Critical Data Corrections
**Trigger:** Diagnostic C finds inconsistent key statistics, OR `[VERIFY]` tags in presentation files

**Method:**
1. Grep for `[VERIFY]` tags in presentation-critical files (04-presentation/, 03-policy-recommendations/, 06-qa-prep/)
2. Identify 5 key statistics that appear in multiple files
3. For each inconsistent statistic:
   - Determine correct value (web search if needed)
   - List all files containing the old value
   - Replace with correct value in ALL files
4. **ACTION:** Edit affected files with consistent data
5. **VERIFY:** Grep shows no remaining inconsistencies

**Files Modified:** Whatever files contain the corrected data

**Done Condition:** Key statistics consistent across all files, `[VERIFY]` tags resolved in presentation-critical files

---

### Upgrade 5: Trigger Factory Cycle for New Engine
**Trigger:** Diagnostic A/B identify domain gap with no engine, OR ENGINE-FACTORY.md flags NEEDED engine

**Method:**
1. Read ENGINE-FACTORY.md Part 3 (Coverage Audit)
2. Identify highest-priority gap (highest Gap Score or strategic value)
3. Verify no existing engine covers this domain adequately
4. **ACTION:** Run ENGINE-FACTORY.md Generator Protocol (Part 4) to create new engine
5. **VERIFY:** New engine created with all genome components, added to registry

**Files Modified:** ENGINE-FACTORY.md (updates), new `[NAME]-ENGINE.md` created

**Done Condition:** New engine exists, registered, ready to run

---

## Part 3: Recursive Protocol

### The State Audit Cycle

```
┌─────────────────────────────────────────────────────────────┐
│  1. DIAGNOSE                                                │
│     • Run all 5 diagnostics (A-E)                          │
│     • Record scores and assessments                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  2. PRIORITIZE                                              │
│     • Map diagnostic scores to needed actions              │
│     • Consider competition timeline                        │
│     • Apply engine dependency order                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  3. ROUTE                                                   │
│     • Select Upgrade 1-5 based on priority                 │
│     • If multiple needed, order by dependency              │
│     • Output: "Run [ENGINE] because [REASON]"              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  4. LOG                                                     │
│     • Record findings in Part 4 (Cycle Log)                │
│     • Update ENGINE-FACTORY.md registry                    │
└─────────────────────────────────────────────────────────────┘
```

### Priority Rules

1. **Data before polish:** If Diagnostic C < 3, route to DEPTH/IMPROVEMENT engines
2. **Content before rehearsal:** If Diagnostic C < 4, don't run PERFORMANCE-ENGINE
3. **Adversarial before performance:** Run QA-ENGINE before PERFORMANCE-ENGINE
4. **Execution before creation:** If engines exist but haven't run (Diagnostic A < 3), run existing engines before creating new ones
5. **Timeline trumps all:** Within 3 weeks of competition, PERFORMANCE-ENGINE is always priority

### Self-Evolution Rules

**When to add new diagnostics:**
- If an important quality dimension isn't being measured
- If a diagnostic consistently scores "perfect" without corresponding quality

**When to remove diagnostics:**
- If a diagnostic hasn't changed score in 3+ cycles
- If diagnostic consistently produces same result regardless of work done

**When to add new upgrades:**
- If there's a recurring action not covered by current upgrades
- If META.md or ENGINE-FACTORY.md change structure significantly

---

## Part 4: Cycle Log

### Entry Format

```
### State Audit #[N] — [Date]
**Diagnostics:**
- A (Execution Rate): [score]/5 — [brief explanation]
- B (Benchmark Progress): [score]/5 — [brief explanation]
- C (Maturity Stage): Stage [X] — [brief explanation]
- D (Hypothesis Currency): [score]/5 — [brief explanation]
- E (Critical Path): [score]/5 — [brief explanation]

**Key Findings:**
- [Most important issue discovered]
- [Second most important issue]

**Actions Taken:**
- [Upgrade number + description]

**Next Recommended Action:**
"Run [ENGINE-NAME] because [specific reason based on diagnostics]"
```

### Log

---

## Part 5: Benchmarks

| Benchmark | Metric | Current | Target |
|-----------|--------|---------|--------|
| Engine execution rate | Diagnostic A score | — | ≥4 |
| Benchmark progress | Aggregate % complete | — | ≥75% |
| Maturity stage | Stage (1-5) | — | ≥4 by T-4 weeks |
| Hypothesis currency | Diagnostic D score | — | ≥4 |
| Critical path alignment | Diagnostic E score | — | ≥4 |
| Data consistency | Key statistics consistent | — | 100% |
| Registry accuracy | Engines properly tracked | — | 100% |
| Routing precision | Correct engine recommended | — | 90%+ |

**When all targets met:** STATE-ENGINE enters maintenance mode (diagnostics only, routing to PERFORMANCE-ENGINE as needed).

---

## Appendix: Principles

1. **The state engine doesn't improve content—it improves the improvement process.** If you find yourself wanting to edit a speaker script here, stop. That's for RHETORIC-ENGINE.

2. **Truth over optimism.** If diagnostics show the repo is behind, say so clearly. Better to know you're at Stage 2 than falsely believe you're at Stage 4.

3. **The recommendation is the deliverable.** A state audit that ends with "everything looks fine" is useless. Every cycle must produce a specific, actionable next step.

4. **Track the trackers.** If ENGINE-FACTORY.md's registry is out of date, that's a finding—not just something to quietly fix.

5. **Timeline is a constraint, not a suggestion.** With 10 weeks to competition, Stage 5 work is premature. With 2 weeks left, Stage 1 work is impossible.

6. **Coordination beats optimization.** A state audit that triggers 5 engine runs in the right order is more valuable than perfect assessment of a single engine.
