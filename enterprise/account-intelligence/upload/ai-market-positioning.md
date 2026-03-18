# MaiaEdge AI Market Positioning & Messaging Guide

> **Merged Document:** This document now includes content from Marketing's MaiaEdge_Inference_Positioning.md (the "north star" problem statement) integrated with the comprehensive AI market strategy.

## The Inference Problem Statement

AI inference is turning milliseconds into money. Token-by-token generation is sequential, latency-sensitive, and intolerant of jitter. The network becomes part of the compute loop.

**What MaiaEdge delivers for AI inference:**
- Deterministic private Ethernet paths engineered for AI inference
- Known hop count, known latency characteristics, controlled failure domains
- End-to-end visibility across paths that traverse multiple networks

**What MaiaEdge does NOT do for inference:**
- Does not run inference workloads
- Does not store or process AI models
- Does not replace GPU infrastructure
- Does not provide compute or storage

MaiaEdge is the network layer that makes distributed inference predictable. The path between GPU clusters is either deterministic or it isn't. Best-effort routing introduces variance that compounds per token. MaiaEdge eliminates that variance.

**Neocloud Note:** For neocloud prospects, lead with observability ("see why you're slow"), NOT deterministic paths. The inference problem statement above is for AI-focused colocation operators and network operators. Neoclouds experience the same problem but don't frame it as a networking issue. See Messaging Framework V4, Section 3.3 for neocloud-specific messaging hierarchy.



**Private paths. Any network. Instantly.**

February 2026 | MaiaEdge Internal — Confidential

---

## Executive Summary

Two structural shifts in enterprise and AI infrastructure are converging to create a significant near-term opportunity for MaiaEdge:

1. **AI inference is overtaking training as the dominant workload.** McKinsey projects inference will represent 70% of total AI demand by 2029, growing at 35% CAGR through 2030. This shift favors distributed, user-proximate 5–10MW facilities over centralized mega-campuses — facilities that need the exact private connectivity fabric MaiaEdge delivers.

2. **Enterprises are repatriating AI workloads from public cloud into hybrid infrastructure.** 87% of enterprises plan to repatriate workloads in the next 12–24 months. AI economics, data sovereignty regulation (EU AI Act enforcement August 2026), and security concerns around agentic AI systems are accelerating the shift. Every repatriated workload needs private, secure connectivity between facilities — and provisioning that connectivity is the immediate bottleneck.

These trends don't require a new product or a new customer segment. The pain points inference operators and repatriating enterprises face are identical to those MaiaEdge already solves: 60–90 day provisioning timelines, multi-carrier visibility loss, inability to federate quickly, and sovereignty concerns. What changes is how we position and message — layering AI-specific context onto our existing segment framework to capture urgency and relevance.

At its core, MaiaEdge lets any operator do what Megaport and Equinix do: automated interconnection and private path provisioning so any provider can deliver private paths, to any network, anywhere. As carriers, providers, and colos increasingly deploy MaiaEdge devices at their edges, it creates a new private internet ecosystem — one built on sovereign routing, operator ownership, and instant provisioning.

### Key Terminology: The Sovereignty Stack

These terms are central to our AI-forward positioning. Own them in every conversation.

| Term | Definition | MaiaEdge Relevance |
|------|-----------|-------------------|
| **Private Cloud** | A cloud computing environment dedicated exclusively to a single organization, offering enhanced security, privacy, and control. | MaiaEdge connects private cloud infrastructure to other sites, clouds, and partners via private paths. |
| **Sovereign Cloud** | A cloud computing service designed to store and process data in compliance with the specific laws, regulations, and jurisdictional requirements of a particular country or region. | MaiaEdge enables the connectivity layer that makes sovereign cloud architectures work across distributed infrastructure. |
| **Data Sovereignty** | The ability of an organization to independently control, manage, and monitor its own IT infrastructure and digital operations without unauthorized third-party interference or dependency. | MaiaEdge's operator-owned fabric means no third party controls or has visibility into the customer's data paths. |
| **Sovereign Routing** *(MaiaEdge owns this language)* | Controlling how data travels across networks to ensure it remains within specific geographic, legal, or organizational boundaries. Unlike traditional routing (BGP) that optimizes for speed or cost, sovereign routing prioritizes data residency, privacy, and security by defining specific, trusted paths for traffic. | This is what MaiaEdge delivers — deterministic, policy-driven path selection that can enforce geographic constraints. PCE computes paths that avoid specific regions, countries, or untrusted network segments. |
| **Operational Sovereignty** | The ability of a service provider to maintain independent control over their own network operations, customer relationships, and service delivery without dependency on third-party platforms. | MaiaEdge's "build your own fabric" model ensures operators maintain sovereignty over their business — not just their customers' data. |

---

## Part 1: The AI Infrastructure Landscape

### The Inference Shift

The AI data center market is splitting into two distinct archetypes. Centralized training mega-campuses (Stargate, $500B+) require massive power and tolerate high latency. Inference workloads powering real-time applications — chatbots, fraud detection, autonomous vehicles, recommendation engines — demand sub-10ms response times and cannot be served from remote locations.

The economics reinforce this split. Training is a one-time capital expense; inference is recurring and directly tied to revenue. GPT-4's inference costs are projected at approximately $2.3 billion in 2024 — roughly 15x its training cost. Inference tasks are atomizable and can be distributed across smaller facilities, favoring metro-proximate deployments.

**Key data points:**

| Metric | 2024 | 2025 | 2030 | CAGR |
|--------|------|------|------|------|
| AI Data Center Market | $98.2B | $129.6B | $1.98T | 35.5% |
| AI Inference Market | $106B | ~$113–135B | $253–255B | 19.2% |
| AI Inference Power Demand | — | 20.9 GW | 93.3 GW | 35% |
| GPUaaS (Neocloud) Market | $24B | — | $65B+ | — |

By 2030, inference will represent over 50% of all AI compute and 30–40% of total data center demand. Currently, 58% of AI budgets are allocated to inference workloads.

### The Repatriation Wave

Cloud repatriation has moved from fringe to mainstream, and AI is the primary accelerant.

| Data Point | Source |
|-----------|--------|
| 86% of CIOs plan to repatriate some public cloud workloads | Barclays CIO Survey, 2025 |
| 87% of enterprises plan to repatriate in the next 12–24 months | SiliconANGLE, 2026 |
| 67% of enterprises have already repatriated some workloads | Nutanix/industry survey |
| $823B projected sovereign cloud market by 2032 (up from $154B in 2025) | HPE/Computer Weekly |
| 55% of IT leaders see value in keeping AI closer to own infrastructure | VMware/Broadcom |
| 80% of enterprises expect cloud repatriation of compute/storage | IDC |

Three forces are driving this:

**AI Economics and Compute Costs.** Training and continuous inference pipelines require specialized compute that becomes cost-prohibitive at scale on public cloud. The neocloud cost advantage (66% lower pricing at $1.39/hr vs. $3.67/hr for comparable GPU instances) is pulling demand away from hyperscalers toward specialized providers who then need connectivity solutions. Repatriated AI workloads still need to reach other sites, cloud endpoints, and partners — MaiaEdge provides the private interconnect fabric that makes distributed hybrid AI architecture work.

**Data Sovereignty and Regulatory Pressure.** The EU AI Act becomes fully applicable August 2026 with fines up to 7% of global revenue. The US CLOUD Act creates tension with GDPR. Eighteen US state privacy laws are active. China, India, and Saudi Arabia all mandate local data processing. By 2028, IDC forecasts 60% of organizations with sovereignty requirements will have migrated sensitive workloads to new environments. These enterprises need provably private paths between facilities — paths where they can demonstrate exactly where their data traverses and actively control routing to avoid specific geographic areas.

**AI Security and Shadow AI Exposure.** Employees using AI tools tripled in the past year while data policy violations doubled. 55% of organizations can't isolate AI systems from sensitive network access. 63% can't enforce purpose limitations on AI agents. Enterprises are responding by pulling AI into controlled environments where they own the network layer. MaiaEdge's AES-256-GCM encrypted paths and deterministic routing mean data never traverses uncontrolled infrastructure.

**Important: Not all enterprises need sovereign AI.** The repatriation trend is strongest in specific verticals with regulatory, safety, or compliance drivers: healthcare providers processing patient data under HIPAA/GDPR, energy grids running safety-critical AI, and carriers delivering real-time network slicing (e.g., T-Systems' 5G use case — giving priority to an ambulance over Netflix in real-time). These verticals are the most likely to need sovereign routing and private connectivity between distributed AI workloads. Generic enterprise IT repatriation creates less acute MaiaEdge demand.

### Geographic Distribution

Power constraints are pushing AI infrastructure into secondary markets, creating connectivity demand in new geographies.

**Established AI Markets:**
- Northern Virginia: 665+ operational data centers, 34M MWh annually — but power-constrained (36+ month time-to-power)
- Texas: 429 facilities, efficient permitting — Stargate Phase 1 in Abilene
- Georgia: 162 existing, 285 planned (176% increase)

**Emerging AI Corridors:**
- Dallas-Fort Worth: Lambda Labs, Crusoe, hyperscaler campuses
- Columbus, OH: Lambda Labs, AWS, Intel Chips Act facility
- Atlanta, GA: Lambda Labs, hyperscaler expansion
- Phoenix, AZ: Vantage, QTS, power availability advantage
- Memphis: 4,300% increase in wavelength connectivity (2023–2024)

**Future Tier 1 Markets (McKinsey):** Des Moines, San Antonio, Columbus — offering 12–24 months faster power delivery and up to 70% lower land costs.

**International Sovereign AI Markets:**
- UK: £14+ billion in committed data center projects (Nscale, CoreWeave)
- Singapore: $26+ billion from tech giants, 15% of global NVIDIA revenue
- Japan: ¥10 trillion ($65B) government commitment through 2030
- Middle East: 19.76% CAGR through 2030, Saudi Arabia's $100B Project Transcendence
- 84% of European organizations are using or planning sovereign cloud adoption within 12 months

For MaiaEdge, this geographic diffusion is directly relevant: inference sites in secondary markets need private metro connectivity that traditional Tier 1 players don't prioritize. Regional operators who can offer sovereign routing — controlling exactly where data traverses — win these accounts.

---

## Part 2: Why This Is a MaiaEdge Opportunity

### Pain Point Alignment

The pain points inference operators and repatriating enterprises face are identical to those we already solve for traditional service providers:

| Inference / Repatriation Pain Point | Traditional SP Pain Point | MaiaEdge Solution |
|-------------------------------------|--------------------------|-------------------|
| 60–90 day provisioning timelines | 60–90 day NNI provisioning | Instant provisioning (minutes) |
| Multi-cloud connectivity complexity | Multi-carrier visibility loss | Unified fabric, end-to-end visibility |
| Latency-sensitive workloads (sub-10ms) | Deterministic path requirements | WAN-Ethernet deterministic routing |
| Need to federate with partners fast | Federation takes 90+ days | Instant federation via PBCs |
| Ownership/sovereignty concerns | Losing customers to Megaport | You own the fabric, customer, revenue |
| AI security requires encrypted paths | — | AES-256-GCM on every PBC, infrastructure-layer encryption |
| Must prove AND control where data traverses | — | Hop-by-hop telemetry + sovereign routing: provision paths that avoid specific locations |
| Complexity of multi-carrier coordination | — | Single fabric across all boundaries — owned, leased, and partner infrastructure unified |

### Technical Capabilities That Map to AI Requirements

| MaiaEdge Spec | Capability | Why It Matters for AI Infrastructure |
|---------------|-----------|--------------------------------------|
| <2 μs latency overhead | Near-zero processing delay | Inference apps require sub-10ms response; PBC adds negligible overhead vs. traditional routing (10–100+ μs) |
| Dual 100GbE throughput | High-bandwidth transport | GPU clusters generate massive data flows; 100G handles inference traffic without bottlenecks |
| Line-rate AES-256-GCM IPsec | Encrypted at full speed | AI workloads contain proprietary model weights and sensitive data; encryption without performance penalty |
| Deterministic path engineering | PCE real-time route calculation with geographic constraints | Inference SLAs require predictable latency; PCE computes optimal paths based on latency, utilization, policy — AND can enforce sovereign routing to avoid specific regions |
| Hop-by-hop telemetry | Jitter, loss, latency visibility + compliance proof | 33% of AI/ML latency is network-related; visibility identifies bottlenecks AND proves data path compliance for regulatory purposes |
| Transport-agnostic fabric | Mix fiber + DIA in unified fabric | AI infra builds fast — start with DIA for instant connectivity, add fiber when available, keep DIA for failover |
| API integrations (Equinix, Megaport) | Native cloud on-ramp | RAG architectures require multi-cloud access; direct AWS/Azure connectivity without routing complexity |
| 1RU form factor | Minimal rack space | AI racks run 30–150kW density; every RU matters; PBC deploys in meet-me room, not GPU rack space |

### Why MaiaEdge Wins This Moment

**Sovereignty by design, not by retrofit.** MaiaEdge was built from the ground up around operator sovereignty. The customer owns the relationship, the brand, and the network. But sovereignty is dual: MaiaEdge enables providers to maintain their own operational sovereignty when working with multiple partners or NaaS fabrics AND enables sovereignty for their customers — provisioning paths that avoid geographic areas (e.g., a healthcare provider in France whose data must never leave the country). In an era where enterprises demand infrastructure-level proof of data control, this dual sovereignty architecture is a fundamental differentiator.

**Path visibility AND control across the middle mile.** Enterprises repatriating for sovereignty reasons need to prove where their data goes — and control it. MaiaEdge's PCE provides hop-by-hop telemetry showing the exact physical path, not just logical endpoints. But it goes beyond visibility: operators can actively provision paths that avoid specific geographic regions, carriers, or untrusted network segments. This isn't just observability — it's sovereign routing for compliance purposes. Most networking vendors can't offer either capability, let alone both.

**Speed and complexity elimination.** The biggest pain points in hybrid architecture are connectivity provisioning speed AND operational complexity. MPLS takes 6–10 weeks and requires extensive multi-carrier coordination. MaiaEdge provisions in minutes with a single fabric that unifies owned, leased, and partner infrastructure. When an enterprise decides to repatriate, neither speed nor complexity should be the bottleneck.

**Encryption at the infrastructure layer.** AES-256-GCM on every PBC means encryption is baked into the path itself, not bolted on as a VPN overlay. This directly addresses the security concerns driving repatriation.

**The private internet ecosystem.** As carriers, providers, and colos increasingly deploy MaiaEdge PBCs at their edges, it creates something larger than individual deployments — a new private internet ecosystem where any provider can deliver private paths, to any network, anywhere, with automated interconnection and sovereign routing. This is how the private internet gets built: operator by operator, edge by edge.

### Competitive Landscape

The connectivity provider market shows clear stratification in AI positioning:

**Tier 1 — Aggressive AI Positioning:**
- **Equinix:** Distributed AI Infrastructure platform, Fabric Intelligence layer (launching Q1 2026), 2,000+ AI partners
- **Lumen:** $5B in AI-related sales booked, $3B+ pipeline, multi-year Microsoft PCF partnership, CEO explicitly targeting inference phase
- **Zayo:** $4B+ in AI-related business, 5,000+ new long-haul route miles, AI Infrastructure Blueprint with Equinix

**Tier 2 — Moderate Positioning:**
- **Megaport:** Acquired Latitude.sh ($115M) for AI compute convergence, launching Megaport AI Exchange (AIx)
- **PacketFabric:** Markets Virtual Cloud Router as "built for AI" but no explicit AI partnerships or inference products

**Tier 3 — Limited/No Positioning:**
- **Console Connect:** General NaaS only, no inference offerings
- **Cogent:** Opportunistic hyperscaler interest, no AI products
- **GTT:** AI positioned for internal operations, not connectivity
- **Crown Castle:** Actively exiting — selling 100,000+ metro route miles to Zayo

**The gap:** There is clear white space between Tier 1 leaders making multi-billion-dollar commitments and mid-tier providers with generic NaaS messaging. MaiaEdge positions as the infrastructure that lets any operator build Equinix-like fabric capabilities — fast, deterministic, secure private interconnection — without the development work or capital investment. Premium services without the development burden.

**Against Lumen PCF specifically:** Our existing positioning applies perfectly for the AI context. GPU cloud providers and inference-focused colos want to own their customer relationships and connectivity margins — they don't want to become dependent on Lumen for their network fabric. *"Lumen builds their empire; MaiaEdge empowers you to build yours."*

---

## Part 3: Impact on Customer Segments

### Recommendation: Enhance Existing Segments, Don't Create New Ones

After analysis, the AI inference and repatriation trends do **not** require a new customer segment. Instead, they require AI-specific messaging tracks and filtering criteria layered onto our existing segmentation framework. Here's why:

1. **Infrastructure model alignment:** GPU cloud providers (CoreWeave, Lambda Labs) lease from colocation operators. The colo is our customer, not the GPU cloud tenant.
2. **Pain points are identical:** Colos serving AI tenants have the same fundamental pain as colos serving enterprise tenants — competing with Equinix/Megaport, provisioning delays, inability to offer fabric-like services.
3. **Decision-makers are the same:** VP Network, VP Infrastructure, CTO at colocation operators. Same personas, same discovery questions, same qualification criteria.
4. **One exception — Neoclouds:** GPU cloud providers (CoreWeave, Lambda Labs, Crusoe, Voltage Park) are classified as their own segment because they ARE the end customer deploying distributed GPU clusters, not a colo serving someone else. Neoclouds are the backbone of Sovereign AI — they need to create a unified fabric across their locations, even if there are multiple different regional carriers in between.

### Where AI Messaging Applies vs. Standard Messaging

| AI Messaging Applies When... | Use Standard Messaging When... |
|------------------------------|-------------------------------|
| GPU cloud providers (CoreWeave, Lambda Labs, Crusoe, Voltage Park) are confirmed tenants | Tenant base is primarily traditional enterprise (non-regulated) |
| Facility has liquid cooling or high-density rack support (30kW+) | Standard power density (5–15kW per rack) |
| Company markets "AI-ready," "GPU cloud," or "AI infrastructure" services | Company focuses on general colo/connectivity |
| Located in emerging AI corridor (DFW, Columbus, Atlanta, Chicago, Phoenix) | Located in traditional markets without AI buildout |
| Recent announcements about power upgrades or capacity expansion for AI | No AI-related news or infrastructure investments |
| Fiber operator with infrastructure near announced AI data center builds (dark or lit) | Fiber operator in regions without AI demand |
| Enterprise customers in healthcare, energy, or carriers deploying inference workloads | Enterprise customers with standard WAN needs |

### AI-Focused Account Identification Signals

Use these observable signals in enrichment workflows to flag accounts for AI-specific messaging:

| Signal Type | What to Look For | Data Sources |
|-------------|-----------------|--------------|
| **Tenant Signals** | CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI as tenants; GPU cloud partnership announcements | Press releases, website tenant pages, news alerts |
| **Infrastructure Signals** | Liquid cooling capabilities; high-density racks (30kW+); power upgrades; GPU cluster support | Website, Data Center Map, press releases |
| **Service Signals** | AI/ML services listed; GPU-as-a-Service; AI cloud on-ramp; inference hosting; "AI-ready" positioning | Website services page, product announcements |
| **Geographic Signals** | Presence in emerging AI corridors: DFW, Phoenix, Columbus, Atlanta, Chicago; secondary markets with power availability | Facility locations, expansion announcements |
| **Hiring Signals** | Job postings for AI infrastructure roles; GPU cluster engineers; ML platform specialists | LinkedIn, company careers page |
| **Financial Signals** | Recent funding rounds mentioning AI; expansion CapEx announcements; GPU procurement deals | Crunchbase, press releases, SEC filings |
| **Repatriation/Sovereignty Signals** | Sovereign cloud adoption; hybrid infrastructure investments; on-prem AI compute announcements; regulatory compliance positioning | Press releases, analyst reports, RFPs |
| **Vertical Signals** | Healthcare data center tenants (HIPAA); energy/grid customers; carrier 5G slicing initiatives | Industry publications, tenant directories |

### Priority Accounts to Flag

**Tier 1 — Confirmed GPU Cloud Tenant Relationships:**

| Company | GPU Cloud Tenant(s) | Details |
|---------|---------------------|---------|
| Aligned Data Centers | Lambda Labs | Multi-facility partnership for Lambda's 2GW+ buildout; DeltaFlow liquid cooling (300kW/rack) |
| Cologix | Lambda Labs, CoreWeave | Columbus, Chicago, Dallas presence; Lambda 320MW+ committed |
| EdgeConneX | Lambda Labs | Distributed edge portfolio; Lambda partnership in multiple markets |
| QTS Data Centers | Hyperscaler AI workloads | Major hyperscaler AI deployments; high-density rack support; strong in DFW, Phoenix |
| Vantage Data Centers | Multiple GPU cloud providers | Hyperscale focus; Phoenix, Dallas, Atlanta campuses |
| Stack Infrastructure | AI infrastructure buildouts | Aggressive expansion in AI corridors |

**Tier 2 — AI-Ready Infrastructure (No Confirmed GPU Cloud Tenant):**
- Digital Realty — 150kW per rack support, "AI inference in major metros" positioning
- DataBank — Edge-focused portfolio, expanding in secondary AI markets
- T5 Data Centers — High-density focus, Atlanta and Dallas presence
- Flexential — Hybrid IT positioning, GPU-as-a-Service offerings
- Stream Data Centers — Texas market focus with power availability

**Tier 3 — Fiber Operators in AI Corridors:**
- Regional operators in Dallas-Fort Worth, Columbus OH, Atlanta GA, Phoenix AZ (dark or lit fiber assets)
- Crown Castle fiber acquisition targets — Zayo purchasing 100,000+ metro route miles creates market disruption and potential customer displacement

---

## Part 4: Segment-Specific AI Messaging

### Colocation Operators — AI Infrastructure Track

**Profile:** Data center operators with GPU cloud tenants or AI-ready infrastructure (liquid cooling, high-density racks, power capacity).

**Primary Pain Point:** "We have GPU cloud tenants demanding instant cross-connects to multiple clouds with sub-10ms latency guarantees, and our current process takes weeks. We're losing deals to Equinix."

**The Real Value:** MaiaEdge enables colos to become an Equinix-like fabric — offering fast, deterministic, secure private interconnection as premium services without the development work. This is the path from colocation to interconnection without giving up control.

**Value Proposition:** "Offer your AI tenants what they can't get from hyperscalers: instant multi-cloud fabric with deterministic latency (<2μs overhead), encrypted at line-rate, under your brand. MaiaEdge's PBC delivers 100G throughput with end-to-end visibility across every path — keeping you in the revenue stream. Premium interconnection services, deployed in weeks, no development team required."

**Hook:** "GPU cloud providers like CoreWeave and Lambda Labs require 35+ cross-connects per deployment with sub-10ms latency guarantees. Are you delivering that in minutes with full visibility — or weeks with blind spots?"

**Repatriation Angle:** "Your AI tenants are asking for private connectivity between facilities. MaiaEdge lets your team provision encrypted paths in minutes, not the 4–6 weeks it takes today, and you keep the customer relationship."

**Revenue Impact:** 3x attach rate per tenant, premium pricing on AI-secure interconnects, zero-touch operations saving ~$610K/year in labor.

**Discovery Questions (AI-Focused):**

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "Are you seeing demand from GPU cloud providers or AI infrastructure tenants?" | "Yes, Lambda/CoreWeave are asking about capacity" or "AI tenants are our fastest-growing segment" | "No AI tenant demand" or "We focus on traditional enterprise only" |
| "How are you handling multi-cloud connectivity requests from AI workloads?" | "We tell them to call Megaport" or "They figure it out themselves" | "We have automated multi-cloud fabric already" |
| "What latency guarantees can you offer AI tenants for cross-facility paths?" | "We can't guarantee latency" or "That's a gap for us" | "We have deterministic paths with SLA guarantees" |
| "Do you have visibility into network performance for AI workloads across cloud connections?" | "No, once it leaves our facility we're blind" or "We can't prove SLAs" | "Full telemetry dashboard with hop-by-hop metrics" |
| "Have you invested in liquid cooling or high-density infrastructure?" | "Yes, 30kW+ racks" or "We're building it out now" | "No plans for high-density" or "Not a priority" |
| "Can your tenants prove to their regulators exactly where their data traverses between your facilities?" | "No, we can't show the physical path" | "Yes, full path compliance reporting" |

### Colocation Operators — Standard Track (With Repatriation Context)

For standard colos without strong AI signals, the repatriation trend still creates urgency.

**Repatriation Hook:** "Every enterprise pulling AI workloads out of public cloud needs private connectivity to their new infrastructure. You're the natural hub — if you can provision fast enough and offer the premium interconnection services they expect."

**Discovery Addition:** "Are any of your enterprise tenants talking about bringing workloads back from public cloud? How are you positioned to offer them private connectivity to their remaining cloud services?"

### Neoclouds (GPU Cloud Providers)

**Profile:** GPU cloud providers (CoreWeave, Lambda Labs, Crusoe, Voltage Park) operating distributed GPU clusters across multiple colocation facilities. Neoclouds are the backbone of Sovereign AI — they deploy massive compute distributed across regions and need unified, deterministic connectivity regardless of how many different regional carriers sit between their facilities.

**Primary Pain Point:** "Our inference workloads span multiple facilities. Connectivity between GPU clusters is inconsistent, provisioning takes too long, and we have no visibility across the middle mile."

**Value Proposition:** "MaiaEdge delivers deterministic paths between your GPU clusters so inference performance is predictable everywhere. Your team provisions paths in minutes and sees the route end-to-end — no routing complexity, no visibility gaps, no middle-mile black holes. One fabric across all your locations, even when there are different regional carriers between each one."

**Hook:** "Your inference workloads span multiple facilities. Is network variance across carriers compounding per-token, degrading performance? MaiaEdge delivers guaranteed private paths with full visibility across the middle mile."

**Sovereign AI Angle:** "You're building the infrastructure that powers sovereign AI. MaiaEdge lets you create a unified fabric across all your locations — deterministic, encrypted, fully visible — regardless of how many different carriers sit in between. Your customers' sovereign workloads get sovereign routing end-to-end."

**Key Distinction:** Neoclouds are the end customer deploying infrastructure, not a colo serving someone else. Messaging focuses on path control, performance predictability, and sovereign routing — not "keep your customer" — they ARE the customer.

**Discovery Questions:**

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "How many facilities are your GPU clusters distributed across?" | "Multiple, and growing" | "Single facility" |
| "What's your current experience with latency consistency between clusters?" | "Variable" or "We're troubleshooting network issues" | "Consistently meets SLAs" |
| "How long does it take to provision connectivity to a new facility?" | "Weeks" or "It depends on the carrier" | "Same-day" |
| "Do you have hop-by-hop visibility across your cross-facility paths?" | "No, we lose visibility at the handoff" | "Full telemetry" |
| "Do your enterprise customers require proof that data stays within specific geographic boundaries?" | "Yes, and we can't provide it today" | "Not a requirement" |
| "How many different carriers are involved in connecting your facilities?" | "Multiple, and coordinating them is painful" | "Single carrier, simple topology" |

### Fiber Operators — AI Corridor Track & Sovereign Middle-Mile

**Profile:** Regional fiber operators with infrastructure (dark or lit) in emerging AI corridors (DFW, Columbus, Atlanta, Chicago, Phoenix) or near announced AI data center builds.

**Primary Pain Point:** "AI data centers are being built in our markets, but we can't deliver deterministic latency paths fast enough to win the business. And the complexity of multi-carrier coordination is killing us."

**The Sovereign Middle-Mile Opportunity:** Regional fiber operators are the key to the "Sovereign Middle-Mile." The customers who need middle-mile connectivity aren't just enterprises — they're healthcare providers needing HIPAA-compliant paths between distributed facilities, carriers who need partners outside their footprint for 5G slicing, and neoclouds connecting GPU clusters across regions. All of them need the middle-mile connectivity that regional fiber operators can uniquely provide. With MaiaEdge, regional operators can both provide sovereign routing for their customers AND maintain their own operational sovereignty — they don't have to hand their customer relationships to a NaaS provider to get fabric capabilities.

**Value Proposition:** "Turn your regional fiber into the sovereign middle-mile for AI infrastructure. MaiaEdge's transport-agnostic fabric lets you provision deterministic, sovereign-routed paths in minutes — start with DIA for instant connectivity, layer in fiber capacity as demand grows. Your customers get private paths that provably stay within geographic boundaries. You keep the customer, the margin, and the operational control. Capture the AI infrastructure buildout happening in your markets before national players do."

**Hook:** "GPU cloud providers are building 2GW+ of distributed infrastructure across Dallas, Columbus, Chicago, and Atlanta. Healthcare systems are pulling AI back into private infrastructure. They all need sovereign middle-mile connectivity. Is your fiber positioned to serve that demand — or are national players capturing it?"

**Repatriation Angle:** "Every enterprise pulling AI workloads out of public cloud needs private connectivity to their new infrastructure. Your fiber — dark or lit — becomes the secure backbone. MaiaEdge lets you activate sovereign paths instantly and monetize capacity at recurring rates."

**Discovery Questions (AI-Focused):**

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "Have you seen increased demand from AI data center builds in your region?" | "Yes, [Lambda/CoreWeave/hyperscaler] is building nearby" or "Huge opportunity we're trying to capture" | "No AI builds in our region" or "Not on our radar" |
| "What's your timeline to deliver deterministic latency paths to a new AI facility?" | "60–90 days" or "We've lost deals because we couldn't move fast enough" | "Days to weeks, fully automated" |
| "Are you losing AI infrastructure deals to Zayo or other national fiber providers?" | "Yes, they move faster" or "We can't match their reach" | "We're winning these deals" |
| "Do you have fiber near any announced AI data center builds?" | "Yes, but we can't monetize it fast enough" or "It's stranded capacity" | "No fiber in AI markets" or "Already fully utilized" |
| "Are healthcare, carrier, or neocloud customers asking for paths that stay within specific geographic boundaries?" | "Yes, sovereignty is coming up more and more" | "Not a conversation we're having" |
| "How much coordination overhead do multi-carrier deals create for your ops team?" | "Significant — it's our biggest bottleneck" | "Minimal, we handle it well" |

### Network Operators — AI Infrastructure Track

**Profile:** Tier 1/2 carriers or VNOs whose enterprise customers are deploying inference workloads requiring sub-10ms latency across hybrid environments.

**Primary Pain Point:** "Our enterprise customers are deploying inference workloads that require sub-10ms latency across hybrid environments. Our current provisioning can't keep up — it's too slow and too complex."

**Value Proposition:** "Extend your automation to the AI edge. MaiaEdge enables deterministic, low-latency paths (<2μs overhead) across your network and partners' networks, with hop-by-hop visibility your AI customers demand for troubleshooting and SLA proof. One fabric that eliminates both the speed and complexity bottlenecks."

**Hook:** "Research shows 33% of AI/ML latency is attributable to network slowness. When your enterprise customers deploy inference, can you prove your network isn't the bottleneck?"

**Repatriation Angle:** "Your enterprise customers pulling AI workloads back from public cloud still need connectivity to remaining cloud services. You're the natural provider — if you can deliver private, deterministic paths without 60-day provisioning cycles and multi-carrier coordination headaches."

**5G Slicing Context:** Network operators delivering 5G network slicing (e.g., T-Systems' use case of giving real-time priority to an ambulance over consumer streaming) need the same deterministic, sovereign-routed connectivity in the middle mile. MaiaEdge extends that determinism across network boundaries.

### MSP/Aggregators — AI Context

**Repatriation Hook:** "Your customers in healthcare, energy, and financial services are repatriating AI workloads and need multi-carrier private connectivity with sovereign routing. You aggregate the carriers — MaiaEdge gives you visibility, automation, and path control across all of them."

---

## Part 5: Competitive Positioning for AI Conversations

### Against Lumen PCF

Lumen has explicitly positioned PCF for AI infrastructure, booking $5B in AI-related sales. CEO Kate Johnson targets the "AI model inference phase."

**MaiaEdge Position:** GPU cloud providers and inference-focused colos want to own their customer relationships and connectivity margins. They don't want to become dependent on Lumen. MaiaEdge lets them build Lumen-like capabilities on their own infrastructure.

**One-liner:** *"Lumen builds their empire; MaiaEdge empowers you to build yours."*

**AI-specific reframe:** "Lumen is betting that inference operators will outsource their connectivity. We're betting they want to own it. CoreWeave didn't build a $23B business by depending on someone else's fabric."

**Sovereignty reframe:** "With Lumen PCF, your sovereign routing depends on Lumen's infrastructure decisions. With MaiaEdge, you control the paths. You prove compliance. You own the sovereignty story."

### Against NaaS (Megaport/Equinix Fabric)

**Standard Position:** "We're not a SaaS fabric you join. We help you build your own."

**AI-specific reframe:** "Megaport just acquired Latitude.sh to converge compute and networking. That means your connectivity margins become their growth strategy. MaiaEdge lets you offer the same AI-ready instant connectivity under your brand — Equinix-like fabric capabilities without giving up control."

**Sovereignty reframe:** "When your customer's data traverses Megaport's fabric, sovereignty sits with Megaport. When it traverses your MaiaEdge-powered fabric, sovereignty sits with you. In the sovereign AI era, that distinction matters."

### Against "Do Nothing"

**AI-specific urgency:** "How long does it take to provision a cross-connect for a GPU cloud tenant? 60–90 days? CoreWeave went from 3 to 32 data centers in two years. Lambda Labs is targeting 3GW by 2030. These operators will go where they can get connected fastest — and where they get the least operational complexity."

**Repatriation urgency:** "87% of enterprises plan to repatriate AI workloads in the next 12–24 months. When they call you for sovereign, private connectivity, what's your answer — minutes or months?"

---

## Part 6: The Urgency — Why Now

Several market dynamics create time-sensitivity for MaiaEdge:

**Geographic Diffusion.** Power constraints are pushing AI infrastructure into secondary markets. These facilities need connectivity solutions that traditional Tier 1 players don't prioritize. Regional operators who move fast win.

**Speed of Neocloud Buildout.** CoreWeave went from 3 to 32 data centers in two years. Lambda Labs has 20+ sites targeting 3GW by 2030. These operators need instant interconnection, not 60–90 day projects.

**Colocation Partnership Model.** Neoclouds primarily lease from colocation partners (Aligned, Cologix, EdgeConneX). These colos are our existing target segment — AI just amplifies their pain and creates an opportunity to offer premium interconnection services without development effort.

**Mid-Tier Connectivity Gap.** PacketFabric, Console Connect, and others have no credible inference-specific or sovereign routing positioning. The window to establish MaiaEdge as the purpose-built solution is open.

**EU AI Act Enforcement (August 2026).** Sovereignty-driven demand will spike as enforcement dates approach. MaiaEdge's sovereign routing and path visibility become compliance enablers.

**Crown Castle Exit.** Crown Castle is selling 100,000+ metro route miles to Zayo, creating market disruption and potential customer displacement among fiber operators.

**Hyperscaler CapEx Surge.** $290B in 2024, expected 40%+ increase in 2025. Microsoft alone outsourced $60B+ to neoclouds due to Azure capacity constraints — all needing connectivity solutions.

**Sovereign AI Regulation Cascade.** Beyond the EU AI Act: 18 US state privacy laws active, China/India/Saudi Arabia mandate local processing, GDPR/CLOUD Act tensions unresolved. The demand for provably sovereign routing will only increase.

---

## Part 7: Recommended Actions

1. **Layer AI messaging onto existing segment playbooks.** Don't create a new segment — add AI-specific hooks, discovery questions, and value props to Colocation, Fiber, and Network Operator playbooks. Frame the colo value as becoming an Equinix-like fabric: premium interconnection services without the development burden.

2. **Add "AI Infrastructure Focus" as an enrichment attribute.** Flag accounts in HubSpot that show AI signals (GPU cloud tenants, liquid cooling, AI-ready positioning, AI corridor presence) so sales can select the appropriate messaging track.

3. **Prioritize neocloud outreach.** GPU cloud providers are the most acute pain point — scaling fast, spending heavily on connectivity, no good solution for deterministic cross-facility paths. Position them as the backbone of Sovereign AI.

4. **Arm colo-focused conversations with repatriation data.** The stats in this document give colo operators a reason to act now: their tenants are already repatriating, and those who offer AI-secure private connectivity win the attach.

5. **Target fiber operators as Sovereign Middle-Mile providers.** Regional operators in DFW, Columbus, Atlanta, Phoenix, and Chicago are sitting on infrastructure (dark or lit) that AI data centers, healthcare systems, and neoclouds need. Message the dual sovereignty value: operators maintain their own sovereignty while enabling it for their customers.

6. **Focus enterprise AI messaging on specific verticals.** Healthcare (HIPAA/GDPR), energy grids (safety-critical), and carriers (5G slicing) — not generic "enterprise repatriation." These verticals have the most acute sovereign routing needs.

7. **Own "Sovereign Routing" as a thought leadership category.** Planning to speak on sovereign routing at CCT Dublin, publish blog series, and secure podcast appearances. The goal is to own this language and space as both a thought leader and product enabler. Sovereign routing should become synonymous with MaiaEdge in the market's vocabulary.

8. **Track Lumen PCF positioning in every deal.** Lumen is the primary competitive threat in AI-focused conversations. Always search for latest Lumen PCF news before competitive discussions. Use the #COMPETITION_PRIVATE_FABRIC tag in HubSpot.

9. **Monitor EU AI Act enforcement timeline (August 2026).** Sovereignty-driven demand creates urgency for path visibility and sovereign routing capabilities. Prepare case studies and compliance positioning materials in advance.

10. **Expand conference presence to AI infrastructure events.** The buyers repatriating AI workloads and building inference infrastructure are CIOs and VP Infrastructure — not traditional telecom network buyers. Meet them where they are.

---

## Appendix: Key Statistics Quick Reference

| Stat | Value | Source / Context |
|------|-------|-----------------|
| Inference share of AI demand by 2029 | 70% | McKinsey |
| Inference CAGR through 2030 | 35% | Industry consensus |
| Enterprises planning repatriation (12–24 months) | 87% | SiliconANGLE, 2026 |
| CIOs planning to repatriate | 86% | Barclays CIO Survey, 2025 |
| AI/ML latency attributable to network | 33% | AWS research |
| Hyperscaler CapEx (2024) | $290B | Public filings |
| Lumen AI-related sales booked | $5B | Lumen earnings |
| Memphis bandwidth growth (2023–2024) | 4,300% | Industry reports |
| EU AI Act fines | Up to 7% global revenue | EU regulation |
| Sovereign cloud market by 2032 | $823B | Industry projections |
| CoreWeave data center growth | 3 → 32 in 2 years | Public reporting |
| Lambda Labs infrastructure target | 2GW+ / 3GW by 2030 | Public reporting |
| Organizations adopting hybrid/multi-cloud by 2027 | 90% | Gartner |
| Cumulative AI infrastructure investment | $5.2T | McKinsey |
| Network latency improvement from edge inference | 41–55ms reduction | AWS Local Zones research |
| European sovereign cloud adoption (within 12 months) | 84% | Industry survey |
| Organizations unable to isolate AI from sensitive access | 55% | Security research |
| Organizations unable to enforce AI purpose limitations | 63% | Security research |

---

*This document combines research from the AI Inference Infrastructure Connectivity Opportunity Brief and the AI Repatriation Wave Strategic Opportunity Brief, incorporating strategic direction from Hannah Roberts (Marketing Director), and aligned to MaiaEdge's Golden Messaging Framework and customer segment definitions.*

*Last updated: February 2026*
