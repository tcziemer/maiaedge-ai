# R10 Field Completeness Sweep — Run Report

**Date:** 2026-06-10 (Wed) 13:32 CT
**Status:** ✅ SUCCESS — zero ICP candidates (pool fully drained)
**Apollo used:** 0 / 25 sub-cap (W24 weekly 0/850, 850 remaining)
**Circuit breaker:** NOT tripped (see note below)

## Stage 0 — Preflight
- HubSpot healthy: 3,411 active companies (customer_segment set, not Flagged).
- Apollo budget read: W24, consumed 0, effective_apollo = min(25, 850) = 25.
- Canvas F0B0AFSB9LN read: conservative skip-superset of 757 distinct HubSpot IDs collected (Tier 3 holds + historical mentions).

## Stage 1 — Candidate pool
- Trigger: 5 OR'd NOT_HAS_PROPERTY groups (account_tier / account_brief / infrastructure_profile / company_sub_segment / signal_heat), each AND `customer_segment NEQ "Flagged for deletion"`. Sort last_enriched_date ASC (nulls first).
- Server union total: **560 records** (549 unique fetched across 3 pages; ~11 multi-trigger dupes).
- Client-side segment breakdown of the union:
  - Other: 354
  - Partner Target: 180
  - blank customer_segment: 15
  - **ICP (6 segments): 0**
- Exclusions applied:
  - Non-ICP (Other / Partner Target): 534 dropped (2026-06-08 loop fix — applied client-side per the 18-filter cap).
  - Blank customer_segment: 15 dropped (R1 Fresh Enrichment owns these).
  - manual_review_required / enriched-today / stale-R2-window (<2026-02-10) / MaiaEdge own / canvas Tier 3 holds: 0 incremental (no ICP records reached these checks).

## Stage 1 — Circuit breaker
- The largest single-field gap in the union is `company_sub_segment` (~534 records, >15% of 3,411). This is **NOT** a connector dropout: every one of those records is an `Other`/`Partner Target` non-ICP reference, which structurally has no valid ICP `company_sub_segment` value and is excluded at the trigger by design. **Zero ICP records show the gap.** No hold, no Cooper DM — working as intended.

## Stage 2/3 — Fill + Write
- **0 candidates → 0 fills, 0 HubSpot writes.**
- Tiers seeded (incl. frozen-blank seed-once): 0
- signal_heat defaults written: 0
- Enriched-field fills: 0
- Apollo firmographic fills: 0
- Partials held for next run: 0
- last_enriched_date bumps: 0

## Field gap counts (ICP pool)
| Field | ICP records missing |
|---|---|
| account_tier | 0 |
| account_brief | 0 |
| infrastructure_profile | 0 |
| company_sub_segment | 0 |
| signal_heat | 0 |
| geographic_focus | 0 |
| hyperscaler_proximity | 0 |
| fabric_provisioning_approach | 0 |
| provisioning_landscape | 0 |
| segmentation_confidence | 0 |

## Interpretation
Every classified ICP record carries all five trigger-completeness fields. R1 (daily), R2 (120-day rotation + Filter-C pre-spread), and R-Tier-Audit (daily) are holding the ICP pool complete; the only union members are the known, excluded non-ICP reference population. No action required. Quiet-on-success — rolls into the 4:45 PM CRM Ops Daily Digest; no standalone DM sent.
