CRM Guardian - Flagged Consolidation - 2026-06-04 - 0 contacts flagged, 0 reassociated, 17 Tier 3 held

Run summary: 150 flagged companies processed (of 250 in queue; 150-company cap reached, 100 carried to next run) · 362 contacts evaluated · 0 Tier 1 Mode B flags / 0 Mode A reassociations / 17 Tier 3 holds · 0 HubSpot writes (idempotent steady-state run) · 150 companies fully resolved (77 zero-contact + 73 with all contacts already flagged or preserved)

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then Filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (this severs the stale associations from reassociated contacts)

- 345 contacts across this in-cap set already carry flagged_for_deletion = true from prior runs (idempotent; no re-write needed) and are awaiting Cooper's bulk-delete.
- 17 Tier 3 holds in the table below: preserved contacts (recent activity within 90 days) sitting on flagged non-fit / defunct / duplicate companies with no ICP primary available for reassociation. Benign; safe default per invariant F.

Run health: YELLOW
- 0 errors, 0 writes, 0 mis-flag investigations requiring Cooper action.
- YELLOW (not GREEN) solely because 17 benign Tier 3 preserved-contact holds are present; PARTIAL because the 150-company cap was reached (100 companies carried to the next run).

Errors: None

Hard-stop / safety checks (all clear this run):
- Customer-protection (closed-won) HARD STOP: 0 fired. 0 deals associated with any of the 73 with-contact companies.
- Open-deal HARD STOP: 0 fired (0 open deals; deal total across the 73 companies = 0).
- Fresh-record safety (createdate within 14 days): 0 skips. Oldest-150 set; max createdate 2026-04-01, well outside the 14-day window.
- Pre-Phase-1 Enterprise defensive check (C-bis): 3 account_brief keyword candidates surfaced (C7 Data Centers, ColoSpace, Pac-West Telecomm) and all 3 cleared as false positives - C7 = defunct Utah colo (DataBank subsidiary/duplicate), ColoSpace = defunct New England colo (FirstLight-acquired), Pac-West = defunct CA CLEC whose "bank" keyword came from a MISDOMAIN note (domain now points to Pacific Western Bank), not because the company is a bank. None are genuine Enterprise-ICP mis-flags. All three are zero-contact and correctly flagged.
- Open POC ticket check: 0 tickets associated with any of the 73 companies.

Note on cap/ordering: queue sorted by hs_object_id ASC (oldest first), consistent with prior runs. This in-cap set is the same oldest-150 non-fit/defunct/duplicate population that 06-01/06-02/06-03 drained; it stays fully flagged-and-held until Cooper archives the companies, which shifts the 150-window forward. Newer high-ID companies (positions 151-250, including any with un-flagged contacts) are processed once the oldest companies clear via archival.

---

## Tier 3 held - preserved contacts, no ICP primary (17)

All preserved by recent activity (notes_last_updated / notes_last_contacted within 90 days). Held, not flagged, not reassociated (companies are flagged non-fits / defunct / duplicates with no non-flagged ICP primary to reassociate to). Auto-re-evaluate next run.

```
| Contact ID    | Name              | Preservation signal(s)                          |
|---------------|-------------------|-------------------------------------------------|
| 494765969108  | Michael Ching     | contacted<=90d, activity<=90d, fresh<=14d       |
| 487432186604  | Rob Schumann      | contacted<=90d, activity<=90d                   |
| 486369299174  | Lynn Bruns        | contacted<=90d, activity<=90d                   |
| 486362106616  | Chris Melloway    | activity<=90d                                   |
| 476652573403  | Michael Hall      | activity<=90d                                   |
| 476512699073  | Jacob Hinton      | activity<=90d                                   |
| 464779318976  | Ryan Sabia        | activity<=90d                                   |
| 455480763107  | Jason Scandrol     | activity<=90d                                  |
| 451588831988  | Sebastian Metti   | activity<=90d                                   |
| 451588830920  | Niraj Yagnik      | activity<=90d                                   |
| 451559667429  | Frank Scandariato | activity<=90d                                   |
| 451518850806  | Colin Sharkey     | contacted<=90d, activity<=90d                   |
| 441467623152  | Steven Garvin     | activity<=90d                                   |
| 314701034216  | Michael Honeycutt | activity<=90d                                   |
| 297261432562  | Rami Yaron        | contacted<=90d, activity<=90d                   |
| 261906818771  | Paulo Machado     | contacted<=90d, activity<=90d                   |
| 261906818770  | Macatoci Kanashiro| contacted<=90d, activity<=90d                   |
```

## Mode A reassociations (0)
None. No flagged company in the in-cap set has a non-flagged ICP primary (same normalized domain/name) to reassociate preserved contacts to. Confirmed non-fit/defunct/duplicate population.

## Mode B flags (0 new)
None. All eligible (not-preserved, not-protected) contacts across the in-cap set already carry flagged_for_deletion = true from prior runs (345 idempotent). 0 new flags written this run.

## Clears (0)
None. No previously-flagged contact in the set newly qualifies as preserved (0 open deals, 0 open POC tickets, no contact crossed the 90-day activity or lifecycle thresholds since prior flagging).
