---
name: call-prep
description: "MaiaEdge call and meeting preparation skill. Use when preparing for meetings or calls with prospects. Produces discovery questions, pain validation, talk tracks by persona, objection handling, and proof points. Trigger on upcoming meeting, call prep, meeting prep, discovery questions, talk tracks, or preparing for a conversation with a prospect."
---

# Call Prep Skill

Triggers automatically when preparing for meetings or calls with MaiaEdge prospects.

## When This Skill Activates

- User mentions an upcoming meeting or call with a prospect
- User asks to prepare for a conversation
- User asks for discovery questions or talk tracks
- User mentions "call prep," "meeting prep," or "preparing for [company]"

## Clarification

Before I build your call brief, two questions:
1. Which segment is this prospect in? (Fiber / Colo / Network Op / Neocloud / MSP-Aggregator / Enterprise - plus sub-segment if known, e.g. "AI Signals colo" or "Tier 1 Inference neocloud")
2. What kind of call - first discovery, POC scoping, or further along?

Coach: if you only have a company name, share it and I'll flag what's missing.

## Reference Files

For deeper context during call preparation, consult:

**Segment context (angles + qualification):**
- `context/segments/colocation.md` - Colo segment angles, signals, qualification
- `context/segments/fiber-operator.md` - Fiber segment angles, signals, qualification
- `context/segments/neocloud.md` - NeoCloud segment angles, signals, qualification
- `context/segments/network-operator.md` - Network Operator segment angles, signals, qualification
- `context/segments/msp-aggregator.md` - MSP/Aggregator segment angles, signals, qualification
- `context/segments/enterprise.md` - Enterprise (Multi-DC ICP) segment scope, hard gate, sub-segments

**Partner cheatsheets (objection handling + persona matrix):**
- `context/partner-assets/cheatsheet-colocation.md` - Colo objection handling, persona matrix
- `context/partner-assets/cheatsheet-fiber-operator.md` - Fiber objection handling, persona matrix
- `context/partner-assets/cheatsheet-neocloud.md` - NeoCloud objection handling, persona matrix
- `context/partner-assets/cheatsheet-network-operator.md` - Network Operator objection handling, persona matrix
- `context/partner-assets/cheatsheet-msp-aggregator.md` - MSP/Aggregator objection handling, persona matrix
- `context/partner-assets/cheatsheet-enterprise.md` - Enterprise objection handling, persona matrix

**Competitive + positioning:**
- `context/core/competitive-positioning.md` - Battle cards, objection handling by competitor
- `context/core/differentiation-naas-aggregator.md` - Cold-safe vs live-call NaaS doctrine; Megaport/Equinix live-call objection handling
- `context/core/icp-playbook.md` - Objection handling per segment; worked per-segment examples and persona pain
- `context/copy-strategy/segment-language.md` - Segment-specific vocabulary and angle selection

**Product + proof:**
- `context/product/proof-points.md` - Customer stories and public quotes (Arvig, RevNet, NTT, IENTC, Ocean Networks)
- `context/product/ai-market-positioning.md` - AI-inference positioning (latency as the bottleneck, deterministic paths). Read for calls with neocloud / AI-colo prospects.
- `context/product/pbc-pce-datasheet.md` - Full PBC/PCE hardware and software spec for technical deep dives
- `context/partner-assets/product-quick-reference.md` - Quick-reference SKU and capability summary
- `context/partner-assets/maiaedge-101.md` - Partner edition; has the 30-second pitch by segment

**Sales context:**
- `context/sales/pricing-reference.md` - PBC/PCE SKUs, term pricing, discount policy
- `context/sales/call-intelligence.md` - Patterns from past calls organized by segment
- `context/sales/use-case-taxonomy.md` - Canonical use cases (21 operator + Enterprise-specific). Map the prospect's likely needs to named use cases before the call so discovery questions land on real territory.
- `context/sales/edge-ai-thesis-montauk.md` - Third-party (Montauk Capital) validation of the distributed edge-AI + latency-bottleneck narrative. Exec-level discovery hook and business-case framing for AI-adjacent prospects.
- `context/sales/neocloud-strategy-brief.md` - NeoCloud go-to-market strategy, competitive angles, and pricing intelligence
- `context/segments/enterprise-use-cases.md` - Enterprise-specific use cases and in-house net-eng discovery patterns
- `context/product/cloud-onramp-business-case.md` - Cloud on-ramp economics model (break-even, margin tiers, multi-cloud vs BGP)
- `context/product/economic-impact-acg-whitepaper.md` - Third-party ACG whitepaper ROI validation for exec-level business case

**HubSpot / deal schema (for POC scoping and deal-stage alignment):**
- `context/hubspot/poc-schema.md` - POC structure, stages, and required fields
- `context/hubspot/deals-schema.md` - Deal stages, defaults, and MEDDPICC fields
- `context/hubspot/call-schema.md` - Call engagement fields and logging schema

**Compliance + sovereignty:**
- `context/europe/sovereignty-positioning.md` - DORA/NIS2 angle for European prospects; sovereign routing framing
- `context/marketing/sovereign-routing-explainer.md` - Technical explainer for path-level sovereignty claims

**Glossary:**
- `context/core/terminology-glossary.md` - Canonical product and network terminology for technical conversations
- `context/partner-assets/use-case-gpu-cluster-connectivity.md` - GPU cluster connectivity use case deep dive (NeoCloud + AI-colo)

**Territory:**
- `context/hubspot/territory-model.md` - Authoritative 5-region owner map (Northeast / Southeast / Central / Europe / International). Use to confirm which rep owns the account before the call.

## Meeting Prep Framework

### 1. Acknowledge What They've Built
Always start by understanding and respecting what the prospect has accomplished. Never lead with what's broken. Lead with what's impressive, then identify the gap.

### 2. Discovery Questions by Segment

**Fiber Operators:**
- "What percentage of your fiber is generating revenue?" (Signal: 30-50% = buying signal)
- "When you extend reach through NNIs, what does that look like?" (Signal: 60-90 days = buying signal)
- "How do you handle Type 2 circuits? What visibility?" (Signal: "black hole" = buying signal)
- "How many multi-state deals have you lost to provisioning delays?"
- "What does NNI establishment look like today?" (Signal: LOAs, VLAN coordination, BGP = buying signal)
- "How do you provision new paths within your own network?" (Signal: manual, different systems = buying signal)

**Red flags (poor fit):** 85%+ fiber utilized, automated NNI establishment, fully automated end-to-end, API-driven in days.

**Colocation:**
- "When tenants need interconnection or cloud connectivity, what happens today?"
- "How do you handle cross-connect provisioning?"
- "Are you seeing demand for self-service connectivity from tenants?"
- "How often do tenants go to Equinix or Megaport for connectivity you could provide?"
- "What does your interconnection revenue look like vs. space and power?"

**Network Operators:**
- "Is your internal automation unified across all network domains?" (Signal: pockets, not unified = buying signal)
- "What's your provisioning timeline for enterprise requests?" (Signal: weeks, compared to cloud = buying signal)
- "How do you handle multi-carrier paths today?" (Signal: painful, LOAs, weeks = buying signal)
- "What happens when customers need connectivity beyond your footprint?"
- "What visibility do you have across internal domains?"

**MSP/Aggregators:**
- "What visibility do you have into carrier networks?" (Signal: none, blind = buying signal)
- "How do you prove SLA compliance to customers?" (Signal: rely on carrier reports = buying signal)
- "What's your provisioning timeline vs. direct carrier relationships?"
- "How do you handle multi-carrier troubleshooting?"
- "Are Tier 1s competing for your customers directly?"

**Neoclouds (sub-segment determines entry):**

*Universal discovery (all neocloud sub-segments):*
- "How do you move data between object storage and your GPU clusters?" (Signal: public internet, slow = buying signal)
- "What does your network observability look like across facilities?" (Signal: none, blind = buying signal)
- "When you spin up a new facility, how long does connectivity take?" (Signal: weeks, multi-week project = buying signal)
- "What's your egress cost profile?" (Signal: $0.05-0.09/GB, don't know Direct Connect = buying signal)

*Tier 1 Inference (Together.ai, Inference.net, Fireworks):*
- "Where does data pipeline latency actually come from? Is it compute or the network?" (Signal: can't tell = buying signal)
- "Do you have anyone dedicated to the network side?" (Signal: lost the person, IT admin only = buying signal)

*Serverless GPU (RunPod, Modal, Vast.ai):*
- "When a customer complains about performance, can you tell if it's the supplier's network?" (Signal: blind = buying signal)
- "How many GPU suppliers are you managing connectivity across?" (Signal: 15+ in random facilities = buying signal)

*Crypto-to-AI (Applied Digital, Hut 8, TeraWulf):*
- "Your power and space are the asset. What does the connectivity look like?" (Signal: enterprise switches, single uplinks = buying signal)
- "Bitcoin doesn't care about latency, but AI does. How are you handling that transition?"

*Large-Scale GPU (Lambda, Crusoe, Nebius):*
- "Your network team is building. What tooling do they have for cross-carrier orchestration?"
- "At 30+ facilities, are you automating connectivity or managing each site individually?"

**Red flags (neocloud poor fit):** Already built 35+ PoPs with dedicated networking team (Groq model), fully solved with unlimited VC, acquired by hyperscaler.

**Enterprise (Multi-DC ICP - sub-segment determines emphasis):**

*Universal discovery (all four Enterprise sub-segments):*
- "How is your dark fiber between DCs redundant today?" (Signal: one pair, one path, no automated failover = buying signal)
- "When you need AWS Direct Connect, Azure ExpressRoute, or GCP Cloud Interconnect, who handles it?" (Signal: Megaport / Equinix Fabric, their portal, their SLA = buying signal)
- "How do you prove to compliance / audit where data went between DCs?" (Signal: can't beyond BGP routing tables = buying signal)
- "How long does a new DC or DR site take to come online from a networking perspective?" (Signal: months = buying signal)
- "What does your network team look like - VP Network, Director, Principal? Where are you hiring?" (Signal: 24/7 NOC + active hiring for senior network roles = strong qualifier)
- "Direct carrier contracts or all through a reseller / MSP?" (Signal: all through reseller / MSP = DISQUALIFIER, not Enterprise ICP)

*Financial Services - Enterprise:*
- "How are inter-DC paths protected from SOX / PCI-DSS perspective?" (Signal: best-effort BGP + manual audit reconstruction = buying signal)
- "Have you been through a recent PCI audit finding or GDPR enforcement event?" (Signal: yes + compliance pressure event = urgency lever)

*Healthcare Systems - Enterprise:*
- "How does EHR DC redundancy survive a single fiber cut today?" (Signal: single fiber pair, no diverse path = buying signal)
- "Have you had a recent HIPAA breach disclosure or HITRUST audit finding?" (Signal: yes = strong urgency lever, regulatory pressure)
- "Are your imaging archives + radiology workloads on the same DC paths as EHR?" (Signal: yes + variable latency = buying signal)

*Retail and Distribution - Enterprise:*
- "How is dark fiber between your corporate DCs redundant today?" (Signal: single pair, no automated failover = buying signal - this is the Meijer-archetype pain)
- "How do distribution-center networks integrate with corporate IT paths?" (Signal: separate fabrics, manual stitching = buying signal)
- "What's your cloud on-ramp posture for SaaS and analytics today?" (Signal: Megaport / Equinix Fabric, portal owned by third party = buying signal)

*Outsourcing Services - Enterprise:*
- "How do you handle delivery-center reliability across geographies?" (Signal: best-effort transport, regional carrier patchwork = buying signal)
- "When clients ask for path-level audit trails on their data, what do you provide?" (Signal: nothing beyond carrier reports = buying signal)
- "Are you a project consulting firm primarily or operational delivery primarily?" (Signal: PROJECT consulting = DISQUALIFIER, not Enterprise ICP)

**Red flags (Enterprise poor fit):** Network fully outsourced to single MSP, single DC, no direct carrier contracts, sub-$1B revenue, Manufacturing / Energy-Utilities / Logistics / Government / Defense / SaaS-only vertical, pure project-based consulting firm.

### 3. Pain Validation (Dig Deeper)

After initial discovery, validate with specific operational questions:
- "Where does provisioning slow down?"
- "What happens when a deal requires cross-carrier paths?"
- "How many people touch a new circuit activation?"
- "What's the cost of a provisioning delay in terms of deals or SLA penalties?"

<!-- Canonical source: context/copy-strategy/segment-messaging.md -->
### 4. Value Prop Mapping

Map MaiaEdge value to THEIR specific situation. Pillars are segment-specific:

**For full value prop matrices per segment, see context/copy-strategy/segment-messaging.md**

| Segment | Pillars |
|---------|---------|
| Fiber | EXTEND REACH \| MONETIZE \| AUTOMATE |
| Network Op / MSP | AUTOMATE \| EXTEND REACH \| MONETIZE |
| Colo | INSTANT \| MONETIZE \| REACH |
| AI Colo | DETERMINISTIC \| INSTANT \| MONETIZE |
| Neocloud | DETERMINISTIC \| PRIVATE \| INSTANT |
| Enterprise (Multi-DC ICP) | REDUNDANT \| SOVEREIGN \| AUTOMATED |

- **Automate:** "Activate deterministic private paths over fiber or DIA instantly. No BGP, no MPLS, no routing complexity."
- **Extend Reach:** "Extend reach through seamless carrier-to-carrier partnerships while maintaining visibility and customer sovereignty."
- **Monetize:** "Turn infrastructure into revenue. Provide services beyond your footprint, monetize idle fiber, offer cloud connectivity under your brand."
- **Deterministic:** "Deterministic paths that eliminate the network as a variable for AI workloads."
- **Private:** "Private cloud connectivity that cuts egress costs 60-80% vs public internet."
- **Instant:** "Instant customer on-ramp. New facilities go live in minutes, not weeks."

### 5. Proof Points (When to Use Each)

| Proof Point | Best For | Trigger |
|-------------|----------|---------|
| Arvig  -  "almost instantaneous" provisioning | Speed objections, fiber operators | "How fast can you really provision?" |
| RevNet  -  "Megaport capability between providers" | NaaS comparison, multi-carrier | "Why not just use Megaport?" |
| NTT  -  Network simplification, PoP acceleration | Tier 1 credibility, scale | "Who else at our scale uses this?" |
| IENTC  -  800+ cell towers, 20+ data centers | Mobile backhaul, massive scale | "Can this handle our volume?" |
| Equinix  -  "Revolutionary and creative" | Technical skeptics, credibility | "Is this proven technology?" |
| Ocean Networks  -  Cross-carrier connectivity to INDATEL | Geographic isolation, partnership | "How does cross-carrier connectivity actually work?" |

### 6. Talk Tracks by Persona

**VP Network / VP Operations (technical leadership):**
"You've invested in fiber/infrastructure, but it's likely fragmented. Different systems at each location, manual provisioning across your own network before you even get to partners. MaiaEdge unifies your network first, then extends that automation to partners."

**VP Sales / Business Development (commercial):**
"What if you could provision across your own network in minutes, not weeks? And then say yes to every multi-state RFP with the same speed? Customers go with whoever's faster. Now that's you, everywhere."

**Director of Engineering / Sr. Network Engineer (technical IC):**
"Provisioning across your own segments probably looks a lot like your NNI process. Manual config at each site, weeks to stand up new paths. MaiaEdge unifies your network first: PBCs at each internal boundary, automated provisioning, end-to-end visibility. No routing protocols, hop-by-hop telemetry across the entire path."

**CEO / President (strategic):**
"You're sitting on infrastructure that should be generating more revenue. MaiaEdge lets you monetize what you already own and extend your reach without building new infrastructure."

**Neocloud CEO / Founder:**
"**Master pitch:** Connecting distributed AI infrastructure simply. You need multi-tenancy, deterministic performance, private cloud connectivity that cuts your customers' egress 60-80%, and instant on-ramp for new facilities. No WAN team required. OPERATOR sovereignty banned. DATA sovereignty ('sovereign by design', 'paths you control') allowed. No network jargon (VLAN, Q-in-Q)."

**Neocloud CTO / VP Eng:**
"You're probably seeing 15-40ms of network variance that nobody's measuring. That compounds per token on inference. We give you hop-by-hop telemetry across paths you don't own, and deterministic paths that eliminate the network as a variable. No VLAN coordination, no Q-in-Q complexity."

**Neocloud VP Infrastructure:**
"Every new facility is a multi-week connectivity project right now. With MaiaEdge, your team provisions paths in minutes. Same connectivity at any colo, unified fabric across all your locations."

**Neocloud CFO / Finance:**
"Public internet egress at $0.05-0.09/GB vs $0.02/GB via private paths. For training runs moving TBs, that's 60-80% savings. OpEx model, no CapEx."

**Enterprise VP Network Infrastructure / Director Network Engineering (primary technical champion):**
"Your DR strategy assumes the dark fiber between your DCs is redundant. Unless you've got PBCs at each end, diverse fibers, and automated failover, it's one cut from an outage. MaiaEdge makes that fabric across your sites - productized, operable by the team you already have, no BGP across the WAN."

**Enterprise CIO (economic buyer):**
"You're multi-cloud and being asked to make that feel like one cloud to the network team and the auditors. AWS Cloud WAN, Azure vWAN, GCP NCC - each works per cloud, none federate across them, and none solve the dark fiber redundancy problem at all. MaiaEdge is the cross-cloud, cross-DC layer under your control. Cloud on-ramps under your brand, audit trails on the wire."

**Enterprise CSO / CISO (security stakeholder):**
"BGP best-effort cannot prove where data went. With MaiaEdge, the path itself is the audit artifact. Policy-based path control with jurisdictional audit trails. Line-rate AES-256-GCM IPsec on every path. Hop-by-hop visibility including Type 2. Compliance asks where the data went - your network team has the answer."

**Enterprise Network Architect / Principal Network Engineer (technical influencer):**
"HAsync and HAfabric on the SSRs sharing a single dark fiber pair is the most common pattern I'm seeing. PBCs at each end of dark fiber, diverse fibers, automated failover. No routing protocols to manage, no BGP convergence to debug. Hop-by-hop telemetry across the entire path, including Type 2."

### 7. Technical Deep Dive (If Needed)

**Product summary for technical conversations:**
- PBC: 1RU, dual 100G, AES-256-GCM, protocol-free forwarding, merged L2/L3, <2μs latency overhead
- PCE: Cloud-native, deterministic path computation, SRLG-aware, hop-by-hop telemetry, white-label portal, API-first
- Port Extender: 48x 10/25GbE, 8x 100GbE, <500ns port-to-port, for colo meet-me rooms
- Integrations: Equinix Fabric API, Megaport API, MEF/Mplify LSO Sonata compatible
- Model: IaaS subscription, 1/3/5-year terms, 10G or 100G tiers

**What PBC is NOT:** Not a router replacement. Complements Cisco/Juniper. Sits at domain boundaries where existing automation stops.

### 8. Cloud On-Ramp Business Case (If Relevant)

For colos and fiber operators interested in cloud connectivity:
- 10G deployment: Breaks even at ~4 customers, ~47% gross margin at full utilization
- 100G deployment: ~59% gross margin at 60% utilization, ~75% at full utilization
- Single 100G port generates 46K+ USD/month contribution at full utilization
- Multi-cloud without BGP complexity  -  no cloud routers needed
- Provider keeps full sovereignty: their portal, pricing, SLAs, customer relationships
