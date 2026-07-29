# R10 Field Completeness Sweep - Run Report

**Date:** 2026-06-09 (Tue) 1:30 PM CT
**Status:** ✅ SUCCESS (quiet-on-success; rolls into CRM Ops Daily Digest)
**Apollo:** 0 / 25 sub-cap used (all fills from existing account_brief research + canonical enums; 0 firmographic gaps). Weekly W24: 0/850.
**Circuit breaker:** CLEAR. Eligible ICP gap pool = 11 vs ~513 (15% of ~3,422 active). No connector-dropout pattern.

## Pool construction

- Raw trigger union (5 missing-field filterGroups, server filter `customer_segment HAS_PROPERTY AND NEQ "Flagged for deletion"`): **557 records**.
- Client-side exclusions:
  - 546 dropped: `customer_segment IN (Other, Partner Target)` — non-ICP loop-fix drop (358 Other + 188 Partner Target). Confirms the 2026-06-08 loop fix is holding; these can never satisfy the ICP-only `company_sub_segment` trigger.
  - 0 dropped for manual_review_required / enriched-today / 120d-stale / MaiaEdge own / canvas Tier 3 hold (none hit after the Other/Partner drop).
- **Eligible ICP pool: 11** (all under the 75 cap; no records deferred).

## What was filled

All 11 were **Path B enriched-field gaps** — each already carried `account_brief`, `company_sub_segment`, `account_tier`, `signal_heat`, and `segmentation_confidence`, but was missing the structured/narrative enriched fields. **`account_tier` was present on all 11, so NO tier/heat recompute was run** (gap-fill only; tier inputs untouched). Completeness Gate PASSED on all 11 after fill → `last_enriched_date` bumped to 2026-06-09.

Per-field gaps closed (capped pool):
- `infrastructure_profile`: 11
- `hyperscaler_proximity`: 11
- `fabric_provisioning_approach`: 11
- `provisioning_landscape`: 11
- `geographic_focus`: 5 missing filled + 1 corrected (Shaun Telecom)
- `state`: 1 missing filled (Shaun Telecom → Hong Kong) + 1 corrected (Internet Subway MI → VA, per its own brief's flagged Apollo HQ)

## Records (11) — all written, 0 failed

| ID | Name | Segment / Sub | Tier | infrastructure_profile | hyperscaler_proximity | fabric | Notes |
|---|---|---|---|---|---|---|---|
| 318106540781 | Trans Pacific Networks | Fiber Op / Subsea cable operator | tier_3 | Route Miles: Mid-Size (1K-10K) | None Known | manuallegacy_processes | Transpacific subsea SPV; operating-vs-financing role still D7-flagged. Bands estimated conservatively from brief. |
| 322362480354 | mStreet Fiber Indiana | Fiber Op / Regional CLEC | tier_3 | Route Miles: Small (<1K) | None Known | manuallegacy_processes | Wholesale FTTP central IN, GigabitNow retail layer. |
| 320373812935 | Eastern Plains Communications | Fiber Op / Regional CLEC | tier_3 | Route Miles: Small (<1K) | None Known | manuallegacy_processes | Rural E. Colorado co-op, RDOF/USDA. |
| 319765072627 | Shaun Telecom | MSP/Aggregator / Telecom Aggregator | tier_2 | None Identified | None Known | manuallegacy_processes | Asset-light voice aggregator. **state filled = Hong Kong; geographic_focus CORRECTED (prior "HQ: US, USA" contradicted country=Hong Kong + APAC/MENA brief).** |
| 320373812938 | Internet Subway | Fiber Op / Regional CLEC | tier_3 | Route Miles: Small (<1K) | None Known | manuallegacy_processes | MDU/multifamily ISP. **state corrected MI → Virginia** per brief's Apollo HQ (both East/Tim Lieto; no owner change). |
| 316529844930 | Data Access Solutions | Fiber Op / Regional CLEC | tier_3 | POPs: Small (<10) | Existing Facility Nearby | standard_ossbss_stack | Toronto VoIP wholesale POP; geographic_focus filled. **Note: brief narrative claims a prior migration to Network Operator/External Extension, but live fields show Fiber Op/Regional CLEC — R10 does not reclassify; left segment as-is, flagged for review.** |
| 316427027134 | Armada | DC Colo / Modular - colo | tier_1 | Facilities: Mid-Size (5-19) | Existing Facility Nearby | homegrownproprietary_platform | Modular edge DCs, Atlas platform; geographic_focus filled. Facility band conservative (2022 startup, flagship deployments). |
| 319765072625 | Red Telecom | MSP/Aggregator / Telecom Aggregator | tier_2 | None Identified | None Known | standard_ossbss_stack | Asset-light US wholesale voice carrier. |
| 319147562721 | Lynch Interactive (LICT) | Network Op / Tier 1 Carrier | tier_1 | Facilities: Mid-Size (5-19);Route Miles: Mid-Size (1K-10K) | None Known | standard_ossbss_stack | US rural ILEC holding co; geographic_focus filled. hs_is_target_account now false (tier already present anyway). |
| 321479592663 | Worldpay | Enterprise / Financial Services | tier_3 | Facilities: Mid-Size (5-19) | Existing Facility Nearby | manuallegacy_processes | $4.9B multi-DC payments; geographic_focus filled. fabric = manuallegacy_processes (traditional enterprise DCI; no confirmed external NaaS evidence). |
| 317660211918 | Provocative Science | DC Colo / Greenfield | tier_1 | Facilities: Small (<5) | None Known | none_identified | Seed-stage greenfield, pre-operational, active MaiaEdge pilot; geographic_focus filled. |

## Tiers seeded / frozen-blank seeds resolved
- None. No blank `account_tier` in the eligible pool (all 11 already tiered).

## Partials held for next run
- None. All 11 passed the Completeness Gate.

## Assumptions noted (autonomous run)
- `infrastructure_profile` bands and `provisioning_landscape` narratives were derived from each record's recent `account_brief` (dated 2026-05-18 to 2026-06-03) rather than fresh web pulls, since the briefs already carry the firmographic/infrastructure detail and Apollo was not needed. Conservative bands used where the brief was thin (TPN subsea, Armada facility count, Provocative pre-op).
- Data Access Solutions segment/sub mismatch (brief vs live fields) surfaced for review, not changed — R10 fills gaps and does not reclassify a populated `customer_segment`.
