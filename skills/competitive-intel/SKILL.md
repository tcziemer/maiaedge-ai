---
name: competitive-intel
description: "MaiaEdge competitive intelligence and positioning skill. Use when positioning against competitors (Megaport, Equinix, Lumen, SD-WAN, orchestration platforms), handling objections, building a battle card, or preparing for a competitive deal. Produces competitive briefs, positioning statements, objection responses, and proof points by segment."
---

# Competitive Intelligence Skill

Triggers automatically when competitive positioning or objection handling is needed.

## When This Skill Activates

- User mentions a competitor (Megaport, Equinix, Lumen, SD-WAN, etc.)
- User asks how to position against a specific company
- User needs objection handling for a deal
- User asks "how do we compare to [competitor]?"

## Clarification

Two questions that materially change the output:
1. Segment - which ICP are you selling into? (Fiber / Colo / Network Op / NeoCloud / MSP / Enterprise, or a mix?)
2. Stage - cold outreach draft, pre-call prep, live discovery, or proposal/follow-up?

Stage governs language register - "fabric-in-a-box" and credibility anchors are live-call/proposal only. If the user already gave a competitor name AND segment, skip straight to stage.

## Reference Files

### Core positioning
- `context/core/differentiation-naas-aggregator.md` - SINGLE SOURCE OF TRUTH for the NaaS/fabric and aggregator lines: the mechanical truth table (DIY NNI vs join-a-fabric vs aggregator vs MaiaEdge), objection responses in three registers (cold-safe / live-call / one-liner) for "How is this not Megaport?", "We already have NNI partners", "So you're an aggregator?", "Whose network does the extension ride?", "Why not just join a fabric?", cost-vs-port, "exchanges failed before", and the internal-build $475M reframe; the sanctioned June 2026 market catalyst (Megaport ~US$594M / A$827M compute raise) with its usage rules; and the claims-to-avoid list (unverified federation mechanics). Read it FIRST for any NaaS, fabric, aggregator, or extension-positioning question.
- `context/core/competitive-positioning.md` - Detailed battle cards, objection handling frameworks, market context
- `context/product/proof-points.md` - Customer stories and outcomes for competitive situations
- `context/product/pbc-pce-datasheet.md` - Hardware specs for technical comparisons
- `context/product/integrated-switch-datasheet.md` - MPP-48 switch specifications

### ICP + messaging context (HIGH)
- `context/core/icp-playbook.md` - Per-segment worked examples, persona pain, objection handling by ICP
- `context/core/messaging-framework.md` - USE/AVOID vocabulary by segment; Cross-Segment Pillar Framework; register rules
- `context/core/maiaedge-101.md` - Canonical company narrative and 30-second pitch by segment
- `context/product/ai-market-positioning.md` - AI-era positioning; GPU cluster connectivity; NeoCloud-to-enterprise demand drivers
- `context/product/cloud-onramp-business-case.md` - ROI model for cloud on-ramp positioning; cost-vs-Megaport/Direct Connect comparisons
- `context/product/economic-impact-acg-whitepaper.md` - Third-party economic validation; use in competitive proposals and discovery
- `context/segments/neocloud.md` - NeoCloud segment deep-dive; GPU pricing reversal; NC1-NC5 sub-segment positioning nuances

### Supplementary context (MEDIUM)
- `context/core/terminology-glossary.md` - Canonical product and category terms; avoid wrong category labels
- `context/segments/enterprise.md` - Enterprise ICP scope, hard gate criteria, and competitive framing rules
- `context/partner-assets/cheatsheet-neocloud.md` - NeoCloud objection handling and persona matrix
- `context/partner-assets/cheatsheet-enterprise.md` - Enterprise objection handling and persona matrix
- `context/sales/neocloud-strategy-brief.md` - NeoCloud go-to-market strategy and competitive angles
- `context/marketing/sovereign-routing-explainer.md` - Sovereignty and data-residency positioning for international deals
- `context/europe/sovereignty-positioning.md` - European DORA/NIS2 framing and sovereignty angles for Markus-territory deals

## Core Positioning

**MaiaEdge is NOT NaaS.** This is the most important distinction. NaaS providers (Megaport, Equinix Fabric) own the customer relationship. MaiaEdge enables the operator to own the customer relationship.

**Category:** Carrier Infrastructure for Federated Private Networking

**Only Statement:** Only MaiaEdge provides the infrastructure that enables network operators to extend services across domains instantly, over any transport, while maintaining complete visibility and sovereignty.

## Competitor Positioning

### Megaport / Equinix Fabric / PacketFabric / Console Connect (NaaS)
**Their model:** They own the fabric, the portal, the customer relationship. Operators become suppliers on someone else's platform.
**Our model:** Operators build their own fabric. Their portal, their brand, their customer, their margin.
**Key line:** "They own the fabric AND your customer. MaiaEdge = you own both. We integrate with them via API for cloud reach."
**In cold emails:** Say "third-party fabric providers," never name them directly.
**Partnership angle:** MaiaEdge integrates with Equinix Fabric and Megaport APIs for cloud on-ramps. They can be infrastructure partners AND competitive alternatives.
**2026 state (details + usage rules in differentiation-naas-aggregator.md §4):** Megaport raised ~US$594M (A$827M, June 3, 2026) to build a distributed GPU inference cloud - the fabric now sells compute against the customers its operator partners serve. Equinix sells sovereignty as a premium Fabric tier (Geo Zones, May 2026). Console Connect's 80% sale to Infratil was cancelled on regulatory grounds (Oct 2024) - platform-dependence risk in one anecdote. PacketFabric is alive (merged with Unitas Global 2023) but its 2023-24 distress arc is the cautionary tale: "what was your contingency if your fabric vendor had been PacketFabric?"

### Aggregators / TSDs (the box we must NOT be filed in)
**Their model:** An aggregator resells many carriers' connectivity on its own paper - it owns the end customer, the quote engine, the invoice; the underlying operator gets the thin wholesale rate and the buyer pays a 25-30% aggregation premium. TSDs/technology advisors are a DISTINCT model (agents selling on the carrier's paper for commission). "Master agent" is a dead category word in 2026.
**The positional line:** an aggregator and a NaaS both sit BETWEEN the operator and the customer; MaiaEdge deploys INSIDE the operator's network. "An aggregator sits between you and your customer. We sit inside your network. Opposite ends of the table."
**The supplier-desk trap:** a Carrier Relations / Supplier Management seat will read any connectivity-sounding pitch as a line-card onboarding request and route it to procurement. Correct in one sentence: "this is infrastructure you deploy and bill on, not a circuit supplier to onboard - we're not asking to be supplier #401." Aim the conversation at CEO / VP Product as a margin-stack decision.
**Full doctrine:** objection responses in three registers, the truth table, and the claims-to-avoid list live in `context/core/differentiation-naas-aggregator.md`.

### Lumen Private Connectivity Fabric (PCF)
**Their model:** Building a national private connectivity empire. AWS partnership (Interconnect Last Mile). ~340K route miles, 163K+ buildings, 400G backbone.
**The threat:** Going direct to enterprises, cutting regional operators out entirely.
**Our positioning:** "Lumen builds their empire; MaiaEdge empowers you to build yours."
**Why it matters:** Regional operators need to extend their reach to match Lumen's. MaiaEdge enables that cross-carrier reach extension.
**HubSpot tag:** #COMPETITION_PRIVATE_FABRIC

### SD-WAN (Cisco Viptela, VMware VeloCloud, Fortinet)
**Their model:** Enterprise branch office connectivity. Last-mile solution.
**Our positioning:** "SD-WAN is for enterprises managing branches. We're built for service providers at carrier-scale."
**The opportunity:** MaiaEdge can be the fabric layer underneath managed SD-WAN services.

### Orchestration Platforms (Ciena Blue Planet, Nokia NSP, Juniper Paragon)
**Their model:** Multi-vendor orchestration software. Complex integration projects.
**Our positioning (live conversations / proposals only):** "6-18 month deployments, $1-5M+ integration cost vs. MaiaEdge fabric-in-a-box in weeks, OpEx subscription."
**In cold email and LinkedIn body:** "Fabric-in-a-box" is banned. Translate to "build your own interconnection layer in weeks, not years" or "deterministic paths and policy on a platform you operate, no multi-vendor integration project required."
**Key difference:** They orchestrate existing infrastructure. MaiaEdge IS the infrastructure.

### Hyperscalers Going Direct (AWS, Azure, Google Cloud)
**The threat:** Building direct enterprise connectivity (AWS Interconnect, Azure ExpressRoute). Cutting regional operators out.
**The opportunity:** Enterprises near new hyperscaler facilities need connectivity fast. Cross-carrier connectivity lets operators compete by combining reach.

## Universal Objection Handling

| Objection | Response Framework |
|-----------|-------------------|
| "We're building our own" | Most teams estimate 18-24 months and millions. We've already done that work. Same team that built Acme Packet and 128 Technology. Why rebuild what exists? |
| "We use Megaport/Equinix" | Three-step: (1) Acknowledge they've built impressive platforms. (2) The difference is who owns the customer relationship. (3) With their model, your tenant becomes their customer. With MaiaEdge, you keep the margin, the relationship, and the roadmap control. |
| "This sounds complex" | The opposite. No routing protocols, no BGP sessions, no MPLS label distribution. That complexity is exactly what we eliminate. |
| "This sounds expensive" | Compare to what you're losing: deals to faster competitors, SLA penalties on paths you can't see, engineering hours on manual provisioning. OpEx subscription, scales with your business. |
| "Who are you?" | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper). SBC used by 90% of carriers. Two exits, $2.5B+ combined. |
| "We have Cisco/Juniper investments" | PBCs complement, not replace, core routers. They sit at domain boundaries where existing automation stops. Unification layer, not rip-and-replace. |

## Segment-Specific Competitive Positioning

### For Fiber Operators
- Megaport/Equinix: "They own the fabric AND your customer. We give you both back."
- Lumen: "Lumen builds their empire; MaiaEdge empowers you to build yours."
- SD-WAN: "Different layer. SD-WAN = enterprise branches. MaiaEdge = carrier infrastructure."

### For Colocation Operators
- Equinix Fabric: "Your tenants go to Equinix for connectivity and become their customer. Build your own fabric instead."
- Megaport: "Every tenant connectivity request that goes through Megaport is revenue and control walking out your door."

### For Network Operators
- Internal orchestration: "Great for internal domains. What about paths crossing carrier boundaries? That's the cross-carrier layer we solve."
- Cisco/Juniper: "Complements, not competes. We sit at domain boundaries where your core automation stops."

### For MSP/Aggregators
- Megaport/Equinix: "They're your competition, not your tool. They aggregate customers on THEIR fabric. MaiaEdge lets YOU be the aggregator."
- Tier 1 Direct: "Match their speed and visibility. Add your value: single invoice, multi-carrier simplification."

### For Neoclouds
- **Groq:** Benchmark, not competitor. Built 35 Equinix POPs in 6 months with unlimited VC. Every neocloud wants what Groq built, nobody can afford to replicate it. Position as: "Groq-quality networking without the Groq budget."
- **Datum.net (channel partner):** Datum solves Layer 7 (proxy, anycast, DDoS). MaiaEdge solves Layer 2/3 (paths, observability, encryption). Together = full-stack answer. CEO Zac Smith has direct relationships with decision-makers at Together.ai, Inference.net, RunPod, Modal. **Do not position as competing with Datum. They're a channel partner.**
- **Equinix Fabric / Megaport (for neoclouds):** Different positioning than operator segment. Neoclouds use these for cloud on-ramps. MaiaEdge automates Direct Connect provisioning through their APIs. Frame as: "Private paths via Equinix Fabric/Megaport API, automated by MaiaEdge."
- **Public internet transit (the real competitor for neoclouds):** Most neoclouds don't know alternatives exist. They move data over public internet at $0.05-0.09/GB because nobody told them about Direct Connect at $0.02/GB. The competition is inertia and ignorance, not another vendor.

### For Enterprise (Multi-DC ICP)

Enterprise (`Enterprise-CustomerSegment`, promoted to ICP 2026-05-11) buys differently from operator segments - the enterprise IS the customer, not selling connectivity. The competitive set is different. Full positioning lives in `context/core/competitive-positioning.md` §3.6 Enterprise Competitive Context.

- **Status Quo / Do Nothing:** #1 competitor (same as every other segment). Manual provisioning, BGP across the WAN, dark fiber "redundancy" via a single fiber pair, cloud on-ramps through Megaport with the SLA owned by the enterprise but the portal owned by someone else. Frame: "Your DR strategy assumes the dark fiber is redundant. It is not - fix it without standing up BGP."
- **SD-WAN (Cisco / Juniper SSR / 128T / Versa / Cato / Fortinet / Palo Alto):** Different layer. SD-WAN handles branch/user; MaiaEdge handles inter-DC and cloud on-ramp. The two run together. Position SD-WAN as session-smart routing that benefits from a deterministic, observable underlay. Do NOT position as a replacement.
- **Carrier-managed circuits (AT&T, Verizon, Lumen, BT, NTT):** Use them. MaiaEdge sits over the existing transport; the carrier keeps providing the circuit, MaiaEdge gives the enterprise determinism + visibility + control across whatever transport is underneath. No carrier replacement, no SLA renegotiation.
- **Third-party fabric providers (Megaport / Equinix Fabric / PacketFabric / Console Connect) - for Enterprise:** Coexist via API where commercially sensible. The portal is theirs, the support is theirs, the cloud bill is theirs, but the customer relationship and SLA stay with the enterprise team. Frame as: "Cloud on-ramps under your brand and your control. Megaport / Equinix become transport options the fabric uses by API rather than vendors you depend on."
- **Cloud-native networking (AWS Cloud WAN, Azure vWAN, GCP NCC):** Each cloud has its own. They do not federate well across clouds, and they do not solve dark fiber redundancy at all. MaiaEdge is the cross-cloud, cross-DC layer that does. Direct Connect / ExpressRoute / Cloud Interconnect become transport options the fabric uses, not the architecture itself.
- **Internal Build:** "We could build this ourselves." 18-24 months, carrier-grade SDN talent enterprises can't hire fast enough. Frame: MaiaEdge is productized fabric - operable by the team you already have, no BGP / MPLS / SRv6 to manage.
- **Lumen PCF + AWS Interconnect direct-to-enterprise:** Rare for the Enterprise ICP because the four sub-segments tend to want sovereignty over their fabric, not a Tier 1 dependency. But surfaces in conversations. Frame: "Lumen builds their empire. MaiaEdge gives you the same instant provisioning capability under your control. You're not a tenant on Lumen's fabric - you own the fabric."

**Enterprise objection reframes (use in discovery + follow-up):**

| Objection | Reframe |
|---|---|
| "We already have SD-WAN" | Different layer. SD-WAN handles branch/user; MaiaEdge handles inter-DC and cloud on-ramp. The two run together - MaiaEdge is the underlay your SD-WAN overlay benefits from. |
| "Megaport works fine" | Until your team owns the SLA. The portal is theirs, the support is theirs, the cloud bill is theirs. MaiaEdge integrates with Megaport via API where it makes commercial sense - the customer relationship and the SLA stay with your team. |
| "We just signed a long carrier agreement" | Use it. MaiaEdge sits over the existing transport; we give your team determinism, visibility, and control over whatever's underneath. |
| "AWS Direct Connect handles our cloud paths" | Per cloud. AWS Cloud WAN, Azure vWAN, GCP NCC don't federate across clouds, and they don't solve dark fiber redundancy at all. MaiaEdge is the cross-cloud, cross-DC layer that does. |
| "We could build this ourselves" | 18-24 months. Network team scope is growing faster than headcount, and carrier-grade SDN talent is scarce. MaiaEdge is productized fabric - operable by the team you already have. |

**Federation note for Enterprise:** Federation framing does NOT apply. Enterprises are not federating with partners - they are the customer. Drop federation language from Enterprise messaging entirely.

## Proof Points for Competitive Situations

| Customer | Quote/Reference | Use When |
|----------|----------------|----------|
| NTT | Network simplification, PoP acceleration | Tier 1 credibility, scale objections |
| Arvig | "Almost instantaneous" provisioning | Speed objections, automation doubts |
| RevNet | "Imagine having Megaport capability between providers" | NaaS comparison, multi-carrier |
| IENTC | 800+ cell towers to 20+ data centers | Mobile backhaul, scale |
| Equinix | "Revolutionary and creative... abstracting complexity with PBC approach" | Technical skeptics |
| Ocean Networks | Cross-carrier connectivity to INDATEL for mainland reach | Geographic isolation, partner reach |
| Ecotel (Germany) | "Great for the fragmented fibre market" | International, fragmented markets |

**Rule:** Never name customers in cold outreach. Anonymize: "One fiber operator saw instantaneous provisioning." Use names only in meetings/follow-ups when prospect asks "who else uses this?"
