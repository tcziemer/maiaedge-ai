# CRM Guardian - Fresh Enrichment - 2026-06-15 - 4/100 processed · 2 Tier 3 held

Run start: 2026-06-15 11:21 ET (15:21 UTC). Cadence: daily M-F 10:00 AM CT. Execution: Cowork scheduled task. Runs after R0 Import Validator (9am CT) and before R2 Stale Re-Enrichment (11am CT).

*Pool:* 4 processable candidates (23 raw from the 5-filterGroup trigger query, minus 19 standing Tier 3 / R3-dedup excludes) · cap 100 (steady state, pool <= 200) · drain projection: 0 days, pool fully drained this run.

*Tier 3 exclusion (19 of 23 raw):* each exclude verified against canvas F0B0AFSB9LN via targeted grep (not trusted from history alone): 4 R1 dedup stubs (Grantsburg Telecom 327026292423, Anthem Business Group 326986523374, Lumos Networks 326675592899, Long Lines Broadband 326675587819), 5 ZZZ QA synthetic fixtures (326675544806 / 326975435454 / 326967068387 / 326617190107 / 326958660290), 3 R0 2026-06-09 subdomain/non-business holds (t.ht.hr 326713856698, wechsler.ch 326642118391, bertellifamily.org 326731977463), SoftBank Capital 326735614690 (R3 dedup), terrycorder.com 326207777466 (R6 dead-site), Poly-AI 326188916440 + PolyAI 326350146247 + ConvergeOne 326171165395 + Cityside Networks 326196119272 (R3 dedup), columbus-networks 324597786339 (MISDOMAIN). NOTE: wvsupport.net and Pearce Renewables appear on the canvas only in R6 territory-hygiene prose (unknown-HQ carry / "CA/US -> Cunningham/West"), NOT in any R0/R1/R2/R4 Tier-3-hold table, so neither is in the R1 exclude set - both were processed.

*Path counts (this run):*
- Path alpha full enrichment: 1 processed -> 1 ICP write, 0 re-routed to gamma
- Path beta re-research: 0 processed
- Path gamma eviction: 1 processed -> 0 Partner keeps, 1 Flagged for deletion, 0 MISDOMAIN re-routes
- Stage 0 dedup -> Tier 3 hold: 1 (Midtel Cable Tv, caught pre-classification)
- Ambiguity -> Tier 3 hold: 1 (wvsupport.net)

*Apollo:* 0 credits this run · 0/850 weekly (W25, auto-rolled from W24 at run start) · 850 remaining. Sub-cap 30, used 0 of 30. No apollo_organizations_enrich calls - all classifications from web research + HubSpot dedup reads; firmographics clear from import data + public sources.
*Git:* commit deferred (concurrent routine holds .git/index.lock); budget JSON + this report updated locally. Per Edit 7 this is a logged non-failure - the next routine that commits sweeps this run into history; the on-disk report + canvas Run-log row are the audit trail of record.

*Path alpha - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Fiber Operator):
  - Jefferson Telecom (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90 / heat Cold) - independent Iowa ILEC (Jefferson Telephone Company, est. 1938) running 100 percent FTTH with symmetrical gigabit across roughly 96 percent of Greene County, fiber build since 2001; also IPTV, landline, long-time wireless agent. Owner Tim Lieto (IA = East), unchanged. Positive Regional-CLEC evidence: facilities-based local exchange carrier operating its own fiber access network with retail + business subscribers (not exclusion-by-default). Sole contact Jamie Daubendiek (GM) already carries customer_segment = Fiber Operator (cascade in sync).
- Enterprise ICP: none this run.
- Enterprise scale-gate failures routed to gamma: none.

*Path beta - Top 5 reclassifications:* none (0 Path beta candidates this run).

*Path gamma - Eviction summary:*
- 0 Partner Target keeps · 1 Flagged for deletion: Pearce Renewables (No ICP fit - renewable-energy O&M services).

*What needs Cooper's attention:*
- 2 Tier 3 holds added this run (canvas F0B0AFSB9LN, section "R1 Fresh Enrichment 2026-06-15"):
  - Midtel Cable Tv (327010669253, midtel.net) - R3-dedup stub of canonical MIDTEL (300468012733, midtel.com, Fiber Operator / Regional Cable Operator, tier_3, enriched 2026-05-19). Mechanical; resolves when R3 merges the pair. This is the 3rd-4th consecutive week of alternate-TLD import stubs (grantsburgtelcom, ftmojave, inlandcell, lumosnet, longlines.biz pattern) - the import-source dedup key issue remains open for Cooper.
  - wvsupport.net (327229537012) - unidentifiable: no company name, blank HQ state/country, owner Cooper (RevOps, does not own prospects), no web-search footprint, Apollo not found on a prior R6 pass, and web_fetch was blocked (URL not in provenance set) so dead-domain status could not be verified. Likely an intentional test record or a junk import. Recommend Cooper delete it if test/junk, or supply identity if it is a real prospect.
- 1 hard-flagged company in HubSpot Companies filter customer_segment = "Flagged for deletion": Pearce Renewables (327108158163).
- 0 partial-gate failures.

*Run health:* YELLOW
- 4/4 processable drained, 0 errors, both definitive gates passed (Jefferson ICP gate, Pearce eviction gate), no Apollo cap pressure, full drain with 0 deferrals.
- YELLOW (not GREEN) solely because of the 2 Tier 3 holds (1 mechanical dedup, 1 ambiguous Cooper-owned record). Consistent with the 2026-06-12 precedent (mechanical dedup holds -> YELLOW).

*Errors:* None. HubSpot MCP reachable; both write batches succeeded (1/1 and 3/3). Slack canvas read required a bounded-grep workaround (ledger exceeds the read-token limit at ~1.0M chars); the exclude set and the 2 R6-prose references were verified via targeted grep. web_fetch on wvsupport.net was blocked (URL not in provenance set) and was not routed around, per content-restriction policy.

## End-of-pipeline self-checks (D5 §9)

1. Sub-segment nullness check: Jefferson Telecom (only ICP customer_segment write) has company_sub_segment = "Regional CLEC - Fiber operator" populated. PASS.
2. Confidence-evidence alignment: Jefferson high_90 is backed by positive evidence (facilities-based independent ILEC, owns/operates 100% FTTH access network, symmetrical gigabit, retail + business subscribers). PASS.
3. Disqualifier audit: 0 "Other" eviction writes this run; Pearce Renewables Flagged-for-deletion cites concrete out-of-scope-industry evidence (renewable-energy O&M services, not carrier infrastructure, no reference value). PASS.
4. Catch-all guard: Jefferson's Regional CLEC assignment rests on POSITIVE evidence (operates its own fiber LEC network), not exclusion-by-default. PASS.

## Per-path tables

### Path alpha - Full ICP writes

```
| Account            | HubSpot ID    | Segment        | Sub-segment                    | Tier   | Confidence |
|--------------------|---------------|----------------|--------------------------------|--------|------------|
| Jefferson Telecom  | 327225613026  | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90    |
```

### Path beta - Reclassifications

```
(none this run - 0 Path beta candidates)
```

### Path gamma - Evictions

```
| Account            | HubSpot ID    | Outcome              | Reason                                                        |
|--------------------|---------------|----------------------|---------------------------------------------------------------|
| Pearce Renewables  | 327108158163  | Flagged for deletion | No ICP fit - renewable-energy O&M services, not carrier infra  |
```

### Tier 3 holds

```
| Account          | HubSpot ID    | Path           | Ambiguity                                                                       |
|------------------|---------------|----------------|---------------------------------------------------------------------------------|
| Midtel Cable Tv  | 327010669253  | Stage 0 dedup  | Alternate-TLD stub of MIDTEL 300468012733 (midtel.com); hand to R3 for merge     |
| wvsupport.net    | 327229537012  | gamma AMBIGUOUS| Unidentifiable; owner Cooper; blank HQ; no footprint; Apollo not found; test/junk?|
```

### Partial gate failures

```
(none this run)
```
