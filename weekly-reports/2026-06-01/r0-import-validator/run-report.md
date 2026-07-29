CRM Guardian - Import Validator - 2026-06-01 - 0 domain-corrected, 0 renamed, 0 flagged, 0 held (new)

Run summary: 1 record scanned, buckets [MATCH 1 / MISDOMAIN 0 / RENAMABLE 0 / HARD_FLAG 0 / DEAD_DOMAIN 0 / AMBIGUOUS 0], 1 HubSpot write, 0 errors

What needs Cooper's attention:
- 2 R0 Tier 3 carryover holds standing (both first surfaced 2026-05-27, neither acted on by Cooper). Carried forward unchanged this run. See "Tier 3 held - carryover" table below.
- 0 new hard-flags, 0 medium-confidence corrections to verify.

Run health: YELLOW
- All writes succeeded and 0 errors, but 2 carryover Tier 3 holds remain present (carryover-holds-present convention, consistent with the 2026-05-28/05-29 runs).

Errors: None

---

## New candidates (24h createdate window, last_enriched_date empty)

```
| HubSpot ID    | Name    | Domain             | Bucket | Confidence | Action                          | web_search summary                                                                 |
|---------------|---------|--------------------|--------|------------|---------------------------------|------------------------------------------------------------------------------------|
| 325110366958  | Verizon | verizonwireless.com| MATCH  | HIGH       | signal_heat = Cold (new-record default); no last_enriched_date stamp; R1 enriches at 10am CT | HubSpot name "Verizon" and domain verizonwireless.com identify the same carrier (Verizon Wireless = Verizon's wireless brand; parent/brand relationship). On-record description confirms largest US wireless operator. Unambiguous identity - no research search consumed. |
```

Note: Verizon / Verizon Enterprise duplicate-pair validation is an R3 (Duplicate Accounts) responsibility per the post-migration data-quality follow-up list, not an R0 name-vs-domain concern. R0 leaves the record in the active pool for R1 Fresh Enrichment.

## Domain Corrections - review
None.

## Renames - review
None.

## Hard-flagged
None.

## Tier 3 held - carryover (re-evaluated against current HubSpot state)

```
| date_first_surfaced | HubSpot ID    | Name              | Domain             | Why held                                                                                                                              | Status this run                                                              |
|---------------------|---------------|-------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [2026-05-27]        | 324524875475  | (empty)           | gatco.net          | No clear public-entity match. Surfaced candidates (GATCO Fine Bathware, GATCO Global UK, GATS Telecom India, GETCO Telecom) diverge.   | CARRY - record unchanged (no name, no segment, no last_enriched_date). Cooper not acted. |
| [2026-05-27]        | 324597786339  | columbus-networks | finetechnologies.co| Directional ambiguity (name vs domain identify distinct entities; could not resolve MISDOMAIN vs RENAMABLE). Cooper to confirm intent.  | CARRY - record unchanged (name "columbus-networks", domain finetechnologies.co, no segment). Cooper not acted. |
```

## Tier 3 held - new this run
None.

## Ledger
Run-log row appended to canvas F0B0AFSB9LN. Both carryover Tier 3 holds re-confirmed standing (no drains this run).
