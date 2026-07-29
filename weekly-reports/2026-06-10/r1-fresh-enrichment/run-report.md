CRM Guardian - Fresh Enrichment - 2026-06-10 - 2/100 processed · 0 Tier 3 held

*Pool:* 2 processable candidates (14 raw -> 12 Tier 3 client-side excluded) · cap 100 · drain projection: 0 days (full drain, pool clear)

*Path counts (this run):*
- Path α full enrichment: 1 processed → 1 ICP write, 0 re-routed to γ
- Path β re-research: 0 processed → 0 reclassified, 0 Tier 3 holds
- Path γ eviction: 1 processed → 0 Partner Target keeps, 1 Flagged for deletion, 0 MISDOMAIN re-routes to α

*Apollo:* 0 credits this run · 0/850 weekly (W24) · 850 remaining for week
*Git:* not attempted (Cowork scheduled-task runtime; JSON updated locally)

*Path α - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Colocation / Fiber / NeoCloud / Network Op / MSP-Aggregator):
  - Cyfuture (Data Center Colo Provider / Standard - colo / tier_3 / high_90) - India-based operator, four MeitY-empaneled Tier III colocation DCs (Noida x2, Jaipur, Raipur), fifth under construction in Chennai (500 racks phase 1). Owner Tim Ziemer (International, India), unchanged. signal_heat=Cold (new account default).
- Enterprise ICP (Multi-DC): none this run.
- Enterprise scale-gate failures routed to Path γ: none this run.

*Path β - Top 5 reclassifications:* none this run.

*Path γ - Eviction summary:*
- 0 Partner Target keeps · 1 Flagged for deletion (No ICP fit: CMDB360 / cmdb360.com - ITSM/CMDB configuration-management software product from Base2Summit LLC, MSP-deployed cloud-asset visibility tool; not carrier infrastructure, not a partner/competitor reference).

*What needs Cooper's attention:*
- 0 Tier 3 holds this run.
- 1 hard-flagged company in HubSpot Companies filter customer_segment = "Flagged for deletion" (CMDB360, 326927535860).
- 0 partial gate failures.
- Note: 12 of 14 raw candidates were client-side excluded as genuine standing holds, all verified individually against canvas F0B0AFSB9LN:
  - R3 dedup pairs/stubs: Poly-AI (326188916440) / PolyAI (326350146247); ConvergeOne (326171165395) vs C1/onec1.com; Cityside Networks (326196119272) vs Cityside Fiber; SoftBank Capital (326735614690) near-dup of SoftBank records.
  - R0 subdomain-artifact / non-business holds (2026-06-09): t.ht.hr (326713856698), bb.softbank.co.jp (326694120179), consultants.ooredoo.qa (326735614700), wechsler.ch (326642118391), bertellifamily.org (326731977463).
  - R6 dead-site hold (Cooper-owned): terrycorder.com (326207777466) - ECONNREFUSED, under R6 review.
  - Standing MISDOMAIN hold: columbus-networks / finetechnologies.co (324597786339).

*Run health:* GREEN
- Full processable pool drained (2/2), 0 errors, gate-pass rate 100%, no Apollo cap pressure.

*Errors:* None

```
Path α full ICP write table
| Account  | HubSpot ID    | Segment                     | Sub-segment    | Tier   | Confidence |
|----------|---------------|-----------------------------|----------------|--------|------------|
| Cyfuture | 326866083559  | Data Center Colo Provider   | Standard - colo| tier_3 | high_90    |
```

```
Path β reclassification table
| Account | HubSpot ID | Was → Became | Confidence delta |
|---------|------------|--------------|------------------|
| (none)  | -          | -            | -                |
```

```
Path γ eviction table
| Account  | HubSpot ID   | Outcome              | Reason                                                                 |
|----------|--------------|----------------------|------------------------------------------------------------------------|
| CMDB360  | 326927535860 | Flagged for deletion | No ICP fit - ITSM/CMDB software product (Base2Summit LLC), MSP tooling  |
```

```
Tier 3 hold table
| Account | HubSpot ID | Path | Ambiguity |
|---------|------------|------|-----------|
| (none)  | -          | -    | -         |
```

```
Partial gate failure table
| Account | HubSpot ID | Path | Missing fields |
|---------|------------|------|----------------|
| (none)  | -          | -    | -              |
```
