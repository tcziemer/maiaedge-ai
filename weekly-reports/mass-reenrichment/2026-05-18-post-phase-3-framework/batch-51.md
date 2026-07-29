# Mass Re-Enrichment Sweep — Batch 51

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 51
**Date:** 2026-05-19
**Kickoff date:** 2026-05-18
**Records processed:** 50/50
**HubSpot writes succeeded:** 50/50 (5 batches of 10)
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled)

## Path mix

- LIGHT: 16 (clean records, 7 fields populated or 1-blank-tolerated)
- LIGHT+audit: 34 (Pellera-pattern target-account Network Op records with 6 blank narrative fields - flagged for post-sweep R2 FULL re-enrichment)
- MEDIUM: 0
- FULL: 0
- HOLD: 0

## Tier writes

- Promotions (toward Tier 1): 0
- Demotions (toward Tier 5): 0
- Skipped (hs_is_target_account=true): 35
- All current tiers match defaults table (idempotent no-op for non-target records)

## Sub-segment auto-migrations

- 0 legacy values detected. All 50 sub-segments are in the 30 active values.

## Segment changes

- 0 cascades fired.

## Customer-protection HOLDs

- 0 closed-won downgrade attempts.

## Side-actions

- recent_news_or_trigger_event cleared on 7 records (stale >90d with no Signal Scan write ≤7d, or '[Date needed]' placeholder):
  - SCTelcom (320875892410) — 717d stale (2024-06)
  - Jefferson Telephone (320873012923) — 138d stale (2026-01)
  - Taylor Telephone Cooperative (320875891449) — '[Date needed]' placeholder
  - South Central Rural Telecommunications Cooperative (320960333518) — 687d stale (2024-07)
  - LigTel Communications (320876610255) — 1326d stale (2022-05)
  - Grantsburg Telcom (320876610252) — 1234d stale (2023-01)
  - TEC (322843549398) — 322d stale (2025-07)

## LIGHT+audit flagged for post-sweep R2 FULL re-enrichment (Pellera-pattern)

These 34 target-account Network Operator Tier 1 carriers (Africa, MENA, Asia, LatAm) have 6 blank core narrative fields (account_brief, geographic_focus, infrastructure_profile, hyperscaler_proximity, fabric_provisioning_approach, provisioning_landscape — only recent_news_or_trigger_event populated, often without date prefix). Same field-write gap pattern Cooper saw in batch 50.

| ID | Name | Sub-segment | Tier |
|---|---|---|---|
| 319190679238 | Mascom Botswana | Tier 1 Carrier - Network Op | tier_2 |
| 319208245977 | Gigared Argentina | Regional Cable Operator - Fiber operator | tier_2 |
| 319208231662 | LinkNet / First Media | Tier 1 Carrier - Network Op | tier_1 |
| 319194127065 | MTC Namibia Wholesale | Pure Wholesale Carrier - Network Op | tier_2 |
| 319182129900 | Jawwal | Tier 1 Carrier - Network Op | tier_2 |
| 319208253171 | Ooredoo Tunisia Wholesale | Pure Wholesale Carrier - Network Op | tier_2 |
| 319208253163 | Korek Telecom Wholesale | Pure Wholesale Carrier - Network Op | tier_2 |
| 319208245976 | Copaco Paraguay | Tier 1 Carrier - Network Op | tier_2 |
| 319208234736 | Telecom Egypt Wholesale | Pure Wholesale Carrier - Network Op | tier_1 |
| 319204695772 | VNPT International | Pure Wholesale Carrier - Network Op | tier_1 |
| 319197768407 | Topnet | Tier 1 Carrier - Network Op | tier_2 |
| 319204712150 | Viva Bolivia NuevaTel | Tier 1 Carrier - Network Op | tier_2 |
| 319197747921 | Vodafone Egypt Wholesale | Pure Wholesale Carrier - Network Op | tier_1 |
| 319190618824 | SRR (SFR Reunion) | Tier 1 Carrier - Network Op | tier_1 |
| 319194089196 | Stc Kuwait Wholesale | Pure Wholesale Carrier - Network Op | tier_2 |
| 319197746887 | Dito Telecommunity | Tier 1 Carrier - Network Op | tier_1 |
| 319194072771 | GO Malta | Tier 1 Carrier - Network Op | tier_1 |
| 319194071775 | Dialog Axiata Wholesale | Pure Wholesale Carrier - Network Op | tier_1 |
| 319190610665 | ePLDT | Tier 1 Carrier - Network Op | tier_1 |
| 319182137025 | Superonline | Tier 1 Carrier - Network Op | tier_2 |
| 319190627051 | GTT Guyana | Tier 1 Carrier - Network Op | tier_2 |
| 319190617847 | Algar Telecom Brasil | Tier 1 Carrier - Network Op | tier_1 |
| 319182106324 | Lao Telecom | Tier 1 Carrier - Network Op | tier_1 |
| 319173058272 | Touch Lebanon | Tier 1 Carrier - Network Op | tier_2 |
| 319176699599 | AIS (Advanced Info Service) | Tier 1 Carrier - Network Op | tier_1 |
| 319176778433 | Movicel Angola | Tier 1 Carrier - Network Op | tier_3 |
| 319182204602 | Paratus Zambia | Tier 1 Carrier - Network Op | tier_2 |
| 319176780504 | NetCo Lebanon | Tier 1 Carrier - Network Op | tier_3 |
| 319182114512 | RACSA Costa Rica | Tier 1 Carrier - Network Op | tier_1 |
| 319182163678 | Solusi Tunas Pratama | Tier 1 Carrier - Network Op | tier_2 |
| 319176782542 | Myanmar Net | Tier 1 Carrier - Network Op | tier_3 |
| 319182206700 | BVI Phones | Tier 1 Carrier - Network Op | tier_3 |
| 319176763117 | Emtel | Tier 1 Carrier - Network Op | tier_2 |
| 319182219973 | PDS Pacific Data Systems | Tier 1 Carrier - Network Op | tier_3 |

## Per-record audit log (all 50)

| ID | Name | Path | Segment | Sub-segment | Tier | Target | News cleared |
|---|---|---|---|---|---|---|---|
| 320875892410 | SCTelcom | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | Y |
| 320873012923 | Jefferson Telephone | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | Y |
| 322370821859 | Blackburn Networks | LIGHT | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | N |  |
| 322837060291 | Aristotle Unified Communications Inc. | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N |  |
| 323221078719 | NetSource Communications | LIGHT | Data Center Colo Provider | Standard - colo | tier_3 | N |  |
| 322761764553 | Angola Cables | LIGHT | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | N |  |
| 322837059320 | Telekom | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N |  |
| 320873732837 | EllaLink | LIGHT | Network Operator(Tier 1 / VNO) | Subsea cable operator | tier_2 | Y |  |
| 320876610273 | Ringgold Telephone Company | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N |  |
| 320875891449 | Taylor Telephone Cooperative | LIGHT | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | N | Y |
| 320874452693 | GVTC Communications | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N |  |
| 320960333518 | South Central Rural Telecommunications Cooperative | LIGHT | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | N | Y |
| 320876610255 | LigTel Communications | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | Y |
| 320876610252 | Grantsburg Telcom | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | Y |
| 320873011948 | DNA Communications | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N |  |
| 322843549398 | TEC | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | Y |
| 319190679238 | Mascom Botswana | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319208245977 | Gigared Argentina | LIGHT+audit | Fiber Operator | Regional Cable Operator - Fiber operator | tier_2 | Y |  |
| 319208231662 | LinkNet / First Media | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319194127065 | MTC Namibia Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_2 | Y |  |
| 319182129900 | Jawwal | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319208253171 | Ooredoo Tunisia Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_2 | Y |  |
| 319208253163 | Korek Telecom Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_2 | Y |  |
| 319208245976 | Copaco Paraguay | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319208234736 | Telecom Egypt Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_1 | Y |  |
| 319204695772 | VNPT International | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_1 | Y |  |
| 319197768407 | Topnet | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319204712150 | Viva Bolivia NuevaTel | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319197747921 | Vodafone Egypt Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_1 | Y |  |
| 319190618824 | SRR (SFR Reunion) | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319194089196 | Stc Kuwait Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_2 | Y |  |
| 319197746887 | Dito Telecommunity | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319194072771 | GO Malta | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319194071775 | Dialog Axiata Wholesale | LIGHT+audit | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_1 | Y |  |
| 319190610665 | ePLDT | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319182137025 | Superonline | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319190627051 | GTT Guyana | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319190617847 | Algar Telecom Brasil | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319182106324 | Lao Telecom | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319173058272 | Touch Lebanon | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319176699599 | AIS (Advanced Info Service) | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319176778433 | Movicel Angola | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y |  |
| 319182204602 | Paratus Zambia | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319176780504 | NetCo Lebanon | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y |  |
| 319182114512 | RACSA Costa Rica | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | Y |  |
| 319182163678 | Solusi Tunas Pratama | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319176782542 | Myanmar Net | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y |  |
| 319182206700 | BVI Phones | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y |  |
| 319176763117 | Emtel | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y |  |
| 319182219973 | PDS Pacific Data Systems | LIGHT+audit | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y |  |

## Drain status

- Pool before batch 51: 309 records
- Pool after batch 51: ~259 records (50 stamped to 2026-05-19, fall out of trigger query)
- Sweep cumulative: ~2,595 / 2,854 (~91%)
- ETA: ~6 more batches at BATCH_SIZE=50

## Run health

:large_green_circle: GREEN — 50/50 HubSpot writes succeeded across 5 batches of 10. 0 errors, 0 retries needed.

## Notable observations

1. Batch 51 was heavy on Africa/MENA/Asia/LatAm Network Operator Tier 1 target-account records — 34 of 50 records (68%) match the Pellera-pattern from batch 50. Same prior-run field-write gap (6 of 7 narrative fields blank, only recent_news_or_trigger_event populated). Confirms the systemic pattern.
2. 7 records had stale recent_news_or_trigger_event content (range: 138 days to 1326 days old). All cleared. The 1326-day staleness on LigTel (May 2022) suggests these were initial enrichment imports that never got refreshed.
3. EllaLink (320873732837) is a target-account Subsea cable operator at tier_2 — sits within the [1,3] ceiling/floor range. Sub-segment was correctly assigned during 2026-05-14 Phase 3 anchor verification (added 30th sub-segment).
4. 0 tier changes this batch (all current tiers match defaults; no signal modifiers fired). High idempotency = clean prior R-Tier-Audit + Phase 3 migration.
