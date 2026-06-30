---
name: pre-deletion-audit
description: "MaiaEdge CRM pre-deletion audit and contact consolidation. Before any company is marked `customer_segment = \"Flagged for deletion\"`, this skill gates the decision through a duplicate check, an open-deal check, and a per-contact activity check so active relationships and ICP records are never lost. When the flagged company is a duplicate of a real ICP company, the skill reassociates salvageable contacts to the primary company and flags the duplicate. When the company is a genuine non-fit, it flags contacts for deletion only if they have no activity in the last 90 days and no association to an open deal. Always operates under the CRM Guardian three-tier safety system. Writes directly to HubSpot via MCP, logs every change as a note on the affected record, and produces a per-run audit report. Use when asked to run pre-deletion audit, flag non-ICP accounts, consolidate duplicate contacts, or process accounts proposed for deletion."
---

# MaiaEdge Pre-Deletion Audit

## Purpose

Before any company gets `customer_segment = "Flagged for deletion"` written to HubSpot, this skill runs a gated audit that prevents three specific failure modes:

1. **Deleting a duplicate** when the contacts on it are the only link to an active relationship.
2. **Orphaning active contacts** - anyone with `notes_last_contacted` in the last 90 days or an association to an open deal must be preserved.
3. **Losing ICP reach** - if the flagged record is actually a duplicate of a real ICP company we already have, its contacts should land on the primary, not disappear.

This skill is the single choke point through which every "mark this non-fit for deletion" decision must pass, whether the decision comes from segment-classification, a CRM Guardian job, or a human request.

## Reference Files

- `context/hubspot/property-schema.md` - company property reference, `customer_segment` values, `flagged_for_deletion_reason` 7-code canonical set (§2.1)
- `context/hubspot/contact-schema.md` - contact property reference, `flagged_for_deletion` boolean, activity fields
- `context/hubspot/hubspot-values.md` - enum value mapping
- `context/hubspot/territory-model.md` - owner mapping (used in notes for traceability)
- `context/hubspot/poc-schema.md` - POC pipeline stages; required to evaluate whether a contact is on an active POC (Preservation Rules, activity signals)
- `context/core/segment-qualification.md` - ICP definition (what counts as in/out)
- `context/core/icp-playbook.md` - ICP boundaries for segment re-evaluation
- `context/segments/enterprise.md` - Enterprise ICP hard scale gate (Step 0 Enterprise defensive check; $1B+ / multi-DC / Equinix Fabric criteria)

## ICP Segments (in scope) - 6 segments as of 2026-05-11

A company is **in ICP** if `customer_segment` is one of:

- `Data Center Colo Provider`
- `Fiber Operator`
- `Network Operator(Tier 1 / VNO)`
- `MSP/Aggregator`
- `NeoCloud`
- `Enterprise-CustomerSegment` - **promoted to ICP 2026-05-11** (Multi-DC enterprises in Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services that pass the hard scale gate per `context/segments/enterprise.md`. Anchor account: Meijer.)

All other values (`Partner Target`, `Other`, `Unknown`) are out of ICP for the purposes of this skill and eligible for flagging. `Flagged for deletion` is terminal - the skill never re-enters the pipeline on these unless a human explicitly requests re-evaluation.

### Critical Pre-Phase-1 Enterprise Defensive Check (added 2026-05-11)

**This skill MUST NOT auto-delete records previously tagged `customer_segment = "Enterprise-CustomerSegment"` under the old non-ICP framing without first re-running segment-classification's Enterprise scale gate.**

Pre-2026-05-11, Enterprise was a non-ICP catch-all and many records carrying that segment value have been quietly accumulating in HubSpot. Some of them are now in-ICP under the new framing (Meijer-class multi-DC enterprises). The risk: this skill's prior version treated Enterprise-CustomerSegment as out-of-ICP and would have eligibility-flagged Meijer-style records for deletion.

**Defensive workflow at Step 0 (before the existing hard stops in Step 1):**

If the candidate company has `customer_segment = "Enterprise-CustomerSegment"`:

1. **DO NOT proceed to Step 1 (hard stops) or Step 2 (dedup primary search) yet.**
2. Check `account_brief` for evidence of new-framing classification: mentions of one of the four Enterprise sub-segments + scale evidence (mention of $1B+ rev, multi-DC, Equinix Fabric/Megaport, in-house net eng) + post-2026-05-11 timestamp on the brief regeneration. If ALL three are present → treat as ICP, exit this defensive workflow, return to Step 1.
3. Otherwise (brief is pre-2026-05-11 OR doesn't show new-framing evidence), surface as **TIER 3 - Pre-Phase-1 Enterprise re-classification needed**. Do NOT proceed to flag. Add to run report:
   - `Pre-Phase-1 Enterprise candidate: [company name]. Brief written before 2026-05-11 ICP promotion. Recommend: route to R2 RE_ENRICH_FULL for scale-gate verification before any flag-for-deletion decision.`
4. Skip the rest of the skill's workflow for this candidate. Cooper validates in HubSpot UI; if the scale gate fails, R2 will reclassify to `Other` Tier 5 (a Tier 2 segment downgrade, NOT a flag-for-deletion eviction - the data is real, the prior framing was wrong).

**Why this matters:** the Meijer anchor account has `customer_segment = "Enterprise-CustomerSegment"`. If this skill ran before the Phase 5 update with old logic, Meijer would have been eligible for `flagged_for_deletion`. The defensive check above prevents that catastrophic data-loss scenario across the entire pre-promotion Enterprise tag base.

## Preservation Rules

A contact is **preserved** (never receives `flagged_for_deletion = true`, never reassociated-and-flagged as a duplicate) if ANY of the following is true. These are belt-and-suspenders  -  any single rule fires → preserve.

### Activity signals

- `notes_last_contacted` is within the last 90 days (from today's date)
- `notes_last_updated` is within the last 90 days
- The contact is associated to any **deal** where `dealstage` is NOT `closedwon` and NOT `closedlost`
- The contact is associated to any **POC ticket** (HubSpot ticket in the POC pipeline  -  see `context/hubspot/poc-schema.md`) where the ticket's `hs_pipeline_stage` is NOT a closed/terminal stage. Active POCs are critical engagement signals and override every other rule except strategic exception.

### Identity signals

- `lifecyclestage` is `customer`, `opportunity`, or `subscriber`. Customers are existing revenue relationships and opportunity-stage contacts are in an active sales motion - never flag regardless of activity recency. Subscribers have opted in and retain communication rights; do not flag. (Note: HubSpot's contact lifecyclestage enum in this instance does NOT include `evangelist` - valid values are `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `other`.)
- Company this contact is associated to has any deal with `hs_is_closed_won = true`. Customer-status overrides company segment in the ICP check.

### New-record grace period

- Contact `createdate` within the last 14 days. A contact created this week can't reasonably have 90-day activity history  -  don't flag for absence of history until the record has had time to accumulate it. The audit will pick these up naturally on future runs once they age past 14 days.
- Company `createdate` within the last 14 days. Same logic at the company level. A company created this week shouldn't be pre-deletion-audited at all; skip the candidate.

### Strategic exception

- Any record with a HubSpot note containing `strategic exception` or `leadership assigned`. Escalate to Tier 3 report and skip.

**Implementation note:** When pulling contact or company data in Step 0, include these fields in the `get_object` call so the preservation rules can be evaluated without additional round-trips: `lifecyclestage`, `createdate`, `notes_last_contacted`, `notes_last_updated`, and association counts for deals + POC tickets.

## Safety Tier Mapping

This skill respects the CRM Guardian three-tier system defined in `skills/crm-guardian/SKILL.md`.

### TIER 1 - AUTO-FIX
- Sync contact `customer_segment` from primary company after reassociation
- Set contact `hubspot_owner_id` to match primary company owner after reassociation
- Set `flagged_for_deletion = true` on contacts with zero activity AND zero open-deal associations on a non-ICP company with no primary duplicate candidate
- Set `customer_segment = "Flagged for deletion"` on a company once all its contacts have been resolved (reassociated, preserved-and-left, or flagged). In the SAME write, set `flagged_for_deletion_reason` (multi-line text) leading with the matching canonical reason code + colon + one evidence sentence (no em dashes): `Duplicate (merged)` on the Mode A path (cite the primary name + record ID), `No ICP fit` on the Mode B all-contacts-flagged non-fit path. See "`flagged_for_deletion_reason` companion write" below for the full code list.

### TIER 2 - AUTO-FIX WITH FLAG
- Reassociating contacts from a duplicate company to the primary ICP company (only when domain match is HIGH confidence - exact domain match or normalized-name exact match)
- Any contact reassociation produces a flagged entry in the run report for Cooper's review

### TIER 3 - HUMAN REVIEW ONLY
- Any company with open deals - skip entirely, do not flag, do not touch contacts
- Any company where the dedup primary candidate is MEDIUM or LOW confidence (fuzzy name match without domain match) - produce a suggested merge for review
- Non-ICP companies with preserved active contacts AND no primary to reassociate to - flag the company cannot proceed; hand to Cooper to decide whether to keep the company or orphan the contacts
- Any contact with association to an open deal - never flag, even if company is being flagged
- Actual archive/delete of any record - the skill only writes `flagged_for_deletion` and `customer_segment`; humans finalize archival

## Workflow

### Step 0: Resolve the candidate

Input: one or more company records proposed for flagging. Source can be:
- crm-guardian Job 7 (scheduled pass over current/proposed non-ICP accounts)
- segment-classification output where verdict is `EXCLUDE`
- Direct human request

For each candidate company, pull these properties via HubSpot MCP `get_object`:
```
name, domain, website, customer_segment, flagged_for_deletion_reason, account_tier, hubspot_owner_id,
state, country, createdate, notes_last_contacted, last_enriched_date,
segmentation_confidence
```

**Company-level grace period check:** If company `createdate` is within the last 14 days, skip this candidate entirely and log as "new record grace period  -  will re-evaluate after 14 days." Do not touch contacts on brand-new companies.

And pull associations (`get_associations`):
- All associated CONTACTs
- All associated DEALs
- All associated TICKETs (specifically POC pipeline tickets  -  used in preservation rules)

When pulling each contact (before the activity check in Mode A or B), include: `firstname, lastname, email, jobtitle, phone, hubspot_owner_id, customer_segment, lifecyclestage, createdate, notes_last_contacted, notes_last_updated, hs_email_optout`. Include association counts for deals + tickets.

### Step 1: Hard stops (must pass all three)

**1a. Customer-history hard stop.** If the company has ANY deal with `hs_is_closed_won = true` or `dealstage = closedwon` - active customer or historical customer - skip this candidate entirely. Customers (past or present) are NEVER flagged for deletion, regardless of current segment classification, activity, or any other signal. If the company was briefly reclassified as non-ICP by a recent enrichment pass, the human should decide, not the routine. Add to run report as TIER 3 with reason "Customer-history protection - company has closed-won deal(s); never auto-flag."

**1b. Open-deal hard stop.** If the company has any deal where BOTH `hs_is_closed_won = false` AND `hs_is_closed_lost = false` (i.e. open):
- Do NOT flag. Do NOT touch contacts. Do NOT proceed past this step for this candidate.
- Add to run report as TIER 3: `company_id, name, open_deal_count, owner` with reason "Open deals present - pre-deletion audit skipped. Deal protection rule."
- Move to next candidate.

**Implementation note:** HubSpot's deal pipeline uses BOTH string keys (`closedwon`, `closedlost`) AND custom numeric stage IDs (e.g. `3401264867` = "Closed Won" in the MaiaEdge custom pipeline). Do NOT filter on `dealstage IN/NOT_IN (closedwon, closedlost)` - numeric closed stages would be missed. Always use the `hs_is_closed_won` + `hs_is_closed_lost` booleans to determine deal status deterministically.

**1c. Strategic-exception hard stop.** If the company has ANY HubSpot note authored by a human (not `[CRM Guardian]`) containing the phrases `strategic exception`, `leadership assigned`, or `do not modify` - skip entirely. Tier 3 report with the note content so Cooper can re-evaluate.

### Step 2: Dedup primary search

Search HubSpot for a potential ICP primary that this candidate may be a duplicate of. Use `search_crm_objects` on COMPANY with these cascading filters:

1. **Domain match (HIGH confidence):** Exact match on `domain` (normalized: strip `www.`, lowercase, drop trailing slash). Primary candidate's `customer_segment` must be in ICP.
2. **Normalized name match (HIGH confidence):** Exact match on `name` after normalization (lowercase, strip `Inc.`, `LLC`, `Ltd`, `Corp`, trailing commas/periods, extra whitespace). Primary's segment must be in ICP.
3. **Fuzzy name match (MEDIUM confidence):** Levenshtein-style similarity ≥ 0.9 on normalized names with same country/state. Primary's segment in ICP.

Decision tree:
- Multiple HIGH confidence candidates → pick the one with the **most recent** `notes_last_contacted` as primary; log the rest for Cooper.
- One HIGH confidence candidate → that is the primary. Proceed to Mode A.
- Only MEDIUM confidence candidate(s) → produce a merge suggestion (TIER 3), do not auto-reassociate. Skip remaining steps for this candidate.
- No candidate → Proceed to Mode B.

### Step 3 - Mode A: Consolidate to ICP primary

For each associated contact on the duplicate company:

1. **Activity check** (see "Preservation Rules" section).
   - If activity present: mark as PRESERVE_AND_REASSOCIATE.
   - If no activity: mark as REASSOCIATE_OR_FLAG (see below).
2. **Dedup check against primary:** Does the primary already have a contact with the same `email` (case-insensitive) OR same `firstname + lastname + company`?
   - If YES: the duplicate contact is itself a dup of a primary contact.
     - If PRESERVE_AND_REASSOCIATE: set `flagged_for_deletion = true` on the duplicate contact; the primary's version wins. Surface both contact IDs (primary + flagged duplicate) in the daily email report so the activity-history linkage is discoverable. (TIER 1)
     - If REASSOCIATE_OR_FLAG: set `flagged_for_deletion = true` on the duplicate contact. (TIER 1)
   - If NO: reassociate the contact to the primary company (add association, then remove association to the duplicate). After reassociation: sync `customer_segment` and `hubspot_owner_id` from primary (TIER 1). The reassociation itself is TIER 2.

After all contacts are processed:
3. Set the duplicate company `customer_segment = "Flagged for deletion"` (TIER 1 - once contacts are resolved, the duplicate can safely be flagged). In the SAME write, set `flagged_for_deletion_reason = "Duplicate (merged): [primary company name] (ID [primary record ID]); contacts reassociated to primary."` (no em dashes - use a colon).
4. Surface the consolidation in the daily email report: duplicate company ID + primary company ID + counts of contacts reassociated, contacts flagged as dups, final state of duplicate company. No HubSpot note is created on either company - the daily report is the audit trail.

### Step 3 - Mode B: Standalone flag (no primary found)

For each associated contact:

1. **Activity check:**
   - If activity present: mark as PRESERVE_ON_COMPANY. Do NOT set `flagged_for_deletion`. Do NOT reassociate - there is no primary. The contact remains attached to the company.
   - If no activity: mark as FLAG. Set `flagged_for_deletion = true` (TIER 1).
2. **Post-loop decision for the company:**
   - If ALL contacts were FLAG (zero preserved): set company `customer_segment = "Flagged for deletion"` (TIER 1). Safe to flag - nothing active on it. In the SAME write, set `flagged_for_deletion_reason = "No ICP fit: [one sentence on why this standalone non-fit company has no ICP value]"` (no em dashes - use a colon).
   - If ANY contacts were PRESERVE_ON_COMPANY: **DO NOT flag the company.** Add to TIER 3 report: "Non-ICP company with N active contacts, no ICP primary identified for reassociation. Decide: keep company, orphan contacts (requires a landing page), or re-evaluate segment." Include the list of preserved contacts and their last activity dates.

### Step 4: Report (no HubSpot notes)

**Do not create HubSpot notes on any record.** Per CRM Guardian convention, the routine never writes per-record notes - they create noise in rep activity feeds, and the current state of the fields (`flagged_for_deletion`, `customer_segment`, association presence) plus the daily email report is a sufficient audit trail.

Every field change, reassociation, and flag action must appear in the Step 5 run report with record IDs, old/new values, and the gate that fired.

### Step 5: Run report

Produce a per-run summary matching the CRM Guardian report schema:

```
PRE-DELETION AUDIT REPORT - [Date] [Time]
==========================================
Candidates processed: [N]
  Open-deal skips (TIER 3): [N]
  Mode A consolidations: [N]
  Mode B standalone flags: [N]
  Held for review (TIER 3): [N]

MODE A - CONSOLIDATIONS (applied, Tier 2 review):
| Duplicate | Primary | Contacts Reassociated | Contacts Flagged (dup) | Duplicate Company Flagged | flagged_for_deletion_reason |
|-----------|---------|-----------------------|------------------------|---------------------------|-----------------------------|

MODE B - STANDALONE FLAGS (applied, Tier 1):
| Company | Owner | Contacts Flagged | Contacts Preserved | Company Flagged? | flagged_for_deletion_reason |
|---------|-------|------------------|--------------------|--------------------|-----------------------------|

TIER 3 - HELD FOR REVIEW:
| Company | Reason | Suggested Action |
|---------|--------|------------------|

SAFETY: [any errors, skipped candidates, API failures]
```

**Surface the reason code for auditability.** This skill audits the deletion pool, so its report MUST surface `flagged_for_deletion_reason` for every company it flags (the `flagged_for_deletion_reason` columns above). This lets Cooper audit the flagged-for-deletion pile by reason code (e.g. "show me every `Duplicate (merged)` from this run" or "review all `No ICP fit` flags") before bulk-archival. When the input batch includes companies already carrying `Flagged for deletion` from a prior run, read and echo their existing `flagged_for_deletion_reason` in the report so the full pool is reason-tagged.

## Edge Cases

- **Contact with activity on a duplicate, same contact already exists on primary with stale data:** Preserve the richer record (more fields populated). If the primary version is stale but is the surviving record, surface the duplicate's `notes_last_contacted` value in the daily email report alongside both contact IDs so the linkage is traceable; then flag the duplicate contact. Do not overwrite primary's email/name.
- **Company flagged for deletion but a contact on it becomes active later:** Not this skill's problem - this skill only runs at decision time. The scheduled re-run will catch it on the next pass if the company has not yet been archived.
- **Multiple candidate companies in the same batch are duplicates of each other:** Process them in order of `createdate` ascending (oldest first treated as primary if both non-ICP; if one is ICP it wins regardless of age).
- **Contact has `flagged_for_deletion = true` from a prior run but now has recent activity:** Clear the flag (set to `false`) as a TIER 1 auto-fix. Surface the flag clear in the daily email report with the activity signal that triggered it.
- **Contact has no email:** Dedup against primary by `firstname + lastname + jobtitle` instead of email.
- **Contact is associated to a company flagged for deletion but NOT in this batch:** Out of scope for this pass. A separate crm-hygiene orphan check handles those.

## MCP Requirements

- `search_crm_objects` - dedup lookups, activity queries
- `get_object` - read company + contact + deal details
- `get_associations` - pull contacts and deals for each company
- `manage_crm_objects` (updateRequest):
  - Write `customer_segment`, `flagged_for_deletion_reason`, `flagged_for_deletion`, `hubspot_owner_id` values
  - Create new associations (reassociate contact → primary company)

### `flagged_for_deletion_reason` companion write (REQUIRED)

Every time this skill sets a company `customer_segment = "Flagged for deletion"`, the SAME `updateRequest` MUST also set `flagged_for_deletion_reason` (multi-line text on the Company object). The value leads with ONE of the 7 canonical reason codes, then a colon and one concrete sentence of evidence. No em dashes - use a colon. The scannable code lives in this field; the prose rationale stays in `account_brief` (unchanged). Codes this skill emits:

- `Duplicate (merged)` - Mode A duplicate consolidation; cite the primary name + record ID.
- `No ICP fit` - Mode B standalone non-fit where all contacts flagged.

(The full 7-code set - `Dead domain`, `Hard junk / non-business`, `D1 disqualified (no reference value)`, `No ICP fit`, `Duplicate (merged)`, `Defunct / out of business`, `Stalled greenfield` - is owned by `context/hubspot/property-schema.md` §2.1; this skill only emits the two above.)

**Clear-on-exit:** if any path moves a company OFF `Flagged for deletion` back into an active segment (e.g. the Step 0 Enterprise defensive check reclassifies, or a contact reactivation reverses a prior flag), clear `flagged_for_deletion_reason` to empty in the same write.
- *(`create_note` is intentionally NOT used - per-record HubSpot notes create rep-feed noise; the daily email report is the audit trail.)*

Note: HubSpot MCP does not expose a native merge endpoint. Consolidation here means reassociate-and-flag, not atomic merge. Humans finalize archival of flagged records in Tier 3 review.

## Do NOT

- Never set `customer_segment = "Flagged for deletion"` on a company with open deals.
- Never set `flagged_for_deletion = true` on a contact with activity in the last 90 days.
- Never set `flagged_for_deletion = true` on a contact associated to any open deal.
- Never archive or delete records - the skill only writes flag fields. Archival is always human action.
- Never flag an ICP-segment company (re-evaluate the segment classification instead - that is segment-classification's job, not this skill's).
- Never auto-reassociate on MEDIUM or LOW confidence dedup matches.

## Skill Chain

- **Upstream triggers:** crm-guardian Job 7, segment-classification (Exclude verdict), human request
- **Writes to:** HubSpot companies, contacts (via MCP)
- **References:** crm-guardian (safety tier definitions, change log format), segment-classification (ICP boundary), crm-hygiene (duplicate detection methodology)
