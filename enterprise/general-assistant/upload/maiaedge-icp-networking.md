---
name: icp-networking
description: >
  Use when asked to "build a LinkedIn target list", "find people to connect with on LinkedIn",
  "network into ICP accounts", "grow my LinkedIn network in target accounts", "run a networking
  batch", or any task involving strategic LinkedIn connection building at MaiaEdge ICP accounts.
version: 2.0.0
---

# ICP LinkedIn Networking Strategy

Strategic peer networking in MaiaEdge ICP accounts. Brand exposure and relationship building, not sales outreach. Cooper Kennedy connects as a RevOps/GTM systems peer.

## Sender Profile

- **Name:** Cooper Kennedy
- **Title:** RevOps at MaiaEdge
- **LinkedIn:** https://www.linkedin.com/in/cooperkennedy/
- **Positioning:** GTM infrastructure and systems peer. Connects on operational common ground.

---

## Workflow (Single Pass)

One command (`/build-targets`) does everything:

1. Pull target companies from HubSpot by segment priority
2. Check activity gate (skip accounts with active conversations)
3. While sourcing, flag any segment misclassifications
4. Search LinkedIn People Search for target titles at those companies
5. Navigate to profiles, send bare connection requests (max 20)
6. After connections: Apollo enrich contacts (verified email + LinkedIn URL). Apollo-HubSpot sync handles contact creation automatically.
7. Output: connection results XLSX + misclassification flags XLSX
8. If misclassifications flagged, ask Cooper to approve corrections and update HubSpot segments

Standalone `/connect-batch` re-runs connections from an existing list without re-sourcing.

---

## Segment Priority

Target companies in this order. Only target companies already in HubSpot (networking into known accounts has direct strategic value).

| Priority | Segment | HubSpot `customer_segment` Value |
|----------|---------|----------------------------------|
| 1 | Neocloud | `NeoCloud` |
| 2 | Colocation | `Data Center Colo Provider` |
| 3 | Network Operator | `Network Operator(Tier 1 / VNO)` |
| 3 | Fiber Operator | `Fiber Operator` |

**Do not target:** MSP/Aggregators (`Enterprise`), pure IT MSPs, enterprise consumers, residential ISPs, tower REITs, resellers/VARs.

**CoreWeave exclusion:** NOT an active target (MetroConnect partnership, Feb 2026).

---

## Target Titles

Prioritize GTM/RevOps peers, then infrastructure leadership, then partnerships.

### Primary (GTM and Revenue Operations -- peer networking)
- VP Revenue Operations, Director RevOps
- Head of Sales Operations, VP Sales Ops
- Director of GTM Strategy, VP GTM
- Chief Revenue Officer, CRO
- Chief Commercial Officer, CCO
- VP Sales, Head of Sales, SVP Sales

### Secondary (Infrastructure and Platform)
- VP Infrastructure, Director of Infrastructure
- Head of Platform Engineering, VP Platform
- VP AI Operations, Director AI Ops
- VP Data Center Operations
- Chief Data Officer, VP Data

### Tertiary (Partnerships and BD)
- VP Partnerships, Director of Partnerships
- VP Business Development, Director BD
- VP Strategic Alliances
- Head of Channel, VP Channel Sales

### Seniority Filter
VP, Director, C-Suite, Head-of, Owner/Founder only. Skip ICs and managers unless the company is very small (<50 employees).

### LinkedIn People Search URL Pattern
```
https://www.linkedin.com/search/results/people/?keywords=%22{CompanyName}%22&titleFreeText=VP%20OR%20Director%20OR%20Chief%20OR%20Head%20OR%20CRO%20OR%20CCO
```
Quote the company name in keywords for accuracy. If the company page is unavailable, this keyword approach reliably surfaces employees.

---

## Activity Gate

Before targeting a company, check its last activity date in HubSpot.

| Last Activity | Action |
|--------------|--------|
| Within 14 days | SKIP. Active conversation in progress. |
| 15-30 days | PROCEED with caution. Note in the log. |
| 31+ days | CLEAR. Good networking target. |

Check HubSpot fields: `notes_last_contacted`, `hs_last_sales_activity_timestamp`.

**Cross-skill reference:** Read the `sdr-pipeline` skill for full activity gate logic.

---

## Misclassification Detection

While reviewing companies from HubSpot, flag records where `customer_segment` does not match observable evidence:

- Retail ISP labeled as Fiber Operator (no wholesale/enterprise services)
- Enterprise consumer labeled as Network Operator (buys, doesn't sell)
- IT MSP labeled as MSP/Aggregator (no carrier aggregation)
- Neocloud labeled as Data Center Colo Provider (sells GPU compute, not rack space)
- Segment blank or wrong

Do NOT auto-correct in HubSpot. Log flags for Cooper to review. Include: company name, current segment, recommended segment, evidence, action needed.

**Cross-skill reference:** Read the `edge-case-researcher` skill for 7 edge case rules. Read the `import-processor` skill for correct HubSpot segment values.

---

## LinkedIn Connection Protocol

- **No note.** Bare connection request only.
- **No message after connecting.**
- **Rate limit:** Maximum 20 connections per session.
- **Spacing:** Wait 3-5 seconds between requests.
- **Navigate directly** to profile URLs (avoids search overlay interference).

### Chrome Steps
1. Navigate to profile URL
2. Wait 2-3 seconds for page load
3. `find` the "Connect" button
4. Click the Connect button ref
5. If modal appears, `find` "Send without a note" and click it
6. If "More" dropdown needed: click More, find Connect, click, then Send without a note
7. If already connected/pending/follow-only: skip and log
8. Wait 4-5 seconds before next profile

### Stop Conditions
- Weekly invitation limit: STOP immediately
- CAPTCHA: STOP, alert Cooper
- Chrome unresponsive: pause, alert Cooper

---

## Post-Connection: Apollo Enrichment

After all connections are sent, enrich each contact via Apollo. The Apollo-HubSpot sync automatically creates the contact in HubSpot, so no manual HubSpot push is needed.

1. Use `apollo_people_match` with the person's LinkedIn URL
2. Extract: first name, last name, title, email, email_status
3. Only keep email if `email_status = "verified"`. Skip guessed/unavailable.
4. Create in Apollo with `apollo_contacts_create` (`run_dedupe: true`)
5. Apollo-HubSpot sync handles the rest (contact creation, company association)

If Apollo match fails for a contact, log it. The contact can be manually added or enriched later.

**Cross-skill reference:** Read the `contact-discovery` skill for Apollo API patterns and credit notes.

---

## Misclassification Corrections (HubSpot)

The only direct HubSpot writes this plugin makes are segment corrections on company records, and only after Cooper approves.

After presenting misclassification flags, if Cooper approves a correction:
1. Update the company's `customer_segment` using exact HubSpot values:
   - Colocation -> `Data Center Colo Provider`
   - Neocloud -> `NeoCloud`
   - Fiber Operator -> `Fiber Operator`
   - Network Operator -> `Network Operator(Tier 1 / VNO)`
2. Update `customer_sub_segment` if applicable
3. Log the change

**Cross-skill reference:** Read the `import-processor` skill for exact HubSpot enum values.

---

## Output Files

### `linkedin-results-{date}.xlsx`
All connections with enrichment results:
| # | First Name | Last Name | Title | Company | Segment | LinkedIn URL | Connection Status | Email | Email Status | Apollo Status |

Summary section: segment distribution, date, totals.

### `misclassification-flags-{date}.xlsx` (if any found)
| Company | Domain | Current Segment | Recommended Segment | Evidence | Action Needed |

---

## Cross-Skill Reference Map

This plugin reads existing MaiaEdge skills at runtime for domain logic. Strategy changes in the source skill cascade automatically.

| Need | Skill to Read |
|------|--------------|
| HubSpot search patterns | `account-sourcing` |
| Segment classification rules | `company-enrichment` or `segment-classification` |
| Misclassification detection | `edge-case-researcher` |
| HubSpot property values | `import-processor` |
| Contact persona mapping | `contact-discovery` |
| Apollo enrichment patterns | `contact-discovery` |
| Activity gate thresholds | `sdr-pipeline` |
| Target company lists | `references/target-companies.md` |

Skills live in:
- `/sessions/cool-great-tesla/mnt/.skills/skills/{skill-name}/SKILL.md`
- `/sessions/cool-great-tesla/mnt/.local-plugins/marketplaces/local-desktop-app-uploads/{plugin-name}/skills/{skill-name}/SKILL.md`
