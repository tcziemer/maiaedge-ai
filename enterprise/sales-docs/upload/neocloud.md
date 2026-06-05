# Neocloud Cheatsheet

**MaiaEdge Sales Quick Reference  -  Neocloud (GPU Cloud Providers)**
February 2026 | Confidential

---

## Know Your Customer

| Attribute | Details |
|-----------|---------|
| What They Own | GPU clusters across multiple colo facilities, AI/ML software stacks, orchestration platforms. They do NOT own buildings  -  they lease from colos. |
| Revenue Model | GPU compute rental (hourly/reserved), inference-as-a-service, training cluster access, managed AI infrastructure. |
| Scale | Rapidly scaling. $50M–$5B+ revenue. Multi-facility (3–30+ locations). Expanding from 3 to 30+ facilities in 1–2 years is common. |
| Competitive Reality | Compute companies that accidentally became networking companies. No WAN teams, no Kentik, no PRTG. Network is an afterthought until inference latency becomes unpredictable. |
| Key Distinction | Neoclouds ARE the end customer  -  they deploy their own infrastructure. Do NOT use "keep your customer" language. They are the customer. |
| Priority | HIGH  -  Top 3 segment alongside Colocation and Fiber Operators. |

**Example Companies:** Lambda Labs, Crusoe Energy, Voltage Park, Together AI, Anyscale, RunPod, Paperspace, Nebius, Groq, Cirrascale, DeepInfra, Vultr, DigitalOcean, Fluidstack, Modal, Nscale, Firmus, E2E Networks, Yotta Data Services, IREN (Iris Energy), Core Scientific, Northern Data Group, TeraWulf

---

## INVERTED MESSAGING HIERARCHY

### MASTER PITCH

Connecting distributed AI infrastructure simply. Every value prop below is a benefit of this master pitch.

| Priority | Pillar | Benefits |
|----------|--------|----------|
| **DETERMINISTIC** | Predictable performance between sites. See exactly where latency comes from. Extend reach across DCs and service providers. |
| **PRIVATE** | Private cloud connectivity (egress savings as competitive advantage for your customers: 2c/GB vs 9c/GB). Sovereign by design: data stays on paths you control. |
| **INSTANT** | Multi-tenancy: serve multiple customers from the same infrastructure. Instant customer on-ramp. New sites online in minutes. |

**Why this structure?** Neoclouds don't frame their pain as a networking problem. They experience it as distributed AI infrastructure that's hard to connect, slow to onboard customers onto, and expensive on egress. Lead with the master pitch, then support with the pillar that matches their specific pain.

---

## Baked Value Props (Path Control / WAN Ownership)

Use these when the email angle is about path control, WAN ownership, or eliminating carrier dependency. Not forced into every email. The master pitch  -  "connecting distributed AI infrastructure simply"  -  is the lead across sequences. Observability is a supporting benefit under the DETERMINISTIC pillar, not the entry. These value props fit when research shows the prospect is already feeling latency variance or is approaching the enterprise scaling wall (see "Enterprise Long-Tail Is the Scaling Wall" section below for angle selection).

**Value Prop 1 (technical framing):**
Every GPU cluster you spin up across sites inherits a best-effort network you don't control. Carrier routing, invisible paths, no recourse when latency spikes. Drop in a MaiaEdge PBC. Instant private WAN between AI sites. No routing protocols. Paths in minutes. Programmable and visible.

**Value Prop 2 (positioning framing):**
Distributed AI needs a different kind of network. One you own, provision instantly, and don't have to beg a carrier to fix. Drop in our infrastructure, private paths between sites come up in minutes. No routing protocols. Programmable and visible.

**Value Prop 3 (multi-tenancy framing):**
Serve multiple customers from the same infrastructure without dedicated hardware per site. Each customer gets isolated, private paths. Onboard new customers in seconds, not weeks. Low friction. They buy a port, you take care of everything else.

**Value Prop 4 (egress competitive advantage):**
Private cloud connectivity means your customers pay 2c/GB instead of 9c/GB over the public internet. That's not just your cost savings. That's a competitive advantage you sell to win and retain customers.

---

## Positioning: Work With Existing Stack (Not Rip-and-Replace)

MaiaEdge is **not a replacement** for anything the neocloud has already deployed. It is an overlay that works with the existing infrastructure choices.

- **NVIDIA-aligned.** PBC/PCE stack complements InfiniBand / Ultra Ethernet / Spectrum-X inside the facility. We orchestrate the paths between facilities, not the fabric inside them.
- **BGP/MPLS-complementary.** We don't replace carrier routing. We overlay deterministic paths above whatever transport the neocloud already has.
- **No routing protocols for the neocloud's team to learn.** PBCs drop in; PCE computes paths. The neocloud's engineering team stays focused on GPU infrastructure.

Use this framing explicitly when a prospect says "we're building our own network team" or "our colo partners handle connectivity" or "we don't want another vendor in the stack." We're not replacing; we're layering above.

---

## Segment Vocabulary Lock

When writing for neoclouds, you MUST use terms from this segment's vocabulary. If a term belongs to another segment, it is BANNED.

**MUST use (neocloud vocabulary):**
inference latency, jitter, middle mile, facility, observability, training run, recompute tax, egress, GPU cluster, deterministic paths, best-effort, carrier routing, WAN, paths, programmable, visible, multi-tenancy, instant customer on-ramp, sovereign by design, provably private, private cloud connectivity, extend your reach

**BANNED (from other segments -- using these in neocloud outreach breaks credibility):**
- OPERATOR sovereignty BANNED: keep your customer, your portal your invoice, build your own fabric. DATA sovereignty ALLOWED: sovereign by design, your data stays on paths you control, provably private. [Canonical source: context/outreach/email-writing-rules.md]
- VLAN, Q-in-Q (Network jargon. Neoclouds are compute people, not networking people. Say "serve multiple customers from the same infrastructure" or "each customer gets isolated, private paths.")
- route miles, NNI, lit vs dark, plant, fiber islands, dark fiber (fiber operator language)
- cross-connect, meet-me room, attach rate, tenant, space and power (colocation language)
- upstream carriers, finger-pointing, SLA compliance, asset-light (MSP language)
- multi-domain orchestration, on-net/off-net, configuration drift (network operator language)
- fabric-in-a-box (colo/fiber positioning)
- Same team that built Acme Packet / 128 Technology (banned in cold outreach; allowed in live presentations, demos, proposals, and objection handling  -  see Objection Handling section)

**No sign-offs in emails.** Signatures are auto-appended by the email platform.

---

## Problems We Solve

| Problem | How MaiaEdge Solves It |
|---------|----------------------|
| Can't see why inference latency varies by facility | Hop-by-hop observability across every path between GPU clusters  -  see the network for the first time |
| Each new facility is a 6-week connectivity project | Provision deterministic paths between facilities in minutes, not weeks |
| No visibility once traffic leaves their infrastructure | End-to-end telemetry across paths that traverse multiple colos and carriers |
| Coordinating multiple carriers for each site is painful | Single control plane across all facility interconnects  -  one platform, not 5 carrier portals |
| Best-effort routing introduces inference latency variance | Deterministic private Ethernet paths with known hop count and controlled latency characteristics |
| Cloud/hyperscaler connectivity is slow to stand up | Cloud on-ramp via API integrations  -  accelerate connectivity to AWS, Azure, GCP across facilities |
| Onboarding new customers is slow and complex | Instant customer on-ramp. They buy a port, you take care of everything else. Seconds, not weeks. |
| Each customer needs dedicated infrastructure per site | Multi-tenancy: serve multiple customers from the same infrastructure. Each gets isolated, private paths. |

---

## Top Pain Points (Their Words)

"We're scaling to 30+ facilities and connectivity is our biggest operational bottleneck."
"Inference latency varies by facility because every path is different."
"We can't see what happens between our facilities  -  it's a black box."
"Provisioning connectivity to a new facility takes weeks. We need it in days."
"We can't guarantee consistent inference SLAs across facilities because the network is unpredictable."
"Each new facility is different  -  different carrier, different topology, different performance."

---

## Key Personas

| Persona | Titles | What They Care About |
|---------|--------|---------------------|
| **CEO/Founder** | CEO, Co-Founder, President | Scaling infrastructure fast, cost efficiency, competitive differentiation. Not a networking buyer  -  cares about removing bottlenecks to GPU utilization. |
| **CTO/VP Engineering** | CTO, VP Engineering, VP Platform | Network determinism for inference, multi-facility consistency, troubleshooting latency. Most likely technical champion. Durable technical signer across all maturity stages. |
| **SVP/VP Infrastructure Engineering** | SVP Infrastructure Engineering, VP Infrastructure Engineering | Scale operations, direct RFP-facing. Where neocloud networking responsibility actually sits (neoclouds rarely silo a "VP Network" title - infra engineering rolls the function up). |
| **VP Infrastructure** | VP Infrastructure, VP Data Center Operations, VP Cloud Infrastructure | Provisioning speed for new facilities, carrier coordination, operational complexity. Feels the pain daily. |
| **Network/IT Admin** | Network Admin, IT Admin, Infrastructure Engineer, DevOps Lead | The person wearing a networking hat who isn't a network engineer. Managing connectivity without WAN expertise. Often the first to feel observability pain. |
| **Network Architect** | Network Architect, Principal Engineer, Head of Networking | End-to-end visibility, cross-facility path control, latency consistency. When this role exists, they're the technical validator. Rare at neoclouds below scale stage. |
| **Head of Platform** | Head of Platform, VP Product, Director Platform Engineering | Consistent inference SLAs, predictable performance regardless of facility location. |
| **CFO** | CFO, VP Finance | Unique to neoclouds vs. traditional cloud: CFO is a co-signer on infrastructure commitments because GPU financing dominates operating economics. Cares about the gross-to-net margin gap (network inefficiency, egress, recompute tax). Enters the buying committee at scale and public/large-cap stages. |

### Persona Prioritization by Company Size

Who to target primarily depends on where the neocloud is in its growth curve. Research the size before picking the title.

| Stage | Primary Targets | Secondary | Notes |
|-------|-----------------|-----------|-------|
| **Pre-revenue / early-stage** (<50 people, 1-2 sites) | CEO / Founder | CTO (if present) | Centralized authority. CEO owns everything. No dedicated network role. |
| **Mid-growth** (50-250 people, 2-5 sites) | CTO (durable technical signer) | SVP/VP Infrastructure Engineering, VP Infrastructure | "VP Network / Head of Networking" titles rare  -  don't over-prioritize that search. Infra engineering rolls up networking. |
| **Scale** (250+ people, 5+ sites) | CTO + SVP/VP Infrastructure Engineering + CFO | Head of Platform (SLA pain), VP Infrastructure | CFO enters as infrastructure cost arbiter / GPU-financing co-signer. Head of Platform owns agentic-latency pain. |
| **Public / large-cap funded** | CTO + CFO (explicit co-signer) | SVP/VP Infrastructure Engineering, Head of Platform | Infrastructure commitments file 8-K Item 1.01/2.03 within 4 business days  -  CFO alignment is required. |

---

## Neocloud Angle by Maturity

Not every neocloud is the same company. Where they are in their growth determines which door to open with. This is a research question, not a CRM field: before you write the email, figure out which angle applies. Same value props behind either door.

| Stage | Profile | What They're Living With | Angle |
|-------|---------|--------------------------|-------|
| **Pre-revenue / single site** | Nodiac, Colony Compute (early). Modular containers at power sites. First facility, no customers yet. | Solving for power, cooling, getting the first tenant in. Network is an afterthought they'll regret later. | **Watch list.** Too early for outreach. Flag when they announce a second site or first GPU tenant. |
| **Early growth (2-5 sites)** | Duos Edge AI, crypto-to-AI pivots (IREN, TeraWulf, Core Scientific). Small facility count, first real customers. | Each site wired up differently. Carrier relationships are one-off. Starting to feel the pain of inconsistency. | **In-pain-now (early).** "Bitcoin doesn't care about latency. Enterprise AI tenants do. The connectivity that worked for mining doesn't survive an inference SLA." |
| **Mid-growth (5-15 sites, mixed customers)** | Together.ai, RunPod, Modal, Baseten, DeepInfra. Mix of hyperscaler + enterprise. Lost or never had a network person. | Actively in pain. Latency varies by facility and they can't diagnose it. Each enterprise customer is a manual provisioning project. | **Both angles work.** Research determines which value prop lands  -  latency-debugging vs. scaling-model. |
| **Scale (15+ sites, hyperscaler-heavy)** | Lambda, Crusoe, Voltage Park, Nebius. Building network teams. Hyperscalers are 80%+ of customer base. | Not in pain today. Hyperscalers bring their own connectivity. But growth plan depends on serving mid-market enterprise who don't bring their own anything. | **Scaling-wall (new).** "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." |

**In-pain-now hooks** (mid-growth, latency variance dominant):
- "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between. That guessing game is expensive."
- "Every new facility is a different carrier, a different topology, a different provisioning timeline. At 5 sites that's manageable. At 15 it breaks."
- "Your team is probably two people who are really server engineers wearing a networking hat. They didn't sign up to debug carrier routing across 15 facilities."

**Scaling-wall hooks** (scale hyperscaler-heavy, enterprise ramp ahead):
- "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will."
- "Hyperscalers bring their own connectivity. The mid-market customers driving your next phase of growth don't."
- "Every enterprise customer onboarding is a connectivity project right now. Manual provisioning, carrier coordination, weeks per connection. That doesn't scale to 40 customers across 15 facilities."
- "GPU utilization gets all the board attention. But the thing that'll bottleneck your enterprise growth isn't compute availability. It's how fast you can get a new customer connected."
- "When a financial services firm asks for a private path to your inference endpoint across three facilities, what does that provisioning process look like today?"
- "The compute is commoditizing. The differentiation is moving to who can onboard enterprise customers fastest. That's an infrastructure problem, not a pricing problem."

**Early-growth / crypto-to-AI hooks** (2-5 sites, connectivity basics still being figured out):
- "Bitcoin doesn't care about latency. Enterprise AI tenants do. The connectivity that worked for mining doesn't survive an inference SLA."
- "The power and cooling are solved. The connectivity between sites is where the next tenant audit fails."
- "Modular compute at the edge solves the power queue. The question is what happens when your GPU tenants need deterministic paths between sites they've never heard of."

**Persona openers for scaling-wall neoclouds:**

| Persona | Opening Problem Statement | Don't |
|---------|--------------------------|-------|
| CEO / Founder | The compute is funded, the facilities are expanding, and the growth plan depends on serving customers who aren't hyperscalers. Each of those enterprise customers is a manual connectivity project right now. That math stops working as you continue to scale. | Technical anything. Protocol names. Don't frame as a networking problem  -  frame as a scaling constraint. |
| CTO / VP Eng | When an enterprise customer needs deterministic paths to your GPU clusters across three facilities, that's either 6 weeks of carrier coordination or it's automated. One of those scales. The other is why you're about to hire 4 network engineers you can't find. | Revenue or strategy framing. Keep it about engineering trade-offs and operational reality. |
| VP Infrastructure | The last 3 enterprise customer onboardings each took how many weeks? Different carrier at each site, different provisioning process, different timeline. Multiply that by the customers on the pipeline. | Vision or strategy. Stay operational. This persona feels the pain daily. |
| CFO / Finance | Enterprise customers on private paths pay 2c/GB instead of 9c/GB over public internet. That's not your cost savings  -  that's a pricing advantage you sell to win the contract. And multi-tenancy means you serve them without spinning up dedicated hardware per customer. | Technical terms. Dollars, unit economics, competitive pricing advantage only. |
| VP Sales / BD | When a mid-market customer asks how fast they can get private connectivity to your inference endpoint, the answer is your close rate. Right now that answer is measured in weeks. The competitors quoting days win that deal. | Architecture or infrastructure. This persona cares about deal velocity and win rate. |

**What stays the same across angles:** DETERMINISTIC | PRIVATE | INSTANT pillars. All value props (observability, cloud on-ramps, deterministic paths, multi-tenancy, instant customer on-ramp, egress competitive advantage). Vocabulary rules. Sovereignty constraints. Email structure and rules. The scaling-wall angle is a different door into the same product.

---

## Neocloud Sub-Segments

> **Note:** AI Data Centers (Nexus, Aligned Data Systems, H5 Data Centers, EdgeConneX) share characteristics with neoclouds but are covered under **Colocation  -  AI Infrastructure** in the ICP Sales Playbook. Cross-reference that section when encountering AI-focused data center operators.

### Sub-Segment Quick Reference

| Sub-Segment | Examples | Key Signal | Messaging Emphasis | HubSpot `company_sub_segment` |
|-------------|----------|------------|-------------------|-------------------------------|
| **Large-Scale GPU NeoClouds** | Nebius, Lambda (15+ US DCs, 320MW), Crusoe | Multi-facility GPU-as-a-service, 20-50+ locations, bare-metal GPU clusters | Observability across distributed training clusters, deterministic inter-facility paths | `Large Scale GPU - Neocloud` |
| **Tier 1 Inference Providers** | Together.ai (25+ cities, 200MW), Groq (35 Equinix POPs), Cirrascale, DeepInfra | Distributed inference endpoints at 20-50+ edge locations, sub-100ms token latency SLAs | Real-time telemetry for latency diagnosis, multi-carrier orchestration between edge POPs | `Tier 1 Inference - Neocloud` |
| **AI Infrastructure Providers** | Vultr, DigitalOcean, Fluidstack, Modal, RunPod | Mid-market cloud providers adding GPU compute, existing customer base asking for AI/ML | Multi-cloud bridge (white-label portal), Mean Time To Innocence, high-margin port arbitrage | `AI Infrastructure providers - Neocloud` |
| **Sovereign AI Clouds** | Nscale (UK/EU, $1.1B Series B), Firmus (Norway), E2E Networks (India), Yotta (India) | Built for GDPR/DPDP/national AI programs, hard restrictions on data storage AND transit | Policy-based sovereign routing, in-country PCE deployment, jurisdictional audit trails | `Sovereign AI Clouds - Neocloud` |
| **Crypto-to-AI (Power-Rich Landlords)** | IREN (Iris Energy, $9.7B Microsoft contract), Core Scientific, Northern Data Group, TeraWulf | Former Bitcoin mining infrastructure pivoting to AI, cheap power ($0.03/kWh), high-density cooling | Simple fabric for tenant audits, observable uptime, infrastructure arbitrage | `Crypto to AI - Neoclouds` |

---

### Sub-Segment Deep Dives

#### 1. Large-Scale GPU NeoClouds

**Who they are:** Specialized cloud providers focused exclusively on GPU-as-a-Service for LLM training and inference. Massive multi-facility footprints (20-50+ locations). NOT traditional clouds  -  bare-metal GPU clusters with custom network topologies and liquid cooling.

**Their architecture:**
- Inside the DC: InfiniBand or Ultra Ethernet for GPU-to-GPU clustering (sub-microsecond latency, lossless)
- Between DCs: Traffic hits gateway/border router, encapsulated into Ethernet/IP, routed over dark fiber + DWDM, Carrier Ethernet / Waves (EXA), or IP Transit / DIA as backup

**Their pain:**
- Zero visibility once traffic leaves their facility. A 20TB dataset transfer from S3 to a GPU cluster takes 3x longer than expected  -  can't tell if it's a saturated switch, bad carrier route, or MTU issue
- BGP best-effort routing. Connecting H100 clusters across multiple regions with no control over path selection. One bad carrier segment kills their SLA
- **Recompute Tax:** Network jitter during training causes session failures. Training crashes mid-job burn $4,800/GPU/month rebuilding KV cache (30% interruption rate on 128K context Llama-3 70B models)
- **Egress bleeding:** Paying $0.05–$0.09/GB on public internet when Direct Connect costs $0.02/GB. Leaving 60-80% savings on the table

**What MaiaEdge delivers:**
- Deterministic paths with visibility: PBCs at each facility create encrypted L2 paths with <2μs latency overhead. Hop-by-hop telemetry at EVERY hop  -  including inside AWS VPC Transit Gateways
- Multi-carrier orchestration: PCE computes optimal paths across existing carrier relationships. Automatic failover if one carrier degrades
- Direct cloud on-ramps: L2 paths into AWS VPCs/Azure VNets eliminate third-party cloud routers (saves $2,500-$5K/month per customer in BGP appliance costs)
- Sovereign routing: Jurisdictional metadata logged at every hop  -  prove training data never left US soil

**Walk-away knowing:** "MaiaEdge gives us deterministic, observable paths between our facilities  -  so our distributed training clusters perform like one unified fabric, not BGP best-effort guessing."

**Opening conversation:**
- "Walk me through what happens when you move 20TB training datasets from S3 to your GPU cluster in Kansas City. Do you know which path that takes? Can you see where latency spikes occur?"
- "When you connect H100 clusters across multiple regions for a distributed training run, how do you ensure deterministic latency between sites?"
- "What does your network team look like? Most NeoClouds we talk to have 1-2 network engineers  -  or IT admins who know servers but not BGP."

---

#### 2. Tier 1 Inference Providers

**Who they are:** Providers who've distributed inference endpoints to 20-50+ edge locations to hit <100ms token latency SLAs. NOT centralized like training clouds  -  they're everywhere users are. Many operate out of Equinix carrier hotels with minimal on-site staff.

**Their architecture:** Multi-city inference deployment requires cross-site connectivity for model synchronization between edge endpoints, routing user requests to nearest available GPU, and fallback when one city is overloaded or down. Right now they're riding public internet or buying point-to-point circuits between POPs. Zero visibility into cross-city paths.

**Their pain:**
- No network team. Example: Together.ai's network person recently quit. They have IT admins, not network architects
- Invisible performance degradation. When customer latency spikes from 60ms to 150ms, they have no idea if it's their carrier, AWS, or something in between
- SLA violations. Contractually obligated to deliver <75ms tokens. When they miss it, customers churn. But they can't diagnose what failed
- Support hell. Finger-pointing with carriers wastes engineering time. "Is it your network or mine?" becomes a recurring nightmare

**What MaiaEdge delivers:**
- Real-time telemetry: Dashboard shows EXACTLY which hop added latency
- Multi-carrier orchestration: PCE computes optimal paths between edge POPs. Auto-failover to alternate carrier path
- Cloud-side visibility: Read-only data from AWS/Azure APIs  -  Direct Connect Gateway status, Transit Gateway health alongside WAN metrics
- Self-service for enterprise customers: Customers click "connect my VPC to inference endpoint" in YOUR white-label portal  -  provisioned in minutes, not weeks

**Walk-away knowing:** "MaiaEdge delivers deterministic sub-100ms token latency across our edge cities  -  even when carriers have bad days  -  because we can see and control the path."

**Opening conversation:**
- "You're distributed across 25+ cities for low-latency inference. When latency spikes, how do you troubleshoot? Do you know if it's your carrier, AWS, or something in between?"
- "What happens when your enterprise customers need private connectivity from their VPC to your inference endpoint? Do you provision that yourself or send them to Megaport?"
- "What percentage of your support tickets are network-related vs compute-related? Can you actually diagnose the network issues?"

---

#### 3. AI Infrastructure Providers

**Who they are:** Mid-market cloud providers adding GPU compute to their product portfolio. Existing customer bases (developers, startups, SMBs) asking for AI/ML infrastructure. Some scaling rapidly to 30+ locations, many focus on high-density GPU capacity in 5–15 strategic global markets.

**Their pain:**
- "Their solution is a silo." Many have launched basic "Direct Connect" versions by 2026, but they're walled gardens. They struggle to provide low-latency, multi-cloud bridges between their GPUs and customer data in AWS S3 or Azure Blob
- Revenue & relationship leakage: Outsourcing connectivity to a third-party NaaS breaks the user experience and sends high-margin revenue to a platform now competing for the same AI infrastructure budget
- Configuration lag: Even if a virtual circuit is technically "up" in hours, manual negotiation of VLAN IDs, BGP ASN exchanges, and IP subnet overlaps takes days of engineering coordination
- Invisible performance gaps: "Lean" teams lack dedicated 24/7 WAN architects. When inference latency spikes, they can't diagnose if it's a saturated switch, bad carrier route, or microburst at the border
- Egress tax: Moving training data from hyperscale object storage to a mid-market cloud over public internet costs up to 9 cents per GB, compared to roughly 2 cents via Direct Connect

**What MaiaEdge delivers:**
- Multi-Cloud Bridge: Separate deterministic L2 paths connecting GPUs to AWS, Azure, GCP. Sub-10ms jitter paths eliminate "walled garden" constraints
- White-Label Portal = Own the Customer Relationship: Customers see the provider's brand, click "Connect to AWS/Azure/GCP," and paths provision in minutes
- Mean Time To Innocence (MTTI): PCE provides hop-by-hop observability to prove definitively whether a performance dip was caused by their fabric or an external carrier
- High-Margin Port Arbitrage: Buy ONE 100Gbps Equinix Unlimited port (only 2-3x cost of 10Gbps), serve many customers through MaiaEdge VLAN slicing and traffic engineering tiers. Turn connectivity from a cost center into a profit center
- Expand Reach: Automated reach extension  -  customer clicks 'Tokyo' in the portal, MaiaEdge orchestrates the path through a partner network. No datacenter build required

**Walk-away knowing:** "MaiaEdge lets us offer true multi-cloud AI infrastructure, where customers' GPUs, storage, and models can live in different clouds with deterministic paths between them, all provisioned through OUR portal, so we own the revenue and relationship."

**Opening conversation:**
- "When enterprise customers ask for Direct Connect to AWS or ExpressRoute to Azure, how do you handle that today? Do you have to send them to a third party and lose that touchpoint?"
- "How much engineering time is currently wasted on the manual 'bureaucracy' of provisioning cross-connects  -  LOAs, VLAN negotiations, and BGP troubleshooting?"
- "If you wanted to turn multi-cloud connectivity into a high-margin, white-labeled product instead of a support headache, what would you need to build?"

---

#### 4. Sovereign AI Clouds

**Who they are:** Cloud providers built specifically to comply with data sovereignty requirements: GDPR (EU), DPDP Act (India), national AI programs (UAE, Saudi Arabia, Canada). They serve enterprises and governments with HARD restrictions on where data can be stored AND where it can TRANSIT.

**Their regulatory context:**
- GDPR: EU data cannot transit non-compliant jurisdictions (fines up to €20M or 4% global revenue)
- EU AI Act: Fully enforceable August 2026. Requires infrastructure-level proof of data control (fines up to 7% global revenue)
- India DPDP Act: Extraterritorial scope  -  applies if serving Indian citizens. Phased enforcement through May 2027
- US CLOUD Act: Creates direct conflict with GDPR. US entities can compel data access regardless of physical location
- National AI programs: UAE, Saudi Arabia, Canada treating sovereign AI as strategic national asset. Require certifiable proof that "every bit stays in-country"

**Trigger signals in research:**
- GAIA-X membership or compliance language
- EU data residency positioning on the website or pitch
- Government or defense contracts referenced publicly
- "Sovereign cloud" used in their own marketing
- Regulated-industry customer base (pharma, automotive, financial services, healthcare)

**Their pain:**
- Data sovereignty isn't just about where GPUs sit  -  it's about where packets TRAVEL. BGP could route training data from London to Amsterdam through New York (CLOUD Act violation) or Singapore (non-GDPR). No way to know, prove compliance, or pass audit
- BGP doesn't understand jurisdictions. It routes to cheapest path, ignoring regulatory boundaries
- Cross-border connectivity breaks sovereignty. When a German sovereign cloud needs to connect to a French sovereign cloud, how do they ensure the path stays within EU?

**What MaiaEdge delivers:**
- Policy-based sovereign routing: Define "traffic MUST stay within EU" or "India-only paths." PCE enforces jurisdictional constraints programmatically. BGP can't override it
- In-country PCE deployment: The control plane itself can run on YOUR sovereign cloud (AWS GovCloud equivalent, Azure Government)  -  routing decisions never leave jurisdiction
- Audit trail: Every hop logged with timestamp, carrier, geographic location, latency. Hand this to regulators when EDPB asks "prove this training data never left EU"
- Cross-border connectivity with policy preservation: London → Paris path needed? PCE computes route that stays within GDPR jurisdiction (e.g., Germany → euNetworks Brussels → Paris). No US/Asia hops

**The reusable framing:** The compute side of sovereign AI scales (multi-tenant clusters, orchestration, software). The connectivity side doesn't. Each new enterprise customer is a manual provisioning project across different carriers. Every hop logged, every path controlled is how MaiaEdge closes that gap at the network layer, not just the compute layer.

**Walk-away knowing:** "MaiaEdge provides cryptographic proof that AI training traffic NEVER left UK/EU/India boundaries  -  even when packets transit three carriers to reach the cloud."

**Opening conversation:**
- "When you tell enterprise customers or government agencies that their data stays within [UK/EU/India], how do you prove that IN TRANSIT  -  not just at rest?"
- "BGP routes to the cheapest path. If a packet goes London → Amsterdam, can you guarantee it didn't touch a US carrier subject to the CLOUD Act?"
- "When GDPR auditors ask you to demonstrate data path control, what documentation do you provide? Do you have hop-by-hop logs with jurisdictional metadata?"
- "The compute is multi-tenant but the connectivity isn't. Every new enterprise customer is a different carrier, a different provisioning project. That doesn't scale the way the platform does."
- "Every enterprise customer you serve needs deterministic paths with provable data sovereignty. Today each one is a custom connectivity project. At a handful of customers that's friction; across the enterprise ramp it's a ceiling."

**When NOT to use the sovereign angle:**
- **US neoclouds.** Drop sovereignty. Swap to deterministic paths and egress savings (2c/GB vs 9c/GB). "Every hop logged, every path controlled" still works as a value bridge. "Compute is multi-tenant but connectivity isn't" still works as the opener. The scaling framing still works: "the connectivity approach that worked at 5 facilities breaks at 30."
- **Tier 1 carriers operating their own sovereign AI factory on their own backbone.** They already own the path. The MaiaEdge fit is thin. Research: if the company is a Tier 1 carrier (Deutsche Telekom, Orange, BT, KDDI, NTT) with a single-site AI cloud product, don't force-fit sovereign AI messaging. Look for distributed neocloud prospects instead.

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
| "How do you handle connectivity between GPU clusters in different facilities?" | "It's painful  -  each facility is different, takes weeks" | "We have a dedicated network team handling it well" |
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
| **"We're focused on GPU infrastructure, not networking"** | That's exactly why. You shouldn't have to become network experts. MaiaEdge gives your team the ability to see why inference is slow across facilities  -  and provision deterministic paths in minutes without routing complexity. Focus on inference, not interconnects. |
| **"Our colo partners handle connectivity"** | Do they deliver deterministic paths with end-to-end visibility? Or best-effort cross-connects? Inference performance depends on network predictability. If you're debugging latency issues, the network is probably the variable you can't see. |
| **"We're building our own network team"** | Building a network team to manage multi-carrier complexity is expensive and slow. MaiaEdge gives you the capability without the headcount. Your team provisions paths; we handle the protocol complexity. |
| **"Each facility is different  -  how does this work?"** | That's exactly what MaiaEdge does. PBCs at each location, unified under one control plane. Doesn't matter if it's Aligned in Dallas or Cologix in Columbus  -  same deterministic paths, same visibility, same provisioning speed. |
| **"We don't have this problem yet"** | You do  -  you just can't see it yet. Inference latency variance is invisible without cross-facility observability. Once you can see the network between your GPU clusters, you'll find the variance that's been there all along. |
| **"Who are you?"** | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper). Two exits, $2.5B+ combined. We built carrier infrastructure that network operators deploy. |

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Cross-Facility Observability** | See why inference is slow. Hop-by-hop visibility across paths between GPU clusters in different colo facilities. The first thing they need. |
| **Distributed Inference Fabric** | Deterministic paths between GPU clusters across multiple colo facilities for consistent inference performance. |
| **Rapid Facility Onboarding** | New facility connectivity in minutes instead of weeks as neocloud scales from 3 to 30+ locations. |
| **Sovereign AI Delivery** | Unified fabric across all locations with sovereign routing  -  customer workloads get provably private paths regardless of underlying carriers. |
| **Cloud On-Ramp Acceleration** | Private paths to AWS/Azure/GCP for RAG architectures requiring multi-cloud data retrieval. Layer 2 of the neocloud pain hierarchy. |
| **Multi-Tenant AI Infrastructure** | Serve multiple customers from the same infrastructure with isolated, private paths per customer. Instant on-ramp for new customers without dedicated hardware per site. |

---

## Account Tiering

| Tier | Criteria |
|------|----------|
| **Tier 1** | 5+ facilities, publicly announced GPU capacity >100MW, rapid expansion trajectory |
| **Tier 2** | 2–4 facilities, growing, $50M+ revenue or significant funding |
| **Tier 3** | Early-stage, single facility expanding to second |

---

## Expansion Path

Land conversation depends on maturity (see "Neocloud Angle by Maturity" section below). Default expansion sequence:

**Land (in-pain-now variant):** Cross-facility observability ("see why you're slow") when research shows latency-debugging pain
**Land (scaling-wall variant):** Instant customer on-ramp when research shows hyperscaler-heavy mix + enterprise growth plans
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
- **Zach Smith** (CEO)  -  Former CEO of Packet (acquired by Equinix). Direct relationships with Together.ai, Inference.net, RunPod, Modal, Groq. Board member at Koya (now Mistral)
- **Brett Mertens** (BD)  -  Primary source of neocloud pain articulation
- **Drew Raines**  -  Technical lead
- **Shelby Lindsey**  -  Incoming backbone lead (ex-Equinix)
- **Manish Singh**  -  Engineering

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
Track Crunchbase/PitchBook for rounds tagged 'GPU cloud', 'AI infrastructure', 'inference platform'. Any Series A+ is a potential prospect. Recent examples: Nscale ($1.1B), Nebius ($1.7B total), Lambda ($1.5B+).

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

**Company Names:** Lambda Labs, Crusoe Energy, Voltage Park, Together AI, Anyscale, RunPod, Paperspace

---

## One-Liner Quick Reference

| Situation | One-Liner |
|-----------|-----------|
| Opening pitch (default) | "Connecting distributed AI. Deterministic, private, instant." |
| Opening (in-pain-now variant) | "See why you're slow. Then fix it." |
| Opening (scaling-wall variant) | "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." |
| They say "we're not a networking company" | "Exactly. You shouldn't have to be." |
| They say "connectivity just works" | "It does, for the hyperscalers bringing their own. The enterprise customers behind them don't." |
| They're scaling fast | "Every new facility doesn't have to be a connectivity project. Every enterprise customer doesn't have to be either." |
| They mention carrier complexity | "One control plane. All facilities. All carriers. Minutes, not weeks." |
| They ask about competitors | "Nobody else gives you hop-by-hop visibility across facilities you don't own networks between." |

---

## Industry Landscape (2025-2026)

### GPU Economics Shifting Fast
H100 pricing cratered 64-75%: cloud rental from $8-10/hr (Q4 2024) to $2.99/hr (Q1 2026). AWS H100 spot prices dropped up to 88%. NVIDIA Blackwell sold out through mid-2026, but TSMC expanding CoWoS capacity to 120-130K wafers/month by late 2026 (up from 75K)  -  supply bottleneck should ease H2 2026. Midjourney moved from NVIDIA to Google TPU v6e, cutting inference spend from ~$2.1M to under $700K/month  -  a cautionary tale for GPU-only neoclouds.

### Inference Overtaking Training
Inference now represents 55% of AI infrastructure spending (early 2026), up from 33% in 2023. Projected 75-80% by 2030. Inference-optimized ASICs generated $20B+ in 2025 revenue. NVIDIA acquired Groq for ~$20B (Dec 2025), integrating LPU into Vera Rubin. Training tolerates retries. Inference doesn't  -  network quality directly impacts customer experience.

### The GPU Debt Wall
Industry-wide: $870B in new AI infrastructure debt backed by assets with 3-4 year practical useful lives. Individual neoclouds carry tens of billions in debt with interest expenses consuming a significant chunk of revenue. Must keep GPUs utilized to service debt  -  network downtime = checkpoints = lost revenue. This is existential pressure.

### Sovereign AI Goes Mainstream
$750B projected global AI infrastructure investment for 2026. Gartner forecasts $80B in sovereign AI cloud IaaS spend. Nscale raised $2B at $14.6B valuation (largest European AI infra play). APAC showing fastest growth: India, South Korea, Indonesia mandating local clouds for critical data.

### Industry Unit Economics
BMaaS gross margins are 55-65% before depreciation, but net profit margins drop to 14-16% after labor, power, and depreciation. Depreciation alone can consume 40-50% of revenue given 3-4 year GPU useful lives. Most neoclouds are pre-profit or barely profitable  -  the gap between gross margin and net margin is where the network and infrastructure costs hide.

### Allocation Is the Real Constraint
The industry narrative frames GPU supply as "easing H2 2026" because TSMC is ramping CoWoS advanced packaging capacity to 120-130K wafers/month. True, but misleading for neocloud operators on the ground. NVIDIA Blackwell sold out through mid-2026. B200/GB200 allocation is tightly managed  -  most neoclouds get what NVIDIA decides to allocate, not what they order. This is why every hour of GPU utilization is existential, not rhetorical. When 128 H100s run at 35% utilization because of 2ms inter-AZ latency, that isn't a networking nuisance  -  it's the equivalent of NVIDIA allocating you 45 GPUs you aren't using. Deterministic paths aren't a networking purchase. They're how you extract revenue from allocation you fought to get.

### Margin Compression Is Explicit Now
H100 cloud rental dropped from $8-10/hr (Q4 2024) to $2.99/hr (Q1 2026)  -  a 64-75% collapse. AWS H100 spot prices fell up to 88%. That isn't pricing data, it's margin evaporation. BMaaS gross margins are 55-65% before depreciation, 14-16% net after labor, power, and depreciation consumes 40-50% of revenue at 3-4 year GPU useful lives. The gap between gross and net is where network-driven inefficiency hides. Inter-AZ latency (128 H100s at 35% across 3 AZs), recompute tax ($4,800/GPU/month rebuilding KV cache on 128K context Llama-3 70B), and egress bleeding ($0.05-$0.09/GB public vs. $0.02/GB Direct Connect) are now P&L items the CFO sees, not infrastructure footnotes. Boards are asking the CTO to quantify them.

### Enterprise Long-Tail Is the Scaling Wall
Scale neoclouds with hyperscaler-heavy customer mixes are often not in pain today. Hyperscalers bring their own connectivity  -  Direct Connect, ExpressRoute, private fiber  -  so the neocloud rarely has to provision anything. That's the trap. Growth plans depend on mid-market enterprise customers, and those customers don't bring their own anything. Every enterprise onboarding becomes a manual connectivity project: different carrier, different topology, different timeline. At a handful it's friction. As the enterprise ramp accelerates it becomes a structural ceiling on growth. This is not a latency-debugging conversation. It's a scaling-model conversation  -  the hyperscaler contracts that got them here didn't need a network team, the enterprise customers coming behind them will. Research separates the "in pain now" neocloud (debugging latency variance across facilities) from the "approaching the wall" neocloud (hyperscaler-heavy mix, growth strategy shifting toward enterprise long-tail). Same value props. Different door.

### Neocloud vs. Colo: Where the Line Blurs
Modular edge operators and crypto-to-AI pivots straddle segment boundaries. Classification drives vocabulary, messaging, and angle  -  so getting it right matters. Key question: are they selling compute, or selling space?
- **Sells compute** (GPUaaS, inference-as-a-service) → Neocloud. Example: Duos Edge AI deploys modular edge pods and sells GPU capacity (2,304 NVIDIA GPUs). They ARE the customer for connectivity. Use neocloud messaging.
- **Sells space/power/cooling to GPU tenants** → AI Colo. Example: Nodiac deploys modular containerized DCs at renewable energy sites and hosts GPU tenants (500+ sites pipeline, 800+ MW). Their GPU tenants are separate neocloud prospects. Use colo messaging.
- **Crypto-to-AI split**: IREN leasing power capacity to Microsoft = AI colo (landlord model). A former miner launching their own GPUaaS product = neocloud. Research the revenue model, not the origin story.
- **Does both**: Lead with primary revenue model. Research the company's site and investor materials to see how they describe themselves. If unclear, the colo angle is usually safer  -  it positions MaiaEdge as an enabler, not a dependency.

### Agentic Latency Compounding
Agentic workflows don't run on one inference call. They chain 10+ sequential calls, each potentially crossing different carrier networks. Montauk Capital's April 2026 thesis: each hop adds 200ms to 2 seconds of delay. Across a ten-step workflow, that compounds into tens of seconds of cumulative lag. For autonomous systems managing physical infrastructure, financial decisions, or human safety, that's operationally unacceptable and contractually fatal. Training tolerates retries. Inference doesn't. Agentic workflows tolerate neither. Deterministic paths across all hops are the difference between "our agents work" and "our agents fail at the 7th hop for reasons we can't diagnose." This is the new framing for the DETERMINISTIC pillar.

### Network Architecture Reality
Two-network architecture: front-end (standard Ethernet for management/user access) + back-end (lossless Ethernet or InfiniBand for GPU-to-GPU synchronization). The largest neoclouds are building dedicated WAN backbones for inter-facility traffic, but most are flying blind with no path visibility across carriers.

Inter-AZ latency is catastrophic for training: 2ms kills performance. Real-world example: 128 H100s running at only 35% utilization when spread across three AZs. Standard Ethernet routing across AZs destroys GPU utilization.

InfiniBand dominates training today but Ethernet projected to win long-term (91% of AI workloads on Ethernet by 2029). RoCEv2 enables RDMA on standard Ethernet. NCCL synchronous All-Reduce means the entire cluster waits for the slowest GPU  -  at $4/hr per GPU, the straggler problem burns cash fast.

Storage recognized as the "$35 billion blind spot" silently taxing every GPU. Data egress is a hidden cost  -  checkpoint movement between facilities can wipe out compute savings when egress fees aren't accounted for.

### What the C-Suite Is Focused On
- GPU utilization as THE metric that determines profitability
- Inference revenue mix and pricing strategy as H100 rates collapse
- Debt servicing  -  keeping clusters running to cover $870B in industry debt
- Multi-site networking without building a networking team
- Observability into why inference performance varies by facility
- Sovereign AI contracts and geographic expansion

---

## Their Information Diet

### What They Read
- The Information, Semianalysis (Dylan Patel), Data Center Dynamics, Lightwave Online

### Key Industry Voices
- Dylan Patel (Semianalysis)  -  GPU economics and supply chain
- Analysts at Omdia, Dell'Oro Group  -  market sizing and forecasts

### Where They Gather
- NVIDIA GTC (March, San Jose), OCP Global Summit, Hot Chips, SC/Supercomputing, AI Infrastructure events

---

## Competitive Dynamics (Their Market)

These are who NEOCLOUDS compete against  -  not MaiaEdge competitors.

### Hyperscaler GPU Instances
AWS, Azure, GCP offering GPU instances with deep ecosystem integration (SageMaker, Vertex AI, Bedrock). Hyperscalers building custom silicon (Google TPUs, AWS Trainium/Inferentia, Microsoft Maia). Name recognition and ecosystem lock-in threaten neocloud momentum  -  but neoclouds growing faster (triple-digit revenue vs hyperscalers' ~20% YoY).

### Each Other
GPU-as-a-Service market: $3.23B (2023) to $49.84B by 2032 (36% CAGR). As more capacity comes online and H100 prices crater, pricing pressure intensifies. Differentiation shifts from "having GPUs" to infrastructure quality  -  network, storage, observability.

### Custom Silicon
Inference-optimized ASICs (Groq LPU, Google TPU, AWS Inferentia) generated $20B+ in 2025. For inference workloads specifically, NVIDIA CUDA lock-in is weaker than for training. Neoclouds must offer more than raw GPU access.

---

## MaiaEdge Relevance Bridges

> **⚠️ Internal angle-selection guide.** The specific proof points referenced below (status-page incident patterns, debt-wall size, recompute-tax dollar figures, egress dollar figures, allocation-constraint mechanics) are **internal triggers for picking which angle to lead with**. They are NOT customer-facing talking points. Do not cite specific incident counts, dollar figures, or debt numbers in cold outreach, LinkedIn, or discovery calls. Use them to determine which relevance bridge fits the account, then write the outreach in segment-appropriate vocabulary (see Segment Vocabulary Lock).

How current industry trends connect to problems MaiaEdge solves. Use these across the full sales motion  -  outreach, discovery, business cases, proposals, closing.

| Their Trend | Their Pain | MaiaEdge Angle |
|---|---|---|
| H100 pricing crashed 64-75% | Unit economics under pressure  -  must maximize GPU utilization to survive margin compression | "GPUs are cheaper. Utilization is what matters now. 2ms of network latency = 65% wasted GPU capacity." |
| Inference overtaking training (55% of spend) | Inference is latency-sensitive and distributed  -  network quality directly impacts customer experience | "Training tolerates retries. Inference doesn't. Your customers feel every jitter spike." |
| GPU Debt Wall ($870B industry-wide) | Must keep GPUs utilized to service debt -- network downtime = checkpoints = lost revenue | "Every network interruption forces a checkpoint rollback. Downtime isn't just costly when debt is mounting -- it's existential." |
| Inter-AZ latency killing utilization | 128 H100s at 35% utilization across 3 AZs  -  network is the bottleneck, not compute | "Your GPUs aren't slow. Your network between facilities is. MaiaEdge gives you deterministic paths so clusters perform." |
| "Compute companies that accidentally became networking companies" | No network team, no WAN visibility, no path control  -  flying blind | "You didn't sign up to be a networking company. MaiaEdge gives you observability and path control without building a NOC." |
| Storage + egress as hidden costs | Data movement between sites eating into margins | "Egress fees can wipe out compute savings overnight. Deterministic paths reduce recompute and checkpoint movement." |
| NVIDIA B200/GB200 allocation scarcity + CoWoS 60-week lead times | Every hour of utilization loss is equivalent to NVIDIA allocating you GPUs you aren't using | "You fought for your allocation. Your network is giving it back. 2ms of inter-AZ latency at 128 GPUs is 45 GPUs you're paying for and not using." |
| Agentic AI compounding latency across 10+ hops (Montauk April 2026) | Agent failures at hop 7 for reasons nobody can diagnose  -  contractually fatal for autonomous workloads | "Training tolerates retries. Inference doesn't. Agents tolerate neither. Best-effort routing compounds into tens of seconds of lag across ten hops. Deterministic paths eliminate the compounding." |
| Margin compression explicit (gross 55-65%, net 14-16%) | Network inefficiency is now a P&L item the CFO sees, not an infrastructure footnote | "Your CFO is about to ask where the gap between gross and net margin is going. Inter-AZ latency, recompute tax, and egress bleeding are where it hides." |
| Enterprise long-tail pulling scale neoclouds past hyperscaler-bundled connectivity | The hyperscaler contracts that got them here didn't need a network team. The enterprise customers coming behind them will. | "Hyperscalers bring their own connectivity. The mid-market customers driving your next phase of growth don't. Every enterprise onboarding is a manual connectivity project, and the ramp doesn't absorb that friction." |
| Mid-market AI buyer expects instant onboarding | Multi-week carrier coordination is the close-rate cap on enterprise deals | "When a financial services firm asks how fast they can get a private path to your inference endpoint, your answer is your close rate. Weeks loses to days." |

---

## Insider Language Bank

Things neocloud executives say internally  -  use these to demonstrate you understand their world.

### Board Meeting Language
- "H100 spot rates dropped 75% in 12 months. What does our unit economics look like at $2.99/hr?"
- "Inference is 55% of AI spend and growing. Our back-end fabric was built for training."
- "128 H100s running at 35% utilization because of 2ms inter-AZ latency"
- "Every checkpoint rollback is money burning"
- "Storage is the $35 billion blind spot"
- "We're a compute company that accidentally became a networking company"
- "The top neoclouds are building dedicated WAN backbones. What are we running?"
- "Our network team is two people, neither are network engineers"
- "Allocation is the only thing that matters. The network is taking allocation back from us."
- "Agentic workloads compound latency across hops  -  ten best-effort hops becomes seconds of lag"
- "Our CFO wants to know where gross-to-net margin is going. Egress, recompute, and inter-AZ latency."
- "Hyperscaler revenue hasn't required a network team  -  they bring their own connectivity"
- "The growth plan says we serve mid-market enterprise next  -  those customers don't bring their own anything"
- "Every enterprise onboarding is a manual provisioning project. The ramp doesn't absorb that."
- "The connectivity approach that worked at 5 facilities breaks at 30."
- "The compute is multi-tenant but the connectivity isn't."

### KPIs They Report
GPU utilization rate, cost per GPU-hour, inference latency (TTFT + tokens/sec), training throughput (TFLOPS), power per rack (kW), total backlog ($), revenue per GPU, depreciation as % of revenue, egress costs, checkpoint frequency, inter-facility latency

### Technical Terms to Know
CoWoS, BMaaS, straggler GPUs, stalled collectives, SHARP (halves All-Reduce traversals), SHIELD (5000x faster link failure recovery), BlueField DPUs, Metro Latency Monitor, front-end/back-end network, lossless fabric, non-blocking architecture, GPU-hours, DGX/HGX/SXM, NVLink/NVSwitch, All-Reduce, east-west traffic, data locality, NVMe caching, spot pricing, reserved instances, HBM3e, GPU depreciation schedule

---

*Cross-references: Messaging Framework V4 (Section 3.3 Neoclouds), ICP Sales Playbook, AI Market Positioning Guide, Cloud On-Ramp Business Case*

*Last updated: April 2026 (trend refresh: allocation as real constraint, margin compression explicit, agentic latency compounding, enterprise long-tail scaling wall, neocloud/colo disambiguation)*
