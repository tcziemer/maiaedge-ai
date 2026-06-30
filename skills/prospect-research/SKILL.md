---
name: prospect-research
description: "Quick pre-outreach research on a specific company and contact for MaiaEdge outreach. Use when preparing to write an email or LinkedIn message for a single prospect. Pulls HubSpot data, runs web research, checks AI signals for colos, researches the contact, and produces a research summary with angle recommendation. NOT for batch enrichment (use company-enrichment) or deep strategy briefs (use account-brief). This is the 5-10 minute research pass that fuels a single email."
---

# MaiaEdge Prospect Research Process

Research every company before writing. No exceptions. Not even for "small" ones.

The entire point of the research is to identify which problem to lead with and confirm you're talking to the right person. The research itself should be invisible in the final email. The prospect should think "yep, that's my life" not "this person Googled me." If you skip research, the email will be generic, and generic emails don't get replies. But the research is fuel, not content.

## Before Starting

One question that materially changes the output: **What's the funnel stage?** Cold first-touch (never spoken), warm re-engagement (prior contact, no active deal), or active-deal prep (use call-prep instead)?

If you have a company and contact and nothing else, ask this one question before proceeding. Sender is set by territory (Step 0.5 reads `context/hubspot/territory-model.md`); signal hypothesis is pulled from HubSpot (Step 0) - neither needs asking.

## Reference Files

- `context/copy-strategy/segment-language.md` - Insider vocabulary, daily reality, and conversational patterns per segment. Read this to understand how they talk about their own problems so your research captures the right signals.
- `context/core/segment-qualification.md` - Proof-based qualification gates per segment.
- **Segment cheatsheets** (`context/segments/colocation.md`, `context/segments/fiber-operator.md`, `context/segments/neocloud.md`, `context/segments/network-operator.md`, `context/segments/msp-aggregator.md`, `context/segments/enterprise.md`)
- `context/outreach/persona-targeting-blocklist.md` - Pre-research persona gate. If the contact title is on the blocklist (Director-Carrier-Wholesale, Director-Field-Operations, Country-Manager-at-HQ-product-org, Account Executive, CSM), surface in the Cooper-review queue rather than producing an outreach package. See Step 0a below.
- `context/outreach/pre-cadence-hygiene.md` - Pre-research hygiene gates. LinkedIn-status check on lead pull catches stale roles before research is invested.
- `context/account-tiering/sub-segment-qualification.md` - Authoritative list of the 30 active `company_sub_segment` values. Use the exact case-sensitive HubSpot string for any sub-segment reference.
- `context/account-tiering/enrichment-protocols.md` - Canonical definitions of `account_brief`, `recent_news_or_trigger_event`, `fabric_provisioning_approach`, and `geographic_focus` - the four enriched fields the research check pulls from.
- `context/sales/marketplace-seeding-strategy.md` - Federation marketplace seeding playbook. Read when the prospect is partnership-track (MSP/Aggregator or Fiber pursuing federation) - it shapes the angle recommendation.
- `context/account-tiering/icp-deep-dives/B-and-C-[segment].md` (if available) - Optional deep background: per-sub-segment markers, anchors, disqualifiers. Pull in only when sub-segment classification confidence is the open question; not required reading.
- `context/hubspot/territory-model.md` - Authoritative 5-region territory map. Use to route sender assignment by HQ state/country (replaces any inline state-to-owner lookup).
- `context/outreach/email-writing-rules.md` - Load-Bearing Assumption Gate authority; angle-quality rules; banned phrases.
- `context/outreach/sender-profiles.md` - Per-sender Craft Register and voice rules.
- `context/signals/outreach-signal-pushback.md` - Signal push-back write semantics, scoring rubric, and `compute_signal_heat` spec. The Final Step reads this as the canonical source.
- `context/hubspot/contact-schema.md` - Contact field reference for HubSpot reads and writes.
- `context/hubspot/property-schema.md` - Company property definitions; 8-field enrichment set; `signal_heat` enum.
- `context/signals/signal-framework.md` - Signal scoring tiers (U1-U6, AP, FR classes); source reliability tiers.
- `context/core/icp-playbook.md` - Per-segment worked examples, persona pain points, and angle selection.

## Step 0a: Persona Pre-Check (Mandatory)

Before any research investment, verify the contact title is NOT on the persona-targeting blocklist (`context/outreach/persona-targeting-blocklist.md`):

- **Universal blocks:** Account Executive, Account Manager, Customer Success Manager.
- **Aggregator / NaaS / TSD blocks:** Director - Carrier Wholesale, Wholesale Manager, Director - Sales (Wholesale).
- **Fiber / ISP blocks:** Director - Field Operations, GM / Regional Operations Manager.
- **International carrier blocks:** Country Manager / GM - [Country] at carriers with HQ product orgs, Finance Director / Treasurer.

If blocked, surface to the Cooper-review queue and do not run Steps 0.5 through 3. The blocklist saves 5-10 minutes of research per blocked contact and prevents the wrong-persona reply pattern (Mark Palma @ iTel "not my purview," Mark Thornton @ Truvista hostile unsubscribe) that consumed 15% of the 60-day corpus replies.

## Step 0b: LinkedIn-Status Check (per pre-cadence-hygiene.md Filter 3)

At list-pull time, verify the contact's current LinkedIn role matches the source list. If different (retired, moved companies, role change), flag for re-research before proceeding to Step 0.5. Catching this here avoids the Dave Furiness @ MCNC pattern (retired contact still in prospect list).

## Step 0: HubSpot Deep Pull

**Always start here.** Before running any web searches, check HubSpot for an existing company record using MCP tools (`search_crm_objects`):
- Search by company name or domain
- Pull ALL available fields: `account_brief`, `recent_news_or_trigger_event`, `customer_segment`, `customer_sub_segment`, `segmentation_confidence`, `account_tier`, `signal_heat`, `state`, `city`, `country`, `hubspot_owner_id`, `notes_last_contacted`, `num_contacted_notes`
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
| `notes_last_contacted` 15-45 days | **WARNING** | "Recent activity [date]. Active conversation - flag for rep review before sending." |
| `notes_last_contacted` 46-60 days | **CAUTION** | Note in summary. Consider referencing prior conversation. |
| `hs_sequences_is_enrolled` = true | **STOP** | "CURRENTLY IN HUBSPOT SEQUENCE. Do not add to Smartlead." |
| `hs_lead_status` = "Connected" or "Open Deal" | **STOP** | "Lead status is [status]. Active relationship. Skip cold outreach." |
| `hs_lead_status` = "Attempted to Contact" | **CAUTION** | Prior outreach attempted. Don't repeat same angle. |
| `linked_in_message` populated | **CAUTION** | LinkedIn already sent. Don't duplicate. |

**Territory check:** After determining HQ state/country, load `context/hubspot/territory-model.md` and resolve the territory owner at runtime. If sender doesn't match territory owner, FLAG: "TERRITORY NOTE: [Company] HQ in [State/Country] = [Territory Owner]'s territory. User specified [Sender]. Proceeding with user's choice."

## Step 1: Company Research

Run these searches:
1. `[Company] cloud connectivity provisioning` or `[Company] network automation services`
2. `[Company] API portal self-service provisioning`
3. `[Company] cross-carrier connectivity multi-carrier`
4. `[Company] expansion announcement 2025 2026`
5. **Segment verification search** (run if HubSpot segment is unconfirmed or confidence is Low): `[Company] business model infrastructure services` -- verify the company actually belongs in the assigned segment. See `context/core/segment-qualification.md` for proof signals and disqualification signals per segment. Do not write outreach for a company you can't verify fits the segment.

### Enterprise (Multi-DC ICP) Research Route

When the HubSpot segment is `Enterprise-CustomerSegment` (or research suggests a multi-DC enterprise in financial services / healthcare / retail / outsourcing), run these instead of/in addition to the operator-route searches:

1. **DC footprint confirmation:** `[Company] data center locations` / `[Company] 10-K data center disclosure` / `site:sec.gov [Company] data center` - confirm 3+ DCs (scale gate). For public companies, 10-K filings often disclose DC count in Item 2 (Properties).
2. **In-house network engineering signal:** `[Company] "VP Network Infrastructure"` / `[Company] "Director Network Engineering"` / `[Company] "Principal Network Engineer" LinkedIn` - confirm in-house net eng team. NOC presence ("[Company] NOC operations 24/7") is equally strong.
3. **Third-party fabric dependency:** `[Company] Equinix Fabric customer` / `[Company] Megaport customer` / `Equinix customer logo [Company]` - confirm the third-party fabric they depend on (drives the cloud on-ramp angle).
4. **Recent trigger event** (Tier 2 ceiling gate): `[Company] M&A 2026` / `[Company] AI workload announcement` / `[Company] CIO hire` / `[Company] data center expansion` - recent trigger (M&A, AI workload, leadership change, DC expansion) ≤6 months is the Tier 2 trigger criterion.
5. **Regulatory exposure signals** (for sub-segment-specific angle): HIPAA breach disclosures (HHS portal for healthcare), PCI audit findings (news), GDPR enforcement (EU regulator news), SOX disclosures (10-K risk factors for financials).
6. **Sub-segment verification:** match the company against `context/segments/enterprise.md` four ICP sub-segments. **Confirm exclusions:** if the company is Manufacturing, Energy/Utilities, Logistics/Supply Chain, Government/Defense, or SaaS-only - DO NOT classify as Enterprise (Watch List or out of scope). If the company is a pure consulting firm (Deloitte, McKinsey, BCG, Bain), it is NOT `Outsourcing Services - Enterprise` regardless of multi-site presence.

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

**Get the contact's email + LinkedIn URL.** If Step 0's HubSpot pull didn't return the contact's `email` or `hs_linkedin_url` - or the rep asks for them directly - fetch from Apollo via the Apollo MCP: `apollo_people_match` by name + company domain reveals the verified email + `linkedin_url`. Use VERIFIED email only (skip unverified / unknown / invalid statuses and say so); tag the source `[Apollo, verified]` vs `[HubSpot]`. To find NET-NEW people at the account (not just the named contact), hand off to `contact-discovery`.

## Step 4: Document What You Found

```
RESEARCH SUMMARY: [Contact Name] at [Company]

ACCOUNT
Company: [Name]
Signal Heat: [Hot / Warm / Cool / Cold]   ← from HubSpot `signal_heat` (Title Case enum); see context/account-tiering/tier-compute-spec.md §11.5 for definition. Reps sort daily by this; a `Cold` account on a target list signals strategic pin without current intent.
Segment: [Fiber Operator / Data Center Colo Provider / NeoCloud / Network Operator(Tier 1 / VNO) / MSP/Aggregator / Enterprise-CustomerSegment]
Customer Sub-Segment: [Use one of the 30 active HubSpot `company_sub_segment` values per `context/account-tiering/sub-segment-qualification.md` - e.g., for NeoCloud: `Large Scale GPU - Neocloud` / `Tier 1 Inference - Neocloud` / `AI Infrastructure providers - Neocloud` / `Sovereign AI Clouds - Neocloud` / `Crypto to AI - Neoclouds`; for AI-signal colos: `AI Signals - colo`; for Enterprise: `Financial Services - Enterprise` / `Healthcare Systems - Enterprise` / `Retail and Distribution - Enterprise` / `Outsourcing Services - Enterprise`; cross-segment `Greenfield` pairs with `Data Center Colo Provider` OR `NeoCloud` parent]
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
Load-bearing assumption check: name the ONE thing this angle assumes is true about how their business works today (e.g. "they resell circuits and don't own a network"). Verify it against a source before recommending the angle. If a capable team at their scale has plausibly already solved it, assume they did until a source proves otherwise, and angle on the gap that survives their competence (per-customer / productization / reach-beyond-footprint). If you cannot verify it, flag the angle UNVERIFIED so the writer reframes forward-state. See `context/outreach/email-writing-rules.md` § The Load-Bearing Assumption Gate.

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
| Enterprise: recent DC expansion or new DC announcement | Frame as the dark fiber redundancy moment. "Your DR strategy assumes the dark fiber is redundant. It is not - unless you've got diverse fibers and automated failover at each new site." |
| Enterprise: M&A activity | Network integration angle. "Two routing stacks, two carriers, two engineering teams now sharing a fabric the integration plan didn't budget for." |
| Enterprise: new VP Network / CIO hire | New leadership inheriting legacy provisioning. "First 90 days the conversation is usually about the inter-DC paths nobody's looked at since the SD-WAN cutover." |
| Enterprise: Equinix Fabric or Megaport customer | Frame the third-party SLA hand-off. "Cloud on-ramp goes through Megaport. Your team owns the SLA." |
| Enterprise: regulated vertical + recent compliance event (HIPAA breach, PCI audit, GDPR action) | Audit-trail framing. "Compliance is asking you to prove where the data went. With BGP, you can't - beyond a routing table." |
| Enterprise: AI workload announcement | Inter-DC determinism angle. "AI is pulling traffic in directions you did not design for. The middle mile is the place where best-effort hurts." |

---

## Final Step: Signal Push-Back to HubSpot

**Inviolable rule:** this step runs AFTER Step 4 ("Document What You Found") (the Research Summary block) has been delivered to the rep. The push-back must never gate, delay, or alter the primary output. If anything in this step fails, the rep already has their research summary in hand; signal-engine staleness is a routine-recovery problem, not a rep-blocker. Skip silently on any failure; the next R-Tier-Audit run reconciles the signal fields.

### When to write back

During Steps 1-2 (company + contact research), you ran web search and (optionally) web fetch. If that research surfaced a **signal-grade event** - funding round, exec hire, M&A, facility/market launch, public outage / RCA, earnings-language shift, or any U1-U6 / AP / FR class in `context/signals/signal-framework.md` - score it against the Signal Scan rubric (Tier x Freshness x Confidence). **Only events scoring ≥8 trigger the push-back.** Sub-8 noise stays silent.

### Comparison gate (write only if fresher)

Read current `last_signal_date` for this company via `mcp__claude_ai_HubSpot__get_crm_objects`. If your discovered **event date** is strictly newer than HubSpot's value (or HubSpot's value is null), proceed. Otherwise no write. Idempotent no-op.

### The write block

One `mcp__claude_ai_HubSpot__manage_crm_objects` call. `updateRequest.objects[]`, `objectType: "companies"`, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`. Fields:

- `recent_news_or_trigger_event` - pure narrative, no date prefix. Format: `"[Signal Type] - [one-line summary]"`. 2-4 sentences, ≤250 char hard cap.
- `last_signal_date` - the **event date** (YYYY-MM-DD), extracted from the source article. Event date, NOT today's run date.
- `last_signal_score` - your rubric score (number, typically 0-60).
- `signal_count_last_30d` - read current value. If current `last_signal_date` is within 30d of your new event date, increment by 1. If current is null or >30d old, write 1.
- `signal_heat` - recompute per `context/signals/outreach-signal-pushback.md`. **Title Case enum:** `Hot` / `Warm` / `Cool` / `Cold`. Lowercase is silently rejected.
- `account_tier` - recompute per `context/account-tiering/tier-compute-spec.md` §4. **Only write if `hs_is_target_account != true`** - flag freezes tier (heat continues regardless).

### `compute_signal_heat`

Use the canonical algorithm in `context/signals/outreach-signal-pushback.md` (also at `context/account-tiering/tier-compute-spec.md` §11.5). Do not inline a local copy - always read from the canonical source to stay current.

Heat writes are idempotent - skip if `computed_heat == current_heat`.

### Stamping policy

**Do NOT bump `last_enriched_date`.** Outreach-time signal push-backs are partial writes, not full enrichment passes. R2's 120-day rotation owns the freshness guarantee.

### Audit log

Add a HubSpot company note alongside the field writes:

```
Signal push-back from prospect-research on YYYY-MM-DD: discovered <signal type> event YYYY-MM-DD, score <N>. Heat <prior> -> <new>. Tier <prior> -> <new>.
```

### Failure handling

If any MCP call fails: log to run report under "Signal push-back deferred" and continue. The rep already has their research summary. R-Tier-Audit reconciles next run. **Never surface push-back failures to the rep as a blocker.**
