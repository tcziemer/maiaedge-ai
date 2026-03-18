---
name: maiaedge-sdr-pipeline
description: "End-to-end MaiaEdge SDR pipeline. Takes a list of companies + contact titles, pulls all intel from HubSpot first (account briefs, contacts, activity, segment), fills gaps with web search and Apollo, verifies segments, checks for active conversations, writes personalized 3-email sequences + LinkedIn, and outputs a Smartlead-ready XLSX + review file. Use when asked to run outreach, process a batch, write emails for a list, prepare a Smartlead import, or do cold outreach for multiple companies. Also trigger when the user provides a list of company names with titles/roles and wants emails written. This skill is the primary workflow for turning a prospect list into send-ready outreach."
---

# MaiaEdge SDR Pipeline

Turn a list of companies + contacts into verified, personalized, send-ready outreach with a Smartlead XLSX and review file.

## What This Skill Does

This is the complete pipeline. User gives you companies and contacts. You produce emails that sound like a smart industry peer wrote them after spending real time learning about the business. These go to C-level and VP-level executives at infrastructure companies. Every claim must be verifiable. Every email must be unique to that person.

**Stack:** HubSpot (CRM) → Apollo (contact enrichment) → This pipeline (research + writing) → Smartlead (sending)

## Input Format

The user will provide some combination of:
- Company names (always)
- Contact titles/roles they want to target (always)
- ICP segment (usually)
- Contact emails (usually — they verify emails before sending)
- Contact/company LinkedIn URLs (sometimes)
- Sender preference: Tim Lieto or Ken Cunningham (ask if not specified)

The user will NOT always provide domains, emails, or LinkedIn URLs. Part of your job is to pull those from HubSpot and fill gaps.

## Before You Start

1. **Confirm sender.** Tim Lieto (AVP, North America Sales, West/Central/National) or Ken Cunningham (Sales, East Region). Ask once for the whole batch unless specified per-contact.

2. **Check Apollo credits.** Run `apollo_users_api_profile` with `include_credit_usage: true`. Report remaining credits. Each contact enrichment costs credits. Estimate consumption for the batch and confirm before proceeding.

3. **Read messaging references.** Before writing any emails, read these reference files:
   - `references/messaging-framework.md` — Segment-specific messaging, tone, writing rules
   - `references/email-writing-rules.md` — Email structure, CTAs, quality checklist, banned phrases
   - `references/hubspot-values.md` — Exact HubSpot property values for segment/sub-segment

---

## The Pipeline (Per Contact)

Process contacts sequentially. Complete one fully before starting the next. Never reuse research across different companies (contacts at the SAME company share company research but get individual contact research and unique emails).

### Step 1: HubSpot Deep Pull

**Company search** — Use `search_crm_objects` (objectType: companies). Search by name AND domain if provided. Pull:

```
name, domain, linkedin_company_page, website,
account_brief, recent_news_or_trigger_event,
customer_segment, customer_sub_segment, segmentation_confidence,
account_tier, description, about_us, linkedinbio, opportunity_description,
state, city, country,
hubspot_owner_id, annualrevenue, numberofemployees,
notes_last_contacted, notes_last_updated, num_contacted_notes
```

**Contact search** — Search contacts by name + company association, or by email if provided. Pull:

```
email, firstname, lastname, jobtitle,
hs_linkedin_url, linkedin_account,
phone, mobilephone,
notes_last_contacted, notes_last_updated, num_contacted_notes,
linked_in_message,
hs_sequences_is_enrolled, hs_latest_sequence_enrolled,
hs_sequences_enrolled_count,
hs_lead_status
```

**Record what you found and what's missing.** Every field gets a source tag:
- `[HS]` — From HubSpot
- `[Apollo]` — From Apollo enrichment (note verified/unverified)
- `[Web]` — From web search
- `[User]` — Provided by user in the input
- `[Missing]` — Not found anywhere. Flag for user.

### Step 2: Activity Gate (MANDATORY — Do Not Skip)

Check for active conversations before proceeding. This prevents tone-deaf outreach.

**Contact-level checks:**

| Field | Threshold | Action |
|---|---|---|
| `notes_last_contacted` within 14 days | **STOP** | Flag: "ACTIVE CONVERSATION. Last contacted [date]. Skipping unless overridden." |
| `notes_last_contacted` 15-30 days | **WARNING** | Flag: "Recent activity [date]. Check with rep before sending." |
| `notes_last_contacted` 31-60 days | **CAUTION** | Note in summary. Consider referencing prior conversation. |
| `hs_sequences_is_enrolled` = true | **STOP** | Flag: "CURRENTLY IN HUBSPOT SEQUENCE [name]. Do not add to Smartlead." |
| `hs_lead_status` = "Connected" or "Open Deal" | **STOP** | Flag: "Lead status is [status]. Active relationship. Skip cold outreach." |
| `hs_lead_status` = "Attempted to Contact" | **CAUTION** | Prior outreach attempted. Don't repeat same angle. |
| `num_contacted_notes` > 10 | **WARNING** | "Contacted 10+ times. Email must be significantly differentiated." |
| `linked_in_message` populated | **CAUTION** | LinkedIn already sent. Don't duplicate. |

**Company-level checks:**

| Field | Threshold | Action |
|---|---|---|
| `notes_last_contacted` within 14 days | **WARNING** | "Company has recent activity. Check if another contact is in active conversation." |
| `num_contacted_notes` > 15 | **WARNING** | "Company contacted 15+ times across contacts. Verify we're not oversaturating." |

If a contact is STOPPED, skip to the next contact. Report the stop reason in the final output.

**Territory check (also mandatory):**
After determining the company's HQ state (from HubSpot `state` field or research), check the territory model. If the user-specified sender does NOT match the territory owner for that state, FLAG it clearly:

> "TERRITORY NOTE: [Company] HQ is in [State], which is [Territory Owner]'s territory. User specified [Sender] as sender. Proceeding with user's choice but flagging for awareness."

This is informational, not a STOP. The user may be doing a cross-territory play intentionally. But they need to see it.

### Step 3: Read the Account Brief

If `account_brief` has content, read it. This is the primary research foundation — someone has already done research on this company.

**But do not trust it blindly.** The brief may be stale (company acquired, pivoted, expanded). You will verify it in Step 4.

If `account_brief` is empty, that's fine. Step 4 will do full research.

### Step 4: Web Research — Verify + Supplement

**Always run these regardless of whether a brief exists:**

1. `[Company] recent news 2025 2026` — Verify brief is current. Look for: acquisitions, pivots, rebrand, leadership change, expansion, funding.
2. Segment-specific research route (see `references/research-routes.md` pattern):
   - Colo: `[Company] data center facilities locations` + `[Company] CoreWeave Lambda Labs Crusoe GPU liquid cooling`
   - Fiber: `[Company] fiber route miles network states` + `[Company] Megaport PacketFabric NaaS`
   - Network Op: `[Company] customer portal API self-service provisioning`
   - MSP: `[Company] managed services carrier aggregation multi-carrier`
   - Neocloud: `[Company] GPU cloud infrastructure facilities` + `[Company] expansion funding 2025 2026`

3. **Timing signal searches** (always run at least one):
   - `[Company] funding round 2025 2026`
   - `[Company] expansion new market acquisition 2025 2026`
   - `[Company] partnership announcement 2025 2026`

4. **Contact-specific search:**
   - `[Contact Name] [Company] LinkedIn` — background, recent posts, role changes

**What you're extracting:**
- Verification that the account brief is still accurate
- Timing signals (funding, expansion, partnership, leadership change)
- Company-specific details for email personalization (facility count, route miles, branded products, named customers, recent wins)
- Contact background for role-appropriate framing
- AI signals for colos (GPU tenants, liquid cooling, AI-ready marketing)

### Step 5: Fill Gaps with Apollo

If HubSpot is missing email, LinkedIn, or phone for a contact:

1. Use `apollo_people_match` with first_name, last_name, domain (or organization_name).
2. **Only use verified emails.** If Apollo returns an email with unverified status, flag it: `[Apollo-Unverified] DO NOT SEND without manual verification.`
3. Tag the source: `email: pjanes@radius-dc.com [Apollo-Verified]`

**Priority order for emails:**
1. User-provided email → trusted (user said they verify)
2. HubSpot email → trusted
3. Apollo verified → safe to send
4. Apollo unverified → FLAG, exclude from Smartlead unless user overrides
5. Web search → FLAG, exclude from Smartlead unless user overrides

### Step 6: Verify Segment

After research, verify the HubSpot `customer_segment` and `customer_sub_segment` match reality.

**Check:**
- Does the segment match what you found? (e.g., classified as "Data Center Colo Provider" but research shows they're actually a fiber operator)
- For colos: Did you find AI signals? If strong → sub-segment should be "AI Infrastructure" not "Standard"
- For network operators: Did you find portal/API evidence? Track A vs Track B.
- Is this company actually on the exclusion list? (IXP, Tower REIT, IT MSP, software vendor, etc.)

**If mismatch:** Flag: `SEGMENT MISMATCH: HubSpot says [X], research says [Y]. Using [Y] for messaging.`
**If confirmed:** Note: `Segment verified: [segment] / [sub-segment]`

Use the CORRECT segment for all email writing, regardless of what HubSpot says.

### Step 7: Angle Selection (MANDATORY — Do Not Skip)

After all research is complete (HubSpot pull, web research, Apollo enrichment, segment verification), STOP and answer one question before writing anything:

**"What is the ONE thing happening at this company right now that creates an urgent, MaiaEdge-relevant problem?"**

This could be: an acquisition they need to integrate, a new build they need to monetize, a market expansion that multiplies operational complexity, a competitive threat that changes their timeline, a technology migration that creates a window. Whatever is most specific and most urgent.

**State the angle in one sentence using this format:**
`"[Company] is [doing X], which means [specific operational problem MaiaEdge solves]."`

**Examples of good angles:**
- "Zayo is integrating Crown Castle's 90,000 acquired route miles into their existing 130K-mile network, which means different provisioning systems at every new domain boundary and enterprise revenue waiting on operational unification."
- "GIX Fiber just completed a dark fiber crossing under the Hudson River and now needs to monetize it, which means manual provisioning for every carrier and enterprise connection at each interconnection point, with overhead that scales faster than revenue."
- "Light Source Communications is building dark fiber across four metros simultaneously with a 500-mile intercity route on the horizon, which means the gap between 'fiber complete' and 'service live' is the bottleneck, and hyperscaler anchors expect activation speed manual NNI provisioning can't deliver."
- "Crosslake Fibre sells ultra-low-latency subsea connectivity for financial trading, but provisioning across landing station partners still takes weeks, which means their provisioning timeline undercuts their speed value proposition."

**Examples of bad angles (segment template restatements — NEVER use these):**
- "Zayo is a network operator, so talk about cross-carrier provisioning." (This is just the segment template.)
- "Crosslake is a fiber operator with subsea routes, so talk about NNI provisioning speed." (Generic segment pain, not company-specific.)

**The key rule:** If you can't identify a company-specific angle from the research, the research is insufficient. Go back to Step 4 and dig deeper rather than defaulting to the segment template. Search for recent news, acquisitions, expansions, partnerships, funding rounds, competitive moves. Every company has something specific happening — find it.

Record the selected angle in the Research Summaries output (Sheet 3, "Angle Used" column). This angle drives everything in Step 8.

### Step 8: Write 3-Email Sequence + LinkedIn

Now write. **The angle selected in Step 7 is your primary reference — it drives the email.** Read `references/email-writing-rules.md` and `references/messaging-framework.md` for vocabulary, proof points, and persona pain mapping that support the angle. The segment messaging framework is a vocabulary and proof-point guide, not a template. It provides the right words and proof points to support your company-specific angle.

**Tone:** Smart industry peer who spent 10 minutes learning about their business. Not a marketing email. Not a sequence tool output. A note from someone who understands their world.

**Email 1 (Initial):**
- Opening: Context. First name. Why you're writing.
- Pain hypothesis: Lead with the company-specific angle from Step 7, framed as the problem this person deals with. "I'd guess" or "I'd imagine" if inferring.
- Context bridge: Connect their specific situation to the problem. Research absorbed into framing, not displayed.
- Value connection: How MaiaEdge relates. Keep tight. Use segment framework vocabulary and proof points to support the angle.
- CTA: One question. "Open to a conversation?" / "Worth a conversation?" / "Dealing with something similar?"

**Email 2 (Follow-up, 3-4 days later):**
- Shorter than Email 1. Reference the first email briefly ("Quick follow-up").
- Add one new data point: anonymized proof point, market trend, or different angle.
- Same CTA style.

**Email 3 (Break-up, 5-7 days later):**
- Shortest. "Last note on this."
- One final value hook or timing signal.
- Graceful exit: "If timing isn't right, no worries."
- Soft CTA.

**LinkedIn Connection Request:**
- Hard limit: 300 characters. Count every character.
- Format: "[Sender first name] from MaiaEdge. [Company-specific detail]. [Value hook]. Same team behind Acme Packet. Worth connecting?"
- Use "from MaiaEdge" not ", MaiaEdge" to avoid ambiguity (the latter could read as if addressing the recipient).
- NO em dashes in LinkedIn messages. Scan for — and replace with commas or periods before finalizing.

**Word count targets by segment (ENFORCE THE FLOOR):**

| Segment | Email 1 | Email 2-3 |
|---|---|---|
| Fiber Operator | 75-125 words | Shorter is fine |
| Colocation | 100-150 words | Shorter is fine |
| AI Colo | 100-150 words | Shorter is fine |
| Neocloud | 100-150 words | Shorter is fine |
| Network Operator | 125-175 words | Shorter is fine |
| MSP / Aggregator | 75-125 words | Shorter is fine |

Email 1 MUST hit the minimum word count for the segment. If you're under the floor, add one more sentence of company-specific observation or pain hypothesis. Do NOT pad with generic filler. Count the words before finalizing.

**Writing rules (non-negotiable):**
- No em dashes. Ever. Use periods or commas.
- No "Hope this finds you well" / "Just wanted to reach out" / "I noticed" / "Revolutionary" / "Game-changing"
- No customer names in cold emails. Anonymize: "one fiber operator" not "Arvig"
- Always pair speed with ownership: "your team provisions in minutes" not just "provision in minutes"
- Credibility anchor in every Email 1
- Subject lines: short, specific to them. "[Company] interconnection" not "Unlock new revenue"
- One idea per email. Not three.

**Role-based framing:**

| Role | Lead With | Avoid |
|---|---|---|
| CEO/President | Revenue, competitive position, market timing | Technical details |
| CFO | 80-90% cost reduction, OpEx model | Architecture, jargon |
| COO | Scale without headcount, automation | Strategic vision |
| CTO/VP Eng | Protocol-free, API-driven, no MPLS/BGP | Revenue metrics |
| VP Product | Launch in weeks, fabric-in-a-box | Operational details |
| VP Sales/Commercial | Deal velocity, instant provisioning | Technical architecture |
| VP Network/Infra | End-to-end visibility, hop-by-hop telemetry | Revenue impact |

### Step 9: Quality Check

Run for every contact before including in output:

**Research quality:**
- [ ] Account brief read and verified (or full research if no brief)
- [ ] Timing signal identified (or noted as absent)
- [ ] Contact background researched
- [ ] Segment verified against research findings
- [ ] Activity gate passed (no STOP flags)
- [ ] Email source verified ([HS] or [Apollo-Verified] or [User])
- [ ] Company-specific angle selected in Step 7 (not a segment template restatement)

**Angle-specificity check:**
- [ ] Would this email make sense sent to a different company in the same segment? If yes, the angle isn't specific enough — go back to Step 7 (Angle Selection).
- [ ] Does the email lead with a company-specific problem, or does it lead with a generic segment pain? If generic, rewrite.
- [ ] Is the angle from Step 7 visible in the email's problem statement? The email should be clearly driven by the company-specific angle, not by the segment framework.

**Email quality:**
- [ ] Within word count for segment
- [ ] Sovereignty/ownership language present
- [ ] Doesn't sound like NaaS (we're infrastructure, not a service)
- [ ] No em dashes (search for — character)
- [ ] No banned phrases
- [ ] No competitor names (Megaport, Equinix, Lumen, etc.) — use "third-party fabric" instead
- [ ] Credibility anchor in Email 1
- [ ] Single CTA per email
- [ ] Pain points match the contact's role
- [ ] Subject line is short and specific to them
- [ ] Each email in the sequence has a DIFFERENT angle (not just shorter versions of Email 1)

**LinkedIn quality:**
- [ ] Under 300 characters (count precisely)
- [ ] Includes company-specific detail
- [ ] Includes credibility anchor
- [ ] Low-friction ask
- [ ] No em dashes (scan for — character specifically)
- [ ] Sender intro uses "from MaiaEdge" format

---

## Output

Produce TWO files:

### File 1: Smartlead Import XLSX

Use openpyxl. Professional formatting. Sheet name: "Smartlead Import"

**Columns:**

| Column | Description |
|---|---|
| first_name | Contact first name |
| last_name | Contact last name |
| email | Verified email address |
| company_name | Company name |
| title | Contact job title |
| linkedin_url | Contact LinkedIn URL |
| phone | Phone number (if available) |
| custom_field_1 | Segment (e.g., "Data Center Colocation") |
| custom_field_2 | Sender name (Tim Lieto or Ken Cunningham) |
| custom_field_3 | Territory owner (per territory model) |
| custom_field_4 | Persona (Technical Champion / Business Sponsor / Economic Buyer) |
| custom_field_5 | Company domain |
| email_subject_line_1 | Subject for Email 1 |
| email_body_1 | Full body text for Email 1 |
| email_subject_line_2 | Subject for Email 2 (usually "Re: [Subject 1]") |
| email_body_2 | Full body text for Email 2 |
| email_subject_line_3 | Subject for Email 3 (usually "Re: [Subject 1]") |
| email_body_3 | Full body text for Email 3 |

**Formatting:**
- Header row: Bold, dark blue fill (#2F5496), white text, centered
- Data rows: Arial 10pt, wrap text on email body columns
- Column widths: Auto-fit for metadata, 60+ for email body columns
- Row heights: 200+ for rows with email content

**Exclusion rules for Smartlead file:**
- Do NOT include contacts with STOP flags (active conversations, enrolled in sequences, Connected/Open Deal status)
- Do NOT include contacts with unverified emails (Apollo-Unverified or Web-sourced)
- Include a note at the bottom or separate "Excluded" sheet listing skipped contacts and reasons

### File 2: Review XLSX

Same data plus research context for human review before sending. Three sheets:

**Sheet 1: "Overview"** — One row per contact with: Company, Contact, Title, Email, Email Source, LinkedIn, Segment (Verified/Mismatch), Activity Flag, Lead Status, Territory Owner, Sender, Notes

**Sheet 2: "Email Sequences"** — One row per contact with: Company, Contact, Persona, Subject 1-3, Email Body 1-3, LinkedIn Message, Word Count E1/E2/E3, LinkedIn Char Count

**Sheet 3: "Research Summaries"** — One row per company with: Company, Domain, Segment, Sub-Segment, Account Brief (from HubSpot), Brief Verified (Y/N), Timing Signals Found, AI Signals, Key Research Findings, Angle Used, Fit Rating

**Sheet 4: "Flags & Excluded"** — Contacts that were stopped, warned, or excluded. Columns: Company, Contact, Flag Type, Reason, Recommendation

### File naming

```
smartlead_import_[YYYY-MM-DD].xlsx
outreach_review_[YYYY-MM-DD].xlsx
```

Save to the user's workspace folder.

---

## Territory Model Reference

| Territory | Owner | States |
|---|---|---|
| East | Tim Lieto (Owner ID: 161889085) | CT, DE, FL, GA, IL, IN, KY, MA, MD, ME, MI, MN, NC, NH, NJ, NY, OH, PA, RI, SC, TN, VA, VT, WI, WV, AL, MS, PR, VI, DC... (30 states) |
| West | Ken Cunningham (Owner ID: 162339176) | AK, AZ, CA, CO, HI, IA, ID, KS, MO, MT, ND, NE, NM, NV, OK, OR, SD, TX, UT, WA, WY (20 states + DC) |
| International | Tim Ziemer (Owner ID: 159350430) | All non-US |

Use HQ state from HubSpot or research to determine territory owner. If user specifies a sender that doesn't match territory, note it but use the user's choice (they may be running a test or cross-territory play).

---

## Proof Points (Anonymized — Use in Emails)

| Use Case | How to Reference |
|---|---|
| Speed | "One fiber operator went from 60-90 day provisioning to under 10 minutes." |
| Sovereignty | "A colo operator told us with third-party fabrics, 'you turn the customer over to them.' With MaiaEdge, they control their destiny." |
| Simplicity | "One operator called it 'fabric in a box. Drop it in, add water, it works.'" |
| Scale | "Deployed across 800+ cell towers and 20+ data centers for a network operator." |
| Industry validation | "Even Equinix called what we're building 'revolutionary and creative.'" |
| Federation | "A fiber operator in the Pacific uses federation to extend to the mainland." |

## Exclusion List

STOP and skip if company is:
IXP, Tower REIT, IT MSP (helpdesk/break-fix), Retail ISP (no wholesale), Software vendor, Hyperscaler (AWS/Azure/GCP/Meta), Enterprise (internal-only network), Under 7 employees, Vendor/Contractor/Manufacturer, Consulting firm, Trade organization, Defunct/Acquired (absorbed into parent)

---

## Competitive Positioning (For Email Context — Use Sparingly)

- **vs. NaaS (Megaport/Equinix Fabric):** "With them, you turn the customer over. With MaiaEdge, you keep the customer." Say "third-party fabric providers" NOT specific competitor names. NEVER write "Megaport" or "Equinix" or any competitor name in a cold email. Use "third-party fabrics" or "someone else's fabric" instead.
- **vs. Lumen PCF:** "Lumen builds their empire. MaiaEdge empowers you to build yours."
- **vs. Status Quo:** Frame the cost of inaction. Most deals are lost to inertia.

## Neocloud Messaging (DIFFERENT from other segments)

Neoclouds are NOT colos. They ARE the customer. Drop ALL sovereignty language. Lead with:
1. Observability ("see why you're slow")
2. Cloud on-ramp (cost savings vs public internet egress)
3. Deterministic paths (message #3, not #1)

## Segment Fallback Messaging

When research doesn't reveal company-specific details, use these defaults. But always try to find something specific first — fallback messaging is generic and these emails go to executives.

- **Colo Standard:** "Build your own fabric rather than joining someone else's."
- **Colo AI:** "Deterministic intelligence delivery. Make the network predictable for inference."
- **Fiber:** "Every multi-state deal lost to provisioning delays is margin walking out."
- **Network Op Track A:** "You've automated internally. Extend that everywhere else."
- **Network Op Track B:** "Unify internally first, then extend externally."
- **MSP:** "You own the customer relationship. We give you visibility into everything behind it."
- **Neocloud:** "See why you're slow. Then fix it."
