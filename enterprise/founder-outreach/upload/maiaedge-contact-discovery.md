---
name: contact-discovery
description: "MaiaEdge contact discovery strategist. Finds the right people at target accounts and audits existing contact coverage. Use when asked to find contacts, prospect for contacts, identify contact gaps, map buying committee, check contact coverage, discover personas, or evaluate who to reach out to at a company. Operates in two modes: (1) HubSpot contact map audit showing persona coverage gaps by segment, (2) Apollo prospecting to find specific titles based on coverage gaps. Understands MaiaEdge buying committee by segment (Technical Champion, Business Sponsor, Economic Buyer, Procurement) and flags missing personas. Multi-threaded outreach ready."
---

# MaiaEdge Contact Discovery

## Purpose

Find the right people at target accounts and identify gaps in contact coverage. This skill combines two capabilities: searching Apollo for new contacts to prospect, and auditing existing HubSpot contacts to assess coverage quality. The goal is to make sure every target account has the right mix of personas engaged — not just one name in the CRM.

MaiaEdge sells infrastructure technology, so the buying committee typically involves network engineering, infrastructure/IT leadership, product/strategy, and procurement. Missing any of these personas means deals can stall without warning.

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
| Business Sponsor | ❌ Gap | — | — | — |
| Economic Buyer | ❌ Gap | — | — | — |
| Procurement | ⚠️ Optional | — | — | — |

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

## When to Use This Skill

Trigger on any of these patterns:
- "Who do we have at [company]?" or "Map contacts"
- "Find contacts at [company]" or "Prospect for [title] at [company]"
- "Who should we reach out to at [company]?"
- "Do we have coverage at [company]?" or "Contact gaps at [company]"
- "Is [company] ready for multi-threaded outreach?" or "Who's the economic buyer?"
- "Check contact coverage" or "Audit our contacts"
- Any mention of: contact map, buying committee, persona coverage, contact gaps, multi-threading

