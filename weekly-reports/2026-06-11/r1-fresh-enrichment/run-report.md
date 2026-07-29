# CRM Guardian - Fresh Enrichment - 2026-06-11 - 9/100 processed · 7 Tier 3 held

*Pool:* 22 raw candidates -> 9 processable after 13-record Tier 3 client-side exclude · cap 100 (steady state) · drain projection: fully drained this run (0 deferrals)

All 13 excludes verified individually against canvas F0B0AFSB9LN as genuine standing holds: 5 R0 2026-06-09 holds (t.ht.hr 326713856698, consultants.ooredoo.qa 326735614700, bb.softbank.co.jp 326694120179, wechsler.ch 326642118391, bertellifamily.org 326731977463), SoftBank Capital 326735614690 (R3 dedup, same R0 batch), ZZZ QA Retest Conflict 326675544806 (R6 QA-fixture hold), terrycorder.com 326207777466 (R6 dead-site Cooper-owned), R3 dedup holds Poly-AI 326188916440 / PolyAI 326350146247 / ConvergeOne 326171165395 / Cityside Networks 326196119272, standing MISDOMAIN columbus-networks 324597786339.

*Path counts (this run):*
- Path α full enrichment: 2 processed → 2 ICP writes, 0 re-routed to γ
- Path β re-research: 0 processed
- Path γ eviction: 0 processed
- Tier 3 holds: 7 (3 R3-dedup stubs with manual_review_required written; 4 ZZZ QA fixtures canvas-held with NO HubSpot writes - see attention section)

*Apollo:* 0 credits this run · 0/850 weekly (W24) · 850 remaining for week
*Git:* n/a (JSON updated locally; no git operations attempted per Cowork runtime)

*Path α - Full ICP enrichments (named, grouped by segment):*
- Operator ICP:
  - Mosaic Technologies (Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4) - CTC Telcom dba Mosaic Technologies, Chibardun Telephone Cooperative lineage, Cameron WI. high_90: 3 of 3 Municipal/Cooperative D5 markers passed (member-owned cooperative structure, operating FTTH across 6 NW Wisconsin counties, $12.6M Wisconsin PSC grant-funded expansion to 2,547 addresses). Owner Tim Lieto (WI = East) unchanged. signal_heat = Cold (new-account default).
  - Nextlink Internet (Fiber Operator / Regional CLEC - Fiber operator / tier_3) - record imported as email-subdomain artifact team.nxlink.com with no name; MISDOMAIN Tier 1 HIGH fix applied (name = Nextlink Internet, domain = nextlinkinternet.com). Hudson Oaks TX operator, fixed wireless + FTTH to 100k+ subs across 12 central US states, $1B+ invested, Nokia multi-gig fiber rollout. medium_7089 (fixed-wireless-heavy mix vs pure fiber keeps it below high_90). Catch-all guard: Regional CLEC assigned on POSITIVE evidence (facilities-based own-network operator, 12-state regional footprint, anchor-institution B2B service), not exclusion-by-default. Owner Ken Cunningham (TX = West) unchanged. signal_heat = Cold. NOTE: prior team.nxlink.com stub (322353590992, held 2026-05-12) no longer exists in CRM; this is a fresh same-pattern import artifact, now permanently resolved by classifying the real entity.

*Path β - Top 5 reclassifications:*
- None this run (all processable candidates were Filter Group A blank-segment new imports).

*Path γ - Eviction summary:*
- 0 Partner Target keeps · 0 Flagged for deletion

*What needs Cooper's attention:*
- 7 Tier 3 holds - see canvas F0B0AFSB9LN section "R1 Fresh Enrichment 2026-06-11":
  - 3 R3-dedup duplicate stubs (manual_review_required written, no segment/tier, no last_enriched_date bump): Anthem Business Group 326986523374 (parent of existing Anthem Broadband 314346084052), Lumos Networks lumosnet.com 326675592899 (dup of Lumos Fiber 324060022515), Long Lines Broadband longlines.biz 326675587819 (dup of Long Lines 323823198918).
  - 4 ZZZ QA test fixtures (326975435454 Retest Clean, 326967068387 Conflict Prospect, 326617190107 Happy Prospect, 326958660290 Prospect B) - created by Cooper 2026-06-10, blank-segment so they match Filter Group A daily. DELIBERATE DEVIATION from the Tier 3 Hold Gate: NO HubSpot writes made (not even segmentation_confidence) to avoid contaminating QA fixture state mid-test; canvas hold only, matching R6's handling of zzz-qa-retest-conflict.com. They will keep matching the trigger query until Cooper disposes of them - the canvas hold keeps R1 from touching them.
- Recurring subdomain-artifact import pattern continues (team.nxlink.com is the 2nd occurrence of this exact domain; us.ntt.net / g.softbank.co.jp / t.ht.hr same family). Import source keeps generating email-domain stubs.

*End-of-pipeline self-checks (D5 §9):*
1. Sub-segment nullness: PASS - both ICP writes carry populated company_sub_segment.
2. Confidence-evidence alignment: PASS - the one high_90 (Mosaic) cites 3/3 named D5 marker passes; Nextlink deliberately medium_7089.
3. Disqualifier audit: PASS (vacuous - no Other/eviction writes this run).
4. Catch-all guard: PASS - Regional CLEC (Nextlink) assigned on cited positive evidence.

*Run health:* GREEN
- Full processable pool drained, 0 errors, gate-pass rate 100% (2/2 ICP gates passed), 0 Apollo pressure, 0 deferrals.

*Errors:* None

## Per-path tables

Path α full ICP write table:
```
| Account             | HubSpot ID   | Segment        | Sub-segment                            | Tier   | Confidence   |
|---------------------|--------------|----------------|----------------------------------------|--------|--------------|
| Mosaic Technologies | 326979656425 | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | high_90      |
| Nextlink Internet   | 327020509900 | Fiber Operator | Regional CLEC - Fiber operator         | tier_3 | medium_7089  |
```

Path β reclassification table:
```
(none)
```

Path γ eviction table:
```
(none)
```

Tier 3 hold table:
```
| Account                  | HubSpot ID   | Path | Ambiguity                                                        |
|--------------------------|--------------|------|------------------------------------------------------------------|
| Anthem Business Group    | 326986523374 | α    | Parent-entity dup of Anthem Broadband 314346084052; R3 dedup     |
| Lumos Networks (legacy)  | 326675592899 | α    | lumosnet.com dup of Lumos Fiber 324060022515; R3 dedup           |
| Long Lines Broadband     | 326675587819 | α    | longlines.biz dup of Long Lines 323823198918; R3 dedup           |
| ZZZ QA Retest Clean      | 326975435454 | -    | Cooper QA fixture; canvas hold only, no writes                   |
| ZZZ QA Conflict Prospect | 326967068387 | -    | Cooper QA fixture; canvas hold only, no writes                   |
| ZZZ QA Happy Prospect    | 326617190107 | -    | Cooper QA fixture; canvas hold only, no writes                   |
| ZZZ QA Prospect B        | 326958660290 | -    | Cooper QA fixture; canvas hold only, no writes                   |
```

Partial gate failure table:
```
(none)
```
