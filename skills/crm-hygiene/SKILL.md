---
name: crm-hygiene
description: "MaiaEdge CRM health checker and data quality auditor. Scans HubSpot for duplicates, missing fields, stale records, incomplete enrichment, deprecated enum values, contact-level mismatches, placeholder ownership, and junk contacts to flag for deletion. Use when asked to check CRM health, find duplicates, audit data quality, clean up HubSpot, find stale accounts, check data completeness, identify records missing key fields, audit contacts, or flag junk contacts. Also trigger on mentions of duplicates, missing data, data cleanup, stale accounts, CRM quality, contact mismatches, hard-bounced emails, spam/test contacts, or contact deletion flagging. Produces health score (0-100), duplicate detection, stale record reports, and contact-level hygiene findings."
---

# MaiaEdge CRM Hygiene Auditor

> **For autonomous CRM maintenance, use the crm-guardian skill instead.** This skill is for manual, on-demand audits of specific CRM health dimensions. CRM Guardian runs proactively and handles routine fixes (segment corrections, owner routing, stale enrichment) with its safety tier system.

## Purpose

Run comprehensive health checks on HubSpot company, contact, and deal records. Identifies data quality issues that degrade pipeline accuracy, cause routing errors, and waste rep time. Produces actionable reports with specific records to fix.

The goal is to catch problems before they compound  -  a missing state leads to wrong territory assignment, which leads to wrong rep, which leads to a cold email from the wrong person. Clean data is the foundation everything else runs on.

## Clarification

Before running, two questions that change the scope:
1. Which mode (or "all")? Full health check (Mode 1 / all modes), a specific check (duplicates, missing fields, stale records, enrichment, contacts, classification drift, signal heat), or a targeted cleanup task?
2. Segment filter? Run across the full CRM, or scope to a specific segment (Colo / Fiber / Network Op / NeoCloud / MSP / Enterprise) or a subset of owners?

Coach: if you just say "clean up the CRM" or "check data quality," I'll default to a full Mode 1 health check across all segments and surface the top issues - you can narrow scope from there.

## Reference Files

For canonical HubSpot schema definitions, read these context files:
- **`context/hubspot/property-schema.md`**  -  Company property definitions, valid values, territory model
- **`context/hubspot/hubspot-values.md`**  -  Exact HubSpot enum values (case-sensitive)
- **`context/hubspot/contact-schema.md`**  -  Contact-level properties, lifecycle, enrichment sync
- **`context/hubspot/deals-schema.md`**  -  Deal pipeline stages, MEDDPICC fields, quote workflows
- **`context/hubspot/territory-model.md`**  -  Authoritative 5-region state-to-owner mapping and territory boundaries (Northeast/Southeast/Central/West/International + Europe). Load this at runtime for all owner-routing lookups; do NOT inline the map.
- **`context/account-tiering/sub-segment-qualification.md`**  -  Canonical 30-value list of active `company_sub_segment` enums (case-sensitive). Source-of-truth for the Mode 7 deprecated enum scan and the new weekly audit below. Key 2026-05-14 entries: `Subsea cable operator` (30th value), `Greenfield` is a real sub-segment paired with Colo or NeoCloud parent, `Crypto to AI - Neoclouds` inclusive of operator AND landlord. Retired values (auto-flag if encountered): `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, `Managed Network Services - Network Operator`.
- **`context/account-tiering/enrichment-protocols.md`**  -  Research-first workflow, D1 disqualifier check, D5 v2 per-sub-segment protocols. §8 (positive-evidence reasoning requirements) and §9 (verification queries) are the canonical source for the weekly audit below.
- **`context/account-tiering/tier-compute-spec.md`**  -  Canonical `account_tier` function. Read when validating tier-vs-segment coherence in audit reports; the spec also governs the `hs_is_target_account = true` override behavior.
- **`context/account-tiering/d1-global-disqualifiers.md`**  -  D1 disqualifier rules. Read before Mode 2 duplicate detection to avoid false-positive merge recommendations on D1-disqualified records.
- **`context/account-tiering/d2-wholesale-arm-policy.md`**  -  Wholesale-arm policy. Read before Mode 2 to avoid flagging legitimate parent/wholesale-arm pairs as duplicates.
- **`context/account-tiering/d3-disambiguation-flowcharts.md`**  -  MEDIUM. Disambiguation flowcharts for borderline segment assignments; aids Mode 12 classification-drift routing decisions.
- **`context/account-tiering/sub-segment-qualification-full.md`**  -  MEDIUM. Full 30-sub-segment reference with qualifying evidence requirements; used in Mode 12 positive-evidence checks.
- **`context/hubspot/call-schema.md`**  -  MEDIUM. Call-level properties; relevant when Mode 4/9 stale-record checks cross-reference call activity.
- **`context/hubspot/poc-schema.md`**  -  MEDIUM. POC schema; relevant when Mode 3 completeness or Mode 11 deletion-safety checks involve POC-stage records.
- **`context/segments/enterprise.md`**  -  MEDIUM. Enterprise ICP deep-dive; used in Mode 3-bis Enterprise completeness validation (referenced inline).

---

## HubSpot Properties Reference

### Company Fields to Audit
```
name, domain, state, hs_state_code, country, city, hubspot_owner_id,
customer_segment, company_sub_segment, account_tier, signal_heat,
segmentation_confidence,
phone, numberofemployees, annualrevenue, industry, founded_year,
notes_last_contacted, notes_last_updated, createdate, hs_lead_status,
last_enriched_date, infrastructure_profile, fabric_provisioning_approach,
geographic_focus, account_brief,
hyperscaler_proximity, provisioning_landscape, recent_news_or_trigger_event,
last_signal_score, last_signal_date, signal_count_last_30d
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

### MODE 3-bis: Enterprise ICP Completeness Validation (added 2026-05-11)

`Enterprise-CustomerSegment` records have stricter required-field completeness than other ICP segments because the hard scale gate ($1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR confirmed in-house net eng + vertical match) means the record needs evidence to belong in ICP at all.

**Required fields for HIGH-confidence Enterprise records:**
- `customer_segment` = `Enterprise-CustomerSegment`
- `company_sub_segment` populated AND in `[Financial Services - Enterprise, Healthcare Systems - Enterprise, Retail and Distribution - Enterprise, Outsourcing Services - Enterprise]` (any other value flags)
- `account_tier` populated (typically tier_2 or tier_3 per Enterprise rules - no Tier 1 path unless exceptional trigger)
- `infrastructure_profile` populated AND mentions either "data center" / "DC" count OR "Equinix Fabric" / "Megaport" / "in-house net eng" / "NOC" - the scale-gate evidence MUST be in the brief
- `account_brief` populated AND framed in Multi-DC ICP terms (mentions sub-segment vertical context, scale evidence, anchor pain - see `context/segments/enterprise.md` Insider Language Bank for sub-segment vocabulary)

**Validation checks:**
1. Find companies where `customer_segment = "Enterprise-CustomerSegment"` AND ANY required field above is missing or non-conforming
2. Find companies where `customer_segment = "Enterprise-CustomerSegment"` AND `company_sub_segment` is in a Watch List vertical (Manufacturing, Energy/Utilities, Logistics) - these are mis-classified, route to R2 RE_ENRICH_FULL for re-evaluation
3. Find companies where `customer_segment = "Enterprise-CustomerSegment"` AND `account_brief` predates 2026-05-11 (before ICP promotion) AND doesn't reference Enterprise sub-segment language - likely tagged under old non-ICP framing; route to R2 RE_ENRICH_FULL for scale-gate verification

**When running under CRM Guardian:** Missing Enterprise-required field → Tier 3 hold ("incomplete Enterprise record - defer to R1/R2"). Watch List sub-segment on Enterprise record → Tier 2 (auto-flag in run report; do NOT auto-correct sub-segment, defer to R2 for re-enrichment). Pre-promotion brief framing → Tier 3 hold for Cooper review.

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

1. Pull all companies with enrichment fields: `customer_segment`, `company_sub_segment`, `account_tier`, `segmentation_confidence`, `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`, `account_brief`, `hyperscaler_proximity`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`
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
2. Search for any other non-standard `customer_segment` values that don't match the canonical list in `context/hubspot/hubspot-values.md`:
   - **ICP values (6 as of 2026-05-11):** `Data Center Colo Provider`, `Fiber Operator`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, `NeoCloud`, `Enterprise-CustomerSegment` (Multi-DC ICP, promoted 2026-05-11; 4 sub-segments only - Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services)
   - Non-ICP values: `Partner Target`, `Other`, `Unknown`, `Flagged for deletion`
   - Stale values to remediate: any record still on the deleted `Enterprise` (rename to `MSP/Aggregator`) or `Dark Fiber - Commercial Enterprise` (deleted May 2026 - re-classify per Fiber Operator rules or flag).
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
3. If state/country is known → look up correct owner via `context/hubspot/territory-model.md` (5-region map: Northeast, Southeast, Central, West, Europe, International). Load the map at runtime; do NOT apply a hardcoded 2-region East/West table.
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

Populate the `flagged_for_deletion` Boolean checkbox on Contact records that meet clear-cut junk criteria so Cooper can bulk-delete them from the HubSpot UI after reviewing the daily email report. This mode is the single source of truth for contact-deletion criteria - crm-guardian only orchestrates and applies safety tiers.

**Fields to pull:** `email`, `firstname`, `lastname`, `phone`, `mobilephone`, `hs_email_hard_bounce_reason_enum`, `hs_email_optout`, `hs_lifecyclestage`, `createdate`, `notes_last_contacted`, `hs_sales_email_last_replied`, associated companies (+ their `customer_segment`), associated deals (+ `dealstage`).

**Steps:**

1. **Apply NEVER-FLAG safety filters first** (compliance + safety gates - exclude before any rule evaluation):
   - `hs_email_optout = true` → retain for CAN-SPAM / GDPR suppression
   - `hs_lifecyclestage` = `customer` or `opportunity`
   - Any contact with an associated deal where `dealstage` is not `closedwon` or `closedlost` (open deal)
   - `createdate` < 30 days ago AND no email AND no phone AND no mobilephone - likely sourcing-pipeline output awaiting Apollo enrichment (route to contact-discovery / Job 5 instead)

2. **TIER 1 - AUTO-FLAG** (set `flagged_for_deletion = true`). Evaluate each remaining contact against these rules; any single match is sufficient:
   - `hs_email_hard_bounce_reason_enum` has ANY value - the address is provably invalid
   - Email matches a generic spam pattern: starts with `noreply@`, `no-reply@`, `donotreply@`, `mailer-daemon@` (case-insensitive)
   - Email matches a test/placeholder pattern: `test@test` anywhere in the local/domain, domain = `example.com`, domain = `yourdomain`, OR both `firstname` and `lastname` equal `"test"` (case-insensitive)
   - Contact is associated ONLY to companies where `customer_segment = "Flagged for deletion"` AND those companies have zero open deals (true orphans remaining after company-level cleanup)

3. **TIER 2 - AUTO-FLAG + REVIEW** (set `flagged_for_deletion = true` AND list in run report for closer inspection):
   - No email AND no phone AND no mobilephone AND no company association AND `createdate` > 180 days ago AND `hs_lifecyclestage` in {blank, `subscriber`, `lead`} AND zero associated deals AND no sales-activity timestamp (`notes_last_contacted` and `hs_sales_email_last_replied` both blank)
   - Duplicate email address across multiple Contact records - keep the record with the most recent sales activity (`notes_last_contacted` most recent; tiebreaker = highest `hs_object_id`), flag every other sibling

4. Produce a report summarizing both tiers with record IDs, matched rule, and - for Tier 2 - a "Review Note" explaining which heuristic fired.

**Output:**
```
CONTACT DELETION FLAGGING REPORT  -  [Date]
============================================

TIER 1 - AUTO-FLAGGED (clear-cut junk)
| Contact ID | Name | Email | Matched Rule |
|------------|------|-------|--------------|

TIER 2 - AUTO-FLAGGED + REVIEW (heuristic match)
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

**When running under CRM Guardian:** Tier 1 rules map to Guardian Tier 1 (auto-fix). Tier 2 rules map to Guardian Tier 2 (auto-fix + flag). No per-record HubSpot notes are written - the `flagged_for_deletion = true` value is the evidence; the daily Guardian email report is the audit trail.

---

### MODE 12: WEEKLY CLASSIFICATION-DRIFT AUDIT (NEW 2026-05-14 - Phase 3 Step 10)
**Trigger:** Weekly cron, or part of full health check, or "Run classification drift audit"

This mode is the **defense-in-depth layer** that catches records which escaped Stage 5 enforcement in R1 / R2 / Signal Scan. It is audit-only - crm-hygiene does NOT write segment / sub-segment / tier corrections itself. Instead it flags records for downstream resolution by R2 (broad re-enrichment) or D7 (deep-research edge-case resolution).

This mode complements:
- **R2** - broad 120-day re-enrichment cadence; D5 v2 protocols at scale
- **D7 Edge Case Resolution** - Cooper-paced, 30 records/run, hard cases requiring multi-source research
- **R-Tier-Audit** - daily M-F drift sweep (3pm CT) recomputing `account_tier` against `context/account-tiering/tier-compute-spec.md`

crm-hygiene's role is to **surface and route**, not to resolve.

**Steps:**

1. **Default-sub-segment audit (positive-evidence requirement per `context/account-tiering/enrichment-protocols.md` §8):** Pull all companies where `company_sub_segment` is one of the framework default values (`Regional CLEC - Fiber operator`, `Standard - colo`, `Telecom Aggregator - MSP`). For each, check that `account_brief` OR a reasoning field contains a positive-evidence string demonstrating the record actually MATCHES the default's qualifying criteria (not just absence of disqualifiers). Records without positive-evidence reasoning → flag for R2 re-enrichment.

2. **Manual-review-required hard rule (per Cooper, hard policy):** Pull all companies where `segmentation_confidence = "manual_review_required"`. For each, compute days-since-set (via canvas `F0B0AFSB9LN` Tier 3 hold timestamps OR `last_enriched_date` as fallback). Any record on `manual_review_required` for **>14 days** → route to **D7 Edge Case Resolution**. This is non-negotiable: holds older than 14 days are stuck holds that need deep research, not another R2 pass.

3. **Stale low-confidence (low_5069) audit:** Pull all companies where `segmentation_confidence = "low_5069"` AND `last_enriched_date` is either blank OR >60 days old. Without a recent R2 touch, low confidence records drift into pseudo-permanence. Flag for R2 re-enrichment.

4. **Confidence-without-reasoning audit (per `context/account-tiering/enrichment-protocols.md` §9):** Pull all companies where `segmentation_confidence` is populated (any non-null value: `high_90`, `medium_7089`, `low_5069`, `manual_review_required`) AND `account_brief` is blank OR contains no reasoning string. Confidence without reasoning is unverifiable - flag for R2 re-enrichment to rebuild the reasoning record.

5. **Retired sub-segment scan (per `context/account-tiering/sub-segment-qualification.md` retired list):** Pull all companies where `company_sub_segment` is in the retired set: `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, `Managed Network Services - Network Operator`. Flag for R2 re-enrichment to re-classify under one of the 30 active sub-segment values.

**Output:**
```
CLASSIFICATION DRIFT AUDIT  -  [Date]
======================================

ROUTE TO R2 (broad re-enrichment)
| Record | Reason | Audit Rule |
|--------|--------|------------|
| ... | default-sub-segment without positive-evidence | §8 violation |
| ... | low_5069 >60 days no R2 touch | stale low-confidence |
| ... | confidence without reasoning | §9 violation |
| ... | retired sub-segment value | enum drift |

ROUTE TO D7 (deep-research edge cases)
| Record | Reason | Days on hold |
|--------|--------|--------------|
| ... | manual_review_required >14 days | [N] days (HARD RULE) |

SUMMARY: [N] flagged for R2, [M] routed to D7 (hard 14-day rule)
```

**When running under CRM Guardian:** This mode writes NO segment / sub-segment / tier / confidence fields itself. The R2-routed list is consumed by R2's next run as priority records. The D7-routed list is consumed by D7's next run within its 30-record cap. Both consumers read the audit output from the Slack DM + the cross-routine canvas ledger (`F0B0AFSB9LN`).

**Why audit-only:** crm-hygiene has no Apollo budget and no deep-research capability. It can detect drift (cheap, query-based) but cannot resolve it (resolution requires Apollo enrichment in R2 or multi-source research in D7). Splitting detection from resolution keeps each routine within its competence and prevents Apollo budget blow-outs.

---

### MODE 13: SIGNAL HEAT DRIFT AUDIT (NEW 2026-05-20)
**Trigger:** Weekly cron, or part of full health check, or "Run signal heat drift audit"

Detects records where the stored `signal_heat` value disagrees with the freshly-computed value per `context/account-tiering/tier-compute-spec.md` §11.5. Catches manual edits, R-Tier-Audit/Signal Scan misses, and stale heat on records that haven't been touched in weeks.

**Audit-only** - crm-hygiene does NOT write `signal_heat` corrections itself. Drift flags route to R-Tier-Audit's next run (cheap to add to the existing sweep) or surface for Cooper's review if the drift is concentrated in suspicious patterns (e.g., many target-account records all show drift, suggesting a routine bug).

**Steps:**

1. Query all active ICP records: `customer_segment IN (NeoCloud, Data Center Colo Provider, Fiber Operator, Network Operator(Tier 1 / VNO), MSP/Aggregator, Enterprise-CustomerSegment) AND type != Customer`. Pull `signal_heat`, `last_signal_score`, `last_signal_date`, `signal_count_last_30d`, `hs_is_target_account`.
2. For each record, also fetch the count of open deals past `appointmentscheduled` (via association lookup; HubSpot `hs_is_closed_won` / `hs_is_closed_lost` booleans for open-deal status).
3. Compute `expected_heat` per the inlined spec (**`last_signal_date` is event date** post-2026-05-28; **enum is Title Case**):

   ```
   signal_heat is computed top-down, first match wins:

   Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
          OR signal_count_last_30d >= 2
          OR account has any associated open deal past `appointmentscheduled`

   Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

   Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

   Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL
   ```

4. Compare against stored `signal_heat`. Flag any record where `expected_heat != stored signal_heat`.
5. Categorize drift: (a) `Cold` -> warmer (a fresh signal landed but heat didn't update), (b) `Hot/Warm` -> colder (signal aged out but heat didn't decay), (c) `null` -> any (heat field never populated - common for legacy records pre-2026-05-20 property creation).

**Output:**

```
SIGNAL HEAT DRIFT AUDIT  -  [Date]
======================================

DRIFT FLAGGED: [N] records (target = <1% of active ICP)

By drift type:
- cold -> warmer: [X] (signal landed without heat update)
- hot/warm -> colder: [Y] (signal aged without decay)
- null -> [bucket]: [Z] (legacy records missing heat field)

ROUTE TO R-TIER-AUDIT (next weekday run)
| Record | Stored Heat | Expected Heat | Reason |
|--------|-------------|---------------|--------|
| ...    | warm        | cool          | last_signal_date 75d, no stack, no open deal |
| ...    | null        | cold          | legacy record, no signal history |

SUMMARY: [N] records flagged for R-Tier-Audit to correct on next sweep.
```

If drift exceeds 1% of active ICP (suggests a routine bug), surface a separate Slack DM to Cooper with the pattern (which routines might be missing the heat write, are heat writes concentrated on target accounts, etc.).
