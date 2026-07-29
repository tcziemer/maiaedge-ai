# Mass Re-Enrichment Sweep — Batch 6

**Sweep:** 2026-05-18-post-phase-3-framework
**Kickoff:** 2026-05-18
**Batch:** 6
**Date:** 2026-05-18
**Records processed:** 50/50
**Apollo this batch:** 0 credits (Apollo not invoked; existing field data sufficient)
**Pool at start of batch:** 2,513 records
**Pool at end of batch:** ~2,455 records
**Cumulative sweep drain:** ~268 / 2,723 records (9.8%)

## Path mix

- LIGHT: 0
- MEDIUM: 43
- FULL (sub-segment reclassification or major rework): 7
- HOLD: 0
- Flagged for deletion: 4

## Notable framework-driven changes

- **Sub-segment reclassifications (7):**
  - COPT Data Centers: Standard - colo → Hyperscale Wholesale - colo (federal build-to-suit pattern matches hyperscale wholesale anchor model)
  - FNTS: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP (Tier IV DC + IBM Cloud/Azure integrations + mainframe = hybrid pattern, not pure aggregator)
  - IPXON Networks: Regional CLEC - Fiber operator → Tier 2 National Wholesale - Fiber operator (20+ LatAm POPs is regional wholesale, not US CLEC)
  - Dynascale: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP (private/hybrid cloud + colo focus, multi-DC footprint)
  - 165 Halsey Street: Standard - colo → AI Signals - colo (1.2M sqft carrier hotel + 40k sqft AI buildout + Megaport fabric)
  - Archer Datacenters: Standard - colo → Greenfield (120 MW Faribault MN campus development, pre-operational)
  - nGenX: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP (DaaS/IaaS cloud-first model)
- **Parent segment change (1):**
  - Far North Digital: Fiber Operator → Network Operator(Tier 1 / VNO); sub-segment Long Haul / Backbone → Subsea cable operator (pan-Arctic submarine cable project; pre-operational, anchor verification pending at low_5069)

## Flagged for deletion (4)

- **ColoSpace** (254561398507) — Acquired by FirstLight 2019-12, ceased independent operations
- **ByteGrid** (264601326324) — Defunct portfolio absorbed by Lincoln Rackhouse 2019-03, three facilities then acquired by DataBank 2020-12
- **Merkle Standard** (264432390882) — Pure BTC mining hosting operator (no AI pivot evidence); was misclassified as AI Signals - colo at tier_1 — corrected to Flagged for deletion since they sit outside ICP scope
- **Agile Data Sites** (254561398518) — Acquired by DataBridge Sites in 2020 and integrated into DataBridge portfolio

## Apollo data quality patterns observed

- **State misclassifications (3 corrections):**
  - Bestline Communications: state PA → Texas (HQ Austin per brief)
  - CVM Inc.: state IL → Connecticut (HQ Branford per brief)
  - nGenX: state NV → Kansas (HQ Overland Park per brief)
- **Owner re-derive (1):** Bestline Communications hubspot_owner_id 161889085 (Tim Lieto East) → 162339176 (Ken Cunningham West) post-state correction to Texas
- **Employee count anomalies:** Bay Pointe Tech Services shows 23,061 employees — clearly Apollo entity confusion. Not corrected this batch (no authoritative source); flagged for D7 review.

## Tier writes

Promotions toward T1: 2 (COPT Data Centers T3→T1, 165 Halsey Street T3→T1)
Other movements: Archer T3→T2 (Greenfield default), IPXON T3→T2 (Tier 2 National Wholesale default)
Skipped (hs_is_target_account=true): 0
Unchanged: 46

## Systemic patterns reinforced from prior batches

- 4-paragraph overlong `account_brief` is universal across the 2026-01-17 enriched cohort. Bulk tightening to 2-4 sentences continues.
- Marketing copy bleed in `account_brief` ("MaiaEdge offers...", "strong fit for MaiaEdge...") is universal in MSP/Aggregator and small colo records. Stripped on every record.
- `recent_news_or_trigger_event` frequently missing date prefix `[YYYY-MM-DD]`. Added on every write.
- "No dated announcements found in research." placeholder text appearing as paragraph 3 of long briefs — removed.
- "Research needed." placeholder in `provisioning_landscape` (DataBridge Sites, Agile Data Sites) — filled.

## Records

### Lifeline Data Centers (254626062048)
- Path: MEDIUM | Segment: unchanged | Sub-segment: unchanged | Tier: tier_3 unchanged
- Tightened brief 4 paragraphs → 3 sentences. Added [2025-06] date prefix to CMMC Level 2 news.

### ColoCenters (254951524030)
- Path: MEDIUM | Segment: unchanged | Sub-segment: unchanged | Tier: tier_3 unchanged
- Tightened brief, standardized geographic_focus format.

### COPT Data Centers (255207759559)
- Path: FULL | Sub-segment: Standard - colo → Hyperscale Wholesale - colo (medium_7089)
- Tier: tier_3 → tier_1 (default for Hyperscale Wholesale - colo)
- Fixed infrastructure_profile: "Facilities: Enterprise (50+)" → "Facilities: Large (20-49)" (31 facilities)

### IC2NET (263772808933)
- Path: MEDIUM | Segment: unchanged | Sub-segment: unchanged | Tier: tier_3 unchanged
- Tightened brief, removed marketing bleed.

### ColoSpace (254561398507)
- Path: FULL | Segment: Data Center Colo Provider → Flagged for deletion
- Defunct (acquired by FirstLight 2019-12).

### Fibernet (254561398517)
- Path: MEDIUM | Segment: unchanged | Sub-segment: unchanged | Tier: tier_3 unchanged
- Tightened brief, removed marketing bleed.

### Wholesale Internet (254566823656)
- Path: MEDIUM | Segment: unchanged | Sub-segment: unchanged | Tier: tier_3 unchanged
- Tightened brief, removed "No dated announcements" placeholder.

### Data Foundry (254565004006)
- Path: MEDIUM | Segment: unchanged | Sub-segment: unchanged | Tier: tier_3 unchanged
- Acknowledged Switch DOCK ownership in brief and recent_news. R3 dedup candidate.

### 165 Halsey Street (254566823657)
- Path: FULL | Sub-segment: Standard - colo → AI Signals - colo (high_90)
- Tier: tier_3 → tier_1 (default for AI Signals - colo; 40k sqft AI buildout + Megaport fabric)
- Updated infrastructure_profile to include POPs: Large (50-99) (60+ networks)
- Cleared stale recent_news (July 2024 = 22 months old).
- NOTE: Initial write failed on invalid POPs band "Large (50+)"; correct enum is "Large (50-99)".

### ByteGrid (264601326324)
- Path: FULL | Segment: Data Center Colo Provider → Flagged for deletion
- Defunct (acquired by Lincoln Rackhouse 2019-03; DataBank acquired 3 facilities 2020-12).

### GigeNET (254541933252)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief, removed "No dated announcements" placeholder.

### FNTS (264588752580)
- Path: FULL | Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Tier: tier_2 unchanged (default for new sub-segment also T2)
- Added [2025-12-10] date prefix to recent_news.

### IPXON Networks (264270693062)
- Path: FULL | Sub-segment: Regional CLEC - Fiber operator → Tier 2 National Wholesale - Fiber operator
- Tier: tier_3 → tier_2 (default for new sub-segment)
- Expanded too-short brief; flagged LatAm regional scope.

### Southwest Cyberport (254541933253)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief, removed marketing bleed.

### Dynascale (254549120743)
- Path: FULL | Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Tier: tier_2 unchanged
- Added [2025-12-12] date prefix to rebrand news.

### ISOMEDIA (254554504939)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief, removed marketing bleed.

### Fiberhub (254570392304)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief; filled "Not found" geographic_focus to "HQ: Las Vegas, Nevada. National US service reach via aggregated carriers."

### TulsaConnect (254566823658)
- Path: MEDIUM | Tier: tier_2 unchanged
- Fixed infrastructure_profile: "POPs: Enterprise (100+)" → "Facilities: Small (<5);POPs: Large (50-99)" (brief says 3 facilities + 50 POPs)
- Tightened brief.

### LOGIN (254561398516)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief, removed marketing bleed.

### IP Pathways (254572221114)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief; added [2025-08-12] date prefix to Myfch partnership news.

### Hamilton Managed Hosting (263560994527)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2025-03-10] date prefix to Huskers partnership news.

### ATLDC / Tulix Systems (264241842929)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief from 4 paragraphs to 3 sentences.

### FIBERTOWN (264355635944)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2025-08-27] date prefix to Consolidated Communications fiber news.

### Merkle Standard (264432390882)
- Path: FULL | Segment: Data Center Colo Provider → Flagged for deletion
- Pure BTC mining hosting; no AI pivot evidence. Was incorrectly classified at tier_1 AI Signals - colo.

### InfoBunker (263392463559)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief from 4 paragraphs to 3 sentences.

### Colocation Northwest (264260027123)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2025-05-30] date prefix to Mike Cannon board news.

### RACK59 (264594125521)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2025-10-27] date prefix to Arelion PoP news.

### MIDCON Recovery Solutions (264592334569)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2025-06-26] date prefix to OK State Regents news.

### Hostirian (264635347669)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; cleared 2022-06 stale recent_news (47 months old).

### Agile Data Sites (254561398518)
- Path: FULL | Segment: Data Center Colo Provider → Flagged for deletion
- Acquired by DataBridge Sites in 2020; now integrated into DataBridge portfolio.

### Dynamic Internet (264594125511)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief, removed "No dated announcements" placeholder.

### CyberLynk (264592334565)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; cleared 2012-02 ancient news (14 years old).

### IgLou Internet Services (264635347664)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2024-06] date prefix to fiber resumption news.

### DataBridge Sites (264590543566)
- Path: MEDIUM | Tier: tier_3 unchanged
- Filled "Research needed." provisioning_landscape; added [2025] date prefix to dark fiber news.

### Archer Datacenters (264414880442)
- Path: FULL | Sub-segment: Standard - colo → Greenfield (high_90)
- Tier: tier_3 → tier_2 (default for Greenfield)
- Pre-operational; 120 MW Faribault MN campus development. Auto-migrates to operational sub-segment per enrichment-protocols.md §7 when first facility goes live.

### Fort Rock Data Center (264254416572)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief.

### FiberState (264590543560)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2025-11-18] date prefix to Hurricane Electric PoP news.

### Global Access Point (264260027122)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; clarified Union Station divestiture (sold to 1547/Harrison Street); GAP continues operations on remaining facilities.

### Colorado Colo (264192113377)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief; added [2024-09] date prefix to Riley O'Connor CTO news.

### Indiana Data Center (264432390878)
- Path: MEDIUM | Tier: tier_3 unchanged
- Tightened brief, removed "No dated announcements" placeholder.

### Bestline Communications (254626062059)
- Path: MEDIUM | Tier: tier_3 unchanged
- Apollo state correction: PA → Texas; owner re-derive: Tim Lieto (East) → Ken Cunningham (West)
- Tightened brief.

### I-Evolve (254572221115)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief, removed marketing bleed.

### CVM (263729676022)
- Path: MEDIUM | Tier: tier_2 unchanged
- Apollo state correction: IL → Connecticut. Owner unchanged (both states under Tim Lieto East).
- Tightened brief.

### 702 Communications (263560994524)
- Path: MEDIUM | Tier: tier_3 unchanged
- Expanded too-short brief.

### Compugen (263392463556)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief; tightened overlong recent_news (3 events with date prefixes).

### BrescoBroadband (254574022374)
- Path: MEDIUM | Tier: tier_3 unchanged
- Expanded too-short brief; added [2024-01-16] date prefix to Ohio Gig PE news.

### Bay Pointe Tech Services (263560994538)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief; preserved [2025-07] Everstream bankruptcy mention. Note: 23,061 employees in Apollo data is clearly wrong; not corrected this batch (no authoritative source) — flagged for D7 review.

### Far North Digital (263392463549)
- Path: FULL | Segment: Fiber Operator → Network Operator(Tier 1 / VNO) | Sub-segment: Long Haul / Backbone - Fiber operator → Subsea cable operator (low_5069)
- Tier: tier_2 unchanged (default for new sub-segment also T2)
- Pre-operational pan-Arctic submarine cable project. Anchor verification pending due to pre-operational status; D7 re-validation expected.

### AiNET (263560994536)
- Path: MEDIUM | Tier: tier_2 unchanged
- Tightened brief from 4 paragraphs to 3 sentences; preserved 2024-07 200 MW AI upgrade signal with date prefix.

### nGenX (263560994530)
- Path: FULL | Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Tier: tier_2 unchanged
- Apollo state correction: NV → Kansas (HQ Overland Park). Owner unchanged (both NV and KS under Ken West).

## Errors / retries

- 1 enum-validation error on initial 165 Halsey Street write: invalid POPs band "Large (50+)" — corrected on retry to "Large (50-99)". All 50 records successfully written.

## Run health: GREEN
