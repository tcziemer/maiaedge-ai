CRM Guardian - Stale Re-Enrichment - 2026-06-01 - 0 Tier 2 flagged, 0 Tier 3 held

Run summary: 0/100 processed · FULL 0 / LIGHT 0 / RECLASSIFY 0 / DEFER 0 · Tier 1 / 2 / 3 = 0 / 0 / 0 · Apollo: 0 credits used / 850 remaining · Freshness: GREEN

What needs Cooper's attention:
- None. 0-candidate GREEN run.

Run health: GREEN

Errors: None

---

Detail

Trigger query (today = 2026-06-01, 120-day cutoff = 2026-02-01):
- Filter group A (last_enriched_date < 2026-02-01, exclude Flagged for deletion + MaiaEdge own): 0 records.
- Filter group B (no last_enriched_date AND customer_segment populated, exclude Flagged for deletion): 1 raw record, but it is MaiaEdge own (124293230301), which is a hard stop. Excluded.
- Net candidate pool after hard-stop exclusion: 0.

Active company population: 3,124 (customer_segment NEQ "Flagged for deletion"). Full 120-day rotation is being held drained by the daily R-Tier-Audit + daily R2 cadence, as designed. This is the seventh consecutive 0-candidate R2 run (2026-05-25, 05-26, 05-27, 05-28, 05-29, and today). Records written by R1 over the past two weeks will not cross the 120-day threshold until ~late September 2026.

Cross-routine ledger (canvas F0B0AFSB9LN):
- R2 Tier 3 carryover queue: empty. Re-verified per the 2026-05-25 R2 audit (all 21 prior R2 holds resolved) and confirmed empty on every R2 run since. No R2 items to drain this run.
- Standing Tier 3 holds present in the canvas belong to R0/R1/R3 (gatco.net 324524875475, columbus-networks 324597786339, Verizon 325110366958 dedup) - not R2 scope, not acted on.

Apollo: 0 credits consumed. Sub-cap 50/run, used 0 of 50. Weekly W22: 0/850, 850 remaining.

Writes: 0 HubSpot writes, 0 segment changes, 0 tier/heat changes, 0 evictions, 0 MISDOMAIN corrections, 0 owner re-derives, 0 recent_news staleness clears.

Tier 3 held: none.
Partial Enrichment (gate failed): none.
Segment changes: none.

Delivery: quiet on success - no DM sent. On-disk run report + one Run-log row appended to canvas F0B0AFSB9LN. CRM Ops Daily Digest (4:45pm CT) will surface this run.
