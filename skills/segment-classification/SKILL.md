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

Every email should reinforce that the operator keeps the customer, the margin, and control. If you mention speed, pair it with ownership: "your team provisions in minutes" not just "provision in minutes." Exception: Neoclouds don't need sovereignty language. They need visibility, speed, and cost reduction.

### The Relevance Principle

Relevance beats personalization. Research is fuel, not content. It tells you WHICH problem to lead with. The email itself should not display the research. The prospect should think "yep, that's my life," not "this person Googled me." No "I noticed," no "Congratulations on," no company facts as standalone sentences. See cold-email skill for full anti-personalization rules.

## Qualified Segments

Classification requires PROOF, not just keywords. Each segment has a Quick Classification Test. If the answer is uncertain, flag for manual review rather than auto-classifying.

| Segment | Description | Quick Classification Test |
|---------|-------------|--------------------------|
| Fiber Operator | Regional/national fiber operators. Own physical fiber plant. $20M-$500M revenue sweet spot. ~1,700-1,900 US operators. | "Does this company own fiber in the ground and sell connectivity services to businesses or carriers?" |
| Colocation Operator | Data center / colocation providers. Multi-site operators preferred. ~700-750 main US facilities. | "Does this company own a building where other companies put their servers, with carrier interconnection available?" |
| AI Colocation Operator | Colos with confirmed GPU cloud tenants or heavy AI infrastructure investment. Liquid cooling, 30kW+ racks, neocloud partnerships. | Same as Colo + "Does this facility have confirmed GPU cloud tenants, liquid cooling, or 30kW+ density?" |
| Neocloud | GPU cloud providers themselves (CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI). They ARE the inference customer. | "Does this company own (or have committed funding to build) GPU hardware in physical facilities and sell compute capacity to other companies?" |
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

### Fiber Operators

**The situation:** Own fiber. Good regional business. Margins tightening. Customers want on-demand connectivity beyond the operator's footprint. Provisioning still takes weeks to months.

**The angle:** MaiaEdge lets them monetize fiber they already own, deliver services faster, extend reach through federation.

**What to lead with:**
- **CEO/President:** Revenue from underutilized fiber. Competitive positioning.
- **CFO:** 80-90% provisioning cost reduction. OpEx model.
- **CTO/VP Engineering:** No MPLS, no BGP, no routing protocols. Protocol-free. API-driven.
- **VP Sales/Commercial:** Win deals they're currently losing on provisioning timelines.
- **COO:** Scale delivery without scaling headcount.

**Pain points:** "Every NNI is a 60-90 day project" / "Once traffic leaves our network, visibility dies" / "Type 2 circuits are a visibility black hole" / "40% of our fiber is sitting dark"

**Word count:** 60-120 words (soft target. A tight, relevant email 10 words under is better than a padded email that hits the number.)

### Colocation Operators

**The situation:** Tenants expect instant interconnections, direct cloud access, self-service control. Most colos can't deliver without massive development. Tenants go to Equinix or Megaport. Colo loses relationship and recurring revenue. Stuck competing on space and power.

**The angle:** MaiaEdge gives them fabric-like capabilities without the multi-year build. They keep the customer, the margin, the control.

**What to lead with:**
- **CEO:** Compete with Equinix on interconnection without their capital investment.
- **CTO:** Fabric-in-a-box. No multi-year development project. Deploy in weeks.
- **VP Sales:** Turn "we need 6 weeks" into "it's live tomorrow."
- **CFO:** Higher attach rates without the infrastructure buildout.

**Pain points:** "Tenants ask for cloud connectivity and we say 'call Megaport'" / "Equinix reps are calling on our tenants" / "Every cross-connect is a project. LOAs, truck rolls, VLAN config" / "We're just selling space and power, not services"

**Word count:** 80-140 words (soft target)

### AI Colocation Operators

Same as Colocation but with AI-specific messaging when strong AI signals are found.

**The situation:** Invested heavily in AI-ready infrastructure: liquid cooling, high-density racks, power. GPU cloud tenants need deterministic, low-latency interconnects between GPU clusters faster than the colo can provision them.

**Additional angles:**
- "You've built the compute and cooling infrastructure. Now complete the AI story with instant interconnection."
- "GPU cloud providers require 35+ cross-connects per deployment with sub-10ms latency. Are you delivering that in minutes?"
- Key stat: "33% of AI/ML latency is attributable to network slowness"

**Word count:** 80-140 words (soft target)

### Neoclouds

These are NOT colos. Neoclouds (CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI) are GPU cloud providers that operate compute across multiple facilities. They ARE the inference customer.

**Note:** CoreWeave is used as a reference example but is NOT an active outreach target. Use the sub-segment framework to identify relevant prospects.

**Critical messaging shift:** Drop "keep your customer" language. They don't need sovereignty messaging. Lead with observability ("see why you're slow"), then cloud on-ramp, then deterministic paths. The inverted hierarchy matters — these companies don't yet know they have a network problem.

**The angle:** See why inference is slow. Diagnose the network. Then fix it with deterministic paths.

**Neocloud Sub-Segments** (assign `customer_sub_segment` in enrichment research summary, import-processor maps to HubSpot `company_sub_segment`):

| Sub-Segment | Examples | Entry Point |
|-------------|----------|-------------|
| Large-Scale GPU NeoClouds | CoreWeave, Crusoe | Cross-facility orchestration |
| Tier 1 Inference Providers | Together AI, Anyscale | Observability + cloud on-ramp |
| AI Infrastructure Providers | Applied Digital, Hut 8 | Basic connectivity + visibility |
| Sovereign AI Clouds | EU/APAC government-backed | Data residency + deterministic paths |
| Crypto-to-AI Pivots | Hive Digital, HUTS | Basic connectivity, cost of recompute |

**Pain points:** "Can't see why inference is slow — is it compute, network, or storage?" / "No visibility across the middle mile between clusters" / "Public internet egress costing $0.05-0.09/GB vs $0.02/GB Direct Connect" / "Best-effort paths introduce jitter that breaks AI workloads"

**Word count:** 80-140 words (soft target)

### HubSpot Segment Mapping

NeoCloud is its own segment value in HubSpot — it is NOT mapped under "Colocation Operator."

| Classification | HubSpot `customer_segment` | HubSpot `company_sub_segment` |
|---------------|---------------------------|-------------------------------|
| GPU cloud provider (neocloud) | `NeoCloud` | [one of 5 neocloud sub-segments — see hubspot-values.md] |
| Colo with AI infrastructure signals | `Data Center Colo Provider` | `AI Signals - colo` |
| Standard colo (no AI signals) | `Data Center Colo Provider` | `Standard - colo` |

### Network Operators (Tier 1/2 Carriers)

**The situation:** Sophisticated internal automation. Not slow. But all of that stops at their network boundary. Cross-carrier paths beyond their footprint still take 60-90 days.

**CRITICAL: Never claim they're slow at what they're fast at.** Research what they've built. Acknowledge it. Then position MaiaEdge as extending their automation beyond their borders.

**Two tracks:**
- **Track A (Has internal automation):** "You've automated internally. MaiaEdge extends that everywhere else." Use when research shows self-service portal, API docs, branded products.
- **Track B (Fragmented internally):** "MaiaEdge unifies your internal boundaries first, then extends to partners." Use when research shows no evidence of portal/API automation.

**Pain points (Track A):** "Automated internally, but beyond our footprint still takes 60-90 days" / "No visibility once traffic leaves our network" / "Enterprise customers expect AWS-like speed" / "Lumen + AWS announced direct enterprise connectivity"

**Word count:** 100-160 words (soft target)

### MSPs / Aggregators

**The situation:** Own the customer relationship but rely on 3+ upstream carriers for transport. Can't see inside carrier networks. Responsible for SLAs they can't verify. Provisioning depends on whichever carrier is slowest. Tier 1s going direct to their customers.

**The angle:** MaiaEdge gives them end-to-end visibility across all upstream providers and instant provisioning. They compete on capability, not just relationship.

**What to lead with:**
- **CEO/President:** Tier 1 capabilities on an asset-light model. Compete on speed, not just price.
- **CFO:** Shift from CapEx to predictable OpEx.
- **VP Engineering:** Unified visibility across all carrier partners. No more blind spots.
- **VP Sales:** Instant activation instead of "depends on the carrier."

**Pain points:** "Blind to what happens inside carrier networks" / "Responsible for SLA but can't see the path" / "'Depends on the carrier' kills deals" / "Tier 1s are going direct to our customers"

**Word count:** 60-120 words (soft target)

## Post-Research Segment Verification (MANDATORY)

After completing web research, verify the segment classification against proof-based criteria. This prevents writing colo messaging for a company that's actually an IT hosting provider, or sending neocloud outreach to an AI software platform.

**Step 1 — Quick Classification Test:**
Run the Quick Classification Test from the segment table above. If the answer to the test question is "no" or "uncertain," the company may be misclassified.

**Step 2 — Check for False Positive Patterns:**
Does the company match any pattern in the Common False Positive Patterns table? If yes, research further before proceeding with outreach.

**Step 3 — Verify HubSpot Classification:**
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

## Emerging Context (2026)

**AI Infrastructure:** Training is concentrated. Inference is distributed. Tenants need low-latency paths between GPU clusters across multiple facilities. MaiaEdge enables the orchestration layer.

**Hyperscalers Going Direct:** AWS + Lumen delivering "last mile" connectivity directly to enterprises. Regional operators risk being cut out. Federation lets operators compete.

**Mplify Alliance:** MaiaEdge is engaged with Mplify Alliance (formerly MEF) on standards. Use selectively with sophisticated buyers.

## Technical Terminology

**Use in Emails:** Automated provisioning, zero-touch provisioning, protocol-free forwarding, API-driven activation, deterministic paths, hop-by-hop telemetry, Federated Private Networking, end-to-end visibility, sovereignty, middle-mile blind spot, transport agnostic, white-label portal.

**Use Sparingly:** Session-smart routing (founder credibility only), PBC (after explaining: "1RU edge device"), PCE (after explaining: "cloud orchestrator"), fabric-in-a-box (colo segment primarily).

**Never in Cold Outreach:** Session-smart routing as a lead. Internal codenames. "Revolutionary." "Game-changing."
