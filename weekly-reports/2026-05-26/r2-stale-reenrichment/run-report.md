# R2 Stale Re-Enrichment - 2026-05-26

**Status:** GREEN - Zero-candidate run
**Run start:** 2026-05-26 11:05 ET (Cowork scheduled task fire)
**Today's ET date:** 2026-05-26
**120-day stale cutoff:** 2026-01-26

---

## Trigger query result

| Filter group | Definition | Records returned |
|---|---|---:|
| A | `last_enriched_date < 2026-01-26` AND `customer_segment NEQ "Flagged for deletion"` AND `hs_object_id NEQ 124293230301` | **0** |
| B | `last_enriched_date NOT_HAS_PROPERTY` AND `customer_segment HAS_PROPERTY` AND `customer_segment NEQ "Flagged for deletion"` AND `hs_object_id NEQ 124293230301` | **0** |
| A OR B (canonical R2 trigger) | | **0** |

Verification probes:

- Filter B without the MaiaEdge own exclude: 1 record returned (MaiaEdge own `124293230301`, hard-stopped by the routine). Confirms the 1 never-enriched-with-segment record in the CRM is the MaiaEdge own record - correctly held out.
- Total active company population (customer_segment HAS_PROPERTY AND NEQ "Flagged for deletion"): **3,025 records**.

---

## What was processed

Zero records. No HubSpot writes, no Apollo spend, no segment changes, no evictions, no Tier 3 holds added.

---

## Cross-routine ledger state

- **R2 Tier 3 carryovers from canvas F0B0AFSB9LN at run start:** 0 standing
  - Yesterday's 2026-05-25 R2 run re-verified that all 21 prior R2 carryovers had been resolved (14 by Mass Re-Enrichment Sweep 2026-05-18/19, 7 removed from HubSpot entirely). The R2 Tier 3 queue is empty at steady state.
- **New R2 Tier 3 holds this run:** 0
- **Same-day cross-routine collisions:** None. Today's R1 added 4 NEW Tier 3 holds (Synnap, Spartan Data Centers, Attobahn, GATCO) but those are net-new accounts that have never been enriched and therefore could not have appeared in R2's stale pool.

---

## Apollo budget

- **Sub-cap:** 50 credits/run
- **Used this run:** 0
- **Weekly W22:** 0/850, 850 remaining

---

## Steady-state interpretation

The 0-candidate result matches yesterday's R2 (also 0). The CRM rotation pool is being held drained by the combination of:

1. The 2026-05-18/19 Mass Re-Enrichment Sweep which re-stamped most active records.
2. R-Tier-Audit running daily M-F (tier+heat-only, no Apollo, no enrichment-date bump - but still keeps tier/heat fresh).
3. R2 running daily M-F to catch anything that crosses the 120-day line.
4. R1 daily M-F draining any fresh imports as they arrive.

At 5,000-record active CRM and 120-day rotation, break-even is ~42 records/day. With the rotation pool drained by Mass Re-Enrichment Sweep, the next ~120 days will see a slow ramp back up as records age past the 2026-01-26+sweep_dates cutoff line. Until that ramp hits steady state, R2 daily runs will continue to show 0-3 candidates.

---

## Run health

GREEN.

- All trigger query probes returned cleanly.
- Apollo budget tracker updated locally (0 cr consumed - no commit needed beyond JSON write).
- Canvas update pending (append run-log row only; no Tier 3 list update needed).
- Slack DM to Cooper (`U0A24D9RJLS`) sent.

---

## Errors

None.
