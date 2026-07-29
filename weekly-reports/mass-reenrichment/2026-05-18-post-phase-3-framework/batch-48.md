# Mass Re-Enrichment Sweep — Batch 48

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 48
**Date:** 2026-05-19
**Records processed:** 50/50
**Path mix:** LIGHT 45 · MEDIUM 5 · FULL 0 · HOLD 0
**Tier changes:** 2 (1 promotion FirstLight T4→T2, 1 demotion Mapletree T3→T5)
**Sub-segment corrections:** 4 (FirstLight, Mapletree, Armstrong Group, IREN)
**Domain/name corrections:** 1 (Armstrong Group)
**Apollo credits:** 0
**Last hs_object_id in batch:** 315977374429 (IREN)

## Pre-flight

- Trigger query: customer_segment IN [6 active ICPs] AND hs_object_id > 298009434830 AND (last_enriched_date < 2026-05-18 OR null) AND type != Customer, sort hs_object_id ASC, limit 55
- Pool total returned by HubSpot: **459** (matches continuation token from batch 47)
- Returned: 55; processed first 50; deferred records 51-55 (Akash Network, Nodiac, Bluebird Network, DTC Telecom, CalTel) to batch 49
- Canvas F0B0AFSB9LN: **0 active Mass Re-Enrichment Sweep holds** (Cooper directive 2026-05-19 "no holds going forward; resolve via best effort" — all prior-batch holds RESOLVED earlier today). No concurrent batch detected.
- Apollo budget JSON: not updated (APOLLO_ENFORCEMENT=disabled per sweep params)
- Web searches: 2 total (Armstrong canonical domain check + Akash Network model verification)

## Batch shape

- **By segment:** 26 Fiber Operator + 16 Data Center Colo Provider + 5 NeoCloud + 2 Network Operator(Tier 1/VNO) + 1 MSP/Aggregator (Mapletree reclassed → Other)
- **hs_is_target_account = true:** 10 records (rows 37-48 partial range — QTD Systems, Qoob, Tiger DC, AmpZ, Verrus, Conapto, Data Horizon, Flexnode, AMA TechTel, Consolidated Comms). All tier writes skipped per §8 manual override rule. Other fields untouched (already framework-consistent LIGHT pass).
- **Open deals at contractsent+:** 0 records (no segment-write blocks fired)
- **Closed-won deals (customers):** 0 records (no customer-protection HOLDs)
- **Records with last_signal_score / last_signal_date populated:** 0 (no signal modifiers fire across batch)
- **Records with non-empty recent_news_or_trigger_event:** 4 (FirstLight, IREN, Pacific Crossing implicit, Comcast Business implicit — all preserved, none cleared as stale)

## MEDIUM corrections detail

### 1. FirstLight (300468012734) — sub-segment + tier promotion
- **Before:** customer_segment=Fiber Operator, company_sub_segment=`Municipal / Cooperative - Fiber operator`, account_tier=tier_4, confidence=high_90
- **After:** company_sub_segment=`Long Haul / Backbone - Fiber operator`, account_tier=tier_2, confidence=high_90
- **Reason:** FirstLight is PE-owned (Antin Infrastructure), NOT municipal/cooperative. 660 employees, 25K+ route miles (infrastructure_profile shows Large 10K-50K), Northeast/Mid-Atlantic, regional wholesale fiber operator. Default Long Haul/Backbone = T2, ceiling 1, floor 3. No signal modifiers fire. Net tier_2. file 06 §5 / D5 protocol F2.
- **Audit:** Significant misclassification corrected. Existing account_brief already references "25k+ route miles across NY/NE/Mid-Atlantic" + "Antin Infrastructure owned" — original Municipal/Coop sub-segment was an enum error from pre-Phase 3 framework. No web_search needed; existing enriched fields had clear evidence.

### 2. Mapletree (302234821315) — segment demotion to Other
- **Before:** customer_segment=MSP/Aggregator, company_sub_segment=`AI Signals - colo`, account_tier=tier_3, confidence=high_90
- **After:** customer_segment=Other, company_sub_segment=(empty), account_tier=tier_5, confidence=high_90
- **Reason:** Mapletree is a Singapore REIT (real estate investor) that OWNS DC buildings leased long-term to operators (e.g., $1.4B North American portfolio leased from Digital Realty). It is NOT an active infrastructure operator. Per CLAUDE.md op principle 7 ("Aggressive Flagged for deletion / Other for non-fits") and `Known Data Quality Follow-ups #1` (5 MSP/Aggregator records with colo sub-segments — Mapletree, Montera, PTS, Lonestar, LS Power). Per Phase 3 D1 disqualifier: passive landlord/REIT pattern. Retained as Other tier_5 for partner/competitive reference value (relevant to understanding DC landlord ecosystem).
- **Audit:** Existing provisioning_landscape field already noted "RECLASSIFIED to Enterprise" (stale instruction from pre-Phase 3) — this batch acts on Cooper's correct guidance: passive landlord = Other, not Enterprise.

### 3. Armstrong Group (303892660925) — name + domain + sub-segment correction
- **Before:** name=`armstronggroup.info`, domain=`armstronggroup.info`, company_sub_segment=`Regional CLEC - Fiber operator`, account_tier=tier_3, confidence=empty
- **After:** name=`Armstrong Group`, domain=`armstrongonewire.com`, company_sub_segment=`Regional Cable Operator - Fiber operator`, account_tier=tier_3 (unchanged), confidence=high_90
- **Reason:** Original record had placeholder ".info" domain matching the company name slot — sourcing artifact. WebSearch confirmed canonical broadband-operating domain `armstrongonewire.com` (Wikipedia + company history page agoc.com confirm Armstrong Group is one of the largest US MSOs, 400K+ homes across PA/OH/MD/WV/KY/NY). Sub-segment shifted Regional CLEC → Regional Cable Operator since Armstrong is historically a cable MSO that has expanded into fiber. Both sub-segments default tier_3, so no tier change. file 06 §5 / D5 protocol F5.
- **Audit:** Identity sanity check (MISDOMAIN) triggered name + domain rewrite. Sub-segment correction is the higher-value fix — frames Armstrong appropriately for the segment-specific MaiaEdge angle.

### 4. IREN (315977374429) — sub-segment Crypto to AI reclass
- **Before:** customer_segment=NeoCloud, company_sub_segment=`AI Infrastructure providers - Neocloud`, account_tier=tier_1, confidence=high_90
- **After:** company_sub_segment=`Crypto to AI - Neoclouds`, account_tier=tier_1 (unchanged), confidence=high_90
- **Reason:** Per CLAUDE.md Operating Principle 9: "**Crypto to AI - Neoclouds** is INCLUSIVE of operator AND landlord models. Former bitcoin miners pivoting to AI infrastructure regardless of business model. Crusoe, IREN, Core Scientific, Galaxy Digital, Bitfarms, TeraWulf, APLD / Applied Digital, Northern Data Group, Prometheus Hyperscale / Hut 8 lineage all land here." IREN's existing recent_news_or_trigger_event explicitly states: "Pivoting from Bitcoin mining to AI infrastructure." Account_brief: "next-gen data center operator pivoting from Bitcoin mining to AI cloud infrastructure." Clear evidence already in record — no web_search needed. Tier default for Crypto to AI = T1 (same as prior Large Scale GPU / AI Infra Providers). No tier change.
- **Audit:** Framework principle 9 retroactive application. $9.7B Microsoft GPU cloud contract + 23K Nvidia GPUs makes IREN one of the marquee Crypto to AI - Neoclouds anchors.

### 5. Pellera Technologies (301784664824) — confidence fill
- **Before:** customer_segment=MSP/Aggregator, company_sub_segment=`Cloud + Telecom Hybrid MSP - MSP`, account_tier=tier_2, confidence=(empty), last_enriched_date=2026-05-05
- **After:** confidence=medium_7089, last_enriched_date=2026-05-19
- **Reason:** R2 Stale Re-Enrichment ran a FULL pass 2026-05-05 (per account_brief stamp) but the segmentation_confidence write didn't land. Fill with medium_7089 (conservative — 3,200 employees, merger-of-equals 2025-07-21 Converge + Mainline Information Systems, classification "Cloud + Telecom Hybrid MSP" is reasonable but the 6 missing narrative enriched fields are a separate data gap not fixable from existing record state). Audit flag for follow-up: 6 of 7 enriched narrative fields are empty (geographic_focus, infrastructure_profile, hyperscaler_proximity, fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event) — defer to a proper R2 FULL re-enrichment outside this sweep window. Sub-segment + tier compute correct as-is.

## Per-record results (full 50)

Format: ID | name | tier (cur→new) | path | sub-segment | notes

| # | ID | Name | Tier | Path | Sub-segment / Notes |
|---|---|---|---|---|---|
| 1 | 298009434833 | Dobson Telephone | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 2 | 298009434835 | Yucca Telecom | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 3 | 298009434836 | Brindlee Mountain Telephone | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 4 | 298009434840 | PemTel | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 5 | 298011233979 | Hunt Midwest SubTropolis | tier_3 | LIGHT | Standard - colo (KC underground colo) |
| 6 | 298011233980 | The SEIMITSU | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 7 | 298011233982 | Talkie Communications | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 8 | 298011233983 | NocTel Communications | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 9 | 298011233984 | DayStarr | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 10 | 298011233985 | Mountain Rural Telephone Coop | tier_4 | LIGHT | Municipal / Cooperative - Fiber operator |
| 11 | 298011233987 | Lincoln Telephone Company | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 12 | 298011233988 | Rise Broadband | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 13 | 298011233989 | La Harpe Telephone | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 14 | 298011233990 | Wheat State Telephone | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 15 | 300329366233 | Cast AI | tier_1 | LIGHT | AI Infrastructure providers - Neocloud |
| 16 | 300402132674 | Ziply Fiber | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 17 | 300402851562 | Comcast Business | tier_1 | LIGHT | Cable MSO Enterprise Division - Network Op |
| 18 | 300403571414 | AT&T | tier_1 | LIGHT | Tier 1 Carrier - Network Op |
| 19 | 300403571424 | Iron Mountain Data Centers | tier_1 | LIGHT | AI Signals - colo |
| 20 | 300466571983 | Pacific Crossing | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator |
| 21 | 300467292881 | Stream Data Centers | tier_1 | LIGHT | AI Signals - colo |
| 22 | 300467292889 | CtrlS | tier_1 | LIGHT | AI Signals - colo |
| 23 | 300468012733 | MIDTEL | tier_3 | LIGHT | Regional Cable Operator - Fiber operator |
| 24 | **300468012734** | **FirstLight** | **tier_4 → tier_2** | **MEDIUM** | **Municipal/Coop → Long Haul / Backbone - Fiber operator** |
| 25 | 300469447405 | SkyRider Communications | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 26 | **301784664824** | **Pellera Technologies** | **tier_2** | **MEDIUM** | **confidence empty → medium_7089** |
| 27 | **302234821315** | **Mapletree** | **tier_3 → tier_5** | **MEDIUM** | **MSP/Aggregator+colo → Other (REIT, D1 disqualifier)** |
| 28 | 303849415383 | ODATA | tier_1 | LIGHT | AI Signals - colo |
| 29 | 303850136250 | Equinix | tier_1 | LIGHT | AI Signals - colo |
| 30 | 303851573997 | Leaseweb | tier_1 | LIGHT | AI Signals - colo |
| 31 | 303851574002 | 5G Networks Ltd | tier_3 | LIGHT | Standard - colo |
| 32 | **303892660925** | **armstronggroup.info → Armstrong Group** | **tier_3** | **MEDIUM** | **name + domain (`armstrongonewire.com`) + sub-segment Regional CLEC → Regional Cable Operator** |
| 33 | 303917854399 | Opticaltel | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 34 | 303925580520 | Elea Data Centers | tier_3 | LIGHT | Standard - colo |
| 35 | 309393917654 | Nexthop | tier_2 | LIGHT | Dark Fiber Specialist - Fiber Operator |
| 36 | 311392963282 | Forge Growth Infrastructure | tier_1 | LIGHT | AI Signals - colo |
| 37 | 313950726874 | QTD Systems | tier_3 | LIGHT | Standard - colo (target_account=true, tier write skipped) |
| 38 | 314012854996 | Qoob Technologies | tier_3 | LIGHT | AI Signals - colo (target_account=true, tier write skipped) |
| 39 | 314012854999 | Tiger DC | tier_1 | LIGHT | AI Signals - colo (target_account=true, tier write skipped) |
| 40 | 314012855000 | AmpZ Energy | tier_1 | LIGHT | AI Signals - colo (target_account=true, tier write skipped) |
| 41 | 314012855001 | Verrus | tier_2 | LIGHT | Standard - colo (target_account=true, tier write skipped) |
| 42 | 314019025641 | RT-One | tier_1 | LIGHT | AI Signals - colo |
| 43 | 314113492720 | Conapto | tier_2 | LIGHT | AI Signals - colo (target_account=true, tier write skipped) |
| 44 | 314133164731 | Data Horizon Americas | tier_2 | LIGHT | Standard - colo (target_account=true, tier write skipped) |
| 45 | 314142327527 | Flexnode | tier_3 | LIGHT | AI Infrastructure providers - Neocloud (target_account=true, tier write skipped) |
| 46 | 314300605141 | Prominic.NET | tier_3 | LIGHT | Standard - colo |
| 47 | 314337137395 | AMA TechTel Communications | tier_3 | LIGHT | Regional CLEC - Fiber operator (target_account=true, tier write skipped) |
| 48 | 314374535919 | Consolidated Communications | tier_2 | LIGHT | Long Haul / Backbone - Fiber operator (target_account=true, tier write skipped) |
| 49 | 315067284210 | Ecoblox | tier_1 | LIGHT | AI Signals - colo |
| 50 | **315977374429** | **IREN** | **tier_1** | **MEDIUM** | **AI Infrastructure providers → Crypto to AI - Neoclouds (BTC heritage per op principle 9)** |

## Notes

- All 50 records: framework-consistent post-batch. The 4 sub-segment corrections + 1 confidence fill resolved the only framework drift detected in this pool slice.
- 0 records had populated last_signal_score / last_signal_date — no signal modifiers fired across batch.
- 0 sub-segment auto-migrations from §7.4a deterministic table (all values already on canonical Phase 3 enum; the 4 corrections were research-grade, not deterministic).
- 0 Greenfield migrations (no Greenfield records in this batch).
- 0 Customer-protection HOLDs (no closed-won deals in batch).
- 0 Completeness Gate fails (no FULL paths invoked).
- 0 manual-review HOLDs (per Cooper 2026-05-19 directive: best-effort classify, no new holds).
- 10 records with hs_is_target_account=true had tier writes skipped per §8 manual override. All other field writes (last_enriched_date stamp) proceeded.
- **Pellera Technologies follow-up flag:** 6 of 7 narrative enriched fields empty despite R2 FULL pass 2026-05-05 stamp in account_brief. Defer to a clean R2 FULL re-enrichment outside this sweep window; today's pass only filled segmentation_confidence (the immediately-fixable gap) + stamped last_enriched_date.

## Standout notable records (top 5 changes)

1. **FirstLight (300468012734)** — Promotion T4 → T2. Antin-owned Northeast/Mid-Atlantic regional wholesale fiber operator, 25K route miles, 660 employees. Long Haul / Backbone - Fiber operator default = T2. The prior `Municipal / Cooperative` sub-segment was a clear pre-Phase 3 misclassification.
2. **Mapletree (302234821315)** — Demotion T3 → T5 / segment reclass to Other. Singapore REIT investor (NOT operator). Closes one of the 5 known MSP/Aggregator + colo sub-segment data quality items (4 to go: Montera, PTS, Lonestar, LS Power).
3. **IREN (315977374429)** — Sub-segment reclass `AI Infrastructure providers - Neocloud` → `Crypto to AI - Neoclouds`. $9.7B Microsoft GPU cloud contract anchor. Tier unchanged at T1.
4. **Armstrong Group (303892660925)** — Name + domain rewrite (`armstronggroup.info` → `armstrongonewire.com`) + sub-segment Regional CLEC → Regional Cable Operator. One of the largest US regional MSOs, 400K+ homes across 6 states.
5. **Pellera Technologies (301784664824)** — Confidence fill empty → medium_7089. Recent merger entity (Converge + Mainline, 2025-07-21), MSP/Aggregator classification reasonable but flagged for proper R2 FULL re-enrichment post-sweep.

## HubSpot write results

5 batches of 10 via `manage_crm_objects` updateRequest with `confirmationStatus = CONFIRMATION_WAIVED_FOR_SESSION`:
- Batch 1/5 (records 1-10): 10/10 updated, 0 failed
- Batch 2/5 (records 11-20): 10/10 updated, 0 failed
- Batch 3/5 (records 21-30, includes FirstLight+Mapletree+Pellera MEDIUM): 10/10 updated, 0 failed
- Batch 4/5 (records 31-40, includes Armstrong MEDIUM): 10/10 updated, 0 failed
- Batch 5/5 (records 41-50, includes IREN MEDIUM): 10/10 updated, 0 failed

Total: 50/50, 0 errors, 0 retries needed. HubSpot company notes per §7.7 deferred (Slack DM + this audit log function as the audit trail — same pattern as batches 46-47).

## Continuation

- LAST_PROCESSED_HS_OBJECT_ID: 315977374429
- POOL_REMAINING (before batch 48): 459
- POOL_REMAINING (after batch 48): 409
- Drain progress: ~86% of sweep complete (2,395 / ~2,804 records assuming original ~2,854 pool less batch 47's 459 = 2,395 done)
- Next batch: 49 — ETA ~8 more batches at BATCH_SIZE=50

## Continuation token (for hands-off resume)

```
SWEEP_NAME=2026-05-18-post-phase-3-framework
SWEEP_KICKOFF_DATE=2026-05-18
NEXT_BATCH=49
BATCH_SIZE=50
APOLLO_ENFORCEMENT=disabled
SEGMENT_SCOPE=all_active_icp
POOL_REMAINING=409
HOLD_POLICY=NONE (best-effort classify)
SORT=hs_object_id ASC
LAST_PROCESSED_HS_OBJECT_ID=315977374429
```
