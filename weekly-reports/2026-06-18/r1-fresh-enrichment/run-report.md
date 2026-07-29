CRM Guardian - Fresh Enrichment - 2026-06-18 - 10/100 processed · 1 Tier 3 held

*Pool:* 22 candidates (raw) · 12 standing Tier 3 / dedup / hygiene excludes (client-side) · 10 processable · cap 100 · drain projection: pool fully drained this run (10/10), steady-state inflow = R0 daily imports.

*Pre-flight:*
- Apollo budget read (apollo-budget.json, W25): consumed 2/850, fresh-enrichment 0. R1 sub-cap 30/run, 30 available. Apollo NOT used this run (see note below).
- Tier 3 exclusion: read canvas F0B0AFSB9LN. Built TIER_3_EXCLUDE_SET = 12 IDs. Verified each candidate ID against the saved canvas: all 10 of today's R0 records have ZERO canvas occurrences (clean); all 12 older candidates appear in standing hold contexts (R0 carryovers, R1 06-17 + 05-27 holds, R3 dedup pairs, R6 hold). Excluded client-side.
- Exclude set (12): 328126464704 (Nextlink, R1 06-17->R3), 327944646384 (Schwarz Digits, R1 06-17->R3), 324597786339 (columbus-networks, R1 05-27), 326713856698 (t.ht.hr, R0->R3), 326642118391 (wechsler.ch, R0), 326731977463 (bertellifamily.org, R0), 326735614690 (SoftBank Capital, R3 dedup), 326188916440 (Poly-AI, R3 dedup), 326350146247 (PolyAI, R3 dedup), 326171165395 (ConvergeOne, R3 dedup), 326196119272 (Cityside Networks, R3 dedup), 326207777466 (terrycorder.com, R6). Matches yesterday's 10 standing-hold excludes + the 2 R1 added 06-17.

*Path counts (this run):*
- Path alpha full enrichment: 5 entered -> 4 ICP writes, 1 resolved to Tier 3 dedup hold at Stage 0 (Bell MTS), 0 re-routed to gamma.
- Path beta re-research: 0 (no Filter C / Filter D candidates in the processable pool; all 10 were Filter Group A blank-segment R0 imports).
- Path gamma eviction: 5 entered -> 4 Other (ecosystem/partner keeps), 1 Flagged for deletion, 0 MISDOMAIN re-routes.

*Apollo:* 0 credits this run. Weekly W25: 2/850, 848 remaining. Sub-cap 30, used 0 of 30.
- Note: All 10 records are well-documented European/Canadian infrastructure entities classified confidently from web_search; state + country were already populated by R0 import (only firstcolo needed a country/state fill, sourced from research, not Apollo). No firmographic gap blocked any completeness gate, so no Apollo enrich was required. Consistent with recent R1 pattern (0 Apollo on EU-import batches). The Apollo enrich tool also carries a mandatory per-call user-confirmation that cannot be satisfied in an unattended scheduled run; web research was sufficient, so this was a non-issue.

*Git:* deferred (best-effort); apollo-budget.json + run report updated locally on disk. Disk report + canvas Run-log row are the audit trail of record.

*Path alpha - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Colocation / Fiber / NeoCloud / Network Op / MSP-Aggregator):
  - TelemaxX (328489878258) - Data Center Colo Provider / Standard - colo / tier_3 / high_90. 5 high-security colo DCs (IPC1-IPC5), Karlsruhe; multi-tenant retail colocation. Owner Hendrich (Germany/Europe).
  - firstcolo GmbH (328466671345) - Data Center Colo Provider / Standard - colo / tier_3 / high_90. Tier III Frankfurt colo, DE-CIX connected, ~1.8 MW, Rosbach expansion planned. Country/state filled (Germany / Hessen). Owner Hendrich.
  - 1&1 Versatel GmbH (328573411062) - Fiber Operator / Tier 2 National Wholesale - Fiber operator / tier_2 / high_90. ~67,000 km national B2B fibre backbone, 350+ cities, wholesale/interconnect, United Internet. Owner Hendrich.
  - Anexia (328553564875) - MSP/Aggregator / Cloud + Telecom Hybrid MSP - MSP / tier_2 / medium_7089. Austrian cloud + managed hosting + own IP-transit backbone (Backbone Europe ~2 Tbit/s, 60+ interconnects). medium reflects cloud-vs-network hybrid ambiguity. Owner Hendrich.
- Enterprise ICP (Multi-DC, 4 sub-segments): none this run.
- Enterprise scale-gate failures routed to gamma: none this run.

*Path beta - reclassifications:* none (0 Path beta candidates).

*Path gamma - Eviction summary:*
- 4 Other keeps (ecosystem/partner references, all tier_5 / high_90 / infrastructure_profile None Identified):
  - AMS-IX (328506112734) - neutral non-profit IXP (~800 networks), not a carrier-infra buyer; ecosystem/peering reference. Owner Hendrich.
  - Odine (328461277894) - telecom software / network-orchestration vendor (MANO, OSS/BSS, wholesale voice), D1 vendor disqualifier; competitive/ecosystem reference. Owner Hendrich (record country UK; founding roots Istanbul TR - territory note below).
  - CGI (328506122975) - global IT consulting / systems integrator (~94k staff), D1 IT-SI disqualifier; SI/channel ecosystem reference. Owner Ziemer (Canada/International).
  - Savecall (328537652929) - telecom/IT advisory + sourcing + reseller (Munich), D1 consultancy disqualifier; telecom-channel ecosystem reference. Owner Hendrich.
- 1 Flagged for deletion:
  - dtms GmbH (328573417154) - "No ICP fit": CCaaS / contact-center software + service-number provider (Verbindungsnetzbetreiber regulatory status only); no owned carrier infrastructure, no partner/competitor reference value. flagged_for_deletion_reason set in same write. Precedent: FreeConferenceCall (2026-06-03).

*What needs Cooper's attention:*
- 1 NEW Tier 3 hold -> R3: Bell MTS (328482682595). Manitoba regional division of Bell Canada (BCE); canonical "Bell" Tier 1 Carrier record already exists (322837059318, bell.ca). D2 wholesale-arm/parent + dedup ambiguity. Held with segmentation_confidence=manual_review_required, NO segment/sub-segment/tier write, last_enriched_date NOT bumped. R3 to decide merge vs keep-distinct before any parallel Tier 1 classification. See canvas section "R1 Fresh Enrichment 2026-06-18 - Tier 3 holds added".
- 1 hard-flagged company in HubSpot Companies filter customer_segment = "Flagged for deletion": dtms GmbH (328573417154).
- Minor data note (no action required): Odine (328461277894) record country = United Kingdom (owner Hendrich/Europe), but web research indicates founding HQ in Istanbul, Turkey (Turkey routes to International/Ziemer, not Europe). Left owner as record-derived since Odine maintains a UK entity and the record is non-ICP "Other"; flagging only for awareness.
- 0 partial-gate failures.

*Manual-review note:* 1 of 10 processed = manual_review_required (Bell MTS). This is a legitimate dedup hold (existing canonical Bell Tier 1 record), NOT an over-applied classification escape hatch or an over-strict-D5 miss. The <5% target governs classification-ambiguity manual_review; with a 10-record batch a single justified dedup hold mechanically reads as 10%. Spirit of the rule honored.

*End-of-pipeline self-checks (4):*
1. Sub-segment nullness: 4 ICP writes (TelemaxX, firstcolo, 1&1 Versatel, Anexia) all have company_sub_segment populated. PASS.
2. Confidence-evidence alignment: every high_90 write cites a named anchor / quantitative marker / D1 rule in account_brief (5 named DCs; Tier III + DE-CIX; 67,000 km national backbone; neutral IXP; D1 vendor/SI/consultancy; No-ICP CCaaS). Anexia correctly medium_7089. PASS.
3. Disqualifier audit: 4 Other evictions each cite the specific disqualifier rationale in account_brief. PASS.
4. Catch-all guard: 2 Standard - colo writes cite POSITIVE colo evidence (operational multi-tenant DCs, certifications, DE-CIX interconnect), not exclusion-by-default. No Regional CLEC / Telecom Aggregator writes. PASS.

*Run health:* GREEN
- Full processable batch drained (10/10), 0 HubSpot write errors (2 batches: 4/4 + 6/6), gate-pass rate 9/9 definitive writes passed (100%), 1 explicit Tier 3 hold, no Apollo cap pressure, no backlog elevation.

*Errors:* None.

---

```
Path alpha - Full ICP write table

| Account            | HubSpot ID    | Segment                    | Sub-segment                              | Tier   | Confidence   |
| ------------------ | ------------- | -------------------------- | ---------------------------------------- | ------ | ------------ |
| TelemaxX           | 328489878258  | Data Center Colo Provider  | Standard - colo                          | tier_3 | high_90      |
| firstcolo GmbH     | 328466671345  | Data Center Colo Provider  | Standard - colo                          | tier_3 | high_90      |
| 1&1 Versatel GmbH  | 328573411062  | Fiber Operator             | Tier 2 National Wholesale - Fiber operator | tier_2 | high_90    |
| Anexia             | 328553564875  | MSP/Aggregator             | Cloud + Telecom Hybrid MSP - MSP         | tier_2 | medium_7089  |
```

```
Path gamma - Eviction table

| Account        | HubSpot ID    | Outcome              | Reason                                                                                  |
| -------------- | ------------- | -------------------- | --------------------------------------------------------------------------------------- |
| AMS-IX         | 328506112734  | Other (tier_5)       | Neutral non-profit IXP / peering fabric; not a carrier-infra buyer; ecosystem reference |
| Odine          | 328461277894  | Other (tier_5)       | Telecom software / orchestration vendor (D1); competitive/ecosystem reference           |
| CGI            | 328506122975  | Other (tier_5)       | Global IT consulting / systems integrator (D1); SI/channel reference                    |
| Savecall       | 328537652929  | Other (tier_5)       | Telecom/IT advisory + sourcing + reseller (D1); telecom-channel reference               |
| dtms GmbH      | 328573417154  | Flagged for deletion | No ICP fit: CCaaS / contact-center software + service numbers; no reference value       |
```

```
Tier 3 hold table

| Account   | HubSpot ID    | Path    | Ambiguity                                                                                                       |
| --------- | ------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| Bell MTS  | 328482682595  | alpha   | Manitoba division of Bell Canada; canonical "Bell" Tier 1 record exists (322837059318, bell.ca). D2 + dedup -> R3 |
```

```
Partial gate failure table

| Account | HubSpot ID | Path | Missing fields |
| ------- | ---------- | ---- | -------------- |
| (none)  |            |      |                |
```
