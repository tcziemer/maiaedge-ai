CRM Guardian - Import Validator - 2026-06-16 - 0 domain-corrected, 0 renamed, 0 flagged, 0 held

Run summary: 2 records scanned, 2 MATCH (0 domain-corrected / 0 renamed / 0 hard-flagged / 0 held), 2 HubSpot writes (signal_heat=Cold defaults), 0 errors

What needs Cooper's attention:
- 0 new Tier 3 holds this run.
- 0 hard-flagged companies this run.
- 9 standing R0 Tier 3 carryover holds remain (unchanged) - see Carryover section. 2 prior holds drained this run.

Run health: GREEN
- 0 errors, 0 new Tier 3 holds, both writes succeeded.

Errors: None

--------------------------------------------------------------------------------

MATCH (left for R1 Fresh Enrichment at 10:00 AM CT; signal_heat=Cold default written):

```
| Company                              | ID           | Domain      | Entity at domain (web_search)                                                                                          | Conf |
| ------------------------------------ | ------------ | ----------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Continental Resources, Inc. (ConRes) | 327581670131 | conres.com  | Continental Resources (ConRes) - women-owned IT VAR / data-center solutions + test-equipment provider, Bedford MA. Name matches domain. type=PARTNER. | HIGH |
| Wasabi Technologies                  | 327644780240 | wasabi.com  | Wasabi Technologies - Boston-based cloud object-storage provider (acquired Seagate Lyve Cloud Apr 2026). Name matches domain. | HIGH |
```

Domain Corrections - review: none
Renames - review: none
Hard-flagged: none
Tier 3 held (NEW this run): none

--------------------------------------------------------------------------------

Drained this run (2, removed from ledger):
- bb.softbank.co.jp (326694120179) - now customer_segment="Flagged for deletion", reason "Duplicate (merged): contacts reassociated to primary SoftBank AI Cloud (324007728852)". Resolved by downstream dedup.
- consultants.ooredoo.qa (326735614700) - now customer_segment="Flagged for deletion", reason "Duplicate (merged): contacts reassociated to primary Ooredoo Qatar AI Cloud (303442039544)". Resolved by downstream dedup.

Carryover R0 Tier 3 holds (9 standing; carried unchanged):
- [2026-06-11] zzz-qa-prospect-b.com (326958660290) - "ZZZ QA Prospect B"; synthetic QA fixture, zero public footprint. HELD - Cooper to confirm disposition.
- [2026-06-11] zzz-qa-happy-prospect.com (326617190107) - "ZZZ QA Happy Prospect"; synthetic QA fixture. HELD.
- [2026-06-11] zzz-qa-conflict-prospect.com (326967068387) - "ZZZ QA Conflict Prospect"; synthetic QA fixture. HELD.
- [2026-06-11] zzz-qa-retest-clean.com (326975435454) - "ZZZ QA Retest Clean"; synthetic QA fixture. HELD.
- [2026-06-11] zzz-qa-retest-conflict.com (326675544806) - "ZZZ QA Retest Conflict"; synthetic QA fixture. HELD.
- [2026-06-09] wechsler.ch (326642118391) - AMBIGUOUS; multiple distinct Swiss "Wechsler" entities, domain not positively identified, no name to anchor. HELD. Awaiting Cooper.
- [2026-06-09] bertellifamily.org (326731977463) - suspected private family foundation / non-business ("family.org" pattern). MEDIUM hard-flag -> Tier 3. HELD. Awaiting Cooper.
- [2026-05-26] columbus-networks / finetechnologies.co (324597786339) - directional ambiguity (Columbus/Liberty Networks slug vs unrelated FL MSP domain). HELD. Awaiting Cooper.
- [2026-06-09] t.ht.hr (326713856698) - Hrvatski Telekom (Croatia) subdomain artifact; no standalone identity. Held for R3 dedup.

--------------------------------------------------------------------------------

Run parameters:
- Trigger window: createdate GTE 2026-06-15T14:03:51Z (now-24h, ET 10:03). Cap 100. 2 candidates returned (single page).
- MaiaEdge own record (124293230301): not present in window.
- Customer-protection / closed-won hard stops: none triggered.
- Apollo credits consumed: 0 (Apollo-free routine).
- web_search: 2 (1 per candidate). web_fetch: 0 (web_search sufficient for both HIGH-confidence MATCHes).
