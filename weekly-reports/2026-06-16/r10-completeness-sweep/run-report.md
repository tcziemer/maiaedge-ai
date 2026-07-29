# R10 Field Completeness Sweep — Run Report

**Date:** 2026-06-16 13:45 CT (Tuesday)
**Run type:** Scheduled (daily M-F 1:30 PM CT)
**Outcome:** ⚠️ CIRCUIT-BREAKER HOLD — 0 HubSpot writes, 0 Apollo credits
**Operator note:** Trigger pool clean (0 candidates). A diligence check on the non-trigger mandatory fields tripped the >15% circuit breaker on `hyperscaler_proximity`. Held per spec; escalated to Cooper.

---

## Stage 0 — Preflight

- **HubSpot MCP:** healthy (company search returned, total 3,755 companies).
- **Apollo budget:** W25 (week_start 2026-06-15), cap 850, consumed 2, **remaining 848**. `effective_apollo = min(25, 848) = 25`. Not used this run.
- **Canvas F0B0AFSB9LN:** read (via subagent — canvas is ~1.05M chars, over the read-token limit). Standing Tier 3 hold IDs collected (R0 9, R2 6, R4 23, R3 dedup pairs, D7). None became relevant — see Stage 1 (no write candidates).
- **Reference files:** `tier-compute-spec.md` + `sub-segment-qualification.md` loaded.

## Stage 1 — Candidate pool + circuit breaker

**Baseline active ICP pool** (`customer_segment IN` the 6 ICP values): **2,852 records.**

**Trigger query** (5 OR filterGroups, each `<field> NOT_HAS_PROPERTY` AND `customer_segment IN` 6 ICP values; this enforces ICP-only server-side and supersedes the spec's client-side Other/Partner drop, within the 18-filter cap at 10 filters):

| Trigger field | Blank count (ICP pool) |
|---|---|
| `account_tier` | 0 |
| `account_brief` | 0 |
| `infrastructure_profile` | 0 |
| `company_sub_segment` | 0 |
| `signal_heat` | 0 |
| **Union total** | **0 candidates** |

R10's chartered 5-field trigger is **fully clean** — every active ICP record carries all five. Nothing to fill in R10's designed scope. (Consistent with R1/R2 draining daily + R10 running daily since 2026-06-04.)

**Diligence check — non-trigger mandatory fields** (a record can have all 5 trigger fields yet miss one of these; the trigger does not independently query them):

| Field | Blank count | % of 2,852 | vs 15% breaker (~428) |
|---|---|---:|---|
| `hyperscaler_proximity` | **1,655** | **58.0%** | **TRIPS** |
| `fabric_provisioning_approach` | 416 | 14.6% | borderline (under) |
| `provisioning_landscape` | 386 | 13.5% | under |
| `geographic_focus` | 215 | 7.5% | under |
| `segmentation_confidence` | 36 | 1.3% | under |

**Circuit breaker: TRIPPED** on `hyperscaler_proximity` (58% >> 15%). Per the R10 connector-dropout guard: do not mass-fill; hold; save dry-run report; DM Cooper.

## Diagnostic — dropout vs. historical backlog

Ran read-only diagnostics to characterize the spike before asserting a cause (per the no-fabrication / verify-before-claiming discipline). Load-bearing assumption tested: *if this were a live connector dropout, recently-enriched records would now show the field blank.*

**Segment cross-tab (where `hyperscaler_proximity` is most applicable):**

| Segment | Total | Blank | % blank |
|---|---:|---:|---:|
| Data Center Colo Provider | 479 | 400 | 83.5% |
| NeoCloud | 188 | 104 | 55.3% |

**Recency:** records with `last_enriched_date >= 2026-06-09` (last 7 days) AND `hyperscaler_proximity` blank = **8** only.

**Spot-check of 9 named records enriched 2026-05-18 → 2026-06-15** (from R1/R2 run notes) — all carry `hyperscaler_proximity`:

| Record | Segment | last_enriched | hyperscaler_proximity |
|---|---|---|---|
| Cyfuture (326866083559) | Colo | 2026-06-10 | `Existing Facility Nearby` |
| ResetData (324591600333) | NeoCloud | 2026-05-26 | `None Known` |
| SoftBank AI Cloud (324007728852) | NeoCloud | 2026-05-18 | `Existing Facility Nearby` |
| Optum (325636927166) | Enterprise | 2026-06-03 | `None Known` |
| AcceleCom (326325637881) | Fiber | 2026-06-05 | `None Known` |
| Broadstar (323981908725) | Fiber | 2026-06-04 | `None Known` |
| Jefferson Telecom (327225613026) | Fiber | 2026-06-15 | `None Known` |
| BTC Broadband (326286037697) | Fiber* | 2026-06-05 | `None Known` |
| Integrity Advanced Technologies (327026419390) | MSP | 2026-06-12 | `None Known` |

\* BTC Broadband now shows `customer_segment = "Flagged for deletion"` while retaining ICP sub-segment/tier — a separate anomaly noted for R4/R-Tier-Audit, not in scope here.

**Conclusion (high confidence): historical backfill gap, NOT a live connector dropout.**
- A live read-dropout would show recent enrichments blank — instead 9/9 spot-checked recent records carry the field and only 8 of the last-7-day cohort are blank.
- The connector reads the field correctly (the `get_crm_objects` above returned real values), so the 1,655 are genuinely unset in HubSpot.
- The field is populated broadly on recent passes across ALL segments; the blanks are the older/legacy cohort whose last enrichment predates wide adoption of this field (or the May migration / Mass Re-Enrichment populated the other 7 enriched fields but under-filled this one).
- The same pattern (older-cohort under-fill) explains the secondary fields `fabric_provisioning_approach` (14.6%), `provisioning_landscape` (13.5%), `geographic_focus` (7.5%).

**Tier-correctness impact: none.** `hyperscaler_proximity` is not a `compute_tier` input (`infrastructure_profile` is the primary structured input, and it is 0% blank across the pool). Blank `hyperscaler_proximity` does not produce wrong tiers; this is an enrichment-completeness gap, not a tiering risk.

## Stage 2 / 3 — Fill / Write

**Not executed. 0 HubSpot writes, 0 Apollo credits.**

Rationale for holding rather than filling:
1. **Breaker policy** is hold-not-fill on a pool-wide single-field blank spike.
2. **Out of R10 scope by design** — these 1,655 records all carry the 5 trigger fields, so they never enter R10's pool through the trigger. Filling them would be inventing scope beyond the spec.
3. **Scale** — 1,655 records is far past R10's 75/run cap, and `hyperscaler_proximity` is a per-record research decision (`Existing Facility Nearby` vs `None Known` depends on each company's DC locations vs hyperscaler availability zones), not a default to stamp unattended.

## Stage 4 — Audit

- This report: `weekly-reports/2026-06-16/r10-completeness-sweep/run-report.md`
- Canvas F0B0AFSB9LN: Run log row appended (status ⚠️).
- Slack: direct DM to Cooper (`U0A24D9RJLS`) — circuit-breaker escalation. (Not the usual quiet-on-success path.)

## Recommendation for Cooper

The daily R10 micro-fill is the wrong tool for a 1,655-record structural backlog. Options:
1. **Targeted backfill sweep** — a Mass Re-Enrichment-style or R2 Filter-C variant that prioritizes `hyperscaler_proximity` / `fabric_provisioning_approach` / `provisioning_landscape` blanks on the legacy cohort (oldest `last_enriched_date` first), so the backlog drains on a controlled cadence with Apollo budget allocated.
2. **Confirm-and-ignore** — if the legacy blanks are acceptable (they don't affect tiering and recent enrichment fills the field going forward), R10 will keep passing them over since they're outside its trigger; the backlog erodes naturally as R2's 120-day rotation re-enriches each record.
3. **Trigger redesign** — add `hyperscaler_proximity` (and/or the other non-trigger forced fields) to R10's Stage 1 trigger so the daily sweep actually catches them — but only paired with a per-run cap that drains the backlog over weeks, not all at once.

Open question for Cooper: is the legacy under-fill of `hyperscaler_proximity` expected (field adopted after most records' last enrichment), or unexpected? That determines whether to schedule (1) or accept (2).
