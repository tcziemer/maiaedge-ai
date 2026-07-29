CRM Guardian - Import Validator - 2026-06-18 - 0 domain-corrected, 0 renamed, 0 flagged, 0 new Tier 3 held

Run summary: 10 records scanned, 10 MATCH / 0 MISDOMAIN / 0 RENAMABLE / 0 HARD_FLAG / 0 DEAD_DOMAIN / 0 AMBIGUOUS, 10 HubSpot writes (signal_heat=Cold defaults), 0 errors.

Trigger window: createdate >= 2026-06-17 10:02 ET (24h), last_enriched_date empty, customer_segment != "Flagged for deletion", excl. MaiaEdge own record (124293230301). Sorted createdate ASC. Single page (10 records, well under the 100 cap).

Customer protection: batch closed-won deal association check across all 10 companies returned 0 - none hard-stopped under Invariant C. MaiaEdge own record not present.

What needs Cooper's attention:
- 0 NEW Tier 3 holds this run.
- 4 standing R0 Tier 3 carryovers re-affirmed (all present in HubSpot, no Cooper action since the prior run) - await Cooper / R3. See the Tier 3 table below.
- 0 medium-confidence corrections to verify.
- 0 hard-flagged companies.

Run health: GREEN
- 0 errors, 10/10 writes succeeded, 0 NEW Tier 3 this run. The only Tier-3 items present are 4 standing carryovers awaiting Cooper/R3 (0 new, 0 drained this run), consistent with the prior two runs logged as success.

Errors: None affecting outcome. The run-end slack_update_canvas append returned an oversized-response error (the echoed canvas exceeds the response token limit); the write itself was verified APPLIED via the saved response file (2 dated 2026-06-18 R0 headers + the unique MISDOMAIN phrase present exactly once, no duplication). No retry issued - retrying would double-append. This is the known benign canvas phantom-error pattern.

---

This was a clean, deliberate import batch - mostly Markus Hendrich's Europe territory (TelemaxX, AMS-IX, Odine, Anexia, Savecall, firstcolo, 1&1 Versatel, dtms) plus Tim Ziemer's international/Canada (Bell MTS, CGI). Every record's HubSpot name matches the real entity at its domain at HIGH confidence (2+ independent sources each). No name-vs-domain defects of any kind.

```
MATCH (10) - signal_heat=Cold default written; segment + enrichment left for R1 (10:00 AM CT)

| ID            | Name                | Domain        | Entity at domain (web_search, HIGH confidence)                                                                                  | Owner          |
| ------------- | ------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| 328482682595  | Bell MTS            | bellmts.ca    | Bell MTS, division of Bell Canada (BCE); Manitoba telecom / network operator. Wikipedia + BCE press + official site.             | Ziemer (Intl)  |
| 328489878258  | TelemaxX            | telemaxx.de   | TelemaxX Telekommunikation GmbH; Karlsruhe colocation/DC operator since 1999 (5 DCs, EN-50600). Official + DataCenterMap.         | Hendrich (EU)  |
| 328506112734  | AMS-IX              | ams-ix.net    | Amsterdam Internet Exchange; neutral non-profit IXP (~12 Tb/s peak). Wikipedia + PeeringDB + official.                           | Hendrich (EU)  |
| 328461277894  | Odine               | odine.com     | Odine (BIST:ODINE); global telecom software / service-orchestration / SI, 25+ yrs. Official + LinkedIn.                          | Hendrich (EU)  |
| 328553564875  | Anexia              | anexia.com    | Anexia (Holding GmbH); Austrian cloud / managed-hosting / colocation, Klagenfurt. Official + DataCenterMap.                      | Hendrich (EU)  |
| 328506122975  | CGI                 | cgi.com       | CGI Inc. (TSX/NYSE:GIB); Montreal IT consulting / systems-integration giant, 90k+ staff. Wikipedia + SEC.                        | Ziemer (Intl)  |
| 328537652929  | Savecall            | savecall.de   | SAVECALL telecommunications consulting GmbH; Grunwald/Munich telecom+IT advisory/sourcing. Official + NorthData.                 | Hendrich (EU)  |
| 328466671345  | firstcolo GmbH      | firstcolo.net | firstcolo GmbH; Frankfurt Tier III colocation/DC, DE-CIX connected, since 2007. Official + DataCenterMap.                        | Hendrich (EU)  |
| 328573411062  | 1&1 Versatel GmbH   | 1und1.net     | 1&1 Versatel (United Internet); German B2B fiber operator (~68,000 km). 1und1.net is its canonical B2B site. united-internet.de. | Hendrich (EU)  |
| 328573417154  | dtms GmbH           | dtms.de       | dtms GmbH; Mainz CCaaS / customer-intelligence + service numbers; licensed connection-network operator. Official + LinkedIn.     | Hendrich (EU)  |
```

Research notes:
- 1&1 Versatel (328573411062) was flagged as a MISDOMAIN suspect before research: the name is the B2B fiber operator, and `1und1.net` superficially resembles the 1&1 consumer brand. Verified FALSE - `1und1.net` is 1&1 Versatel's own canonical B2B domain (it hosts the official 1&1 Versatel corporate presentations; United Internet lists it as the brand site). No domain correction.
- Several MATCH records are advisory / software / SI businesses (Odine, Savecall, CGI, dtms) rather than carriers/operators. ICP fit and segment are R1's call - R0 confirms only name-vs-domain identity, which is clean for all.

```
Domain Corrections - review (MEDIUM): none.
Renames - review (MEDIUM): none.
Hard-flagged for deletion: none.

Tier 3 held (4 standing carryovers; 0 NEW this run, 0 drained):

| Date first surfaced | ID           | Domain (name)                          | Issue                                                                                              | Disposition                                          |
| ------------------- | ------------ | -------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| 2026-06-09          | 326642118391 | wechsler.ch                            | AMBIGUOUS; multiple distinct Swiss "Wechsler" entities, domain not positively identified, no name. | HELD - await Cooper. Re-verified present, no action. |
| 2026-06-09          | 326731977463 | bertellifamily.org                     | Suspected private family foundation / non-business. MEDIUM hard-flag (below HIGH auto-flag bar).    | HELD - await Cooper. Re-verified present.            |
| 2026-05-26          | 324597786339 | finetechnologies.co ("columbus-networks") | Directional ambiguity (Columbus/Liberty Networks slug vs unrelated FL MSP domain).              | HELD - await Cooper. Re-verified present.            |
| 2026-06-09          | 326713856698 | t.ht.hr                                | Hrvatski Telekom (Croatia) subdomain artifact; no standalone identity.                              | HELD for R3 dedup. Re-verified present.              |
```

Caps & budget:
- Record cap: 100 (10 used).
- Apollo credits: 0 (Apollo-free routine).
- web_search: ~10 used (1 per record; all reached HIGH confidence on first pass, no second query needed).
- web_fetch: 0 (web_search sufficient at HIGH for all 10).
- HubSpot writes: 1 batch of 10, 0 failures.
- Ledger canvas (F0B0AFSB9LN): read at run start (drained/re-evaluated R0 carryovers); Run-log row + Tier 3 status appended at run end.
