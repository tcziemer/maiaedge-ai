CRM Guardian - Import Validator - 2026-06-09 - 0 domain-corrected, 7 renamed, 1 flagged, 5 held

Run summary: 40 records scanned (bulk-import spike of international carriers, NeoClouds, and noise), buckets 0 MISDOMAIN / 7 RENAMABLE / 1 HARD_FLAG / 5 Tier 3 held / 27 MATCH, 35 HubSpot writes, 0 errors.

What needs Cooper's attention:
- 5 Tier 3 holds (see tables below) - 1 ambiguous (wechsler.ch), 1 suspected non-business (bertellifamily.org), 3 carrier subdomain artifacts routed to R3 dedup (bb.softbank.co.jp, consultants.ooredoo.qa, t.ht.hr).
- 0 hard-flagged companies this run requiring archive review beyond the 1 below: Filter HubSpot Companies -> customer_segment = "Flagged for deletion" to find YTL Hotels (ytlhotels.co.uk).
- 1 medium-confidence rename to verify: LitFiber (litfiber.org) - canonical public domain may be litfiber.us; R1 full enrichment should confirm domain.
- 6 prior R0 Tier 3 holds carried forward unchanged (Cooper has not acted; all re-checked against current HubSpot state - still blank name/segment, no last_enriched_date).

Run health: YELLOW
- Writes all succeeded (35/35) but 5 NEW Tier 3 holds present + 1 medium-confidence rename flagged for verification.

Errors: None.

last_enriched_date stamping: left BLANK on all RENAMABLE + MATCH records (R1 Fresh Enrichment picks them up at 10:00 AM CT). Stamped 2026-06-09 only on the 1 HARD_FLAG eviction (YTL Hotels) per the unified stamping policy.

---

## Renames (7) - Tier 1 HIGH (6) + Tier 2 MEDIUM (1)

```
| HubSpot ID    | Domain            | Old name                       | New name           | Conf   | Entity at domain (web_search)                                                                 |
| ------------- | ----------------- | ------------------------------ | ------------------ | ------ | -------------------------------------------------------------------------------------------- |
| 326717559539  | recursal.ai       | (blank)                        | Recursal AI        | HIGH   | Recursal AI, SF startup; serverless inference for open-source models, RWKV/Eagle LLM lineage. |
| 326710146783  | sambanova.com     | (blank)                        | SambaNova Systems  | HIGH   | SambaNova Systems, Palo Alto AI chip (RDU) + inference cloud for enterprise/sovereign AI.     |
| 326585989844  | denvr.com         | Dan.com - a GoDaddy brand      | Denvr Dataworks    | HIGH   | Denvr Dataworks, Calgary AI cloud; H200/H100/A100 GPU compute. Old name = Dan.com aftermarket scraping artifact. |
| 326154804931  | neysanetworks.com | (blank)                        | Neysa Networks     | HIGH   | Neysa (fka Neysa Networks), Mumbai AI accel cloud; $1.2B raise led by Blackstone.             |
| 326722976497  | stackit.cloud     | (blank)                        | STACKIT            | HIGH   | STACKIT, Schwarz Group (Lidl/Kaufland) sovereign cloud + colo; multiple EU DCs.              |
| 326585995981  | lxp.lu            | (blank)                        | LuxProvide         | HIGH   | LuxProvide S.A., LuxConnect subsidiary; operates MeluXina supercomputer (Bissen DC2).        |
| 326710261493  | litfiber.org      | (blank)                        | LitFiber           | MEDIUM | LitFiber, Madisonville KY FTTH ISP (Oak Hill Capital, merging w/ Omni Fiber). Canonical may be litfiber.us - verify in R1. |
```

## Hard-flagged (1) - Tier 2 HIGH

```
| HubSpot ID    | Domain           | Reason code                 | Entity at domain (web_search)                                                          |
| ------------- | ---------------- | --------------------------- | ------------------------------------------------------------------------------------- |
| 326690363078  | ytlhotels.co.uk  | Hard junk / non-business    | YTL Hotels, luxury hospitality arm of YTL conglomerate (UK/EU/Asia hotels & resorts). No carrier-infra path. last_enriched_date stamped 2026-06-09. |
```

## Tier 3 held (5 NEW) - no write, surfaced for Cooper

```
| HubSpot ID    | Domain                  | Type                         | web_search summary                                                                                          |
| ------------- | ----------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 326642118391  | wechsler.ch             | AMBIGUOUS                    | Multiple distinct Swiss "Wechsler" entities (line construction, butcher, IT consultant, real estate); domain wechsler.ch not positively identified to one. No name to anchor. HELD, not auto-flagged. |
| 326731977463  | bertellifamily.org      | Suspected non-business (MED) | "family.org" pattern; closest matches are private family foundations (e.g. Bertin Family Foundation). bertellifamily.org not positively identified. MEDIUM hard-flag -> Tier 3, not auto-flagged. |
| 326694120179  | bb.softbank.co.jp       | Subdomain dup -> R3 dedup    | SoftBank broadband subdomain artifact; near-dup of SoftBank records (incl. SoftBank Capital softbank.com 326735614690 in same batch). Held for R3 dedup. |
| 326735614700  | consultants.ooredoo.qa  | Subdomain dup -> R3 dedup    | Ooredoo (Qatar telecom) consultants subdomain artifact; no standalone identity. Held for R3 dedup vs any Ooredoo parent record. |
| 326713856698  | t.ht.hr                 | Subdomain dup -> R3 dedup    | Hrvatski Telekom (Croatia) subdomain artifact; no standalone identity. Held for R3 dedup vs any Hrvatski Telekom parent record. |
```

## Carryover R0 Tier 3 holds (6) - re-checked, unchanged, carried forward

```
| Date first surfaced | HubSpot ID    | Domain / slug                          | Status                                                                  |
| ------------------- | ------------- | -------------------------------------- | ---------------------------------------------------------------------- |
| 2026-06-05          | 326184182509  | indatelservices.com                    | Dup of INDATEL (322761764552); held for R3 dedup. CARRY.               |
| 2026-06-04          | 325800222448  | teampoka.com                           | Dup of Poka Lambro Telecom (320876610271); routed R3 dedup. CARRY.     |
| 2026-05-27          | 324524875475  | gatco.net                              | No clear public-entity match (India-registered); ambiguous. CARRY.     |
| 2026-05-27          | 324597786339  | columbus-networks / finetechnologies.co | Directional ambiguity (slug Columbus/Liberty Networks vs FL MSP domain). CARRY. |
| 2026-06-02          | 325335795443  | g.softbank.co.jp                       | SoftBank subdomain artifact; dup. Routed R3 dedup. CARRY.              |
| 2026-06-02          | 325335796410  | us.ntt.net                             | NTT Global IP backbone subdomain; near-dup of NTT (277437319928). CARRY. |
```

## MATCH (27) - signal_heat = Cold default written, last_enriched_date left blank for R1

326644726503 Replicate (replicateinc.com), 326715774698 FPT Software, 326701494983 Intellinet, 326712100572 Bit Digital, 326735606513 MyRealData (Real Time Cloud Services brand), 326745948917 Ace Cloud Hosting, 326735587023 Reliance Industries Limited, 326699661004 YTL, 326735614690 SoftBank Capital, 326694120171 iGenius, 326175264490 Ibghy Architectes (non-ICP architecture firm - R1 will evict), 326722976489 DISH Network, 326390414029 exoscale, 326390414028 T-Mobile Polska, 326719389425 OIB, 326674182894 Bits in Flight Ltd, 326690362102 SEOX (non-ICP SEO agency - R1 will evict), 326692100825 Telenor Sweden, 326168029929 Vivo (Telefonica Brasil), 326712109770 Indus Towers, 326642119370 Telenor Pakistan, 326674183868 SKTA Innopartners, 326644735707 Swiss Life (insurer - R1 to assess), 326745988819 Riversand (MDM software - R1 to assess), 326381387478 Telenor Danmark, 326381387481 Swiss Re (reinsurer - R1 to assess), 326646278880 Assembly (assembly.nl, European sovereign private AI infra).

Notes: Several MATCH records are clearly non-ICP (Ibghy Architectes, SEOX, Riversand, Swiss Life, Swiss Re) but name and domain agree, so R0 leaves them for R1 to evict Apollo-free via Path gamma rather than auto-flagging. Apollo consumed this run: 0.
