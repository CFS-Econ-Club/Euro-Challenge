# PERFORMANCE-ENGINE.md — Physical Performance and Team Coordination

## What This File Is

META.md decides what matters. IMPROVEMENT-ENGINE.md handles data. RHETORIC-ENGINE.md handles words. QA-ENGINE.md handles adversarial preparation. This file handles **what happens in the room.**

Its domain is:
1. **Speaker scripts** (04-presentation/speaker-*.md) — for timing verification
2. **Rehearsal materials** (09-practice/*.md) — for practice structure
3. **Team coordination** — distribution of roles, backups, contingencies
4. **Stage presence** — delivery, eye contact, vocal dynamics, body language
5. **Crisis handling** — what to do when things go wrong

Its concern is not WHAT is said (RHETORIC-ENGINE) or WHETHER it's true (IMPROVEMENT-ENGINE), but **HOW IT LANDS** when delivered live.

**Invocation:** *"Read PERFORMANCE-ENGINE.md and run a performance cycle."*

**Boundary with other engines:**
- RHETORIC-ENGINE handles the words on the page, including vocal markers
- This engine handles whether those words are delivered within time, with composure, and as a coordinated team
- QA-ENGINE handles what we say in Q&A; this engine handles WHO says it and HOW WE TRANSITION

---

## Part 1: Diagnostics

### Diagnostic A: Timing Accuracy

**Question:** Is every speaker within their allocated time at competition speaking pace?

**Method:**
1. Read each speaker script (04-presentation/speaker-*.md)
2. Count words for each speaker
3. Calculate estimated time at 150 words/minute (standard presentation pace)
4. Add 10% for pauses, transitions, and slide changes
5. Compare to allocated time in CLAUDE.md (Speaker 1: 3:30, S2: 2:30, S3: 3:30, S4: 3:30, S5: 2:00)
6. Flag any speaker over or under by more than 10%

**Scoring:**
- 1 = Multiple speakers >15% over/under time
- 2 = One speaker >15% off, or multiple 10-15% off
- 3 = All speakers within 15% of allocation
- 4 = All speakers within 10% of allocation
- 5 = All speakers within 5% of allocation, verified by timed read-through

**Current Assessment (Cycle 0):** Score = Unknown (not yet measured)

**Why This Matters:** Going over time is an automatic penalty. Going under time means missed content. Timing is 100% preventable with proper measurement.

---

### Diagnostic B: Team Coordination Readiness

**Question:** Does every team member know their role and have backup for Q&A?

**Method:**
1. Read strategy-notes.md for team distribution plan
2. Check: Is there a primary speaker for each domain? (Euro, Netherlands, Climate, Policy 1, Policy 2)
3. Check: Is there a backup speaker for each domain?
4. Check: Is there a "team captain" who can redirect stuck Q&A?
5. Check: Is there a signal system for "I need help" during Q&A?

**Scoring:**
- 1 = No distribution plan exists
- 2 = Distribution plan exists, no backups defined
- 3 = Primary + backup for each domain, no signal system
- 4 = Full coordination protocol including signals
- 5 = Protocol documented + practiced in at least 2 rehearsals

**Current Assessment (Cycle 0):** Score = 2
- strategy-notes.md shows distribution: S1 (Euro/ECB), S2 (NL), S3 (Climate), S4-5 (Policies)
- No backup assignments documented
- No signal system for stuck moments

**Why This Matters:** Teamwork is 10% of score (6 points). Fumbling who answers what looks unprepared and loses points.

---

### Diagnostic C: Rehearsal Effectiveness

**Question:** Is the team following a structured practice schedule with measurable improvement?

**Method:**
1. Read rehearsal-schedule.md and improvement-log.md
2. Check: Are rehearsals scheduled? How many completed?
3. Check: Does each rehearsal have specific goals and evaluation criteria?
4. Check: Is improvement-log.md being updated after each rehearsal?
5. Check: Are scores trending upward in self-evaluation-rubric.md?

**Scoring:**
- 1 = No rehearsals completed
- 2 = 1-2 rehearsals completed, no improvement tracking
- 3 = 3+ rehearsals, tracking exists but inconsistent
- 4 = Structured rehearsal program with tracking, scores documented
- 5 = 5+ rehearsals, clear improvement trend, mock competition completed

**Current Assessment (Cycle 0):** Score = 2
- rehearsal-schedule.md exists with 5 rehearsals planned
- improvement-log.md has template + 4 example entries (appears to be sample data)
- No evidence of actual completed rehearsals

**Why This Matters:** Teams that rehearse with structure outperform teams that "practice" without goals. Measured practice produces measurable improvement.

---

### Diagnostic D: Contingency Preparedness

**Question:** Does the team have plans for when things go wrong?

**Method:**
1. Check for documented contingencies:
   - What to do if running over time (cut points marked?)
   - What to do if running under time (expand points marked?)
   - What to do if a speaker forgets their lines
   - What to do if a judge asks a question no one can answer
   - What to do if technology fails (slides don't work)
2. Are these contingencies written down anywhere?
3. Have they been practiced?

**Scoring:**
- 1 = No contingencies documented
- 2 = 1-2 contingencies mentioned but not formalized
- 3 = Basic contingencies documented (over/under time)
- 4 = Full contingency set documented
- 5 = Full contingencies documented + practiced in mock rehearsal

**Current Assessment (Cycle 0):** Score = 1
- No contingency documentation found
- improvement-log.md mentions "running over time" as an issue but no protocol for handling it

**Why This Matters:** Things go wrong in live presentations. Teams with contingency plans recover; teams without them panic.

---

### Diagnostic E: Stage Presence Readiness

**Question:** Are speakers prepared to deliver with confidence and engagement?

**Method:**
1. Read each speaker script for stage directions
2. Check: Are there [PAUSE] markers? Eye contact notes? Slide transition cues?
3. Check: Is there guidance on vocal dynamics (speed, volume, emphasis)?
4. Check: Has any delivery technique been practiced?
5. Check: Are there notes on body language, stance, or movement?

**Scoring:**
- 1 = No performance markers in scripts
- 2 = Basic [PAUSE] markers only
- 3 = Pause + slide markers, no vocal/body guidance
- 4 = Full performance markers (pause, slides, vocal, eye contact)
- 5 = Performance markers + practiced delivery feedback documented

**Current Assessment (Cycle 0):** Score = 3
- Speaker 1 script has [PAUSE] markers and [SLIDE X] cues
- No vocal dynamics markers (speed up, slow down, emphasis)
- No body language or eye contact notes
- RHETORIC-ENGINE Upgrade 7 covers this but not yet applied

**Why This Matters:** Presentation is 10% of score (6 points). Delivery quality affects how judges perceive all other content.

---

## Part 2: Upgrades

These are ordered by impact. Work top-down. Do not skip upgrades.

### Upgrade 1: Measure and Verify Timing

**Trigger:** Apply when Diagnostic A scores below 4

**Method:**
1. For each speaker script (speaker-1 through speaker-5):
   a. Count total words (excluding stage directions in brackets)
   b. Calculate: Estimated Time = Word Count / 150 (words per minute)
   c. Add 10% for pauses: Adjusted Time = Estimated Time × 1.10
   d. Convert to minutes:seconds format
2. Compare to allocated time:
   - Speaker 1: 3:30 (210 seconds)
   - Speaker 2: 2:30 (150 seconds)
   - Speaker 3: 3:30 (210 seconds)
   - Speaker 4: 3:30 (210 seconds)
   - Speaker 5: 2:00 (120 seconds)
3. Create a timing report table:

```
| Speaker | Word Count | Est. Time | Adjusted | Allocated | Variance | Status |
|---------|------------|-----------|----------|-----------|----------|--------|
| 1 | X | Y:ZZ | A:BB | 3:30 | +/-C sec | OK/Over/Under |
```

4. For any speaker >10% off:
   - If OVER: Mark cut points in their script (sentences that can be skipped)
   - If UNDER: Mark expand points (additional detail that can be added)

**Files Modified:**
- 04-presentation/speaker-*.md (add cut/expand markers if needed)
- Create 09-practice/timing-report.md with results

**Done Condition:** All speakers within 10% of allocation, with cut/expand markers for safety margin

---

### Upgrade 2: Build Team Coordination Protocol

**Trigger:** Apply when Diagnostic B scores below 4

**Method:**
1. Create a team coordination document (09-practice/team-coordination.md) with:
   a. **Domain ownership table:**
      | Domain | Primary Speaker | Backup Speaker |
      |--------|----------------|----------------|
      | Euro Area / ECB | Speaker 1 | Speaker 4 |
      | Netherlands Economy | Speaker 2 | Speaker 1 |
      | Climate Challenge | Speaker 3 | Speaker 2 |
      | Policy 1 (Grid) | Speaker 4 | Speaker 5 |
      | Policy 2 (Agriculture) | Speaker 4 | Speaker 5 |
      | Policy 3 (Skills) | Speaker 5 | Speaker 4 |
      | Euro Implications | Speaker 5 | Speaker 1 |

   b. **Q&A signal system:**
      - "I can take this" — make eye contact and slight nod to teammates
      - "I need help" — pause, look at backup speaker, slight gesture
      - "Pass to me" — backup speaker makes eye contact with stuck speaker

   c. **Team captain role:** Who coordinates if multiple people could answer? (Usually Speaker 1 or 5)

   d. **"I don't know" protocol:**
      - Never say "I don't know" directly
      - Instead: "That's an interesting angle — based on our research, we'd expect..."
      - Or: "We didn't encounter that specific data point, but here's how we'd reason through it..."
      - Signal for help if truly stuck

**Files Created:**
- 09-practice/team-coordination.md

**Done Condition:** Domain ownership table complete with primary + backup for all domains; signal system documented

---

### Upgrade 3: Structure the Rehearsal Program

**Trigger:** Apply when Diagnostic C scores below 4

**Method:**
1. Review and enhance rehearsal-schedule.md to include:
   a. **Before each rehearsal:** Specific goals (what to test)
   b. **During each rehearsal:** Who facilitates, who times, who evaluates
   c. **After each rehearsal:** How feedback is captured and logged

2. Create rehearsal checklist template:

```
## Rehearsal [N] — [Date]
**Goals:** [What we're testing]
**Timer:** [Who times]
**Evaluators:** [Who watches]

### Timing Check
| Speaker | Target | Actual | Status |
|---------|--------|--------|--------|
| 1 | 3:30 | ___:___ | ✅/❌ |
...

### Q&A Distribution
| Domain | Questions Asked | Who Answered | Quality (1-5) |
|--------|-----------------|--------------|----------------|
| Euro | | | |
...

### Issues Identified
1. [Issue] → [Action to fix] → [Owner]
2. ...

### Improvement Log Entry
[To be copied to improvement-log.md]
```

3. Assign rehearsal roles:
   - **Timer:** Tracks each speaker's time, signals if over
   - **Evaluator(s):** Watch for content accuracy, delivery quality, transitions
   - **Mock judge:** Asks prepared questions (rotates among team members)

**Files Modified:**
- 09-practice/rehearsal-schedule.md

**Files Created:**
- 09-practice/rehearsal-checklist-template.md

**Done Condition:** Each scheduled rehearsal has goals, roles, and evaluation criteria; checklist template created

---

### Upgrade 4: Build Contingency Protocols

**Trigger:** Apply when Diagnostic D scores below 4

**Method:**
1. Create 09-practice/contingency-protocols.md with:

   a. **Running over time:**
      - Each speaker has "cut points" marked in script (from Upgrade 1)
      - Team captain signals if running long (pre-agreed hand signal)
      - Speaker skips to their closing line and transitions

   b. **Running under time:**
      - Each speaker has "expand points" marked in script
      - Can add additional data point, example, or explanation
      - If still short, smooth recovery: "Let me add one more point..."

   c. **Speaker forgets lines:**
      - Don't panic, don't apologize
      - Glance at notes (it's allowed)
      - Bridge phrase: "Building on that point..." or "What this means for the Netherlands is..."
      - Teammates can prompt with a keyword if needed

   d. **Question no one can answer:**
      - Use "I don't know" protocol from Upgrade 2
      - Reason through logically: "We'd approach that by considering..."
      - Concede honestly if truly outside scope: "That's beyond what we researched, but..."

   e. **Technology failure:**
      - Slides don't work: Continue without them (know your data)
      - Microphone fails: Project voice, move closer to judges
      - Have printed backup of key data points (brochure serves this)

   f. **Judge interruption:**
      - Stop speaking immediately
      - Listen fully to the interruption
      - Respond directly, then resume or skip to next point

2. Practice at least one contingency in a mock rehearsal

**Files Created:**
- 09-practice/contingency-protocols.md

**Done Condition:** All 6 contingency types documented; at least 1 practiced

---

### Upgrade 5: Add Performance Markers to Scripts

**Trigger:** Apply when Diagnostic E scores below 4

**Method:**
1. For each speaker script, add performance markers beyond [PAUSE]:

   a. **Vocal dynamics:**
      - **[SLOW]** — Slow down for emphasis (critical numbers, key claims)
      - **[FAST]** — Speed up for lists or buildup
      - **[DROP VOICE]** — Lower volume to force audience to lean in
      - **[EMPHASIZE word]** — Stress this specific word

   b. **Eye contact:**
      - **[EYE CONTACT]** — Look at judges, not slides
      - **[SCAN ROOM]** — Brief sweep of audience

   c. **Body language:**
      - **[GESTURE TO SLIDE]** — Point to specific chart element
      - **[OPEN STANCE]** — Hands visible, facing audience
      - **[STEP FORWARD]** — Move toward judges for key point

   d. **Transitions:**
      - **[TURN TO SPEAKER X]** — Physical transition between speakers
      - **[NOD TO NEXT]** — Acknowledge handoff

2. Example transformation:
   ```
   Before: "The Netherlands has 43% debt to GDP."

   After: "**[SLOW] [EYE CONTACT]** The Netherlands has just **[EMPHASIZE: just]** 43% debt-to-GDP **[PAUSE]** — well below the EU limit."
   ```

**Note:** This overlaps with RHETORIC-ENGINE Upgrade 7. Coordinate to avoid duplication. RHETORIC-ENGINE focuses on the words; this engine ensures the markers are physically practiced.

**Files Modified:**
- 04-presentation/speaker-*.md

**Done Condition:** Each script has markers for vocal dynamics, eye contact, and body language

---

### Upgrade 6: Create Mock Judge Question Bank

**Trigger:** Apply after Upgrades 1-5 are complete

**Method:**
1. Create 09-practice/mock-judge-questions.md with:
   a. 20 questions drawn from qa-master-document.md (mix of categories)
   b. 5 anchor questions from anchor-questions.md
   c. 3 "nightmare" questions (hard adversarial questions)
   d. 2 curveball questions (unexpected angles not in Q&A prep)

2. Format for mock judge use:
   - Questions numbered, with domain and difficulty noted
   - Space to record who answered and quality rating

3. Rotate mock judge role among team members or recruit external mock judges (teachers, parents)

**Files Created:**
- 09-practice/mock-judge-questions.md

**Done Condition:** 30 questions prepared, categorized by domain and difficulty

---

### Upgrade 7: Conduct and Log First Timed Rehearsal

**Trigger:** Apply after Upgrades 1-3 are complete

**Method:**
1. Schedule and conduct Rehearsal 1 (or next rehearsal in sequence)
2. Use rehearsal checklist from Upgrade 3
3. Time each speaker with stopwatch
4. Record actual times, Q&A distribution, and issues
5. Update improvement-log.md with findings
6. Identify top 3 issues to fix before next rehearsal

**Files Modified:**
- 09-practice/improvement-log.md
- 09-practice/self-evaluation-rubric.md (if team completes evaluations)

**Done Condition:** One full timed rehearsal completed and logged; at least 3 issues identified with actions

---

## Part 3: Recursive Protocol

### The Cycle

```
1. RUN DIAGNOSTICS A-E (Part 1)
   → Produces prioritized weakness list

2. SELECT the lowest-scoring diagnostic
   → If multiple at same score, priority order: A > B > D > E > C
   (Timing is most critical — can't recover from over-time in competition)

3. APPLY the relevant Upgrade (Part 2)
   → Follow the method exactly

4. EVALUATE
   → Re-run the diagnostic — did score improve?
   → If no improvement, check if method was followed correctly

5. LOG the cycle (Part 4)

6. RETURN TO STEP 1 if any diagnostic scores < 4
```

### Priority Rules

- **Timing before everything.** If scripts are over time, nothing else matters — you'll be cut off. Address Diagnostic A first.
- **Coordination before polish.** A team that knows who says what looks professional. A team with beautiful delivery but confused Q&A distribution looks unprepared.
- **Practice after structure.** Don't rehearse until you know what you're rehearsing and how you'll measure it.

### Self-Evolution Rules

1. **After each cycle**, update diagnostic "Current Assessment" fields
2. **If a new performance issue is discovered** (e.g., a speaker has a nervous habit), add it as a diagnostic or upgrade
3. **If an upgrade method doesn't produce measurable improvement**, revise the method
4. **When all benchmarks are met**, change engine status to COMPLETE and shift to maintenance mode (periodic check-ins only)

---

## Part 4: Cycle Log

### Template

```
### Cycle [N] — [Date]
**Diagnostic results:** [Scores for each diagnostic]
**Upgrade applied:** [Which upgrade; which files]
**Before:** [State before]
**After:** [State after]
**Assessment:** [What improved; what still needs work]
**Next priority:** [Which upgrade to run next]
```

### Log

*(No cycles run yet. This section will grow with each invocation.)*

---

## Part 5: Benchmarks

| Benchmark | Metric | Current | Target |
|-----------|--------|---------|--------|
| B1: Timing accuracy | All speakers within 10% of allocation | Unknown | 5/5 |
| B2: Timing safety margin | Each script has cut/expand points marked | 0/5 | 5/5 |
| B3: Team coordination | All domains have primary + backup | 0/6 | 6/6 |
| B4: Signal system | Q&A help signals documented and known | No | Yes |
| B5: Rehearsal structure | Each rehearsal has goals + evaluation | Partial | Full |
| B6: Contingencies | All 6 contingency types documented | 0/6 | 6/6 |
| B7: Performance markers | Each script has vocal + eye contact markers | 0/5 | 5/5 |
| B8: Mock question bank | 30 questions prepared for mock judges | 0 | 30 |
| B9: Completed rehearsals | Full timed rehearsals logged | 0 | 3+ |
| B10: Diagnostic scores | All diagnostics score 4+ | Unknown | All 4+ |

**Engine Status:** ACTIVE (benchmarks 0/10 met)

---

## Appendix: Principles of Performance Preparation

1. **Time is non-negotiable.** Going over time in competition means being cut off mid-sentence. The only way to guarantee timing is to measure it, mark cut points, and practice with a timer.

2. **Confusion is visible.** When three team members look at each other during Q&A, judges see it. When one speaker struggles and no one helps, judges see it. Coordination signals prevent visible confusion.

3. **Things go wrong.** Technology fails. Speakers blank. Judges ask impossible questions. Teams with contingency plans recover; teams without them unravel.

4. **Rehearsal without measurement is just repetition.** A "practice" without timing, without feedback, without logging improvement is not preparation — it's comfort. Measured practice produces improvement.

5. **The room is different from the page.** A script that reads well may not speak well. Only actual timed read-throughs reveal where speakers stumble, run long, or lose energy.

6. **Excellence is visible in transitions.** The handoff between speakers, the smooth recovery from a hard question, the seamless continuation after a technology glitch — these are where judges distinguish good teams from great ones.

7. **You cannot improvise coordination.** Teams that say "we'll figure out who answers during Q&A" always look confused. The time to decide is before, not during.
