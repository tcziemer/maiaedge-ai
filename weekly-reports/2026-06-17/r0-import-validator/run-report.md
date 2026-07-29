CRM Guardian - Import Validator - 2026-06-17 - 0 domain-corrected, 2 renamed, 0 flagged, 0 held

Run summary: 3 records scanned, 2 RENAMABLE + 1 MATCH (0 domain-corrected / 2 renamed / 0 hard-flagged / 0 NEW Tier 3 held), 3 HubSpot writes, 0 errors

What needs Cooper's attention:
- 0 new Tier 3 holds this run.
- 0 hard-flagged companies this run.
- 2 HIGH-confidence renames written directly (Schwarz Digits, NXLink) - no review needed; segment left for R1 Fresh Enrichment at 10:00 AM CT.
- 5 standing R0 Tier 3 carryover holds drained this run (all five zzz-qa-* synthetic QA fixtures were deleted from HubSpot by Cooper since the prior run). 4 R0 Tier 3 carryovers remain standing.

Run health: GREEN
- 0 errors, 0 new Tier 3 holds, all 3 writes succeeded.

Errors: None

--------------------------------------------------------------------------------

RENAMABLE (HIGH; renamed, segment left for R1 at 10:00 AM CT; last_enriched_date left blank):

```
| Old name | New name       | ID           | Domain          | Entity at domain (web_search)                                                                                                                                                                                       | Conf |
| -------- | -------------- | ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| (blank)  | Schwarz Digits | 327944646384 | digits.schwarz  | Schwarz Digits - IT/digital-services arm of Germany's Schwarz Group (Lidl/Kaufland parent); STACKIT sovereign cloud + 200MW Luebbenau data-center campus (up to 100k GPUs). .schwarz is a Schwarz-exclusive brand TLD, so the domain is authentic. Owner Tim Z (Intl), DE. | HIGH |
| (blank)  | NXLink         | 328126464704 | team.nxlink.com | NXLink - cloud-native CCaaS platform by Singapore-based NXAI (voice/chat/SMS/WhatsApp); sibling brand NXCloud = CPaaS messaging. team.nxlink.com is a portal subdomain of nxlink.com. Likely application-layer (non-carrier); R1 to confirm ICP fit. Owner Ken (West), TX. | HIGH |
```

MATCH (left for R1; signal_heat=Cold default written):

```
| Company             | ID           | Domain               | Entity at domain (web_search)                                                                                                                                                              | Conf |
| ------------------- | ------------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Omada Technologies  | 328067841760 | omadatechnologies.com | Omada Technologies - New England IT VAR (network infra, security, data protection, storage), HQ Portsmouth NH, founded 2017, <25 employees. Name matches domain; existing brief accurate. Already customer_segment=Other (channel partner). Owner Tim Lieto (East), NH. | HIGH |
```

Domain Corrections - review: none
Renames - review (MEDIUM): none (both renames HIGH confidence, written directly)
Hard-flagged: none
Tier 3 held (NEW this run): none

--------------------------------------------------------------------------------

Drained this run (5, removed from ledger - all deleted from HubSpot by Cooper since prior run):
- zzz-qa-prospect-b.com (326958660290) - synthetic QA fixture; record no longer exists in HubSpot (notFound on re-read).
- zzz-qa-happy-prospect.com (326617190107) - synthetic QA fixture; record no longer exists.
- zzz-qa-conflict-prospect.com (326967068387) - synthetic QA fixture; record no longer exists.
- zzz-qa-retest-clean.com (326975435454) - synthetic QA fixture; record no longer exists.
- zzz-qa-retest-conflict.com (326675544806) - synthetic QA fixture; record no longer exists.

Carryover R0 Tier 3 holds (4 standing; carried unchanged; all re-verified present in HubSpot this run):
- [2026-06-09] wechsler.ch (326642118391) - AMBIGUOUS; multiple distinct Swiss "Wechsler" entities, domain not positively identified, no name to anchor. HELD. Awaiting Cooper.
- [2026-06-09] bertellifamily.org (326731977463) - suspected private family foundation / non-business. MEDIUM hard-flag -> Tier 3. HELD. Awaiting Cooper.
- [2026-05-26] columbus-networks / finetechnologies.co (324597786339) - directional ambiguity (Columbus/Liberty Networks slug vs unrelated FL MSP domain). HELD. Awaiting Cooper.
- [2026-06-09] t.ht.hr (326713856698) - Hrvatski Telekom (Croatia) subdomain artifact; no standalone identity. Held for R3 dedup.

--------------------------------------------------------------------------------

Run parameters:
- Trigger window: createdate GTE 2026-06-16T14:02:24Z (now-24h, ET 10:02). Cap 100. 3 candidates returned (single page).
- MaiaEdge own record (124293230301): not present in window.
- Customer-protection / closed-won hard stops: none triggered (all 3 are fresh leads / channel partner, no associated deals).
- Apollo credits consumed: 0 (Apollo-free routine).
- web_search: 4 total (Schwarz Digits x1, NXLink x2, Omada x1). web_fetch: 0 (web_search sufficient for all three HIGH-confidence determinations).
- HubSpot writes: 3 (Schwarz Digits name+account_brief; NXLink name+account_brief; Omada signal_heat=Cold). 1 batch, 0 errors, 0 retries.
