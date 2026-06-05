---
name: prospect-research
description: "Quick pre-outreach research on a specific company and contact for MaiaEdge outreach. Use when preparing to write an email or LinkedIn message for a single prospect. Pulls HubSpot data, runs web research, checks AI signals for colos, researches the contact, and produces a research summary with angle recommendation. NOT for batch enrichment (use company-enrichment) or deep strategy briefs (use account-brief). This is the 5-10 minute research pass that fuels a single email."
---

# MaiaEdge Prospect Research Process

Research every company before writing. No exceptions. Not even for "small" ones.

The entire point of the research is to identify which problem to lead with and confirm you're talking to the right person. The research itself should be invisible in the final email. The prospect should think "yep, that's my life" not "this person Googled me." If you skip research, the email will be generic, and generic emails don't get replies. But the research is fuel, not content.

## Reference Files

- **segment-language.md**  -  Insider vocabulary, daily reality, and conversational patterns per segment. Read this to understand how they talk about their own problems so your research captures the right signals.
- **segment-qualification.md**  -  Proof-based qualification gates per segment
- **Segment cheatsheets** (colocation.md, fiber-operator.md, neocloud.md, network-operator.md, msp-aggregator.md)

## Step 0: HubSpot Deep Pull

**Always start here.** Before running any web searches, check HubSpot for an existing company record using MCP tools (`search_crm_objects`):
- Search by company name or domain
- Pull ALL available fields: `account_brief`, `recent_news_or_trigger_event`, `customer_segment`, `customer_sub_segment`, `segmentation_confidence`, `account_tier`, `state`, `city`, `country`, `hubspot_owner_id`, `notes_last_contacted`, `num_contacted_notes`
- For contacts: pull `email`, `jobtitle`, `hs_linkedin_url`, `notes_last_contacted`, `num_contacted_notes`, `hs_sequences_is_enrolled`, `hs_latest_sequence_enrolled`, `hs_lead_status`, `linked_in_message`
- If `account_brief` exists, read it  -  this is your primary research foundation. But do NOT trust blindly. Verify in Step 1.
- If complete classification exists and data is recent → skip to Step 3 (Contact Research)
- If new account or incomplete data → proceed to Step 1

**Tag every data point with its source:**
- `[HS]`  -  From HubSpot
- `[Apollo]`  -  From Apollo enrichment (note verified/unverified)
- `[Web]`  -  From web search
- `[User]`  -  Provided by user
- `[Missing]`  -  Not found anywhere. Flag for user.

This avoids duplicate research and ensures you're building on what's already in the CRM.

## Step 0.5: Activity Gate (MANDATORY)

Check for active conversations BEFORE proceeding to research. This prevents tone-deaf outreach.

| Field | Threshold | Action |
|---|---|---|
| `notes_last_contacted` within 14 days | **STOP** | "ACTIVE CONVERSATION. Last contacted [date]. Skipping unless overridden." |
| `notes_last_contacted` 15-30 days | **WARNING** | "Recent activity [date]. Check with rep before sending." |
| `notes_last_contacted` 31-60 days | **CAUTION** | Note in summary. Consider referencing prior conversation. |
| `hs_sequences_is_enrolled` = true | **STOP** | "CURRENTLY IN HUBSPOT SEQUENCE. Do not add to Smartlead." |
| `hs_lead_status` = "Connected" or "Open Deal" | **STOP** | "Lead status is [status]. Active relationship. Skip cold outreach." |
| `hs_lead_status` = "Attempted to Contact" | **CAUTION** | Prior outreach attempted. Don't repeat same angle. |
| `linked_in_message` populated | **CAUTION** | LinkedIn already sent. Don't duplicate. |

**Territory check:** After determining HQ state, check territory model. If sender doesn't match territory owner, FLAG: "TERRITORY NOTE: [Company] HQ in [State] = [Territory Owner]'s territory. User specified [Sender]. Proceeding with user's choice."

Territory model: Tim Lieto = East (30 states), Ken Cunningham = West (20 states + DC), Tim Ziemer = International.

## Step 1: Company Research

Run these searches:
1. `[Company] cloud connectivity provisioning` or `[Company] network automation services`
2. `[Company] API portal self-service provisioning`
3. `[Company] cross-carrier connectivity multi-carrier`
4. `[Company] expansion announcement 2025 2026`
5. **Segment verification search** (run if HubSpot segment is unconfirmed or confidence is Low): `[Company] business model infrastructure services` -- verify the company actually belongs in the assigned segment. See `references/segment-qualification.md` for proof signals and disqualification signals per segment. Do not write outreach for a company you can't verify fits the segment.

## Step 2: AI Signal Check

**When to run:**
- Colocation operators: ALWAYS
- Fiber operators in AI corridors (Dallas-Fort Worth, Columbus, Atlanta, Phoenix, Chicago, Memphis): ALWAYS
- Any company marketing "AI-ready" infrastructure

**AI searches:**
1. `[Company] Lambda Labs Crusoe Nebius`
2. `[Company] liquid cooling high-density GPU`
3. `[Company] AI infrastructure 2025 2026`

**Strong AI signals:** GPU cloud tenants confirmed (Lambda Labs, Crusoe, Voltage Park, Together AI, Nebius), liquid cooling / 30kW+ racks, announced GPU cloud partnerships.

**Medium AI signals:** "AI-ready" marketing language, facilities in AI corridors, hiring for GPU cluster roles.

If strong AI signals found: Classify as AI Colocation Operator and use AI messaging track.

**Pre-flagged AI accounts (Tier 1):** Aligned Data Centers, Cologix, EdgeConneX, QTS Data Centers, Vantage Data Centers, Stack Infrastructure.

## Step 3: Contact Research

Search `[Name] [Company] LinkedIn`:
- Current title and tenure
- Career history (where they came from, what they've done)
- Technical vs. business background
- Recent job change (within 6-12 months)

Don't over-research individuals. You need enough to know what they care about and how to frame the conversation.

## Step 4: Document What You Found

```
RESEARCH SUMMARY: [Contact Name] at [Company]

ACCOUNT
Company: [Name]
Segment: [Fiber Operator / Colocation Operator / AI Colocation Operator / Neocloud / Network Operator / MSP-Aggregator]
Customer Sub-Segment: [For Neoclouds: Large-Scale GPU NeoClouds / Tier 1 Inference Providers / AI Infrastructure Providers / Sovereign AI Clouds / Crypto-to-AI Pivots] [For Colos with AI signals: AI Infrastructure] [For others: applicable sub-segment per segment]
What they've built: [Specific services, products, automation, footprint]
The gap: [Where automation stops, what's still manual, cross-carrier challenges]
AI signals: [Found / None]
Recent news: [Anything relevant]

CONTACT
Name: [Full Name]
Title: [Title]
Role type: [Decision-Maker / Technical / Commercial]
Background: [Notable career details]

ANGLE
What this person probably cares about: [Based on role + company gap]
One-sentence positioning: [How MaiaEdge fits their specific situation]
Angle quality check: Does this angle enable research-as-fuel or research display?
  If the angle IS a company fact ("they expanded into 3 states"), it will produce research display.
  Reframe as a problem: "new markets create provisioning bottlenecks" enables fuel.
  "Expansion into 3 states" enables display. Always frame the angle as a PROBLEM, not a fact.

SEGMENT VERIFICATION
HubSpot says: [segment / sub-segment]
Research says: [segment / sub-segment]
Status: VERIFIED | MISMATCH (using [Y] for messaging)

ACTIVITY GATE
Status: CLEAR | WARNING | CAUTION | STOP
Last contacted: [date or N/A]
Lead status: [status]
Sequences enrolled: [Y/N]

DATA SOURCES
Email: [source tag]
LinkedIn: [source tag]
Domain: [source tag]

FIT: EXCELLENT | STRONG | MODERATE | WEAK
```

## What Research Signals Tell You About the Email

Research drives WHICH problem you lead with. It does not appear as "I noticed" observations. The table below shows how each signal informs the problem framing.

| What You Found | How It Shapes the Problem Statement |
|----------------|--------------------------------------|
| Recent promotion or new role | They're inheriting legacy processes. Lead with the operational gap they just walked into. |
| Company announced expansion | Expansion compounds provisioning bottlenecks. Lead with time-to-revenue on new footprint. |
| Technical background, now in leadership | Balance strategic outcome with one technical proof point. They'll respect specificity. |
| Hiring aggressively | "Scaling the team is one way. Scaling without headcount is another." |
| Long tenure at company | They know the provisioning pain intimately. Be direct about the problem, skip the preamble. |
| Came from a carrier or competitor | Cut to the chase. Assume they know the provisioning challenge. Skip education. |
| Recent M&A | Network complexity compounds with every acquisition. Lead with the integration bottleneck. |
| Underutilized fiber (lit, dark, stranded laterals) | "Monetize what you already have in the ground. Instant private fabric across any transport, no routing complexity." |
| Multi-state footprint | "Sell into markets beyond your footprint without building there. Partner interconnection in minutes, not 60-90 days." |
