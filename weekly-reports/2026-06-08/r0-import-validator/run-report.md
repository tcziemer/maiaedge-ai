# CRM Guardian - Import Validator - 2026-06-08 - All clean (0 fresh imports in last 24h)

**Run summary:** 0 records scanned (0 fresh imports in the 24-hour createdate window), buckets 0 domain-corrected / 0 renamed / 0 flagged / 0 held-new, 0 HubSpot writes, 0 validation errors, 1 canvas-write anomaly (Run-log row double-appended - see Errors).

**Trigger window (ET):** 2026-06-07 11:09 -> 2026-06-08 11:09 (run fired ~11:09 ET / 10:09 CT).
Filter: `createdate GTE now-24h` AND `last_enriched_date IS EMPTY` AND `customer_segment != "Flagged for deletion"` AND `hs_object_id != 124293230301`. Sort `createdate ASC`, cap 100.

**Zero-result verification (not a query artifact):**
- Trigger query returned `total: 0` with the ISO bound (`2026-06-07T15:09:06Z`) AND again with the epoch-millis bound (`1780844946000`) - consistent across both formats.
- Widened to a 7-day window (`createdate GTE 1780326546000`): 53 un-enriched companies exist, but the newest is dated `2026-06-05T20:27Z` (Friday's bulk import batch). All 53 predate the 24-hour window, so they are out of R0 scope and owned by R1 Fresh Enrichment's blank-segment backlog.
- Conclusion: genuinely no companies were created in the last 24 hours. Clean zero-candidate run.

## What needs Cooper's attention

- **6 carried R0 Tier 3 holds remain on ledger `F0B0AFSB9LN`** (none resolved by Cooper since the prior run; each re-checked against current HubSpot this run - all 6 still active with blank `customer_segment`, blank `last_enriched_date`, no `flagged_for_deletion_reason`):
  - **4 duplicate-routed (awaiting R3 dedup merge):** indatelservices.com (326184182509), teampoka.com (325800222448), g.softbank.co.jp (325335795443), us.ntt.net (325335796410). No R0 action available - R3 owns the merge.
  - **2 genuinely ambiguous (awaiting Cooper adjudication):** gatco.net (324524875475, pending since 2026-05-27 - GATCO Bathware / GATCO Global UK / GATS Telecom diverge, India-registered) and columbus-networks / finetechnologies.co (324597786339, pending since 2026-05-26 - MISDOMAIN vs RENAMABLE unresolved: name suggests Columbus Networks/Liberty Networks, domain serves an unrelated FL MSP). Both are AMBIGUOUS by classification, so R0 cannot auto-resolve without risking a bad write; surfaced for Cooper.
- No new hard-flags, no new domain corrections, no new renames this run.

## Run health: YELLOW

- Validation work itself was clean: 0 candidates, 0 validation errors, all HubSpot reads succeeded, 0 HubSpot writes required.
- YELLOW because (a) a canvas Run-log row double-appended on a timed-out `slack_update_canvas` write (cosmetic, documented in Errors, deliberately not retried), and (b) 6 carried R0 Tier 3 holds remain on the ledger.

## Errors

**Canvas Run-log double-append (cosmetic, documented, not retried).** The `slack_update_canvas` append to `F0B0AFSB9LN` timed out after 180s, but the write still landed - and landed TWICE. Verified: the row `2026-06-08 11:09 ET | CRM Guardian - Import Validator` appears 2x in the canvas (grep, only-matching), and the file grew ~835 chars (= two copies of a ~360-char row). The 180s timeout triggered an internal connector retry that applied the append twice. I did NOT issue another canvas write: every canvas write is currently timing out and double-applying, and the duplicate is a table ROW (no individual section_id), so deduping would require replacing the entire Run-log table element - which risks losing cross-routine run-log history. Conservative call: leave one duplicate row, document here. Cooper can delete the extra row manually.

**Root cause - canvas bloat (fleet-wide, recommend rotation).** `F0B0AFSB9LN` is now ~851K chars - it was ~356K on 2026-06-04, so it has more than doubled in 4 days. At this size, canvas writes exceed the 180s timeout and the connector auto-retry double-applies. This exposes EVERY routine that appends a Run-log row, not just R0. Recommendation: rotate/archive the ledger canvas - stand up a fresh F-canvas, carry over the open Tier 3 items + a short run-log tail, archive the old one.

**Canvas read.** Succeeded both times but exceeded the in-context token limit (~851K chars); R0 sections + Run-log tail were extracted via offline slicing. Not a failure.

## Per-bucket tables

**Domain Corrections (this run):** none
**Renames (this run):** none
**Hard-flagged (this run):** none
**Tier 3 - new this run:** none

**Tier 3 - carried, unchanged (ledger drain detail):**

```
| ID            | Domain                         | Ledger date | Disposition                          | Current HubSpot state          |
|---------------|--------------------------------|-------------|--------------------------------------|--------------------------------|
| 326184182509  | indatelservices.com            | 2026-06-05  | Dup of INDATEL (indatel.com) -> R3   | active, no segment, no enrich  |
| 325800222448  | teampoka.com                   | 2026-06-04  | Dup of Poka Lambro Telecom -> R3     | active, no segment, no enrich  |
| 325335795443  | g.softbank.co.jp               | 2026-06-02  | SoftBank mail subdomain dup -> R3    | active, no segment, no enrich  |
| 325335796410  | us.ntt.net                     | 2026-06-02  | NTT backbone subdomain dup -> R3     | active, no segment, no enrich  |
| 324524875475  | gatco.net                      | 2026-05-27  | AMBIGUOUS -> Cooper                  | active, no segment, no enrich  |
| 324597786339  | columbus-networks/finetech.co  | 2026-05-27  | AMBIGUOUS (MISDOMAIN vs RENAME)      | active, no segment, no enrich  |
```

## Delivery

Quiet on success per the Delivery rule - no Slack DM sent. Record of run = this report + the ✅ Run-log row appended to canvas `F0B0AFSB9LN`. CRM Ops Daily Digest (4:45 PM CT) surfaces this run.
