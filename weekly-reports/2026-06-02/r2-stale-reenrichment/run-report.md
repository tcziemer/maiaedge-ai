CRM Guardian - Stale Re-Enrichment - 2026-06-02 - 0 Tier 2 flagged, 0 Tier 3 held

Run summary: 0/100 processed · FULL 0 / LIGHT 0 / RECLASSIFY 0 / DEFER 0 · Tier 1 0 / Tier 2 0 / Tier 3 0 · Apollo: 0/50 sub-cap (W23 0/850) · Freshness: GREEN

What needs Cooper's attention:
- Nothing. 0-net-candidate GREEN run. No holds, no evictions, no segment changes, no partial enrichments.

Run health: GREEN

Errors: None

---

## Trigger query result

Today (ET): 2026-06-02. 120-day cutoff: 2026-02-02.

- **Filter group A** (last_enriched_date < 2026-02-02, customer_segment NEQ "Flagged for deletion"): 0 records.
- **Filter group B** (last_enriched_date NOT_HAS_PROPERTY AND customer_segment HAS_PROPERTY, customer_segment NEQ "Flagged for deletion"): 1 raw record = MaiaEdge own (124293230301, maiaedge.io, customer_segment=Other). Hard-stopped by the routine (own record never written). Net candidates after hard-stop: 0.

Total candidates processed: 0. No Apollo spend, no HubSpot writes.

## CRM freshness

Total active company population (customer_segment NEQ "Flagged for deletion"): **3,121** records. At a 120-day rotation that is a ~26/day steady-state break-even; the daily R-Tier-Audit (M-F 3pm) + daily R2 (M-F 11am) cadence continues to hold the rotation pool fully drained.

This is the 8th consecutive 0-net-candidate R2 run (2026-05-25, 05-26, 05-27, 05-28, 05-29, 06-01, and today 06-02). Post-Mass-Re-Enrichment-Sweep + daily-cadence steady state remains **GREEN**. This morning's R1 (10:20am CT) wrote 5 net-new ICP records, but none cross the 120-day threshold until ~2026-09-29, so they do not enter the R2 pool today.

## Cross-routine ledger (canvas F0B0AFSB9LN)

- **Drain at run start:** R2-scoped Tier 3 carryover queue confirmed EMPTY (re-verified by the 2026-05-25 R2 audit and reaffirmed every R2 run since). Standing canvas Tier 3 holds are all R0/R1/R3 scope (gatco.net, columbus-networks/finetechnologies.co, Verizon 325110366958 dedup, Synnap, Spartan Data Centers, Attobahn, Tract Capital, plus today's three R1 dedup holds: Digital Fortress dfcolo.com, us.ntt.net, g.softbank.co.jp) - not R2's to drain. 0 R2 holds re-evaluated, 0 resolved.
- **Append at run end:** 0 new Tier 3 holds. One ✅ Run-log row appended.

## Apollo budget

Sub-cap 50/run, used 0 of 50. Weekly W23: 0/850, 850 remaining. No post-run JSON increment required (0 consumption).

## Detail tables

- Segment changes (old -> new): none.
- Tier 3 held: none.
- Partial Enrichment (gate failed): none.
- Recent news cleared (stale): none.
- Legacy format pending backfill: none surfaced (0 records read).
