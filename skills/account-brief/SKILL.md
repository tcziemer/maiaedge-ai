---
name: maiaedge-account-brief
description: MaiaEdge account strategy brief generator for high-value prospect research. Use when creating account research briefs, prospect strategy documents, or preparing for strategic account pursuit. Generates structured briefs with qualification, contact strategy, outreach drafts, value proposition mapping, technical fit assessment, and discovery prep. Outputs professional Word document (.docx) plus ready-to-send outreach.
---

# MaiaEdge Account Strategy Brief

Generate comprehensive account strategy briefs for high-value MaiaEdge prospects.

## Before Starting - Clarification

Three inputs that change the brief materially:

1. **Account and segment** - what company, which segment (Colo / Fiber / Network Op / NeoCloud / MSP / Enterprise)? Share the HubSpot name or ID to pull existing tier and signal data.
2. **Cold or warm** - cold approach, follow-up after a first call, or prep for an upcoming meeting? Determines how the outreach draft is framed.
3. **Known contacts** - specific names/titles to build the Contact Matrix around, or should contact discovery be part of the output?

Coach: if you give too little, share company name, segment, and cold-vs-warm - that's enough to begin.

## Reference Files

- `context/copy-strategy/segment-language.md` - Insider vocabulary, daily reality, conversational patterns per segment. Read before writing angles, outreach drafts, or discovery questions to sound like a peer, not a salesperson.
- `context/core/segment-qualification.md` - Proof-based qualification gates
- **Segment cheatsheets** (`context/segments/colocation.md`, `context/segments/fiber-operator.md`, `context/segments/neocloud.md`, `context/segments/network-operator.md`, `context/segments/msp-aggregator.md`, `context/segments/enterprise.md`)
- `context/outreach/email-writing-rules.md` - For the ready-to-send email draft (angle-first, segment lock, no credibility anchors)
- `context/core/competitive-positioning.md` + `context/core/differentiation-naas-aggregator.md` - The objection bank for the Discovery & Objection Prep section. NaaS / fabric / aggregator objections are answered from `context/core/differentiation-naas-aggregator.md`'s written register; never improvise federation mechanics.
- `context/hubspot/territory-model.md` - State-to-owner mapping for the recommended owner in the brief.
- `context/sales/marketplace-seeding-strategy.md` - Federation marketplace seeding playbook. Read for partnership-track prospects (MSP/Aggregator and Fiber segments pursuing federation) - it supplies the first-mover / geography angle.
- `context/sales/edge-ai-thesis-montauk.md` + `context/product/ai-market-positioning.md` - Business-case validation and AI-inference positioning for AI-adjacent prospects (neocloud, AI-signals colo).
- `context/account-tiering/icp-deep-dives/B-and-C-[segment].md` (if available) - Optional deep background: per-sub-segment quantitative markers, anchors, and disqualifiers. Pull in only when the brief needs sub-segment-level depth; not required reading.
- `context/product/proof-points.md` - Customer proof points (NTT, RevNet, Arvig, etc.) cited in Section 4 Value Proposition. Load before writing proof-point bullets.
- `context/outreach/sender-profiles.md` - Per-sender Craft Register and territory. Used when writing the outreach draft in Section 3.
- `context/outreach/voice-gold-standard.md` - Tone and voice calibration for the email draft.
- `context/core/icp-playbook.md` - Per-segment worked examples and persona pain points for the Contact Matrix and Discovery Prep sections.
- `context/signals/outreach-signal-pushback.md` - Canonical signal push-back spec. The inline `compute_signal_heat` block and write logic in the "Final Step" section of this skill **must stay in sync with this file**. If the two diverge, `context/signals/outreach-signal-pushback.md` is authoritative.

## Output Format

Deliver as:
1. **Word document** (.docx) with professional formatting
2. **Summary in chat** with key highlights
3. **Ready-to-send email** for primary contact

## Brief Structure

### Section 1: Quick Qualification

**Purpose:** Should we pursue this? How much effort is justified?

| Field | Options |
|-------|---------|
| Company | Name, segment, HQ |
| Account Tier | `tier_1` - `tier_5` (from HubSpot `account_tier`) |
| Signal Heat | `Hot` / `Warm` / `Cool` / `Cold` (Title Case; from HubSpot `signal_heat`; see `context/account-tiering/tier-compute-spec.md` §11.5). Tier = strategic value; heat = current intent. A `tier_1` + `Cold` account is strategic but quiet; `tier_3` + `Hot` is opportunistic. |
| Deal Tier | Strategic / Large / Mid / Small |
| Contract Potential | POC only / 1-year / Multi-year expansion |
| Technical Fit | Deploy now / 6-12 months / Long-term / Disqualified |
| Fit Assessment | Excellent / Strong / Moderate / Weak / Pass |
| Research Depth | Deep (2+ hrs) / Standard (1 hr) / Quick (30 min) |

**Red Flags / Disqualifiers:**
- No infrastructure where PBCs deploy
- Already locked into Megaport/Equinix long-term
- No cross-carrier or customer connectivity need
- Too early stage (no customers yet)

*If "Pass" → Stop here, document why, move on.*

---

### Section 2: Contact Strategy

**Purpose:** Who to engage and why. Validate before deep research.

**Primary Contact:**
- Name, title, email, LinkedIn URL
- Why them (owns the problem, relationship exists, accessible)
- Contact-to-use-case fit: ✅ Strong / ⚠️ Partial / ❌ Mismatch

**Pulling contact details:** read `email` + `hs_linkedin_url` from HubSpot first. When they're missing - or the rep asks for the committee's emails / LinkedIn URLs - fetch from Apollo via the Apollo MCP: `apollo_people_match` by name + company domain reveals the verified email + `linkedin_url`. Use VERIFIED email only and tag the source (`[Apollo, verified]` / `[HubSpot]`). To map the full buying committee or fill persona gaps, compose on `contact-discovery` rather than re-implementing the search here.

**Existing Relationship (if any):**
- Who knows them (Tim L, Tim Z, Abilash, other)
- Context (sold to them before, met at event, warm intro)
- Approach: Warm reconnect vs. cold outreach

**Contact Validation Table:**

| Contact | Their Domain | MaiaEdge Use Case | Fit |
|---------|--------------|-------------------|-----|
| [Name] | [What they own] | [Use case to pitch] | ✅/⚠️/❌ |

**Backup Contacts:** If primary doesn't fit or respond.

*If no contact fits the use case → flag it, reconsider approach or deprioritize.*

---

### Section 3: Outreach (Ready to Execute)

**Purpose:** Action-oriented, send this week.

**Contents:**
- Email draft for primary contact (per MaiaEdge Email Bot guidelines)
- Subject line options (2-3)
- LinkedIn request (if applicable)
- Warm intro draft (if relationship exists)
- Timing trigger: Why now?

---

### Section 4: Value Proposition (Account-Specific)

**Purpose:** What to say when they reply.

**Contents:**
- **For the company:** 2-sentence value prop
- **For primary contact:** Role-specific, in their language
- **Lead use case:** The ONE use case to open with
- **Supporting use cases:** 1-2 others if traction
- **Proof points:** Which references to cite (NTT, RevNet, Arvig)
- **Competitive positioning:** Why MaiaEdge vs. alternatives

---

### Section 5: Company Context

**Purpose:** Background to sound credible in conversations.

**Contents:**
- Business model (what they sell, how they make money)
- Scale (revenue, funding, employees, footprint)
- Infrastructure they operate
- Key partnerships/customers
- Recent news (last 12 months)
- What they've built (acknowledge strengths)
- The gap (where MaiaEdge fits)

---

### Section 5.5: Enterprise-Specific Context (use ONLY when segment = Enterprise Multi-DC ICP)

When the account is `customer_segment = "Enterprise-CustomerSegment"`, replace the generic Section 5 fields with this Enterprise-specific block. Skip this section entirely for operator segments.

**Sub-segment (must be one of):** `Financial Services - Enterprise` / `Healthcare Systems - Enterprise` / `Retail and Distribution - Enterprise` / `Outsourcing Services - Enterprise`.

**Hard gate check (BOTH must be confirmed in research):**
- Vertical: one of the four ICP sub-segments. If Manufacturing / Energy-Utilities / Logistics / Government / SaaS-only → not Enterprise ICP.
- Scale: $1B+ revenue AND (3+ DCs OR direct Equinix Fabric / Megaport port OR confirmed in-house net eng).

**DC footprint:** Number of data centers, geographic distribution, any DCs disclosed in 10-K Item 2 (Properties) for SOX-regulated public companies. Note new-DC announcements in the last 12 months.

**Current fabric posture (semantic flip for Enterprise - what they CONSUME):** Megaport user? Equinix Fabric customer? PacketFabric / Console Connect? Carrier-managed (AT&T, Verizon, Lumen, BT, NTT)? Self-built corporate WAN? How is cloud on-ramp handled today and who owns the SLA?

**Regulatory framework:** HIPAA + HITRUST for healthcare; SOX + PCI-DSS for financial services; GDPR if EU operations; client-specific compliance for outsourcing services (often a mix of HIPAA / PCI-DSS / SOX / GDPR depending on client portfolio).

**AI / GPU strategy (if any):** AI workload announcements, GPU infrastructure investments, multi-cloud migration kickoffs. Pulls inter-DC traffic in directions the network team didn't design for.

**Recent network-relevant events:** M&A activity, new VP Network / CIO / CSO hires (last 6 months), DC expansion announcements, AI workload kickoffs, regulatory pressure events (HIPAA breach disclosures, PCI audit findings, GDPR actions).

**Account tier note:** Enterprise records cap at Tier 2 unless an exceptional trigger emerges. There is no Tier 1 path. Tier 2 requires `high_90` confidence + $1B+ revenue + 3+ DCs + in-house net eng + recent trigger event ≤6 months. Tier 3 is most baseline-qualified Enterprise records. Reflect this in the Quick Qualification table at Section 1.

**Lead angle by sub-segment** (use this for Section 4 Value Proposition mapping):
- **Retail and Distribution**: dark fiber redundancy between corporate DCs first, cloud on-ramp under enterprise control second.
- **Financial Services**: deterministic inter-DC paths + audit-ready policy enforcement (SOX / PCI-DSS / GDPR) + cloud on-ramps under enterprise control.
- **Healthcare Systems**: diverse dark fiber redundancy between EHR DCs + HIPAA-aligned policy control + cloud on-ramps for radiology / analytics.
- **Outsourcing Services**: delivery-center reliability + client data sovereignty + dark fiber redundancy between primary delivery hubs.

**Personas to prioritize for Section 7 Contact Matrix:**
- Technical Champion: VP Network Infrastructure / Director Network Engineering / Principal Network Engineer
- Economic Buyer: CIO (or CTO at retail/healthcare)
- Security Stakeholder: CSO / CISO
- Compliance (regulated verticals only): Chief Compliance Officer / VP Risk

---

### Section 6: Timing Fit

**Purpose:** Why is right now a good time for this company to be looking at MaiaEdge? This section must be research-driven  -  not generic urgency language. If you can't find real signals, say so and flag low timing confidence.

**Company-Level Timing Signals (research required):**
- Recent expansion, new markets, or footprint announcements
- Recent funding round or new capital (runway to invest in infrastructure)
- New product line or service launch that requires faster provisioning
- Recent acquisition or merger (network complexity just compounded)
- Competitive pressure signals (losing deals to faster operators, Tier 1s going direct)
- Hiring patterns that suggest scaling pains (ops headcount growing without automation)
- Partnership announcements that imply cross-carrier connectivity need
- Public statements from leadership about where the company is heading

**Contact-Level Timing Signals (research required, per contact):**
- New role or recent promotion (setting priorities, open to new vendors)
- New responsibility or expanded scope (inherited a problem they didn't create)
- LinkedIn or public statements about provisioning, automation, or scaling pain
- Career background that makes the MaiaEdge problem immediately familiar

**Output format:**

> **Company timing:** [2-3 sentences. Specific signals from research. What's happening at this company right now that makes this a timely conversation? If nothing strong found, say: "No strong timing signals found  -  approach is based on ICP fit, not urgency."]

> **Contact timing:** [Per contact if multiple. What's happening with this specific person right now that creates an opening? If nothing found, flag it.]

> **Timing confidence:** Strong / Moderate / Weak  -  with one-line rationale

---

### Section 7: Contact Matrix

**Purpose:** For every named contact at this account, map what they actually care about to the best MaiaEdge angle for them  -  grounded in both the account segment and what's actually happening at this company right now. Not generic role descriptions. If the angle could apply to anyone with this title anywhere, rewrite it.

**Instructions:**
- Pull from company research AND contact research (background, tenure, career path, public statements)
- Map angle to the account segment (Fiber Operator, Colo, MSP, etc.)  -  messaging should reflect segment-specific pain
- If multiple contacts, include all of them in the matrix
- Flag if any contact is a poor fit for direct outreach (e.g., capital markets / finance role  -  suggest intro path instead)

| Contact | Title | What They Care About | Best MaiaEdge Angle (account + segment specific) | Fit | Outreach Priority |
|---------|-------|---------------------|--------------------------------------------------|-----|-------------------|
| [Name] | [Title] | [Role-specific + company-context specific] | [The single most relevant angle for this person at this company right now] | ✅/⚠️/❌ | Primary / Secondary / Intro Path |

**Angle quality check:** Before finalizing each row, ask: "Could this angle have been written for a different person at a different company?" If yes, make it more specific. Then name the one assumption each angle depends on about how their business works (e.g. they resell vs. already own a network) and verify it against a source. If a capable team at their scale has plausibly already solved it, assume they did and angle on the surviving gap. See `context/outreach/email-writing-rules.md` § The Load-Bearing Assumption Gate.

---

### Section 8: Technical Fit Assessment

**Purpose:** Can we actually deploy here?

| Field | Assessment |
|-------|------------|
| Infrastructure type | Colo / Fiber / Carrier PoPs / Cloud regions / Edge |
| Where PBCs deploy | Specific locations if known |
| Cross-carrier need | Yes / No / Unclear |
| Customer connectivity need | Yes / No / Unclear |
| Integration complexity | Low / Medium / High |
| Timeline to deploy | Immediate / 6 months / 12+ months |

**Technical Red Flags:**
- [ ] No physical infrastructure (pure software/platform)
- [ ] Single-site only
- [ ] Already automated cross-carrier
- [ ] Locked into competing platform

---

### Section 9: Discovery & Objection Prep

**Purpose:** Prep for first real conversation.

**Opening Questions:**
- "How do customers connect to [platform] today?"
- "What's the timeline for new customer connectivity?"

**Pain Validation:**
- "Where does provisioning slow down?"
- "What happens when a deal requires cross-carrier paths?"

**Objection Handling Table:**

| Objection | Response |
|-----------|----------|
| "We're building our own" | [Account-specific response] |
| "We use Megaport/Equinix" | [Account-specific response] |
| "Who else uses this?" | [Proof points] |

---

### Section 10: Deal Execution

**Purpose:** Path after first meeting.

**Contents:**
- Entry point: Primary contact
- Technical validation: Who approves architecture
- Executive sponsor: Who signs
- POC scope: What pilot looks like
- Expansion potential: Where it goes after initial win
- Internal MaiaEdge team: Who owns account? Need Abilash/Tim Z?

---

## Research Process

### Phase 1: Quick Qualification (before deep research)

Run these searches to determine if account is worth pursuing:

```
[Company] business model
[Company] funding valuation 2024 2025
[Company] network infrastructure connectivity
```

Assess fit. If Pass → stop. If pursuing → continue.

### Phase 2: Contact Identification

```
[Company] leadership team executives
[Company] CTO VP Engineering infrastructure
[Contact name] LinkedIn
```

Validate contact-to-use-case fit before proceeding.

### Phase 3: Deep Research (if warranted)

```
[Company] network automation provisioning API
[Company] cross-carrier connectivity multi-carrier
[Company] customer connectivity interconnection
[Company] Megaport Equinix fabric partnership
[Company] expansion announcement 2024 2025
[Company] [specific product/platform] architecture
```

For AI infrastructure targets, add:
```
[Company] Lambda Labs Crusoe GPU cloud
[Company] liquid cooling high-density
```

---

## Quality Checklist

Before finalizing brief:

**Qualification:**
- [ ] Fit assessment justified with evidence
- [ ] Red flags documented if present
- [ ] Research depth matches deal tier
- [ ] Each angle's load-bearing assumption verified against a source or reframed (assume competence; never assert they have not already solved the problem without a source)

**Contact Strategy:**
- [ ] Primary contact validated against use case
- [ ] Existing relationships captured
- [ ] Backup contacts identified

**Outreach:**
- [ ] Email follows MaiaEdge Email Bot guidelines
- [ ] No em dashes
- [ ] NO credibility anchors in cold email (no Acme Packet, no 128 Technology)
- [ ] Company-specific angle drives the email (not segment template)
- [ ] CTA is low-friction
- [ ] Within word count for segment

**Value Prop:**
- [ ] Lead use case identified (not a list of 4 equal options)
- [ ] Claims based on research, not assumptions
- [ ] Acknowledges what they've built before identifying gap

**Technical Fit:**
- [ ] Deployment locations identified
- [ ] Cross-carrier/customer connectivity need validated
- [ ] Red flags checked

---

## Segment Reference

| Segment | Primary Hook | Key Use Case |
|---------|--------------|--------------|
| Fiber Operators | "Monetize underutilized fiber. Instant private fabric any transport, no routing complexity. Sell new services (cloud on-ramp)." | Monetize idle/stranded fiber, productize private paths, enable cloud on-ramp |
| Colos | "Build your own fabric. Automated virtual cross-connects + cloud on-ramp under your brand, no multi-year development project." | Automated cross-connects, services layer, multi-site fabric, cloud on-ramp as native product |
| AI Colos | "GPU tenants deploy dense interconnection fast. The connectivity layer either keeps up or becomes the gap in the facility." | Deterministic paths between AI sites, automated cross-connects for GPU tenants, cloud on-ramps for GPU workloads. Modular DC + greenfield variants apply. |
| Tier 1 Carriers | "Sell beyond your footprint. Monetize existing infrastructure." | Extend reach, cross-carrier paths |
| MSPs/VNOs | "Visibility, reach into new markets, services to sell" | Upstream carrier visibility, monetize capacity |
| Neoclouds (in-pain-now, 5-15 sites) | "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between." | Multi-tenancy, deterministic paths, observability as supporting benefit |
| Neoclouds (scaling-wall, 15+ sites hyperscaler-heavy) | "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." | Instant customer on-ramp, enterprise-ramp velocity, private cloud connectivity |
| Neoclouds (early-growth, crypto-to-AI) | "Bitcoin doesn't care about latency. Enterprise AI tenants do." | Tenant-readiness + basic connectivity + observability |
| Enterprise - Retail and Distribution (Multi-DC ICP) | "Your dark fiber between corporate DCs is one cut from an outage. Diverse fibers and automated failover, no BGP across the WAN." | Dark fiber redundancy that is actually redundant + cloud on-ramp under enterprise control |
| Enterprise - Financial Services | "Inter-DC paths are best-effort. Compliance is asking you to prove the path." | Deterministic inter-DC paths + audit-ready policy enforcement (SOX/PCI-DSS/GDPR) + cloud on-ramps under enterprise control |
| Enterprise - Healthcare Systems | "EHR DC redundancy depends on a single fiber pair. PHI rides that path." | Diverse dark fiber redundancy between EHR DCs + HIPAA-aligned policy control + cloud on-ramps for radiology/analytics |
| Enterprise - Outsourcing Services | "Your clients' regulators are asking where their data went. You have a BGP routing table." | Delivery-center reliability + client data sovereignty + dark fiber redundancy between primary delivery hubs |

---

## Final Step: Signal Push-Back to HubSpot

> **Sync note:** the inline `compute_signal_heat` spec and write-field list in this section are a local copy of `context/signals/outreach-signal-pushback.md`. If the two diverge, `context/signals/outreach-signal-pushback.md` is authoritative.

**Inviolable rule:** this step runs AFTER the 10-section strategy brief has been delivered to the rep. The push-back must never gate, delay, or alter the primary output. If anything in this step fails, the rep already has their brief in hand - signal-engine staleness is a routine-recovery problem, not a rep-blocker. Skip silently on any failure; the next R-Tier-Audit run reconciles the signal fields.

**Why account-brief is the highest-value push-back surface:** the 10-section brief is the deepest signal-rich research the toolkit produces. Trigger events, exec moves, M&A, funding, facility launches - all of these surface during account-brief research. Pushing them back into HubSpot at the end means every brief generation refreshes the engine.

### When to write back

During the deep research that produced sections like Trigger Events, Recent News, Funding & Capital, M&A, Strategic Moves, etc., you almost certainly surfaced **signal-grade events** - funding round, exec hire, M&A, facility/market launch, public outage / RCA, earnings-language shift, or any U1-U6 / AP / FR class in `context/signals/signal-framework.md`. Score each event against the Signal Scan rubric (Tier × Freshness × Confidence). **Pick the single highest-scored event ≥8** for the push-back. Sub-8 events stay in the brief but don't drive the push-back.

### Comparison gate (write only if fresher)

Read current `last_signal_date` for this company via `mcp__claude_ai_HubSpot__get_crm_objects`. If your discovered **event date** is strictly newer than HubSpot's value (or HubSpot's value is null), proceed. Otherwise no write. Idempotent no-op.

### The write block

One `mcp__claude_ai_HubSpot__manage_crm_objects` call with `updateRequest.objects[]`, `objectType: "companies"`, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`. Fields:

- `recent_news_or_trigger_event` - pure narrative, no date prefix. Format: `"[Signal Type] - [one-line summary]"`. 2-4 sentences, ≤250 char hard cap.
- `last_signal_date` - the **event date** (YYYY-MM-DD), extracted from the source article or research note. Semantics narrowed 2026-05-28 - event date, NOT today's run date.
- `last_signal_score` - your rubric score (number, typically 0-60).
- `signal_count_last_30d` - read current value. If current `last_signal_date` is within 30d of your new event date, increment by 1. If current is null or >30d old, write 1.
- `signal_heat` - recompute per the inlined spec below. **Title Case enum:** `Hot` / `Warm` / `Cool` / `Cold`. Lowercase is silently rejected.
- `account_tier` - recompute per `context/account-tiering/tier-compute-spec.md` §4. **Only write if `hs_is_target_account != true`** - flag freezes tier (heat continues regardless).

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

Heat writes are idempotent - skip if `computed_heat == current_heat`.

### Stamping policy

**Do NOT bump `last_enriched_date`.** Outreach-time signal push-backs are partial writes, not full enrichment passes. R2's 120-day rotation owns the freshness guarantee.

### Audit log

Add a HubSpot company note alongside the field writes:

```
Signal push-back from account-brief on YYYY-MM-DD: discovered <signal type> event YYYY-MM-DD, score <N>. Heat <prior> -> <new>. Tier <prior> -> <new>.
```

### Failure handling

If any MCP call fails: log to run report under "Signal push-back deferred" and continue. The rep already has their brief. R-Tier-Audit reconciles next run. **Never surface push-back failures to the rep as a blocker.**

---

## References

- Consult the cold-email skill (`skills/cold-email/SKILL.md`) for email copywriting guidelines
- Consult segment cheatsheets for detailed pain points and personas: `context/segments/colocation.md`, `context/segments/fiber-operator.md`, `context/segments/neocloud.md`, `context/segments/network-operator.md`, `context/segments/msp-aggregator.md`, `context/segments/enterprise.md`
