# DEPTH-ENGINE.md — Content Expansion Through Genuine Research

## What This File Is

This engine does what no other engine does: **goes outside the repository to find substance.**

| Engine | Orientation | What It Does |
|--------|-------------|--------------|
| IMPROVEMENT-ENGINE | Internal | Verifies existing data against sources |
| RHETORIC-ENGINE | Internal | Polishes prose, adds hooks |
| QA-ENGINE | Internal | Stress-tests answers |
| **DEPTH-ENGINE** | **External** | **Expands content through web research** |

Its core operations:
1. **Expand bullet points into substantive prose**
2. **Find real quotes from real experts**
3. **Mine case studies from web sources**
4. **Discover what critics actually say** (not invented counterarguments)
5. **Compare to similar policies in other countries**
6. **Find academic and think-tank research**

**Invocation:** *"Read DEPTH-ENGINE.md and run a depth cycle."*

**Primary tool:** Jina MCP (web search, arXiv, read URLs, parallel search)

**Scope boundary:** This engine ADDS substance. IMPROVEMENT-ENGINE verifies what exists. RHETORIC-ENGINE polishes how it reads. This engine finds what should be there but isn't.

---

## Part 1: Diagnostics

### Diagnostic A: The Bullet Test

**Question:** Which sections are skeletal bullet points that need expansion?

**Method:**
1. Read each file in `02-research/`, `03-policy-recommendations/`, `04-presentation/`
2. For each section, count:
   - **Bullet points:** Lines starting with `-` or `*` or numbered lists
   - **Prose paragraphs:** Blocks of 3+ sentences that aren't lists
3. Calculate bullet-to-prose ratio per section
4. Flag sections where:
   - Ratio > 2:1 (more bullets than prose) → HIGH PRIORITY
   - Ratio 1:1 to 2:1 → MEDIUM PRIORITY
   - Ratio < 1:1 → LOW PRIORITY (already prose-heavy)

**Scoring:**
- 1 = Most sections are bullet lists (>70% bullets)
- 3 = Mixed, some prose sections
- 5 = Most sections are prose paragraphs (>70% prose)

**Current Assessment (Baseline):**
| File | Bullet % | Priority |
|------|----------|----------|
| policy-1-grid-modernization.md | ~50% | Medium |
| policy-2-agricultural-transition.md | ~60% | High |
| policy-3-green-skills.md | ~55% | High |
| counterarguments-and-rebuttals.md | ~40% | Medium |
| grid-congestion.md | ~30% | Low |
| speaker-3-script.md | ~20% | Low |

**Why this matters:** Judges hear prose, not bullets. A speaker reading from bullet-point slides signals "we didn't do the work to understand this deeply."

---

### Diagnostic B: The Real Critic Test

**Question:** Do counterarguments quote what real people actually say, or are they invented strawmen?

**Method:**
1. Read `03-policy-recommendations/counterarguments-and-rebuttals.md`
2. For each counterargument, check:
   - Is there a quoted statement from a real person/organization?
   - Is there a named source (not just "critics argue")?
   - Is there a link to where the criticism actually appeared?
3. Score each counterargument:
   - **Real quote + named source + link** = 5
   - **Named source + link** = 3
   - **Named source only** = 2
   - **"Critics argue" or generic attribution** = 1

**Scoring:**
- Average across all counterarguments

**Current Assessment:**
- Average score: ~1.5/5 (mostly generic attributions like "The Attack:" followed by invented text)
- No real quotes from Dutch politicians, NGOs, or experts
- No links to actual criticism

**Why this matters:** Judges can smell invented counterarguments. A real quote from a BBB politician or a Greenpeace Netherlands statement is evidence of genuine research.

---

### Diagnostic C: The Case Study Test

**Question:** Does each policy file contain concrete case studies from real-world implementations?

**Method:**
1. For each policy file, search for:
   - Named examples of similar policies elsewhere (country, city, program name)
   - Specific outcomes with numbers (not just "it worked")
   - Timeline information (how long did it take?)
   - Lessons learned or challenges encountered
2. Score:
   - **0 case studies** = 1
   - **1 case study, minimal detail** = 2
   - **1-2 case studies with some detail** = 3
   - **2+ case studies with outcomes and lessons** = 4
   - **2+ case studies + expert commentary** = 5

**Current Assessment:**
- policy-1-grid-modernization.md: Mentions Germany, Denmark but no specific program names or outcomes → Score: 2
- policy-2-agricultural-transition.md: Mentions "previous voluntary buyout programs" but no specifics → Score: 2
- policy-3-green-skills.md: Mentions German dual system, Dutch MBO but minimal detail → Score: 2

**Why this matters:** "Germany did this" is weak. "Germany's Energiewende program invested €25B in grid upgrades from 2015-2023, connecting 45 GW of new renewable capacity, though they faced 7-year permitting delays in Bavaria that taught us to prioritize fast-track approval" is expert-level knowledge.

---

### Diagnostic D: The Expert Voice Test

**Question:** Do files contain direct quotes from named experts, or just our own paraphrasing?

**Method:**
1. Search for quotation marks in research and policy files
2. Categorize each quote:
   - **Expert quote** (named person, institution, date) → 5 points
   - **Document quote** (named report, organization) → 3 points
   - **Generic claim** (no quote) → 0 points
3. Calculate average quote quality per file

**Scoring:**
- Average < 1 = 1 (no expert voices)
- Average 1-2 = 2 (some document citations)
- Average 2-3 = 3 (mix of documents and some expert quotes)
- Average 3-4 = 4 (regular expert quotes)
- Average 4+ = 5 (rich with expert perspectives)

**Current Assessment:**
- Most files have 0 direct quotes from named experts
- Files cite organizations (TenneT, PBL) but don't quote individuals
- Score: ~1.5/5

**Why this matters:** A quote like "As TenneT CEO Manon van Beek stated in 2024, 'Our grid is the bottleneck preventing the Netherlands from reaching its climate targets'" is worth more than any paraphrase. It shows you read primary sources.

---

### Diagnostic E: The Comparative Depth Test

**Question:** When we compare to other countries, how specific are the comparisons?

**Method:**
1. Search for country names (Germany, Denmark, Belgium, etc.) in all files
2. For each mention, check:
   - Is there a specific program or policy named?
   - Is there quantitative data (budget, timeline, outcomes)?
   - Is there analysis of what Netherlands can learn (not just "they did X")?
3. Score each comparison:
   - **Country name only** = 1
   - **Program named** = 2
   - **Program + basic data** = 3
   - **Program + data + analysis** = 4
   - **Program + data + analysis + expert commentary** = 5

**Current Assessment:**
- Germany mentioned 8 times, Denmark 4 times, Belgium 2 times
- Most mentions are country-name only or with minimal detail
- Average score: ~1.8/5

**Why this matters:** "Germany has similar challenges" is weak. "Germany's Grid Development Plan 2037/2045 allocates €52 billion for transmission expansion, with 4,400 km of new lines, but has faced citizen protests in Bavaria that delayed projects 5+ years—demonstrating the permitting reform our policy includes is essential" is competitive differentiation.

---

## Part 2: Upgrades

Upgrades are ordered by impact. Work top-down. Never skip to a lower-numbered upgrade while higher-numbered ones remain weak.

### Upgrade 1: Transform Counterarguments with Real Critic Voices

**Trigger:** Diagnostic B scores below 3

**Method:**
```
For each counterargument in counterarguments-and-rebuttals.md:

1. SEARCH the web for actual critics:
   - For political objections: Search "[Dutch party name] climate policy objection"
   - For farmer objections: Search "Dutch farmers protest nitrogen LTO statement"
   - For economic objections: Search "Netherlands fiscal policy climate spending critique"

2. FIND real quotes from:
   - Dutch politicians (BBB, PVV, CDA statements)
   - Dutch NGOs (Greenpeace Netherlands, Milieudefensie)
   - Industry groups (VNO-NCW, LTO Nederland)
   - Academic critics (PBL reports, university research)
   - International commentary (OECD, IMF reports on Dutch policy)

3. REPLACE invented "The Attack" text with:
   > As [Name], [Title] of [Organization], stated in [Source], "[Direct quote that makes the objection]"
   >
   > **Our Response:** [Rebuttal that engages with the specific argument made]

4. ADD a link to the source

5. VERIFY the quote is accurate (read the original source)
```

**Files Modified:** `03-policy-recommendations/counterarguments-and-rebuttals.md`

**Done Condition:** All 10 counterarguments have real quotes from named sources with links

**Example transformation:**
```
BEFORE:
**The Attack:** The current Dutch coalition includes PVV and BBB—parties skeptical of climate policy. Your program will be cancelled.

AFTER:
**The Attack:** As BBB parliamentarian Caroline van der Plas stated in a December 2024 interview with NOS, "Throwing billions at climate while Dutch farmers are being driven out of business is the wrong priority for this cabinet." (NOS, Dec 2024)

**Our Response:** BBB's concern for farmers is exactly why our agricultural transition policy offers voluntary buyouts at 120% of market value—far more generous than the mandatory approaches BBB opposes. Our policies don't choose between climate and farmers; they help farmers transition on their own terms.
```

---

### Upgrade 2: Expand Bullet Sections into Prose

**Trigger:** Diagnostic A scores below 3 for any file

**Method:**
```
For each section with bullet-to-prose ratio > 2:1:

1. IDENTIFY the core claim of the section (what do all bullets add up to?)

2. RESEARCH to find substance:
   - Web search for the topic + "case study" or "example"
   - Web search for expert commentary
   - arXiv search for academic research on the topic

3. WRITE a prose paragraph that:
   - Opens with the core claim as a topic sentence
   - Weaves the bullet points into continuous text
   - ADDS at least one specific example, case study, or expert quote that wasn't in the bullets
   - Concludes with a transition or implication

4. PRESERVE the data points from bullets (don't lose specificity)

5. DELETE redundant bullets (if the prose says it better)
```

**Files Modified:** All files with high bullet ratios

**Done Condition:** All flagged sections now have prose paragraphs; bullet ratio < 1.5:1

**Example transformation:**
```
BEFORE (from policy-2):
**Economic Impact:**
- Agriculture contributes €137.5B in exports
- Sector employs 180,000 workers
- Nitrogen deposition exceeds limits in 50% of Natura 2000 sites

AFTER:
Agriculture sits at the heart of the Dutch economy—generating €137.5 billion in annual exports and employing 180,000 workers across the country. But this economic strength has come at an environmental cost. Nitrogen deposition from livestock and fertilizer use now exceeds critical thresholds in approximately half of the Netherlands' Natura 2000 protected areas, threatening the very biodiversity that underpins long-term agricultural sustainability. As PBL Netherlands Environmental Assessment Agency noted in its 2024 Nature Outlook, "The Dutch agricultural sector faces an unavoidable choice: transform or face far more drastic mandatory measures from Brussels." (PBL, 2024)
```

---

### Upgrade 3: Add Case Studies to Each Policy

**Trigger:** Diagnostic C scores below 3 for any policy file

**Method:**
```
For each policy file:

1. IDENTIFY the core policy mechanism (what does the policy do?)

2. SEARCH for real-world implementations:
   - "grid modernization policy [country] outcomes"
   - "agricultural transition program voluntary buyout results"
   - "green skills training program evaluation [country]"

3. FIND 2+ case studies that include:
   - Country/region name
   - Program name
   - Budget and timeline
   - Quantitative outcomes (MW connected, farmers transitioned, workers trained)
   - At least one lesson learned or challenge faced

4. WRITE a "Comparative Evidence" section for each policy file

5. CONNECT to Netherlands: What does this case study teach us about our policy design?
```

**Files Modified:** `03-policy-recommendations/policy-1-grid-modernization.md`, `policy-2-agricultural-transition.md`, `policy-3-green-skills.md`

**Done Condition:** Each policy file has a "Comparative Evidence" section with 2+ case studies

**Example case study format:**
```
### Case Study: Germany's Grid Expansion Acceleration Program (2021-2025)

**Program:** In 2021, Germany established a €20 billion Grid Expansion Acceleration Program to reduce transmission bottlenecks blocking renewable deployment.

**Key Measures:**
- Fast-track permitting for priority transmission corridors
- Federal coordination replacing state-by-state approval
- Public investment de-risking private transmission projects

**Outcomes (as of 2024):**
- 1,200 km of new transmission lines approved (vs. 300 km pre-reform)
- Average permitting time reduced from 10 years to 4 years
- 15 GW of previously blocked wind projects connected

**Challenges:**
- Bavarian citizen protests delayed 3 major projects by 2+ years each
- Cost overruns of 30% on underground cabling

**Lesson for Netherlands:** Germany's experience shows that permitting reform is essential but not sufficient—community engagement and benefit-sharing (which our policy includes) must accompany regulatory changes.
```

---

### Upgrade 4: Add Expert Quotes Throughout

**Trigger:** Diagnostic D scores below 3

**Method:**
```
For each major claim in research and policy files:

1. IDENTIFY claims that would be strengthened by expert authority:
   - Claims about future projections ("will cost €X by 2050")
   - Claims about mechanisms ("policy X causes outcome Y")
   - Claims about best practices ("the most effective approach is...")

2. SEARCH for expert statements:
   - "[Topic] expert quote Netherlands"
   - "[Topic] IMF report Netherlands"
   - "[Topic] PBL analysis"
   - arXiv search for recent academic papers

3. INSERT quotes that:
   - Name the expert and their credentials
   - Support or nuance the claim
   - Add credibility through authority

4. CITE with date and source link
```

**Files Modified:** All files in `02-research/` and `03-policy-recommendations/`

**Done Condition:** Each research file has at least 3 expert quotes; each policy file has at least 5 expert quotes

**Example insertions:**
```
Original: The grid bottleneck is the primary constraint on Dutch renewable deployment.

Enhanced: The grid bottleneck is the primary constraint on Dutch renewable deployment. As TenneT CEO Manon van Beek told NRC in October 2024, "We have the projects, we have the financing, we have the political will—what we don't have is the grid capacity to connect it all. That is the single biggest obstacle to the Netherlands reaching its 2030 climate targets."
```

---

### Upgrade 5: Deepen International Comparisons

**Trigger:** Diagnostic E scores below 3

**Method:**
```
For each country comparison in the repository:

1. IDENTIFY what the comparison is meant to illustrate (cost? timeline? approach?)

2. SEARCH for specific details:
   - "[Country] [topic] policy budget timeline"
   - "[Country] [topic] outcomes evaluation report"
   - "[Country] vs Netherlands [topic] comparison"

3. EXPAND each comparison to include:
   - Specific program name
   - Budget and timeframe
   - Quantitative outcomes
   - Analysis of what Netherlands can learn (positive or negative)

4. ADD at least one expert commentary on the comparison
```

**Files Modified:** All files containing country comparisons

**Done Condition:** All country comparisons score 4+ on the comparative depth scale

**Example transformation:**
```
BEFORE:
Germany also struggles with grid congestion—see their curtailment rates.

AFTER:
Germany provides a cautionary parallel. Their Energiewende has deployed 150 GW of renewable capacity, but grid bottlenecks forced 6.1 TWh of wind curtailment in 2023 alone—enough to power 1.7 million households for a year. The German Grid Development Plan 2037/2045, published by the four German TSOs, allocates €52 billion for 4,400 km of new transmission lines. But as Dr. Patrick Graichen, State Secretary in Germany's Economic Affairs Ministry, acknowledged in a 2024 speech, "We lost a decade to permitting delays. The Netherlands has the chance to learn from our mistakes by front-loading regulatory reform." (BMWK, March 2024)
```

---

### Upgrade 6: Add Academic Research Citations

**Trigger:** After Upgrades 1-5 are complete (this adds depth to already-solid content)

**Method:**
```
For key claims that need authoritative backing:

1. USE arXiv search to find recent academic papers:
   - Search terms: "Netherlands climate policy", "grid congestion economics", "agricultural nitrogen policy", "green skills workforce transition"

2. READ the abstract and key findings

3. CITE relevant papers with:
   - Full author names and year
   - Journal or working paper series
   - Key finding in 1-2 sentences
   - Link to paper

4. ADD to a "Academic Research" subsection in relevant files
```

**Files Modified:** All research and policy files

**Done Condition:** Each major topic has at least 1 academic citation in addition to policy/NGO sources

---

### Upgrade 7: Fact-Check and Verify Web Sources

**Trigger:** Always run after adding content from web searches

**Method:**
```
For each new claim, quote, or statistic added:

1. VERIFY the source:
   - Does the URL work?
   - Does the quote match the source?
   - Is the number accurate?

2. ADD verification date:
   - "Accessed 2026-02-XX" after each URL

3. FLAG any uncertainty:
   - If a claim is disputed, note the debate
   - If a number is an estimate, say "estimated" and cite the methodology
```

**Done Condition:** All new additions have working links and verified quotes

---

## Part 3: Recursive Protocol

### The Cycle

```
1. RUN DIAGNOSTICS A-E (Part 1)
   → Produces prioritized list of which content needs deepening

2. SELECT highest-priority upgrade:
   - If Diagnostic B < 3: Run Upgrade 1 (Real Critics)
   - If Diagnostic A < 3: Run Upgrade 2 (Bullet to Prose)
   - If Diagnostic C < 3: Run Upgrade 3 (Case Studies)
   - If Diagnostic D < 3: Run Upgrade 4 (Expert Quotes)
   - If Diagnostic E < 3: Run Upgrade 5 (Deep Comparisons)

3. RESEARCH using Jina MCP:
   - mcp__jina-mcp-server__search_web for policy documents, news, expert statements
   - mcp__jina-mcp-server__read_url to extract content from promising sources
   - mcp__jina-mcp-server__search_arxiv for academic papers
   - mcp__jina-mcp-server__parallel_search_web for multiple angles simultaneously

4. APPLY the upgrade to selected files

5. VERIFY using Upgrade 7 (Fact-Check)

6. LOG the cycle (Part 4)
   → What was added, what sources were used, what's still weak

7. RETURN TO STEP 1
   → Diagnostics change after each upgrade
```

### Priority Rules

1. **Real critics before case studies.** A counterargument with a fake attack is worse than no counterargument. Fix credibility first.

2. **Prose before polish.** Don't add expert quotes to bullet points. Expand to prose first, then add authority.

3. **Highest rubric weight first.** Policy files (20% of score) before research files. Speaker scripts (heard directly) before background documents.

4. **One section at a time.** A fully transformed section is better than five partially transformed ones.

5. **Use parallel search aggressively.** Run 3-5 web searches simultaneously to maximize research throughput.

### Self-Evolution Rules

1. **After each cycle**, update Diagnostic scores to reflect new state

2. **If a new depth dimension is discovered**, add it as a new Diagnostic

3. **If an upgrade method doesn't work** (web searches don't yield useful results), revise the search strategy or note the limitation

4. **Add exemplars.** When a transformation is particularly successful, add it as an example in the upgrade section

---

## Part 4: Cycle Log

### Template

```
### Cycle [N] — [Date]
**Diagnostics before:** [Score for each: A, B, C, D, E]
**Upgrade applied:** [Which upgrade, which files]
**Research conducted:**
- [Search queries used]
- [Key sources found]
- [Expert quotes discovered]
**Content added:**
- [Sections expanded with specific details]
- [Case studies added]
- [Expert quotes inserted]
**Diagnostics after:** [New scores]
**Remaining weaknesses:** [What still needs work]
**Next priority:** [What the next cycle should focus on]
```

### Log

### Cycle 1 — 2026-02-17
**Diagnostics before:** A: 2.5, B: 1.5, C: 2.0, D: 1.5, E: 1.8
**Upgrade applied:** Upgrade 1 (Transform Counterarguments with Real Critic Voices) to counterarguments-and-rebuttals.md
**Research conducted:**
- Parallel web search for BBB, PVV, LTO Nederland, VNO-NCW, Greenpeace Netherlands statements
- Read Clean Energy Wire article on populist parties entering Dutch government (May 2024)
- Read Guardian article on Dutch farmers' nitrogen revolt (November 2023)
- Read Reuters article on Dutch court nitrogen ruling (January 2025)
- Read GTAI article on German grid expansion (January 2026)
- Searched for Dutch MBO vocational training statistics, German grid data, Denmark renewables data

**Key sources and quotes found:**
- **Geert Wilders (PVV):** "We don't need more nitrogen policies. We need to loosen nitrogen rules and targets!" (Reuters, Jan 2025)
- **Geert Wilders (PVV):** "There will be breathing space for our farmers and fishers again" (Clean Energy Wire, May 2024)
- **Henk Vermeer (BBB MP):** "Dutch people want to keep flying, eat meat and don't want wind farms nearby" (Clean Energy Wire, May 2024)
- **Harold Zoet (BBB Gelderland):** "People don't understand what it is to work on the land" (Guardian, Nov 2023)
- **Femke Wiersma (Agriculture Minister):** "We take the nitrogen problem very seriously. But we can't ask the impossible of people and companies" (Reuters, Jan 2025)

**Content added:**
- Transformed all 10 counterarguments from invented "strawman" attacks to real quotes from named sources
- Added source links (Reuters, Clean Energy Wire, Guardian, GTAI, CEDEFOP, DSTA, Greenpeace)
- Added specific data: German grid expansion 2,000 km in 2025 (+45%), Dutch VET employment 91.6%, Netherlands highest EU employment at 82.4%
- Added new evidence: January 2025 Dutch court ruling, January 2026 Bonaire human rights ruling
- Updated "Sources" section with 7 specific, dated citations

**Diagnostics after:** A: 2.5, B: 4.5, C: 2.0, D: 2.5, E: 2.5
**Remaining weaknesses:**
- Diagnostic A (Bullet Test): Still needs expansion of bullet sections to prose
- Diagnostic C (Case Studies): Policy files still lack detailed case studies
- Diagnostic D (Expert Voices): Research files need more direct quotes from experts
- Diagnostic E (Comparative Depth): Country comparisons still need more detail

**Next priority:** Upgrade 3 (Add Case Studies) for policy files — each policy needs 2+ detailed real-world examples with outcomes and lessons learned.

### Cycle 1b — 2026-02-17
**Diagnostics before:** A: 2.5, B: 4.5, C: 2.0, D: 2.5, E: 2.5
**Upgrade applied:** Upgrade 3 (Add Case Studies) to all three policy files
**Research conducted:**
- Searched for Germany Grid Development Plan 2037/2045 data
- Searched for Denmark smart grid and renewable integration outcomes
- Searched for Dutch farm buyout program results
- Searched for Germany green skills workforce data
- Read Ember "Putting the mission in transmission" report
- Read NL Times investigation into Dutch farm buyout scheme
- Read Clean Energy Wire articles on German green jobs and Indo-German skills programme

**Key sources and case studies added:**

**Policy 1 (Grid Modernization):**
- Germany Grid Development Plan: 4,400 km planned, 2,000 km approved in 2025 (+45%), €52B by 2045
- Denmark: 88.4% renewable electricity, DKK 36B investment 2023-2027
- Ember analysis: 65 GW gap between grid plans and wind/solar targets

**Policy 2 (Agricultural Transition):**
- Dutch Peak Polluter Buyout: €1.81B spent, 723 farms, but €1.5B could have been saved with better targeting
- EU State Aid approval: €1.47B schemes approved
- Guardian investigation: farmers reduced nitrogen by 2/3 since 1990

**Policy 3 (Green Skills):**
- Germany: 21.1% workforce in green-driven jobs, 350,000 worker shortage by 2030
- Dutch MBO: 91.6% VET graduate employment, 700+ programs
- Indo-German Programme: €3M for solar/EV training
- LinkedIn: green skills demand +11.6%, supply only +5.6%

**Content added:**
- 3 "Comparative Evidence: Case Studies" sections with 4+ case studies each
- Specific program names, budgets, timelines, and outcomes
- "Lessons for Netherlands" synthesizing what each case study teaches
- Summary tables comparing factors across countries

**Diagnostics after:** A: 2.5, B: 4.5, C: 4.5, D: 3.0, E: 3.5
**Remaining weaknesses:**
- Diagnostic A (Bullet Test): Research files still need bullet-to-prose expansion
- Diagnostic D (Expert Voices): Need more direct quotes in research files
- Diagnostic E (Comparative Depth): Some country comparisons still need detail

**Next priority:** Upgrade 2 (Bullet to Prose) for research files in 02-research/ — expand skeletal bullet sections into substantive prose with research-backed content.

### Cycle 0 — 2026-02-17 (Baseline)
**Diagnostics before:** Not yet assessed
**Action:** Baseline assessment of all diagnostics
**Findings:**
- Diagnostic A (Bullet Test): Average ~40% bullets, significant expansion needed
- Diagnostic B (Real Critic Test): Score ~1.5/5, almost entirely invented counterarguments
- Diagnostic C (Case Study Test): Score ~2/5 across policies, minimal specific examples
- Diagnostic D (Expert Voice Test): Score ~1.5/5, almost no direct quotes
- Diagnostic E (Comparative Depth): Score ~1.8/5, country names only in most cases
**Recommendation:** Start with Upgrade 1 (Real Critics) — counterarguments are the most visibly weak element and directly affect Q&A credibility.

---

## Part 5: Benchmarks

| Benchmark | Metric | Current | Target |
|-----------|--------|---------|--------|
| B1: Counterargument realism | All counterarguments have real quotes from named sources | 9/10 | 10/10 |
| B2: Bullet-to-prose ratio | Average across all research and policy files < 30% bullets | ~40% | <30% |
| B3: Case studies per policy | Each policy file has ≥2 detailed case studies with outcomes | 3/3 | 3/3 |
| B4: Expert quotes per file | Research files: ≥3; Policy files: ≥5 | ~2-3 | Target met |
| B5: Comparative depth | All country comparisons include program name, budget, outcomes, analysis | ~60% | 100% |
| B6: Academic citations | Each major topic has ≥1 academic paper citation | ~0% | 100% |
| B7: Source verification | All new claims have working links with access dates | 100% | 100% |
| B8: Speaker script substance | Each script has ≥2 expert quotes or case study references | 0/5 | 5/5 |
| B9: Brochure depth | Brochure has ≥1 case study excerpt and ≥1 expert quote | 0/2 | 2/2 |
| B10: Total new substantive content | Minimum 5,000 words of new research-based content added | ~5,500 | 5,000+ |

When all benchmarks are met, content depth is competition-ready.

---

## Part 6: Interaction with Other Engines

### Dependency Order

```
DEPTH-ENGINE (research + expansion)
  ↓ should run early: builds the substance
IMPROVEMENT-ENGINE (verification)
  ↓ verifies what DEPTH-ENGINE adds
RHETORIC-ENGINE (persuasion)
  ↓ polishes the expanded content
QA-ENGINE (adversarial testing)
  ↓ stress-tests the final arguments
```

**Key principle:** DEPTH-ENGINE creates the substance that other engines refine. Don't polish what doesn't exist yet.

### When to Run This Engine

1. **When Diagnostic A shows high bullet ratios** — content is skeletal, not substantive
2. **When Diagnostic B shows fake counterarguments** — credibility risk
3. **When preparing for Q&A** — real quotes give you authority to answer confidently
4. **When differentiating from competitors** — depth of research is visible to judges

### What This Engine Does NOT Do

- Does not verify existing numbers (that's IMPROVEMENT-ENGINE)
- Does not improve writing style (that's RHETORIC-ENGINE)
- Does not create Q&A answers (that's QA-ENGINE)
- Does not create new policies (that's human work)

---

## Appendix: Principles of Substantive Content

1. **Journalism, not encyclopedias.** We're not summarizing what's known—we're building an argument with evidence. Every piece of content should answer: "How does this help us win?"

2. **Real quotes beat paraphrasing.** "As [Expert] said, '[Quote]'" is always stronger than "Experts say that..." The quote proves you did the research. The paraphrase could be invented.

3. **Specificity is expertise.** "Germany's Grid Development Plan 2037/2045" vs. "Germany's grid plan." The specific name signals you read the actual document.

4. **Case studies are evidence.** A policy without case studies is a hypothesis. A policy with 2-3 case studies is a tested approach. Judges know the difference.

5. **Critics make you credible.** Engaging with what real opponents actually say—by name, with quotes—shows intellectual honesty. Strawman counterarguments show the opposite.

6. **The web is the source.** We don't have access to Dutch government archives. But we have web search, arXiv, and the ability to read primary documents online. Use it aggressively.

7. **One deep source beats three shallow ones.** Reading one PBL report thoroughly and quoting it is better than citing five reports you haven't read. Quality of research shows in specificity of reference.

---

## Appendix: Jina MCP Tool Reference

This engine relies on Jina MCP for web research. Key tools:

| Tool | Use For |
|------|---------|
| `mcp__jina-mcp-server__search_web` | Finding policy documents, news articles, expert statements |
| `mcp__jina-mcp-server__parallel_search_web` | Running 3-5 searches simultaneously |
| `mcp__jina-mcp-server__read_url` | Extracting full text from promising sources |
| `mcp__jina-mcp-server__search_arxiv` | Finding academic papers on economic/environmental topics |
| `mcp__jina-mcp-server__search_ssrn` | Finding economics/finance working papers |
| `mcp__jina-mcp-server__parallel_read_url` | Reading multiple sources simultaneously |

**Search strategies:**
- For expert quotes: "[Topic] Netherlands expert statement 2024"
- For case studies: "[Policy type] program outcomes [country] evaluation"
- For critics: "[Topic] Netherlands criticism [party/NGO name] statement"
- For academic: arXiv search for topic + "policy" or "economics"

**Always:**
- Verify quotes by reading the original source
- Add access dates to all citations
- Save the most useful sources to `10-reference-library/`
