CRM Guardian - Fresh Enrichment - 2026-06-01 - 2/100 processed · 1 Tier 3 held

*Pool:* 2 candidates (8 raw, 6 standing Tier 3 excluded) · cap 100 · drain projection: 0 days (pool drained; 1 frozen-tier loop record awaits Cooper, not R1-drainable)

*Path counts (this run):*
- Path α full enrichment: 0 processed (the 1 fresh Filter-Group-A record resolved to a Stage 0 dedup Tier 3 hold before enrichment)
- Path β re-research: 1 processed (ResetData) → 0 reclassified, 0 Tier 3 holds (frozen-tier no-op)
- Path γ eviction: 0 processed

*Apollo:* 0 credits this run · 0/850 weekly · 850 remaining for week
*Git:* deferred (concurrent routine); JSON updated locally

*Path α - Full ICP enrichments (named, grouped by segment):*
None this run.

*Path β - Top 5 reclassifications:*
None. ResetData (324591600333) re-evaluated as a no-op: already NeoCloud / Sovereign AI Clouds - Neocloud / high_90, fully enriched 2026-05-26. Caught by Filter Group B2 (account_tier NOT_HAS_PROPERTY) but account_tier write is frozen by hs_is_target_account = true per inviolable rule. No write. Recurring daily reappearance loop already escalated to Cooper (2026-05-28, 2026-05-29).

*Path γ - Eviction summary:*
0 Partner Target keeps · 0 Flagged for deletion.

*Stage 0 dedup hold (new this run):*
- Verizon (325110366958, verizonwireless.com): Stage 0 dedup found this record duplicates the existing master ICP record 192899501812 (Verizon, verizon.com, Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / target account / high_90). Verizon Wireless is Verizon Communications' consumer wireless division, not a separate legal entity. Deferred to R3 (Duplicate Accounts). Wrote segmentation_confidence = manual_review_required + dedup account_brief. No segment write, no last_enriched_date bump. This is consistent with the documented "Verizon / Verizon Enterprise duplicate-pair" data-quality follow-up (R3-owned).

*What needs Cooper's attention:*
- 1 new Tier 3 hold (Verizon / verizonwireless.com) - dedup, see canvas F0B0AFSB9LN section "R1 Fresh Enrichment 2026-06-01" + table below. R3 should merge 325110366958 into 192899501812 as primary.
- ResetData frozen-tier loop persists (3rd+ consecutive R1 reappearance). Resolution requires either setting account_tier manually OR clearing hs_is_target_account so the algorithm can assign tier_1 (Sovereign AI default). R1 cannot resolve this autonomously.
- 6 standing Tier 3 holds excluded this run (columbus-networks, GATCO, Synnap, Spartan Data Centers, Attobahn, Tract Capital) - all unchanged, awaiting Cooper review per their respective canvas sections.
- 0 records partial-enriched (gate-fail). 0 Flagged for deletion.

*Run health:* GREEN
- Full pool processed (2/2), 0 errors, 0 Apollo pressure, no backlog. 1 Tier 3 hold is the correct dedup outcome, not a gate failure.

*Errors:* None

---

## Path α full ICP write table
```
| Account | HubSpot ID | Segment | Sub-segment | Tier | Confidence |
|---------|-----------|---------|-------------|------|------------|
| (none)  |           |         |             |      |            |
```

## Path β reclassification table
```
| Account   | HubSpot ID    | Was → Became                          | Confidence delta |
|-----------|---------------|---------------------------------------|------------------|
| ResetData | 324591600333  | NeoCloud/Sovereign AI Clouds (no-op)  | none (high_90)   |
```

## Path γ eviction table
```
| Account | HubSpot ID | Outcome | Reason |
|---------|-----------|---------|--------|
| (none)  |           |         |        |
```

## Tier 3 hold table
```
| Account | HubSpot ID    | Path    | Ambiguity                                                                 |
|---------|---------------|---------|---------------------------------------------------------------------------|
| Verizon | 325110366958  | Stage 0 | Duplicate of master ICP record 192899501812 (Verizon/verizon.com); defer to R3 merge |
```

## Partial gate failure table
```
| Account | HubSpot ID | Path | Missing fields |
|---------|-----------|------|----------------|
| (none)  |           |      |                |
```
