CRM Guardian - Flagged Consolidation - 2026-06-05 - 0 contacts flagged, 0 reassociated, 1 Tier 3 held

Run summary: 218 flagged companies in pool (cap 150/run; no contact writes required, full un-flagged population evaluated in one sweep) · 89 un-flagged contacts evaluated · 0 Tier 1 Mode B flags / 0 Tier 1-2 reassociations / 1 Tier 3 hold · 0 HubSpot writes this run

Run fired 2026-06-05 ~12:07 PM CT (R4 daily window). HubSpot is source of truth. No Apollo, no web. Quiet-on-success: no DM sent (no hard failure).

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs stale associations from reassociated contacts)

The 218-company Flagged-for-deletion pool and the standing flagged-contact queue (flagged_for_deletion = true, set on prior R4 runs) remain ready for Cooper's manual bulk-delete / archive. This run added nothing to the flag queue because every un-flagged contact still on a flagged company carries a live preservation signal.

- 1 Tier 3 hold this run (open-deal block; likely upstream mis-flag). See table below.

Run health: YELLOW
- Writes attempted: 0; all evaluations succeeded; 1 Tier 3 hold present; 0 errors.

Errors: None

---

## How the pool resolved

Backlog has drained from the 379-company first-run baseline to 218 active flagged companies. Of those, the un-flagged contact population (contacts on a flagged company NOT already carrying flagged_for_deletion = true) is only 89 records. The dead contacts were flagged by prior R4 runs; the 89 survivors are exactly the records that keep preserving.

6-signal preservation result for all 89: every contact fired at least one preservation signal -
- Signal 1/2 (notes_last_contacted / notes_last_updated within 90 days, ET cutoff 2026-03-07): fired for all 89. These are recently sourced/enriched 2026 lead contacts with current activity timestamps.
- Signal 5 (lifecyclestage in {customer, opportunity, subscriber}): 1 contact at `opportunity` (Anthony Salamoni), 1 at `other`, remainder `lead`.
- Signal 6 (createdate within 14 days, ET cutoff 2026-05-22): ~30 contacts created 2026-05-26 onward (recent sourcing) - fresh-record safety preserves these regardless.

Result: 0 contacts eligible for Mode B flagging. No contact reached the not-preserved state.

Mode A reassociation: 0 this run. The flagged companies holding these preserved contacts are unique non-ICP / defunct-carrier / out-of-scope records (residential cable brands, defunct acquired carriers, industrial distributors, professional-services firms, international wholesale telecoms), not duplicates of an active ICP primary. No HIGH-confidence exact domain/name match to a non-flagged ICP company was identified, so no preserved contact had a reassociation target. Preserved contacts remain associated with their current (flagged) company - they will be cleaned up when Cooper archives the company, or re-evaluated if the company is reclassified back to an active segment.

Invariant checks:
- C (closed-won customer protection): no `customer` lifecyclestage among the 89; no closed-won contact surfaced. Clean.
- C-bis (pre-2026-05-11 Enterprise mis-flag backfill): not triggered - flagged companies in this population were flagged after the 2026-05-11 Enterprise ICP promotion (recent createdates), so the one-time backfill window does not apply. Note for Cooper: a few non-ICP-by-design records sit in the pool (Allegion, Wurth Industry North America, McGough, Latham & Watkins, Currency.com) - these are security-hardware / industrial-distribution / construction / legal / crypto entities, correctly outside the 4 Enterprise sub-segments. No action.
- D (open-deal hard stop): 1 company caught - Fast Wave (see Tier 3 below).
- E (fresh-record safety, createdate < 14 days): the ~30 newest contacts are preserved by this rule as well as by signal 1/2; no premature judgments made.

---

## Tier 3 held (1)

```
| Company | Company ID | Contact | Contact ID | Reason | Recommendation |
|---|---|---|---|---|---|
| Fast Wave | 323666965217 | Anthony Salamoni (opportunity) | 489067118326 | Open deal hard stop (Invariant D). Associated open deal "Broadstar - New Logo" - $10,000 USD, dealstage presentationscheduled, hs_is_closed = false, created 2026-06-02. Contact email anthonys@broadstar.com (domain mismatch vs flagged company fastwavenetworks.com - possible Broadstar/Fast Wave identity confusion upstream). | Do NOT consolidate. Active $10K opportunity = strong mis-flag signal. Recommend: remove customer_segment = "Flagged for deletion" from Fast Wave (323666965217), reclassify, and route to R1/R2. Resolve or re-home the deal/contact association. |
```

## Mode B flags (0)

```
None this run. No un-flagged contact reached the not-preserved state.
```

## Reassociations (0)

```
None this run. No HIGH-confidence ICP-primary duplicate identified for any preserved contact.
```

---

## Notes / carry-forward

- This was a complete (not cap-limited) evaluation of the un-flagged contact population - the full 89 were assessed in a single sweep, not a 150-company-capped partial. Steady state reached for contact flagging.
- The standing bulk-delete queue (contacts already at flagged_for_deletion = true) is unchanged by this run and remains Cooper's manual action.
- One Tier 3 item appended to canvas F0B0AFSB9LN this run: Fast Wave open-deal mis-flag.
