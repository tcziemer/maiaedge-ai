---
description: Source companies from HubSpot, find people on LinkedIn, connect, enrich, and push to CRM
allowed-tools: Read, Write, Bash, Grep, Glob, Agent, WebSearch, WebFetch, TodoWrite
argument-hint: "[segment] [count]"
---

Main command. Pulls target companies from HubSpot, finds contacts on LinkedIn, sends connection requests, enriches each contact via Apollo, and pushes them into HubSpot. Flags misclassified segments along the way.

Read the `icp-networking` skill first for full context. Then read `references/cross-skill-map.md` to know which existing skills to consult.

## Inputs

- **Segment filter:** $1 (default: "neocloud,colocation". Valid: neocloud, colocation, network, fiber, all)
- **Target count:** $2 (default: 20 connection requests)

---

## STEP 1: Source Target Companies from HubSpot

Search HubSpot companies by `customer_segment`:
- Neocloud: filter `customer_segment` = `NeoCloud`
- Colocation: filter `customer_segment` = `Data Center Colo Provider`
- Network Operator: filter `customer_segment` = `Network Operator(Tier 1 / VNO)`
- Fiber Operator: filter `customer_segment` = `Fiber Operator`

Pull these fields for each company:
`name`, `domain`, `customer_segment`, `customer_sub_segment`, `hubspot_owner_id`, `notes_last_contacted`, `hs_last_sales_activity_timestamp`, `account_tier`, `state`, `country`, `hs_object_id`

**Cross-skill reference:** Read the `account-sourcing` skill if you need HubSpot search pattern guidance.

### Activity Gate

For each company, check last activity:
- Within 14 days of today: SKIP (active conversation)
- 15-30 days: include but flag as "caution" in the log
- 31+ days or never contacted: CLEAR

### Prioritize

Sort the companies:
1. Segment priority: Neocloud > Colocation > Network/Fiber
2. Account tier: Tier 1 > Tier 2 > Tier 3 > untiered
3. Staleness: longest since last activity first

Select enough companies to yield ~20 contacts (typically 8-12 companies, 1-3 contacts each).

---

## STEP 2: Validate Segments and Flag Misclassifications

While reviewing HubSpot data, check if each company's `customer_segment` matches what you know or can quickly verify:
- Does the company name/domain match the stored segment?
- Is the sub-segment populated and correct?
- Has the company pivoted, been acquired, or changed since enrichment?

If something looks off, add it to the misclassification flags list. Do NOT correct HubSpot yet. Include:
- Company name, domain
- Current HubSpot segment
- What it should be (with brief evidence)
- Action needed: "Update segment", "Update sub-segment", "Remove from ICP", "Needs research"

**Cross-skill reference:** Read the `edge-case-researcher` skill for the 7 misclassification rules.

---

## STEP 3: Search LinkedIn for Contacts

For each target company:

1. Navigate to LinkedIn People Search:
   ```
   https://www.linkedin.com/search/results/people/?keywords=%22{CompanyName}%22&titleFreeText=VP%20OR%20Director%20OR%20Chief%20OR%20Head%20OR%20CRO%20OR%20CCO
   ```

2. Review the first page of results. Select 1-3 contacts per company matching the target title list from the skill:
   - Priority 1: GTM/RevOps titles (peer networking)
   - Priority 2: Infrastructure/platform titles
   - Priority 3: Partnerships/BD titles

3. For each selected contact, capture: first name, last name, title, company, LinkedIn profile URL.

4. Prefer people with 2nd-degree connections (Connect button visible).

**Company name issues:** If the company name is too generic (e.g., "Switch", "Modal") or returns wrong results:
- Try the company name + a distinguishing term: "Switch data center", "Modal cloud GPU"
- Try the domain name instead of the company name
- If still no good results, skip and move to the next company

Build up the list until you have ~20 contacts total.

---

## STEP 4: Send Connection Requests

For each contact in the list:

1. Navigate directly to their LinkedIn profile URL
2. Wait 2-3 seconds for page load
3. Use `find` tool to locate "Connect" button
4. Click the Connect button ref
5. If modal appears: `find` "Send without a note", click it
6. If "More" dropdown needed: click More, find Connect, click, then find "Send without a note", click
7. If already connected / pending / follow-only: skip, log status
8. Wait 4-5 seconds before next profile

**Stop conditions:**
- Weekly invitation limit message: STOP immediately, report count
- CAPTCHA: STOP, alert Cooper
- Chrome unresponsive: pause, alert Cooper

Log each result: name, company, title, LinkedIn URL, status (Sent / Already Connected / Pending / Follow Only / Error).

---

## STEP 5: Apollo Enrichment

For every contact where a connection was successfully sent (status = "Sent"):

1. Call `apollo_people_match` with the contact's LinkedIn URL
2. Extract: first_name, last_name, title, email, email_status, organization_name
3. Email rule: ONLY keep the email if `email_status = "verified"`. If guessed or unavailable, discard email.
4. Call `apollo_contacts_create` with the enriched data and `run_dedupe: true`
5. Apollo-HubSpot sync handles contact creation in HubSpot automatically. No manual HubSpot push needed.

If Apollo match fails for a contact, log it and move on. The contact can be enriched later.

**Cross-skill reference:** Read the `contact-discovery` skill for Apollo API patterns and credit notes.

---

## STEP 6: Output

### File 1: `linkedin-results-{date}.xlsx`

| # | First Name | Last Name | Title | Company | Segment | LinkedIn URL | Connection Status | Email | Email Status | Apollo Status |

Summary section at bottom:
- Segment distribution (X Neocloud, X Colo, X Network/Fiber)
- Connection totals (X sent, X skipped, X errors)
- Enrichment totals (X with verified email, X no verified email, X Apollo failed)
- Date

### File 2: `misclassification-flags-{date}.xlsx` (only if flags were found)

| Company | Domain | HubSpot ID | Current Segment | Recommended Segment | Evidence | Action Needed |

### Present Results to Cooper

Show:
1. Connection summary (X sent, X skipped)
2. Enrichment summary (X with verified email, X without, X failed)
3. Misclassification flags (if any) with recommended corrections
4. Links to output files

If misclassification flags exist, ask Cooper to approve or reject each correction. For approved corrections, update the company's `customer_segment` in HubSpot using exact values:
- Colocation -> `Data Center Colo Provider`
- Neocloud -> `NeoCloud`
- Fiber Operator -> `Fiber Operator`
- Network Operator -> `Network Operator(Tier 1 / VNO)`

**Cross-skill reference:** Read the `import-processor` skill for exact HubSpot enum values.

---

## Notes

- Target count is CONNECTION REQUESTS, not companies. Source enough companies to fill the count.
- Default to neocloud + colocation for first runs. Add network/fiber in later batches.
- If HubSpot has fewer companies in a segment than expected, note it but do NOT fall back to web search. This plugin networks into known CRM accounts only.
- Update `references/target-companies.md` after each run with connected/pending contacts to avoid duplicates next time.
