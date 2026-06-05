---
name: contact-discovery
description: "MaiaEdge contact discovery strategist. Finds the right people at target accounts and audits existing contact coverage. Use when asked to find contacts, prospect for contacts, identify contact gaps, map buying committee, check contact coverage, discover personas, or evaluate who to reach out to at a company. Operates in two modes: (1) HubSpot contact map audit showing persona coverage gaps by segment, (2) Apollo prospecting to find specific titles based on coverage gaps. Understands MaiaEdge buying committee by segment (Technical Champion, Business Sponsor, Economic Buyer, Procurement) and flags missing personas. Multi-threaded outreach ready."
---

# MaiaEdge Contact Discovery

## Purpose

Find the right people at target accounts and identify gaps in contact coverage. This skill combines two capabilities: searching Apollo for new contacts to prospect, and auditing existing HubSpot contacts to assess coverage quality. The goal is to make sure every target account has the right mix of personas engaged  -  not just one name in the CRM.

MaiaEdge sells infrastructure technology, so the buying committee typically involves network engineering, infrastructure/IT leadership, product/strategy, and procurement. Missing any of these personas means deals can stall without warning.

## Reference Files

- **contact-schema.md**  -  Contact properties, lifecycle stages, enrichment sync mappings
- **territory-model.md**  -  State-to-owner mapping for routing new contacts

---

## Target Personas by Segment

The right contacts to find depend on the customer segment. Here's who matters at each type of company:

### Colocation / Data Center Providers
| Persona | Typical Titles | Role in Deal |
|---------|---------------|--------------|
| **Technical Champion** | VP Network Engineering, Director of Network Operations, Network Architect | Evaluates technical fit, runs POC |
| **Business Sponsor** | VP/SVP Operations, COO, VP Product | Owns budget, cares about competitive differentiation |
| **Economic Buyer** | CFO, VP Finance, VP Strategy | Approves spend, cares about ROI |
| **Procurement** | Director of Procurement, Vendor Management | Handles contracts, MSAs |

### Fiber Operators
| Persona | Typical Titles | Role in Deal |
|---------|---------------|--------------|
| **Technical Champion** | VP Engineering, Director Network Planning, OSP Manager | Evaluates fit for their network |
| **Business Sponsor** | VP Enterprise Sales, VP Wholesale, GM | Cares about new revenue from enterprise services |
| **Economic Buyer** | CFO, CEO (smaller operators) | Budget authority |

### Network Operators / Carriers
| Persona | Typical Titles | Role in Deal |
|---------|---------------|--------------|
| **Technical Champion** | VP Network Architecture, Director of SDN/NFV, CTO | Technical evaluation |
| **Business Sponsor** | VP Product, VP Enterprise, SVP Network Services | Revenue and product strategy |
| **Economic Buyer** | CFO, SVP/EVP | Budget authority |

### Neoclouds (GPU Cloud Providers)
| Persona | Typical Titles | Role in Deal |
|---------|---------------|--------------|
| **Technical Champion** | VP Infrastructure, Director of Network Engineering, Head of Platform | Cares about interconnect performance |
| **Business Sponsor** | VP Operations, COO, VP Product | Cares about multi-site orchestration |
| **Economic Buyer** | CFO, CEO (many are VC-backed startups) | Burn rate conscious |

### MSP / Aggregators
| Persona | Typical Titles | Role in Deal |
|---------|---------------|--------------|
| **Technical Champion** | VP Engineering, Director of Network Services | Evaluates integration with their platform |
| **Business Sponsor** | VP Sales, VP Partnerships, GM | Cares about adding value to their service portfolio |

### Enterprise (Multi-DC ICP)

HubSpot `customer_segment = "Enterprise-CustomerSegment"`. Four sub-segments: Financial Services, Healthcare Systems, Retail and Distribution, Outsourcing Services. Promoted to ICP 2026-05-11.

| Persona | Typical Titles | Role in Deal |
|---------|---------------|--------------|
| **Technical Champion** | VP Network Infrastructure, Director Network Engineering, VP Networks, Director WAN Engineering, Principal Network Engineer, Network Architect, Lead Network Architect | **Primary technical champion.** Owns inter-DC paths, dark fiber redundancy, BGP / MPLS burden, Type 2 visibility gaps. Runs technical evaluation and POC. |
| **Business Sponsor** | CIO, Chief Information Officer, CTO (at retail/healthcare) | Cares about unified private connectivity across all sites, AI infrastructure access, cloud cost. Budget visibility. |
| **Economic Buyer** | CIO (most enterprises) OR CTO (at retail/healthcare) | Approves spend, signs the order form. Same person as Business Sponsor at most enterprises. |
| **Security Stakeholder** | CSO, CISO, Chief Information Security Officer, VP Cybersecurity | Cares about line-rate AES-256-GCM encryption, hop-by-hop visibility, audit-ready policy enforcement, data sovereignty. Regulatory framing (HIPAA / PCI-DSS / SOX / GDPR / HITRUST) lands here. |
| **Compliance** (regulated verticals only) | Chief Compliance Officer, VP Risk, VP Audit, Compliance Director | Owns regulatory exposure (HIPAA at healthcare, PCI-DSS at retail/financial, SOX at financials, GDPR at multi-national, client-specific at BPO). May be involved in audit-trail / policy-control conversations. |
| **Procurement** | Director of Procurement, Vendor Management, Strategic Sourcing | Handles MSAs, multi-year terms. Active later in the cycle, not early. |

**Persona-gap detection rules for Enterprise:** An Enterprise account is "well-covered" when at least **Technical Champion + Business Sponsor (CIO)** are mapped in HubSpot. For regulated verticals (`Financial Services - Enterprise` / `Healthcare Systems - Enterprise` / `Outsourcing Services - Enterprise` when handling regulated client data), "well-covered" raises to **Technical Champion + Business Sponsor + Security Stakeholder (CSO/CISO)**. Flag a gap if only one role is in HubSpot. Coverage of all 6 personas is rarely needed before Stage 3 deal progression.

---

## Task Routing

### MODE 1: ACCOUNT CONTACT MAP (HubSpot Audit)
**Trigger:** "Who do we have at [company]?" or "Map contacts at [company]" or "Contact coverage for [company]"

**Steps:**

1. Search HubSpot for the company by name or domain
2. Get the company's `customer_segment` and `customer_sub_segment` for persona mapping
3. Search HubSpot contacts associated with that company
4. For each contact, pull: `firstname`, `lastname`, `email`, `jobtitle`, `phone`, `hubspot_owner_id`, `notes_last_contacted`, `lifecyclestage`
5. Map each contact to a persona role (Technical Champion, Business Sponsor, Economic Buyer, Procurement) based on their job title
6. Identify which persona slots are filled and which are gaps

**Output:**
```
CONTACT MAP: [Company Name]
==============================
Segment: [segment] | Sub-segment: [sub-segment]
Owner: [rep name] | Contacts in HubSpot: [N]

COVERAGE ASSESSMENT
| Persona | Status | Contact | Title | Last Contacted |
|---------|--------|---------|-------|----------------|
| Technical Champion | ✅ Found | [name] | [title] | [date] |
| Business Sponsor | ❌ Gap |  -  |  -  |  -  |
| Economic Buyer | ❌ Gap |  -  |  -  |  -  |
| Procurement | ⚠️ Optional |  -  |  -  |  -  |

COVERAGE SCORE: [N]/4 personas ([%])

UNMATCHED CONTACTS (in HubSpot but don't fit a key persona)
| Name | Title | Email | Last Contacted |
|------|-------|-------|----------------|

RECOMMENDED ACTION:
[If gaps exist]: Search Apollo for [specific titles] at [company]
[If well-covered]: Ready for multi-threaded outreach
```

---

### MODE 2: APOLLO PROSPECTING (Find New Contacts)
**Trigger:** "Find contacts at [company]" or "Who should we reach out to at [company]?" or "Prospect for contacts"

**Steps:**

1. First, run Mode 1 to understand existing HubSpot coverage
2. Identify persona gaps from the coverage map
3. For each gap, search Apollo for matching job titles at the company
4. Filter for current employees (not former)
5. Prioritize by seniority (director/VP preferred)
6. Deduplicate against existing HubSpot contacts

**Output:**
```
APOLLO PROSPECTING RESULTS: [Company Name]
=============================================
Segment: [segment] | Coverage Gaps: [personas]

[Persona]: [Title]
- Name: [name]
- Email: [email]
- LinkedIn: [URL]
- Current Status: [active/inactive]

[Next Persona]: [Title]
...

ACTION:
- Add to HubSpot and assign to rep
- Add to sequence (if applicable)
```

---

---

### MODE 3: APOLLO + LINKEDIN HYBRID FILL (Guardian Mode)
**Trigger:** "Fill persona gaps" or when CRM Guardian Job 5 runs

**Approach:** Hybrid  -  Apollo for programmatic search, LinkedIn for validation. Apollo's direct search can return stale/wrong contacts. LinkedIn profiles are self-maintained and more accurate. Use Apollo to find candidates, then validate against LinkedIn before creating.

**Tools required:** Apollo MCP + HubSpot MCP

**Steps:**

1. Pull target companies (Tier 1/2 from HubSpot where `account_tier` = `tier_1` or `tier_2`). Also pull `signal_heat` for each (Title Case enum: `Hot` / `Warm` / `Cool` / `Cold`). **Rank companies for persona-fill priority by `signal_heat` first, then `account_tier`**: `Hot` before `Warm` before `Cool` before `Cold`; within each heat bucket, Tier 1 before Tier 2. Apollo budget hits the highest-intent accounts first. `Cold` Tier 1 accounts still get filled, they just queue behind `Hot` accounts.
2. For each company, run Mode 1 (HubSpot contact audit) to identify persona gaps
3. For each persona gap:

   a. **Apollo search:** Search by company domain + segment-specific titles (from persona table above) + VP/Director/C-Suite seniority. Filter: current employees only, verified email only. Skip unverified, unknown, or invalid email statuses.

   b. **LinkedIn validation (if Apollo returns `linkedin_url`):**
      - `web_fetch` the LinkedIn public profile URL
      - **Company match check:** Verify the person's current company on LinkedIn matches the target account. If mismatch → skip this candidate (likely stale Apollo data), try next Apollo result.
      - **Title correction:** Use LinkedIn's current title as source of truth over Apollo's title. If LinkedIn says "SVP, Network Engineering" but Apollo says "VP Engineering", use LinkedIn's version for `jobtitle`.

   c. **Create or flag:**
      - **LinkedIn validated** (company matches + verified email): Auto-create contact in HubSpot:
        - `firstname`, `lastname`, `email`, `phone` from Apollo
        - `jobtitle` from LinkedIn (source of truth, corrected)
        - `linkedin_url` from Apollo
        - `lifecyclestage` = `lead`
        - `hubspot_owner_id` = company owner (inherited)
        - `customer_segment` = company segment (inherited)
        - `company` = company name
        - `hs_marketable_status` = `"false"` (non-marketing - MANDATORY default for every auto-created contact; prevents silent inflation of the paid marketing contact tier)
      - **Apollo data only** (no LinkedIn URL from Apollo): Auto-create with Apollo data + `hs_marketable_status = "false"`. Flag in the daily email report as `LinkedIn unverified - Apollo data only` so Cooper can spot-check. No HubSpot note is created.
      - **LinkedIn shows different company:** Skip this candidate. Try next Apollo result.
      - **When running under CRM Guardian:** The Guardian's safety tier system and deal protection rule apply. See crm-guardian skill for the authoritative tier definitions.

   d. **Flag remaining gaps for reps:** If Apollo couldn't find a verified match for a persona gap (no results, all failed LinkedIn validation, or no verified email):
      ```
      ACTION NEEDED: [Company Name]  -  missing [Persona]
      Suggested LinkedIn search: Go to [company] LinkedIn page → People → filter by [title keywords from persona table]
      Then: Apollo extension → verify email → add to HubSpot
      Owner: [rep name]
      ```

4. Deduplicate all Apollo results against existing HubSpot contacts by email before creating

5. **Opt-out / suppression check (MANDATORY before creating any contact):**

   Before any Apollo contact is created in HubSpot, check the proposed email against suppression signals. Use HubSpot MCP `search_crm_objects` on CONTACT filtered by the proposed email. If a match exists with any of the following, DO NOT create and DO NOT re-prospect:
   - `hs_email_optout = true` (global opt-out)
   - `hs_email_hard_bounced = true` (hard-bounced; emailing again damages sender reputation)
   - `flagged_for_deletion = true` (explicitly flagged by an earlier Guardian run  -  recreating defeats the purpose)
   - `hs_lifecyclestage_other_date` indicates previously unsubscribed lifecycle
   - Contact exists with a HubSpot note containing `suppressed`, `unsubscribe`, or `do not contact`

   If a suppression match is found, log as a skipped candidate in the run report: `SUPPRESSED: [email] at [company]  -  reason: [signal]`. Surface to Cooper so he can verify the suppression is intentional (occasionally the signal is stale).

   This check also applies to Apollo-returned emails that do NOT yet exist in HubSpot: if Apollo's record shows `status = opted_out` or `email_status = unsubscribed`, skip that candidate.

**Output:**
```
PERSONA GAP FILL REPORT  -  [Date]
===================================

CONTACTS AUTO-CREATED (LinkedIn validated)
| Company | Contact | Title (from LinkedIn) | Email | Persona |
|---------|---------|----------------------|-------|---------|

CONTACTS AUTO-CREATED (Apollo only  -  LinkedIn unverified)
| Company | Contact | Title | Email | Persona |
|---------|---------|-------|-------|---------|

DEAL-PROTECTED (flagged, not created  -  account has open deal)
| Company | Contact | Title | Email | Deal Name |
|---------|---------|-------|-------|-----------|

GAPS FLAGGED FOR REPS (Apollo couldn't fill)
| Company | Missing Persona | Suggested Titles | Owner |
|---------|-----------------|------------------|-------|

SUMMARY: [N] companies audited, [N] gaps found, [N] auto-created (LinkedIn), [N] auto-created (Apollo only), [N] flagged for reps
```

---

### MODE 4: JOB CHANGE DETECTION
**Trigger:** "Check for job changes" or "Contact audit" or when CRM Guardian Job 6 runs

**Tools required:** Apollo MCP + HubSpot MCP

**Steps:**

1. Pull contacts at Tier 1/2 accounts AND contacts at accounts with open deals
2. For each contact with an email address:

   a. **Apollo check:** Search Apollo by email to check current employment status

   b. **LinkedIn cross-check:** If Apollo returns a LinkedIn URL and the contact's employment status is uncertain, `web_fetch` the LinkedIn profile to verify current company

   c. If contact is confirmed no longer at the associated company (Apollo shows different company OR LinkedIn shows different company):
      - Surface the departure in the daily email report with: contact name, former company, detected departure date, Apollo's reported current role, LinkedIn's reported current company/title. The old contact record remains in HubSpot unchanged (the rep may still want to reach out via a different channel); the report is the audit trail. No HubSpot note is written on the contact record.
      - **Find replacement:** Search Apollo for same persona (based on original contact's title mapping to persona table), same company, current employee, verified email
      - **LinkedIn validate replacement:** If Apollo returns a LinkedIn URL for the replacement, `web_fetch` to confirm company match + get accurate title
      - **Opt-out / suppression check (MANDATORY):** Before creating the replacement, apply the same suppression check as Mode 3 step 5. Check the proposed email against HubSpot for any existing record with `hs_email_optout = true`, `hs_email_hard_bounced = true`, `flagged_for_deletion = true`, or suppression notes. Also check Apollo's own opt-out status on the returned email. If suppressed: do not create, log as skipped candidate, flag the persona gap for the rep instead.
      - If validated replacement found AND no suppression hits → auto-create in HubSpot with LinkedIn-corrected title. Set `hs_marketable_status = "false"` (non-marketing default for every auto-created contact).
      - If replacement found but no LinkedIn URL → auto-create with Apollo data + `hs_marketable_status = "false"`. Flag in the run report as `LinkedIn unverified - Apollo data only`.
      - If no replacement found → flag for rep:
        ```
        ACTION NEEDED: [Company]  -  [contact name] departed, [Persona] gap
        Suggested LinkedIn search: Go to [company] LinkedIn page → People → filter by [title keywords]
        Then: Apollo extension → verify email → add to HubSpot
        Owner: [rep name]
        ```
      - **When running under CRM Guardian:** The Guardian's safety tier system and deal protection rule apply. See crm-guardian skill for the authoritative tier definitions.

**Output:**
```
JOB CHANGE DETECTION REPORT  -  [Date]
=======================================

DEPARTURES DETECTED
| Contact | Former Company | Persona | Now At | Source |
|---------|---------------|---------|--------|--------|

REPLACEMENTS AUTO-CREATED
| Company | New Contact | Title | Email | Replaced | Validated |
|---------|-------------|-------|-------|----------|-----------|

GAPS FLAGGED FOR REPS (no replacement found)
| Company | Departed Contact | Persona | Owner |
|---------|-----------------|---------|-------|

DEAL-PROTECTED (replacement flagged, not created)
| Company | New Contact | Deal Name |
|---------|-------------|-----------|

SUMMARY: [N] contacts checked, [N] departures, [N] replacements created, [N] gaps flagged
```

---

### MODE 5: BULK PERSONA COVERAGE REPORT
**Trigger:** "Persona coverage report" or "How are our accounts covered?" or "Contact coverage"

**Steps:**

1. Pull all Tier 1/2 companies from HubSpot
2. For each company, run Mode 1 (HubSpot contact audit)
3. Produce aggregate report

**Output:**
```
PERSONA COVERAGE REPORT  -  [Date]
===================================

COVERAGE BY TIER
| Tier | Accounts | Avg Personas | 3+ Personas | Gaps |
|------|----------|-------------|-------------|------|

COVERAGE BY SEGMENT
| Segment | Accounts | Avg Personas | Most Common Gap |
|---------|----------|-------------|-----------------|

PERSONA GAP HEAT MAP
| Persona | Missing At | % of Accounts |
|---------|-----------|---------------|
| Technical Champion | [N] | [X]% |
| Business Sponsor | [N] | [X]% |
| Economic Buyer | [N] | [X]% |
| Procurement | [N] | [X]% |

PRIORITY: Tier 1 accounts with open deals and <2 contacts
| Company | Contacts | Missing Personas | Deal | Owner |
|---------|----------|------------------|------|-------|
```

---

## When to Use This Skill

Trigger on any of these patterns:
- "Who do we have at [company]?" or "Map contacts"
- "Find contacts at [company]" or "Prospect for [title] at [company]"
- "Who should we reach out to at [company]?"
- "Do we have coverage at [company]?" or "Contact gaps at [company]"
- "Is [company] ready for multi-threaded outreach?" or "Who's the economic buyer?"
- "Check contact coverage" or "Audit our contacts"
- "Fill persona gaps" or "Find missing contacts" or "Apollo search"
- "Check for job changes" or "Has anyone left?"
- "Persona coverage report" or "How are our accounts covered?"
- Any mention of: contact map, buying committee, persona coverage, contact gaps, multi-threading, job changes, Apollo, LinkedIn validation

---

## Skill Chain

- **Reads from:** HubSpot (existing contacts + company associations), Apollo (prospecting)
- **Outputs to:** HubSpot (new contacts created with persona mapping)
- **Feeds into:** sdr-pipeline, cold-email (newly discovered contacts become outreach targets)

