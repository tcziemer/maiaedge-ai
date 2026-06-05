---
name: segment-classification
description: Classify companies into MaiaEdge customer segments and apply segment-specific messaging. Use when determining what type of company a prospect is (fiber operator, colocation, neocloud, network operator, MSP) and what messaging angle to use. Includes exclusion list and segment-specific pain points, angles, and positioning.
---

# MaiaEdge Segment Classification & Messaging

## What MaiaEdge IS

MaiaEdge is an infrastructure provider. We give network operators the tools to build and deliver their own private connectivity services. The operator keeps the customer, the invoice, the brand, the margin. We're the infrastructure behind their service, not the service itself.

**The product:**
- **PBC (Path Border Controller):** 1RU edge device. Dual 100 Gbps. AES-256-GCM encryption. Protocol-free forwarding. Merged L2/L3.
- **Port Extender:** 1RU switch. 48 x 10/25GbE tenant ports. Built for colo meet-me rooms.
- **PCE (Path Computation Engine):** Cloud orchestrator. Computes optimal paths, automates provisioning, hop-by-hop telemetry. White-label multi-tenant portal. API-first.

**The model:** IaaS subscription. 1/3/5-year terms. 10G or 100G tiers.

**Key numbers:** Traditional provisioning: 60-90 days. MaiaEdge: under 10 minutes. Cost reduction: 80-90%.

**The team:** Founded by the team behind Acme Packet (sold to Oracle for $2.1B) and 128 Technology (acquired by Juniper). $2.55B combined exits. Just raised $20M Series A.

### What MaiaEdge is NOT

| They (NaaS: Megaport, Equinix Fabric) | Us (MaiaEdge) |
|----------------------------------------|----------------|
| Own circuits, deliver services to enterprises | Provide infrastructure. Operators deliver services. |
| You join THEIR fabric | You build YOUR OWN fabric |
| Their portal, their invoice, their brand | Your portal, your invoice, your brand |
| They own the customer | You own the customer |

Not SD-WAN. Not a router replacement. We integrate with Equinix Fabric and Megaport via API. In cold outreach, say "third-party fabric providers" not specific names.

### Sovereignty: The Thread in Every Message

Every email should reinforce that the operator keeps the customer, the margin, and control. If you mention speed, pair it with ownership: "your team provisions in minutes" not just "provision in minutes." Exception: Neoclouds -- OPERATOR sovereignty banned. DATA sovereignty ("sovereign by design", "paths you control") allowed. Lead with deterministic performance, private connectivity, instant on-ramp.

### The Relevance Principle

Relevance beats personalization. Research is fuel, not content. It tells you WHICH problem to lead with. The email itself should not display the research. The prospect should think "yep, that's my life," not "this person Googled me." No "I noticed," no "Congratulations on," no company facts as standalone sentences. See cold-email skill for full anti-personalization rules.

## Qualified Segments

Classification requires PROOF, not just keywords. Each segment has a Quick Classification Test. If the answer is uncertain, flag for manual review rather than auto-classifying.

| Segment | Description | Quick Classification Test |
|---------|-------------|--------------------------|
| Fiber Operator | Regional/national fiber operators. Own physical fiber infrastructure. $20M-$500M revenue sweet spot. ~1,700-1,900 US operators. | "Does this company own fiber in the ground and sell connectivity services to businesses or carriers?" |
| Colocation Operator | Data center / colocation providers. Multi-site operators preferred. ~700-750 main US facilities. | "Does this company own a building where other companies put their servers, with carrier interconnection available?" |
| AI Colocation Operator | Colos with confirmed GPU cloud tenants or heavy AI infrastructure investment. Liquid cooling, 30kW+ racks, neocloud partnerships. | Same as Colo + "Does this facility have confirmed GPU cloud tenants, liquid cooling, or 30kW+ density?" |
| Neocloud | GPU cloud providers themselves (Lambda Labs, Crusoe, Voltage Park, Together AI). They ARE the inference customer. | "Does this company own (or have committed funding to build) GPU hardware in physical facilities and sell compute capacity to other companies?" |
| Network Operator | Tier 1/2 carriers with 50+ PoPs, complex multi-domain networks. Sophisticated internal automation (usually). | "Is this a national/global carrier with 50+ PoPs that sells enterprise connectivity?" |
| MSP / Aggregator | Managed service providers and VNOs that aggregate connectivity across multiple upstream carriers. NOT IT MSPs. | "Does this company buy circuits from multiple telecom carriers and resell bundled connectivity to enterprises?" |

## Exclusion List

EXCLUDE if any of the following apply:

| Exclude Category | Why |
|------------------|-----|
| Internet Exchange Point (IXP) | Infrastructure marketplace, not an operator |
| Tower REIT | Real estate, not network operations |
| IT MSP (managed IT services, helpdesk, break-fix) | Wrong type of MSP. Apply the IT MSP Test: if website lists helpdesk, endpoint management, cybersecurity, backup/DR with no carrier circuit aggregation, it's an IT MSP. |
| Retail ISP (verified no wholesale business) | Consumer broadband, not our buyer |
| Software vendor (including AI software platforms) | Not an operator. "AI cloud" marketing without physical GPU infrastructure = software vendor. |
| Hyperscaler (AWS, Azure, GCP, Meta) | Not our customer |
| Enterprise (internal network only) | Wrong ICP |
| Under 10 employees (verified from 2+ sources) | Too small (unless holding company with operator subsidiaries) |
| Vendor / Contractor / Manufacturer | Equipment maker, not operator. Includes fiber construction contractors. |
| Consulting firm | Advisory, not operator |
| Trade organization | Industry body, not operator |
| Defunct / Acquired (absorbed into parent) | No longer exists as independent entity |
| IT hosting / managed hosting (no physical colo) | Uses "colocation" or "data center" language but doesn't own/operate multi-tenant facilities with interconnection |
| Cloud GPU reseller (no owned infrastructure) | Resells hyperscaler GPU instances, not a neocloud |

### Exclude Verdict Routing

An `EXCLUDE` verdict from this skill does **not** directly write `customer_segment = "Flagged for deletion"` to HubSpot. The verdict is passed to the **pre-deletion-audit** skill (see `skills/pre-deletion-audit/SKILL.md`), which gates the decision through:

1. Open-deal hard stop (companies with any non-closed deal are never flagged)
2. Duplicate detection against existing ICP records (if the excluded company is a duplicate of a real ICP primary, its contacts are reassociated to the primary before the duplicate is flagged)
3. Per-contact activity check — any contact with `notes_last_contacted` within the last 90 days, a `notes_last_updated` within the last 90 days, or an association to an open deal is preserved and never receives `flagged_for_deletion = true`

This routing applies whether segment-classification is invoked standalone, from the enrichment pipeline, or under CRM Guardian Job 7. The classification verdict is the input to the audit; the audit is the only path that writes `customer_segment = "Flagged for deletion"`.

## Common False Positive Patterns

These company types frequently match segment keywords but should NOT be classified:

| Company Type | Keyword Match | Correct Action |
|---|---|---|
| IT hosting provider | "colocation," "data center" | Exclude: no multi-tenant facility with interconnection |
| Residential-only ISP | "fiber," "network operator" | Exclude unless wholesale/enterprise division verified |
| Cable MSO (residential) | "fiber network" | Exclude unless wholesale/transport division verified |
| Municipal broadband | "fiber operator" | Exclude unless commercial services arm verified |
| SD-WAN vendor | "network operator" | Exclude: software, not carrier infrastructure |
| VoIP/UCaaS provider | "carrier," "network services" | Exclude: application provider, not transport |
| IT MSP | "managed services," "MSP" | Exclude: IT services, not telecom aggregation |
| AI software platform | "AI cloud," "GPU cloud" | Exclude: software, not GPU infrastructure owner |
| AI consulting firm | "AI infrastructure" | Exclude: services, not compute provider |
| Fiber construction contractor | "fiber," "network infrastructure" | Exclude: builds for others, doesn't operate |

## Segment Messaging

**For full messaging framework, see context/copy-strategy/segment-messaging.md**

### Fiber Operators

**The situation:** Own fiber. Good regional business. Margins tightening. Significant fiber underutilized (lit, dark, and stranded laterals). Standing up private paths still requires routing complexity the ops team doesn't want to run. Cloud on-ramp is either not offered or offered with thin margin.

**The angle:** Monetize underutilized fiber. Stand up an instant private fabric across your network over any transport (fiber, wave, DIA, 5G/fixed wireless, satellite) with no routing complexity. Sell new services you couldn't before  -  cloud on-ramp flagship.

**Pillars:** MONETIZE | AUTOMATE | EXTEND REACH

**What to lead with:**
- **CEO/President:** Monetize underutilized fiber. New services (cloud on-ramp) you couldn't offer before. Competitive positioning.
- **CFO:** 80-90% provisioning cost reduction. OpEx model. New revenue from existing assets.
- **CTO/VP Engineering:** No VLAN stitching, no BGP, no MPLS, no SRv6. Any transport, any site. API-driven.
- **VP Sales/Commercial:** Win deals they're currently losing on provisioning timelines. Cloud on-ramp as a product to sell.
- **COO:** Scale delivery without scaling headcount.

**Pain points:** "Every NNI is a 60-90 day project" / "Once traffic leaves our network, visibility dies" / "We've got fiber sitting idle while the board wants revenue growth" / "Cloud on-ramp would be a product if we could stand it up without a hyperscale facility build" / "Our ops team isn't a routing team  -  we don't want to run MPLS/BGP just to stand up private paths"

### Colocation Operators

**Pillars:** INSTANT | MONETIZE | REACH

**The situation:** Every cross-connect is still a manual project (LOAs, truck rolls, VLAN coordination). Tenants expect portal-driven self-service the operator hasn't built. Standing up a services layer in-house is years of development. Cloud on-ramp is either not offered or offered through an arrangement that requires a hyperscale facility build. Multi-site operators have no easy way to stitch sites together for a tenant who wants capacity in more than one.

**The angle:** Build your own fabric without a multi-year development project. Automated virtual cross-connects, a services layer you can productize, and cloud on-ramp as a native product under your brand.

**What to lead with:**
- **CEO:** Build your own fabric. New high-margin services layer without a multi-year development project.
- **CTO:** Fabric-in-a-box. Automated virtual cross-connects. Virtual meet-me room. Deploy in weeks.
- **VP Sales:** Turn "we need 6 weeks" into "it's live today." Cloud on-ramp becomes a native product to sell.
- **CFO:** Higher attach rates without infrastructure buildout. New revenue from services, not more cabinets.

**Pain points:** "Every cross-connect is a project. LOAs, truck rolls, VLAN config" / "Tenants expect portal-driven self-service we haven't built" / "Building our own connectivity services is a multi-year project" / "Cloud on-ramp would be a product if we could stand it up without a hyperscale facility build" / "We have multiple sites and no easy way to connect them for a tenant who wants more than one"

> **Sparingly:** "Losing tenants to third-party fabric providers" is still allowed as a supporting hook, but only when research confirms a third-party fabric referral is already happening and no stronger angle is available. Don't lead with it.

### AI Colocation Operators

Same as Colocation but with AI-specific messaging when strong AI signals are found.

**Pillars:** DETERMINISTIC | INSTANT | MONETIZE

**The situation:** Invested heavily in AI-ready infrastructure: liquid cooling, high-density racks, power density. GPU cloud tenants bring interconnection demand and latency expectations best-effort networking doesn't meet. The connectivity layer hasn't caught up to the compute investment. Distributed and modular operators have multiple sites that need to behave like one fabric.

**Messaging lead:** Deterministic paths between distributed AI sites + automated cross-connects for GPU tenant deployments + cloud on-ramps for GPU workloads. NOT generic colo messaging. AI colo has its own messaging identity.

**Core hook:** "GPU tenants deploy dense interconnection fast. The connectivity layer either keeps up or it becomes the gap in the facility."

**Additional angles:**
- "You've built the compute and cooling infrastructure. Now complete the AI story with a connectivity layer that matches."
- "Best-effort networking is the uncontrolled variable in inference performance. Your tenants feel it."

**Do NOT use:** "35+ cross-connects per deployment," "sub-10ms latency," "33% of AI/ML latency is attributable to network slowness." These specific quant claims are retired  -  broader framing lands better because the numbers vary by tenant and workload.

**Modular DC variant** (Nodiac, Colony Compute, containerized-capacity-at-power-sites operators): Use AI Colo messaging with the multi-site angle front-and-center. "Every new pod at a new power site is either a separate networking project or a day-one join to your fabric. MaiaEdge makes it the second one." See [context/segments/colocation.md](context/segments/colocation.md) "Modular DC Variant" section for full treatment.

**Greenfield colo disambiguation:** Read their plans before writing. AI-ready build (liquid cooling / high-density power / announced GPU tenants / "AI campus" language) → AI Colo messaging. Standard build (traditional colo, no AI-ready signals) → Standard Colo messaging. Shared angle across both: multi-site fabric from the day the second site comes online.

### Neoclouds

These are NOT colos. Neoclouds (Lambda Labs, Crusoe, Voltage Park, Together AI) are GPU cloud providers that operate compute across multiple facilities. They ARE the inference customer.

**Pillars:** DETERMINISTIC | PRIVATE | INSTANT

**Critical messaging shift:** Drop "keep your customer" language. OPERATOR sovereignty banned. DATA sovereignty ("sovereign by design", "paths you control") allowed. No network jargon (VLAN, Q-in-Q). Lead with deterministic performance, private cloud connectivity (egress savings for their customers), and instant customer on-ramp.

**Master pitch:** Connecting distributed AI infrastructure simply. Benefits: multi-tenancy, deterministic performance, private cloud connectivity (egress savings for their customers), instant customer on-ramp. Observability is a supporting benefit under DETERMINISTIC, NOT the universal lead.

**Angle selection by maturity** (research-driven; same pillars, different door):

| Stage | Profile | Angle | Opening hook |
|-------|---------|-------|--------------|
| Pre-revenue / single site | Modular pre-tenant | **Watch list.** Too early. | N/A — flag on 2nd site or 1st GPU tenant. |
| Early growth (2-5 sites, crypto-to-AI pivots) | Duos Edge AI, IREN, TeraWulf, Core Scientific | **Early-growth.** Tenant-readiness framing. | "Bitcoin doesn't care about latency. Enterprise AI tenants do." |
| Mid-growth (5-15 sites, mixed customers, network person lost or never had one) | Together.ai, RunPod, Modal, Baseten, DeepInfra | **In-pain-now** (observability under DETERMINISTIC). | "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between." |
| Scale (15+ sites, hyperscaler-heavy 80%+, enterprise ramp plan) | Lambda, Crusoe, Voltage Park, Nebius | **Scaling-wall** (lead with INSTANT). | "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." |

**Flagship DETERMINISTIC proof point (all angles):** Agentic compounding latency. Ten inference hops across best-effort routing compounds into tens of seconds of delay. "Training tolerates retries. Inference doesn't. Agentic workflows tolerate neither." (Source: Montauk Capital April 2026 "Last Millisecond" thesis.)

**Neocloud Sub-Segments** (assign `customer_sub_segment` in enrichment research summary, import-processor maps to HubSpot `company_sub_segment`):

| Sub-Segment | Examples | Default Angle | Entry Point |
|-------------|----------|---------------|-------------|
| Large-Scale GPU NeoClouds | Lambda, Crusoe, Voltage Park, Nebius | Scaling-wall (default). In-pain-now only if latency variance is their stated pain. | Enterprise onboarding velocity. |
| Tier 1 Inference Providers | Together.ai, Fireworks, Baseten | In-pain-now (agentic angle lands hard). | Real-time telemetry + agentic compounding latency. |
| AI Infrastructure Providers | Vultr, DigitalOcean, Fluidstack, Modal, RunPod | In-pain-now. | Multi-cloud bridge + egress competitive advantage. |
| Sovereign AI Clouds | Nscale, Firmus, E2E Networks, Yotta | In-pain-now with sovereignty framing. | Policy-based sovereign routing (always qualify "sovereign"). |
| Crypto-to-AI Pivots | IREN, Core Scientific, TeraWulf | Early-growth. | Tenant-readiness + basic connectivity. |

**Pain points:** "Best-effort paths introduce jitter that breaks AI workloads" / "No visibility across the middle mile between clusters" / "Public internet egress costing $0.05-0.09/GB vs $0.02/GB Direct Connect" / "Every new facility is a multi-week connectivity project" / "Enterprise customers don't bring their own connectivity — every onboarding is a manual project"

### HubSpot Segment Mapping

NeoCloud is its own segment value in HubSpot  -  it is NOT mapped under "Colocation Operator."

| Classification | HubSpot `customer_segment` | HubSpot `company_sub_segment` |
|---------------|---------------------------|-------------------------------|
| GPU cloud provider (neocloud) | `NeoCloud` | [one of 5 neocloud sub-segments  -  see hubspot-values.md] |
| Colo with AI infrastructure signals | `Data Center Colo Provider` | `AI Signals - colo` |
| Standard colo (no AI signals) | `Data Center Colo Provider` | `Standard - colo` |

### Network Operators (Tier 1/2 Carriers)

**Pillars:** AUTOMATE | EXTEND REACH | MONETIZE (same as fiber)

**The situation:** Sophisticated internal automation. Not slow. But all of that stops at their network boundary. Cross-carrier paths beyond their footprint still take 60-90 days.

**Messaging lead:** Extend your reach, monetize existing assets. Same lead as fiber operators.

**CRITICAL: Never claim they're slow at what they're fast at.** Research what they've built. Acknowledge it. Then position MaiaEdge as extending their automation beyond their borders.

**Two tracks:**
- **Track A (Has internal automation):** "You've automated internally. MaiaEdge extends that everywhere else." Use when research shows self-service portal, API docs, branded products.
- **Track B (Fragmented internally):** "MaiaEdge unifies your internal boundaries first, then extends to partners." Use when research shows no evidence of portal/API automation.

**Pain points (Track A):** "Automated internally, but beyond our footprint still takes 60-90 days" / "No visibility once traffic leaves our network" / "Enterprise customers expect AWS-like speed" / "Lumen + AWS announced direct enterprise connectivity"

### MSPs / Aggregators

**The situation:** Own the customer relationship but rely on 3+ upstream carriers for transport. Can't see inside carrier networks. Responsible for SLAs they can't verify. Provisioning depends on whichever carrier is slowest. Tier 1s going direct to their customers.

**The angle:** MaiaEdge gives them end-to-end visibility across all upstream providers and instant provisioning. They compete on capability, not just relationship.

**What to lead with:**
- **CEO/President:** Tier 1 capabilities on an asset-light model. Compete on speed, not just price.
- **CFO:** Shift from CapEx to predictable OpEx.
- **VP Engineering:** Unified visibility across all carrier partners. No more blind spots.
- **VP Sales:** Instant activation instead of "depends on the carrier."

**Pain points:** "Blind to what happens inside carrier networks" / "Responsible for SLA but can't see the path" / "'Depends on the carrier' kills deals" / "Tier 1s are going direct to our customers"

## Post-Research Segment Verification (MANDATORY)

After completing web research, verify the segment classification against proof-based criteria. This prevents writing colo messaging for a company that's actually an IT hosting provider, or sending neocloud outreach to an AI software platform.

**Step 1  -  Quick Classification Test:**
Run the Quick Classification Test from the segment table above. If the answer to the test question is "no" or "uncertain," the company may be misclassified.

**Step 2  -  Check for False Positive Patterns:**
Does the company match any pattern in the Common False Positive Patterns table? If yes, research further before proceeding with outreach.

**Step 3  -  Verify HubSpot Classification:**
- Does the HubSpot `customer_segment` match what research found?
- For colos: Did you find strong AI signals? If yes, sub-segment should be "AI Infrastructure" not "Standard." BUT also verify they actually own/operate the facility (not managed hosting).
- For network operators: Did you find portal/API evidence? Determines Track A vs Track B. BUT also verify carrier-scale infrastructure (50+ PoPs, enterprise connectivity).
- For neoclouds: Did you confirm they OWN physical GPU infrastructure? "AI cloud" marketing alone is not sufficient.
- For MSPs: Did you confirm telecom carrier aggregation? Apply the IT MSP Test if unclear.
- Is this company actually on the exclusion list? (Check for acquisitions, defunct status, wrong category, hosting-not-colo, software-not-neocloud)

**If mismatch:** Flag clearly: `SEGMENT MISMATCH: HubSpot says [X], research says [Y]. Using [Y] for messaging.`
**If false positive detected:** Flag: `QUALIFICATION CONCERN: Company classified as [segment] but [specific concern]. Verify before sending outreach.`
**If confirmed:** Note: `Segment verified: [segment] / [sub-segment]`

Always use the CORRECT segment for email writing, regardless of what HubSpot says. If qualification is uncertain, skip the company rather than send misaligned outreach.

## Segment Change Cascade Rules

When `customer_segment` is changed on a company record  -  whether from new classification, re-enrichment, correction, or deprecated enum migration  -  the following cascade MUST be applied:

1. **Re-derive `company_sub_segment`:** Apply sub-segment assignment rules from hubspot-values.md for the new segment. If the old sub-segment doesn't belong to the new segment, it MUST change. For example, if segment changes from `Enterprise` (MSP) to `Fiber Operator`, sub-segment must change from `Telecom Aggregator - MSP` to one of the Fiber sub-segments.

2. **Re-derive `account_tier`:** Apply tier criteria from property-schema.md. A segment change may upgrade or downgrade tier:
   - Moving from MSP to Fiber Operator with HIGH confidence → upgrade to Tier 2
   - Moving from NeoCloud to Data Center Colo Provider → may downgrade from Tier 1 if no AI signals
   - Any segment change resets tier evaluation from scratch

3. **Re-derive `segmentation_confidence`:** If the segment changed, confidence should reflect the evidence for the NEW segment, not the old one. If the change was a correction without new research, set to MEDIUM unless strong evidence exists.

4. **Re-derive `infrastructure_profile`:** Only if new research was performed during the segment change. If this is a field correction or enum migration without new research, leave `infrastructure_profile` as-is.

5. **Sync to contacts:** Update `customer_segment` on all associated contacts to match the new company segment. Company record is source of truth.

6. **Update `last_enriched_date`:** Set to today's date (YYYY-MM-DD).

### Special Case: Segment Changing TO "Flagged for deletion"

When the new segment is `"Flagged for deletion"`, the cascade above does NOT apply. Instead, hand the candidate to the **pre-deletion-audit** skill (Step 0 input) and let it run its own workflow. The audit decides per-contact whether to reassociate, preserve, or flag  -  it does not blindly sync `customer_segment = "Flagged for deletion"` to associated contacts.

Specifically: skip steps 1-5 of the cascade for this case, and do NOT write the company's new segment until pre-deletion-audit has resolved all associated contacts. The audit writes the company segment itself once contacts are resolved.

**This section is the single source of truth for cascade behavior.** CRM Guardian references this section  -  it does not redefine cascade logic.

**When running under CRM Guardian:** This cascade executes automatically. The Guardian's safety tier system applies  -  see crm-guardian skill for tier definitions and deal protection rules.

**In standalone mode:** Produce the cascade recommendation without writing:
```
SEGMENT CHANGE CASCADE  -  [Company]
Segment: [old] → [new]
Sub-segment: [old] → [recommended new]
Tier: [old] → [recommended new]
Confidence: [old] → [recommended new]
Contacts to sync: [N]
```

---

## Emerging Context (2026)

**AI Infrastructure:** Training is concentrated. Inference is distributed. Tenants need low-latency paths between GPU clusters across multiple facilities. MaiaEdge enables the orchestration layer.

**Hyperscalers Going Direct:** AWS + Lumen delivering "last mile" connectivity directly to enterprises. Regional operators risk being cut out. Cross-carrier connectivity lets operators compete.

**Mplify Alliance:** MaiaEdge is engaged with Mplify Alliance (formerly MEF) on standards. Use selectively with sophisticated buyers.

## Technical Terminology

**Use in Emails:** Automated provisioning, zero-touch provisioning, protocol-free forwarding, API-driven activation, deterministic paths, hop-by-hop telemetry, Federated Private Networking, end-to-end visibility, sovereignty, middle-mile blind spot, transport agnostic, white-label portal.

**Use Sparingly:** Session-smart routing (founder credibility only), PBC (after explaining: "1RU edge device"), PCE (after explaining: "cloud orchestrator"), fabric-in-a-box (colo segment primarily).

**Never in Cold Outreach:** Session-smart routing as a lead. Internal codenames. "Revolutionary." "Game-changing."
