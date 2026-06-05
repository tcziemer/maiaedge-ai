---
name: crm-hygiene
description: "MaiaEdge CRM health checker and data quality auditor. Scans HubSpot for duplicates, missing fields, stale records, incomplete enrichment, deprecated enum values, contact-level mismatches, placeholder ownership, and junk contacts to flag for deletion. Use when asked to check CRM health, find duplicates, audit data quality, clean up HubSpot, find stale accounts, check data completeness, identify records missing key fields, audit contacts, or flag junk contacts. Also trigger on mentions of duplicates, missing data, data cleanup, stale accounts, CRM quality, contact mismatches, hard-bounced emails, spam/test contacts, or contact deletion flagging. Produces health score (0-100), duplicate detection, stale record reports, and contact-level hygiene findings."
---

# MaiaEdge CRM Hygiene Auditor

> **For autonomous CRM maintenance, use the crm-guardian skill instead.** This skill is for manual, on-demand audits of specific CRM health dimensions. CRM Guardian runs proactively and handles routine fixes (segment corrections, owner routing, stale enrichment) with its safety tier system.

## Purpose

Run comprehensive health checks on HubSpot company, contact, and deal records. Identifies data quality issues that degrade pipeline accuracy, cause routing errors, and waste rep time. Produces actionable reports with specific records to fix.

The goal is to catch problems before they compound  -  a missing state leads to wrong territory assignment, which leads to wrong rep, which leads to a cold email from the wrong person. Clean data is the foundation everything else runs on.

## Reference Files

For canonical HubSpot schema definitions, read these context files:
- **property-schema.md**  -  Company property definitions, valid values, territory model
- **hubspot-values.md**  -  Exact HubSpot enum values (case-sensitive)
- **contact-schema.md**  -  Contact-level properties, lifecycle, enrichment sync
- **deals-schema.md**  -  Deal pipeline stages, MEDDPICC fields, quote workflows
- **territory-model.md**  -  State-to-owner mapping, territory boundaries

---

## HubSpot Properties Reference

### Company Fields to Audit
```
name, domain, state, hs_state_code, country, city, hubspot_owner_id,
customer_segment, company_sub_segment, account_tier, segmentation_confidence,
phone, numberofemployees, annualrevenue, industry, founded_year,
notes_last_contacted, notes_last_updated, createdate, hs_lead_status,
last_enriched_date, infrastructure_profile, fabric_provisioning_approach,
geographic_focus, account_brief, maiaedge_value_proposition
```

### Contact Fields to Audit
```
firstname, lastname, email, jobtitle, phone, hubspot_owner_id,
customer_segment, company, notes_last_contacted, createdate, lifecyclestage
```

### Deal Fields to Audit
```
dealname, dealstage, amount, hubspot_owner_id, customer_segment,
closedate, createdate, pipeline, notes_last_contacted, num_associated_contacts
```

---

## Task Routing

### MODE 1: FULL CRM HEALTH CHECK
**Trigger:** "Run a health check" or "How's our CRM looking?" or "Audit data quality"

Run all of the checks below (Modes 2-11) in sequence and produce a consolidated health report. This is the "give me everything" mode.

**Output:**
```
CRM HEALTH REPORT  -  [Date]
============================

OVERALL HEALTH SCORE: [X]/100

SUMMARY
| Category | Issues Found | Severity |
|----------|-------------|----------|
| Duplicates | [N] likely duplicate pairs | High |
| Missing Critical Fields | [N] records | High |
| Deprecated Enum Values | [N] records | High |
| Cooper-Owned Accounts | [N] routeable / [N] unrouteable | High |
| Stale Records | [N] untouched 90+ days | Medium |
| Stale NEW Leads | [N] leads untouched 14+ days | Medium |
| Contact Mismatches | [N] owner / [N] segment | Medium |
| Incomplete Enrichment | [N] partially enriched | Medium |
| Contacts Flagged for Deletion | [N] Tier 1 / [N] Tier 2 | High |
| Data Completeness | [avg]% across all records | Varies |

TOP PRIORITY FIXES (do these first):
1. [Most impactful issue with count]
2. [Second most impactful]
3. [Third most impactful]

[Detailed sections from each mode follow]
```

Health score calculation:
- Start at 100
- -2 per duplicate pair
- -1 per record missing critical field (segment, state, owner, domain)
- -1 per deprecated enum value
- -1 per stale NEW lead (14+ days)
- -0.5 per stale record (90+ days no contact)
- -0.5 per contact owner mismatch
- -0.5 per record below 60% completeness
- Floor at 0

---

### MODE 2: DUPLICATE DETECTION
**Trigger:** "Find duplicates" or "Are there duplicate companies?" or "Dedupe our CRM"

**Steps:**

1. Pull all companies with: `name`, `domain`, `state`, `hubspot_owner_id`, `customer_segment`, `createdate`
2. **Domain-based duplicates**: Group by `domain`  -  any domain appearing 2+ times is a definite duplicate
3. **Name-based fuzzy matches**: Flag companies with very similar names (e.g., "Lambda Labs" vs "Lambda Labs Inc" vs "Lambda"). Look for:
   - Exact name matches (case-insensitive)
   - Name with/without common suffixes: Inc, LLC, Corp, Ltd, Co, Group, Holdings
   - Name with/without "The" prefix
4. Cross-check contacts for duplicate email domains
5. For each duplicate set, identify which record is the "primary" (most complete, most recent activity)

**Output:**
```
DUPLICATE DETECTION REPORT  -  [Date]
======================================

DOMAIN DUPLICATES (definite  -  same domain, different records)
| Domain | Record Count | Record IDs | Names | Recommended Primary |
|--------|-------------|------------|-------|-------------------|

NAME SIMILARITY MATCHES (likely  -  review needed)
| Group | Names | Domains | Confidence |
|-------|-------|---------|------------|

SUMMARY: [N] definite duplicates, [N] likely matches
```

**When running under CRM Guardian:** All duplicates are Tier 3 (never auto-merge). Report only.

---

### MODE 3: MISSING CRITICAL FIELDS
**Trigger:** "Check for missing fields" or "What records are incomplete?" or "Missing segments"

**Steps:**

1. Pull all companies with critical fields: `customer_segment`, `state`, `hubspot_owner_id`, `domain`
2. Flag any record where one or more critical fields are blank
3. Categorize by which field is missing
4. Prioritize: missing segment > missing owner > missing state > missing domain

**Output:**
```
MISSING CRITICAL FIELDS REPORT  -  [Date]
=========================================

| Company | Domain | Missing Fields | Impact |
|---------|--------|----------------|--------|

SUMMARY BY FIELD:
| Field | Missing Count | % of CRM |
|-------|--------------|----------|
| customer_segment | [N] | [X]% |
| hubspot_owner_id | [N] | [X]% |
| state | [N] | [X]% |
| domain | [N] | [X]% |
```

**When running under CRM Guardian:** Missing segment → enrich (Tier 1 if HIGH confidence). Missing owner with known state → Tier 1 auto-fix. Missing state → research (Tier 1 if found). Missing domain → Tier 3.

---

### MODE 4: STALE RECORD IDENTIFICATION
**Trigger:** "Find stale records" or "Untouched accounts" or "Dead records"

**Steps:**

1. Pull all companies with: `notes_last_contacted`, `notes_last_updated`, `createdate`, `hubspot_owner_id`, `customer_segment`
2. Flag records where `notes_last_contacted` is blank OR older than 90 days
3. Exclude Closed Won accounts (active customers)
4. Sort by days since last contact, descending
5. Group by owner for accountability

**Output:**
```
STALE RECORDS REPORT  -  [Date]
===============================

STALE ACCOUNTS (90+ days no contact)
| Company | Owner | Segment | Days Since Contact | Last Activity |
|---------|-------|---------|--------------------|---------------|

BY OWNER:
| Owner | Stale Count | % of Their Accounts |
|-------|-------------|---------------------|

SUMMARY: [N] stale records out of [N] total ([X]%)
```

**When running under CRM Guardian:** Report only  -  no action, no tier downgrade.

---

### MODE 5: INCOMPLETE ENRICHMENT TRACKING
**Trigger:** "Check enrichment status" or "Which accounts need enrichment?" or "Incomplete enrichment"

**Steps:**

1. Pull all companies with enrichment fields: `customer_segment`, `company_sub_segment`, `account_tier`, `segmentation_confidence`, `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`, `account_brief`, `maiaedge_value_proposition`, `last_enriched_date`
2. For records WITH a `customer_segment` (already classified), check which enrichment fields are blank
3. Flag records where `last_enriched_date` is blank (never enriched) or 120+ days old (stale enrichment)
4. Score enrichment completeness: count of populated enrichment fields / total enrichment fields

**Output:**
```
ENRICHMENT STATUS REPORT  -  [Date]
====================================

NEVER ENRICHED (has segment but no last_enriched_date)
| Company | Segment | Missing Fields |
|---------|---------|----------------|

STALE ENRICHMENT (last_enriched_date 120+ days ago)
| Company | Segment | Last Enriched | Days Since |
|---------|---------|---------------|------------|

PARTIALLY ENRICHED (classified but missing key fields)
| Company | Segment | Completeness | Missing Fields |
|---------|---------|-------------|----------------|

SUMMARY: [N] never enriched, [N] stale (120+ days), [N] partially enriched
```

**When running under CRM Guardian:** Stale enrichment feeds into Job 2 (re-enrichment). Partial enrichment feeds into Job 1 gap filling.

---

### MODE 6: DATA COMPLETENESS ANALYSIS
**Trigger:** "Data completeness" or "How complete is our data?" or "Field fill rates"

**Steps:**

1. Pull all companies with all auditable fields
2. Calculate fill rate per field across all records
3. Calculate average completeness per record
4. Flag records below 60% completeness
5. Identify the most commonly empty fields

**Output:**
```
DATA COMPLETENESS REPORT  -  [Date]
====================================

FIELD FILL RATES
| Field | Populated | Total | Fill Rate |
|-------|-----------|-------|-----------|

RECORDS BELOW 60% COMPLETENESS
| Company | Completeness | Key Missing Fields |
|---------|--------------|--------------------|

AVERAGE COMPLETENESS: [X]%
```

---

### MODE 7: DEPRECATED ENUM DETECTION
**Trigger:** Part of full health check or "Check for deprecated values" or "Enum audit"

**Steps:**

1. Search HubSpot for all companies where `customer_segment` = `AI - Colocation Operator`
   - This value was deprecated in March 2026
   - Correct mapping: `customer_segment` = `Data Center Colo Provider` + `company_sub_segment` = `AI Signals - colo`
2. Search for any other non-standard `customer_segment` values that don't match the canonical list in hubspot-values.md:
   - `Data Center Colo Provider`, `Fiber Operator`, `Network Operator(Tier 1 / VNO)`, `Enterprise` (MSP), `NeoCloud`
   - Plus non-ICP values: `Dark Fiber - Commercial Enterprise`, `Enterprise-CustomerSegment`, `Partner Target`, `Other`, `Unknown`, `Flagged for deletion`
3. Report all records with deprecated or invalid enum values

**Output:**
```
DEPRECATED ENUM REPORT  -  [Date]
==================================

DEPRECATED: AI - Colocation Operator (migrate to Data Center Colo Provider + AI Signals - colo)
| Company | Domain | Current Segment | Current Sub-Segment |
|---------|--------|-----------------|---------------------|

INVALID/NON-STANDARD VALUES
| Company | Field | Current Value | Expected Values |
|---------|-------|---------------|-----------------|

SUMMARY: [N] deprecated, [N] invalid
```

**When running under CRM Guardian:** Deprecated `AI - Colocation Operator` → Tier 1 auto-fix (migrate to `Data Center Colo Provider` + `AI Signals - colo`). Invalid values → Tier 3 (flag for review).

---

### MODE 8: CONTACT-LEVEL HYGIENE
**Trigger:** Part of full health check or "Audit contacts" or "Contact data quality"

**Steps:**

1. Pull all contacts with: `hubspot_owner_id`, `customer_segment`, `email`, `firstname`, `lastname`, `jobtitle`, `company`
2. For each contact, get the associated company record (via HubSpot associations)
3. **Owner mismatch check:** Compare contact `hubspot_owner_id` to associated company `hubspot_owner_id`. Flag mismatches.
4. **Segment mismatch check:** Compare contact `customer_segment` to associated company `customer_segment`. Flag mismatches. Company record is source of truth.
5. **Orphaned contacts:** Flag contacts with no associated company.
6. **Missing email:** Flag contacts where `email` is blank.
7. **Missing title:** Flag contacts where `jobtitle` is blank (impacts persona mapping).

**Output:**
```
CONTACT HYGIENE REPORT  -  [Date]
==================================

OWNER MISMATCHES (contact owner != company owner)
| Contact | Company | Contact Owner | Company Owner | Correct Owner |
|---------|---------|---------------|---------------|---------------|

SEGMENT MISMATCHES (contact segment != company segment)
| Contact | Company | Contact Segment | Company Segment |
|---------|---------|-----------------|-----------------|

ORPHANED CONTACTS (no associated company)
| Contact | Email | Title | Created |
|---------|-------|-------|---------|

MISSING EMAIL
| Contact | Company | Title |
|---------|---------|-------|

SUMMARY: [N] owner mismatches, [N] segment mismatches, [N] orphaned, [N] missing email
```

**When running under CRM Guardian:** Owner sync = Tier 1 auto-fix. Segment sync from company = Tier 1 auto-fix. Orphaned contacts and missing email = report only.

---

### MODE 9: STALE LEAD DETECTION
**Trigger:** Part of full health check or "Check stale leads" or "Untouched new leads"

**Steps:**

1. Pull all companies where `hs_lead_status` = `NEW`
2. For each, check `createdate`  -  if created more than 14 days ago, it's stale
3. Cross-check `notes_last_contacted`  -  if blank or older than `createdate`, no one has acted on it
4. Group by owner for accountability

**Output:**
```
STALE NEW LEADS REPORT  -  [Date]
==================================

LEADS UNTOUCHED 14+ DAYS
| Company | Owner | Segment | Created | Days Since | Last Activity |
|---------|-------|---------|---------|------------|---------------|

BY OWNER:
| Owner | Stale NEW Leads | Total NEW Leads |
|-------|-----------------|-----------------|

SUMMARY: [N] stale NEW leads out of [N] total NEW leads
```

**When running under CRM Guardian:** Report only  -  no auto-action. Surfaces in the run report for rep awareness.

---

### MODE 10: COOPER-OWNED ACCOUNT DETECTION
**Trigger:** Part of full health check or "Check Cooper's accounts" or "Placeholder ownership"

Cooper Kennedy (Owner ID: `160267902`) is RevOps. Accounts assigned to Cooper are placeholders that should be routed to the correct sales rep based on HQ state.

**Steps:**

1. Pull all companies where `hubspot_owner_id` = `160267902`
2. For each, check if `state` or `hs_state_code` is populated
3. If state is known → look up correct owner via territory model:
   - East states → Tim Lieto (`161889085`)
   - West states + DC → Ken Cunningham (`162339176`)
   - Non-US → Tim Ziemer (`159350430`)
4. If state is blank → flag as unrouteable (needs state first)

**Output:**
```
COOPER-OWNED ACCOUNTS REPORT  -  [Date]
========================================

ROUTEABLE (state known  -  can auto-assign)
| Company | State | Recommended Owner |
|---------|-------|-------------------|

UNROUTEABLE (state blank  -  needs manual review)
| Company | Domain | Country | Notes |
|---------|--------|---------|-------|

SUMMARY: [N] routeable (auto-fix ready), [N] unrouteable (manual review)
```

**When running under CRM Guardian:** Routeable accounts = Tier 1 auto-fix (correct `hubspot_owner_id` based on HQ state). Unrouteable = Tier 3 (flag for manual state lookup).

---

### MODE 11: CONTACT DELETION FLAGGING
**Trigger:** Part of full health check or "Flag junk contacts" or "Find contacts to delete" or "Hard bounce cleanup"

Populate the `flagged_for_deletion` Boolean checkbox on Contact records that meet clear-cut junk criteria so Cooper can bulk-delete them from the HubSpot UI after reviewing the daily email report. This mode is the single source of truth for contact-deletion criteria — crm-guardian only orchestrates and applies safety tiers.

**Fields to pull:** `email`, `firstname`, `lastname`, `phone`, `mobilephone`, `hs_email_hard_bounce_reason_enum`, `hs_email_optout`, `hs_lifecyclestage`, `createdate`, `notes_last_contacted`, `hs_sales_email_last_replied`, associated companies (+ their `customer_segment`), associated deals (+ `dealstage`).

**Steps:**

1. **Apply NEVER-FLAG safety filters first** (compliance + safety gates — exclude before any rule evaluation):
   - `hs_email_optout = true` → retain for CAN-SPAM / GDPR suppression
   - `hs_lifecyclestage` = `customer` or `opportunity`
   - Any contact with an associated deal where `dealstage` is not `closedwon` or `closedlost` (open deal)
   - `createdate` < 30 days ago AND no email AND no phone AND no mobilephone — likely sourcing-pipeline output awaiting Apollo enrichment (route to contact-discovery / Job 5 instead)

2. **TIER 1 — AUTO-FLAG** (set `flagged_for_deletion = true`). Evaluate each remaining contact against these rules; any single match is sufficient:
   - `hs_email_hard_bounce_reason_enum` has ANY value — the address is provably invalid
   - Email matches a generic spam pattern: starts with `noreply@`, `no-reply@`, `donotreply@`, `mailer-daemon@` (case-insensitive)
   - Email matches a test/placeholder pattern: `test@test` anywhere in the local/domain, domain = `example.com`, domain = `yourdomain`, OR both `firstname` and `lastname` equal `"test"` (case-insensitive)
   - Contact is associated ONLY to companies where `customer_segment = "Flagged for deletion"` AND those companies have zero open deals (true orphans remaining after company-level cleanup)

3. **TIER 2 — AUTO-FLAG + REVIEW** (set `flagged_for_deletion = true` AND list in run report for closer inspection):
   - No email AND no phone AND no mobilephone AND no company association AND `createdate` > 180 days ago AND `hs_lifecyclestage` in {blank, `subscriber`, `lead`} AND zero associated deals AND no sales-activity timestamp (`notes_last_contacted` and `hs_sales_email_last_replied` both blank)
   - Duplicate email address across multiple Contact records — keep the record with the most recent sales activity (`notes_last_contacted` most recent; tiebreaker = highest `hs_object_id`), flag every other sibling

4. Produce a report summarizing both tiers with record IDs, matched rule, and — for Tier 2 — a "Review Note" explaining which heuristic fired.

**Output:**
```
CONTACT DELETION FLAGGING REPORT  -  [Date]
============================================

TIER 1 — AUTO-FLAGGED (clear-cut junk)
| Contact ID | Name | Email | Matched Rule |
|------------|------|-------|--------------|

TIER 2 — AUTO-FLAGGED + REVIEW (heuristic match)
| Contact ID | Name | Email | Matched Rule | Review Note |
|------------|------|-------|--------------|-------------|

SKIPPED (never-flag filters applied)
| Reason | Count |
|--------|-------|
| hs_email_optout = true | [N] |
| Customer / Opportunity lifecycle | [N] |
| Open-deal association | [N] |
| Recent sourcing (< 30d, no contact info) | [N] |

SUMMARY: [N] Tier 1 flagged, [M] Tier 2 flagged, [K] skipped (safety)
BULK DELETE: filter HubSpot contacts on `flagged_for_deletion = true` → review → bulk delete
```

**When running under CRM Guardian:** Tier 1 rules map to Guardian Tier 1 (auto-fix). Tier 2 rules map to Guardian Tier 2 (auto-fix + flag). No per-record HubSpot notes are written — the `flagged_for_deletion = true` value is the evidence; the daily Guardian email report is the audit trail.
