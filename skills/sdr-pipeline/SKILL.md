---
name: sdr-pipeline
description: "End-to-end MaiaEdge SDR pipeline. Takes a list of companies + contact titles, pulls all intel from HubSpot first (account briefs, contacts, activity, segment), fills gaps with web search and Apollo, verifies segments, checks for active conversations, writes personalized 3-email sequences + LinkedIn, and outputs a Smartlead-ready XLSX + review file. Use when asked to run outreach, process a batch, write emails for a list, prepare a Smartlead import, or do cold outreach for multiple companies. Also trigger when the user provides a list of company names with titles/roles and wants emails written. This skill is the primary workflow for turning a prospect list into send-ready outreach."
---

# MaiaEdge SDR Pipeline

Turn a list of companies + contacts into verified, personalized, send-ready outreach with a Smartlead XLSX and review file.

## Hard Gate Before Writing (Step 7d Below)

Before writing any email body for a contact, emit a complete **Research Receipt** for that contact. The Receipt requires literal search query strings actually run, paired with results: minimum 3 if claiming a cataloged signal, minimum 5 if claiming NONE. Contact-level finding required on every Receipt.

At batch scale, the Receipt populates Sheet 3 of the review XLSX. A row with `Signal Code = NONE`, fewer than 5 entries in Searches Run, and a thin Contact Finding is the audit signature of research-skipping. If you cannot fill the Sheet 3 Receipt columns truthfully, do not include the contact in the Smartlead output.

## What This Skill Does

This is the complete pipeline. User gives you companies and contacts. You produce emails that sound like a smart industry peer wrote them after spending real time learning about the business. These go to C-level and VP-level executives at infrastructure companies. Every claim must be verifiable. Every email must be unique to that person.

**Stack:** HubSpot (CRM) → Apollo (contact enrichment) → This pipeline (research + writing) → Smartlead (sending)

## Input Format

The user will provide some combination of:
- Company names (always)
- Contact titles/roles they want to target (always)
- ICP segment (usually)
- Contact emails (usually  -  they verify emails before sending)
- Contact/company LinkedIn URLs (sometimes)
- Sender preference: Tim Lieto or Ken Cunningham (ask if not specified)

The user will NOT always provide domains, emails, or LinkedIn URLs. Part of your job is to pull those from HubSpot and fill gaps.

## Before You Start

1. **Confirm sender.** Tim Lieto (AVP, North America Sales, West/Central/National) or Ken Cunningham (Sales, East Region). Ask once for the whole batch unless specified per-contact.

2. **Check Apollo credits.** Run `apollo_users_api_profile` with `include_credit_usage: true`. Report remaining credits. Each contact enrichment costs credits. Estimate consumption for the batch and confirm before proceeding.

3. **Read messaging references.** Before writing any emails or LinkedIn messages, read these reference files:
   - `references/segment-language.md`  -  **Read first.** Insider vocabulary, daily reality, conversational patterns per segment. This is how you sound like a peer, not a salesperson.
   - `references/email-writing-rules.md`  -  Email structure, CTAs, quality checklist, banned phrases (fabric-in-a-box ban, "Federation"-verb ban, brand-voice "We built carrier infrastructure that…" ban), segment lock rule
   - `references/segment-messaging.md`  -  Per-segment value-prop matrices and embed-by-contrast templates. **Network Operator §5 is split into Tier 1 (Global + National) vs Tier 2/3 Regional Wholesale lead motions.** **Colocation has Standard + AI Signals sub-segment routing.**
   - `references/fallback-messaging.md`  -  Per-segment fallback E1/E2/E3 templates. Colo Standard / Colo AI Infrastructure / Network Op Tier 1 / Network Op Tier 2/3 / Track B / Fiber blocks all live here.
   - `references/persona-targeting-blocklist.md`  -  **Pre-write gate (Step 0a below).** Title-by-title block list for the standard SDR cadence.
   - `references/pre-cadence-hygiene.md`  -  **Pre-write gate (Step 0b below).** Three list-hygiene filters (auto-bounce, OOO, LinkedIn-status).
   - `references/messaging-framework.md`  -  Segment-specific messaging, tone, writing rules
   - `references/hubspot-values.md`  -  Exact HubSpot property values for segment/sub-segment
   - Segment cheatsheets for the relevant segment (colocation.md, fiber-operator.md, neocloud.md, network-operator.md, msp-aggregator.md, enterprise.md)
   - `references/signal-framework.md`  -  Universal signal types, scoring model, noise list. Required for the new Public Signal Cited rule.
   - `references/[segment]-signals.md`  -  Per-segment cataloged signals with `Pattern:` fields used as web search queries in the new catalog-grounded research step (Step 4).
   - `references/sub-segment-qualification.md` (context/core/)  -  Authoritative list of the 30 active `company_sub_segment` values. Use exact case-sensitive HubSpot strings for any sub-segment reference in research notes, voice guides, or written copy.
   - `references/enrichment-protocols.md` (context/core/)  -  Canonical definitions of `account_brief`, `recent_news_or_trigger_event`, `fabric_provisioning_approach`, and `geographic_focus` - the four enriched fields that ground the per-contact angle in real prospect substance.

## Pre-Pipeline Gates (Mandatory Before Any Per-Contact Step)

The pipeline below assumes the contact list has cleared two pre-cadence gates. If you receive a raw list (Cooper, the rep, or an enrichment pull), run these gates first and surface any blocks BEFORE running Step 1:

### Step 0a - Persona Pre-Check (per `context/outreach/persona-targeting-blocklist.md`)

For every contact in the input list, verify the title is NOT on the blocklist:
- **Universal blocks:** Account Executive, Account Manager, Customer Success Manager.
- **Aggregator / NaaS / TSD blocks:** Director - Carrier Wholesale, Wholesale Manager, Director - Sales (Wholesale).
- **Fiber / ISP blocks:** Director - Field Operations, GM / Regional Operations Manager.
- **International carrier blocks:** Country Manager / GM - [Country] at carriers with HQ product orgs, Finance Director / Treasurer.

Blocked contacts are surfaced in a Cooper-review queue (separate XLSX tab or markdown table), not silently dropped.

### Step 0b - Pre-Cadence Hygiene (per `context/outreach/pre-cadence-hygiene.md`)

For every contact, run the three filters at the appropriate stage:
1. **LinkedIn-status check on lead pull:** flag if current LinkedIn role differs from source list (retired, moved companies, role change).
2. **Auto-bounce / autoresponder detection:** at Smartlead campaign export, check historical 90-day bounce/autoresponder activity by email address.
3. **OOO detection at send-time:** runs continuously during the cadence (between E1 and E2, E2 and E3).

Surface filter hits in the same Cooper-review queue as Step 0a blocks.

---

## The Pipeline (Per Contact)

Process contacts sequentially. Complete one fully before starting the next. Never reuse research across different companies (contacts at the SAME company share company research but get individual contact research and unique emails).

### Step 1: HubSpot Deep Pull

**Company search**  -  Use `search_crm_objects` (objectType: companies). Search by name AND domain if provided. Pull:

```
name, domain, linkedin_company_page, website,
account_brief, recent_news_or_trigger_event,
customer_segment, customer_sub_segment, segmentation_confidence,
account_tier, signal_heat, description, about_us, linkedinbio, opportunity_description,
state, city, country,
hubspot_owner_id, annualrevenue, numberofemployees,
notes_last_contacted, notes_last_updated, num_contacted_notes
```

**Sort the batch by `signal_heat` first, then by `account_tier`.** Hot before warm before cool before cold. Within each heat bucket, lower tier number first (Tier 1 before Tier 5). This puts the highest-intent accounts at the top of the batch so the limited Apollo + writing budget hits the workable accounts first. Cold accounts at high tier are still in scope (they're strategic), they just queue behind hot accounts.

> **Note on `recent_news_or_trigger_event`:** This field is populated weekly by the `weekly-signal-scan` skill. It can be STALE for any contact added or surfaced mid-week. Per the new Public Signal Cited rule, this field is CONFIRMATION ONLY, not source-of-truth. The catalog-grounded web search in Step 4 is the primary signal lookup.

**Contact search**  -  Search contacts by name + company association, or by email if provided. Pull:

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
- `[HS]`  -  From HubSpot
- `[Apollo]`  -  From Apollo enrichment (note verified/unverified)
- `[Web]`  -  From web search
- `[User]`  -  Provided by user in the input
- `[Missing]`  -  Not found anywhere. Flag for user.

### Step 1.5: Warm/Cold Classification

Based on HubSpot data, classify each contact before proceeding:

**WARM (any of these):**
- `notes_last_contacted` within 90 days
- Company notes mention shared events (#MetroConnect26, #PTC26, #FiberConnect, #ITW26, etc.)
- Deal or POC history exists in HubSpot

**COLD:** No meaningful activity meeting the above criteria.

**Classification drives writing rules in Step 8:**
- Warm contacts get shorter emails (10-15% below cold targets), more casual tone, warm-but-vague framing ("We've connected with a few folks at [Company]") ONLY with HubSpot backup
- NEVER fabricate warmth. No activity = go cold. Do NOT fake familiarity.

Record classification: `WARM: [reason]` or `COLD: No qualifying activity`

### Step 1.6: Verify Segment (Moved Here -- Before Research)

After HubSpot pull, immediately verify the segment before investing in research.

**Check:**
- Does `customer_segment` match the company description? (e.g., "Data Center Colo Provider" but HubSpot `description` shows fiber operator)
- For colos: Any AI signals in the description or notes?
- Is this company on the exclusion list? (IXP, Tower REIT, IT MSP, software vendor, etc.)

**If mismatch:** Flag: `SEGMENT MISMATCH: HubSpot says [X], initial check says [Y]. Will verify in Step 4 research.`
**If obvious:** Note: `Segment preliminary: [segment] / [sub-segment]`

Full segment verification happens again after web research (Step 4). This early check prevents wasting research time on clearly misclassified companies.

**When segment changes:** `SEGMENT CORRECTED. Reload segment-language.md for [new segment]. All draft emails must use corrected vocabulary.`

### Step 2: Activity Gate (MANDATORY -- Do Not Skip)

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

If `account_brief` has content, read it. This is the primary research foundation  -  someone has already done research on this company.

**But do not trust it blindly.** The brief may be stale (company acquired, pivoted, expanded). You will verify it in Step 4.

If `account_brief` is empty, that's fine. Step 4 will do full research.

### Step 4: Web Research  -  Catalog-Grounded Signal Lookup (REQUIRED for Public Signal Cited rule)

**The web search must be grounded in the segment's signals catalog (`references/[segment]-signals.md`), not in generic "[company] news" queries. This enforces the signal taxonomy and prevents the writer from grabbing whatever press release looks shiny.**

**Lookup sequence (mandatory, in order):**

1. **Open the segment's signals catalog** for the contact's segment (e.g., `references/fiber-signals.md` for a fiber operator). Read the Tier A signals first, then Tier B if no Tier A hits.

2. **Run each Tier A signal's `Pattern:` field as a web search query.** Substitute `[company name]` for the company. Examples for fiber:
   - F-A1 pattern: `"BEAD subgrant awarded" + [company name] + route miles`
   - F-A2 pattern: `[company name] + ("definitive agreement" OR "to acquire" OR "completes acquisition") + fiber`
   - F-A3 pattern: `[company name] + ("AI data center" OR "hyperscaler" OR "GPU cluster") + ("dark fiber" OR "IRU" OR "wavelength" OR "400G" OR "800G")`
   - F-A5 pattern: `[company name] + ("named" OR "appointed" OR "joins as") + (VP OR SVP OR Chief) + (Network Automation OR Network Operations OR Wholesale OR Carrier Relations OR Service Delivery OR Transport OR Interconnection)`
   - F-A6 pattern: `[company name] + ("IRU" OR "indefeasible right of use" OR "dark fiber agreement") + (hyperscaler OR carrier)`
   - F-A7 pattern (broader M&A): `[company name] + ("merger" OR "acquisition" OR "divestiture" OR "carve-out" OR "consolidation")`

3. **If a HIGH-confidence Tier A hit lands, stop.** That's the signal. Tag it with the catalog code (e.g., `F-A1`).

4. **If no Tier A hits, expand to Tier B patterns** from the same catalog.

5. **Cross-check `account_brief` and HubSpot `recent_news_or_trigger_event`** for confirmation or additional context. If HubSpot has something the web search missed, pull it in. If the web search found something fresher than HubSpot, web search wins (HubSpot can be stale).

6. **Contact-specific search:** `[Contact Name] [Company] LinkedIn` for background, recent posts, role changes.

7. **Tag every signal found with one of:**
   - **Catalog code** (e.g., `F-A1`, `NC-A2`, `NO-B3`) when the finding matches a cataloged pattern
   - **`NON-CATALOG`** when the writer found a real signal that doesn't match a cataloged pattern (e.g., earnings call language shift not in the catalog)
   - **`NONE`** when web search and HubSpot both came up empty at all tiers - the writer falls back to inference, posture must be ASKED

**What you're extracting:**
- A specific public signal you can cite by code (or honestly mark as NONE)
- Verification that the account brief is still accurate
- Company-specific details that would already show up in the cataloged signal (don't re-research route miles, facility counts, etc. - those are research display, not research-as-fuel)
- Contact background for role-appropriate framing
- AI signals for colos (GPU tenants, liquid cooling, AI-ready marketing) - these are cataloged in `colocation-signals.md` Tier A

Use catalog-pattern searches, not generic "[Company] recent news 2025 2026" queries. Catalog patterns produce structured findings that are signals by construction.

### Step 5: Fill Gaps with Apollo

**Skip condition:** If the user already provided a verified email AND LinkedIn URL for the contact, skip this step entirely. Apollo is for filling gaps, not re-verifying data the user already confirmed. If email is provided but LinkedIn URL is missing (or vice versa), still run Apollo to fill the missing field.

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

### Step 7: Angle Selection (MANDATORY  -  Do Not Skip)

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

Note: These angle statements are INTERNAL planning tools. The numbers and facts in the angle drive the email's problem statement, but they do not appear in the email itself. See Step 8's "Research as Fuel" section for the translation from angle to email.

**Examples of bad angles (segment template restatements  -  NEVER use these):**
- "Zayo is a network operator, so talk about cross-carrier provisioning." (This is just the segment template.)
- "Crosslake is a fiber operator with subsea routes, so talk about NNI provisioning speed." (Generic segment pain, not company-specific.)

**The key rule:** If you can't identify a company-specific angle from the research, the research is insufficient. Go back to Step 4 and dig deeper rather than defaulting to the segment template. Search for recent news, acquisitions, expansions, partnerships, funding rounds, competitive moves. Every company has something specific happening  -  find it.

**Step 7b: Contact-level tailoring (MANDATORY after company angle):**

For EACH contact at this company, answer this question before writing their email: "What facet of this company angle does this specific person own?"

The CEO cares about revenue, competitive position, board-level risk. The CTO cares about architecture and reliability. The VP Sales cares about deal velocity and win rates. The VP Infrastructure cares about day-to-day operational burden. The same company angle produces different emails for different roles. If multiple contacts at the same company get identical emails (different name, same message), the tailoring is missing.

**Format:** `"[Company] is [doing X]. For [contact's role], this means [specific facet of the problem this person owns]."`

**Example (same company, two contacts):**
- Zayo, CEO Steve Smith: "Zayo is integrating Crown Castle's 90K acquired route miles. For the CEO, the question is how fast integration converts to enterprise revenue the street is watching for."
- Zayo, CTO Jane Doe: "Zayo is integrating Crown Castle's 90K acquired route miles. For the CTO, the operational reality is two OSS stacks, two provisioning systems, and every cross-domain circuit a manual coordination project."

See email-writing-rules.md "Research Sequence" for the canonical rule. Lazy outreach skips this step and sends segment-default messaging to every contact on the list.

**Earned-Problem Doctrine (canonical in email-writing-rules.md).** The selected angle must clear three
gates: (1) it is grounded in what the contact publicly cares about OR is a predictable challenge of
their stated growth, not an assumed flaw; (2) it is framed forward-state ("as you scale into X…"), never
as a verdict on how their business runs today; (3) there are no bold, unverifiable claims about their
current network/provisioning/operations. If the angle fails any gate, return to research — do not write.

Record the selected angle AND contact-level tailoring in the Research Summaries output (Sheet 3, "Angle Used" column). This drives everything in Step 8.

**Step 7c: Posture Decision (MANDATORY after contact-level tailoring):**

For EACH contact, decide the E1 posture (DIRECT or ASKED) based on signal strength and role. Posture is NOT randomized to a quota - match the move to what you actually have.

**Go DIRECT when:**
- Step 4 produced a HIGH-confidence cataloged signal (Tier A from segment signals catalog) you can point at
- Recipient is a technical buyer (CTO, VP Engineering, VP Network) who values precision
- Pain is universally acknowledged in the segment

**Go ASKED when:**
- Step 4 returned `NONE` (no public signal found - inferring)
- Recipient is a senior business buyer (CEO, CFO) who deserves to be treated as a thinking peer
- Pain is variable across the segment
- Writer is genuinely uncertain whether the email is timely

**Format the posture decision in the Research Summaries output:**
- `Posture: DIRECT - HIGH-confidence cataloged signal F-A1 (BEAD subgrant), technical buyer (VP Engineering)`
- `Posture: ASKED - NO catalog signal, inferring; senior business buyer (CEO)`

The posture decision drives the E1 voice (declarative vs illumination question) and the E2/E3 rotation (see Step 8).

### Step 7d: Emit Research Receipt (HARD GATE before writing)

Before any email body is written for this contact, emit a complete **Research Receipt** block. No Receipt = do not write the email.

**Receipt format (mandatory):**

```
RESEARCH RECEIPT - [Contact First Last] @ [Company]

Segment: [segment / sub-segment]   Status: VERIFIED | CORRECTED from [X]
Catalog: context/signals/[segment]-signals.md

Searches run (literal query strings - not paraphrased):
1. `[exact query you ran in Step 4]` → [URL + date, OR "no Tier A hit"]
2. `[exact query]` → [URL + date, OR "no Tier A hit"]
3. `[exact query]` → [URL + date, OR "no Tier A hit"]
[minimum 3 if claiming a cataloged signal; minimum 5 if claiming NONE]

Company-level finding: [signal description with source quote + date, OR "NONE - no Tier A or Tier B hits across [N] searches"]
Contact-level finding: [what THIS specific contact owns / recent role activity / why they care about THIS facet of the problem. REQUIRED on every Receipt, including when company finding is NONE.]

Signal code: [F-A1 | NC-A2 | NO-B3 | NON-CATALOG | NONE]
Posture: [DIRECT | ASKED] - [one-line reason tied to the finding above]
```


**Refuse-to-write rule:** If you cannot honestly fill all four sections (Searches Run with at least 3 literal queries paired with results, Company-level finding, Contact-level finding, Posture with reason), output `RESEARCH INCOMPLETE: [specific reason]` in place of the email body, mark the contact as skipped with reason `SKIPPED: Research incomplete`, and move on. Do NOT fabricate a Receipt to look compliant.

**Receipt → XLSX mapping:** The Receipt fields populate Sheet 3 columns directly:
- `Searches Run (E1)` ← the literal query list (newline-separated)
- `Company Finding (E1)` ← Company-level finding line
- `Contact Finding (E1)` ← Contact-level finding line
- `Signal Code (E1)` ← Signal code line
- `Posture (E1)` ← Posture line

A row with `Signal Code = NONE` and a thin `Contact Finding` is the audit signature of research-skipping. Cooper scans for this pattern.

### Step 8: Write 3-Email Sequence + LinkedIn

<!-- Canonical source: context/copy-strategy/segment-language.md -->
**Segment Lock (mandatory before writing):**
1. Confirm the segment from Step 6.
2. Read `references/segment-language.md` for that segment's insider vocabulary, daily reality, and conversational patterns.
3. Use ONLY that segment's vocabulary. If a term belongs to another segment, it is banned. Using colo terms for a fiber operator, or fiber terms for a neocloud, breaks credibility instantly.
4. Use their words, not ours: "dark fiber sitting idle" not "underutilized assets," "NNI" not "network interconnection," "pointing fingers" not "operational complexity."

**Research as Fuel (mandatory before writing):**

Research is fuel, not decoration. Most cold emails fail because they display research instead of using it. They open with "I noticed your recent expansion into three new states," which tells the recipient exactly one thing: you googled them. That's not a conversation starter. That's a sequence tool.

The email that gets a reply takes that same research and uses it to speak the recipient's language. Instead of displaying "I see you have 15,000 route miles," you use that knowledge to frame a problem the way THEY would frame it: "Every multi-state deal that stalls on provisioning is margin walking out the door." You never mention the route miles. But the email couldn't have been written without knowing them.

The research disappears into the voice. The recipient reads it and thinks: "This person gets it."

**What research-display looks like (NEVER do this):**
- "Your 50,000 route miles is an impressive network." (flattery + displayed stat)
- "I noticed you recently acquired Crown Castle's fiber assets." (I-noticed + displayed fact)
- "With your 12 data center facilities across 6 states..." (company facts as standalone observation)

**What research-as-fuel looks like (DO this):**
- "Every acquired route mile that isn't provisioned on day one is integration cost without integration revenue." (the 50K miles informed the framing, but the number is invisible)
- "Unifying two provisioning systems after an acquisition is the kind of thing that takes 18 months unless the architecture does the heavy lifting." (the acquisition selected the angle, but is never mentioned)
- "I'd guess every new market means a different carrier relationship and a different provisioning timeline." (the expansion is fuel for the problem statement, not content)

**Voice and Tone:**

- Write like a real person having a conversation with a peer.
- **Connect your reasoning with so / since / but / even though; one bare fragment per body, max.** Don't stack clipped one-thought-per-sentence declaratives — let the clauses flow into one train of thought that arrives at a point. Keep the short, direct spirit; just connect it.
- Confident but not aggressive, direct but not polished. Speak at eye level.
- Say the thing, don't announce it. Active voice, second person — "your team provisions," not "the team provisions."
- Plain words, kept industry words. Swap the consultant words (productizing → sell / turn up; operating model → way of working; addressable / TAM → the sites you can reach; monetize → new revenue / get paid for, but keep operator-native "monetize idle fiber"; leverage / utilize / enablement / "solution" → plain words). Keep the insider terms they say: NNI, off-net, route miles, lit / dark, meet-me room, cross-connect, attach rate, GPU cluster, deterministic paths.
- When uncertain, say so honestly. "I'd guess," "I'd imagine," "hard to tell from outside," "tends to," "usually" — used genuinely, capped at 30% of E1s in a batch.
- One core idea per message. Commit fully, no stacking backup points.
- Research fades into voice. Reader should feel you understand their world, not that you processed them through a system.
- Vary sentence length. A flowing connected sentence next to a short one lands; three stacked fragments read as ad copy. Some sentences should just sound like someone talking.
- Never use em dashes. Periods or commas instead.
- The test: would a real person actually write this?

Now write. **The angle selected in Step 7 is your primary reference  -  it drives the email.** Read `references/email-writing-rules.md` and `references/messaging-framework.md` for proof points and persona pain mapping that support the angle. Read `references/segment-language.md` for the exact words this person would use to describe their own problem. The segment language guide is how you sound like a peer. The messaging framework provides proof points to support your angle.

**Tone:** Defined in the Voice and Tone section above. Every email must pass that standard. If it reads like a sequence tool, a marketing email, or a salesperson who researched a company, rewrite it.

**Posture Rotation Per Sequence (applies to all 3 emails):**

Across the 3-email sequence to one contact, rotate posture so the recipient doesn't get three declarative pain statements (or three illumination questions) in a row:

- **E1:** declarative or asked (whichever matches the signal strength from Step 7c)
- **E2:** the OTHER posture (if E1 was declarative, E2 is asked, and vice versa)
- **E3:** take-away or detached close (regardless of E1/E2 posture)

The same contact getting three declarative pain statements reads as one writer pushing one angle three times. The same contact getting declarative-asked-detached reads as one writer thinking out loud across a window of time.

**Email 1 (Initial) -- HARD CAPS:**
- **70-85 words.** Count before finalizing. Applies across every segment; overrides segment soft floors.
- **1-3 paragraphs** with proper blank-line spacing between them.
- **First name on its own line**, then a blank line, then the body. Example:
  ```
  Paul,

  [problem paragraph, with embedded value bridge contrast clause OR followed by 1-sentence standalone value bridge]

  [optional CTA + optional peak-end observation]
  ```
- Opening: Lead directly into the problem. No warm-up, no flattery, no acknowledgment opener ("Cold email, so here's the short version" is BANNED).
- **Posture (DIRECT or ASKED):** Per Step 7c. DIRECT = declarative problem statement, no hedge needed when signal is HIGH-confidence. ASKED = illumination question or premise hedge ("Not sure if you're already solving this, but…" / "Probably already on your radar, but…").
- **Public-signal observation (encouraged):** When Step 4 returned a cataloged signal, open with "Saw the [signal] mentioned in [source]" / "Saw the [signal type] post" / "Caught your panel at…" The signal observation grounds the email in something specific the writer actually looked at. See email-writing-rules.md "Public-Signal Observations" for the full rule.
- Context bridge: Connect their specific situation to the problem. Research is invisible EXCEPT for the public-signal observation. No stats, no facts, no compliments, no numbers.
- **No flattery-as-problem-statement.** BANNED examples: "Growth through acquisition is the right play," "Building Tier-4 facilities is the hard part," "Your expansion into the Southeast is smart." These read as validation of their strategy with a pain bolted on. Lead with the problem itself, no approval clause.
- **No third-person case-study opener.** BANNED: "For a [role] at [type of company doing X]..." (e.g., "For a CFO at a fiber operator expanding into the Southeast..."). A peer doesn't frame their opener like a case study.
- **Value bridge (AT MOST 1 sentence, embed when possible):** Two valid placements:
  - EMBEDDED: woven into the problem paragraph as a contrast clause. Example: "The fix is infrastructure that lets your team stand up those paths in minutes, under your brand."
  - STANDALONE: a single sentence after the problem paragraph, in "I" voice. Example: "I've been working on infrastructure that lets fiber operators stand up cross-carrier paths in minutes, under your brand."
  BANNED: multi-sentence value bridge paragraphs. BANNED generic-category openers: "MaiaEdge is..." / "We help operators…" / "We built infrastructure that…" / "We built carrier infrastructure that…" / "We built MaiaEdge for…" / "We work with…" / "Most operators we talk to…" — these are us-to-a-category sentences with no specific mechanic. Default to "I" voice. **Allowed exception (EMAIL only) — the specific-mechanic peer line:** a "we" attribution is fine when it names a SPECIFIC mechanic and a plain outcome, because that reads as spoken peer credibility, not a slogan: "We've been helping similar [cohort] [specific mechanic], so [plain outcome]." Test: a reader can tell exactly what we DO from the sentence. If the "we" line could describe any vendor ("we help operators grow"), it's the banned generic claim. One peer line per sequence, max; never in LinkedIn (no room under the char cap — see Step 8 LinkedIn rule). For Enterprise and neocloud the mechanic is data-sovereignty / audit-ready-path framing, never operator resale. Max 1 product-specific term per email. **Also BANNED in cold body:** "fabric-in-a-box" (cheatsheet / live-conversation only), "federate" as a verb. The noun phrase "Federated Private Networking" is allowed only in partner-facing collateral, never in cold body.
- CTA: One question. "Open to a conversation?" / "Worth a conversation?" / "Dealing with something similar?" Optional when a strong illumination question carries the close.
- **Peak-end observation (optional, 1 max, only when meaningful):** A non-business observation tied to something specific about the recipient's company or location, separated from the CTA. Must pass the "forwarded by colleague" test. NEVER in E2 or E3.
- **Non-functional voice required when there's something to say.** At least one sentence in E1 should not "do work" structurally (an aside, an honest acknowledgment of uncertainty, a peak-end observation). Don't force it. A forced non-functional sentence reads as performance.

**Research Display Detector (run before finalizing every email):**
Scan every sentence. If any of these appear, rewrite before proceeding:
- Company facts as standalone observations ("[Company] has/is/raised...")
- "Your [number] [thing]" patterns
- Opening sentences that describe the company rather than name a problem
- Dollar amounts, facility counts, route miles stated as facts
See email-writing-rules.md "Research Display Detection" for the full translation table.

**Cited-Signal Cap (HARD CONSTRAINT - applies to every E1 in the batch):**
Maximum ONE cited public signal in the opening two sentences of E1. When the account has multiple Tier A signals (funding + project + tenant), pick the SINGLE strongest one for the opener. The rest informs framing but stays out of displayed text. At batch scale this matters more than at single-email scale: when 5+ contacts at the same account each get an email opening with the same fact recap ($X funding + Y project + Z tenant), recipients who compare notes see a campaign rather than a peer message.

Markers to count in opening 2 sentences (≥2 = cap violation, rewrite):
- Dollar amounts ($X B/M)
- Power figures (X MW, Y GW)
- Named hyperscaler tenants (Microsoft, NVIDIA, AWS, Oracle, OpenAI, AMD, Meta, Google, Stargate, AI Infrastructure Partnership, named investors)
- Named projects/campuses (Caprock, Comanche, TCDC, Jupiter, etc.)
- Building/site/facility counts ("6 buildings", "9 campuses")

Same rule applies to E2 and the LinkedIn message. If the same fact recap appears in E1, E2, AND LinkedIn for the same contact, all three are stamped - the campaign is read.

See `skills/cold-email/SKILL.md` "Cited-Signal Cap" for full examples and rationale.

**Role-Addressing Language (BANNED):**
- "At the [role] level" / "From a [function] standpoint" / "For an operator [doing X]" / "At your scale"
Instead: state the problem directly. A peer says "the fiber buildout is moving" not "at the CEO level, I'd imagine..."

**Warm Contact Adaptations (if classified WARM in Step 1.5):**
- Use warm-but-vague framing: "We've connected with a few folks at [Company]" ONLY if HubSpot backs it up
- If event-tagged notes exist: weave shared event into opener naturally
- 10-15% shorter than cold targets. More casual. Fewer proof points.
- NEVER fabricate warmth. No activity = proceed cold.

**Email 2 (3-4 days later) -- HARD CAPS:**

Same voice as Email 1. Same rules: research-as-fuel, peer tone, problem-first. The differences are length, angle, and the no-meta rule.

- **Under 55 words.** Enforce strictly.
- **First name on its own line**, blank line, body.
- **No re-introduction.** BANNED openers: "Quick follow-up," "Following up on my last email," "Circling back," "Just wanted to bump this." These signal automation.
- **No meta-references to Email 1.** BANNED phrases: "The other angle on this," "Another way to think about this," "To build on my last note." Email 2 leads with the new thought, not a reference to the prior send.
- Bring a genuinely different dimension from a DIFFERENT angle category than Email 1. Six categories: Revenue, Competitive, Operational, Market Timing, Cost-of-Inaction, Peer Social Proof. Standalone test: would Email 2 make sense if you removed Email 1? If not, it's not differentiated enough.
- Cap "one operator told us..." at 1 per 3-email sequence. Good device but becomes templated when every Email 2 uses it.
- The brevity comes from having ONE tight idea, not from compressing Email 1.
- Same CTA style, but rotate the phrasing. If Email 1 used "Open to a conversation?" try "Dealing with something similar?" or "On your radar?"
- This should read like a real person had another thought and came back to share it. Not like step 2 of a sequence.

**Email 3 (5-7 days later) -- HARD CAPS:**

E3 has TWO valid energy modes. Pick based on whether a real timing hook exists:

- **Timing-anchored close (Event Mode + accounts with a real milestone):** "Show is coming up" energy. There's a window closing (event date, quarter end, buildout milestone, fiscal boundary) and that's the reason to engage now.
- **Detached close (non-event sequences without a real timing hook):** Match the silence. The recipient never engaged, so there's no "project" to reference (Voss-style "Have you shelved this?" / "Have you given up on this project?" are DEAL-CYCLE phrases - they belong in active-deal nurture where the prospect agreed something existed, NOT in cold outreach where they never engaged). Cold-appropriate detached closes:
  - "Sounds like the timing isn't right. Easy to reach me if it ever lands differently."
  - "I'll stop here. Door's open if anything shifts."
  - "Worth me staying in touch on this, or should I move on?"
  - "Last note from me. If this becomes relevant later in the year, you know where to find me."

The detached close is preferred when E1 used a take-away or asked posture. The timing close fits when E1 was DIRECT and a real milestone exists.

- **2-3 sentences max.** Not "3-4." Not "a short paragraph." Two or three sentences, full stop.
- **First name on its own line**, blank line, body.
- **Exactly ONE CTA.** No second ask. No "hope to cross paths" tail. No "either way" closer. BANNED pattern: "If [X] is worth a conversation... Either way, hope to cross paths." Pick one.
- Do NOT default to "Last note on this" as an opener. Cold-email cliche.
- For timing-anchored mode: The CTA should be timing-anchored when possible: "Show is in two weeks, worth grabbing time?" beats "Happy to pick this up whenever." The nudge is the window, not the politeness.
- For detached mode: Match the energy. If they've gone quiet, you go quiet. The close acknowledges silence without manufacturing urgency AND without inventing a "project" the recipient never agreed to.
- **NEVER use deal-cycle phrases in cold E3.** BANNED in cold: "Have you shelved this project?" / "Have you given up on this?" / "Have you deferred this initiative?" These assume the prospect agreed something existed. They belong in active-deal nurture, not cold outreach.

**LinkedIn Connection Request:**

LinkedIn format: NO sender intro in body. Recipient sees who sent the request from LinkedIn's UI.

- **Target length: 35-50 words. Hard cap: 280 characters** (still under LinkedIn's 300 hard limit). Long DMs are a sequence-tool tell.
- **NO sender intro.** Recipient sees who sent the connection request from LinkedIn's UI. The in-message intro ("Tim from MaiaEdge.") is redundant and triggers the sales-pitch reflex before the recipient reads the actual message.
- **Format:** `[Recipient first name], [observation/question with company-specific signal]. [Optional: one sentence of context]. [CTA or no CTA].`
- The angle must be chosen at the intersection of the company's situation AND the contact's responsibilities. The same company gets a different message for the CTO vs the CEO.
- **Public-signal observation preferred opener:** "saw the Tennessee build wraps in Feb" / "caught your panel at MetroConnect" - same Public Signal Cited rule as cold email applies here.
- **Posture rotation:** LinkedIn message should NOT use the same posture as E1 (per the per-sequence rotation rule). If E1 was DIRECT, the LinkedIn message can be ASKED (illumination question), and vice versa.
- NO credibility anchors (no Acme Packet, no 128 Technology). The message does the talking.
- NO em dashes in LinkedIn messages. Scan for  -  and replace with commas or periods before finalizing.
- NO "we" constructions ("We help operators…" - banned in LinkedIn DMs too). The full we-ban holds for LinkedIn: the email-only specific-mechanic peer line does NOT apply here, since there's no room for it under the 280-char cap. Stay in "I" voice or second person.
- Research is fuel: the research selects which problem to lead with. The message names the problem. The research itself stays invisible. Don't recite facts back to them.
- **Sequential processing:** LinkedIn messages MUST be written one at a time, reading the contact's Email 1 before writing. Never batch-template LinkedIn messages.
- See linkedin-outreach skill for full methodology, company+contact angle selection, and research-as-fuel standard.

**Example of the new LinkedIn format (full Receipt above the body):**
```
RESEARCH RECEIPT - Paul Janes @ Fatbeam

Segment: Fiber Operator   Status: VERIFIED
Catalog: context/signals/fiber-signals.md

Searches run:
1. `"BEAD subgrant awarded" Fatbeam route miles` → texas-comptroller.gov/.../bead-q1-2026, 2026-03-15
2. `Fatbeam ("definitive agreement" OR "to acquire") fiber` → no Tier A hit
3. `Fatbeam ("named" OR "appointed") (VP OR Chief)` → no Tier A hit

Company-level finding: F-A1 BEAD subgrant award. Texas Comptroller, 2026-03-15: $12M Eastern Texas middle-mile.
Contact-level finding: Paul Janes, VP Engineering since 2024. Owns provisioning. Recent LinkedIn posts on automation.

Signal code: F-A1
Posture: ASKED - illumination question fits a connection request even with a strong signal

---

Paul, saw the BEAD subgrant for Eastern Texas. Curious how you're handling the cross-carrier piece into the new market. Usually that's where the revenue clock starts at the other carrier's pace.
```
(36 words, 218 chars in the message body. No sender intro. Cataloged signal cited. Asked posture (illumination question carrying the close). No CTA needed.)

<!-- Canonical source: context/outreach/email-writing-rules.md "Sequence Length & Structure (HARD CAPS)" -->
**Sequence length (HARD CAPS, apply across all segments):**

| Email | Limit | Structure |
|---|---|---|
| Email 1 | 70-85 words | 1-3 paragraphs, proper spacing, first name on its own line |
| Email 2 | Under 55 words | First name on its own line, no re-intro, no meta-references |
| Email 3 | 2-3 sentences max | First name on its own line, exactly one CTA, "show is coming up" energy |

These caps override any segment-specific targets. A tight, relevant email under the cap is always better than padding. NEVER pad with observations, flattery, or restated value props. Count words (Email 1, 2) and sentences (Email 3) before finalizing every contact.

Segment-specific word targets in `references/segment-messaging.md` remain as tone calibration - they inform density and technical depth, NOT length.

<!-- Canonical source: context/outreach/email-writing-rules.md -->
**Writing rules (non-negotiable):**
- No em dashes. Ever. Use periods or commas.
- No "Hope this finds you well" / "Just wanted to reach out" / "I noticed" / "Revolutionary" / "Game-changing"
- No customer names in cold emails. Anonymize: "one fiber operator" not "Arvig"
- Always pair speed with ownership: "your team provisions in minutes" not just "provision in minutes"
- NO credibility anchors in cold emails (no Acme Packet, no 128 Technology). The message does the talking. Reserve credibility anchors for live conversations only.
- **Nudge, don't preach.** No absolutes ("the only way," "the single biggest"). No prescriptive musts ("you need to," "what you should do"). No definitive diagnostics about their business you can't actually know. Hypotheses and relational framing only. Claims about our category can be direct but never grandiose. See email-writing-rules.md "Diplomatic Claims."
- **Reply-worthy test.** After each email, ask: would THIS specific person (not a generic recipient) want to reply? If replying would feel like submitting to a pitch, rewrite. The goal is peer engagement.
- Subject lines: short, specific to them. "[Company] interconnection" not "Unlock new revenue"
- One idea per email. Not three.
- **Hedge variety:** "I'd guess" and "I'd imagine" capped at 30% of Email 1s in a batch. Use alternative constructions: direct assertions, illumination questions, premise hedges ("Not sure if you're already solving this, but…" / "Probably already on your radar, but…"), peer observations, market observations, role-native voice, cost framing.
- **Structural variety (batches of 10+):** Use at least 3 different Email 1 structures. Vary where the opener/context lands, vary paragraph count, vary where the value bridge appears. Self-check: after 5 emails, re-read in sequence. If you can predict the next paragraph's purpose, restructure.
- **Sender voice check:** After writing, re-read sender-profiles.md. Does this email sound like it came from this specific person?

<!-- Canonical source: context/copy-strategy/segment-messaging.md -->
**Role-based framing:**

| Role | Lead With | Avoid |
|---|---|---|
| CEO/President | Revenue, competitive position, market timing | Technical details |
| CFO | 80-90% cost reduction, OpEx model | Architecture, jargon |
| COO | Scale without headcount, automation | Strategic vision |
| CTO/VP Eng | Protocol-free, API-driven, no MPLS/BGP | Revenue metrics |
| VP Product | Launch in weeks, build your own interconnection layer without years of development | Operational details |
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
- [ ] Would this email make sense sent to a different company in the same segment? If yes, the angle isn't specific enough  -  go back to Step 7 (Angle Selection).
- [ ] Would this email make sense sent to a different role at the same company? If yes, contact-level tailoring is missing  -  go back to Step 7b.
- [ ] Does the email lead with a company-specific problem, or does it lead with a generic segment pain? If generic, rewrite.
- [ ] Is the angle from Step 7 visible in the email's problem statement? The email should be clearly driven by the company-specific angle, not by the segment framework.

**Diplomacy and reply-worthiness check:**
- [ ] No absolutes ("the only way," "the single biggest," "you MUST")
- [ ] No prescriptive musts ("you need to," "what you should do," "the right approach is")
- [ ] No definitive diagnostics about their business ("your team can't do X," "your approach is failing") unless research provides direct evidence
- [ ] Claims about their business are hedged or relational; claims about our category are direct but not grandiose
- [ ] Would this specific person want to reply?

**Email quality:**
- [ ] Email 1: 70-85 words, 1-3 paragraphs with proper spacing, first name on its own line
- [ ] Email 2: under 55 words, first name line, no re-intro, no meta-references to Email 1
- [ ] Email 3: 2-3 sentences max, first name line, exactly one CTA, "show is coming up" energy
- [ ] No flattery-as-problem-statement ("X is the right play" / "X is smart" / "X is the hard part")
- [ ] No "For a [role] at [type of company]..." opener
- [ ] Sovereignty/ownership language present
- [ ] Doesn't sound like NaaS (we're infrastructure, not a service)
- [ ] No em dashes (search for  -  character)
- [ ] No banned phrases
- [ ] No competitor names (Megaport, Equinix, Lumen, etc.)  -  use "third-party fabric" instead
- [ ] NO credibility anchors (no Acme Packet, no 128 Technology)
- [ ] Single CTA per email
- [ ] Pain points match the contact's role
- [ ] Subject line is short and specific to them
- [ ] Each email in the sequence has a DIFFERENT angle (not just shorter versions of Email 1)
- [ ] Email 2 comes from a different angle category than Email 1
- [ ] Email 3 has exactly one CTA (no double asks)
- [ ] Email 2 and 3 read like a real person coming back with a new thought, not like scheduled sequence steps. No "Quick follow-up" or "Last note on this" as default openers.
- [ ] No role-addressing language ("at the [role] level", "from a [function] standpoint", etc.)
- [ ] **Value bridge is 1 sentence max**, embedded by contrast OR standalone-but-punchy. Multi-sentence value bridge paragraph is BANNED.
- [ ] **No generic-category we-claims** ("We help operators…" / "We work with…" / "Most operators we talk to…"). Default to "I" voice. The specific-mechanic peer line ("We've been helping similar [cohort] [specific mechanic], so [plain outcome]") is the one allowed "we" sentence in EMAIL — one per sequence, never in LinkedIn.
- [ ] **Research Receipt present above the email body** for every contact (Step 7d output) with all four sections complete: Searches Run (≥3 literal queries paired with results, ≥5 if claiming NONE), Company-level finding, Contact-level finding, Posture with reason. "NONE" without literal queries above it is research-skipping and fails this check.
- [ ] **Posture matches signal strength.** DIRECT when there's a real cataloged signal you can point at; ASKED when inferring. NOT randomized to a quota.
- [ ] **Posture rotates across the 3-email sequence to the same contact.** E1/E2/E3 should NOT all be the same posture; if E1 was DIRECT, E2 should be ASKED, etc. LinkedIn posture should also differ from E1.
- [ ] **Hedge cap: "I'd guess" / "I'd imagine" appear in ≤30% of E1s** in any batch of 10+ contacts.
- [ ] **Non-functional voice present in E1** when there's a meaningful thing to say.
- [ ] **Peak-end observation (if used)** passes the "forwarded by colleague" test. NEVER in E2 or E3.
- [ ] **No acknowledgment openers** ("Cold email, so here's the short version" - banned).
- [ ] **Catalog-grounded web research actually happened** (visible in the Receipt's Searches Run section as literal queries). If "NONE" cited, the Receipt shows ≥5 literal queries that were tried, not just a NONE declaration.
- [ ] **Sheet 3 of XLSX has all five Receipt columns populated** for every contact: Searches Run (E1), Company Finding (E1), Contact Finding (E1), Signal Code (E1), Posture (E1). Audit pattern to flag: NONE Signal Code + fewer than 5 Searches Run + thin Contact Finding = research-skipping.
- [ ] **Earned-Problem check (per contact):** problem is publicly-grounded or a forward-state growth
  challenge, not an unverifiable current-state claim; direct but non-offending; one easy-solution line.
  Run the offense test (read as the recipient who built the company).

**Research-display audit (run on every email and LinkedIn message):**
- [ ] No flattery or congratulations anywhere in the sequence ("impressive," "exciting," "congratulations on," "remarkable growth")
- [ ] No "I noticed" PHRASE (specific "Saw…" / "Caught your panel…" public-signal observations are ALLOWED and ENCOURAGED - see Public-Signal Observations rule)
- [ ] No "I came across" / "I was researching" patterns (LinkedIn surveillance)
- [ ] No company facts stated as standalone observations ("You have 50,000 route miles" / "With your 12 facilities across 6 states")
- [ ] The first sentence is about a PROBLEM (or a public-signal observation), never about the prospect's company as a generic stat
- [ ] Research is invisible EXCEPT for the public-signal observation when one applies
- [ ] If you remove the company name, does the email still read as flattery or a research showcase? If yes, rewrite.
- [ ] The email passes the peer test: would someone who spent 15 years in this segment read this and think "this person gets it"?

**LinkedIn quality:**
- [ ] Target 35-50 words. Hard cap 280 characters (still under LinkedIn's 300 hard limit).
- [ ] **NO sender intro** in body ("Tim from MaiaEdge" is BANNED - recipient sees sender from LinkedIn UI). Format starts with recipient first name.
- [ ] Company-specific detail baked into the problem statement (not just segment pain)
- [ ] Problem-first (not feature-first, not flattery)
- [ ] Public-signal observation opener preferred ("saw the Tennessee build wraps in Feb")
- [ ] NO credibility anchors (no Acme Packet, no 128 Technology)
- [ ] NO "we" constructions ("We help operators…" - banned in LinkedIn DMs too). Full we-ban holds; the email-only specific-mechanic peer line does NOT apply under the char cap.
- [ ] Research absorbed, not displayed (research selects the angle, message names the problem)
- [ ] Low-friction ask ("Worth connecting?" or equivalent) - OPTIONAL when a strong illumination question carries the close
- [ ] No em dashes (scan for  -  character specifically)
- [ ] Doesn't repeat Email 1 language or posture (same problem, different lens)
- [ ] Research Receipt present above the LinkedIn message body (same four-section format as E1 Receipt - Searches Run, Company Finding, Contact Finding, Posture)

### Batch Quality Reset (Every 30 Contacts)

Context drift degrades email quality in later batches. After every 30 contacts (3 batches of 10), MANDATORY quality reset:

1. Re-read segment-language.md for the active segment
2. Re-read email-writing-rules.md (especially the research display detection and role-addressing sections)
3. Re-read the last 3 emails you wrote -- check for pattern repetition
4. Reset hedge variety counter (are you overusing "I'd guess/imagine"?)
5. Check structural variety (are all recent emails following the same arc?)

This is not optional. Context drift produces visible quality drop after batch 5.

- **Current-state assertion sweep:** scan the batch for any line claiming how a prospect's business runs today (network, provisioning, ops) without a public signal. Reframe every hit to forward-state.

### Event Mode

When the user indicates this is event-based outreach (conference, trade show), activate these modifications:

- **CTAs become event-anchored:** "Open to connecting at [Event]?" not "Open to a conversation?"
- **Email 3 becomes "show is coming up" energy,** NOT graceful exit. The timing nudge is the event date.
- **Static subject line option:** User may specify (e.g., "connect at itw?") -- use it for all contacts.
- **Email 3 gets exactly ONE close sentence.** Not a CTA plus "hope to cross paths." ONE close.
- **Event-specific LinkedIn pattern:** `coming to [event]? [one lowercase sentence from E1 angle]` -- see linkedin-outreach skill for full pattern and approved examples.
- **Event-specific CTA rotation banks:**
  - Email 1: "Open to connecting at [Event]?" / "Worth grabbing a few minutes at [Event]?"
  - Email 2: "Worth a conversation at the show?" / "On your radar for [Event]?"
  - Email 3: "Happy to find time at [Event]." / "Door is open at the show."

### Skip Reason Standards

When a contact is skipped, use exactly one of these standardized reasons in the output:

- `SKIPPED: Active conversation (last contacted YYYY-MM-DD)`
- `SKIPPED: Currently in HubSpot sequence [sequence name]`
- `SKIPPED: Lead status [Connected/Open Deal]`
- `SKIPPED: Excluded category ([IXP/Tower REIT/IT MSP/etc.])`
- `SKIPPED: Wrong persona for MaiaEdge ([reason])`
- `SKIPPED: Segment corrected to excluded category`
- `SKIPPED: Insufficient data (no email, no domain)`

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
| custom_field_6 | Account Tier (`tier_1` - `tier_5` from HubSpot `account_tier`) |
| custom_field_7 | Signal Heat (`Hot` / `Warm` / `Cool` / `Cold` from HubSpot `signal_heat` - Title Case per HubSpot enum; see `context/account-tiering/tier-compute-spec.md` §11.5). Surfaces current intent at send time so reps can prioritize replies. |
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

**Sheet 1: "Overview"**  -  One row per contact with: Company, Contact, Title, Email, Email Source, LinkedIn, Segment (Verified/Mismatch), Account Tier, Signal Heat, Activity Flag, Lead Status, Territory Owner, Sender, Notes

**Sheet 2: "Email Sequences"**  -  One row per contact with: Company, Contact, Persona, Subject 1-3, Email Body 1-3, LinkedIn Message, Word Count E1/E2/E3, LinkedIn Char Count

**Sheet 3: "Research Summaries"**  -  One row per CONTACT (not per company - Receipts are contact-level) with: Company, Contact, Domain, Segment, Sub-Segment, Account Brief (from HubSpot), Brief Verified (Y/N), AI Signals, Angle Used, Fit Rating, **Searches Run (E1)**, **Company Finding (E1)**, **Contact Finding (E1)**, **Signal Code (E1)**, **Posture (E1)**

The five Research Receipt columns make the Receipt rule auditable at batch scale:
- **Searches Run (E1):** The literal query strings you ran in Step 4, newline-separated, each paired with its result (URL + date, or "no Tier A hit"). Minimum 3 queries; minimum 5 if Signal Code = NONE.
- **Company Finding (E1):** The company-level finding line from the Receipt (signal description with source quote + date, OR "NONE - no Tier A or Tier B hits across [N] searches").
- **Contact Finding (E1):** The contact-level finding line from the Receipt (what THIS specific contact owns / recent role activity / why they care about this facet). REQUIRED on every row, including NONE rows. A blank or generic Contact Finding paired with NONE is the audit signature of research-skipping.
- **Signal Code (E1):** "F-A1" / "NC-A2" / "NO-B3" / "NON-CATALOG" / "NONE".
- **Posture (E1):** "DIRECT" or "ASKED" with the one-line reason (e.g., "DIRECT - HIGH-confidence F-A1, technical buyer (VP Engineering)" or "ASKED - NO catalog signal, inferring; senior business buyer (CEO)").

**Audit pattern:** A row with `Signal Code = NONE`, fewer than 5 entries in Searches Run, AND a thin Contact Finding is the audit signature of research-skipping. Cooper scans Sheet 3 for this pattern. High NONE rate paired with thin Contact Findings is research-skipping, not a feature of a hard list.

**Sheet 4: "Flags & Excluded"**  -  Contacts that were stopped, warned, or excluded. Columns: Company, Contact, Flag Type, Reason, Recommendation

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

## Proof Points (Anonymized  -  Use in Emails)

| Use Case | How to Reference |
|---|---|
| Speed | "One fiber operator went from 60-90 day provisioning to under 10 minutes." |
| Sovereignty | "A colo operator told us with third-party fabrics, 'you turn the customer over to them.' With MaiaEdge, they control their destiny." |
| Simplicity | "One operator called it 'fabric in a box. Drop it in, add water, it works.'" |
| Scale | "Deployed across 800+ cell towers and 20+ data centers for a network operator." |
| Industry validation | "Even Equinix called what we're building 'revolutionary and creative.'" |
| Reach extension | "A fiber operator in the Pacific extends reach to the mainland without new infrastructure." |

## Exclusion List

STOP and skip if company is:
IXP, Tower REIT, IT MSP (helpdesk/break-fix), Retail ISP (no wholesale), Software vendor, Hyperscaler (AWS/Azure/GCP/Meta), Under 7 employees, Vendor/Contractor/Manufacturer, Consulting firm (Deloitte/McKinsey/BCG/Bain - project-based, NOT Outsourcing Services Enterprise), Trade organization, Defunct/Acquired (absorbed into parent), Manufacturing/Energy-Utilities/Logistics-Supply-Chain (Watch List, not Enterprise ICP), Government/Defense (FedRAMP-gated). **Note:** `customer_segment = "Enterprise-CustomerSegment"` records that pass the four-vertical + scale gate ARE ICP as of 2026-05-11 - see Enterprise (Multi-DC ICP) section below.

---

## Competitive Positioning (For Email Context  -  Use Sparingly)

- **vs. NaaS (Megaport/Equinix Fabric):** "With them, you turn the customer over. With MaiaEdge, you keep the customer." Say "third-party fabric providers" NOT specific competitor names. NEVER write "Megaport" or "Equinix" or any competitor name in a cold email. Use "third-party fabrics" or "someone else's fabric" instead.
- **vs. Lumen PCF:** "Lumen builds their empire. MaiaEdge empowers you to build yours."
- **vs. Status Quo:** Frame the cost of inaction. Most deals are lost to inertia.

## Neocloud Messaging (DIFFERENT from other segments)

Neoclouds are NOT colos. They ARE the customer. OPERATOR sovereignty banned. DATA sovereignty ("sovereign by design", "paths you control") allowed. No network jargon (VLAN, Q-in-Q).

**Master pitch:** Connecting distributed AI infrastructure simply.

**Pillars:** DETERMINISTIC | PRIVATE | INSTANT
1. Deterministic performance (eliminate the network as a variable)
2. Private cloud connectivity (egress savings for their customers)
3. Instant customer on-ramp (new facilities live in minutes)

## Enterprise (Multi-DC ICP) Messaging (DIFFERENT from operator segments)

HubSpot `customer_segment = "Enterprise-CustomerSegment"`. Priority 5 (lowest ICP). Tier 2 ceiling. Anchor: Meijer.

**Critical voice difference:** Enterprises ARE the customer, NOT an operator selling to one. Drop operator-monetization framing. OPERATOR sovereignty BANNED (same logic as neoclouds). DATA sovereignty + audit-trail framing ALLOWED. HIPAA/PCI-DSS/SOX/GDPR mentions are appropriate when the persona implies regulatory exposure.

**Four sub-segments (assigned via HubSpot `company_sub_segment`):**
- `Financial Services - Enterprise`
- `Healthcare Systems - Enterprise`
- `Retail and Distribution - Enterprise`
- `Outsourcing Services - Enterprise`

**Hard gate (BOTH must pass before any Enterprise email is written):**
- **Vertical gate:** one of the four sub-segments. Manufacturing / Energy-Utilities / Logistics-Supply-Chain / Government-Defense / SaaS-only are NOT Enterprise - Watch List or out of scope.
- **Scale gate:** $1B+ revenue AND (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house network engineering team).

**Pillars:** REDUNDANT | SOVEREIGN | AUTOMATED

**Lead angles by sub-segment** (use as fallback if research doesn't surface a stronger company-specific angle):

- **Retail and Distribution:** "Your dark fiber between corporate DCs is one cut from an outage." Dark fiber redundancy that is actually redundant + cloud on-ramp under enterprise control.
- **Financial Services:** "Inter-DC paths are best-effort and compliance is asking you to prove the path." Deterministic inter-DC paths + audit-ready policy enforcement for SOX / PCI-DSS / GDPR + cloud on-ramps under enterprise control.
- **Healthcare Systems:** "EHR DC redundancy depends on a single fiber pair. PHI rides that path." Diverse dark fiber redundancy + HIPAA-aligned policy control + cloud on-ramps for radiology/analytics.
- **Outsourcing Services:** "Your clients' regulators are asking where their data went." Delivery-center reliability + client data sovereignty + dark fiber redundancy between primary delivery hubs.

**Personas to target:**
- **VP Network Infrastructure / Director Network Engineering** (primary technical champion)
- **CIO** (economic buyer at most enterprises)
- **CSO / CISO** (security stakeholder; regulatory framing lands here)
- **Network Architect / Principal Network Engineer** (technical influencer; can take more technical specificity)

**Banned for Enterprise emails (in addition to global ban list):** "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "wholesale activation," "extend reach to new markets," "tenant," "meet-me room," "interconnection revenue," "aggregator," "TSD." Federation framing has no place in Enterprise copy.

**Reference:** Full Enterprise positioning, sub-segment cheatsheets, persona pain language, objection reframes, and HubSpot mapping live in `context/segments/enterprise.md`.

## Segment Fallback Messaging

**For current fallback hooks, see context/outreach/fallback-messaging.md**

When research doesn't reveal company-specific details, use these defaults. But always try to find something specific first  -  fallback messaging is generic and these emails go to executives.

- **Colo Standard:** "You can build your own fabric instead of handing tenants to a third party: automated virtual cross-connects, a services layer you sell under your own brand, and cloud on-ramp, without a multi-year build or a hyperscale facility."
- **Colo AI:** "GPU tenants want dense interconnection fast, so the connectivity layer either keeps up or it becomes the gap in the facility. Deterministic paths between AI sites, automated cross-connects, and cloud on-ramps for GPU workloads."
- **Fiber:** "You can get paid for the fiber you already own by standing up an instant private fabric across your network over any transport, no routing complexity, and selling services you couldn't before, including cloud on-ramp."
- **Network Op Track A:** "You've already automated internally, so the next step is extending that same reach everywhere else."
- **Network Op Track B:** "Unify internally first, then extend externally once the inside is clean."
- **MSP:** "You own the customer relationship, but once traffic leaves your network you're flying blind. The fix is visibility into everything behind it, end to end."
- **Neocloud (in-pain-now):** "When inference latency swings by facility, your team ends up guessing whether it's the carrier, the colo, or something in between, since you can't see the whole path."
- **Neocloud (scaling-wall, 15+ sites hyperscaler-heavy):** "The first 5 hyperscaler contracts didn't need a network team, but the next 40 enterprise customers will, and that's a different problem."
- **Neocloud (early-growth, crypto-to-AI):** "Bitcoin never cared about latency, but enterprise AI tenants do, so the connectivity that worked for mining doesn't survive an inference SLA."
- **Enterprise - Retail and Distribution:** "If the dark fiber between your corporate DCs is a single pair, it's one cut from an outage. Diverse fibers with automated failover at each end, no BGP across the WAN." (data-sovereignty / redundancy framing, not operator resale)
- **Enterprise - Financial Services:** "Inter-DC paths tend to go best-effort while compliance is asking you to prove where the data went, so the win is making the path itself the audit artifact." (audit-ready framing, not operator resale)
- **Enterprise - Healthcare Systems:** "If EHR DC redundancy leans on a single fiber pair, PHI rides that path, so it takes diverse fibers, automated failover, and HIPAA-aligned policy control on the wire." (data-sovereignty framing, not operator resale)
- **Enterprise - Outsourcing Services:** "Your clients' regulators are asking where their data went, so the path across every delivery center has to be the audit artifact, provable on demand." (client data-sovereignty framing, not operator resale)

---

## Final Step: Signal Push-Back to HubSpot (per-company, at end of each per-company processing loop)

**Inviolable rule:** this step runs AFTER the per-company drafted sequence (Email 1 + Email 2 + Email 3 + optional LinkedIn DM) has been generated and added to the in-progress Smartlead XLSX. The push-back must never gate, delay, or alter the primary output. If anything in this step fails, the rep already has that company's drafts queued in the batch — signal-engine staleness is a routine-recovery problem, not a rep-blocker. Skip silently on any failure; the next R-Tier-Audit run reconciles the signal fields.

**Why per-company, not at end-of-batch:** sdr-pipeline processes companies sequentially. Each company's research is freshest right after it completes. Running push-back per-company means a 100-company batch refreshes 100 companies' signals over the course of the run; an end-of-batch sweep would lose context for the earliest companies and double the MCP load (re-reading HubSpot for the comparison gate).

### When to write back (per company in the batch)

During the inline research that produced this company's drafts, you ran web search and (optionally) web fetch. If that research surfaced a **signal-grade event** — funding round, exec hire, M&A, facility/market launch, public outage / RCA, earnings-language shift, or any U1-U6 / AP / FR class in [`context/signals/signal-framework.md`](../../context/signals/signal-framework.md) — score it against the Signal Scan rubric (Tier × Freshness × Confidence). **Pick the single highest-scored event ≥8** for the push-back. Sub-8 events stay in the research notes but don't drive the push-back.

### Comparison gate (write only if fresher)

Read current `last_signal_date` for this company via `mcp__claude_ai_HubSpot__get_crm_objects`. If your discovered **event date** is strictly newer than HubSpot's value (or HubSpot's value is null), proceed. Otherwise no write. Idempotent no-op. **At batch scale this gate matters:** without it, every company in the batch would generate a HubSpot write even when Signal Scan already has fresher data.

### The write block

One `mcp__claude_ai_HubSpot__manage_crm_objects` call per company with `updateRequest.objects[]`, `objectType: "companies"`, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`. Fields:

- `recent_news_or_trigger_event` — pure narrative, no date prefix. Format: `"[Signal Type] - [one-line summary]"`. 2-4 sentences, ≤250 char hard cap.
- `last_signal_date` — the **event date** (YYYY-MM-DD), extracted from the source article. Semantics narrowed 2026-05-28 — event date, NOT today's run date.
- `last_signal_score` — your rubric score (number, typically 0-60).
- `signal_count_last_30d` — read current value. If current `last_signal_date` is within 30d of your new event date, increment by 1. If current is null or >30d old, write 1.
- `signal_heat` — recompute per the inlined spec below. **Title Case enum:** `Hot` / `Warm` / `Cool` / `Cold`. Lowercase is silently rejected.
- `account_tier` — recompute per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md) §4. **Only write if `hs_is_target_account != true`** — flag freezes tier (heat continues regardless).

**Batch rate-limiting:** Loop ≤10 writes per `manage_crm_objects` call (HubSpot MCP cap). 250ms minimum between batches. Exponential backoff (1s → 2s → 4s) on HTTP 429.

### `compute_signal_heat` (inlined from `context/account-tiering/tier-compute-spec.md` §11.5)

```
signal_heat is computed top-down, first match wins:

Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
       OR signal_count_last_30d >= 2
       OR account has any associated open deal past `appointmentscheduled`

Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

Inputs: last_signal_score, last_signal_date (event date), signal_count_last_30d, open-deal state.
Output: enum `Hot` | `Warm` | `Cool` | `Cold` (Title Case per HubSpot).

Override behavior:
- hs_is_target_account = true does NOT freeze signal_heat.
  Tier is rep-locked; heat always reports the truth.
```

Heat writes are idempotent — skip if `computed_heat == current_heat`.

### Stamping policy

**Do NOT bump `last_enriched_date`.** Outreach-time signal push-backs are partial writes, not full enrichment passes. R2's 120-day rotation owns the freshness guarantee.

### Audit log

For each company push-back that fires, add a HubSpot company note:

```
Signal push-back from sdr-pipeline on YYYY-MM-DD: discovered <signal type> event YYYY-MM-DD, score <N>. Heat <prior> -> <new>. Tier <prior> -> <new>.
```

### Batch-level reporting

At end of batch, surface in the sdr-pipeline run summary:

- **Push-backs fired:** N companies received signal-engine writes
- **Push-backs skipped (idempotent):** N companies where HubSpot already had equal-or-fresher data
- **Push-backs deferred (failure):** N companies where MCP write failed — these get reconciled by R-Tier-Audit next run

### Failure handling

If any MCP call fails: log to the deferred list and continue to the next company. The rep's Smartlead XLSX still gets that company's drafts. **Never surface push-back failures as a batch blocker.**

---

## Skill Chain

- **Inputs:** User-provided prospect lists. Pulls from HubSpot + Apollo during execution. Does its own research inline (does NOT require prospect-research first, but benefits from existing account briefs).
- **Outputs:** Smartlead XLSX (for email sending), research summaries
- **QA:** copy-strategist (run on completed batches before sending)
