# Mass Re-Enrichment Sweep — Batch 55

**Sweep:** `2026-05-18-post-phase-3-framework`
**Batch:** 55
**Date:** 2026-05-19
**Records returned:** 50 / Pool total before batch: 109
**Path mix:** LIGHT 42 · MEDIUM 0 · FULL 7 (reclassifications, web-research-free leverage-and-patch) · HOLD 1
**Apollo this batch:** 0 credits · Sweep cumulative: 0
**APOLLO_ENFORCEMENT:** disabled
**VERIFY_DEPTH:** leverage-and-patch
**Run health:** 🟢 GREEN

---

## Reclassifications (7 records — segment / sub-segment / tier writes)

### Crusoe Energy Systems (320960333516)
- Path: FULL (leverage-and-patch reclass; no web research needed — Cooper 2026-05-14 op-principle #9 explicitly names Crusoe for the move)
- Domain: crusoe.ai (unchanged)
- Segment: NeoCloud → NeoCloud (unchanged)
- Sub-segment: Large Scale GPU - Neocloud → **Crypto to AI - Neoclouds** (op-principle #9: BTC mining heritage — flared-gas BTC mining lineage; NC5 is inclusive of operator AND landlord models post-Cooper 2026-05-14)
- Confidence: high_90 → high_90
- Tier: tier_1 → tier_1 (skipped hs_is_target_account=true)
- Customer protection invoked: no (0 closed-won deals)
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Cooper 2026-05-14 op-principle #9 reclassification — Crusoe moved from Large Scale GPU - Neocloud to Crypto to AI - Neoclouds (NC5).

### Prometheus Hyperscale (320892129013)
- Path: FULL (leverage-and-patch reclass)
- Domain: prometheushyperscale.com (unchanged)
- Segment: Data Center Colo Provider → **NeoCloud** (op-principle #9: Prometheus Hyperscale = Hut 8 lineage; "Companies previously listed as Large Scale GPU - Neocloud or AI Signals - colo anchors but with BTC mining heritage now route to NC5 instead")
- Sub-segment: AI Signals - colo → **Crypto to AI - Neoclouds**
- Confidence: high_90 → high_90
- Tier: tier_1 → tier_1 (Crypto to AI - Neoclouds default 1, ceiling 1, floor 2; computed = 1; no change)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Cooper 2026-05-14 op-principle #9 — Prometheus Hyperscale (Hut 8 lineage) reclassified from DCCP/AI Signals to NeoCloud/Crypto to AI. Wyoming Hyperscale 321238936271 logged to canvas for R3 parent-child consolidation.

### New Era Energy & Digital (320988084985)
- Path: FULL (leverage-and-patch reclass)
- Domain: newerainfra.ai (unchanged)
- Segment: Data Center Colo Provider → Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo → **Greenfield** (op-principle #8 + enrichment-protocols.md §7: actively-being-built campus, Series A-C funded, no operational facility yet — NUAI Nasdaq $245.6M mkt cap, 7 emp, founded 2023; Texas Critical Data Centers 1+ GW hyperscale campus in Ector County, pre-operational)
- Confidence: high_90 → high_90
- Tier: tier_3 → **tier_2** (Greenfield default 2, ceiling 1, floor 3; no signal modifiers fire; computed = 2)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Pre-operational Greenfield reclassification per enrichment-protocols §7 — TCDC campus is funded but pre-operational.

### Sailfish Digital Ventures (321025750773)
- Path: FULL (leverage-and-patch reclass)
- Domain: sailfishinvestors.com (unchanged)
- Segment: Data Center Colo Provider → Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo → **Greenfield** (op-principle #8 + enrichment-protocols.md §7: Comanche Circle is a 2,600-acre 5,000 MW (5 GW) master-planned community in Tolar TX, pre-operational, single-emp investment vehicle)
- Confidence: high_90 → high_90
- Tier: tier_3 → **tier_2** (Greenfield default 2; no modifiers; computed = 2)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Pre-operational Greenfield reclassification — Comanche Circle master plan only.

### Helios Towers Ghana (321429968619)
- Path: FULL (D1 disqualifier reclass)
- Domain: htghana.com (unchanged)
- Segment: Fiber Operator → **Other** (D1 disqualifier: passive tower infrastructure leasing to MNOs is not active connectivity — consistent with sibling 320523046634 Helios Towers Malawi correction in batch 54)
- Sub-segment: Regional CLEC - Fiber operator → **(cleared)** (not applicable to Other)
- Confidence: high_90 → high_90
- Tier: tier_3 (left unchanged — not in 6 ICPs, Step A0 skips tier write)
- Customer protection invoked: no (0 closed-won deals verified)
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: D1 disqualifier — tower operator (passive infra) not fiber operator. account_brief appended with correction context. R3 to handle parent-child consolidation with 319134249719 Helios Towers Plc (WA).

### Verizon Belgium Luxembourg (322286161650)
- Path: FULL (leverage-and-patch reclass)
- Domain: be.verizon.com (unchanged)
- Segment: Fiber Operator → **MSP/Aggregator** (existing classification incorrect — Verizon BE subsidiary is enterprise managed services / Verizon Business EMEA PoP, not a fiber operator with a Belgian fiber buildout)
- Sub-segment: Regional CLEC - Fiber operator → **Managed Network Services - MSP** (Cooper 2026-05-14 IT-MSP test irrelevant — this is global-carrier managed network services PoP)
- Confidence: high_90 → high_90
- Tier: tier_3 → **tier_2** (MSP/Managed Network Services default 2, ceiling 1, floor 4; computed = 2)
- Customer protection invoked: no (0 closed-won deals)
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Subsidiary misclassification — Verizon BE is enterprise managed services arm, not fiber operator. Flag R3 to consolidate with Verizon parent (or keep as own record per D2 wholesale-arm policy; international subsidiaries may stay as own records when serving distinct local enterprise market).

### Verizon Norway AS (322286148335)
- Path: FULL (leverage-and-patch reclass)
- Domain: no.verizon.com (unchanged)
- Segment: Fiber Operator → **MSP/Aggregator** (same rationale as Verizon BE)
- Sub-segment: Regional CLEC - Fiber operator → **Managed Network Services - MSP**
- Confidence: high_90 → high_90
- Tier: tier_3 → **tier_2** (MSP/MNS default 2; computed = 2)
- Customer protection invoked: no (0 closed-won deals)
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Subsidiary misclassification — Verizon NO is enterprise managed services arm.

---

## HOLD (1 record — appended to canvas F0B0AFSB9LN)

### Wyoming Hyperscale (321238936271)
- Path: HOLD
- Domain: wyominghyperscalewhitebox.com
- Reason: DUPLICATE of 320892129013 Prometheus Hyperscale per existing account_brief ("DUPLICATE OF PROMETHEUS HYPERSCALE (320892129013) — same entity, post-2024 rebrand. Pending R3 consolidation 2026-05-06"). Sweep does not re-litigate dups — R3 routine owns parent-child consolidation. No HubSpot writes, no date bump. Record remains in sweep pool until R3 archives or resolves.

---

## LIGHT path — 42 records (date-bump + tier recompute idempotent no-op)

All 42 records are framework-consistent (sub-segment in 30-active, no legacy-string detection in account_brief, computed_tier == current_tier or hs_is_target_account=true freeze). Tier recompute fired on each; no write triggered. last_enriched_date stamped to 2026-05-19.

### hs_is_target_account=true (tier-frozen LIGHT records)

| ID | Name | Segment / Sub-segment | Current Tier | Default | Modifiers | Computed | Tier Action |
|---|---|---|---|---|---|---|---|
| 322503843537 | Umniah Wholesale | NetworkOp / Pure Wholesale Carrier | tier_2 | 1 | none | 1 (would lower) | SKIPPED (target=true) |
| 320876610253 | AWASR | NetworkOp / Tier 1 Carrier | tier_1 | 1 | none | 1 | SKIPPED (target=true, idempotent) |
| 320876610254 | zamtel | NetworkOp / Tier 1 Carrier | tier_3 | 1 | none | 1 (would raise) | SKIPPED (target=true) |
| 322761764558 | Blue Ridge Mountain EMC | Fiber / Municipal-Cooperative | tier_2 | 4 | none | 4 (would lower) | SKIPPED (target=true) |
| 320875891448 | Pilot Fiber | Fiber / Regional CLEC | tier_3 | 3 | none | 3 | SKIPPED (target=true, idempotent) |
| 323221077749 | Flow Digital Infrastructure | DCCP / Standard - colo | tier_3 | 3 | none | 3 | SKIPPED (target=true, idempotent) |
| 323221077748 | EonFibre | Fiber / Regional CLEC | tier_3 | 3 | none | 3 | SKIPPED (target=true, idempotent) |

### Tier-stable LIGHT records (computed == current, no write)

| ID | Name | Segment / Sub-segment | Tier | Default | Modifiers | Notes |
|---|---|---|---|---|---|---|
| 320990013160 | Paratus Angola | Fiber / Regional CLEC | tier_3 | 3 | none | stale news (2022) cleared |
| 321034217198 | Fermi America | DCCP / AI Signals - colo | tier_1 | 1 | none | Pre-operational AEIC TX megacampus — already AI Signals (not Greenfield reclass; AI Signals applies to operational + planned AI-anchored facilities per file 06) |
| 321020350175 | BorderPlex Digital Assets | DCCP / AI Signals - colo | tier_1 | 1 | none | Project Jupiter 2.45 GW; news fresh (2026-04-27) |
| 321479152324 | i3 Broadband | Fiber / Regional CLEC | tier_3 | 3 | none | Fiber Connect 2026 attendee |
| 320997081786 | ambiFOX GmbH | MSP / Telecom Aggregator | tier_2 | 2 | none | sparse fields (1/7); flagged for R2 narrative backfill |
| 321635744480 | Rowan Digital Infrastructure | DCCP / AI Signals - colo | tier_1 | 1 | none | Blackstone-Quinbrook 49% stake April 2026 (would-be hot signal but signal-persistence fields blank; signal scan to repopulate) |
| 321768447684 | Unifique | Fiber / Long Haul-Backbone | tier_2 | 2 | none |  |
| 320875891446 | iBasis | Fiber / Long Haul-Backbone | tier_2 | 2 | none | Rev $1.2B; voice/messaging wholesale (could fit Pure Wholesale Carrier - Network Op but sub-segment stable, leverage-and-patch) |
| 320875891447 | BIG Fiber | Fiber / Dark Fiber Specialist | tier_2 | 2 | none | Alberta Canada |
| 321479592663 | Worldpay | Enterprise / Financial Services | tier_3 | 3 | none | $3.9B rev, 8,500 emp; payments processor — Multi-DC Enterprise ICP confirmed |
| 322503843535 | Fidium Fiber | Fiber / Dark Fiber Specialist | tier_2 | 2 | none | Consolidated Communications brand |
| 322368676578 | Segra | Fiber / Dark Fiber Specialist | tier_2 | 2 | none | $4.1B reported (data quality flag) |
| 322837059318 | Bell Canada | NetworkOp / Tier 1 Carrier | tier_1 | 1 | none | Canadian incumbent |
| 322370821844 | Cox | NetworkOp / Cable MSO Enterprise Div | tier_1 | 1 | none | Charter-Cox combination cleared FCC (white-hot-equivalent news, but signal-persistence fields blank — Signal Scan to populate) |
| 322837059313 | AT TOKYO | DCCP / Standard - colo | tier_3 | 3 | none | NTT subsidiary, Tokyo |
| 322038348534 | WOW! (WideOpenWest) | Fiber / Regional Cable Operator | tier_3 | 3 | none | $1.2B rev — sizeable but default 3 with ceiling 1 holds without signal trigger |
| 321984706290 | RiverStreet | Fiber / Regional CLEC | tier_3 | 3 | none | NC rural fiber |
| 322041939684 | IBT Group USA | Fiber / Regional CLEC | tier_3 | 3 | none | Miami FL, IBT Group Spain parent |
| 322503843536 | Green Datacenter AG | DCCP / Standard - colo | tier_3 | 3 | none | stale news (2025-07) cleared |
| 323221077752 | Vero Fiber Networks | Fiber / Regional CLEC | tier_3 | 3 | none | stale news (2025-12-02) cleared; BendTel acquisition info lost (Signal Scan to repopulate if still material) |
| 322837059311 | CMC Networks | Fiber / Regional CLEC | tier_3 | 3 | none | stale news (2023-12) cleared |
| 322362484462 | Chelan County PUD #1 | Fiber / Municipal-Cooperative | tier_4 | 4 | none | WA hydro+fiber |
| 322407808702 | 832 Communications | Fiber / Regional CLEC | tier_3 | 3 | none | Houston-area fiber |
| 322353526464 | AccessPlus | Fiber / Regional CLEC | tier_3 | 3 | none | MA regional |
| 322364277473 | TruVista Communications | Fiber / Regional Cable Operator | tier_3 | 3 | none | SC/GA rural ILEC |
| 322358873829 | Lumbee River EMC | Fiber / Municipal-Cooperative | tier_4 | 4 | none | NC electric coop |
| 322386206456 | Paducah Power System | Fiber / Regional CLEC | tier_3 | 3 | none | KY municipal utility |
| 322407809750 | Rapid Fiber Internet | Fiber / Regional CLEC | tier_3 | 3 | none | SVEC subsidiary, FL |
| 322382680794 | Sound Broadband | Fiber / Regional CLEC | tier_3 | 3 | none | Fixed wireless / 5G NR; BEAD focus |
| 322364276470 | SLICFiber | Fiber / Regional CLEC | tier_3 | 3 | none | Atlas Connectivity; rural NY |
| 322395164381 | Digicom | Fiber / Regional CLEC | tier_3 | 3 | none | QC Canada |
| 322357183197 | Jamadots | Fiber / Regional CLEC | tier_3 | 3 | none | Small regional ISP |
| 322398799566 | Pierce Pepin Cooperative | Fiber / Municipal-Cooperative | tier_4 | 4 | none | WI electric coop (SwiftCurrent Connect) |
| 322393359088 | Citizens Fiber | Fiber / Regional CLEC | tier_3 | 3 | none | Westmoreland County PA |
| 322391560939 | Townes Telecommunications | Fiber / Regional CLEC | tier_3 | 3 | none | Macclenny FL rural ILEC |

---

## Stale `recent_news_or_trigger_event` clears (4 records, LIGHT side-action)

Per §7.4 rule: date prefix >90 days old AND no Signal Scan write in last 7 days → clear field. Signal Scan last ran 2026-05-11 (8 days ago, outside 7d window).

| ID | Name | Old news date | Days stale | Cleared |
|---|---|---|---|---|
| 320990013160 | Paratus Angola | Jul 2022 (rebrand from ITA) | ~1390d | ✅ |
| 322503843536 | Green Datacenter AG | 2025-07-15 (IFM acquisition) | 308d | ✅ |
| 323221077752 | Vero Fiber Networks | 2025-12-02 (BendTel M&A) | 168d | ✅ |
| 322837059311 | CMC Networks | 2023-12-01 (Center3 acquisition) | 905d | ✅ |
| 323221077749 | Flow Digital Infrastructure | 2025-07-29 (Tokyo campus init) | 294d | ✅ |

Actual count = 5 (Flow Digital also stale; total = 5 stale-news clears).

---

## HubSpot writes — summary

| Phase | Records | Tool calls | Failures |
|---|---:|---:|---:|
| Phase 1 reclassifications | 7 | 1 batch (manage_crm_objects) | 0 |
| Phase 2a-e date-bumps + stale-clears | 42 | 5 batches (10/10/10/10/2) | 0 |
| **HubSpot writes total** | **49** | **6** | **0** |
| Canvas HOLD append | 1 (Wyoming Hyperscale) | 1 slack_update_canvas | 0 |
| §7.7 HubSpot company notes | 49 | (batched in Phase 3 below) |  |

---

## Apollo accounting

| Metric | Value |
|---|---|
| Apollo credits this batch | 0 |
| Sweep cumulative Apollo | 0 (APOLLO_ENFORCEMENT=disabled, sweep is out of weekly-cap scope) |
| `weekly-reports/apollo-budget.json` updated? | No (sweep-mode; budget tracker not touched) |

---

## Pool drain status

| Metric | Value |
|---|---:|
| Pool size before batch 55 | 109 |
| Processed this batch | 49 (excludes Wyoming Hyperscale HOLD which remains in pool) |
| Pool after batch 55 | **~60** |
| ETA at BATCH_SIZE=50 | ~2 more batches |
| Total batches in sweep | 55 |

Sweep is in late-drain phase. Most remaining records are likely small fiber operators / regional accounts with sparse enrichment that R2 will need to backfill on the next 120-day rotation.

---

## Pre-batch sanity checks

| Check | Status | Detail |
|---|---|---|
| 1. Concurrency | ✅ PASS | Batch 54 finished 2026-05-19 21:12 UTC; batch 55 fires 21:19 UTC. 7-min gap. No concurrent run. |
| 2. R2 paused | ✅ Inferred PAUSE | apollo-budget.json still on week_iso 2026-W19 (today is W21). R2 hasn't consumed Apollo since 2026-05-13. Consistent with §12 sweep-mode pause. |
| 3. Framework freshness | ✅ PASS | tier-compute-spec.md mod 2026-05-15 (pre-kickoff); sub-segment-qualification.md mod 2026-05-14 (pre-kickoff); enrichment-protocols.md mod 2026-05-15 (pre-kickoff). All ≤ SWEEP_KICKOFF_DATE 2026-05-18. |
| 4. Pool projection | ✅ PASS | 109 → ~60 remaining; sweep on track to close in 2 more batches. |

---

## Notable findings for CLAUDE.md "Known Data Quality Follow-ups"

1. **Verizon international subsidiaries pattern** — Verizon Belgium Luxembourg + Verizon Norway AS were misclassified as `Fiber Operator / Regional CLEC - Fiber operator` (presumably auto-assigned at import). Reclassified to `MSP/Aggregator / Managed Network Services - MSP` in this batch. Recommend scanning HubSpot for other Verizon `*.verizon.com` country subdomains likely carrying the same misclassification. Add to existing Verizon dup-pair flag in CLAUDE.md §"Known Data Quality Follow-ups".

2. **Helios Towers sibling pattern** — Helios Towers Ghana (321429968619) reclassified Fiber Operator → Other consistent with batch 54's Helios Towers Malawi (320523046634) correction. Tower infrastructure operators (passive leasing to MNOs) are D1 disqualifiers. Helios Towers parent (319134249719 HT Plc) is already correctly classified. Recommend account-sourcing audit of `htX.com` subdomains for additional country subsidiaries needing the same correction.

3. **Cooper op-principle #9 backlog** — Prometheus Hyperscale (Hut 8 lineage) reclassified DCCP/AI Signals → NeoCloud/Crypto to AI in this batch. Crusoe sub-segment moved Large Scale GPU → Crypto to AI. CLAUDE.md explicitly lists "Crusoe, Applied Digital, Prometheus Hyperscale moved 2026-05-14" — Crusoe + Prometheus done in batch 55; **Applied Digital still pending** — likely already enriched outside this batch's window, but R-Tier-Audit or a quick crm-hygiene scan should verify Applied Digital and any other BTC-lineage anchors carry the correct NC5 sub-segment.

4. **Pre-operational Greenfield pattern** — New Era Energy & Digital + Sailfish Digital Ventures reclassified Standard - colo → Greenfield in this batch. These were obvious Greenfield candidates (NUAI single-emp investment vehicle with 1+ GW announced pre-operational campus; Sailfish single-emp vehicle with 5 GW master plan). Recommend a one-time sweep over `Data Center Colo Provider / Standard - colo` records with `numberofemployees < 20 OR account_brief contains "pre-operational" OR "Series A" OR "Series B" OR "master-planned"` to catch additional Greenfield candidates.

5. **Sparse-enrichment R2 backlog growing** — Several records in this batch carry only 1-3 of 7 enriched fields populated (Umniah, AWASR, zamtel, ambiFOX, Worldpay, Verizon BE/NO, WOW!, RiverStreet, IBT). Cumulative R2 backlog now substantial (~300+ records per batch 54 estimate). Once sweep closes, R2 should run several catch-up cycles to populate infrastructure_profile / hyperscaler_proximity / fabric_provisioning_approach / provisioning_landscape / recent_news_or_trigger_event for these records.

---

**End of batch 55 audit log.**
