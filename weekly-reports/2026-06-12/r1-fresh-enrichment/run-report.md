# CRM Guardian - Fresh Enrichment - 2026-06-12 - 4/100 processed · 3 Tier 3 held

*Pool:* 24 raw candidates · 20 excluded as verified standing Tier 3 / R3-dedup holds · 4 net processable · cap 100 (steady state) · drain projection: 0 days (pool fully drained this run)

*Pre-flight:* Canvas F0B0AFSB9LN read (963k chars, parsed via saved dump). All 20 excludes verified individually against hold tables before dropping: 5 ZZZ QA fixtures (326675544806, 326975435454, 326967068387, 326617190107, 326958660290 - Cooper QA test state, no writes), 5 R0 2026-06-09 subdomain/non-business holds (t.ht.hr 326713856698, consultants.ooredoo.qa 326735614700, bb.softbank.co.jp 326694120179, wechsler.ch 326642118391, bertellifamily.org 326731977463), 8 R3-dedup stubs (SoftBank Capital 326735614690, Poly-AI 326188916440, PolyAI 326350146247, ConvergeOne 326171165395, Cityside Networks 326196119272, Anthem Business Group 326986523374, Lumos Networks 326675592899, Long Lines Broadband 326675587819), terrycorder.com 326207777466 (R6 dead site), columbus-networks/finetechnologies.co 324597786339 (standing MISDOMAIN). No over-exclusion.

*Path counts (this run):*
- Path α full enrichment: 1 processed → 1 ICP write (gate-held, see below), 0 re-routed to γ
- Path β re-research: 0 processed
- Path γ eviction: 0 processed
- Tier 3 dedup holds (Stage 0 catch): 3

*Apollo:* 0 credits this run · 0/850 weekly (W24) · 850 remaining for week. Sub-cap 30, used 0. No firmographic gaps required Apollo (state/country resolved from web research); apollo_users_api_profile monthly pre-flight skipped as moot at 0 planned consumption.
*Git:* deferred (sandbox mount showed a stale truncated copy of apollo-budget.json at commit time - the known mount-sync illusion; host file verified intact via direct read, twice). JSON updated locally on host; next routine that commits cleanly will sweep this run's update. Did NOT commit from the stale mount to avoid pushing a truncated file (the suspected 06-04/06-08 corruption mechanism).

*Path α - Full ICP enrichments:*
- Operator ICP (Fiber Operator):
  - Integrity Advanced Technologies (327026419390, integrityatech.com) → Fiber Operator / Long Haul / Backbone - Fiber operator / tier_2 / low_5069 / signal_heat=Cold. Tribally owned JV (Teya Support Services ANC + Integrity Technologies Corp, formed Dec 2024), national CONUS dark + lit fiber footprint marketed for alternative long haul and access, big-carrier diversity, rural connectivity; customers: government, carriers, hyperscalers. Primary NAICS 517111 Wired Telecom. D5 F2: F2.1 + F2.3 + F2.5 supported, F2.2 route-mile scale UNVERIFIED, F2.4 absent → low_5069 with infrastructure_profile=None Identified per confidence-implication rule. **Data fixes in same write:** country Brazil → United States (import artifact; HQ is North Dakota per company site), state set North Dakota, owner re-derived Tim Ziemer → Ken Cunningham (162339176, ND=West).
  - **ICP Completeness Gate: FAIL** (segmentation_confidence low_5069 < medium_7089 floor). Partial write of all resolved fields executed; last_enriched_date NOT stamped. Record intentionally handed to R2 Filter B / D7 for verification-depth follow-up, matching the 2026-06-08 low_5069 handoff precedent.

*Path β - reclassifications:* none.

*Path γ - Eviction summary:* 0 Partner Target keeps · 0 Flagged for deletion.

*Tier 3 holds added this run (3 - all Stage 0 alternate-TLD dedup stubs, same import pattern as 2026-06-11 Lumos/Long Lines/Anthem):*

```
| Account | HubSpot ID | Path | Ambiguity |
|---|---|---|---|
| Inland Cellular (inlandcell.com) | 327072714478 | Stage 0 dedup | Alt-domain dup of Inland Cellular 320873011959 (inlandcellular.com, Fiber Operator / Regional CLEC, classified). manual_review_required + dedup brief written; no segment write, no stamp. R3 primary: 320873011959. |
| Grantsburg Telecom (grantsburgtelcom.com) | 327026292423 | Stage 0 dedup | Alt-domain dup of Grantsburg Telcom 320876610252 (grantsburgtelcom.net, Fiber Operator, classified; canonical site is .net). Same treatment. R3 primary: 320876610252. |
| Fort Mojave Telecommunications (ftmojave.net) | 327063752413 | Stage 0 dedup | Alt-domain dup of Fort Mojave Telecommunications 297782865622 (ftmojave.com, Fiber Operator, classified; canonical site is .com). Same treatment. R3 primary: 297782865622. |
```

*Partial gate failure table:*

```
| Account | HubSpot ID | Path | Missing for gate |
|---|---|---|---|
| Integrity Advanced Technologies | 327026419390 | α | segmentation_confidence ≥ medium_7089 (route-mile/POP scale of claimed CONUS fiber network unverifiable from public web; R2/D7 to verify network reality, e.g. FCC 477/BDC filings, peering records, ITC network maps) |
```

*What needs Cooper's attention:*
- 3 NEW Tier 3 R3-dedup holds (table above) - second consecutive day of alternate-TLD duplicate import stubs (yesterday: Lumos/Long Lines/Anthem; today: Inland/Grantsburg/Fort Mojave). **The upstream import source is generating alt-domain dupes of already-classified Feb-2026 records; worth checking the import list dedup key before the next batch.**
- Fresh signal found during dedup research, NOT written (out of R1 scope - belongs on a non-candidate record): **Inland Cellular (primary 320873011959) acquired First Step Internet, announced 2026-05-08** (Moscow, ID ISP; creates combined regional wireless + fiber broadband operator in Inland Northwest). Candidate for Signal Scan / outreach push-back on the primary record.
- 1 partial-gate record (IAT) intentionally un-stamped; will surface to R2 tomorrow via Filter B.
- Grantsburg stub carries grantsburgtelcom.com while canonical is .net - NOT treated as MISDOMAIN (same-brand TLD variant, not a wrong entity); R3 merge resolves it since the primary already holds .net.

*End-of-pipeline self-checks (D5 §9):*
1. Sub-segment nullness: PASS (1 ICP write has sub-segment; 3 holds carry manual_review_required + named dedup reasoning in account_brief).
2. Confidence-evidence alignment: PASS (vacuous - no high_90 writes this run).
3. Disqualifier audit: PASS (vacuous - no Other/eviction writes).
4. Catch-all guard: PASS (vacuous - no Regional CLEC / Standard - colo / Telecom Aggregator writes; IAT classified Long Haul / Backbone on positive evidence).

*Run health:* YELLOW
- Completed full drain (4/4), 0 write errors (1 batch, 4/4 OK), 0 Apollo pressure - but 3 Tier 3 holds added (mechanical R3-dedup stubs, not classification ambiguity) and 1 ICP gate failure (deliberate low_5069 handoff). No backlog (24 raw << 200 benchmark; trigger logic healthy).

*Errors:* None
