---
name: crm-hygiene
description: "MaiaEdge CRM health checker and data quality auditor. Scans HubSpot for duplicates, missing fields, stale records, incomplete enrichment, and data quality issues. Use when asked to check CRM health, find duplicates, audit data quality, clean up HubSpot, find stale or untouched accounts, check data completeness, identify records missing segments or key fields, or run any kind of CRM hygiene check. Also trigger when user mentions duplicates, missing data, data cleanup, stale accounts, dead records, CRM quality, incomplete records, or data hygiene. Produces health score (0-100), duplicate detection with fuzzy matching, missing critical field reports, stale record identification, and enrichment completion tracking."
---

# MaiaEdge CRM Hygiene Auditor

## Purpose

Run comprehensive health checks on HubSpot company, contact, and deal records. Identifies data quality issues that degrade pipeline accuracy, cause routing errors, and waste rep time. Produces actionable reports with specific records to fix.

The goal is to catch problems before they compound — a missing state leads to wrong territory assignment, which leads to wrong rep, which leads to a cold email from the wrong person. Clean data is the foundation everything else runs on.

---

## HubSpot Properties Reference

### Company Fields to Audit
```
name, domain, state, hs_state_code, country, city, hubspot_owner_id,
customer_segment, company_sub_segment, phone, numberofemployees,
annualrevenue, industry, founded_year, notes_last_contacted,
notes_last_updated, createdate, hs_lead_status
```

### Contact Fields to Audit
```
firstname, lastname, email, jobtitle, phone, hubspot_owner_id,
company, notes_last_contacted, createdate, lifecyclestage
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

Run all of the checks below (Modes 2–6) in sequence and produce a consolidated health report. This is the "give me everything" mode.

**Output:**
```
CRM HEALTH REPORT — [Date]
============================

OVERALL HEALTH SCORE: [X]/100

SUMMARY
| Category | Issues Found | Severity |
|----------|-------------|----------|
| Duplicates | [N] likely duplicate pairs | 🔴 High |
| Missing Critical Fields | [N] records | 🔴 High |
| Stale Records | [N] untouched 90+ days | 🟡 Medium |
| Incomplete Enrichment | [N] partially enriched | 🟡 Medium |
| Data Completeness | [avg]% across all records | 🟢/🟡/🔴 |

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
- -0.5 per stale record (90+ days no contact)
- -0.5 per record below 60% completeness
- Floor at 0

---

### MODE 2: DUPLICATE DETECTION
**Trigger:** "Find duplicates" or "Are there duplicate companies?" or "Dedupe our CRM"

**Steps:**

1. Pull all companies with: `name`, `domain`, `state`, `hubspot_owner_id`, `customer_segment`, `createdate`
2. **Domain-based duplicates**: Group by `domain` — any domain appearing 2+ times is a definite duplicate
3. **Name-based fuzzy matches**: Flag companies with very similar names (e.g., "CoreWeave" vs "CoreWeave Inc" vs "Core Weave"). Look for:
   - Exact name matches (case-insensitive)
   - Name with/without common suffixes: Inc, LLC, Corp, Ltd, Co, Group, Holdings
   - Name with/without "The" prefix
4. Cross-check contacts for duplicate email domains
5. For each duplicate set, identify which record is the "primary" (most complete, most recent activity)

**Output:**
```
DUPLICATE DETECTION REPORT — [Date]
======================================

DOMAIN DUPLICATES (definite — same domain, different records)
| Domain | Record Count | Record IDs | Names | Recommended Primary |
|--------|-------------|------------|-------|-------------------|

NAME SIMILARITY MATCHES (likely — review needed)
| Group | Names | Domains | Confidence |
