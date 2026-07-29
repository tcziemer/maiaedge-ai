# R2 Stale Re-Enrichment - 2026-05-29

**Status:** GREEN - Zero-candidate run
**Run start:** 2026-05-29 ~11:00 ET (Cowork scheduled task fire)
**Today's ET date:** 2026-05-29
**120-day stale cutoff:** 2026-01-29

---

## Trigger query result

| Filter group | Definition | Records returned |
|---|---|---:|
| A | `last_enriched_date < 2026-01-29` AND `customer_segment NEQ "Flagged for deletion"` AND `hs_object_id NEQ 124293230301` | **0** |
| B | `last_enriched_date NOT_HAS_PROPERTY` AND `customer_segment HAS_PROPERTY` AND `customer_segment NEQ "Flagged for deletion"` AND `hs_object_id NEQ 124293230301` | **0** |
| A OR B (canonical R2 trigger) | | **0** |

Verification probes:

- Canonical A-OR-B query (without the MaiaEdge own exclude) returned exactly **1** record: MaiaEdge own (`124293230301`), matched via group B (blank `last_enriched_date`, `customer_segment = "Other"`). Hard-stopped by the routine - never written. Confirms the only never-enriched-with-segment record in the CRM is the MaiaEdge own record, correctly held out.
- Standalone Filter A probe (`last_enriched_date < 2026-01-29`, not flagged): **0** records - confirms the date filter is functioning and nothing has aged past the 120-day line.
- Total active company population (`customer_segment HAS_PROPERTY` AND `NEQ "Flagged for deletion"`): **3,110 records** (matches the CRM scale baseline; up from 3,025 on 2026-05-26 as sourcing/import continues).

---

## What was processed

Zero records. No HubSpot writes, no Apollo spend, no segment changes, no evictions, no Tier 3 holds added. No `last_enriched_date` bumps.

---

## Cross-routine ledger state (canvas F0B0AFSB9LN)

- **R2 Tier 3 carryovers at run start:** 0 standing. The R2 Tier 3 queue has been empty at steady state since 2026-05-22 (confirmed by the 2026-05-26 and 2026-05-27 ledger entries). Nothing to drain or re-evaluate this run.
- **New R2 Tier 3 holds this run:** 0
- **Same-day cross-routine collisions:** None. R2 returned no candidates, so no overlap with R0/R1/R4 was possible.

---

## Apollo budget

- **Sub-cap:** 50 credits/run
- **Used this run:** 0
- **Weekly W22 (started 2026-05-25):** 0/850, 850 remaining

---

## Steady-state interpretation

The 0-candidate result is consistent with the 2026-05-26 and 2026-05-27 R2 runs (both 0). The rotation pool remains drained by the combination of:

1. The 2026-05-18/19 Mass Re-Enrichment Sweep, which re-stamped most active records.
2. The mid-May Account Tiering & Segmentation Overhaul migration, which touched the bulk of the active pool.
3. R2 + R-Tier-Audit + R1 running daily M-F to keep the pool fresh and drain fresh imports as they arrive.

The earliest `last_enriched_date` values in the active pool are all later than 2026-01-29, so nothing has crossed the 120-day staleness line yet. The next rotation wave will ramp up gradually beginning ~mid-September 2026 (120 days after the mid-May migration/sweep). Until then, daily R2 runs will continue to show 0-3 candidates.

---

## Run health

GREEN.

- All trigger query probes returned cleanly; date filter verified functioning.
- Apollo budget tracker: 0 cr consumed (history note appended; no commit needed beyond JSON write).
- Canvas F0B0AFSB9LN: run-log row appended; no Tier 3 list update needed (queue empty).
- Slack DM to Cooper (`U0A24D9RJLS`) sent.

---

## Errors

None.
