CRM Guardian - Fresh Enrichment - 2026-06-16 - 4/100 processed · 0 Tier 3 held

*Pool:* 4 processable candidates (25 raw, 21 standing Tier 3 / R3-dedup / QA-fixture holds excluded client-side) · cap 100 (steady state, pool <=200) · drain projection: pool fully drained, 0 remaining

*Path counts (this run):*
- Path alpha full enrichment: 1 processed (Wasabi Technologies, pre-scored alpha on "cloud" keyword) -> 0 ICP writes, 1 re-routed to gamma (non-ICP after research)
- Path beta re-research: 0 processed (all 4 processable were Filter Group A blank-segment new imports)
- Path gamma eviction: 4 processed -> 3 Other keeps, 1 Flagged for deletion, 0 MISDOMAIN re-routes

*Apollo:* 0 credits this run · 2/850 weekly (W25) · 848 remaining for week. No apollo_organizations_enrich calls - all 4 are non-ICP with no firmographic gap; classifications from web_search + public knowledge.
*Git:* commit deferred (concurrent routine holds .git/index.lock; index reported corrupt - bad signature). apollo-budget.json + run-report.md updated locally and verified host-side via Read tool. The bash-mount json.load parse error was the known sandbox stale-mount illusion (mount showed pre-edit length), not real corruption. Disk report + canvas Run-log row are the audit trail of record; next routine to commit sweeps this run into git history.

*Path alpha - Full ICP enrichments (named, grouped by segment):*
- None this run. (Wasabi Technologies pre-scored alpha on the "cloud" keyword but research confirmed hot cloud object storage = a connectivity destination, not a carrier/colo/GPU/Enterprise ICP; re-routed to gamma as Other.)

*Path beta - Top 5 reclassifications:*
- None this run.

*Path gamma - Eviction summary:*
- 3 Other (PARTNER_KEEP / vetted non-ICP ecosystem references): CrowdStrike, Wasabi Technologies, Continental Resources (ConRes)
- 1 Flagged for deletion: Innosight (No ICP fit)

*What needs Cooper's attention:*
- 1 Flagged for deletion (Innosight, 327880423099) in HubSpot Companies filter customer_segment = "Flagged for deletion" - pure management/innovation consultancy (Huron Consulting Group), no carrier-infrastructure relevance and no partner or competitive reference value.
- 0 Tier 3 holds added this run (full clean drain).
- Import-source observation (non-blocking): today's batch was 4 non-ICP tech companies (cybersecurity, strategy consulting, cloud object storage, IT VAR), all created 2026-06-15/16. None are carrier-infrastructure ICPs. If this list came from a recurring source, an ICP pre-filter upstream would cut R1 noise. Flagging the pattern, not acting on it.
- 21 standing holds remain excluded from the daily pool (unchanged, NOT new): 5 R3-dedup stubs (Grantsburg Telecom, Anthem Business Group, Lumos Networks, Long Lines Broadband, Midtel Cable Tv), 5 ZZZ QA fixtures, 3 R0 subdomain/non-business (t.ht.hr, wechsler.ch, bertellifamily.org), SoftBank Capital, terrycorder.com (R6), Poly-AI / PolyAI / ConvergeOne / Cityside Networks (R3 dedup), columbus-networks (MISDOMAIN), wvsupport.net (R1 2026-06-15 AMBIGUOUS, Cooper to confirm test-vs-prospect). These are R0/R3/R6/Cooper scope, not R1-resolvable.

*Run health:* GREEN
- Full processable pool drained (4/4), 0 errors, gate-pass rate 100% (4/4 definitive writes), 0 Apollo pressure, 0 Tier 3 holds.

*Errors:* None.

*End-of-pipeline self-checks (all PASS):*
1. Sub-segment nullness: 0 ICP writes this run -> vacuously PASS.
2. Confidence-evidence alignment: 4 high_90 writes, all non-ICP; each cites a specific D1 disqualifier basis (not a D5 over-claim) -> PASS.
3. Disqualifier audit: 3 Other writes each cite a specific D1 rule (D1.5 security platform / D1.1-analogous destination / D1.2 system integrator); Innosight Flagged cites the "No ICP fit" reason code -> PASS.
4. Catch-all guard: 0 records classified as Regional CLEC / Standard - colo / Telecom Aggregator -> vacuously PASS.

---

### Path alpha - Full ICP write table
```
(none this run)
```

### Path beta - Reclassification table
```
(none this run)
```

### Path gamma - Eviction table
```
Account                              | HubSpot ID    | Outcome                        | Reason
-------------------------------------|---------------|--------------------------------|------------------------------------------------------------
CrowdStrike                          | 327800966897  | Other (tier_5, high_90)        | D1.5 pure-play security platform (Falcon endpoint/cloud/identity); explicitly named D1 disqualifier
Wasabi Technologies                  | 327644780240  | Other (tier_5, high_90)        | Hot cloud object storage = connectivity destination, not carrier/colo/GPU/Enterprise; D1.1-analogous destination rationale
Continental Resources (ConRes)       | 327581670131  | Other (tier_5, high_90)        | IT value-added reseller / systems integrator (hardware + DC solutions + test equipment); D1.2, no carrier network ops
Innosight                            | 327880423099  | Flagged for deletion (high_90) | No ICP fit - strategy/innovation consultancy (Huron Consulting Group), no infrastructure, no partner/competitive reference value
```

### Tier 3 hold table
```
(none added this run)
```

### Partial gate failure table
```
(none this run)
```

---

*Field-level writes (audit):*
- CrowdStrike 327800966897: customer_segment=Other, account_tier=tier_5, segmentation_confidence=high_90, infrastructure_profile="None Identified", account_brief written, last_enriched_date=2026-06-16. Owner unchanged (Ken Cunningham 162339176, CA=West - both CA and current Austin TX HQ map to Ken; state left as CA, immaterial for non-ICP Other). No signal_heat (Path gamma does not touch heat).
- Wasabi Technologies 327644780240: customer_segment=Other, account_tier=tier_5, segmentation_confidence=high_90, infrastructure_profile="None Identified", account_brief written, last_enriched_date=2026-06-16. Owner unchanged (Tim Lieto 161889085, MA=East). No signal_heat.
- Continental Resources (ConRes) 327581670131: customer_segment=Other, account_tier=tier_5, segmentation_confidence=high_90, infrastructure_profile="None Identified", account_brief written, last_enriched_date=2026-06-16. Owner unchanged (Tim Lieto 161889085, MA=East). No signal_heat.
- Innosight 327880423099: customer_segment="Flagged for deletion", flagged_for_deletion_reason="No ICP fit: ...", segmentation_confidence=high_90, account_brief written, last_enriched_date=2026-06-16. No account_tier (compute_tier Step A0 no-ops non-ICP segments). Owner unchanged (Tim Lieto 161889085, MA=East). No signal_heat.

1 HubSpot batch (4/4 OK, 0 failed). Sub-cap 30, used 0 of 30. Weekly W25: 2/850, 848 remaining.
