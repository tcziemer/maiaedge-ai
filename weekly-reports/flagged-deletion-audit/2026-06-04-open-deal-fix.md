# Flagged-for-Deletion + Open Deal Fix - 2026-06-04 (ad-hoc, requested by Cooper)

## Scope check

Cooper flagged that some companies have open deals while sitting in `customer_segment = "Flagged for deletion"`.

- Total flagged-for-deletion pool: **251 companies**
- `num_associated_deals > 0` company-side filter: returned only 1 (property under-populated / unreliable)
- Authoritative deal-side cross-object query (`SELECT ... FROM DEAL WHERE COMPANY.customer_segment = 'Flagged for deletion'`): **1 deal** -> **Broadstar - New Logo**

Both methods converge: **exactly one** flagged record currently has an associated deal. The framework hard stops (open deal at `contractsent`+ / closed-won customer protection) are otherwise holding across the other 250 flagged records. No hard-stop / customer-protection records to route.

## Record fixed

| Field | Before | After |
|---|---|---|
| company | Broadstar (323981908725, broadstar.com) | same |
| customer_segment | Flagged for deletion | **Fiber Operator** |
| company_sub_segment | (none) | **Regional CLEC - Fiber operator** |
| account_tier | (none) | **tier_2** (Regional CLEC default T3, open-deal -1) |
| signal_heat | (none) | **Hot** (open deal past appointmentscheduled) |
| flagged_for_deletion_reason | "Duplicate (merged): ... primary Gigabit Fiber ..." | "" (cleared on exit) |
| account_brief | "[R1 2026-05-22 TIER 3 HOLD - DUPLICATE...]" | rewritten, accurate, pure prose |
| last_enriched_date | null | null (left for R2 full pass) |

Deal: **Broadstar - New Logo**, $10,000, stage `presentationscheduled` (POC & Technical Validation), created 2026-06-02. Below `contractsent`, so segment write permitted (not a hard stop).

## Why the flag was wrong

The record was flagged as a duplicate of Gigabit Fiber (company 193867595510, gigabitfiber.com) back when its domain pointed at gigabitfiber.com (a data-entry error). The domain has since been corrected to **broadstar.com**, which is a genuinely separate entity: a national MDU fiber-to-the-home provider (apartments, HOAs, condos, senior care, student housing), West Palm Beach FL, founded 1994, recently upgraded to 10G with IP Infusion OcNOS disaggregated switching. Gigabit Fiber remains a live, distinct ICP record. Broadstar passes D1 (operates real fiber infrastructure) and has an active POC, so it belongs in the active pool, not the delete queue.

## Open follow-up

The stale dedup earlier reassociated some of Broadstar's contacts to Gigabit Fiber. Broadstar now shows 2 associated contacts. Worth verifying whether any contacts moved to Gigabit Fiber should be returned to Broadstar. Not auto-reversed (requires knowing which contacts; low risk to defer).

## Recommendation (recurring safeguard)

No scheduled task currently auto-catches "flagged-for-deletion + has open deal." Options:
1. Add a guardrail check to R4 Flagged Consolidation (daily 12pm) that surfaces any flagged record with an open/closed-won deal as KEEP_AND_RECLASSIFY.
2. Add the same one-line check to the CRM Ops Daily Digest (read-only surface to Cooper).
3. Stand up a small dedicated daily scheduled task mirroring this fix (auto-reclassify safe ones, route hard-stops).

Given the live scope is currently 1 record and the hard stops are holding, option 1 or 2 (lightweight surface inside an existing routine) is the proportionate fix. Pending Cooper's direction - not built without sign-off.
