CRM Guardian - Fresh Enrichment - 2026-06-04 - 5/100 processed · 2 Tier 3 held

*Pool:* 15 candidates raw · 10 standing Tier 3 holds excluded client-side · 5 processed · cap 100 · drain projection: 0 days (pool drained, steady state)

*Path counts (this run):*
- Path α full enrichment: 2 processed → 1 ICP write (LitFiber), 1 re-routed to γ (Core Technologies)
- Path β re-research: 3 processed → 0 reclassified, 1 frozen-tier no-op (ResetData), 2 Tier 3 dedup holds (INDATEL Services, teampoka)
- Path γ eviction: 1 processed → 0 Partner Target keeps, 1 Flagged for deletion, 0 MISDOMAIN re-routes

*Apollo:* 0 credits this run · 0/850 weekly (W23) · 850 remaining for week
*Git:* see budget-json note

*Path α - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Fiber):
  - LitFiber (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90). MISDOMAIN corrected litfiber.org -> litfiber.us. Western Kentucky FTTH ISP (Madisonville / Hopkins County), symmetrical up to 8 Gbps residential + business. Distinct from existing Lit Fiber (OmniFiber) Ohio record - not a dup. Owner Tim Lieto (KY = East), unchanged. signal_heat = Cold.
- Enterprise ICP: none this run.
- Enterprise scale-gate failures routed to Path γ: none this run.

*Path β - Top 5 reclassifications:* none (0 reclassifications this run).
- Frozen-tier no-op: ResetData (324591600333) - NeoCloud / Sovereign AI Clouds / high_90, last_enriched 2026-05-26. account_tier blank caught by Filter Group B2, but hs_is_target_account=true freezes the tier write per inviolable rule. Recurring daily B2 reappearance loop - already escalated to Cooper (2026-05-28/29, 06-01/02/03). No write.

*Path γ - Eviction summary:*
- 0 Partner Target keeps · 1 Flagged for deletion (HARD_DELETE / No ICP fit: Core Technologies)

*What needs Cooper's attention:*
- 2 Tier 3 dedup holds added this run (deferred to R3): INDATEL Services (326184182509, dup of indatel.com 322761764552) and teampoka.com (325800222448, likely dup of Poka Lambro Telecom poka.com 320876610271). See canvas F0B0AFSB9LN section "R1 Fresh Enrichment 2026-06-04".
- 1 hard-flagged company in HubSpot Companies filter customer_segment = "Flagged for deletion": Core Technologies (325787887340).
- ResetData B2 reappearance loop persists (frozen-tier no-op recurring daily). Resolution: set account_tier manually OR clear hs_is_target_account so the algo assigns tier_1 (Sovereign AI default).
- 0 partial gate failures.

*Run health:* GREEN
- Full pool drained (5/5 actionable records processed; 10 standing holds correctly excluded), 0 errors, gate-pass rate 100%, no Apollo cap pressure. All 4 end-of-pipeline self-checks PASS.

*Errors:* None

---

Path α full ICP write table:
```
| Account   | HubSpot ID    | Segment        | Sub-segment                    | Tier   | Confidence |
|-----------|---------------|----------------|--------------------------------|--------|------------|
| LitFiber  | 325917807315  | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90    |
```

Path β reclassification table:
```
| Account   | HubSpot ID    | Was -> Became         | Confidence delta |
|-----------|---------------|-----------------------|------------------|
| ResetData | 324591600333  | no-op (tier frozen)   | none             |
```

Path γ eviction table:
```
| Account          | HubSpot ID    | Outcome              | Reason                                                              |
|------------------|---------------|----------------------|---------------------------------------------------------------------|
| Core Technologies| 325787887340  | Flagged for deletion | No ICP fit - federal IT/AV/cabling installation integrator, not operator |
```

Tier 3 hold table:
```
| Account          | HubSpot ID    | Path | Ambiguity                                                        |
|------------------|---------------|------|------------------------------------------------------------------|
| INDATEL Services | 326184182509  | β    | Duplicate of indatel.com (322761764552); defer to R3 dedup       |
| teampoka.com     | 325800222448  | β    | Likely dup of Poka Lambro Telecom poka.com (320876610271); R3     |
```

Partial gate failure table:
```
| Account | HubSpot ID | Path | Missing fields |
|---------|------------|------|----------------|
| (none)  |            |      |                |
```

Standing Tier 3 holds excluded client-side this run (10): us.ntt.net (325335796410), Digital Fortress (325323215608), g.softbank.co.jp (325335795443), Verizon/verizonwireless.com (325110366958), columbus-networks/finetechnologies.co (324597786339), gatco.net (324524875475), Synnap (324498712298), Spartan Data Centers (324535363289), Attobahn (324610914007), Tract Capital (321983866611).
