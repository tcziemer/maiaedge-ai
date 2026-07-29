CRM Guardian - Import Validator - 2026-06-03 - 0 domain-corrected, 0 renamed, 0 flagged, 0 held (NEW)

Run summary: 2 records scanned, 2 MATCH / 0 MISDOMAIN / 0 RENAMABLE / 0 HARD_FLAG / 0 DEAD_DOMAIN / 0 AMBIGUOUS, 2 HubSpot writes, 0 errors. 4 prior R0 Tier 3 carryover holds re-evaluated; all 4 carry forward unchanged (none resolved by Cooper since 2026-06-02 run).

What needs Cooper's attention:
- 0 NEW Tier 3 holds this run.
- 4 standing R0 Tier 3 carryover holds remain pending Cooper / R3 dedup adjudication (see Tier 3 table below). No action newly required - these are unchanged from the 2026-06-02 run.
- 0 medium-confidence corrections to verify.
- 0 hard-flagged companies.

Run health: GREEN
- 0 errors, 0 NEW Tier 3 holds, all writes succeeded. (4 pre-existing carryover holds standing, already on Cooper's plate; not new this run.)

Errors: None

Window: createdate GTE 2026-06-02T14:02:49Z (ET 10:02), last_enriched_date IS EMPTY, customer_segment NEQ "Flagged for deletion", excl. 124293230301. Sort createdate ASC. Cap 100. Returned: 2.

---

## MATCH (2) - no enriched-field writes; left for R1 Fresh Enrichment at 10:00 AM CT

```
| HubSpot ID    | Name               | Domain                  | Confidence | Evidence (web_search)                                                                                           | Action                          |
| 325540511471  | FreeConferenceCall | freeconferencecall.com  | HIGH       | FreeConferenceCall.com LLC, conferencing/collaboration provider (Long Beach CA, est. 2001, 800k+ business      | signal_heat=Cold (new-record    |
|               |                    |                         |            | customers). Wikipedia + LinkedIn + Crunchbase + company About page agree. Name maps 1:1 to domain.             | default). last_enriched_date    |
|               |                    |                         |            |                                                                                                                | left blank for R1.              |
| 325636927166  | Optum              | optum.com               | HIGH       | Optum, health services/tech arm of UnitedHealth Group (Eden Prairie MN, ~300k employees, OptumHealth/Insight/  | signal_heat=Cold (new-record    |
|               |                    |                         |            | Rx). Wikipedia + SEC filings + company About page agree. Name maps 1:1 to domain.                             | default). last_enriched_date    |
|               |                    |                         |            |                                                                                                                | left blank for R1.              |
```

Customer-protection check: neither candidate has any closed-won deal (verified via associated-deals query, hs_is_closed_won = true → 0 results). signal_heat default write authorized.

Note: ICP fit for both records is R1's call. Optum may pass the Enterprise (Healthcare Systems) ICP scale gate; FreeConferenceCall is a UCaaS/conferencing provider and likely non-ICP - but R0 does not flag it (name matches domain, not a hard-flag category). Both correctly left at blank last_enriched_date for R1.

## Domain Corrections (0)
None.

## Renames (0)
None.

## Hard-flagged (0)
None.

## Tier 3 held (4 carryover - 0 NEW this run)

```
| date_first_surfaced | HubSpot ID    | Name              | Domain              | Why held                                                                                          | Status this run                                  |
| [2026-05-27]        | 324524875475  | (blank)           | gatco.net           | No clear public-entity match; candidates (GATCO Fine Bathware, GATCO Global UK, GATS Telecom,     | CARRY - unchanged (blank name/segment, no        |
|                     |               |                   |                     | GETCO Telecom) diverge.                                                                            | last_enriched_date). Pending Cooper.             |
| [2026-05-27]        | 324597786339  | columbus-networks | finetechnologies.co | Directional ambiguity: slug = Columbus Networks / Liberty Networks; domain = unrelated FL MSP.    | CARRY - unchanged. MISDOMAIN vs RENAMABLE        |
|                     |               |                   |                     |                                                                                                   | unresolved; Cooper to confirm import intent.     |
| [2026-06-02]        | 325335795443  | (blank)           | g.softbank.co.jp    | No-name SoftBank group subdomain; probable duplicate of SoftBank AI Cloud (324007728852).         | CARRY - unchanged. Held for Cooper / R3 dedup.   |
| [2026-06-02]        | 325335796410  | (blank)           | us.ntt.net          | NTT Global IP Network backbone subdomain; near-duplicate of NTT (277437319928) / NTT Global DC    | CARRY - unchanged. Held for Cooper / R3 dedup.   |
|                     |               |                   |                     | (133486361310).                                                                                   |                                                  |
```

web_search / web_fetch budget used: 2 web_search calls (1 per MATCH candidate). 0 MISDOMAIN discovery searches needed. No proxy blocks encountered.
