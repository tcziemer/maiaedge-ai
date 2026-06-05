# Flagged-for-Deletion Audit (Cowork Manual-Trigger Task)

**Execution model:** Manual-trigger audit. Fire from inside the CRM Guardian Cowork project whenever Cooper wants to validate the `customer_segment = "Flagged for deletion"` pool before bulk-deleting records. Permanent reusable capability.
**Owner:** Cooper Kennedy (Slack DM: `U0A24D9RJLS`)
**Platform:** Cowork-only
**Apollo budget:** 0 (HubSpot reads only; no Apollo, no web fetching)
**Read/write profile:** READ-ONLY by default. Writes occur ONLY if `WRITE_BACK = "enabled"` and Cooper has approved the verdicts.
**First created:** 2026-05-18

---

## 1. Why this prompt exists

The "Flagged for deletion" customer_segment pool accumulates over time as routines (R1, R2, R4, R0) evict non-ICP records. Before Cooper manually deletes them in bulk from HubSpot, he wants to ensure:

1. **No records with associated deals get deleted.** Open deals, closed-won (customer) deals, even closed-lost deals carry context that shouldn't be lost.
2. **No records with attachments get deleted without review.** Contracts, MSAs, POCs, NDAs, signed documents - these are legal/audit material.
3. **No records with recent activity get deleted.** Last 90 days of emails, meetings, calls, or notes signals a relationship that needs human review.
4. **Duplicates of real ICP primaries are consolidated before deletion.** If a flagged record is a dupe of a live ICP record, its contacts should be reassociated to the primary first.
5. **The remaining pool is clean.** Once verdicts are applied, what's left is genuinely safe to bulk-delete - no surprises.

This audit is also the gate that runs BEFORE any Mass Re-Enrichment Sweep, so the re-enrichment runs on a clean active-ICP pool with no orphans or mis-flagged records.

---

## 2. Parameters

```
WRITE_BACK         = "disabled"   # default: audit only, no writes. Set to "enabled" once Cooper has approved verdicts to execute reclassification + consolidation actions.
ACTIVITY_WINDOW    = 90           # days back to count "recent activity"
CAP                = 0            # 0 = no cap, read all flagged records. Set to N to test on a subset.
ATTACHMENT_REVIEW  = "all"        # "all" = surface every record with any attachment. "important_only" = filter to contract / MSA / POC / NDA / legal keywords.
```

---

## 3. Required reading at run start

- `CLAUDE.md` — operating principles, customer protection rule, hard stops
- `skills/pre-deletion-audit/SKILL.md` — three-tier safety system, contact-consolidation policy, 90-day activity preservation
- `skills/crm-guardian/SKILL.md` — Non-ICP Eviction Rule reference
- `context/hubspot/property-schema.md` — `customer_segment` values, attachment schema, deal-association reads

---

## 4. Workflow

### Step 4.1 — Read the flagged pool

HubSpot `search_crm_objects` on COMPANY:

```
Filters (AND):
  customer_segment EQ "Flagged for deletion"
  company_id NEQ 124293230301

Sort: hs_lastmodifieddate DESC (most-recently-flagged first; helps spot recent errors)
Cap: CAP (0 = unlimited)
```

For each flagged record, pull:
- Identity: `name`, `domain`, `company_id`, `hs_lastmodifieddate`
- Classification audit: `customer_segment`, prior `customer_segment` (if findable in note history), `account_brief` (often contains eviction reason), `flagged_for_deletion_reason` (the scannable canonical reason code + evidence sentence set when the record was flagged — see `context/hubspot/property-schema.md` §2.1 for the 7-code spec)
- Owner: `hubspot_owner_id`
- Lifecycle: `last_enriched_date`, `createdate`, `notes_last_updated`
- Engagement counts: total notes, emails, meetings, calls in last `ACTIVITY_WINDOW` days
- Associated deals: ALL deals (open + closed-won + closed-lost), with `dealstage` + `closedate` + `amount` per deal
- Associated contacts: count + list of contact IDs
- Attachments: count + filenames + types

Pagination 100/page, ≥1s between pages.

### Step 4.2 — Per-record verdict logic

For each flagged record, apply this verdict tree:

#### Verdict A: KEEP_AND_RECLASSIFY (most-critical surface)

Trigger conditions (ANY of):
- Has any deal in `closedwon` stage (customer protection — record is a customer regardless of segment label)
- Has any deal in stages past `appointmentscheduled` and not in `closedlost` (active pipeline)
- Has recent activity (notes/emails/meetings/calls) in last `ACTIVITY_WINDOW` days from a rep, not from automation
- Has 5+ associated contacts (signals real relationship, even if segment was misclassified)

Action recommendation: Cooper reclassifies `customer_segment` back to the right ICP value (use `account_brief` + research to determine) BEFORE bulk-delete.

#### Verdict B: ATTACHMENT_REVIEW (manual gate)

Trigger conditions:
- Has any attachments AND `ATTACHMENT_REVIEW = "all"`
- Has attachments matching contract / MSA / POC / NDA / agreement / signed / legal / proposal keywords (case-insensitive) AND `ATTACHMENT_REVIEW = "important_only"`

Action recommendation: Cooper manually opens the record, downloads attachments if needed for legal/audit retention, THEN proceeds with verdict (could still be SAFE_TO_DELETE after attachment review).

#### Verdict C: CONSOLIDATE_AS_DUPLICATE

Trigger conditions:
- Fuzzy-match `name` OR `domain` against active-ICP records (`customer_segment` in the 6 ICPs). Use:
  - Normalized name match (lowercase, strip "Inc"/"LLC"/"Ltd"/spaces/punct)
  - Root domain match (strip subdomains, normalize `www.`)
  - HIGH-confidence match = exact normalized-name OR exact root-domain match against a live ICP record
- Has 1+ associated contacts (otherwise dedup gives no value)

Action recommendation: Treat as a duplicate of the matched ICP primary. Pre-deletion-audit workflow runs:
1. Reassociate all contacts from the flagged record to the ICP primary
2. Transfer any closed-lost deal history (notes) to the primary as a record-of-history note
3. Then bulk-delete is safe

If `WRITE_BACK = "enabled"`: execute the contact reassociation automatically per `skills/pre-deletion-audit/SKILL.md` workflow.

#### Verdict D: SAFE_TO_DELETE

Trigger condition (default verdict if no other trigger fires):
- No deals at all OR only `closedlost` deals
- No recent activity in last `ACTIVITY_WINDOW` days
- No attachments (or `ATTACHMENT_REVIEW = "important_only"` AND no important-keyword matches)
- No duplicate match against active ICP pool (or <5 contacts to consolidate)
- ≤4 associated contacts

Action recommendation: Bulk-delete via HubSpot UI. No prerequisites.

#### Verdict E: ANOMALY_INVESTIGATE (rare)

Trigger conditions:
- `account_brief` is empty AND record was flagged within last 30 days (suspicious — eviction routines normally write a `account_brief` reason)
- Has both closed-won deals AND last_enriched_date older than 365 days (very stale customer)
- Has notes from Cooper or a co-founder (`hubspot_owner_id` in `[Cooper, Abilash, Tim Z]`) within 30 days

Action recommendation: Manual eyeball before any other action. Routine eviction may have been wrong, or this is a customer that fell through the cracks.

### Step 4.3 — Compile verdicts table

Build a per-record verdict log:

| Verdict | Count | % of pool |
|---|---|---|
| KEEP_AND_RECLASSIFY | <count> | <%> |
| ATTACHMENT_REVIEW | <count> | <%> |
| CONSOLIDATE_AS_DUPLICATE | <count> | <%> |
| SAFE_TO_DELETE | <count> | <%> |
| ANOMALY_INVESTIGATE | <count> | <%> |

**Also build a reason-code distribution table** by grouping the pool on the leading canonical code in `flagged_for_deletion_reason` (parse the substring before the first colon). This lets Cooper bulk-delete by reason (e.g. clear all `Dead domain` and `Hard junk / non-business` rows in one sweep while holding `Duplicate (merged)` for consolidation review):

| Reason code | Count | % of pool |
|---|---|---|
| Dead domain | <count> | <%> |
| Hard junk / non-business | <count> | <%> |
| D1 disqualified (no reference value) | <count> | <%> |
| No ICP fit | <count> | <%> |
| Duplicate (merged) | <count> | <%> |
| Defunct / out of business | <count> | <%> |
| Stalled greenfield | <count> | <%> |
| (empty / no reason set) | <count> | <%> |

Surface records with an empty `flagged_for_deletion_reason` so Cooper can decide whether to backfill the reason or delete.

Per-record detail (in XLSX for Cooper):

| company_id | name | domain | last_enriched_date | flagged date (hs_lastmodifieddate) | flagged reason code | flagged reason detail | open deals | closed-won deals | closed-lost deals | contact count | attachment count | last activity date | account_brief excerpt | duplicate match (ICP primary) | verdict | action recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### Step 4.4 — Audit log + XLSX

Write:
- Markdown audit log: `weekly-reports/flagged-deletion-audit/YYYY-MM-DD-audit.md` with full verdict counts + per-record table
- XLSX file: `outputs/flagged-deletion-audit-YYYY-MM-DD.xlsx` for Cooper to filter and review (use the `xlsx` skill)

Present the XLSX via `mcp__cowork__present_files` so Cooper can open it directly from the Cowork chat.

### Step 4.5 — Write-back actions (only if WRITE_BACK = "enabled")

For each verdict, execute the corresponding action:

- **KEEP_AND_RECLASSIFY**: NO automatic write. Cooper handles manually after reviewing the suggestion (the record's correct segment is rarely deterministic from this audit's data). When Cooper reclassifies a record back into an active ICP segment, he must clear `flagged_for_deletion_reason` to empty in the same edit (clear-on-exit per `context/hubspot/property-schema.md` §2.1) — surface this reminder in the DM next-steps.
- **ATTACHMENT_REVIEW**: NO automatic write. Cooper handles manually.
- **CONSOLIDATE_AS_DUPLICATE**: 
  1. Reassociate contacts from flagged record to the ICP primary (per `skills/pre-deletion-audit/SKILL.md`)
  2. Add HubSpot note on the ICP primary documenting the consolidation: `"[Flagged-for-Deletion Audit] [YYYY-MM-DD]: Consolidated <N> contacts from duplicate company <flagged_company_id> (<flagged_name>) before bulk-delete."`
  3. Add HubSpot note on the flagged record: `"[Flagged-for-Deletion Audit] [YYYY-MM-DD]: Contacts reassociated to primary <icp_company_id> (<icp_name>). Record is now safe to bulk-delete."`
  4. On the flagged record, set/normalize `flagged_for_deletion_reason = "Duplicate (merged): contacts reassociated to primary <icp_name> (company <icp_company_id>); flagged loser."` in the same update — this overwrites any prior reason (the record is now confirmed a duplicate) and backfills the field if it was empty (legacy flag). Leading code `Duplicate (merged)`, colon, one evidence sentence, no em dashes. Spec: `context/hubspot/property-schema.md` §2.1. The record stays `customer_segment = "Flagged for deletion"` (no re-upgrade here, so no clear-on-exit).
  5. Tier 1 writes per `skills/crm-guardian/SKILL.md` safety system
- **SAFE_TO_DELETE**: NO automatic write. Cooper handles the bulk-delete manually via HubSpot UI (this prompt does NOT delete records).
- **ANOMALY_INVESTIGATE**: NO automatic write. Cooper handles manually.

If `WRITE_BACK = "disabled"` (default): skip Step 4.5 entirely. Audit is purely informational.

### Step 4.6 — Slack DM to Cooper

```
:mag: *Flagged-for-Deletion Audit* — YYYY-MM-DD

*Total flagged records reviewed:* <N>
*Write-back:* enabled / disabled

*Verdict distribution:*
  :white_check_mark: SAFE_TO_DELETE        — <count> (<%>) → safe to bulk-delete
  :warning: KEEP_AND_RECLASSIFY            — <count> (<%>) → reclassify before delete (open deals / closed-won / recent activity / 5+ contacts)
  :package: ATTACHMENT_REVIEW              — <count> (<%>) → manual review for legal/audit retention
  :twisted_rightwards_arrows: CONSOLIDATE  — <count> (<%>) → dupes of ICP primaries; contacts <reassociated automatically | need manual reassociation>
  :grey_question: ANOMALY_INVESTIGATE      — <count> (<%>) → manual eyeball

*Reason-code distribution (bulk-delete by reason):*
  Dead domain — <count>
  Hard junk / non-business — <count>
  D1 disqualified (no reference value) — <count>
  No ICP fit — <count>
  Duplicate (merged) — <count>
  Defunct / out of business — <count>
  Stalled greenfield — <count>
  (no reason set / legacy) — <count>

*Top 10 records by largest potential issue:*
1. <Company> — <verdict> — <reason>
2. ...

*Actions written (WRITE_BACK = enabled):*
  Contacts reassociated: <N>
  HubSpot notes added: <N>

*Next steps for Cooper:*
1. Open the XLSX and review the <reclassify> + <attachment_review> + <anomaly> rows individually
2. Reclassify the KEEP_AND_RECLASSIFY records back to the correct customer_segment — and clear `flagged_for_deletion_reason` to empty in the same edit (clear-on-exit)
3. Manually review attachment records, save anything important locally
4. Once verdicts B / E are resolved → bulk-delete in HubSpot via Filter Companies → customer_segment = "Flagged for deletion" (the reason-code distribution above lets you bulk-delete by reason — clear Dead domain / Hard junk / non-business / No ICP fit first)

*Full audit log:* weekly-reports/flagged-deletion-audit/YYYY-MM-DD-audit.md
*Spreadsheet:* outputs/flagged-deletion-audit-YYYY-MM-DD.xlsx
```

If `WRITE_BACK = "disabled"`, the "Actions written" section is omitted.

---

## 5. Safety + hard stops

- **No automatic deletes.** This prompt never deletes a HubSpot record. Bulk-delete is always Cooper's manual action via the HubSpot UI.
- **No automatic reclassification.** KEEP_AND_RECLASSIFY records get the suggestion but no write — Cooper reclassifies manually because the correct segment is rarely obvious from an audit-time read.
- **Contact reassociation only when CONSOLIDATE_AS_DUPLICATE has HIGH-confidence dupe match AND `WRITE_BACK = "enabled"`.** LOW/MEDIUM matches surface in DM for Cooper to review but don't auto-execute.
- **Hard stops:** MaiaEdge own (`company_id = 124293230301`). Records with closed-won deals (always route to KEEP_AND_RECLASSIFY, never SAFE_TO_DELETE).
- **HubSpot write batching:** 10 `objects` per `manage_crm_objects` call, ≥250ms between batches. `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

---

## 6. Failure handling

| Symptom | Action |
|---|---|
| HubSpot 429 / 5xx | Exponential backoff (1s, 2s, 5s). Continue with remaining records |
| Slack DM send fails | Retry 3× exponential backoff. If all fail, log to audit folder |
| XLSX generation fails (xlsx skill error) | Fall back to markdown-only audit. DM Cooper with note about missing spreadsheet |
| Fuzzy-match for duplicates returns >10 candidates for a single flagged record | Surface all candidates in DM for Cooper to pick the right primary; verdict downgrades to ANOMALY_INVESTIGATE |
| Record's `account_brief` references a now-active ICP segment | Likely flagged in error. Route to KEEP_AND_RECLASSIFY with high suggestion priority |

---

## 7. Recommended frequency

Fire this prompt:
- Before every Mass Re-Enrichment Sweep (to ensure the active-ICP pool is clean before the sweep starts)
- Quarterly as a standalone hygiene pass
- Whenever the flagged pool exceeds 500 records and bulk-delete is on Cooper's mind

Not a scheduled task — purely manual when Cooper needs it.

---

## 8. Coordination with other routines

- **R4 Flagged Consolidation (daily 12pm CT)** continues to handle ad-hoc new flaggings during the audit. R4 and this audit don't conflict.
- **R2 Stale Re-Enrichment** excludes flagged records from its trigger query, so no interference.
- **R3 Duplicate Accounts (Claude Code, 2am daily)** runs duplicate detection across the full CRM. This audit's CONSOLIDATE_AS_DUPLICATE verdict is a narrower flagged-record-only pass — R3 catches broader patterns.

---

**End of Flagged-for-Deletion Audit prompt.** Read-only by default. Audits the pool before bulk-delete and before any Mass Re-Enrichment Sweep.
