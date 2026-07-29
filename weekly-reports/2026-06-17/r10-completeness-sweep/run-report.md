# R10 Field Completeness Sweep — Run Report

**Date:** 2026-06-17 (Wed), ~1:46 PM CT
**Routine:** R10 Field Completeness Sweep (Cowork scheduled task, daily M-F 1:30 PM CT)
**Status:** ✅ SUCCESS — 1 record filled, 0 failed, 0 partials, 0 escalations
**Circuit breaker:** CLEAR

---

## Stage 0 — Preflight

- **MCP health:** HubSpot ✅, Slack ✅, web_search ✅, Apollo ✅ (all reachable).
- **Apollo budget:** `apollo-budget.json` week W25 (week_start 2026-06-15), consumed 2/850, remaining 848. `effective_apollo = min(25, 848) = 25`.
- **Canvas `F0B0AFSB9LN`:** read (1M+ char export). 84 active Tier 3 / standing-hold company IDs collected for the skip set (15 clean classification holds + 72 R3 dedup-pair IDs, deduped). None intersected today's pool.

## Stage 1 — Candidate pool + circuit breaker

Server-side trigger: 5 OR-combined `NOT_HAS_PROPERTY` filterGroups (`account_tier`, `signal_heat`, `account_brief`, `infrastructure_profile`, `company_sub_segment`), each AND'd with `customer_segment IN (6 ICPs)`. Using the `IN (6 ICPs)` filter cleanly excludes Flagged-for-deletion + Other + Partner Target server-side in one filter (no client-side drop needed for the loop fix). MaiaEdge own (124293230301) is non-ICP and excluded by the IN filter. Sort `last_enriched_date ASC`, cap 75.

**Circuit-breaker baseline.** Raw "active classified, non-flagged" pool = 3,386. ICP-only pool = **2,846**. 15% threshold (ICP) = ~427.

| Field | Raw active-classified blanks | ICP-scoped blanks | % of ICP pool | Breaker |
|---|---|---|---|---|
| `account_tier` | 5 | 0 | 0.0% | ok |
| `signal_heat` | 238 | 1 | 0.04% | ok |
| `account_brief` | 13 | 0 | 0.0% | ok |
| `infrastructure_profile` | 193 | 1 | 0.04% | ok |
| `company_sub_segment` | 488 | 0 | 0.0% | ok |

The large raw blanks (488 sub-segment, 238 heat, 193 infra) are **entirely non-ICP Other/Partner Target reference records**, which legitimately have no ICP sub-segment / ICP-classification enriched fields. ICP-scoped blanks are ≤1 per field. This confirms the **2026-06-08 loop fix is holding** (ICP `company_sub_segment` blanks = 0) and rules out a connector dropout. **Circuit breaker CLEAR.**

**Candidate pool: 1 record** — union of all 5 ICP triggers returned total = 1.

| ID | Name | Segment / sub-segment | Path | Missing fields |
|---|---|---|---|---|
| 167113651945 | Sumauma (Sumaúma Telecom) | MSP/Aggregator / Telecom Aggregator - MSP | B (enriched-field gap) | `infrastructure_profile`, `hyperscaler_proximity`, `provisioning_landscape`, `signal_heat` |

Sumauma is **not** in the 84 active canvas holds (its 2026-06-08 R4 mention was a transient preserved-contact hold, superseded by the generic count in later runs; not a standing company hold). `segmentation_confidence = high_90` (not manual_review), `last_enriched_date = 2026-05-18` (not stale, not today), `hs_is_target_account` not set (not frozen). Eligible.

## Stage 2 — Fill (enrich-first, tier-last)

**Sumauma (167113651945) — Path B.** Present + current (left untouched): `customer_segment` MSP/Aggregator, `company_sub_segment` Telecom Aggregator - MSP, `account_tier` tier_2, `segmentation_confidence` high_90, `account_brief`, `geographic_focus`, `fabric_provisioning_approach` homegrownproprietary_platform, `state` State of Sao Paulo, `country` Brazil, `hubspot_owner_id` 159350430 (Tim Ziemer / International — correct for Brazil).

Research-first fill of the 4 gaps:
- **`infrastructure_profile` = `None Identified`.** Web research (Lusha/ZoomInfo/B2Brazil/company site) confirms an asset-light telecom aggregator + software/technology-and-consulting provider to telecom carriers, "rather than operating as a direct fiber network or infrastructure operator." No disclosed owned facilities / route miles / POPs → sentinel.
- **`hyperscaler_proximity` = `None Known`.** Small Brazilian telecom-software/services firm; no disclosed hyperscaler on-ramp adjacency.
- **`provisioning_landscape`** (3 sentences, no em dashes, "carrier infrastructure" descriptor): asset-light aggregator on a homegrown proprietary platform, provisions by aggregating/integrating partner capacity across Brazil + LatAm; MaiaEdge angle = programmatic private connectivity to extend footprint without owning underlying paths.
- **`signal_heat` = `Cold`.** No signal history (`last_signal_date`/`score`/`count` all blank) and **0 associated deals** (open-deal check returned total 0) → Cold.

**Tier compute (last):** `account_tier` already tier_2 and not blank → no seed needed. Recompute is idempotent: MSP/Aggregator + "Telecom Aggregator - MSP" default = tier_2, no signal modifiers (Cold, no signal date, 0 open deals), not frozen. Computed tier == current tier → no write. No frozen-blank seed needed (tier not blank).

**Completeness Gate:** after the fill, ALL mandatory ICP fields present → **gate PASS** → `last_enriched_date` bumped to 2026-06-17 (full enrichment pass per Unified Stamping Policy). Sumauma drops out of the R10 pool permanently and re-enters the normal 120-day R2 rotation.

**Apollo:** 0 credits used (state/country/employees already present; no firmographic gap). Sub-cap 25 untouched. Weekly W25 remains 2/850.

## Stage 3 — Write

1 `manage_crm_objects` update, batch 1/1 OK (`updated:1, failed:0`), `CONFIRMATION_WAIVED_FOR_SESSION`. Read-back verified all 5 written fields landed and the untouched fields are intact.

## Data-quality flag for Cooper (surface, do not auto-fix)

**Sumauma (167113651945) — classification vs web tension.** The stored `account_brief` describes a residential ISP ("internet, TV, and voice services" to residential + business customers). Independent web sources (Lusha, ZoomInfo, B2Brazil) describe Sumaúma Telecom primarily as a **B2B telecom software / technology-solutions / consulting provider to other telecom carriers** — which reads closer to a software vendor/integrator than a "Telecom Aggregator" and, at the edge, could be a D1.x software disqualifier (→ Other) rather than an ICP MSP. Also a firmographic discrepancy: HubSpot `numberofemployees = 10` vs web 50-99 employees, ~$5-10M revenue. R10 did **not** reclassify or rewrite the brief (out of R10 scope; classification is high_90 from the 2026-05-18 Mass Re-Enrichment pass, and one web pass is insufficient to overturn it). Recommend a D7 / manual re-look at whether Sumauma is "Telecom Aggregator - MSP" vs Other, and an employee-count refresh. Gap fills are robust to the outcome (asset-light either way → `None Identified` / `None Known` hold).

## Stage 4 — Audit
- This on-disk report.
- Canvas `F0B0AFSB9LN` Run log: 1 row appended (✅).
- No standalone Slack DM (quiet-on-success; rolls into the 4:45 PM CRM Ops Daily Digest). No fatal abort, no circuit-breaker trip → no direct DM to Cooper.

## Tallies
- Pool: 1 | Filled: 1 | Partials held: 0 | Tiers seeded (frozen-blank): 0 | Evictions: 0
- Apollo: 0 / 25 | Writes: 1/1 OK | Circuit breaker: CLEAR | Run health: GREEN
