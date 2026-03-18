# Neocloud Cheatsheet

**MaiaEdge Sales Quick Reference — Neocloud (GPU Cloud Providers)**
February 2026 | Confidential

---

## Know Your Customer

| Attribute | Details |
|-----------|---------|
| What They Own | GPU clusters across multiple colo facilities, AI/ML software stacks, orchestration platforms. They do NOT own buildings — they lease from colos. |
| Revenue Model | GPU compute rental (hourly/reserved), inference-as-a-service, training cluster access, managed AI infrastructure. |
| Scale | Rapidly scaling. $50M–$5B+ revenue. Multi-facility (3–30+ locations). Expanding from 3 to 30+ facilities in 1–2 years is common. |
| Competitive Reality | Compute companies that accidentally became networking companies. No WAN teams, no Kentik, no PRTG. Network is an afterthought until inference latency becomes unpredictable. |
| Key Distinction | Neoclouds ARE the end customer — they deploy their own infrastructure. Do NOT use "keep your customer" language. They are the customer. |
| Priority | HIGH — Top 3 segment alongside Colocation and Fiber Operators. |

**Example Companies:** CoreWeave, Lambda Labs, Crusoe Energy, Voltage Park, Together AI, Anyscale, RunPod, Paperspace, Nebius, Groq, Cirrascale, DeepInfra, Vultr, DigitalOcean, Fluidstack, Modal, Nscale, Firmus, E2E Networks, Yotta Data Services, IREN (Iris Energy), Core Scientific, Northern Data Group, TeraWulf

> **⚠️ CoreWeave Targeting Note:** CoreWeave told Abilash at MetroConnect (Feb 2026) that they do not have the same challenges as other NeoClouds. **Not an active target right now.** Keep as reference company for market context and segment classification, but do not include in active outreach campaigns.

---

## INVERTED MESSAGING HIERARCHY

Unlike every other MaiaEdge segment, neocloud messaging follows an inverted order:

| Priority | Message | Hook |
|----------|---------|------|
| **1. LEAD** | **Observability** | "See why you're slow. Then fix it." |
| **2. SECOND** | **Cloud On-Ramp** | Accelerate cloud and hyperscaler connectivity across multi-facility deployments |
| **3. THIRD** | **Deterministic Paths** | Known hop count, controlled latency, eliminate network as a variable |

**Why inverted?** Neoclouds don't frame their pain as a networking problem. They experience it as "inference is slow and we can't figure out why." Lead with the symptom (you can't see why inference is slow), NOT the solution (deterministic paths). Once they see the visibility, the path engineering sells itself.

---

## Baked Value Props (Path Control / WAN Ownership)

Use these when the email angle is about path control, WAN ownership, or eliminating carrier dependency. Not forced into every email. The observability-first hierarchy still holds for Email 1 in most sequences. These fit Email 2, or when research shows the prospect already has some WAN visibility and the gap is control.

**Value Prop 1 (technical framing):**
Every GPU cluster you spin up across sites inherits a best-effort network you don't control. Carrier routing, invisible paths, no recourse when latency spikes. Drop in a MaiaEdge PBC. Instant private WAN between AI sites. No routing protocols. Paths in minutes. Programmable and visible.

**Value Prop 2 (positioning framing):**
Distributed AI needs a different kind of network. One you own, provision instantly, and don't have to beg a carrier to fix. MaiaEdge is instant WAN for GPU clouds. Drop in our infrastructure, private paths between sites come up in minutes. No routing protocols. Programmable and visible.

---

## Segment Vocabulary Lock

When writing for neoclouds, you MUST use terms from this segment's vocabulary. If a term belongs to another segment, it is BANNED.

**MUST use (neocloud vocabulary):**
inference latency, jitter, middle mile, facility, observability, training run, recompute tax, egress, GPU cluster, deterministic paths, best-effort, carrier routing, WAN, paths, programmable, visible

**BANNED (from other segments -- using these in neocloud outreach breaks credibility):**
- sovereignty, keep your customer, your portal your invoice (operator sovereignty language)
- route miles, NNI, lit vs dark, plant, fiber islands, dark fiber (fiber operator language)
- cross-connect, meet-me room, attach rate, tenant, space and power (colocation language)
- upstream carriers, finger-pointing, SLA compliance, asset-light (MSP language)
- multi-domain orchestration, on-net/off-net, configuration drift (network operator language)
- build your own fabric, fabric-in-a-box (colo/fiber positioning)
- Same team that built Acme Packet / 128 Technology (no credibility anchors in outreach)

**No sign-offs in emails.** Signatures are auto-appended by the email platform.

---

## Problems We Solve

| Problem | How MaiaEdge Solves It |
|---------|----------------------|
| Can't see why inference latency varies by facility | Hop-by-hop observability across every path between GPU clusters — see the network for the first time |
| Each new facility is a 6-week connectivity project | Provision deterministic paths between facilities in minutes, not weeks |
| No visibility once traffic leaves their infrastructure | End-to-end telemetry across paths that traverse multiple colos and carriers |
| Coordinating multiple carriers for each site is painful | Single control plane across all facility interconnects — one platform, not 5 carrier portals |
| Best-effort routing introduces inference latency variance | Deterministic private Ethernet paths with known hop count and controlled latency characteristics |
| Cloud/hyperscaler connectivity is slow to stand up | Cloud on-ramp via API integrations — accelerate connectivity to AWS, Azure, GCP across facilities |

---

## Top Pain Points (Their Words)

"We're scaling to 30+ facilities and connectivity is our biggest operational bottleneck."
"Inference latency varies by facility because every path is different."
"We can't see what happens between our facilities — it's a black box."
"Provisioning connectivity to a new facility takes weeks. We need it in days."
"We can't guarantee consistent inference SLAs across facilities because the network is unpredictable."
"Each new facility is different — different carrier, different topology, different performance."

---

## Key Personas

| Persona | Titles | What They Care About |
|---------|--------|---------------------|
| **CEO/Founder** | CEO, Co-Founder, President | Scaling infrastructure fast, cost efficiency, competitive differentiation. Not a networking buyer — cares about removing bottlenecks to GPU utilization. |
| **CTO/VP Engineering** | CTO, VP Engineering, VP Platform | Network determinism for inference, multi-facility consistency, troubleshooting latency. Most likely technical champion. |
| **VP Infrastructure** | VP Infrastructure, VP Data Center Operations, VP Cloud Infrastructure | Provisioning speed for new facilities, carrier coordination, operational complexity. Feels the pain daily. |
| **Network/IT Admin** | Network Admin, IT Admin, Infrastructure Engineer, DevOps Lead | The person wearing a networking hat who isn't a network engineer. Managing connectivity without WAN expertise. Often the first to feel observability pain. |
| **Network Architect** | Network Architect, Principal Engineer, Head of Networking | End-to-end visibility, cross-facility path control, latency consistency. When this role exists, they're the technical validator. |
| **Head of Platform** | Head of Platform, VP Product, Director Platform Engineering | Consistent inference SLAs, predictable performance regardless of facility location. |

---

## Neocloud Sub-Segments

> **Note:** AI Data Centers (Nexus, Aligned Data Systems, H5 Data Centers, EdgeConneX) share characteristics with neoclouds but are covered under **Colocation — AI Infrastructure** in the ICP Sales Playbook. Cross-reference that section when encountering AI-focused data center operators.

### Sub-Segment Quick Reference

| Sub-Segment | Examples | Key Signal | Messaging Emphasis | HubSpot `customer_sub_segment` |
|-------------|----------|------------|-------------------|-------------------------------|
| **Large-Scale GPU NeoClouds** | CoreWeave*, Nebius, Lambda (15+ US DCs, 320MW) | Multi-facility GPU-as-a-service, 20-50+ locations, bare-metal GPU clusters | Observability across distributed training clusters, deterministic inter-facility paths | `Large-Scale GPU NeoClouds` |
| **Tier 1 Inference Providers** | Together.ai (25+ cities, 200MW), Groq (35 Equinix POPs), Cirrascale, DeepInfra | Distributed inference endpoints at 20-50+ edge locations, sub-100ms token latency SLAs | Real-time telemetry for latency diagnosis, multi-carrier orchestration between edge POPs | `Tier 1 Inference Providers` |
| **AI Infrastructure Providers** | Vultr, DigitalOcean, Fluidstack, Modal, RunPod | Mid-market cloud providers adding GPU compute, existing customer base asking for AI/ML | Multi-cloud bridge (white-label portal), Mean Time To Innocence, high-margin port arbitrage | `AI Infrastructure Providers` |
| **Sovereign AI Clouds** | Nscale (UK/EU, $1.1B Series B), Firmus (Norway), E2E Networks (India), Yotta (India) | Built for GDPR/DPDP/national AI programs, hard restrictions on data storage AND transit | Policy-based sovereign routing, in-country PCE deployment, jurisdictional audit trails | `Sovereign AI Clouds` |
| **Crypto-to-AI (Power-Rich Landlords)** | IREN (Iris Energy, $9.7B Microsoft contract), Core Scientific, Northern Data Group, TeraWulf | Former Bitcoin mining infrastructure pivoting to AI, cheap power ($0.03/kWh), high-density cooling | Simple fabric for tenant audits, observable uptime, infrastructure arbitrage | `Crypto-to-AI Pivots` |

*CoreWeave: Not an active target per Metro Connect intel (Feb 2026). Reference only.*

---

### Sub-Segment Deep Dives

#### 1. Large-Scale GPU NeoClouds

**Who they are:** Specialized cloud providers focused exclusively on GPU-as-a-Service for LLM training and inference. Massive multi-facility footprints (20-50+ locations). NOT traditional clouds — bare-metal GPU clusters with custom network topologies and liquid cooling.

**Their architecture:**
- Inside the DC: InfiniBand or Ultra Ethernet for GPU-to-GPU clustering (sub-microsecond latency, lossless)
- Between DCs: Traffic hits gateway/border router, encapsulated into Ethernet/IP, routed over dark fiber + DWDM, Carrier Ethernet / Waves (EXA), or IP Transit / DIA as backup

**Their pain:**
- Zero visibility once traffic leaves their facility. A 20TB dataset transfer from S3 to a GPU cluster takes 3x longer than expected — can't tell if it's a saturated switch, bad carrier route, or MTU issue
- BGP best-effort routing. Federating H100 clusters across multiple regions with no control over path selection. One bad carrier segment kills their SLA
- **Recompute Tax:** Network jitter during training causes session failures. Training crashes mid-job burn $4,800/GPU/month rebuilding KV cache (30% interruption rate on 128K context Llama-3 70B models)
- **Egress bleeding:** Paying $0.05–$0.09/GB on public internet when Direct Connect costs $0.02/GB. Leaving 60-80% savings on the table

**What MaiaEdge delivers:**
- Deterministic paths with visibility: PBCs at each facility create encrypted L2 paths with <2μs latency overhead. Hop-by-hop telemetry at EVERY hop — including inside AWS VPC Transit Gateways
- Multi-carrier orchestration: PCE computes optimal paths across existing carrier relationships. Automatic failover if one carrier degrades
- Direct cloud on-ramps: L2 paths into AWS VPCs/Azure VNets eliminate third-party cloud routers (saves $2,500-$5K/month per customer in BGP appliance costs)
- Sovereign routing: Jurisdictional metadata logged at every hop — prove training data never left US soil

**Walk-away knowing:** "MaiaEdge gives us deterministic, observable paths between our facilities — so our distributed training clusters perform like one unified fabric, not BGP best-effort guessing."

**Opening conversation:**
- "Walk me through what happens when you move 20TB training datasets from S3 to your GPU cluster in Kansas City. Do you know which path that takes? Can you see where latency spikes occur?"
- "When you federate H100 clusters across multiple regions for a distributed training run, how do you ensure deterministic latency between sites?"
- "What does your network team look like? Most NeoClouds we talk to have 1-2 network engineers — or IT admins who know servers but not BGP."

---

#### 2. Tier 1 Inference Providers

**Who they are:** Providers who've distributed inference endpoints to 20-50+ edge locations to hit <100ms token latency SLAs. NOT centralized like training clouds — they're everywhere users are. Many operate out of Equinix carrier hotels with minimal on-site staff.

**Their architecture:** Multi-city inference deployment requires cross-site connectivity for model synchronization between edge endpoints, routing user requests to nearest available GPU, and fallback when one city is overloaded or down. Right now they're riding public internet or buying point-to-point circuits between POPs. Zero visibility into cross-city paths.

**Their pain:**
- No network team. Example: Together.ai's network person recently quit. They have IT admins, not network architects
- Invisible performance degradation. When customer latency spikes from 60ms to 150ms, they have no idea if it's their carrier, AWS, or something in between
- SLA violations. Contractually obligated to deliver <75ms tokens. When they miss it, customers churn. But they can't diagnose what failed
- Support hell. Finger-pointing with carriers wastes engineering time. "Is it your network or mine?" becomes a recurring nightmare

**What MaiaEdge delivers:**
- Real-time telemetry: Dashboard shows EXACTLY which hop added latency
- Multi-carrier orchestration: PCE computes optimal paths between edge POPs. Auto-failover to alternate carrier path
- Cloud-side visibility: Read-only data from AWS/Azure APIs — Direct Connect Gateway status, Transit Gateway health alongside WAN metrics
- Self-service for enterprise customers: Customers click "connect my VPC to inference endpoint" in YOUR white-label portal — provisioned in minutes, not weeks

**Walk-away knowing:** "MaiaEdge delivers deterministic sub-100ms token latency across our edge cities — even when carriers have bad days — because we can see and control the path."

**Opening conversation:**
- "You're distributed across 25+ cities for low-latency inference. When latency spikes, how do you troubleshoot? Do you know if it's your carrier, AWS, or something in between?"
- "What happens when your enterprise customers need private connectivity from their VPC to your inference endpoint? Do you provision that yourself or send them to Megaport?"
- "What percentage of your support tickets are network-related vs compute-related? Can you actually diagnose the network issues?"

---

#### 3. AI Infrastructure Providers

**Who they are:** Mid-market cloud providers adding GPU compute to their product portfolio. Existing customer bases (developers, startups, SMBs) asking for AI/ML infrastructure. Some scaling rapidly to 30+ locations, many focus on high-density GPU capacity in 5–15 strategic global markets.

**⚠️ Competitive Threat — Megaport/Latitude.sh:** With Megaport's acquisition of Latitude.sh, a primary connectivity partner has transformed into a direct GPU-as-a-Service competitor. Sending customers to a Megaport portal for cloud on-ramp now introduces them to a platform actively selling native bare-metal GPUs. This makes MaiaEdge's white-label portal especially valuable for this sub-segment.

**Their pain:**
- "Their solution is a silo." Many have launched basic "Direct Connect" versions by 2026, but they're walled gardens. They struggle to provide low-latency, multi-cloud bridges between their GPUs and customer data in AWS S3 or Azure Blob
- Revenue & relationship leakage: Outsourcing connectivity to a third-party NaaS breaks the user experience and sends high-margin revenue to a platform now competing for the same AI infrastructure budget
- Configuration lag: Even if a virtual circuit is technically "up" in hours, manual negotiation of VLAN IDs, BGP ASN exchanges, and IP subnet overlaps takes days of engineering coordination
- Invisible performance gaps: "Lean" teams lack dedicated 24/7 WAN architects. When inference latency spikes, they can't diagnose if it's a saturated switch, bad carrier route, or microburst at the border
- Egress tax: Moving training data from hyperscale object storage to a mid-market cloud over public internet costs up to 9 cents per GB, compared to roughly 2 cents via Direct Connect

**What MaiaEdge delivers:**
- Multi-Cloud Bridge: Separate deterministic L2 paths connecting GPUs to AWS, Azure, GCP. Sub-10ms jitter paths eliminate "walled garden" constraints
- White-Label Portal = Own the Customer Relationship: Customers see the provider's brand, click "Connect to AWS/Azure/GCP," and paths provision in minutes. Customers never visit Megaport/Equinix portals where they'd discover competing GPU offerings
- Mean Time To Innocence (MTTI): PCE provides hop-by-hop observability to prove definitively whether a performance dip was caused by their fabric or an external carrier
- High-Margin Port Arbitrage: Buy ONE 100Gbps Equinix Unlimited port (only 2-3x cost of 10Gbps), serve many customers through MaiaEdge VLAN slicing and traffic engineering tiers. Turn connectivity from a cost center into a profit center
- Expand Reach: Automated federation — customer clicks 'Tokyo' in the portal, MaiaEdge orchestrates the path through a federated partner. No datacenter build required

**Walk-away knowing:** "MaiaEdge lets us offer true multi-cloud AI infrastructure, where customers' GPUs, storage, and models can live in different clouds with deterministic paths between them, all provisioned through OUR portal, so we own the revenue and relationship."

**Opening conversation:**
- "When enterprise customers ask for Direct Connect to AWS or ExpressRoute to Azure, how do you handle that today? Do you have to send them to a third party and lose that touchpoint?"
- "How much engineering time is currently wasted on the manual 'bureaucracy' of provisioning cross-connects — LOAs, VLAN negotiations, and BGP troubleshooting?"
- "If you wanted to turn multi-cloud connectivity into a high-margin, white-labeled product instead of a support headache, what would you need to build?"

---

#### 4. Sovereign AI Clouds

**Who they are:** Cloud providers built specifically to comply with data sovereignty requirements: GDPR (EU), DPDP Act (India), national AI programs (UAE, Saudi Arabia, Canada). They serve enterprises and governments with HARD restrictions on where data can be stored AND where it can TRANSIT.

**Their regulatory context:**
- GDPR: EU data cannot transit non-compliant jurisdictions (fines up to €20M or 4% global revenue)
- EU AI Act: Fully enforceable August 2026. Requires infrastructure-level proof of data control (fines up to 7% global revenue)
- India DPDP Act: Extraterritorial scope — applies if serving Indian citizens. Phased enforcement through May 2027
- US CLOUD Act: Creates direct conflict with GDPR. US entities can compel data access regardless of physical location
- National AI programs: UAE, Saudi Arabia, Canada treating sovereign AI as strategic national asset. Require certifiable proof that "every bit stays in-country"

**Their pain:**
- Data sovereignty isn't just about where GPUs sit — it's about where packets TRAVEL. BGP could route training data from London to Amsterdam through New York (CLOUD Act violation) or Singapore (non-GDPR). No way to know, prove compliance, or pass audit
- BGP doesn't understand jurisdictions. It routes to cheapest path, ignoring regulatory boundaries
- Cross-border federation breaks sovereignty. When a German sovereign cloud needs to connect to a French sovereign cloud, how do they ensure the path stays within EU?

**What MaiaEdge delivers:**
- Policy-based sovereign routing: Define "traffic MUST stay within EU" or "India-only paths." PCE enforces jurisdictional constraints programmatically. BGP can't override it
- In-country PCE deployment: The control plane itself can run on YOUR sovereign cloud (AWS GovCloud equivalent, Azure Government) — routing decisions never leave jurisdiction
- Audit trail: Every hop logged with timestamp, carrier, geographic location, latency. Hand this to regulators when EDPB asks "prove this training data never left EU"
- Cross-border federation with policy preservation: London → Paris path needed? PCE computes route that stays within GDPR jurisdiction (e.g., Germany → euNetworks Brussels → Paris). No US/Asia hops

**Walk-away knowing:** "MaiaEdge provides cryptographic proof that AI training traffic NEVER left UK/EU/India boundaries — even when packets transit three carriers to reach the cloud."

**Opening conversation:**
- "When you tell enterprise customers or government agencies that their data stays within [UK/EU/India], how do you prove that IN TRANSIT — not just at rest?"
- "BGP routes to the cheapest path. If a packet goes London → Amsterdam, can you guarantee it didn't touch a US carrier subject to the CLOUD Act?"
- "When GDPR auditors ask you to demonstrate data path control, what documentation do you provide? Do you have hop-by-hop logs with jurisdictional metadata?"

---

#### 5. Crypto-to-AI (The Power-Rich Landlords)

**Who they are:** Hardware-heavy firms that built massive power and cooling infrastructure for Bitcoin mining. Now pivoting to AI because they have the cheapest electricity ($0.03/kWh vs $0.08-$0.12 industry average), advanced cooling (immersion/liquid) already deployed, and high-density power (100kW+ per rack).

**Business model:** They are LANDLORDS, not cloud operators. They rent space, power, and cooling to Tier 1 Inference providers or Large-Scale GPU clouds. A Tier 1 Inference provider might actually be renting from a Crypto-to-AI company.

**Their architecture reality:** In crypto, if internet blips for 30 seconds, you lose 30 seconds of mining revenue. Annoying, but not catastrophic. In AI, if the network blips for 30 seconds during a 40TB training run, the entire job crashes. That's a million-dollar mistake for their tenants.

**Their pain:**
- The Uptime Trap: 59% of North American CIOs are cautious about retrofitted crypto facilities because they lack network redundancy. Tier 1 tenants won't sign leases if the facility doesn't have Tier 3+ network reliability
- Audit failures: When a $100M/year GPU tenant asks "Do you have 99.99% uptime and multi-path network failover?" they have no good answer. They're at the mercy of a local ISP
- Limited network expertise: They have power engineers, not network architects. They don't want to hire 5 new CCIEs to manage routing complexity

**What MaiaEdge delivers:**
- Simple fabric architecture that passes tenant audits: multi-path failover without routing protocol complexity
- Observable uptime: Dashboard proves to tenants that the network didn't cause the training crash. Eliminates finger-pointing
- Infrastructure arbitrage: They have $0.03/kWh power. If they can add connectivity as a margin-generating service (vs just passing through carrier costs), they improve economics

**Walk-away knowing:** "MaiaEdge upgrades your power-rich facility from a 'mining shed' to an 'AI-grade data center' by delivering the network redundancy and observability that Tier 1 GPU tenants demand, enabling operational efficiency with a lean team."

**Opening conversation:**
- "When a Tier 1 GPU cloud asks if you can provide 99.99% uptime and multi-path network redundancy, what do you tell them?"
- "How do you prove to tenants that a network issue didn't cause their training job to crash?"

---

## Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "How many facilities are you deployed across?" | "Multiple, and scaling rapidly" | "Single facility" |
| "How do you handle connectivity between GPU clusters in different facilities?" | "It's painful — each facility is different, takes weeks" | "We have a dedicated network team handling it well" |
| "What visibility do you have into paths between facilities?" | "None once traffic leaves our infrastructure" | "Full visibility end-to-end" |
| "Are you experiencing inference latency variance across different paths?" | "Yes, and it's hard to debug" | "Performance is consistent" |
| "How many different carriers are involved in connecting your facilities?" | "Multiple, and coordinating them is painful" | "Single carrier, simple topology" |
| "Do your enterprise customers require proof that data stays within specific geographic boundaries?" | "Yes, and we can't provide it today" | "Not a requirement" |
| "When inference performance degrades, how do you determine if it's GPU, software, or network?" | "It's usually a guessing game" | "We have full-stack observability" |
| "Who on your team manages network connectivity between facilities?" | "It's kind of everyone and no one" | "We have a dedicated WAN team" |

---

## Objection Handling

| Objection | Rebuttal |
|-----------|----------|
| **"We're focused on GPU infrastructure, not networking"** | That's exactly why. You shouldn't have to become network experts. MaiaEdge gives your team the ability to see why inference is slow across facilities — and provision deterministic paths in minutes without routing complexity. Focus on inference, not interconnects. |
| **"Our colo partners handle connectivity"** | Do they deliver deterministic paths with end-to-end visibility? Or best-effort cross-connects? Inference performance depends on network predictability. If you're debugging latency issues, the network is probably the variable you can't see. |
| **"We're building our own network team"** | Building a network team to manage multi-carrier complexity is expensive and slow. MaiaEdge gives you the capability without the headcount. Your team provisions paths; we handle the protocol complexity. |
| **"Each facility is different — how does this work?"** | That's the point of federation. MaiaEdge PBCs at each location, unified under one control plane. Doesn't matter if it's Aligned in Dallas or Cologix in Columbus — same deterministic paths, same visibility, same provisioning speed. |
| **"We don't have this problem yet"** | You do — you just can't see it yet. Inference latency variance is invisible without cross-facility observability. Once you can see the network between your GPU clusters, you'll find the variance that's been there all along. |
| **"Who are you?"** | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper). Two exits, $2.5B+ combined. We built carrier infrastructure that network operators deploy. |

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Cross-Facility Observability** | See why inference is slow. Hop-by-hop visibility across paths between GPU clusters in different colo facilities. The first thing they need. |
| **Distributed Inference Fabric** | Deterministic paths between GPU clusters across multiple colo facilities for consistent inference performance. |
| **Rapid Facility Onboarding** | New facility connectivity in minutes instead of weeks as neocloud scales from 3 to 30+ locations. |
| **Sovereign AI Delivery** | Unified fabric across all locations with sovereign routing — customer workloads get provably private paths regardless of underlying carriers. |
| **Cloud On-Ramp Acceleration** | Private paths to AWS/Azure/GCP for RAG architectures requiring multi-cloud data retrieval. Layer 2 of the neocloud pain hierarchy. |

---

## Account Tiering

| Tier | Criteria |
|------|----------|
| **Tier 1** | 5+ facilities, publicly announced GPU capacity >100MW, rapid expansion trajectory |
| **Tier 2** | 2–4 facilities, growing, $50M+ revenue or significant funding |
| **Tier 3** | Early-stage, single facility expanding to second |

---

## Expansion Path

**Land:** Cross-facility observability ("see why you're slow")
**Expand 1:** Deterministic paths between primary GPU cluster locations
**Expand 2:** Rapid onboarding for new facilities as they scale
**Expand 3:** Cloud on-ramp for multi-cloud data access (RAG, hybrid inference)

---

## Channel Partnership Context

Neoclouds can be reached through colocation operators who host them. Datum.net (colo partner) provides potential channel access to neocloud tenants. The colo sells MaiaEdge as part of their connectivity fabric; the neocloud benefits from deterministic paths and observability.

**Key insight:** When a colo has GPU cloud tenants, MaiaEdge solves problems for BOTH the colo (revenue, retention) AND the neocloud (observability, performance). This is a dual-sale opportunity.

---

## Datum.net Channel Intelligence

**Datum is a channel partner, not just a customer.** Virtual telco with 18 Equinix POPs via NetActuate, scaling to 40+. Cloudflare-like anycast proxy architecture. They solve Layer 7 (proxy, anycast, DDoS); MaiaEdge solves Layer 2/3 (paths, observability, encryption). Together = full-stack answer.

### Key Contacts
- **Zach Smith** (CEO) — Former CEO of Packet (acquired by Equinix). Direct relationships with Together.ai, Inference.net, RunPod, Modal, Groq. Board member at Koya (now Mistral)
- **Brett Mertens** (BD) — Primary source of neocloud pain articulation
- **Drew Raines** — Technical lead
- **Shelby Lindsey** — Incoming backbone lead (ex-Equinix)
- **Manish Singh** — Engineering

### Specific Neocloud Intelligence from Datum
- **Together.ai:** Network person recently quit. Biggest pain is data movement from object stores
- **RunPod:** 200K+ users, 15+ GPU suppliers in random facilities
- **Modal:** Serverless compute. Same networking gaps as RunPod
- **Groq:** 35 Equinix PoPs in 6 months, targeting sub-100ms inference latency

---

## Neocloud TAM & Coverage Analysis

### Estimated Total Addressable Universe: 250–350 Companies
Triangulated from multiple sources (Neocloud.world, SemiAnalysis, McKinsey, Crunchbase).

### Current Coverage
- 142 companies identified, 125 tagged in HubSpot
- ~40–55% of estimated global universe
- Gap to close: ~100–200 companies not yet identified

### Coverage by Sub-Segment
| Sub-Segment | Estimated Total | Current Coverage | Gap |
|---|---|---|---|
| Tier 1 Inference Providers | 15–20 | 75–85% | Small |
| Large-Scale GPU Cloud | 20–30 | 60–70% | Moderate |
| Crypto-to-AI Pivots | 25–40 | ~45% | Moderate |
| Serverless/Inference Startups | 40–60 | 35–45% | Large |
| Sovereign AI / Telco GPU Clouds | 30–50 | ~25% | Very Large |
| Enterprise AI Platforms | 50–80 | ~20% | Very Large |

### 90-Day Coverage Targets
- From 142 → 200+ identified companies
- Crypto-to-AI pivots: 11 → 20–25
- Sovereign/Telco GPU clouds: 8–10 → 25+
- Serverless/inference startups: 10–12 → 20–25

---

## Neocloud Discovery Signal Framework

Seven signals to monitor for identifying new neocloud prospects:

### Signal 1: NVIDIA GPU Allocation Announcements
NVIDIA's preferred allocation strategy is the single best leading indicator. Monitor NVIDIA newsroom, GTC keynotes, regional AI factory announcements (18+ telco partnerships in last 18 months).

### Signal 2: Crypto Mining Pivot Announcements
CoinShares reports miners announced $65B in AI/HPC contracts by October 2025. Track SEC filings (10-K pivot language), hyperscaler lease announcements, GPU procurement orders. WGMI ETF holdings = ready prospect list. Watch: Applied Digital, Galaxy Digital, Stronghold, Argo Blockchain, Mawson, Northern Data Group, Cathedra Bitcoin, Soluna.

### Signal 3: Venture Capital / Growth Equity Rounds
Track Crunchbase/PitchBook for rounds tagged 'GPU cloud', 'AI infrastructure', 'inference platform'. Any Series A+ is a potential prospect. Recent examples: Nscale ($1.1B), Nebius ($1.7B total), CoreWeave (IPO'd at $48B).

### Signal 4: Sovereign AI National Initiatives
Active programs: Canada ($2B), India ($1.25B IndiaAI), EU AI Factories (13+ sites), Saudi Arabia (HUMAIN), UAE (Core42/Stargate), South Korea (260K+ GPUs), Japan (SoftBank, KDDI). Each initiative spawns 2–5 new GPU cloud operators.

### Signal 5: AI Colocation Tenant Lists
Existing colo segment is a direct feeder. Who's leasing at Aligned, Stack, Vantage, QTS, EdgeConneX? Those tenants are neocloud prospects. Every colo conversation should generate neocloud intelligence.

### Signal 6: Industry Trackers
McKinsey AI Index, Neocloud.world, SemiAnalysis, Synergy Research Group.

### Signal 7: Conference Intelligence
Key events: NVIDIA GTC (March, San Jose), OCP Global Summit, SC/Supercomputing, AI Infrastructure Day, Data Centre World, Datacloud Global Congress. Exhibitor and speaker lists are prospect lists.

---

## Instant Classification Keywords

"GPU cloud," "GPU-as-a-service," "AI cloud provider," "inference cloud," "ML infrastructure provider"

**Company Names:** CoreWeave, Lambda Labs, Crusoe Energy, Voltage Park, Together AI, Anyscale, RunPod, Paperspace

---

## One-Liner Quick Reference

| Situation | One-Liner |
|-----------|-----------|
| Opening pitch | "See why you're slow. Then fix it." |
| They say "we're not a networking company" | "Exactly. You shouldn't have to be." |
| They say "connectivity just works" | "Until inference latency varies by facility and you can't see why." |
| They're scaling fast | "Every new facility doesn't have to be a connectivity project." |
| They mention carrier complexity | "One control plane. All facilities. All carriers. Minutes, not weeks." |
| They ask about competitors | "Nobody else gives you hop-by-hop visibility across facilities you don't own networks between." |

---

*Cross-references: Messaging Framework V4 (Section 3.3 Neoclouds), ICP Sales Playbook, AI Market Positioning Guide, Cloud On-Ramp Business Case*

*Last updated: February 2026*
