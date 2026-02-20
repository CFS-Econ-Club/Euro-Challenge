# CONSISTENCY-ENGINE.md — Global Coherence Enforcer

## What This File Is
- **Scope**: Entire repository. Ensures changes in one place (e.g., a policy FACELIFT) propagate accurately to all related artifacts (Q&A, presentation scripts, brochures, summaries).
- **Out of Scope**: Creating new content, rewriting for persuasion (that's RHETORIC-ENGINE's job), or deep research (DEPTH-ENGINE's job). This engine purely deals with synchronization and preventing contradictions.
- **Invocation command**: *"Read CONSISTENCY-ENGINE.md and run a consistency cycle."*

## Part 1: Diagnostics
- **DIAGNOSTIC A: Policy-Q&A Synchronization**
  - **QUESTION:** Do the questions and answers in `06-qa-prep/*` accurately reflect the *current* versions of the policies in `03-policy-recommendations/*`?
  - **METHOD:**
    1. Read the core policies in `03-policy-recommendations/`.
    2. Read `06-qa-prep/qa-master-document.md` and related Q&A files.
    3. Check for outdated references, changed costs, altered timelines, or abandoned mechanisms.
  - **SCORE:** pass/fail
  - **CURRENT ASSESSMENT:** To be filled on first run

- **DIAGNOSTIC B: Presentation-Policy Synchronization**
  - **QUESTION:** Do the speaker scripts in `04-presentation/*` describe exactly the same policies and mechanisms as the detailed documents in `03-policy-recommendations/*`?
  - **METHOD:**
    1. Read the core policies.
    2. Read the speaker scripts.
    3. Verify that all specific details (numbers, names, timelines) mentioned in the scripts match the policy documents perfectly.
  - **SCORE:** pass/fail
  - **CURRENT ASSESSMENT:** To be filled on first run

- **DIAGNOSTIC C: Brochure Consistency**
  - **QUESTION:** Does the judge brochure in `05-brochure/*` accurately reflect the current policies and economic data used elsewhere in the repository?
  - **METHOD:**
    1. Read `05-brochure/brochure-content.md` (or equivalent).
    2. Cross-reference against policies and data files.
  - **SCORE:** pass/fail
  - **CURRENT ASSESSMENT:** To be filled on first run

- **DIAGNOSTIC D: Macro Data Uniformity**
  - **QUESTION:** Is the same macroeconomic data (e.g., inflation rate, GDP growth) used consistently across the scripts, research summaries, and Q&A?
  - **METHOD:**
    1. Identify key statistics used in Speaker 1's script.
    2. Search the repository for these metrics to ensure no contradictory numbers exist elsewhere.
  - **SCORE:** pass/fail
  - **CURRENT ASSESSMENT:** To be filled on first run

## Part 2: Upgrades
- **UPGRADE 1: Q&A Synchronization**
  - **TRIGGER:** Diagnostic A fails.
  - **METHOD:**
    1. Identify all contradictions between the policies and the Q&A documents.
    2. Rewrite the Q&A answers (and adjust the questions if necessary) to perfectly reflect the new policy details.
    3. Delete Q&A items that are no longer relevant due to policy shifts.
  - **FILES MODIFIED:** `06-qa-prep/*`
  - **DONE CONDITION:** Diagnostic A passes.

- **UPGRADE 2: Script Synchronization**
  - **TRIGGER:** Diagnostic B fails.
  - **METHOD:**
    1. Identify deviations in the speaker scripts from the core policy documents.
    2. Edit the scripts to align the facts while preserving the rhetorical flow (defer to RHETORIC-ENGINE for deep style edits, just fix the facts here).
  - **FILES MODIFIED:** `04-presentation/speaker-*.md`
  - **DONE CONDITION:** Diagnostic B passes.

- **UPGRADE 3: Brochure Synchronization**
  - **TRIGGER:** Diagnostic C fails.
  - **METHOD:**
    1. Update the brochure content to reflect the current state of the policies and data.
  - **FILES MODIFIED:** `05-brochure/brochure-content.md`
  - **DONE CONDITION:** Diagnostic C passes.

- **UPGRADE 4: Data Uniformity Enforcement**
  - **TRIGGER:** Diagnostic D fails.
  - **METHOD:**
    1. Establish the "master" values for disputed statistics (usually based on `08-data/` or the most recently updated core document).
    2. Update all divergent references across the repository to match the master values.
  - **FILES MODIFIED:** Various (search and replace).
  - **DONE CONDITION:** Diagnostic D passes.

## Part 3: Recursive Protocol
- The cycle: diagnose → select → apply → evaluate → log
- **Priority Rules:**
  1. Fix Presentation Scripts first (what judges will definitely hear).
  2. Fix Q&A second (what judges will likely ask about).
  3. Fix Brochure third (what judges will read).
  4. Fix Macro data last (important, but less likely to be glaringly contradictory than a changed policy).
- **Self-evolution rules:** If the engine consistently finds the same type of desynchronization, add a specific diagnostic for that failure mode.

## Part 4: Cycle Log
### Log Template
```
### Consistency Cycle [N] — [Date]
**Diagnostics Run:** [List]
**Failing Diagnostics:** [List]
**Upgrades Applied:** [List]
**Files Modified:** [List]
**Result:** [Summary of sync state]
```

### Log Entries
*To be filled.*

## Part 5: Benchmarks
| Benchmark | Metric | Current | Target |
|-----------|--------|---------|--------|
| Policy-Q&A Sync | Diagnostic A | FAIL | PASS |
| Policy-Script Sync | Diagnostic B | FAIL | PASS |
| Brochure Sync | Diagnostic C | FAIL | PASS |
| Data Uniformity | Diagnostic D | FAIL | PASS |

## Appendix: Principles
1. **The Policy is the Source of Truth:** If the presentation script contradicts the policy document in `03-policy-recommendations/`, the policy document is assumed correct, and the script must change (unless explicitly directed otherwise).
2. **Delete Stale Fragments:** It is better to have a slightly shorter Q&A doc than to leave in a question about a mechanism we deleted during a FACELIFT.
3. **No Silent Changes:** When this engine changes a script to match a policy, it should flag that change clearly in the cycle log, as it may affect timing or rhetorical flow.
4. **Trigger After Upheaval:** This engine is most critical immediately after `FACELIFT-ENGINE` runs. A major structural change necessitates a consistency pass.