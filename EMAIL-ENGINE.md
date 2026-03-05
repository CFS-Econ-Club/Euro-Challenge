# EMAIL-ENGINE.md — Stakeholder Communication Drafting System

## What This File Is

- **What domain this engine covers**: Drafting professional emails to three stakeholder groups: (1) team members, (2) parents/guardians, and (3) school teachers/administrators. Also covers follow-up messages, progress updates, meeting requests, and thank-you notes.
- **What it does NOT cover**: Q&A preparation (QA-ENGINE), presentation scripts (RHETORIC-ENGINE), brochure content (RHETORIC-ENGINE Upgrade 6), or internal team coordination protocols (PERFORMANCE-ENGINE). This engine handles *external-facing* and *formal internal* written communication only.
- **Invocation**: *"Read EMAIL-ENGINE.md and run a cycle."*

---

## Part 1: Diagnostics

### DIAGNOSTIC A: Audience Segmentation Test
**QUESTION**: Does the repo contain distinct email templates for each of the three stakeholder audiences with appropriately tailored tone and content?

**METHOD**:
1. Check for a dedicated `11-communication/` or similar folder with email drafts
2. For each stakeholder group (team, parents, teachers), check:
   - Is there at least one email template?
   - Does the tone match the audience? (team = collaborative/direct; parents = informative/reassuring; teachers = formal/academic)
3. Score:
   - 1 = No email templates exist
   - 2 = Templates exist but are generic/interchangeable across audiences
   - 3 = Templates exist for 2 audiences with some differentiation
   - 4 = Templates exist for all 3 audiences with clear tone differentiation
   - 5 = Templates exist for all 3 audiences + situational variants (request, update, thank-you)

**CURRENT ASSESSMENT**: 1 — No communication folder or email templates detected in repo.

**WHY THIS MATTERS**: Different stakeholders need different information at different levels of formality. Judges may perceive professionalism through parent/teacher communications (e.g., permission letters, progress reports).

---

### DIAGNOSTIC B: Content Completeness Test
**QUESTION**: Do email templates include all necessary information for their purpose?

**METHOD**:
1. For each existing email template, check for these elements:
   - Clear subject line
   - Appropriate greeting
   - Purpose stated in first 2 sentences
   - Relevant details (dates, times, locations, expectations)
   - Call-to-action or next steps
   - Professional sign-off
2. Score:
   - 1 = No templates exist
   - 2 = Templates exist but missing 3+ required elements
   - 3 = Templates missing 1-2 required elements
   - 4 = All templates have all required elements
   - 5 = Templates have all elements + anticipatory answers to likely questions

**CURRENT ASSESSMENT**: 1 — No templates exist.

**WHY THIS MATTERS**: Incomplete emails create back-and-forth confusion and project unprofessionalism.

---

### DIAGNOSTIC C: Tone Calibration Test
**QUESTION**: Are emails appropriately formal, warm, and confident without being stiff or casual?

**METHOD**:
1. Read any existing email templates
2. Evaluate each for:
   - Formality level (appropriate for audience)
   - Warmth (not robotic)
   - Confidence (not apologetic or uncertain)
   - Conciseness (no unnecessary verbosity)
3. Score:
   - 1 = No templates to evaluate
   - 2 = Templates are tone-deaf (too casual for teachers, too formal for team, etc.)
   - 3 = Templates are acceptable but generic/flat
   - 4 = Templates strike appropriate tone for each audience
   - 5 = Templates are exemplary — warm, professional, and memorable

**CURRENT ASSESSMENT**: 1 — No templates exist.

**WHY THIS MATTERS**: Tone affects how stakeholders perceive the team's seriousness and professionalism.

---

### DIAGNOSTIC D: Situational Coverage Test
**QUESTION**: Does the email library cover the key situations the team will encounter?

**METHOD**:
1. Check for templates in these categories:
   - **Team**: Meeting requests, task assignments, deadline reminders, celebration/thanks
   - **Parents**: Initial notification, progress updates, event invitations, thank-you
   - **Teachers**: Permission/request letters, progress reports, invitation to presentation, thank-you
2. Score:
   - 1 = 0-2 situational templates
   - 2 = 3-4 situational templates
   - 3 = 5-6 situational templates
   - 4 = 7-8 situational templates
   - 5 = All 9+ situational templates present

**CURRENT ASSESSMENT**: 1 — No templates exist.

**WHY THIS MATTERS**: Teams waste time drafting from scratch under pressure. Templates ensure consistency and quality.

---

### DIAGNOSTIC E: Customization Ease Test
**QUESTION**: Can a team member quickly customize a template for their specific situation without breaking the structure?

**METHOD**:
1. Review template formatting
2. Check for:
   - Clear placeholders marked (e.g., `[DATE]`, `[NAME]`)
   - Instructions for customization
   - Modular sections that can be added/removed
3. Score:
   - 1 = No templates exist
   - 2 = Templates exist but are rigid blocks of text
   - 3 = Templates have some placeholders but unclear customization guidance
   - 4 = Templates have clear placeholders and brief instructions
   - 5 = Templates are highly modular with detailed customization notes

**CURRENT ASSESSMENT**: 1 — No templates exist.

**WHY THIS MATTERS**: Templates that are hard to customize won't be used — teams will write from scratch instead.

---

## Part 2: Upgrades

### UPGRADE 1: Create Communication Folder Structure
**TRIGGER**: Apply when Diagnostic A scores ≤2

**METHOD**:
1. Create folder: `11-communication/`
2. Create subfolders:
   - `11-communication/team/`
   - `11-communication/parents/`
   - `11-communication/teachers/`
3. Create a `README.md` in `11-communication/` with:
   - Purpose of the folder
   - How to use templates
   - Quick links to each subfolder

**FILES MODIFIED**: New folder structure created

**DONE CONDITION**: Folder structure exists with README navigation guide

---

### UPGRADE 2: Draft Core Team Email Templates
**TRIGGER**: Apply when Diagnostic A scores ≤3 OR Diagnostic D scores ≤2

**METHOD**:
1. Create these templates in `11-communication/team/`:
   - `meeting-request.md` — Request for ad-hoc or recurring meeting
   - `task-assignment.md` — Assigning responsibility with deadline
   - `deadline-reminder.md` — Friendly reminder about upcoming deadline
   - `progress-update.md` — Sharing completed work with team
   - `celebration-thanks.md` — Acknowledging team member contribution
2. Each template must include:
   - Subject line options (2-3 variants)
   - Greeting
   - Purpose in first 2 sentences
   - Relevant details with `[PLACEHOLDER]` markers
   - Clear call-to-action
   - Professional but warm sign-off

**FILES MODIFIED**: `11-communication/team/*.md`

**DONE CONDITION**: All 5 templates created with complete structure

---

### UPGRADE 3: Draft Parent Email Templates
**TRIGGER**: Apply when Diagnostic A scores ≤3 OR Diagnostic D scores ≤2

**METHOD**:
1. Create these templates in `11-communication/parents/`:
   - `initial-notification.md` — Informing parents about competition participation
   - `progress-update.md` — Mid-project update on team progress
   - `event-invitation.md` — Inviting parents to final presentation
   - `thank-you.md` — Post-competition gratitude
2. Tone: Informative, reassuring, proud but not boastful
3. Include practical details parents care about:
   - Time commitment
   - Educational value
   - Key dates
   - How they can support (if applicable)

**FILES MODIFIED**: `11-communication/parents/*.md`

**DONE CONDITION**: All 4 templates created with parent-appropriate tone

---

### UPGRADE 4: Draft Teacher Email Templates
**TRIGGER**: Apply when Diagnostic A scores ≤3 OR Diagnostic D scores ≤2

**METHOD**:
1. Create these templates in `11-communication/teachers/`:
   - `permission-request.md` — Requesting permission to miss class/submit late work
   - `progress-report.md` — Formal update on learning outcomes
   - `presentation-invitation.md` — Inviting teachers to attend final presentation
   - `thank-you.md` — Post-competition gratitude and reflection
2. Tone: Formal, respectful, academically oriented
3. Emphasize:
   - Educational alignment
   - Skills being developed
   - Academic rigor
   - Gratitude for support

**FILES MODIFIED**: `11-communication/teachers/*.md`

**DONE CONDITION**: All 4 templates created with teacher-appropriate formality

---

### UPGRADE 5: Add Customization Guidance
**TRIGGER**: Apply when Diagnostic E scores ≤3

**METHOD**:
1. Add to each template:
   - `[PLACEHOLDER]` markers in ALL CAPS with brackets
   - Brief inline comments: `<!-- Replace with specific date -->`
   - A "Customization Notes" section at the end of each template
2. Create `11-communication/TEMPLATE-GUIDE.md` with:
   - How to use placeholders
   - Tone guidelines for each audience
   - Common mistakes to avoid
   - Examples of well-customized emails

**FILES MODIFIED**: All template files + new `TEMPLATE-GUIDE.md`

**DONE CONDITION**: All templates have clear placeholders and customization notes; guide file exists

---

### UPGRADE 6: Add Situational Variants
**TRIGGER**: Apply when Diagnostic D scores ≤4

**METHOD**:
1. Identify gaps in situational coverage
2. Create additional templates based on team needs:
   - `urgent-notice.md` — Last-minute changes/cancellations
   - `apology.md` — For missed deadlines or mistakes
   - `follow-up.md` — After a meeting or conversation
   - `resource-request.md` — Asking for materials, contacts, or support
3. Place in appropriate audience subfolder

**FILES MODIFIED**: `11-communication/*/` as needed

**DONE CONDITION**: 9+ total templates across all audiences

---

### UPGRADE 7: Tone Polish Pass
**TRIGGER**: Apply when Diagnostic C scores ≤3

**METHOD**:
1. Read each template aloud
2. For team emails: Ensure collaborative, peer-appropriate tone (not bossy, not passive)
3. For parent emails: Ensure informative, reassuring tone (not condescending, not overly casual)
4. For teacher emails: Ensure formal, respectful tone (not stiff, not casual)
5. Remove:
   - Apologetic language ("Sorry to bother you...")
   - Uncertainty ("I think we might...")
   - Unnecessary formality for team emails
6. Add:
   - Warmth markers (appropriate for audience)
   - Confidence markers ("We will..." not "We hope to...")
   - Specificity (concrete details over vague promises)

**FILES MODIFIED**: All template files

**DONE CONDITION**: Diagnostic C scores 4+

---

### UPGRADE 8: Real-World Validation
**TRIGGER**: Apply when all other upgrades are complete

**METHOD**:
1. Have each team member customize and send at least one template email
2. Collect feedback:
   - Was the template easy to use?
   - Did the recipient understand the message?
   - Was the tone appropriate?
3. Revise templates based on feedback
4. Log any edge cases the templates didn't cover

**FILES MODIFIED**: All template files (as needed based on feedback)

**DONE CONDITION**: All templates have been field-tested and revised

---

## Part 3: Recursive Protocol

### The Cycle
```
1. DIAGNOSE — Run all 5 diagnostics, score each
2. SELECT — Pick highest-priority upgrade based on:
   - Foundational first (folder structure before templates)
   - Coverage gaps before polish
   - Audience completeness before situational variants
3. APPLY — Execute upgrade method exactly as specified
4. EVALUATE — Re-run affected diagnostics, confirm improvement
5. LOG — Record cycle in Part 4
```

### Priority Rules
1. **Foundation first**: Never draft templates (Upgrades 2-4) before folder structure exists (Upgrade 1)
2. **Coverage before polish**: Complete all core templates before tone polish (Upgrade 7)
3. **Audience completeness**: Ensure all 3 audiences have templates before adding situational variants
4. **Field test last**: Always validate with real use (Upgrade 8) after all other upgrades

### Self-Evolution Rules
- If a new stakeholder group emerges (e.g., external mentors, competition judges), add a subfolder and templates
- If templates are consistently misused, add better customization guidance
- If a template type is used frequently, create variants for common sub-situations

---

## Part 4: Cycle Log

### Template for Entries
```
### Cycle [N] — [Date]
**Diagnostics**: A=[score], B=[score], C=[score], D=[score], E=[score]
**Upgrades Applied**: [List]
**Files Created/Modified**: [List]
**Results**: [Summary of improvements]
**Next Priority**: [Which upgrade to run next]
```

### Log

### Cycle 1 — 2026-03-04
**Diagnostics**: A=1, B=1, C=1, D=1, E=1 (no templates existed)
**Upgrades Applied**: 1, 2, 3, 4, 5
**Files Created/Modified**: 
- `11-communication/README.md`
- `11-communication/TEMPLATE-GUIDE.md`
- `11-communication/team/meeting-request.md`
- `11-communication/team/task-assignment.md`
- `11-communication/team/deadline-reminder.md`
- `11-communication/team/progress-update.md`
- `11-communication/team/celebration-thanks.md`
- `11-communication/parents/initial-notification.md`
- `11-communication/parents/progress-update.md`
- `11-communication/parents/event-invitation.md`
- `11-communication/parents/thank-you.md`
- `11-communication/teachers/permission-request.md`
- `11-communication/teachers/progress-report.md`
- `11-communication/teachers/presentation-invitation.md`
- `11-communication/teachers/thank-you.md`
**Results**: Complete email template infrastructure created. 13 templates across 3 audiences with full customization guidance. All templates include placeholder markers, customization notes, and tone-appropriate language.
**Next Priority**: Upgrade 6 (Add Situational Variants) if team identifies gaps during use. Upgrade 8 (Real-World Validation) — have team members send at least one template email and collect feedback.

---

## Part 5: Benchmarks

| Benchmark | Metric | Current | Target |
|-----------|--------|---------|--------|
| Folder Structure | `11-communication/` with 3 subfolders exists | No | Yes |
| Team Templates | 5+ team email templates created | 0 | 5 |
| Parent Templates | 4+ parent email templates created | 0 | 4 |
| Teacher Templates | 4+ teacher email templates created | 0 | 4 |
| Total Templates | All situational templates present | 0 | 13+ |
| Placeholder Quality | All templates use `[PLACEHOLDER]` format | N/A | 100% |
| Customization Guide | `TEMPLATE-GUIDE.md` exists | No | Yes |
| Tone Calibration | Diagnostic C scores 4+ | 1 | 4 |
| Field Testing | All templates tested by team members | No | Yes |
| Feedback Integration | Templates revised based on real use | N/A | Yes |

---

## Appendix: Principles

### 1. Audience First
Every email starts with: "Who is reading this, and what do they need to know?" Team members need clarity and actionability. Parents need reassurance and key dates. Teachers need formality and academic justification. Never use the same tone for all three.

### 2. Purpose in Two Sentences
If the recipient can't identify the email's purpose in the first two sentences, the email is too long. Front-load the message. Details come after clarity.

### 3. Placeholders Are Promises
Every `[PLACEHOLDER]` is a commitment that the user must fulfill. Mark them clearly. Add notes explaining what belongs there. A template with ambiguous placeholders creates worse emails than no template at all.

### 4. Warmth Without Familiarity
Professional emails can be warm without being casual. Use names. Express genuine appreciation. Avoid corporate stiffness. But never cross into informality with parents or teachers — no slang, no emojis, no "Hey!"

### 5. Test Before Trusting
A template that hasn't been used is a hypothesis, not a tool. Every template must be field-tested with a real recipient. If it fails in the wild, revise it. The repo values working templates over complete ones.

### 6. Modular Over Monolithic
Templates should be easy to customize. Use clear sections. Mark optional paragraphs. Let users delete what doesn't apply. A rigid template will be abandoned; a flexible one will be adapted.

### 7. Completeness Beats Perfection
It's better to have a usable draft for every situation than a perfect template for one. Coverage first, polish second. Run this engine until all benchmarks are met, then refine.
