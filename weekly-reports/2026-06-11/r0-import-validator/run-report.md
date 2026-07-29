# CRM Guardian - Import Validator - 2026-06-11 - 0 domain-corrected, 3 renamed, 0 flagged, 5 held

Run summary: 9 records scanned, 0 MISDOMAIN / 3 RENAMABLE / 1 MATCH / 0 HARD_FLAG / 0 DEAD_DOMAIN / 5 AMBIGUOUS-Tier 3, 4 HubSpot writes, 0 errors

What needs Cooper's attention:
- 5 Tier 3 holds - the "ZZZ QA ..." test records (see table below). These are synthetic QA fixtures (zzz-qa-*.com placeholder domains, zero public footprint, created 2026-06-10 17:25-20:17 UTC). By the book they bucket DEAD_DOMAIN, but they are clearly deliberately created test records (R6 reached the same read this morning), so R0 held rather than auto-flagged to avoid disrupting an active QA test. Confirm disposition: flag for deletion, delete directly, or leave in place while testing continues.
- Ledger drain: 5 R0 carryovers were resolved downstream on 2026-06-10 (moved to Flagged for deletion, high_90) and were removed from the ledger: indatelservices.com, teampoka.com, us.ntt.net, g.softbank.co.jp, gatco.net. 6 carryovers remain (3 awaiting R3 dedup, 3 awaiting Cooper).

Run health: YELLOW
- Writes all succeeded, 0 errors, but Tier 3 holds present.

Errors: None

## Renames - HIGH confidence (Tier 1 writes)

```
| ID           | Domain                  | Old name | New name              | Evidence                                                                                  |
|--------------|-------------------------|----------|-----------------------|-------------------------------------------------------------------------------------------|
| 326675587819 | longlines.biz           | (blank)  | Long Lines Broadband  | longlines.biz is Long Lines' own domain (facebook@longlines.biz on official FB; canonical site longlines.com). Iowa tri-state broadband operator, Schurz-owned since 2015. R6 independently placed HQ in Iowa. |
| 326675592899 | lumosnet.com            | (blank)  | Lumos Networks        | lumosnet.com is the legacy Lumos Networks domain redirecting to lumosfiber.com. VA/NC/SC fiber operator, now part of T-Mobile Fiber. Bloomberg/Wikipedia/LinkedIn corroborate. Canonical domain now lumosfiber.com - left for R1 to evaluate. |
| 326986523374 | anthembusinessgroup.com | (blank)  | Anthem Business Group | LinkedIn company page + CEO profile confirm Anthem Business Group, shared-services parent of Anthem Broadband (ID/OR/NV/MT ISP), Dynamite Wireless, Northwest Datacom. R6 independently corrected owner to Cunningham/West via Apollo (Idaho). |
```

All three left with blank `last_enriched_date` so R1 (10:00 AM CT) picks them up for full enrichment per stamping policy.

## MATCH

```
| ID           | Domain                | Name                | Action                                            |
|--------------|-----------------------|---------------------|---------------------------------------------------|
| 326979656425 | experiencemosaic.com  | Mosaic Technologies | MATCH (Cameron WI fiber broadband co-op, 110+ employees, $12.6M WI PSC grants 2024). signal_heat defaulted to Cold. No other writes; R1 enriches. |
```

## Tier 3 held - ZZZ QA test records (no writes)

```
| ID           | Domain                       | Name                     | web_search summary                                      |
|--------------|------------------------------|--------------------------|----------------------------------------------------------|
| 326958660290 | zzz-qa-prospect-b.com        | ZZZ QA Prospect B        | No public footprint; synthetic placeholder domain        |
| 326617190107 | zzz-qa-happy-prospect.com    | ZZZ QA Happy Prospect    | No public footprint; synthetic placeholder domain        |
| 326967068387 | zzz-qa-conflict-prospect.com | ZZZ QA Conflict Prospect | No public footprint; synthetic placeholder domain        |
| 326975435454 | zzz-qa-retest-clean.com      | ZZZ QA Retest Clean      | No public footprint; synthetic placeholder domain        |
| 326675544806 | zzz-qa-retest-conflict.com   | ZZZ QA Retest Conflict   | No public footprint; synthetic placeholder domain        |
```

Judgment call (noted for autonomous run): DEAD_DOMAIN flag was the literal bucket, but the naming convention and same-day creation pattern indicate intentional QA fixtures, and the hard-flag bar requires a confirmed hard-flag category. Held per Invariant F. If Cooper confirms they are disposable, next R0 run (or Cooper directly) can flag them.

## Ledger changes

- Removed (resolved 2026-06-10 downstream): indatelservices.com (326184182509), teampoka.com (325800222448), us.ntt.net (325335796410), g.softbank.co.jp (325335795443), gatco.net (324524875475)
- Carried (6): wechsler.ch (326642118391), bertellifamily.org (326731977463), columbus-networks / finetechnologies.co (324597786339) - awaiting Cooper; bb.softbank.co.jp (326694120179), consultants.ooredoo.qa (326735614700), t.ht.hr (326713856698) - awaiting R3 dedup
- Added (5): the ZZZ QA records above

Apollo credits consumed: 0 (Apollo-free by design)
