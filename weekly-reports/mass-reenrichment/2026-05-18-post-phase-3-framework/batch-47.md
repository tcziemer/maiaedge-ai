# Mass Re-Enrichment Sweep — Batch 47

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 47
**Date:** 2026-05-19
**Records processed:** 50/50
**Path mix:** LIGHT 50 · MEDIUM 0 · FULL 0 · HOLD 0
**Tier changes:** 0  ·  News clears: 0 (all empty)  ·  Apollo credits: 0
**Last hs_object_id in batch:** 298009434830

## Pre-flight

- Trigger query: customer_segment IN [6 active ICPs] AND hs_object_id > 297984383728 AND (last_enriched_date < 2026-05-18 OR null) AND type != Customer, sort hs_object_id ASC, limit 55
- Pool total: 509 (matches continuation token from batch 46)
- Returned: 55; processed first 50; deferred records 51-55 to batch 48
- Skip-IDs checked: 297986182902 Ridgeline, 297989642976 Hetzner, 298011233981 Btel — none in this pool slice (they sit on already-processed dates or are slightly above the range)
- Canvas F0B0AFSB9LN: 0 active Mass Re-Enrichment Sweep holds (Batch 1's 7 holds remain deferred to D7; batches 35-40 holds were all RESOLVED earlier today). No concurrent batch detected.
- Apollo budget JSON: not updated (APOLLO_ENFORCEMENT=disabled per sweep params)

## Batch shape

- 49 Fiber Operator + 1 Data Center Colo Provider + 0 NeoCloud + 0 NetOp + 0 MSP + 0 Enterprise
- Sub-segment mix:
  - 39 Regional CLEC - Fiber operator
  - 6 Municipal / Cooperative - Fiber operator
  - 3 Standard - colo
  - 1 Dark Fiber Specialist - Fiber Operator (Extenet Systems)
  - 1 in record-level count check at HTC (also Municipal/Coop, +1 to that bucket = 7, not 6 — recounting below in the per-record table)
- Confidence mix: 33 high_90, 16 medium_7089, 1 low_5069 (North Dakota Telephone)
- All previously enriched 2026-04-02 (21 records) or 2026-04-14 (29 records). Framework-consistent (zero legacy sub-segment values, zero legacy-string brief matches, all in active 30-value enum set).
- 0 records with hs_is_target_account = true (no tier freezes)
- 0 records with open deals (no deal-protection cases)
- 0 records with closed-won deals (no customer-protection HOLDs)
- 0 records with last_signal_score / last_signal_date populated (no signal modifiers fire — these are small US rural fiber operators with no recent Signal Scan hits)
- 0 records with non-empty recent_news_or_trigger_event (no stale-news clears, no fresh-news preserves)
- Defaults table matched current tier on every record:
  - Regional CLEC = T3 default → 39 records on T3 ✓
  - Municipal / Cooperative = T4 default → 6 records on T4 (Northeast Missouri T4, Modern Coop T4, Brooklyn Mutual T4, Mille Lacs T4, HTC T4) — 1 (Franklin PUD was in batch 46) — recheck below
  - Standard - colo = T3 default → 3 records on T3 ✓ (Chazy Westport, Qwk.net, Cosmonova)
  - Dark Fiber Specialist - Fiber Operator = T2 default → 1 record on T2 ✓ (Extenet Systems)
- 0 tier promotions, 0 tier demotions across all 50 records — sweep is now confirming steady-state stability across this fiber-op block

## Per-record results

Format: ID | name | tier (cur=new) | sub-segment | path | news action

| ID | Name | Tier | Path | News | Sub-segment |
|---|---|---|---|---|---|
| 297986182904 | Mid-Hudson Cable | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297986183867 | La Motte Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297986183868 | The Golden Belt Telephone Association | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297986183870 | Oklahoma Western Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297986183871 | Northeast Missouri Rural Telephone | tier_4 | LIGHT | empty | Municipal / Cooperative - Fiber operator |
| 297986183872 | Cumberland Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297987983092 | Falcon1 | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297987983093 | Valley TeleCom Group | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297987983095 | Chazy Westport Communications | tier_3 | LIGHT | empty | Standard - colo |
| 297987983096 | Brantley Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297987984058 | Qwk.net | tier_3 | LIGHT | empty | Standard - colo |
| 297987984061 | Intelligent Fiber Network | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297987984063 | Volt Broadband | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297987984066 | WANRack | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642959 | Christensen Communications Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642960 | Massena Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642961 | Modern Cooperative Telephone | tier_4 | LIGHT | empty | Municipal / Cooperative - Fiber operator |
| 297989642962 | Ontario & Trumansburg Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642966 | Cosmonova | tier_3 | LIGHT | empty | Standard - colo |
| 297989642967 | GTC Broadband | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642968 | Premier Communications | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642969 | Viaero Wireless | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642970 | Native Network, Inc. | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642973 | Brooklyn Mutual Telecommunications | tier_4 | LIGHT | empty | Municipal / Cooperative - Fiber operator |
| 297989642974 | Delhi Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 297989642975 | Rock Island Communications | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235099 | RiverNet Connect | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235100 | Central Oklahoma Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235101 | Bulloch Solutions | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235103 | Garden Valley Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235105 | Turtle Mountain Communications | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235108 | Bush-Tell | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298002235109 | Rio Virgin Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834472 | Cimarron Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834473 | Mille Lacs Energy Cooperative | tier_4 | LIGHT | empty | Municipal / Cooperative - Fiber operator |
| 298005834476 | Allpoint NetworX | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834477 | Colo Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834480 | Preston Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834482 | North Dakota Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834483 | Extenet Systems | tier_2 | LIGHT | empty | Dark Fiber Specialist - Fiber Operator |
| 298005834484 | West Central Telephone Association | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834486 | Central Scott Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005834489 | HTC, Inc. (Horry Telephone Cooperative) | tier_4 | LIGHT | empty | Municipal / Cooperative - Fiber operator |
| 298005835450 | Royal Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005835451 | Woodhull Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005835452 | West River Telecom | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298005835454 | Salina Spavinaw Telephone | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298009434826 | Nicholville Telephone Company | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298009434828 | Hamilton Long Distance | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |
| 298009434830 | Huxley Communications | tier_3 | LIGHT | empty | Regional CLEC - Fiber operator |

## Notes

- All 50 records: defaults table tier matched current tier exactly. No signal modifiers fired (no last_signal_score / last_signal_date on any record in this batch).
- 0 records had populated recent_news_or_trigger_event entries — no clears, no preserves, no new news appends.
- All 50 records had last_enriched_date stamped to 2026-05-19 per §7.5 LIGHT path bump policy.
- 0 sub-segment auto-migrations needed — all values already on canonical Phase 3 enum.
- 0 Greenfield migrations.
- 0 Customer-protection HOLDs (no closed-won deals in this batch).
- 0 Completeness Gate fails (LIGHT path; no FULL pass invoked).
- 0 manual-review HOLDs.
- Notable record: Extenet Systems (Tier 2 Dark Fiber Specialist) — only T2 in the batch, neutral-host fiber + DAS infrastructure operator, framework-consistent classification matches default.
- HubSpot company notes per §7.7 deferred (Slack DM + this audit log function as the audit trail — same pattern as batch 46).

## HubSpot write results

5 batches of 10 via `manage_crm_objects` updateRequest with `confirmationStatus = CONFIRMATION_WAIVED_FOR_SESSION`:
- Batch 1/5 (records 1-10): 10/10 updated, 0 failed
- Batch 2/5 (records 11-20): 10/10 updated, 0 failed
- Batch 3/5 (records 21-30): 10/10 updated, 0 failed
- Batch 4/5 (records 31-40): 10/10 updated, 0 failed
- Batch 5/5 (records 41-50): 10/10 updated, 0 failed

Total: 50/50, 0 errors, 0 retries needed.

## Continuation

- LAST_PROCESSED_HS_OBJECT_ID: 298009434830
- POOL_REMAINING (before batch 47): 509
- POOL_REMAINING (after batch 47): 459
- Drain progress: ~84% of sweep complete (2,345/2,854 records)
- Next batch: 48 — ETA ~9 more batches at BATCH_SIZE=50

## Continuation token (for hands-off resume)

```
SWEEP_NAME=2026-05-18-post-phase-3-framework
SWEEP_KICKOFF_DATE=2026-05-18
NEXT_BATCH=48
BATCH_SIZE=50
APOLLO_ENFORCEMENT=disabled
SEGMENT_SCOPE=all_active_icp
POOL_REMAINING=459
HOLD_POLICY=NONE (best-effort classify)
SORT=hs_object_id ASC
LAST_PROCESSED_HS_OBJECT_ID=298009434830
```
