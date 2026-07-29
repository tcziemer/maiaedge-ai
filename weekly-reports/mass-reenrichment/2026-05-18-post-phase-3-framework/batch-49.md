# Mass Re-Enrichment Sweep — Batch 49

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 49
**Date:** 2026-05-19
**Records processed:** 50/50
**Path mix:** LIGHT 46 · MEDIUM 4 · FULL 0 · HOLD 0
**Tier changes:** 1 (Tillion T1→T2 on Greenfield migration)
**Sub-segment / segment corrections:** 2 (Southern Cross subsea reclass + Tillion Greenfield migration)
**Name corrections:** 3 (S&T Communications, TIM S.p.A., Southern Cross Cable Network)
**Apollo credits:** 0
**Last hs_object_id in batch:** 317223880415 (Airtel Business)

## Pre-flight

- Trigger query: customer_segment IN [6 active ICPs] AND hs_object_id GT 315977374429 AND (last_enriched_date LT 2026-05-18 OR NULL); sort hs_object_id ASC; limit 50
- Pool total returned by HubSpot: **409** (matches continuation token from batch 48; verified)
- Returned: 50 (no overage this batch — first 50 cleanly aligned)
- Canvas F0B0AFSB9LN: **0 active Mass Re-Enrichment Sweep holds** (Cooper directive 2026-05-19 "no holds going forward; resolve via best effort" still in effect). No concurrent batch detected.
- Apollo budget JSON: not updated (APOLLO_ENFORCEMENT=disabled per sweep params)
- Web searches: 0 total (all decisions made from existing enriched-field evidence per CLAUDE.md op principle 3)

## Batch shape

- **By segment:** 31 Fiber Operator + 8 Data Center Colo Provider + 4 NeoCloud + 3 Network Operator(Tier 1/VNO) + 4 MSP/Aggregator + 0 Enterprise. Post-batch: 30 Fiber Operator + 8 DCCP + 4 NeoCloud + 4 Network Operator (Southern Cross moved) + 4 MSP/Aggregator. Tillion stays in DCCP under Greenfield.
- **hs_is_target_account = true:** 0 records in this batch
- **Open deals at contractsent+:** 0 records (no segment-write blocks fired)
- **Closed-won deals (customers):** 0 records (no customer-protection HOLDs)
- **Records with last_signal_score / last_signal_date populated:** 0 (no signal modifiers fire across batch)
- **Records with non-empty recent_news_or_trigger_event:** ~35 (varied freshness; none cleared as stale per Cooper's best-effort directive)

## MEDIUM corrections detail

### 1. S&T Communications (316218856147) — name correction
- **Before:** name=`st-tel.net`, domain=`st-tel.net`
- **After:** name=`S&T Communications`, domain=`st-tel.net` (unchanged)
- **Reason:** Existing account_brief: "S&T Communications (S&T Telephone Cooperative), founded 1952 in Brewster, KS, serving 34+ communities across western Kansas." Name field was a sourcing artifact = domain string. Sub-segment / tier / confidence all framework-consistent (Regional CLEC - Fiber operator, tier_3, high_90). No tier change. file 06 §5 / D5 protocol F1.

### 2. TIM S.p.A. (316522694352) — name correction + account_brief cleanup
- **Before:** name=`SET`, account_brief contained legacy meta-commentary ("RECLASSIFIED to Network Operator(Tier 1 / VNO)... R1 2026-05-07 reclassification (was Other/low_5069 - this was a major misclassification)")
- **After:** name=`TIM S.p.A.`, account_brief rewritten to clean 4-sentence Phase 3-compliant narrative
- **Reason:** Domain `telecomitalia.it` resolves to TIM S.p.A. (formerly Telecom Italia S.p.A.). Name field "SET" was likely a sourcing artifact (the prior `customer_segment = Other / low_5069` misclassification was already corrected by R1 2026-05-07). Cleaned brief: "TIM S.p.A. (formerly Telecom Italia S.p.A.) is the largest Italian telecommunications carrier by revenue and subscribers, and former state monopoly headquartered in Rome/Milan/Naples. Subsidiaries include TIM Brasil (72.6M customers in Brazil) and Telecom Italia Sparkle (international wholesale). Recently restructured to spin out NetCo to KKR. Tier 1 national incumbent with full-service mobile, fixed-line, DSL, and fiber across 114M+ customers worldwide." 4 sentences (in cap). Segment/sub-segment/tier all unchanged: Network Operator(Tier 1/VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90. file 06 §6.1.

### 3. Southern Cross Cable Network (316558341874) — name + segment + sub-segment reclass to Subsea
- **Before:** name=`sccn.bm`, customer_segment=`Fiber Operator`, company_sub_segment=`Long Haul / Backbone - Fiber operator`, segmentation_confidence=`high_90`, account_tier=`tier_2`
- **After:** name=`Southern Cross Cable Network`, customer_segment=`Network Operator(Tier 1 / VNO)`, company_sub_segment=`Subsea cable operator`, segmentation_confidence=`medium_7089`, account_tier=`tier_2` (unchanged)
- **Reason:** Existing brief: "Trans-Pacific submarine cable operator with 30,500 km fiber in protected triple-ring topology across 9 landing stations. Up to 18 Tbps capacity. Owned by Spark NZ (38%), Singtel (30%), Telstra (25%), Verizon (6.4%)." This is a clear Subsea cable operator (the 30th sub-segment added 2026-05-14 per Operating Principle 10). Per CLAUDE.md "Known Data Quality Follow-ups #7" — Subsea cable operator policy classifications surface during sweeps. Southern Cross sits between BORDERLINE and HIGH on the anchor list (carrier-JV ownership echoes the consortium concern, but it operates as a distinct corporate entity selling wholesale capacity under the SX NEXT brand — not a pure capacity-allotment consortium like FLAG/SEA-ME-WE/ACE/EIG which are D1-evicted per file 06 §3). Confidence set medium_7089 to flag the borderline status for next quarterly anchor refresh. Default Subsea cable operator = T2, ceiling 1, floor 3. No signal modifiers fire. Tier stays tier_2 (same as prior Long Haul Backbone default). file 06 §6.1 / D5 protocol N5.

### 4. Tillion (316558342847) — Greenfield migration per Operating Principle 8
- **Before:** company_sub_segment=`AI Signals - colo`, account_tier=`tier_1`, segmentation_confidence=`medium_7089`
- **After:** company_sub_segment=`Greenfield`, account_tier=`tier_2`, segmentation_confidence=`medium_7089` (unchanged)
- **Reason:** Existing brief: "Azora-backed hyperscale data center platform with 2B euro investment in Zaragoza campus (300MW). Purpose-built for AI/cloud workloads... Pre-operational — construction starting 2026." Per CLAUDE.md Operating Principle 8 + Enrichment Protocols §7: Greenfield is a real sub-segment for actively-being-built Colo/NeoCloud companies (Series A-C funded, sites under construction). Tillion fits the pattern precisely (Azora institutional backing, 2B euro raised, 300MW campus under construction, no operational facility yet). When first operational site goes live, R2 will auto-migrate to AI Signals - colo (target operational sub-segment given the AI/cloud-workload product positioning). Default Greenfield = T2, ceiling 1, floor 3. No signal modifiers fire (last_signal_score empty). Net tier_2 (one-tier downgrade from prior tier_1 AI Signals default). file 06 §6.7 / D5 protocol G + Enrichment Protocols §7.

## LIGHT path follow-up flags (audit only — no FULL run in sweep window)

Records flagged with 4+ missing narrative enriched fields (matching the Pellera batch-48 precedent). These got `last_enriched_date = 2026-05-19` LIGHT stamp + audit note here; defer to a proper R2 FULL re-enrichment outside this sweep window:

| ID | Name | Missing fields | Note |
|---|---|---|---|
| 316427027134 | Armada | geo, infra, hyper, fabric, prov, news | Has "[Routine 2 FULL] [2026-05-04]" prefix on account_brief; R2 FULL pass ran but 6 narrative writes didn't land. Same pattern as Pellera (batch 48). |
| 316453414595 | Flux Core Data Systems | geo, infra, hyper, fabric, prov, news | Same Pellera-pattern field-write gap. |
| 316466007749 | NexGen Cloud | geo, infra, hyper, fabric, prov, news | Same Pellera-pattern field-write gap. |
| 316491210473 | Vapor IO | geo, infra, hyper, fabric, prov, news | Same Pellera-pattern field-write gap. |
| 316504259305 | Sparktelecomm | geo, infra, hyper, fabric, prov, news | Same Pellera-pattern field-write gap. |
| 316528134882 | Go4Mobility | geo, infra, hyper, fabric, prov, news | Same Pellera-pattern field-write gap. |
| 316529844930 | Data Access Solutions | geo, infra, hyper, fabric, prov, news | Same Pellera-pattern field-write gap. R1 2026-05-06 segment reclass landed for `customer_segment` only. |
| 316504261334 | Voxbridge, Inc | hyper, fabric, prov, news | 4 missing narrative fields. |
| 316528134884 | Sipstatus | hyper, fabric, prov, news | 4 missing narrative fields. |
| 316558342843 | Omobio | hyper, fabric, prov, news | 4 missing narrative fields. |
| 316614767312 | Gizat Global | hyper, fabric, prov, news | 4 missing narrative fields. |
| 316616574678 | EZ Mobile LLC | hyper, fabric, prov, news | 4 missing narrative fields. |

Note: `hyperscaler_proximity` missing on non-Colocation records is expected per Enrichment Protocols §4.5 ("meaningful only for Colocation + Greenfield; for Fiber Op / Network Op / NeoCloud / MSP / Enterprise this field is typically None Known"). Only flagged the 12 records above where multiple narrative fields are missing.

## Per-record results (full 50)

Format: ID | name | tier (cur→new) | path | sub-segment / notes

| # | ID | Name | Tier | Path | Sub-segment / Notes |
|---|---|---|---|---|---|
| 1 | 316007524065 | Akash Network | tier_1 | LIGHT | Large Scale GPU - Neocloud |
| 2 | 316157438671 | Nodiac | tier_1 | LIGHT | Modular - colo |
| 3 | 316163237567 | Bluebird Network | tier_3 | LIGHT | Standard - colo |
| 4 | 316165032669 | DTC Telecom | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 5 | 316170410717 | CalTel | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 6 | 316176615100 | CS Technologies | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 7 | 316205322955 | NM Fiber Network | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 8 | 316218856147 | **S&T Communications** | tier_3 | **MEDIUM** | **Name rewrite from `st-tel.net`** |
| 9 | 316224514748 | Metro MPLS | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 10 | 316227875521 | Pinnacle Telecom | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 11 | 316303584986 | MTC Communications | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 12 | 316427027134 | Armada | tier_1 | LIGHT+audit | Modular - colo (6 narrative fields blank, R2 FULL stamp prefix) |
| 13 | 316453414595 | Flux Core Data Systems | tier_1 | LIGHT+audit | Modular - colo (6 narrative fields blank) |
| 14 | 316466007749 | NexGen Cloud | tier_1 | LIGHT+audit | Sovereign AI Clouds - Neocloud (6 narrative fields blank) |
| 15 | 316491210473 | Vapor IO | tier_1 | LIGHT+audit | Modular - colo (6 narrative fields blank) |
| 16 | 316498875129 | FIBERX | tier_3 | LIGHT | Regional CLEC - Fiber operator (PR-based small operator; infra=None Identified accepted given thin scale evidence) |
| 17 | 316498876097 | Quantcom | tier_3 | LIGHT | Regional CLEC - Fiber operator (Czech small operator) |
| 18 | 316498876102 | Silica Networks - Datco Group | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 19 | 316500681428 | GasLINE | tier_2 | LIGHT | Dark Fiber Specialist - Fiber Operator |
| 20 | 316504259305 | Sparktelecomm | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (6 narrative fields blank) |
| 21 | 316504261334 | Voxbridge, Inc | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 narrative fields blank) |
| 22 | 316504261342 | Netia | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 23 | 316506947265 | Independents Fiber Network | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 24 | 316508758717 | Xenith IG | tier_2 | LIGHT | Dark Fiber Specialist - Fiber Operator |
| 25 | 316522694352 | **TIM S.p.A.** | tier_1 | **MEDIUM** | **Name `SET` → `TIM S.p.A.` + brief cleanup (removed legacy `RECLASSIFIED` meta-commentary)** |
| 26 | 316528134882 | Go4Mobility | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (6 narrative fields blank) |
| 27 | 316528134884 | Sipstatus | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 narrative fields blank) |
| 28 | 316528134888 | FlexNetworks | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 29 | 316529844930 | Data Access Solutions | tier_3 | LIGHT+audit | Regional CLEC - Fiber operator (6 narrative fields blank, R1 2026-05-06 segment-only write) |
| 30 | 316529844941 | Red Eléctrica de España | tier_2 | LIGHT | Dark Fiber Specialist - Fiber Operator |
| 31 | 316529844947 | Eatel | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 32 | 316558341874 | **Southern Cross Cable Network** | tier_2 | **MEDIUM** | **Segment Fiber/Long Haul → Network Operator/Subsea cable operator + name rewrite + confidence high_90 → medium_7089 (borderline JV anchor status)** |
| 33 | 316558342843 | Omobio | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 narrative fields blank) |
| 34 | 316558342847 | **Tillion** | **tier_1 → tier_2** | **MEDIUM** | **Sub-segment AI Signals - colo → Greenfield (pre-operational Azora campus per Op Principle 8); tier defaults Greenfield T2** |
| 35 | 316596757226 | Acuative | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 36 | 316598423258 | Wave Business | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 37 | 316614767312 | Gizat Global | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 narrative fields blank) |
| 38 | 316616574678 | EZ Mobile LLC | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 narrative fields blank) |
| 39 | 316618313423 | EOLO WHOLESALE | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 40 | 316620028618 | Redder | tier_3 | LIGHT | Standard - colo |
| 41 | 316620030686 | Fibernetics | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 42 | 316621828851 | Duos Technologies | tier_1 | LIGHT | AI Infrastructure providers - Neocloud |
| 43 | 316621829822 | IPC Systems | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 44 | 316623621835 | SEACOM | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator (hybrid subsea+terrestrial — terrestrial 3,000km+ keeps Long Haul classification, NOT Subsea cable operator per file 06 §6.1 tiebreaker — only "subsea-primary with minimal terrestrial" reclassifies) |
| 45 | 316623621852 | Eurofiber | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 46 | 316627225337 | Eastlink | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 47 | 316627226300 | Acronym Solutions | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 48 | 316725284544 | AXS Bolivia S.A. | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator (landlocked Bolivia, NOT subsea) |
| 49 | 316745276104 | Brasil TecPar | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 50 | 317223880415 | Airtel Business | tier_1 | LIGHT | Tier 1 Carrier - Network Op |

## Notes

- All 50 records: framework-consistent post-batch. The 4 MEDIUM corrections (3 name rewrites + 2 sub-segment / segment reclasses) resolved the framework drift detected in this pool slice.
- 0 records had populated last_signal_score / last_signal_date — no signal modifiers fired across batch.
- 0 sub-segment auto-migrations from §7.4a deterministic table (all values already on canonical Phase 3 enum).
- 1 Greenfield migration (Tillion AI Signals - colo → Greenfield; pre-operational AI campus).
- 0 Customer-protection HOLDs (no closed-won deals in batch).
- 0 Completeness Gate fails (no FULL paths invoked).
- 0 manual-review HOLDs (per Cooper 2026-05-19 directive: best-effort classify, no new holds).
- 0 records with hs_is_target_account=true.
- **12 LIGHT+audit records** flagged for clean R2 FULL re-enrichment post-sweep (4-6 narrative fields blank; Pellera-pattern field-write gaps). Tabulated above.

## Standout notable records (top 5 changes)

1. **Southern Cross Cable Network (316558341874)** — Segment + sub-segment reclass `Fiber Operator / Long Haul Backbone` → `Network Operator(Tier 1/VNO) / Subsea cable operator`. Trans-Pacific 30,500km submarine cable JV (Spark/Singtel/Telstra/Verizon). 30th sub-segment migration; medium_7089 confidence flags JV-vs-consortium borderline for next quarterly anchor refresh.
2. **Tillion (316558342847)** — Sub-segment `AI Signals - colo` → `Greenfield`; tier T1 → T2. Azora-backed 300MW Zaragoza campus, pre-operational. Auto-migration trigger captured per Operating Principle 8.
3. **TIM S.p.A. (316522694352)** — Name rewrite `SET` → `TIM S.p.A.` + account_brief cleanup. Largest Italian carrier; legacy "RECLASSIFIED" meta-commentary stripped from brief.
4. **Southern Cross / TIM / S&T name corrections** — Three records had domain-as-name sourcing artifacts now resolved to canonical brand identities.
5. **12 Pellera-pattern flags** — Recurring narrative-field-write gap from R2 FULL passes on 2026-05-04 / 2026-05-05 / 2026-05-07. Worth investigating R2 write-path reliability post-sweep.

## HubSpot write results

5 batches of 10 via `manage_crm_objects` updateRequest with `confirmationStatus = CONFIRMATION_WAIVED_FOR_SESSION`:
- Batch 1/5 (records 1-10, includes S&T Communications MEDIUM rename): 10/10 updated, 0 failed
- Batch 2/5 (records 11-20): 10/10 updated, 0 failed
- Batch 3/5 (records 21-30, includes TIM MEDIUM): 10/10 updated, 0 failed
- Batch 4/5 (records 31-40, includes Southern Cross + Tillion MEDIUM): 10/10 updated, 0 failed
- Batch 5/5 (records 41-50): 10/10 updated, 0 failed

Total: 50/50, 0 errors, 0 retries needed. HubSpot company notes per §7.7 deferred (Slack DM + this audit log function as the audit trail — same pattern as batches 46-48).

## Continuation

- LAST_PROCESSED_HS_OBJECT_ID: 317223880415
- POOL_REMAINING (before batch 49): 409
- POOL_REMAINING (after batch 49): 359
- Drain progress: ~87% of sweep complete (2,445 / ~2,804 records assuming original ~2,854 pool less remaining 359 = 2,495 done; batch 49 +50 = 2,495)
- Next batch: 50 — ETA ~7 more batches at BATCH_SIZE=50

## Continuation token (for hands-off resume)

```
SWEEP_NAME=2026-05-18-post-phase-3-framework
SWEEP_KICKOFF_DATE=2026-05-18
NEXT_BATCH=50
BATCH_SIZE=50
APOLLO_ENFORCEMENT=disabled
SEGMENT_SCOPE=all_active_icp
POOL_REMAINING=359
HOLD_POLICY=NONE (best-effort classify)
SORT=hs_object_id ASC
LAST_PROCESSED_HS_OBJECT_ID=317223880415
```
