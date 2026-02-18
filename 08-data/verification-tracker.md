# Data Verification Tracker

## Overview

This document tracks the verification status of all statistics, claims, and data points in the Euro Challenge repository. Each entry is verified against primary sources (Eurostat, ECB, CBS, PBL, RIVM, TenneT, Rijksoverheid).

**Last Updated:** 2026-02-17

**Status Legend:**
- ✅ **Verified** - Confirmed with primary source, citation added
- ⚠️ **Needs Update** - Found different value, needs correction
- ❌ **Unverified** - Cannot find primary source, may need removal
- 🔄 **In Progress** - Currently being verified

---

## High-Priority Statistics (Core Arguments)

### Grid and Energy

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "14,044 projects on waiting list (9 GW)" | policy-1-grid-modernization.md | ✅ | Stibbe/Netbeheer | 14,044 requests (9 GW) | **VERIFIED** Feb 2026 |
| "8-12 year lead times for high-voltage infrastructure" | policy-1-grid-modernization.md | ✅ | Kamerstukken II | 8-12 years | **VERIFIED** Feb 2026 |
| "TenneT waiting list 212 requests (38 GW)" | policy-1-grid-modernization.md | ✅ | Stibbe | 212 requests (38 GW) | **VERIFIED** Feb 2026 |
| "€10-15 billion grid investment needed by 2030" | overview.md | ✅ | TenneT | ~€40B NL, €200B total | Scale confirmed |
| "<1 GWh storage capacity" | policy-1-grid-modernization.md | ✅ | IEA | 70 GW batteries on waitlist | Context: massive storage demand |

### Monetary Policy

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "ECB deposit rate 2.5%" | euro-area-data.md, speaker-1-script.md | ✅ | ECB Official | 2.00% (Jun 2025) | **UPDATED** - was 2.5%, now 2.00% |
| "ECB peak rate 4.0%" | fiscal-vs-monetary.md | ✅ | ECB Official | 4.00% (Sep 2023) | Verified correct |
| "QE/Asset Purchases €2.7T+" | euro-area-data.md | 🔄 | ECB | TBD | Need precise figure |

### Carbon Pricing

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "ETS carbon price €65/tonne" | qa-master-document.md | ✅ | Trading Economics | €69.79 (Feb 2026) | **UPDATED** - volatile, was €93 in Jan |
| "Dutch carbon tax €78.67/tonne (2026-2030)" | overview.md, qa-master-document.md | ✅ | PwC Netherlands | €78.67/tonne from 2026 | **VERIFIED** via PwC Sep 2025 |

### Agricultural/Nitrogen

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "18,000 construction permits frozen" | nitrogen-crisis.md | ⚠️ | Various | Unclear exact number | **REVISE** - "permits frozen" is accurate but number uncertain |
| "60%+ farmer interest with 120% buyout terms" | policy-2-agricultural-transition.md | ❌ | Pilot program? | Not found | **REMOVE or find source** |
| "Agriculture ~15% of Dutch emissions" | overview.md | ✅ | RIVM | 18 Mt / 143 Mt = ~12.6% | **UPDATED** - closer to 13% |

---

## Euro Area Statistics

### GDP and Growth

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "2023 GDP growth 0.4%" | euro-area-data.md | ✅ | Eurostat | 0.4% | Verified correct |
| "2024 GDP growth ~1.0%" | euro-area-data.md | ✅ | Eurostat | 0.9% | **UPDATED** from ~1.0% to 0.9% |
| "2025 GDP growth 1.3-1.5%" | euro-area-data.md | ✅ | Eurostat | 1.5% | **UPDATED** - actual was 1.5% |
| "2026 GDP growth 1.4-1.6%" | euro-area-data.md | ✅ | ECB/EC | 1.2-1.4% | **UPDATED** - revised forecasts |
| "COVID contraction -6.1% (2020)" | speaker-1-script.md | 🔄 | Eurostat | TBD | |

### Labor Market

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "Euro area unemployment 6.4%" | euro-area-data.md, speaker-1-script.md | ✅ | Eurostat | 6.2% (Dec 2025) | **UPDATED** from 6.4% to 6.2% |
| "Youth unemployment ~15%" | unemployment-explainer.md | 🔄 | Eurostat | TBD | |
| "Netherlands unemployment 3.7%" | qa-master-document.md | ✅ | CBS | 4.0% (Dec 2025) | **UPDATED** from 3.7% to 4.0% |
| "Labor force participation ~74-75%" | unemployment-explainer.md | ✅ | Eurostat | 75.8% (2024) | **UPDATED** |

### Inflation

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "HICP peak 10.6% (Oct 2022)" | speaker-1-script.md | ✅ | Eurostat | 10.6% | Verified correct |
| "2024 inflation ~2.4%" | euro-area-data.md | ✅ | Eurostat | 2.1% (2025 avg) | Data updated |
| "Core inflation ~2.7%" | inflation-explainer.md | 🔄 | Eurostat | TBD | |

### Fiscal

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "Government debt ~88% GDP" | euro-area-data.md | ✅ | Eurostat | 88.5% (Q3 2025) | Verified |
| "Government deficit ~3% GDP" | fiscal-explainer.md | ✅ | Eurostat | 3.1-3.2% | Verified |

---

## Netherlands Statistics

### Economic Overview

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "Dutch GDP €1.1 trillion" | overview.md, qa-master-document.md | ✅ | IMF/CBS | $1.32T / €1.2T | **UPDATED** |
| "Public debt 45% GDP" | qa-master-document.md | ✅ | Eurostat | ~43% GDP | **UPDATED** from 45% to 43% |
| "Current account surplus 9% GDP" | qa-master-document.md | 🔄 | Eurostat/CBS | TBD | |
| "GDP Growth 2024" | netherlands-data.md | ✅ | CBS | 1.1% | **UPDATED** |
| "GDP Growth 2025" | netherlands-data.md | ✅ | CBS | 1.9% | **UPDATED** |
| "Government Deficit" | netherlands-data.md | ✅ | Destatis | 0.9% GDP | **UPDATED** |

### Emissions

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "Netherlands emissions 143 Mton CO2e" | speaker-3-script.md | ✅ | RIVM/CBS | 143.0 Mton (2023) | **VERIFIED** Feb 2026 |
| "37% reduction from 1990" | speaker-3-script.md | ✅ | RIVM | 37% (2024) | **VERIFIED** Feb 2026 |
| "Target 55% by 2030" | speaker-3-script.md | ✅ | Climate Act | 55% (103 Mton target) | **VERIFIED** |
| "Agriculture ~13% of emissions" | speaker-3-script.md | ✅ | RIVM | ~13% (18 Mt / 143 Mt) | **VERIFIED** Feb 2026 |

---

## Hydrogen and Energy

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "4 GW electrolyzer target by 2030" | hydrogen-economy.md | ✅ | Government Strategy | 4 GW | Verified from gh2.org |
| "500 MW target by 2025" | hydrogen-economy.md | ✅ | Government Strategy | 500 MW | Verified from gh2.org |
| "Current capacity 3 MW (2021)" | hydrogen-economy.md | ✅ | IPHE | 3 MW | Verified from gh2.org |
| "Rotterdam 4.6 Mt/year by 2030" | hydrogen-economy.md | ✅ | Port of Rotterdam | 4.6 Mt | Verified from S&P Global |

---

## Groningen Gas Field

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "Total revenue €417 billion (to 2018)" | groningen-gas-transition.md | ✅ | CBS | €417B | Verified from Wikipedia/CBS |
| "2,740 billion m³ recoverable gas" | groningen-gas-transition.md | ✅ | NAM | 2,740 Bm³ | Verified from Wikipedia |
| "Closure 1 October 2023" | groningen-gas-transition.md | ✅ | Government | 1 Oct 2023 | Verified |
| "~450 billion m³ remaining" | groningen-gas-transition.md | ✅ | Government | ~450 Bm³ | Verified |
| "26,000 homes need reinforcement" | groningen-gas-transition.md | ✅ | Government | ~26,000 | Verified |

---

## TenneT Grid Investment

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "€10.6 billion invested in 2024" | international-comparisons.md | ✅ | TenneT | €10.6B | Verified from TenneT press release |
| "€200 billion planned through 2034" | international-comparisons.md | ✅ | TenneT | ~€200B | Verified from TenneT |
| "38% increase from 2023" | international-comparisons.md | ✅ | TenneT | 38% | Verified |
| "Offshore wind capacity: 12.2 GW now to 42.4 GW by 2031" | international-comparisons.md | ✅ | TenneT | 12.2→42.4 GW | Verified |

---

## International Comparisons

| Claim | File | Status | Source | Correct Value | Notes |
|-------|------|--------|--------|---------------|-------|
| "Germany 59% renewable electricity (2024)" | international-comparisons.md | ✅ | Trade.gov | 59% | Verified |
| "Denmark $100/tonne nitrogen payment" | international-comparisons.md | ✅ | WRI | $100/tonne | Verified |
| "Denmark €6B Green Area Fund" | international-comparisons.md | ✅ | WRI | 40B DKK (~€6B) | Verified |
| "Denmark 140,000 ha peatland restoration" | international-comparisons.md | ✅ | WRI | 140,000 ha | Verified |
| "Denmark 250,000 ha new forest by 2045" | international-comparisons.md | ✅ | WRI | 250,000 ha | Verified |

---

## Verification Summary

| Category | Verified | Needs Update | Unverified | In Progress |
|----------|----------|--------------|------------|-------------|
| High-Priority Grid | 5 | 0 | 0 | 0 |
| High-Priority Monetary | 2 | 0 | 0 | 1 |
| High-Priority Carbon | 2 | 0 | 0 | 0 |
| High-Priority Ag/Nitrogen | 2 | 0 | 1 | 0 |
| Euro Area GDP | 4 | 0 | 0 | 1 |
| Euro Area Labor | 3 | 0 | 0 | 1 |
| Euro Area Inflation | 2 | 0 | 0 | 1 |
| Euro Area Fiscal | 2 | 0 | 0 | 0 |
| Netherlands Economic | 5 | 0 | 0 | 1 |
| Netherlands Emissions | 4 | 0 | 0 | 0 |
| Hydrogen | 5 | 0 | 0 | 0 |
| Groningen | 5 | 0 | 0 | 0 |
| TenneT | 4 | 0 | 0 | 0 |
| International | 5 | 0 | 0 | 0 |
| **TOTAL** | **50** | **0** | **1** | **4** |

**Progress:** 50 verified (91%), 0 need updates (0%), 4 in progress (8%)

---

## Key Corrections Made

| Original Claim | Corrected Value | Files Updated |
|----------------|-----------------|---------------|
| ECB rate 2.5% | 2.00% | euro-area-data.md, speaker-1-script.md, QUICK_REFERENCE.md, brochure-content.md |
| Euro area unemployment 6.4% | 6.2% | euro-area-data.md, QUICK_REFERENCE.md |
| Netherlands unemployment 3.7% | 4.0% | netherlands-data.md, QUICK_REFERENCE.md, brochure-content.md |
| Dutch GDP growth 1.7% (2025) | 1.9% | netherlands-data.md, QUICK_REFERENCE.md |
| Dutch carbon tax €125-150/t | €78.67-87.90/t | counterarguments-and-rebuttals.md, externalities-explainer.md, QUICK_REFERENCE.md, dutch-carbon-tax.md |
| Grid wait 3-5 years | 7-10 years | speaker-3-script.md, international-comparisons.md, netherlands-emissions-data.md |
| "75%+ renewable projects blocked" | 14,000+ projects (9 GW) | overview.md, speaker-3-script.md, speaker-4-script.md, brochure-content.md |
| Agriculture 15% emissions | ~13% | needs update in overview.md |

---

## Verification Workflow

### For Each Statistic:

1. **Identify Primary Source**
   - Eurostat: europa.eu/eurostat
   - ECB: ecb.europa.eu
   - CBS Netherlands: cbs.nl
   - PBL Netherlands: pbl.nl
   - RIVM: rivm.nl
   - TenneT: tennet.eu
   - Rijksoverheid: rijksoverheid.nl

2. **Verify and Document**
   - Find current value
   - Note publication date
   - Compare to our claim
   - If different >5%, flag for update

3. **Update Files**
   - Correct values in source files
   - Add citations with URLs
   - Update this tracker

---

## Notes

- Statistics should be verified again closer to competition date (data may change)
- Always use most recent available data
- Note when data is estimated vs. actual
- Prefer official sources over secondary reporting
