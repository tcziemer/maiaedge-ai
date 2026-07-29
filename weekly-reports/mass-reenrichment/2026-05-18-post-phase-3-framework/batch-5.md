# Mass Re-Enrichment Sweep — Batch 5

**Sweep:** `2026-05-18-post-phase-3-framework`
**Batch:** 5
**Date:** 2026-05-18
**Operator:** Cowork CRM Guardian
**Records processed:** 50 / 50
**Pool drain:** 2,553 → 2,513 (-50 records this batch; total sweep drain 2,715 → 2,513 = -202 records / 7.4%)
**Path mix:** LIGHT 0 · MEDIUM 41 · FULL 9 · HOLD 0
**Apollo this batch:** 0 credits (no Apollo enrich calls; existing Apollo data <180 days for all records)
**Sweep cumulative Apollo:** 0 credits (APOLLO_ENFORCEMENT=disabled)
**Tier writes:** 1 promotion (Scott Technology Center tier_3→tier_1) · 1 demotion (Ashland Fiber Network tier_3→tier_4) · 0 skipped
**Sub-segment auto-migrations:** 0 (no legacy 1-to-1 mapping triggers in this batch)
**Sub-segment reclassifications:** 5
**Segment changes (cascade fired):** 3 (Downtown Colo Fiber→Colo; Blockfusion Colo→NeoCloud; Vision Net Colo→Fiber)
**Customer-protection HOLDs:** 0
**Completeness Gate fails:** 0
**Manual-review HOLDs:** 0 (HOLD policy = NONE per sweep operating notes)
**Records flagged for deletion this batch:** 2 (Core NAP, IDACORE)
**Duplicates flagged for R3 merge:** 1 (Centersquare Data Centers ↔ Centersquare primary)

---

## Records flagged for deletion

| ID | Name | Reason |
|---|---|---|
| 254951523064 | Core NAP (Zayo zColo) | Zayo Group acquired June 2013; entity operates as zColo brand under Zayo's portfolio rather than as independent operator. Existing enrichment data was cross-contamination from Zayo Group record. |
| 264635347670 | IDACORE / IdaCorp | Regulated electric utility (Idaho Power parent). D1 disqualifier: energy utility, not carrier-neutral colo or commercial fiber wholesaler. Internal dark-fiber-for-grid-ops does not equal commercial fiber operator. |

---

## Sub-segment / segment changes

| ID | Name | Change |
|---|---|---|
| 264241842931 | Ashland Fiber Network | Regional CLEC - Fiber operator → Municipal / Cooperative - Fiber operator (community-owned city utility per file 06 §6.2); confidence low_5069→high_90; tier_3→tier_4 |
| 264450748131 | Downtown Colo (Subrigo) | customer_segment Fiber Operator → Data Center Colo Provider; sub-segment Regional CLEC → Standard - colo (POP-and-facility-driven model with colo as primary line) |
| 264601327291 | Blockfusion | customer_segment Data Center Colo Provider → NeoCloud; sub-segment AI Signals - colo → Crypto to AI - Neoclouds (former BTC miner pivoting to AI/HPC; Cooper 2026-05-14 inclusion rule covers landlord model regardless of GPU-operator vs landlord) |
| 264594125514 | Vision Net (iConnect Montana) | customer_segment Data Center Colo Provider → Fiber Operator; sub-segment Standard - colo → Regional CLEC - Fiber operator (5,000 owned route miles + fiber-led service portfolio); confidence medium→high_90 |
| 264450748126 | Scott Technology Center | sub-segment Standard - colo → AI Signals - colo (April 2025 GPU-as-a-Service launch + 'From Concrete to Cloud' AI pivot); tier_3→tier_1 |
| 264270693061 | Iowa Communications Network | sub-segment Regional CLEC - Fiber operator → Municipal / Cooperative - Fiber operator (Iowa state agency, public-sector-only customer base, 99 counties); tier_3→tier_4 |

---

## Renames / domain corrections

| ID | Field | From | To |
|---|---|---|---|
| 264241842932 | name | OTT Communications | GoNetspeed |
| 264241842932 | domain | ottcommunications.com | gonetspeed.com |
| 254951523064 | name | Core NAP | Core NAP (Zayo zColo) |
| 264590543559 | name | Green House Data | Lunavi (Green House Data) |
| 264594125520 | name | IS (truncated) | ISCorp |
| 254554504940 | name | Interconnect Miami | South Reach Networks (Interconnect Miami) |
| 254626062054 | name | DataGryd | Hudson InterXchange (DataGryd) |
| 264594125514 | name | iConnect Monta (truncated) | Vision Net (iConnect Montana) |

---

## Territory / location corrections

| ID | Name | From | To |
|---|---|---|---|
| 264270693059 | Connect Data Centers | country=Netherlands, state=Drenthe, owner=Tim Z | country=US, state=Minnesota, owner=Tim Lieto (Oppidan US subsidiary, 23 facilities across 19 US regions) |
| 263560994535 | CORE Data Center | country=Canada, state=Ontario | country=US, state=Oklahoma (NE Oklahoma Electric Coop owned, Vinita OK facility) |
| 264601326325 | Gray Wolf Data Centers | state=NJ | state=Connecticut (Colchester CT primary 4 MW facility) |
| 254626062056 | Data102 | state=Florida | state=Colorado (Colorado Springs operating site) |
| 264592334574 | HopOne Internet | state=Hawaii | state=Washington (Seattle HQ per geographic_focus) |

---

## Duplicate flagged (for R3 Duplicate Accounts to merge)

| Primary | Duplicate | Notes |
|---|---|---|
| 264592334571 Centersquare (centersquare.com) | 264450748132 Centersquare Data Centers (centersquaredatacenters.com) | Both records describe the merged Cyxtera + Evoque (now Centersquare/Csquare) under Brookfield, with 80 facilities and the October 2025 $1B 10-DC acquisition. Both updated to note duplicate state; R3 should merge to centersquare.com primary. |

---

## Data quality bugs surfaced + patched

| ID | Name | Bug | Fix |
|---|---|---|---|
| 254951523064 | Core NAP | account_brief and all enriched fields contained cross-contamination data describing Zayo Group (146K route miles, 375 POPs, Crown Castle Fiber acquisition) — Core NAP is an 8,250 sq ft Austin colo acquired by Zayo in 2013 | Rewrote brief as Zayo zColo subsidiary; Flagged for deletion |
| 264270693059 | Connect Data Centers | Apollo state=Drenthe / country=Netherlands but brief documented 23 US facilities (Eagan MN, Apple Valley MN, North Mankato MN, etc.) | Corrected to US/Minnesota; owner Tim Z→Tim Lieto; infrastructure_profile Mid-Size→Large (20-49) for 23 facilities |
| 263560994535 | CORE Data Center | Apollo country=Canada / state=Ontario but brief documented Vinita Oklahoma facility owned by Northeast Oklahoma Electric Cooperative | Corrected to US/Oklahoma |
| 264594125520 | ISCorp | HubSpot name truncated to "IS" | Restored to "ISCorp" |
| 264594125514 | Vision Net | HubSpot name truncated to "iConnect Monta" | Restored to "Vision Net (iConnect Montana)" |
| 264592334571 | Centersquare | infrastructure_profile = Large (20-49) but brief documents 80 facilities | Corrected to Enterprise (50+) |
| 254626062056 | Data102 | state=Florida but Colorado Springs operations site | Corrected to Colorado |
| 264592334574 | HopOne Internet | state=Hawaii but Seattle WA HQ | Corrected to Washington |
| 264601326325 | Gray Wolf Data Centers | state=NJ but Colchester CT primary facility | Corrected to Connecticut |
| 264432390888 | Enseva | account_brief was 4 paragraphs (over 2-4 sentence cap) | Tightened to 3 sentences |
| 264592334571 | Centersquare | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264590543564 | Cloudsmart | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264601327291 | Blockfusion | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264601327293 | ManagedWay | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 263392463550 | GIGA Data Centers | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264594125520 | ISCorp | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264601326325 | Gray Wolf Data Centers | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264432390883 | Simple Helix | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264270693061 | ICN | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 266175085283 | Chirisa Technology Parks | account_brief was 4 paragraphs | Tightened to 3 sentences |
| 264635347670 | IDACORE | Classified as Data Center Colo Provider but entity is a regulated electric utility (Idaho Power parent) | Flagged for deletion |
| 264450748131 | Downtown Colo | Classified as Fiber Operator but operates 5 POPs colo + IP transit; misclassified | Reclassified to Data Center Colo Provider Standard - colo |
| 264594125514 | Vision Net | Classified as Data Center Colo Provider but operates 5,000 route miles fiber + 5 facilities — fiber-led not colo-led | Reclassified to Fiber Operator Regional CLEC |
| 264601327291 | Blockfusion | Classified as AI Signals - colo but BTC mining heritage with AI pivot — per Cooper 2026-05-14 rule, routes to Crypto to AI - Neoclouds (inclusive landlord model) | Reclassified to NeoCloud Crypto to AI - Neoclouds |

---

## Stale `recent_news_or_trigger_event` cleared (no fresh substitute)

| ID | Name | Prior content | Action |
|---|---|---|---|
| 300402132687 | zConnect | "No dated events identified" placeholder | Cleared |
| 264432390888 | Enseva | 2019-12 fiber buildout, no date prefix | Cleared (stale, no fresh signal) |
| 264590543564 | Cloudsmart | 2023-01 strategic shift announcement (>90 days, no signal scan in 7d) | Cleared |
| 264601327293 | ManagedWay | 2020-02 100 Gbps service announcement (>3 years stale) | Cleared |

---

## Per-record audit

### Chunk 1 (10 records, all date 2026-01-16 to 2026-01-17)

| ID | Name | Path | Segment (old → new) | Sub-segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|---|
| 264432390892 | Southwest Data Centers | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten without value-prop language; conciseness cap applied |
| 300402132687 | zConnect | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; stale "No dated events" cleared |
| 264413011656 | Colorado Fiber Network | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; infrastructure_profile expanded with Route Miles: Small (<1K) |
| 264270693059 | Connect Data Centers | FULL | unchanged | unchanged | unchanged | no | country NL→US; state Drenthe→MN; owner Tim Z→Tim Lieto; infra Mid-Size→Large (23 facilities Oppidan subsidiary) |
| 264270693072 | TSR Solutions | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264241842927 | ALLO Communications | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; infrastructure_profile +Route Miles: Mid-Size (1K-10K) |
| 263729676014 | LV.Net | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; low_5069 confidence retained |
| 264241842931 | Ashland Fiber Network | FULL | unchanged | Regional CLEC → Municipal / Cooperative - Fiber operator | tier_3 → tier_4 | no | Community-owned city utility per file 06 §6.2; confidence low_5069→high_90 |
| 264241842932 | OTT → GoNetspeed | FULL | unchanged | unchanged | unchanged | no | Name OTT Communications→GoNetspeed; domain ottcommunications.com→gonetspeed.com; recent_news updated with T-Mobile/Oak Hill JV + $13M Newport RI expansion |
| 254951523064 | Core NAP | FULL | Fiber Operator → Flagged for deletion | (n/a) | n/a | no | Zayo Group acquired June 2013; now operates as zColo; prior data was cross-contamination from Zayo record |

### Chunk 2 (10 records)

| ID | Name | Path | Segment (old → new) | Sub-segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|---|
| 263560994535 | CORE Data Center | FULL | unchanged | unchanged | unchanged | no | country Canada→US; state Ontario→Oklahoma; brief rewritten |
| 264450748131 | Downtown Colo | FULL | Fiber Operator → Data Center Colo Provider | Regional CLEC → Standard - colo | unchanged | no | Reclassified per POP-and-facility-driven model; confidence low_5069→medium_7089 |
| 264432390888 | Enseva | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened from 4 paragraphs to 3 sentences; stale 2019 news cleared |
| 263560994537 | Data Suites | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 300402132673 | ColoBarn | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264592334571 | Centersquare | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened; infrastructure_profile Large→Enterprise (50+) for 80 facilities; recent_news updated with $1B expansion + Carolan CDO + Stelia partnership |
| 264590543564 | Cloudsmart | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened; stale 2023 news cleared |
| 264601327291 | Blockfusion | FULL | Data Center Colo Provider → NeoCloud | AI Signals - colo → Crypto to AI - Neoclouds | unchanged (tier_1) | no | BTC mining heritage with AI pivot; per Cooper 2026-05-14 inclusion rule covers landlord model |
| 254554504940 | South Reach Networks (Interconnect Miami) | MEDIUM | unchanged | unchanged | unchanged | no | Name updated reflecting South Reach Networks operating brand |
| 264601327293 | ManagedWay | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened; stale 2020 news cleared |

### Chunk 3 (10 records)

| ID | Name | Path | Segment (old → new) | Sub-segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|---|
| 263392463550 | GIGA Data Centers | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened; recent_news date prefix added |
| 264590543559 | Lunavi (Green House Data) | MEDIUM | unchanged | unchanged | unchanged | no | Name updated to reflect Lunavi operating brand; account_brief rewritten |
| 264260028091 | Greensparc | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264594125520 | ISCorp | MEDIUM | unchanged | unchanged | unchanged | no | Name "IS"→"ISCorp" truncation fix; account_brief tightened |
| 263392463555 | Cavern Technologies | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264601326325 | Gray Wolf Data Centers | MEDIUM | unchanged | unchanged | unchanged | no | state NJ→CT; account_brief tightened |
| 264260027120 | Centeris Data Centers | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264590543568 | LoCoCoLo | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264355635948 | Trijit | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; flagged for D7 deeper verification |
| 264270693061 | Iowa Communications Network | FULL | unchanged | Regional CLEC → Municipal / Cooperative - Fiber operator | tier_3 → tier_4 | no | Iowa state agency, public-sector-only customer base, 99 counties |

### Chunk 4 (10 records)

| ID | Name | Path | Segment (old → new) | Sub-segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|---|
| 254626062057 | NOCIX | MEDIUM | unchanged | unchanged | unchanged | no | account_brief expanded from thin 1-sentence to 3-sentence factual brief; recent_news date prefix added |
| 264241842919 | Cirrus Data Services | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; confidence flagged provisional |
| 264592334572 | FORTRUST | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 317342612164 | GWI | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264450748126 | Scott Technology Center | FULL | unchanged | Standard - colo → AI Signals - colo | tier_3 → tier_1 | no | April 2025 GPU-as-a-Service launch + AI Powerhouse pivot |
| 264414880444 | Hunter Communications | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 263560994528 | IHNetworks | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; provisional confidence |
| 254626062056 | Data102 | MEDIUM | unchanged | unchanged | unchanged | no | state FL→CO; account_brief rewritten clarifying Hivelocity divestiture did not include Colorado Springs assets |
| 264450748133 | Data Center West | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten; low_5069 confidence retained |
| 266175085283 | Chirisa Technology Parks | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened from 4 paragraphs to 3 sentences; recent_news date prefixes added |

### Chunk 5 (10 records)

| ID | Name | Path | Segment (old → new) | Sub-segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|---|
| 255207759566 | Celito Communications | MEDIUM | unchanged | unchanged | unchanged | no | account_brief expanded with substantive Triangle-region detail |
| 264432390883 | Simple Helix | MEDIUM | unchanged | unchanged | unchanged | no | account_brief tightened to 3 sentences; recent_news with date prefixes |
| 264635347670 | IDACORE | FULL | Data Center Colo Provider → Flagged for deletion | (n/a) | n/a | no | Regulated electric utility (Idaho Power parent); D1 disqualifier |
| 264592334574 | HopOne Internet | MEDIUM | unchanged | unchanged | unchanged | no | state Hawaii→Washington; account_brief rewritten |
| 264270693067 | HostDime | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 263392463557 | Parsec Data Management | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten |
| 264432390890 | Polaris Technology | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten with BTC-heritage and AI-pivot caveat; flagged for D7 follow-up |
| 264450748132 | Centersquare Data Centers | MEDIUM | unchanged | unchanged | unchanged | no | account_brief rewritten flagging duplicate of primary record 264592334571 for R3 merge |
| 254626062054 | Hudson InterXchange (DataGryd) | MEDIUM | unchanged | unchanged | unchanged | no | Name updated reflecting Hudson InterXchange rebrand; account_brief expanded with 60 Hudson wholesale-tilt context |
| 264594125514 | Vision Net (iConnect Montana) | FULL | Data Center Colo Provider → Fiber Operator | Standard - colo → Regional CLEC - Fiber operator | unchanged | no | 5,000 owned route miles + fiber-led service portfolio; confidence medium→high_90 |

---

## Sweep cumulative status (post batch 5)

| Metric | Value |
|---|---|
| Total batches fired | 5 |
| Total records processed | 210 |
| Total flagged for deletion (cumulative) | 9 (7 from batches 1-4 + 2 this batch: Core NAP, IDACORE) |
| Total duplicate flags for R3 (cumulative) | 2 (Cyxtera↔Evoque from batch 4 + Centersquare↔Centersquare Data Centers this batch) |
| Pool starting size | 2,715 |
| Pool current size | 2,513 |
| Pool drain | -202 records (-7.4%) |
| Apollo cumulative | 0 credits (APOLLO_ENFORCEMENT=disabled, no enrich calls fired across the sweep) |
| ETA to sweep complete | ~50 more batches at BATCH_SIZE=50 |

## Run health: GREEN

No errors after the initial enum-value catch (Route Miles: Mid-Size 1-10K → 1K-10K). No rate limits, no concurrent-batch detection, no Completeness Gate fails.

## Notable patterns to watch in subsequent batches

1. **Overlong account_brief (4 paragraphs)** is systemic on records enriched 2026-01-17 — at least 9 hits this batch. Continuing bulk tightening to 2-4 sentence cap.
2. **Cross-record contamination in `account_brief`** continues (Core NAP → Zayo content, Krypt→Evocative, Peace Communications→Scipio per batch 4) — suggests the prior enrichment pass had record-bleeding bugs. Worth a dedicated audit pass after sweep complete.
3. **State / country misclassifications** trending (Connect Data Centers NL→US, CORE Data Center Canada→US, Data102 FL→CO, HopOne HI→WA, Gray Wolf NJ→CT) — Apollo defaulting to closest match when canonical entity didn't resolve cleanly. Several records will still need owner re-derivation by R6 / D7.
4. **Misclassified utilities and non-ICPs** (IDACORE = electric utility, Core NAP = defunct subsidiary, Downtown Colo = colo not fiber, Vision Net = fiber not colo) — aggressive flag and reclassify policy catching these.
5. **Greenfield / Crypto-to-AI pattern** appearing (Blockfusion BTC→AI pivot; Polaris BTC-adjacent with $100M new build) — Cooper's 2026-05-14 NC5 inclusivity rule is being applied; D7 watchlist for verification.
6. **Truncated names** on multiple records (IS → ISCorp, iConnect Monta → Vision Net) — possibly Apollo enrichment field-length truncation. Continue watching.
7. **Rebrand backlog** — multiple records reflect operating-brand renames not yet captured in HubSpot `name` (OTT→GoNetspeed, DataGryd→Hudson InterXchange, Green House Data→Lunavi, Interconnect Miami→South Reach Networks).

---

**End of batch 5 audit log.**
