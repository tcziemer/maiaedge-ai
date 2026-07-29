# CRM Guardian - Import Validator - 2026-06-12 - 0 domain-corrected, 2 renamed, 1 flagged, 0 held

Run summary: 5 records scanned (createdate window 2026-06-11T14:03Z -> 2026-06-12T14:03Z), buckets: 2 RENAMABLE HIGH / 1 HARD_FLAG HIGH / 2 MATCH / 0 MISDOMAIN / 0 AMBIGUOUS / 0 DEAD_DOMAIN, 5 HubSpot writes (1 batch, 5/5 succeeded, read-back verified), 0 errors

What needs Cooper's attention:
- 1 hard-flagged company - Union Transtel (327020648154) - Filter HubSpot Companies -> customer_segment = "Flagged for deletion"
- 11 ledger carryover holds remain open (none Cooper-resolved since prior run): 5 ZZZ QA fixtures awaiting Cooper disposition (326675544806, 326975435454, 326967068387, 326617190107, 326958660290 - held write-free per R6 precedent), 4 subdomain/dup artifacts awaiting R3 dedup (bb.softbank.co.jp 326694120179, consultants.ooredoo.qa 326735614700, t.ht.hr 326713856698, wechsler.ch 326642118391*), 2 ambiguous (bertellifamily.org 326731977463, columbus-networks/finetechnologies.co 324597786339). *wechsler.ch is the AMBIGUOUS Swiss-entities hold, grouped with R3-routed in prior ledger wording.
- Data quality note for R1/R6 (no R0 write - outside pre-authorized scope): Integrity Advanced Technologies (327026419390) carries country=Brazil, but the company is a North Dakota-headquartered, tribally owned JV (Teya Support Services + Integrity Technologies Corp, formed 2024). Owner currently Tim Ziemer (International) via the Brazil value. R1 full enrichment today should re-derive geography/owner.

Run health: GREEN
- 0 errors, 0 NEW Tier 3 holds, all writes succeeded and verified by read-back
- web_fetch unavailable this session (provenance restriction in runtime); all determinations made on web_search per the opportunistic-enhancement rule - no confidence downgrades applied
- DNS resolution checked via nslookup for all 5 domains: all resolve, no NXDOMAIN

Errors: None

## Renames (Tier 1, HIGH confidence)

```
| HubSpot ID   | Old name | New name                       | Domain        | Evidence                                                                                                    |
|--------------|----------|--------------------------------|---------------|-------------------------------------------------------------------------------------------------------------|
| 327063752413 | (empty)  | Fort Mojave Telecommunications | ftmojave.net  | ftmojave.net is FMTI's contact/email domain (contact@ftmojave.net; RocketReach email-format listing).        |
|              |          |                                |               | Tribal ILEC operating fiber + telephone in Mohave Valley AZ - carrier-infrastructure carveout, NOT hard-flag.|
| 327072714478 | (empty)  | Inland Cellular                | inlandcell.com| inlandcell.com is an alternate Inland Cellular employee email domain (LeadIQ/SignalHire); state=Idaho        |
|              |          |                                |               | matches footprint (Lewiston/Moscow ID + SE WA regional wireless carrier, est. 1989).                         |
```

Both records left with blank last_enriched_date - R1 Fresh Enrichment picks them up at 10:00 AM CT (blank-segment filter). signal_heat left for R1 Path alpha default (Cold default is MATCH-path-only per R0 spec).

## Hard-flagged (Tier 2, HIGH confidence)

```
| HubSpot ID   | Name           | Domain            | Category                  | Reason code | Evidence                                                                  |
|--------------|----------------|-------------------|---------------------------|-------------|---------------------------------------------------------------------------|
| 327020648154 | Union Transtel | uniontranstel.com | Infrastructure CONTRACTOR | No ICP fit  | Union TransTel LLC, Oceanside CA (own site unioncorporation.net, ZoomInfo,|
|              |                |                   | (builds, doesn't operate) |             | Crunchbase, D&B agree): telecom infrastructure consulting - site surveys, |
|              |                |                   |                           |             | install/de-install, DC power plant, NOC builds. No operated network.      |
```

last_enriched_date stamped 2026-06-12 (definitive eviction). Reason code choice: R0 prompt's HARD_FLAG template suggests "Hard junk / non-business", but Union TransTel is a real business in a no-ICP-path category; per property-schema section 2.1 semantics (framework wins on conflict), "No ICP fit" is the truthful code. Record state was name+domain same business, so no MISDOMAIN redemption.

## MATCH (passed clean to R1)

```
| HubSpot ID   | Name                            | Domain              | Note                                                                                     |
|--------------|---------------------------------|---------------------|-------------------------------------------------------------------------------------------|
| 327026292423 | Grantsburg Telecom              | grantsburgtelcom.com| Initially looked MISDOMAIN (canonical site is grantsburgtelcom.net) but the company       |
|              |                                 |                     | publishes office@grantsburgtelcom.com - the .com is their own email domain. Same business |
|              |                                 |                     | (Farmers Independent Telephone Co. dba Grantsburg Telcom, WI fiber ILEC, est. 1907).      |
|              |                                 |                     | Domain left as-is. signal_heat defaulted Cold.                                            |
| 327026419390 | Integrity Advanced Technologies | integrityatech.com  | Name and domain identify the same business (ND-HQ tribally owned JV, 2024; national fiber |
|              |                                 |                     | footprint + satellite/SD-WAN/DC solutions). signal_heat defaulted Cold. Country=Brazil    |
|              |                                 |                     | anomaly noted above for R1/R6.                                                            |
```

## Tier 3 held (NEW this run)

None.

## Ledger carryover drain evaluation

All 16 candidate hold IDs re-read from HubSpot this run. The 5 holds flagged 2026-06-10 (g.softbank.co.jp 325335795443, us.ntt.net 325335796410, teampoka.com 325800222448, indatelservices.com 326184182509, gatco.net 324524875475) were already drained from the ledger by the 2026-06-11 run. The 11 remaining holds are unchanged in HubSpot (no segment set, no Cooper action detected) -> all CARRY. No re-investigation performed: each carries a documented disposition (Cooper disposition / R3 dedup queue) from prior runs; nothing new for R0 to add without Cooper input.

## Run mechanics

- Customer protection: 0 of 5 candidates have closed-won deals (verified via deals search before any write).
- MaiaEdge own record: not in candidate set.
- Apollo credits: 0 (routine is Apollo-free).
- web_search calls: 7 (within ~2/record budget). web_fetch: 0 (provenance-restricted; opportunistic only, no penalty).
- Trigger query: single page, total=5, sorted createdate ASC. Cap 100 not approached.
- Canvas read: first attempt returned connector error; retry succeeded (956KB canvas, parsed via grep offline). Non-blocking.
