# MaiaEdge ICP Sales Playbook — Complete Reference

**Private paths. Any network. Instantly.**

February 2026 | MaiaEdge Internal — Confidential

---

## How to Use This Document

This is the comprehensive ICP reference for MaiaEdge. It covers every customer segment, including classification logic, personas, pain points, value propositions, discovery questions, objection handling, and exclusion criteria. Use it to:

- **Classify accounts** during enrichment and prospecting
- **Prepare for discovery calls** with segment-specific pain language
- **Select the right messaging track** based on observable signals
- **Qualify or disqualify** accounts using tiering and exclusion logic
- **Handle objections** with proven reframes

**Cross-references:** For competitive positioning, see the Competitive Positioning Guide. For AI-specific messaging and market trends, see the AI Market Positioning & Messaging Guide. For email writing, see the Messaging Framework V4. For HubSpot property architecture, see the 12-Property Framework. For Cloud On-Ramp business cases, see the Cloud On-Ramp Business Case.

---

## Segment Quick Reference

| Segment | What They Own | Revenue Model | Scale | Priority | Example Companies |
|---------|---------------|---------------|-------|----------|-------------------|
| **Neocloud** | GPU clusters across multiple colo facilities, AI/ML software stack | GPU compute rental, inference-as-a-service | Rapidly scaling, $50M–$5B+ revenue, multi-facility | HIGH | CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI |
| **Colo — AI Infrastructure** | Buildings, meet-me rooms, metro fiber + liquid cooling, high-density power | Space/power (premium for AI), cross-connects, AI infrastructure services | 1–50+ facilities, GPU cloud tenants, $50M–$1B+ | HIGH | Aligned, Cologix, EdgeConneX, QTS, Vantage, Stack |
| **Colo (Standard)** | Buildings, meet-me rooms, metro fiber (NOT route miles) | Space/power (60–80%), cross-connects (10–20%), cloud on-ramps (0–5%) | 1–50+ facilities, $10M–$500M revenue | HIGH | RevNet, Centra, ARK, DataBank, Flexential |
| **Fiber Operator** | Physical fiber, optical transport (measured in route miles) | Dark fiber (IRUs), lit wavelengths, metro Ethernet, wholesale | 500–100,000 route miles, $25M–$500M revenue | HIGH | Arvig, Ocean Networks, Crown Castle Fiber, Fatbeam |
| **Network Operator** | National/global network, mix of owned fiber and leased capacity | Enterprise connectivity, MPLS, wavelengths, IP transit | 50+ PoPs, 500+ employees, national/global | MEDIUM | NTT, IENTC, AT&T, Verizon, Lumen |
| **MSP/Aggregator** | Contracts (not infrastructure), aggregate 3+ carriers | Margin on resold connectivity, managed services fees | 50–500 employees, $20M–$500M revenue | MEDIUM | INDATEL, 11:11 Systems, Granite |
| **Enterprise (Dark Fiber)** | Own or lease private fiber/WAN for internal use | Internal cost center, not selling services | Varies — universities, healthcare, HFT, utilities | LOW | Research universities, hospital networks, financial firms |

---

## Classification Decision Tree

```
START
 ↓
GPU cloud provider (CoreWeave, Lambda Labs, Crusoe, Voltage Park, etc.)?
 → YES → NEOCLOUD
 ↓ NO
Owns DC facilities + offers colocation services?
 → YES → Check AI signals
 │           ├── AI signals STRONG → COLOCATION — AI INFRASTRUCTURE
 │           └── AI signals NONE/WEAK → COLOCATION (Standard)
 ↓ NO
Owns >500mi fiber + sells commercially?
 → YES → FIBER OPERATOR
 ↓ NO
Tier 1/2 carrier OR national/global scale?
 → YES → NETWORK OPERATOR
 ↓ NO
Aggregates 3+ carriers + minimal owned infrastructure?
 → YES → MSP/AGGREGATOR
 ↓ NO
Uses internally + doesn't sell services?
 → YES → ENTERPRISE (Low Priority)
 ↓ NO
Matches any EXCLUDE criteria? → YES → EXCLUDE
 ↓ NO
Pure reseller/VAR/consultancy? → YES → EXCLUDE — LOW VALUE
END
```

### Classification Keywords (Instant Triggers)

| Segment | Instant Classification Keywords |
|---------|--------------------------------|
| **Neocloud** | "GPU cloud," "GPU-as-a-service," "AI cloud provider," "inference cloud," "ML infrastructure provider." Company names: CoreWeave, Lambda Labs, Crusoe Energy, Voltage Park, Together AI, Anyscale, RunPod, Paperspace |
| **Colo — AI Infrastructure** | Colo keywords + "liquid cooling," "DeltaFlow," "GPU-ready," "AI-ready data center," "high-density colocation," "30kW racks," confirmed GPU cloud tenants |
| **Colo (Standard)** | "colocation provider," "carrier hotel," "interconnection facility," "data center operator," "meet-me room," "carrier neutral," "interconnection fabric" |
| **Fiber Operator** | "lit fiber services," "fiber to the premise," "facilities-based broadband," "fiber network operator," "dark fiber provider," "wholesale fiber," "regional fiber operator," "route miles" |
| **Network Operator** | "Tier 1 carrier," "Tier 2 carrier," "national backbone," "global carrier," "incumbent carrier," "managed connectivity services," "multi-domain orchestration" |
| **MSP/Aggregator** | "carrier broker," "white label provider," "B2B marketplace," "carrier aggregator," "network aggregator" |

---

## Exclusion Criteria

**EXCLUDE if any of the following apply.** These are definitive disqualifications — do not tier, do not enrich, do not outreach.

| Exclusion Category | Description | How to Identify |
|-------------------|-------------|-----------------|
| **IXP (Internet Exchange Point)** | Operate peering exchanges, not connectivity services. They facilitate peering, not private path provisioning. | Website says "internet exchange," "peering exchange," PeeringDB lists them as IXP. Examples: DE-CIX, AMS-IX, LINX |
| **Tower REIT** | Own/operate cell towers and passive infrastructure. Don't provision connectivity services. | "Tower company," "wireless infrastructure," SBA Communications, American Tower, Uniti Group |
| **IT MSP (Managed IT Services)** | Manage IT help desk, endpoints, cybersecurity — NOT network infrastructure. Distinct from Network MSP/Aggregator. | "Managed IT," "IT support," "cybersecurity MSP," "endpoint management." No carrier relationships or wholesale connectivity |
| **Retail ISP (verified no wholesale)** | Consumer broadband providers without wholesale/enterprise connectivity offerings. | Residential-only pricing pages, "home internet," no enterprise/wholesale services page. Must verify — some retail ISPs also sell wholesale |
| **Software/Platform Vendor** | Build orchestration, SDN, or connectivity software. Potential PARTNER, not customer. | "Network orchestration software," "SDN platform," "network automation tool." Examples: Itential, Netcracker, Blue Planet |
| **Hyperscaler** | AWS, Azure, Google Cloud, Oracle Cloud. They build their own infrastructure at planetary scale. | Self-evident. Also includes hyperscaler subsidiaries focused on cloud services |
| **Enterprise (internal network only)** | Large enterprises with private networks used exclusively internally. No commercial connectivity sales. | No "Services" page selling connectivity. Network exists to serve their own business (banks, retailers, manufacturers with no wholesale arm) |
| **<10 employees (verified)** | Too small to be a viable customer. Must be verified — some holding companies appear small but operate significant infrastructure. | LinkedIn employee count <10, confirmed via website/LinkedIn. Flag for manual review if infrastructure signals are strong despite small headcount |
| **Vendor/Contractor/Manufacturer** | Makes networking equipment, provides installation services, or manufactures hardware. No operator business. | "Network equipment manufacturer," "fiber installation contractor," "cable manufacturer." Examples: Corning, CommScope (unless they have operator divisions) |
| **Consulting Firm** | Telecom consultants, network design firms, advisory practices. | "Telecom consulting," "network design services," "advisory firm." No owned infrastructure or commercial connectivity |
| **Trade Organization** | Industry associations, standards bodies, advocacy groups. | "Association," "consortium," "alliance," "standards body." Examples: NTCA, Fiber Broadband Association, MEF |
| **Defunct/Acquired** | Company no longer operates independently. Merged, acquired, or shut down. | Website down, redirects to acquirer, news confirms acquisition/closure. Note acquirer in HubSpot for potential outreach to parent company |

### Edge Cases Requiring Manual Review

Some companies straddle categories. Flag for human review when:

- Company says "MSP" but also mentions owned fiber (might be Fiber Operator)
- Retail ISP with enterprise division (might qualify if wholesale arm exists)
- Small headcount (<10) but significant infrastructure signals
- Software vendor with network operations division
- "Consulting" firm that also operates infrastructure
- Company recently acquired — parent company might be a target

---

## Segment 1: Neoclouds (GPU Cloud Providers)

### How This Business Works

Neoclouds are GPU cloud providers — they own massive clusters of GPUs distributed across multiple colocation facilities and sell compute capacity (training and inference) to enterprises and AI companies. They don't own data center buildings; they lease space from colocation operators. Their value is in the GPU fleet, AI/ML software stack, and the ability to deliver compute at scale.

Neoclouds are the backbone of Sovereign AI. They create unified compute fabrics across distributed locations, even when multiple different regional carriers sit between their facilities.

**What They Own:** GPU clusters, AI/ML software stacks, orchestration platforms. They do NOT own buildings — they lease from colos.

**Revenue Model:** GPU compute rental (hourly/reserved), inference-as-a-service, training cluster access, managed AI infrastructure.

**Scale:** Rapidly scaling. $50M–$5B+ revenue. Multi-facility (3–30+ locations). Expanding from 3 to 30+ facilities in 1–2 years is common.

**Key Distinction:** Neoclouds ARE the end customer — they deploy their own infrastructure. Messaging focuses on path control and performance predictability, NOT "keep your customer" (they are the customer).

> **⚠️ CoreWeave Targeting Note:** CoreWeave told Abilash at MetroConnect (Feb 2026) that they do not have the same challenges as other NeoClouds. **Not an active target right now.** Keep as reference company for market context and segment classification, but do not include in active outreach campaigns.

### Neocloud Sub-Segments

> **For detailed sub-segment profiles (architecture, pain points, walk-away statements, opening conversations), see the Neocloud Cheatsheet.** The table below provides routing guidance for messaging priority.

> **Note:** AI Data Centers (e.g., IREN, Core Scientific, Northern Data Group, TeraWulf) are covered under Colocation Operators — AI Infrastructure (Segment 2). Cross-reference when a prospect straddles both segments.

| Sub-Segment | Examples | Lead With | Networking Sophistication |
|-------------|----------|-----------|--------------------------|
| **Large-Scale GPU NeoClouds** | Crusoe, Voltage Park, Nebius, Lambda Labs | All three layers (scale creates all three pains) — highlight Recompute Tax ($4,800/GPU/month at 30% interruption rate) | Variable — some have networking staff |
| **Tier 1 Inference Providers** | Together AI, Groq, DeepInfra, Anyscale | Observability + deterministic paths (inference is their product, tail latency kills SLAs) | Moderate — may have some network awareness |
| **AI Infrastructure Providers** | Cirrascale, Vultr, Fluidstack, DigitalOcean, Nscale | Cloud on-ramp + observability (API-driven, multi-cloud) — note Megaport/Latitude.sh competitive threat | Minimal — developer-first |
| **Sovereign AI Clouds** | Firmus, E2E Networks, Yotta, Nscale (EU) | Sovereign routing + observability (regulatory compliance is a driver — GDPR, EU AI Act, DPDP, CLOUD Act) | Variable — compliance-driven |
| **Crypto-to-AI Pivots** | IREN (Iris Energy), Core Scientific, Northern Data Group, TeraWulf | Observability (they're learning networking as they go — legacy crypto infrastructure wasn't built for AI traffic patterns) | Minimal — learning curve |

### ⚠️ INVERTED MESSAGING HIERARCHY

**Unlike other segments, neocloud messaging follows an inverted hierarchy:**

1. **LEAD: Observability** — "See why you're slow. Then fix it."
2. **SECOND: Cloud On-Ramp** — Accelerate cloud and hyperscaler connectivity
3. **THIRD: Deterministic Paths** — Known hop count, controlled latency

Neoclouds are compute companies that accidentally became networking companies. They have NO WAN teams, NO Kentik, NO PRTG. Lead with the symptom (you can't see why inference is slow), not the solution (deterministic paths).

### Key Personas

| Persona | Titles | Primary Concerns |
|---------|--------|-----------------|
| **CEO/Founder** | CEO, Co-Founder, President | Scaling infrastructure fast, cost efficiency, competitive differentiation |
| **CTO/VP Engineering** | CTO, VP Engineering, VP Platform | Network determinism for inference, multi-facility consistency, troubleshooting |
| **VP Infrastructure** | VP Infrastructure, VP Data Center Operations, VP Cloud Infrastructure | Provisioning speed for new facilities, carrier coordination, operational complexity |
| **Network Architect** | Network Architect, Principal Engineer, Head of Networking | End-to-end visibility, cross-facility path control, latency consistency |
| **Head of Platform** | Head of Platform, VP Product, Director Platform Engineering | Consistent inference SLAs, predictable performance regardless of facility |
| **Network/IT Admin** | IT Generalist, Infrastructure Engineer, Infra Operations | Day-to-day network troubleshooting, lack of formal WAN training, managing networking as secondary role |

### Pain Points (Their Language)

| Persona | Pain Points |
|---------|-------------|
| **CEO/Founder** | "We're scaling to 30+ facilities and connectivity is our biggest operational bottleneck." "Each new facility is a 6-week connectivity project." |
| **CTO/VP Engineering** | "Inference latency varies by facility because every path is different." "We can't see what happens between our facilities — it's a black box." |
| **VP Infrastructure** | "Provisioning connectivity to a new facility takes weeks. We need it in days." "Coordinating multiple carriers for each site is painful." |
| **Network Architect** | "No visibility once traffic leaves our infrastructure." "We're debugging inference latency issues blind across the middle mile." |
| **Head of Platform** | "We can't guarantee consistent inference SLAs across facilities because the network is unpredictable." |
| **Network/IT Admin** | "I'm not a network person, but I'm stuck managing connectivity between our GPU clusters. I don't have visibility or tools designed for this." |

### Value Propositions by Persona

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/Founder** | Scale without connectivity being the bottleneck. Every new facility connects in minutes, not weeks. Same deterministic performance everywhere. | "Your inference performance shouldn't depend on which facility or which path. MaiaEdge makes it predictable everywhere." |
| **VP Infrastructure** | Provision paths between facilities in minutes, not weeks. Same deterministic connectivity whether you're in Aligned, Cologix, or any federated partner. | "Every new facility doesn't have to be a connectivity project. Your team provisions paths in minutes." |
| **CTO/VP Engineering** | Explicit private Ethernet paths with known hop count and controlled latency. No best-effort variance compounding per token. Visibility across every hop. | "Inference latency is predictable when the path is predictable. MaiaEdge eliminates the network as a variable." |
| **Network Architect** | End-to-end visibility across paths that traverse multiple colos and carriers. Hop-by-hop telemetry on paths you don't own. | "See the path yourself. Stop debugging blind across the middle mile." |
| **Head of Platform** | Consistent inference performance regardless of where workloads run. Deterministic paths mean predictable SLAs. | "Your SLAs depend on network predictability. MaiaEdge delivers it." |
| **Network/IT Admin** | Observability dashboard showing why inference is slow. Automated provisioning so you don't need deep networking expertise. | "See where the latency is coming from. Get it fixed without network PhDs." |

### Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "How many facilities are you deployed across?" | "Multiple, and scaling rapidly" | "Single facility" |
| "How do you handle connectivity between GPU clusters in different facilities?" | "It's painful — each facility is different, takes weeks" | "We have a dedicated network team handling it well" |
| "What visibility do you have into paths between facilities?" | "None once traffic leaves our infrastructure" | "Full visibility end-to-end" |
| "Are you experiencing inference latency variance across different paths?" | "Yes, and it's hard to debug" | "Performance is consistent" |
| "How many different carriers are involved in connecting your facilities?" | "Multiple, and coordinating them is painful" | "Single carrier, simple topology" |
| "Do your enterprise customers require proof that data stays within specific geographic boundaries?" | "Yes, and we can't provide it today" | "Not a requirement" |

### Objection Handling

| Objection | Rebuttal | Frequency | Why They Ask |
|-----------|----------|-----------|-------------|
| "We're focused on GPU infrastructure, not networking" | That's exactly why. You shouldn't have to become network experts. MaiaEdge gives your team the ability to provision deterministic paths in minutes without routing complexity. Focus on inference, not interconnects. | HIGH | They see networking as distraction from core competency |
| "Our colo partners handle connectivity" | Do they deliver deterministic paths with end-to-end visibility? Or best-effort cross-connects? Inference performance depends on network predictability. If you're debugging latency issues, the network is probably the variable you can't see. | HIGH | They assume colo responsibility ends at facility boundary |
| "We're building our own network team" | Building a network team to manage multi-carrier complexity is expensive and slow. MaiaEdge gives you the capability without the headcount. Your team provisions paths; we handle the protocol complexity. | MEDIUM | They're in network hiring mode, may think build is cheaper |
| "Each facility is different — how does this work?" | That's the point of federation. MaiaEdge PBCs at each location, unified under one control plane. Doesn't matter if it's Aligned in Dallas or Cologix in Columbus — same deterministic paths, same visibility, same provisioning speed. | MEDIUM | Worried about operational fragmentation |

### Use Cases

- **Distributed Inference Fabric:** Deterministic paths between GPU clusters across multiple colo facilities for consistent inference performance
- **Rapid Facility Onboarding:** New facility connectivity in minutes instead of weeks as neocloud scales
- **Sovereign AI Delivery:** Unified fabric across all locations with sovereign routing — customer workloads get provably private paths regardless of underlying carriers
- **Multi-Cloud Data Access:** Private paths to AWS/Azure/GCP for RAG architectures requiring multi-cloud data retrieval
- **Cloud On-Ramp:** Native connectivity to hyperscaler regions for seamless data pipeline integration

### What Change We're Asking

**Infrastructure Changes**
Connectivity between facilities becomes automatically provisioned rather than manually coordinated with carriers. PBCs at each colo location unify the multi-carrier reality into a single control plane. No new carrier agreements needed — you're just adding a path provisioning layer on top of existing facility agreements.

**Operational Changes**
Move from "coordination projects" to "provisioning in minutes." When spinning up a new facility, networking stops being a 6-week dependency. Your infrastructure team goes from reactive (waiting on carriers) to proactive (facilities go live on schedule).

**Commercial Model Changes**
Your SLA guarantees change. Today you can't promise inference latency because network is unpredictable. With deterministic paths, inference performance becomes predictable, which means you can guarantee SLAs to your customers.

**Integration**
The PCE manages path provisioning via API. Your facility onboarding workflow triggers path provisioning automatically. Your observability dashboard (Kentik, custom, etc.) integrates to show end-to-end path telemetry.

**Team & Skills**
Your IT/Network Admin doesn't need to become a BGP expert. They provision paths from a portal, monitor latency through dashboards, and escalate when needed. The complexity is abstracted away.

### Why Change Statement

"Every day you spend coordinating carriers for new facilities is a day you're not scaling compute. And every facility where network is unpredictable is a facility where you can't guarantee inference latency to customers. That's not just a networking problem — it's a business problem."

### Proof Points

- CoreWeave, Lambda Labs, and other major GPU cloud providers are all multi-facility and need deterministic connectivity
- AI workloads are latency-sensitive at the token level — jitter from best-effort paths directly impacts inference performance
- Customers are asking for sovereign routing guarantees — you need to prove data stays within geographic boundaries
- **Recompute Tax:** A single network interruption during distributed training forces checkpoint rollback. At $4,800/GPU/month with a 30% interruption rate on 128K context Llama-3 70B, the recompute cost dwarfs the MaiaEdge subscription
- **Egress economics:** Neoclouds moving 50–200TB/month between facilities and cloud regions. Egress at $0.08–$0.12/GB = $4K–$24K/month per facility. Shared port model via MaiaEdge reduces per-connection cost dramatically
- **Competitive threat:** Megaport acquired Latitude.sh (2024), now offering GPU-as-a-Service + networking bundle. Positions against neoclouds building their own connectivity. MaiaEdge counter: sovereignty — own your paths, don't rent Megaport's

### Account Tiering

| Tier | Criteria |
|------|----------|
| **Tier 1** | 5+ facilities, publicly announced GPU capacity >100MW, rapid expansion trajectory |
| **Tier 2** | 2–4 facilities, growing, $50M+ revenue or significant funding |
| **Tier 3** | Early-stage, single facility expanding to second |

### Expansion Path

- **Land:** Deterministic paths between two facilities with visibility
- **Expand 1:** Cloud On-Ramp to AWS/Azure/GCP regions
- **Expand 2:** Federation to multi-carrier strategy across all regions
- **Expand 3:** Sovereign routing with compliance reporting

---

## Segment 2: Colocation Operators — AI Infrastructure

### How This Business Works

Same as standard colocation operators (own/operate facilities, rent space/power/cooling) BUT with significant investment in AI-ready infrastructure: liquid cooling, high-density racks (30kW+), GPU cloud tenants (CoreWeave, Lambda Labs, etc.), and AI-focused marketing.

The real value MaiaEdge delivers: becoming an Equinix-like fabric — offering fast, deterministic, secure private interconnection as premium services without the development work or capital investment.

**What They Own:** Same as standard colo PLUS liquid cooling systems, high-density power infrastructure, GPU-ready facilities.

**Revenue Model:** Same as standard colo PLUS premium pricing for AI infrastructure services, higher power revenue per rack, AI tenant attach rates.

**Key Signal Difference from Standard Colo:** Confirmed GPU cloud tenants, liquid cooling investment, "AI-ready" marketing, presence in AI corridors (DFW, Columbus, Atlanta, Phoenix).

### AI Signal Detection

| Signal | Strong AI (Use AI Track) | Weak/No AI (Use Standard Track) |
|--------|--------------------------|--------------------------------|
| GPU cloud tenants | CoreWeave, Lambda Labs, Crusoe, Voltage Park confirmed | No GPU/AI tenants |
| Infrastructure | Liquid cooling, 30kW+ racks, GPU cluster support | Standard 5–15kW per rack |
| Marketing | "AI-ready," "GPU cloud," "inference hosting" | General colocation services |
| Geography | DFW, Columbus, Atlanta, Chicago, Phoenix | Traditional markets without AI buildout |
| News | Power upgrades, capacity expansion for AI | No AI-related investments |

### Key Personas

| Persona | Titles | Primary Concerns |
|---------|--------|-----------------|
| **CEO/President** | CEO, President, Managing Director | Competitive differentiation, AI tenant acquisition, M&A positioning |
| **CTO/VP Engineering** | CTO, VP Engineering, VP Technology, VP Infrastructure | Network determinism for inference, matching compute investment with connectivity |
| **CFO** | CFO, VP Finance | ROI on AI infrastructure investment, premium pricing justification |
| **VP Sales/CRO** | CRO, VP Sales, VP Commercial | Winning GPU cloud tenants, selling inference-grade connectivity |
| **Sr. Network Engineer** | Sr. Network Engineer, Lead Network Engineer, Network Architect | Best-effort jitter breaking inference, no visibility across paths |
| **Director DC Operations** | Director Data Center Operations, VP Operations | Completing the AI infrastructure stack — power, cooling, AND network |

### Pain Points (Their Language)

| Persona | Pain Points |
|---------|-------------|
| **CEO/President** | "We've invested in AI infrastructure but can't differentiate on connectivity." "GPU cloud providers are evaluating facilities — connectivity is part of that decision." |
| **CTO/VP Engineering** | "We've built the power and cooling for AI. But our network is still best-effort." "Inference is latency-sensitive at the token level. Traditional IP routing introduces jitter." |
| **VP Sales/CRO** | "GPU cloud providers are asking for latency guarantees we can't make." "We're winning on power density but losing when tenants ask about inference-grade connectivity." |
| **Sr. Network Engineer** | "Best-effort routing introduces micro-jitter that breaks inference performance." "Tenants complain about inference latency spikes, but I have no visibility across the path." |
| **Director DC Operations** | "We've built 30kW racks and liquid cooling for AI workloads, but connectivity is still the same as traditional enterprise." |

### Value Propositions by Persona

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/President** | Complete the AI infrastructure story. Deterministic connectivity that matches your power and cooling investments. Win GPU cloud tenants on the full stack. | "AI tenants are evaluating now. When they ask about latency guarantees for distributed inference, you have an answer." |
| **CTO/VP Engineering** | Deterministic private Ethernet paths engineered for AI inference. Known hop count, known latency characteristics, controlled failure domains. | "Your GPU cloud tenants need network determinism, not best-effort. MaiaEdge makes the path predictable." |
| **VP Sales/CRO** | Sell inference-grade connectivity alongside your AI infrastructure. Deterministic private paths with guaranteed latency characteristics. | "GPU cloud tenants aren't asking for faster cross-connects. They're asking for deterministic paths. Different conversation, different sale." |
| **Sr. Network Engineer** | Explicit private Ethernet paths with known hop count and controlled latency. No dynamic rerouting, no queueing variance. | "Inference latency issues are impossible to troubleshoot on best-effort paths. MaiaEdge gives you deterministic transport and the visibility to prove it." |
| **Director DC Operations** | Complete your AI infrastructure investment. Engineered the facility for high-density compute — now engineer the network for inference-grade determinism. | "You've built AI-ready facilities. MaiaEdge makes your connectivity AI-ready too." |

### Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "Do you have GPU cloud tenants like Lambda Labs, CoreWeave, or Crusoe?" | "Yes, they're our fastest-growing segment" | "No GPU/AI tenants" (→ use Standard Colo) |
| "Are you investing in liquid cooling or high-density power (30kW+ racks)?" | "Yes, we're building out AI-ready infrastructure" | "Standard density only" (→ use Standard Colo) |
| "What are GPU cloud tenants asking for that you can't deliver today?" | "Latency guarantees, deterministic paths, visibility" | "Just faster cross-connects" |
| "How do you differentiate from other AI-ready facilities?" | "Power and cooling, but connectivity is the same" | "We have differentiated connectivity" |
| "Can your tenants prove to regulators exactly where their data traverses between facilities?" | "No, we can't show the physical path" | "Yes, full path compliance reporting" |

### Objection Handling

| Objection | Rebuttal | Frequency | Why They Ask |
|-----------|----------|-----------|-------------|
| "Our GPU cloud tenants haven't asked for this" | They will. Inference performance depends on network predictability. Best-effort introduces jitter that impacts token-by-token latency. When they start debugging inference performance issues, the network is the first place they'll look. | HIGH | They think current relationships are stable |
| "We just provide the facility — networking is their problem" | GPU cloud tenants need network determinism as much as they need power and cooling. If you're investing in liquid cooling and high-density racks, network predictability is the missing piece. MaiaEdge lets you be the full-stack AI infrastructure partner. | HIGH | They see themselves as real estate, not service provider |
| "Equinix already offers this" | Equinix offers it on THEIR infrastructure, for THEIR customers. Your tenants use Equinix Fabric and build loyalty to Equinix. MaiaEdge lets you offer Equinix-like fabric capabilities under your brand. Premium services without the development burden. | MEDIUM | They acknowledge need but see competitor as blocking |

### Priority Accounts

| Company | GPU Cloud Tenant(s) | Details |
|---------|---------------------|---------|
| Aligned Data Centers | Lambda Labs | Multi-facility partnership, DeltaFlow liquid cooling (300kW/rack) |
| Cologix | Lambda Labs, CoreWeave | Columbus, Chicago, Dallas; Lambda 320MW+ committed |
| EdgeConneX | Lambda Labs | Distributed edge portfolio, multiple markets |
| QTS Data Centers | Hyperscaler AI workloads | DFW, Phoenix; high-density rack support |
| Vantage Data Centers | Multiple GPU cloud | Phoenix, Dallas, Atlanta campuses |
| Stack Infrastructure | AI infrastructure buildouts | Hyperscale campus model |

### What Change We're Asking

**Infrastructure Changes**
Deploy Path Border Controllers in your meet-me rooms — typically one PBC per facility to start, potentially more as you scale. The PBC is a 1RU device with dual 100G interfaces. It connects to your existing switching infrastructure at the meet-me room level. The PBC doesn't replace your existing switches or routers — it sits alongside them as the automation and visibility layer.

**Operational Process Changes**
Your operations team moves from executing individual cross-connects to managing the fabric itself. Instead of touching the network for every tenant request, they're monitoring the platform, handling exceptions, and focusing on higher-value work. The volume of routine tickets drops dramatically, but the nature of the work changes.

**Commercial Model Changes**
You're shifting from selling cross-connects as a low-margin, operationally-heavy add-on to selling connectivity as a core service line. This means new pricing structures, new service catalog (cloud on-ramps, automated cross-connects), new sales motions.

**Integration Requirements**
The PCE runs in the cloud and manages your PBCs. You'll integrate via APIs with cloud fabric providers (Megaport, Equinix Fabric) to offer cloud on-ramps under your brand. If you want tenant self-service, you'll either use our white-label portal or integrate our APIs into your existing customer portal.

**Team & Skills**
You don't need BGP experts or MPLS engineers. The platform abstracts that complexity. Your team needs to understand the portal, basic troubleshooting, and how to position the new services to tenants. Plan for 1-2 days of training for operations staff, half-day for sales.

### Why Change Statement

"Every day you're telling tenants 'call Megaport' is a day you're training them to build a relationship with someone else. That's not just lost margin on this transaction — it's lost control of your customer for every future connectivity need they have."

### Proof Points

- RevNet (DFW): "Imagine having Megaport capability between providers"
- Equinix Endorsement: "Revolutionary and creative" — Josh Sordelet, Principal PM
- Centra: "Fabric-in-a-box, drop it in and add water and it works... we get control over our destiny"

### Expansion Path

- **Land:** Automated cross-connects in primary facility
- **Expand 1:** Cloud on-ramps (AWS/Azure/GCP under your brand)
- **Expand 2:** Multi-site DCI between facilities
- **Expand 3:** Federation with partner networks

---

## Segment 3: Colocation Operators — Standard

### How This Business Works

Colocation operators own and operate physical data center facilities. They rent space, power, and cooling to tenants — enterprises, cloud providers, and carriers. Facilities are typically "carrier-neutral," meaning multiple carriers can connect, making them natural interconnection hubs.

**What They Own:** Buildings (data centers, carrier hotels), meet-me rooms, cross-connect infrastructure, metro fiber connecting their facilities. They do NOT typically own long-haul fiber or measure their network in "route miles" — that's a fiber operator signal.

**Revenue Model:** Space and power is the commodity (60–80% of revenue) — low margin, highly competitive. Cross-connects between tenants (10–20%) — higher margin but manual. Cloud on-ramps (0–5% today) — this is where they're losing to Megaport/Equinix.

**Scale:** 1–50+ facilities, 20–500 employees, $10M–$500M revenue, 10–100+ tenants per facility.

**Competitive Reality:** Hyperscalers and national players (Equinix, Digital Realty) have changed tenant expectations. Customers expect instant cross-connects, direct cloud access, and self-service control. When tenants need AWS Direct Connect or Azure ExpressRoute, they call Megaport — and the colo loses that revenue and customer relationship.

### Key Personas at Colocation Operators

1. **CTO / VP Engineering** — Signs contracts, owns technical vision (Priority #1)
   - Title Variations: CTO, Chief Technology Officer, Chief Technical Officer, VP Engineering, VP of Engineering, Vice President Engineering, VP Technology, VP Technical Operations, VP Infrastructure, VP Platform
   - Their Job: Responsible for all technical infrastructure, network architecture decisions, and platform strategy. Reports to CEO. Manages a small team (2-10 network engineers). Constantly balancing build vs. buy decisions with limited resources.
   - What They Care About: Investment protection (no rip-and-replace), scalability path, operational simplicity (team is already stretched thin), lifecycle control (upgrades, redundancy, visibility).
   - What Moves the Needle: "We're essentially in the network service provider business now - this gives us a way to act like one without adding headcount."

2. **VP Sales / CRO** — Revenue sponsor, feels competitive pain daily (Priority #2)
   - Title Variations: VP Sales, Vice President Sales, CRO, Chief Revenue Officer, VP Business Development, VP Commercial, VP Partnerships, SVP Sales, VP Strategic Accounts
   - Their Job: Owns tenant acquisition and retention. Competes daily against Equinix and Digital Realty. Hears "but can you offer what Equinix offers?" constantly. Responsible for revenue growth targets.
   - What They Care About: New revenue streams, competitive differentiation, closing deals faster, reducing tenant churn. They want something to sell beyond "space and power."
   - What Moves the Needle: "Right now, I've got a piece of real estate. I don't have a product. This gives me something to sell."

3. **Sr. Network Engineer** — Technical champion, lives the daily pain (Priority #3)
   - Title Variations: Senior Network Engineer, Sr Network Engineer, Sr. Network Engineer, Staff Network Engineer, Lead Network Engineer, Principal Network Engineer, Network Engineer III, Network Architect, Infrastructure Architect
   - Their Job: Handles day-to-day cross-connect provisioning, VLAN configuration, troubleshooting. Manages the meet-me room. Processes LOAs. The person who actually does the work that takes 60-90 days.
   - What They Care About: Reducing manual work, eliminating repetitive configuration, having visibility when things break, not getting blamed for provisioning delays.
   - What Moves the Needle: "Our ops team doesn't want anything else to manage - this actually reduces our workload instead of adding to it."

4. **Director of Data Center Operations** — Operational validator (Priority #4)
   - Title Variations: Director DC Operations, Director of Data Center Operations, Director Data Center, Data Center Director, Director of Colocation, Director of Facilities, Director of Infrastructure, Director of Operations
   - Their Job: Oversees all data center operations including power, cooling, physical security, and network infrastructure. Ensures compliance with SLAs and uptime guarantees. Manages operational staff and coordinates with engineering.
   - What They Care About: Lean execution, minimal management overhead, operational efficiency, maintaining SLAs without adding complexity to the stack.
   - What Moves the Needle: "If it doesn't simplify operations, I don't want it. Show me how this reduces tickets and truck rolls."

5. **CEO / President** (Companies <100 employees) — Ultimate decision-maker at smaller colos (Escalation)
   - Title Variations: CEO, Chief Executive Officer, President, Owner, Founder, Managing Director, General Manager
   - Their Job: At smaller colos, the CEO is often directly involved in major technology decisions. They're looking for strategic differentiation and revenue growth opportunities.
   - What They Care About: Strategic growth, competitive positioning against Equinix/Digital Realty, new revenue streams, protecting and growing tenant base.
   - What Moves the Needle: "How do I compete with the big guys? What can I offer that they can't?"

**MaiaEdge Examples:** RevNet, Centra, ARK, EdgeNebula

### Pain Points (Their Language)

| Persona | Pain Points |
|---------|-------------|
| **CEO/President** | "We're stuck competing on price for space and power." "Lower attach rates, M&A positioning concerns." |
| **CFO** | "CapEx for connectivity infrastructure doesn't match our model." "ROI justification for multi-year development projects." |
| **CTO/VP Engineering** | "Investment protection — no rip-and-replace." "We're essentially in the network service provider business now but don't have the tools." |
| **VP Sales/CRO** | "Right now, I've got a piece of real estate. I don't have a product." "Third-party fabric reps are calling on my tenants." |
| **Sr. Network Engineer** | "Every cross-connect is a project — LOAs, truck rolls, VLAN config." "Once traffic leaves our facility, visibility dies." |
| **Director DC Operations** | "Power, cooling, physical security — and now network complexity." "We've built infrastructure but can't match hyperscale service expectations." |

### Value Propositions by Persona

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/President** | Compete with hyperscale fabric providers on speed without their capital investment. Move beyond space and power to recurring, high-margin revenue streams. | "Compete on interconnection without the infrastructure investment." |
| **CFO** | OpEx subscription model. Higher attach rates without infrastructure buildout. Clear payback period. | "Higher attach rates without the infrastructure buildout." |
| **CTO/VP Engineering** | "Fabric-in-a-box" simplicity without a multi-year development project. Deploy PBCs, automate cross-connects, offer cloud on-ramps under your brand. | "Fabric-in-a-box. No multi-year development project." |
| **VP Sales/CRO** | Sell interconnection services alongside space and power. Higher attach rates, faster sales, premium pricing. | "Turn 'we need 6 weeks' into 'it's live tomorrow.'" |
| **Sr. Network Engineer** | Eliminates manual cross-connect work. 1RU device, no routing protocols. Cloud PCE handles path computation. Minutes instead of weeks. | "Your team stops managing cross-connects manually." |
| **Director DC Operations** | Add connectivity services without operational complexity. Same footprint, no new protocols to manage. | "Add connectivity services without adding operational burden." |

### Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|---------------------------|----------|
| "How do you handle tenant requests for cloud connectivity?" | "We tell them to call a third-party fabric" | "We have our own cloud on-ramps" |
| "What's your revenue split: space/power vs. connectivity?" | "90% space/power, 10% cross-connects" | "Connectivity is 30%+ of revenue" |
| "When a tenant needs a cross-connect, what's the timeline?" | "Days to weeks — LOAs, truck rolls" | "Minutes, fully automated" |
| "How do you compete with Equinix for tenant retention?" | "We can't match their services" or "We lose tenants" | "We have equivalent services" |
| "What happens when tenants use Megaport for cloud connectivity?" | "We lose the revenue and relationship" | "We offer our own fabric" |

### Colocation Operator Discovery Deep Dive

After Universal questions, go deeper on colo-specific pain points.

1. "When a tenant needs a cross-connect to another tenant or carrier, what's the process and timeline?"
   - Good: "Hours per connection, LOAs, manual config, router touch required"
   - Red Flag: "We've automated this already" or "Minutes, fully self-service"

2. "How do you handle tenant requests for AWS Direct Connect or Azure ExpressRoute today?"
   - Good: "We tell them to call Megaport" or "We don't offer that"
   - Red Flag: "We have our own cloud on-ramps built out"

3. "Are you competing for tenants against Equinix or Digital Realty? How's that going?"
   - Good: "We lose on services - they win on connectivity" or "We compete on price, not capabilities"
   - Red Flag: "We're not really competing with them" or "We win most deals"

4. "Do tenants have self-service capabilities for connectivity?"
   - Good: "No, everything goes through tickets" or "They email us and we provision manually"
   - Red Flag: "Yes, full portal with instant provisioning"

5. "What's your revenue split between space/power versus connectivity services?"
   - Good: "90% space and power, maybe 10% cross-connects" or "Almost all facilities revenue"
   - Red Flag: "Connectivity is already 30%+ of revenue"

6. "When tenants ask about interconnection services you can't provide, where do they go?"
   - Good: "Megaport, Equinix Fabric... we lose that relationship" or "They figure it out themselves"
   - Red Flag: "We can provide everything they need"

7. "How many cross-connects are you processing per month? What does that cost in engineering time?"
   - Good: "Dozens, each takes hours of manual work" or "It's a bottleneck for our team"
   - Red Flag: "Fully automated, minimal touch"

8. "What happens when a tenant outgrows your facility but wants to stay connected to your ecosystem?"
   - Good: "We lose them entirely" or "No good answer for that today"
   - Red Flag: "We have multi-site interconnection capabilities"

9. "If a hyperscaler announced a new region within 50 miles, how would that change your business?"
   - Good: "Huge opportunity but we couldn't capitalize - no cloud on-ramp capability"
   - Red Flag: "We're already positioned for that"

10. "What's your biggest barrier to offering Equinix-like services under your own brand?"
    - Good: "Development cost, engineering resources, time to market" or "We'd need millions and years"
    - Red Flag: "We're already there" or "Not a priority for us"

11. "How do you handle SLA reporting for tenants today? Can you show them jitter, latency, packet loss?"
    - Good: "We can't - no visibility into network performance" or "Basic uptime only"
    - Red Flag: "Full telemetry dashboard for every tenant"

12. "Are you seeing tenants leave for facilities with better connectivity options?"
    - Good: "Yes, especially cloud-heavy workloads" or "It's becoming a problem"
    - Red Flag: "No, connectivity isn't a decision factor"

### Objection Handling

| Objection | Rebuttal | Frequency | Why They Ask |
|-----------|----------|-----------|-------------|
| "We're too small for this" | Regional operators are actually the sweet spot. You have the facilities and the tenants — you just need the fabric layer. One PBC per facility, cloud-managed. No team of 50 required. | HIGH | They see Equinix as only customer for enterprise solutions |
| "We just built a Megaport connection" | Now your tenants see Megaport's portal and build loyalty to Megaport. MaiaEdge lets you offer the same instant connectivity under YOUR brand. You keep the customer and the margin. And we integrate with Megaport via API for cloud reach. | MEDIUM | They've already made connectivity infrastructure decision |
| "Sounds expensive" | The opposite. No routing stacks, no truck rolls after PBC deployment. Subscription pricing, start at 1G, scale to 100G. One colo operator described it as building their own fabric without the development project. | MEDIUM | They're concerned about OpEx burden |

### What Change We're Asking

**Infrastructure Changes**
Deploying Path Border Controllers in your meet-me rooms — typically one PBC per facility to start, potentially more as you scale. The PBC is a 1RU device with dual 100G interfaces. It connects to your existing switching infrastructure at the meet-me room level.

**Operational Process Changes**
A cross-connect request triggers automated provisioning instead of manual work. Today: receive ticket, generate LOA, coordinate with carrier/tenant, configure VLANs, update routing, test, close. That process takes hours or days. With MaiaEdge, it takes minutes.

**Commercial Model Changes**
You're shifting from selling cross-connects as a low-margin, operationally-heavy add-on to selling connectivity as a core service line with new pricing structures, service catalogs, and SLA commitments.

**Integration Requirements**
The PCE runs in the cloud and manages your PBCs. You'll integrate via APIs with cloud fabric providers to offer cloud on-ramps under your brand. If you want tenant self-service, you'll either use the white-label portal or integrate APIs into your existing customer portal.

**Team & Skills**
You don't need BGP experts or MPLS engineers. Plan for 1-2 days of training for operations staff, half-day for sales.

### Why Change Statement

"Every day you're telling tenants 'call Megaport' is a day you're training them to build a relationship with someone else. That's not just lost margin on this transaction — it's lost control of your customer for every future connectivity need they have."

### Proof Points

- One colo operator described it as "building their own fabric without the development project"
- Another operator called it "drop it in and it works"
- Equinix Fabric validation that deterministic private paths are critical for infrastructure

### Expansion Path

- **Land:** Automated cross-connects in primary facility
- **Expand 1:** Cloud on-ramps (AWS/Azure/GCP under your brand)
- **Expand 2:** Multi-site DCI between facilities
- **Expand 3:** Federation with partner networks

---

## Segment 4: Fiber Operators

### How This Business Works

Fiber operators own regional fiber networks and sell connectivity services - both "lit" services (where they provide the electronics) and "dark fiber" (raw fiber strands the customer lights themselves). They measure their network in "route miles" - typically 500-50,000+ miles. They also lease capacity from other carriers ("Type 2 circuits") to extend their reach.

**What They Own:** Physical fiber infrastructure (buried in the ground), optical transport equipment, regional coverage. They often lease Type 2 circuits or long-haul capacity from other carriers to extend beyond their footprint.

**Revenue Model:** Dark fiber leases (IRUs), lit wavelength services, metro Ethernet, enterprise connectivity, wholesale to other carriers. The challenge: 30-70% of their fiber capacity is underutilized - stranded assets not generating revenue.

**Scale:** Typically 50-500 employees, $25M-$500M revenue, regional focus (2-10 state footprint), 500-100,000+ route miles.

**The Sovereign Middle-Mile Opportunity:** Regional fiber operators are the key to the "Sovereign Middle-Mile." Their customers aren't just enterprises — they're healthcare providers needing HIPAA-compliant paths, carriers needing partners outside their footprint for 5G slicing, and neoclouds connecting GPU clusters across regions. With MaiaEdge, regional operators can both provide sovereign routing for their customers AND maintain their own operational sovereignty.

### The Operational Reality

Fiber operators face common challenges: underutilized capacity they want to monetize, regional density they want to extend through partnerships, and enterprise customers demanding services (cloud on-ramps, multi-site connectivity) they can't deliver alone.

Every scenario requires establishing NNIs (Network-to-Network Interconnects) with partner carriers - and the only model most know is a 60-90 day manual process involving LOAs, VLAN coordination, and BGP configuration. That friction means deals are lost to whoever can provision faster.

**The Visibility Black Hole:** Once traffic leaves their network onto a Type 2 circuit or partner handoff, they're blind. They're responsible for the customer SLA but can't see the path, can't troubleshoot effectively, and can't prove performance.

### Key Personas at Fiber Operators

1. **VP Network / VP Operations** — Economic buyer, owns provisioning bottleneck (Priority #1)
   - Title Variations: VP Network, VP Network Operations, VP of Network, VP Network Services, VP Transport, VP Operations, Vice President Operations, VP Ops, VP Service Delivery, VP Network Engineering
   - Their Job: Responsible for network operations, provisioning, capacity planning, and partner carrier relationships. Manages the team that handles NNI establishment and Type 2 circuit procurement. Accountable for SLA compliance.
   - What They Care About: Reducing provisioning time (they know 60-90 days is killing deals), getting visibility into Type 2 circuits, simplifying NNI establishment, proving SLA compliance to customers.
   - What Moves the Needle: "We've turned down deals because we couldn't provision fast enough. If we could do NNIs in minutes instead of months, we'd win those deals."

2. **VP Sales / VP Business Development** — Revenue unlock, feels footprint limitation (Priority #2)
   - Title Variations: VP Sales, Vice President Sales, VP Business Development, VP BD, VP Commercial, VP Strategic Sales, SVP Sales, VP Wholesale, VP Enterprise Sales, VP Carrier Sales
   - Their Job: Sells fiber services to enterprises and carriers. Negotiates wholesale agreements. Builds partner relationships for extended reach. Their win rate drops dramatically the moment a deal requires crossing their footprint boundary.
   - What They Care About: Extending reach without building fiber, winning multi-state deals, monetizing underutilized capacity, competing with carriers who can provision faster.
   - What Moves the Needle: "We win deals inside our footprint, lose deals that require partners. Our close rate drops the moment a path crosses carrier boundaries."

3. **Director of Engineering** — Owns provisioning, technical authority (Priority #3)
   - Title Variations: Director of Engineering, Director Engineering, Dir Engineering, Director of Network, Director Network, Network Director, Director Network Engineering, Director of Transport
   - Their Job: Manages the engineering team responsible for network design, NNI establishment, and service delivery. Often the technical decision-maker for new infrastructure investments.
   - What They Care About: Simplifying network architecture, reducing manual configuration, improving provisioning velocity, maintaining visibility across owned and leased infrastructure.
   - What Moves the Needle: "I need to see end-to-end, even on paths I don't own. And I need to provision without waiting 60 days for a partner."

4. **Sr. Network Engineer / Transport Engineer** — Technical champion, hands-on pain (Priority #4)
   - Title Variations: Senior Network Engineer, Sr Network Engineer, Transport Engineer, Transmission Engineer, Optical Engineer, DWDM Engineer, Fiber Engineer, WDM Engineer, Lead Network Engineer, Staff Network Engineer
   - Their Job: Hands-on with optical transport, DWDM systems, wavelength provisioning. Configures NNIs, manages BGP peering, handles Type 2 circuit turn-up. The person who experiences the 60-90 day provisioning pain.
   - What They Care About: Eliminating manual BGP configuration, getting visibility into paths they don't control, reducing time spent on LOAs and VLAN coordination, troubleshooting faster.
   - What Moves the Needle: "Almost instantaneous" provisioning. "It simplifies processes so you can focus on making a path rather than doing all the complex networking traditionally required." — Arvig

5. **CTO** — Strategic approval, long-term vision (Escalation)
   - Title Variations: CTO, Chief Technology Officer, Chief Technical Officer, VP Technology, SVP Engineering, Chief Network Officer
   - Their Job: Sets the technology roadmap and makes strategic infrastructure decisions. At fiber operators, often involved in partnerships and platform decisions that affect competitive positioning.
   - What They Care About: Strategic differentiation, platform investments that scale, partnerships that extend reach without building fiber, positioning for M&A or growth.
   - What Moves the Needle: "Show me how this makes us more valuable - to customers, to partners, and to potential acquirers."

**MaiaEdge Examples:** Arvig, Crown Castle Fiber, Alabama Fiber Network, Ocean Networks

### Pain Points (Their Language)

| Persona | Pain Points |
|---------|-------------|
| **CEO/President** | "We own thousands of route miles but can't monetize 40% of it." "National players are winning deals in our markets." |
| **CFO** | "CapEx for expansion doesn't pencil without guaranteed utilization." |
| **COO** | "Can't scale service delivery without scaling headcount proportionally." "Every NNI is a project that consumes engineering resources." |
| **CTO** | "Protocol complexity (BGP/MPLS) requires specialized talent we can't find." "Type 2 circuits are a visibility black hole — responsible for customer but can't see the path." |
| **VP Sales/Commercial** | "6-week provisioning kills deals." "I can't sell what I can't deliver fast." "Every enterprise deal outside our region requires a partner we can't control." |
| **VP Network/Operations** | "Different systems at each location." "Manual provisioning across our own network before we even get to partners." |
| **Director Engineering** | "I need to see end-to-end, even on paths I don't own." "Every NNI is a 60–90 day project — LOAs, VLAN coordination, BGP config." |
| **Sr. Network Engineer** | "Hours per cross-connect, LOAs, VLAN coordination." "Once traffic leaves our network, we lose all visibility." |

### Value Propositions by Persona

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/President** | Transform fiber to revenue asset. New revenue streams from fiber you already own. Compete with Lumen's instant provisioning. | "New revenue streams from fiber you already own." |
| **CFO** | 80–90% reduction in provisioning OpEx. Monetize stranded capacity. Turn fiber into deterministic services. | "80–90% reduction in provisioning OpEx." |
| **COO** | Scale service delivery without scaling headcount. Automated provisioning eliminates manual NNI work. | "Scale service delivery without scaling headcount." |
| **CTO** | No MPLS or routing protocols to manage. End-to-end visibility across Type 2 circuits. Protocol-free forwarding eliminates configuration drift. | "No MPLS or routing protocols to manage." |
| **VP Sales/Commercial** | Win deals you're currently losing on provisioning timelines. What takes weeks today, your team does in minutes. | "Win deals you're currently losing on speed." |
| **VP Network/Operations** | Unify fiber islands into one automated fabric first. Then extend automation to partners. PBCs at internal boundaries and external handoffs. | "Unify your fiber islands into one automated fabric." |
| **Director Engineering** | Provision without waiting 60 days for a partner. Hop-by-hop visibility across network boundaries. Eliminate manual BGP configuration. | "Provision without waiting 60 days for a partner." |
| **Sr. Network Engineer** | Minutes instead of weeks. Automated provisioning eliminates manual config. Real-time visibility across every hop. | "What used to take weeks is now almost instantaneous." |

### Fiber Operator Discovery Deep Dive

After Universal questions, go deeper on fiber-specific pain points.

1. "What percentage of your fiber is actually generating revenue right now?"
   - Good: "30-50%... we have a lot of stranded capacity" or "Not enough"
   - Red Flag: "85%+ utilized" or "Capacity is our constraint"

2. "When you need to extend reach through NNIs or partner carriers, what does that look like?"
   - Good: "60-90 day process... we've turned down deals because of it"
   - Red Flag: "We have automated NNI establishment"

3. "How do you handle Type 2 circuits? What visibility do you have?"
   - Good: "It's a black hole... responsible for SLAs but can't see the path"
   - Red Flag: "Full visibility through our OSS"

4. "Are you losing deals because you can't deliver outside your footprint fast enough?"
   - Good: "Yes, multi-state deals especially" or "All the time"
   - Red Flag: "No, we have strong partner relationships that move fast"

5. "How many route miles do you own versus lease? What's the visibility difference?"
   - Good: "Own X thousand, lease significant portion... can't see leased paths"
   - Red Flag: "All owned" or "Full visibility regardless"

6. "When an enterprise RFP requires coverage beyond your footprint, what happens?"
   - Good: "We either pass or quote 60-90 days and lose to faster competitors"
   - Red Flag: "We win those regularly"

7. "What does your NNI establishment process look like today? Walk me through a recent one."
   - Good: "LOAs, VLAN coordination, BGP config, testing... weeks of back and forth"
   - Red Flag: "API-driven, days not weeks"

8. "How do you prove SLA compliance to customers when the path crosses partner networks?"
   - Good: "We can't really - we just hope it works" or "It's a gap"
   - Red Flag: "End-to-end monitoring regardless of path"

9. "Are you seeing enterprises ask for cloud on-ramps as part of fiber deals?"
   - Good: "Constantly - and we have to partner or lose the deal"
   - Red Flag: "We have native cloud connectivity"

10. "What would it mean for your sales team if NNIs took minutes instead of months?"
    - Good: "We could compete for deals we're currently passing on" or "Huge"
    - Red Flag: "Not a major issue for us"

11. "How do you handle failover when a path includes Type 2 circuits?"
    - Good: "Manual process, no automatic rerouting across carrier boundaries"
    - Red Flag: "Automated failover across all path types"

12. "When a customer reports performance issues on a path that crosses partner networks, how do you troubleshoot?"
    - Good: "Open tickets with each carrier and wait... no unified visibility"
    - Red Flag: "Single pane of glass across all paths"

### Objection Handling

| Objection | Rebuttal | Frequency | Why They Ask |
|-----------|----------|-----------|-------------|
| "We just invested in MPLS" | MaiaEdge sits at the edge and complements your core. No rip-and-replace. Deploy PBCs at boundaries where automation stops today. Your MPLS core continues running. | HIGH | Sunk cost fallacy - protecting previous investment |
| "Our NNI process works fine" | How long? 60–90 days? How many deals are you losing to provisioning delays while competitors do it in minutes? One fiber operator we work with went from 60-day NNIs to same-day activation. | HIGH | They've normalized slow and accepted status quo |
| "Can't justify the investment" | Start with one PBC pair. Prove the value on a single partner connection. If same-day NNI activation doesn't change your win rate, we'll know fast. | MEDIUM | Cost-conscious about infrastructure investments |

### What Change We're Asking

**Infrastructure Changes**
You're deploying PBCs at strategic points in your network: your major PoPs, carrier hotels where you peer, and critically, at the boundaries where your network meets partner networks or Type 2 circuits. For a regional fiber operator with 10-20 key sites, that's typically 10-20 PBCs to start.

**Operational Process Changes**
Your NNI establishment process changes fundamentally. Today it's: negotiate agreement, exchange LOAs, coordinate VLAN assignments, configure BGP peering, test, document, go live — 60-90 days of back-and-forth. With MaiaEdge, both you and your partner deploy PBCs at the interconnection point. Federation happens through the PCE — path establishment is minutes, not months.

For Type 2 circuits, the change is about visibility. Today, once traffic leaves your network, you're blind. With PBCs at each boundary, you get hop-by-hop telemetry across the entire path — including portions you don't own.

**Commercial Model Changes**
This enables new services: guaranteed fast provisioning, multi-state coverage through federation, SLA-backed services across Type 2 circuits, premium tiers with real-time visibility dashboards for customers.

**Integration Requirements**
The PCE integrates with your existing OSS/BSS via APIs. Service orders trigger path provisioning automatically; lifecycle events flow back to your billing system. For carriers standardized on MEF LSO Sonata, we're working directly with Mplify on that integration.

**Team & Skills**
Your network engineers don't need to learn new routing protocols — the platform eliminates that complexity. They need to understand path management through the PCE, how federation works, and how to interpret the new telemetry data.

### Why Change Statement

"Every multi-state deal you lose because you can't activate partners fast enough is revenue walking out the door. Your fiber is a valuable asset - but only if you can sell it before the customer moves on to whoever says 'yes' faster."

### Proof Points

- Arvig (MN): "Almost instantaneous" provisioning, "simplifies processes so you can focus on making a path rather than doing all the complex networking traditionally required"
- Arvig: "A whole new way to look at our existing network and end-to-end information on how a circuit's performing"
- Ocean Networks (Hawaii): Inter-island fiber connectivity, federation to mainland carriers

### Expansion Path

- **Land:** Internal network simplification (site-to-site connectivity)
- **Expand 1:** Fiber monetization (dark fiber as deterministic services)
- **Expand 2:** Partner NNIs (federation with adjacent operators)
- **Expand 3:** Cloud on-ramps (AWS/Azure/GCP under your brand)

---

## Segment 5: Network Operators (Tier 1/2 Carriers)

### How This Business Works

Large national or international service providers with complex, distributed networks. May own extensive infrastructure (traditional carriers) or operate virtually on leased infrastructure (VNOs). Key characteristic: scale and multi-domain complexity.

**What They Own:** Traditional Carriers: 10,000–100,000+ route miles, 100–1,000+ PoPs. VNOs: Minimal/no owned fiber, software-defined overlays.

**Revenue Model:** Enterprise connectivity, MPLS services, wavelengths, IP transit, managed services. High-margin enterprise deals.

**Scale:** 1,000–50,000+ employees, $500M–$50B+ revenue, national or global footprint.

**Competitive Reality:** Even internal automation may be fragmented across domains. Cross-carrier paths still manual. Enterprise customers expect AWS/Azure-like provisioning speed.

### CRITICAL: Two Messaging Tracks

Network Operators require research to determine which messaging track to use. The key question: **Do they have internal automation already?**

| Signal | Indicates | Track |
|--------|-----------|-------|
| Branded self-service portal (NetBond, Express Waves, SDI) | Internal automation exists | **TRACK A: External Extension** |
| API documentation publicly available | Internal automation exists | **TRACK A** |
| "Instant provisioning" in their marketing | Internal automation exists | **TRACK A** |
| No portal, no API docs, manual quoting process | Internal automation lacking | **TRACK B: Internal + External Unification** |
| Multiple acquisitions with separate systems | Internal fragmentation | **TRACK B** |
| Job postings for "network automation" roles | Building automation, not there yet | **TRACK B** |

### Track A: External Extension (Has Internal Automation)

**CRITICAL:** Never claim they're slow at what they're fast at. Acknowledge what they've built FIRST.

**Primary Hook:** "You've automated internally. MaiaEdge extends that automation everywhere else."

**Core Problem:** Internal automation stops at domain boundaries. Cross-carrier paths still take weeks. Customer expectations set by AWS/Azure instant provisioning.

**Pain Points (Track A):**

| Persona | Pain Points |
|---------|-------------|
| **CEO/Strategy** | "Lumen and AWS just announced direct enterprise connectivity. We need to match that experience." "Cross-carrier deals are profitable but operationally painful." |
| **VP Network Strategy** | "We've automated internally, but anything beyond our footprint still takes weeks." "The gap is cross-carrier, not internal." |
| **VP Sales** | "Enterprise team can only sell connectivity on-net." "Cross-carrier deals take too long to close." |
| **VP Product** | "Productizing cross-carrier paths requires a multi-year dev cycle." "Can't match AWS/Lumen instant provisioning experience." |

**Value Props (Track A):**

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/Strategy** | Extend your competitive moat beyond your network boundary. Same automation you've built internally, extended to partners instantly. | "Your automation stops at your border. MaiaEdge extends it everywhere." |
| **VP Network Strategy** | Federation layer that extends automation across partner boundaries. PBCs at the edges where your automation currently stops. | "Your automation stops at your border. Extend it across every partner." |
| **VP Sales** | Sell off-net paths at on-net speed. Enterprise team stops saying no to deals outside your footprint. | "Sell off-net at on-net speed." |
| **VP Product** | Ship cross-carrier products without a multi-year dev cycle. MaiaEdge is the federation layer — your existing systems stay in place. | "Ship cross-carrier products without the dev cycle." |

### Track B: Internal + External Unification (No Internal Automation)

**Primary Hook:** "Unify internally first, then extend externally. One infrastructure for both."

**Core Problem:** Multi-domain orchestration is complex even within their own network. Different systems across domains mean manual handoffs.

**Pain Points (Track B):**

| Persona | Pain Points |
|---------|-------------|
| **CEO/Strategy** | "Multi-domain complexity is our biggest operational cost center." "Enterprise customers expect AWS-like provisioning. We're still quoting weeks." |
| **VP Network Strategy** | "Multi-domain orchestration is complex even within our own network." "Different systems across domains mean manual handoffs." |
| **Principal Network Architect** | "We need to unify before we can federate." "Integration complexity across acquired networks." |
| **VP Sales** | "Provisioning timeline varies by which domains are involved." "Can't give customers a consistent experience." |

**Value Props (Track B):**

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/Strategy** | One infrastructure that unifies your internal domains AND extends to partners. Streamline internally, then federate externally. | "Unify your network, then extend your reach. Same infrastructure for both." |
| **VP Network Strategy** | Single fabric layer across all internal domain boundaries. Then the same infrastructure extends to partners. No separate systems. | "Unify your domains first, then federate everywhere." |
| **Principal Architect** | PBCs at internal boundaries and external handoffs. Centralized path computation across all domains. One control plane. | "One control plane across all your domains, internal and external." |
| **VP Sales** | Consistent provisioning experience regardless of which domains are involved. Then extend that speed to cross-carrier. | "Same speed everywhere, on-net and off-net." |

### Network Operator Discovery (Both Tracks)

| Question | Good Answer (Buying Signal) | Determines Track |
|----------|---------------------------|------------------|
| "Is your internal automation unified across all network domains?" | "We have pockets of automation, but it's not unified." | → Track B |
| "Is your internal automation unified across all network domains?" | "Yes, internally we're automated. The gap is cross-carrier." | → Track A |
| "What's your provisioning timeline for enterprise requests?" | "Still quoting weeks... customers compare us to cloud" | Either track |
| "How do you handle multi-carrier paths today?" | "Painful — LOAs, manual coordination, weeks" | Either track |
| "Do you have a self-service portal or API for provisioning?" | "Yes, for on-net." | Track A (gap is off-net) |
| "When you need to activate a new PoP, what does that process look like?" | "Months — BGP configuration, MPLS setup, testing" | Track B |

#### Deeper Network Operator Discovery

1. "When you need to activate a new PoP, what does that process look like? Timeline?"
   - Good: "Months... BGP configuration, MPLS setup, testing across domains"
   - Red Flag: "Days - we've automated PoP activation"

2. "How do you handle multi-domain orchestration? What happens at domain boundaries?"
   - Good: "It's complex... manual coordination, different teams, different tools"
   - Red Flag: "Unified orchestration across all domains"

3. "What's your mix of owned vs. leased infrastructure? How do you manage visibility across both?"
   - Good: "Significant leased component... visibility stops at our edge"
   - Red Flag: "Full visibility regardless of ownership"

4. "Are customer expectations changing? Asking for more on-demand, cloud-like provisioning?"
   - Good: "Absolutely... they want instant, we're still at weeks/months"
   - Red Flag: "We're already delivering on-demand"

5. "How much have you invested in OSS/BSS? Where does automation stop?"
   - Good: "Millions... but it stops at domain boundaries" or "Inside domains only"
   - Red Flag: "End-to-end automation across all domains"

6. "What protocols are you running today? BGP, MPLS, OSPF? How's that complexity impacting operations?"
   - Good: "All of the above... requires specialized expertise at every hop"
   - Red Flag: "We've simplified our protocol stack"

7. "When you acquire a new network or merge domains, what does integration look like?"
   - Good: "Years of work... different systems, different protocols, different teams"
   - Red Flag: "We have a standard integration playbook that takes months"

8. "How do your enterprise customers compare your provisioning speed to cloud providers?"
   - Good: "Unfavorably - they expect AWS-like instant and we deliver in weeks"
   - Red Flag: "We're competitive with cloud"

9. "What's your biggest operational bottleneck for service activation?"
   - Good: "Cross-domain coordination, protocol configuration, testing"
   - Red Flag: "No major bottlenecks"

10. "If you could activate a new PoP in days instead of months, what would that mean for your expansion plans?"
    - Good: "Accelerate growth significantly, faster time to revenue"
    - Red Flag: "Not a priority - we're not expanding aggressively"

11. "How do you handle wavelength services across your network? What's the provisioning timeline?"
    - Good: "Still manual, still weeks" or "Complex coordination required"
    - Red Flag: "Automated, same-day provisioning"

12. "Are you competing with hyperscalers for enterprise connectivity? How's that going?"
    - Good: "Losing on speed - they provision instantly, we can't match it"
    - Red Flag: "We're winning" or "Different market"

### Network Operator Objection Handling

| Objection | Rebuttal | Frequency | Why They Ask |
|-----------|----------|-----------|-------------|
| "We've already invested heavily in automation" | And it works — internally. But what about cross-carrier? Enterprise customers don't see your network boundary; they see provisioning timelines. MaiaEdge extends what you've built to everywhere else. | HIGH | Sunk cost protection |
| "This sounds like it overlaps with our SDN strategy" | MaiaEdge complements SDN. Your SDN handles internal path optimization. MaiaEdge handles cross-network federation — the boundary where your SDN stops and partner complexity begins. | MEDIUM | Jurisdictional concern about strategic initiatives |
| "We're a Tier 1 — we don't need edge devices" | MaiaEdge PBCs sit at the boundaries between YOUR network domains and partner networks. Same team that built Acme Packet and 128 Technology. Why rebuild what exists? | MEDIUM | Scale/status concern |
| "Just invested in Cisco/Juniper infrastructure" | We're not asking you to replace that investment. MaiaEdge sits at the edge, alongside your Cisco and Juniper equipment. Your core routers keep doing what they do. What we add is capabilities your existing infrastructure can't provide. NTT deployed MaiaEdge for network simplification without replacing their core. | HIGH | Sunk cost fallacy |
| "Can you handle our scale? We have 100+ PoPs." | Absolutely. IENTC in Mexico is using MaiaEdge to connect over 800 cell towers to more than 20 data centers. NTT is deploying across their global network. The architecture is designed for scale. | MEDIUM | Legitimate scale concern |
| "How does this integrate with our existing OSS/BSS?" | MaiaEdge is designed to fit into your existing operational stack, not replace it. The PCE exposes APIs that integrate with your BSS, OSS, and service orchestration systems. Your existing ordering systems trigger path provisioning, and service lifecycle events flow to your billing system. | HIGH | Integration complexity concern |
| "What about security and compliance requirements?" | Security is built in, not bolted on. Every path is encrypted end-to-end with line-rate AES-256-GCM IPsec - no performance penalty, no throughput degradation. Multi-tenant isolation uses Q-in-Q tagging so every customer remains completely separated. | MEDIUM | Enterprise/regulated customer concern |
| "We're in the middle of a network transformation project" | That might actually be perfect timing. Most transformations stall at the edge - where your OSS/BSS meets partner networks and customer handoffs. MaiaEdge is the missing layer that makes your transformation actually reach the edge. | MEDIUM | Timing objection |

### What Change We're Asking

**Infrastructure Changes**
At your scale, deployment is measured in dozens to hundreds of PBCs across your network. Typical placement: every major PoP, every domain boundary, every location where you hand off to partners or take handoffs from underlying carriers. For mobile backhaul use cases, PBCs deploy at aggregation points connecting to cell tower infrastructure.

**Operational Process Changes**
Activating a new PoP changes from "months of work involving network architecture, engineering, and operations" to "rack the PBC, connect it to your infrastructure, register it with the PCE."

For services that don't need the full complexity of your MPLS infrastructure - basic point-to-point connectivity, cloud on-ramps, partner hand-offs - traffic can flow over MaiaEdge paths instead. You're not replacing MPLS; you're offloading the services where MPLS is overkill.

**Integration Requirements**
This is critical at carrier scale. The PCE exposes APIs that integrate with your BSS, OSS, and service orchestration systems. Your existing ordering systems trigger path provisioning; lifecycle events flow to your operational systems and billing.

**Commercial Model Changes**
You can now offer: on-demand provisioning matching cloud provider speed, SLA-backed services across infrastructure you don't fully own, faster time-to-revenue on new PoPs and new markets, simplified enterprise connectivity products.

**Team & Skills**
Your network engineers don't need to unlearn BGP and MPLS - those skills still matter for your core infrastructure. What changes is that edge services no longer require that expertise. Junior engineers can provision paths that previously required senior network architects.

### Why Change Statement

"Your enterprise customers are comparing you to AWS and Azure — they expect provisioning in minutes, not weeks. Every day the gap between their expectations and your delivery time widens, you're training them to look elsewhere for connectivity."

### Proof Points

- NTT: Network simplification, PoP acceleration — Tier 1 carrier validation
- IENTC (Mexico): Mobile backhaul connecting cell towers to data centers at scale
- Tier 1 carriers validating the technology at scale

### Expansion Path

- **Land:** DCI between data centers (internal simplification)
- **Expand 1:** New PoP activation (faster time-to-revenue)
- **Expand 2:** Mobile backhaul (cell tower connectivity)
- **Expand 3:** Federation with partner networks

---

## Segment 6: MSP/Aggregators

### How This Business Works

MSPs aggregate and resell connectivity from multiple carriers. They don't own significant infrastructure — their value is in the carrier relationships, multi-source pricing, and managed service wrapper. Their model is asset-light: contracts, not fiber.

**What They Own:** Contracts with carriers, customer relationships, service management platforms. Minimal or no physical infrastructure.

**Revenue Model:** Margin on resold connectivity (10–30%), managed services fees, implementation/professional services.

**Scale:** 50–500 employees, $20M–$500M revenue, 3+ carrier relationships.

**Competitive Reality:** Tier 1 carriers are going direct to enterprise customers, cutting out MSPs. MSPs can't match direct carrier speed or visibility, and struggle to prove SLA compliance independently.

### Key Personas at MSP/Aggregators

1. **VP Operations / COO** — Service delivery owner, feels carrier dependency (Priority #1)
   - Title Variations: VP Operations, Vice President Operations, COO, Chief Operating Officer, VP Service Delivery, VP Ops, SVP Operations, VP Client Operations, VP Managed Services Operations
   - Their Job: Owns service delivery, carrier relationships, and operational efficiency. Manages the team that coordinates across multiple underlying carriers. Accountable for SLA compliance but lacks the tools to enforce it.
   - What They Care About: Reducing carrier dependencies, getting visibility into networks they don't own, speeding up provisioning timelines, reducing finger-pointing when things break.
   - What Moves the Needle: "You own the customer relationship but wait weeks for circuits. MaiaEdge treats all your carriers as one fabric - instant provisioning, end-to-end visibility, OpEx model."

2. **VP Product / CTO** — Platform strategy, differentiation (Priority #2)
   - Title Variations: VP Product, VP of Product, CTO, Chief Technology Officer, VP Platform Strategy, VP Technology, Chief Product Officer, VP Product Management, VP Solutions
   - Their Job: Defines the service portfolio and platform roadmap. Looks for ways to differentiate from other MSPs and compete with Tier 1s. Evaluates technology that could change the competitive equation.
   - What They Care About: Competitive differentiation, new service capabilities, reducing time-to-market for new offerings, matching Tier 1 provisioning speed.
   - What Moves the Needle: "Tier 1 carriers are going direct to your enterprise customers with instant connectivity. MaiaEdge is how you match that - without owning fiber."

3. **Director of Carrier Relations** — Manages carrier partnerships (Priority #3)
   - Title Variations: Director of Carrier Relations, Director Carrier Relations, Carrier Relations Manager, Director of Vendor Management, Director of Partner Operations, Director of Supplier Management, VP Carrier Relations
   - Their Job: Manages relationships with underlying carriers, negotiates contracts, coordinates service delivery across multiple providers. Often the person who feels provisioning pain most acutely.
   - What They Care About: Simplifying carrier coordination, reducing provisioning dependencies, getting better visibility into carrier performance, streamlining multi-carrier service delivery.
   - What Moves the Needle: "I spend half my time chasing carriers for updates. If I could see the path myself and provision without waiting, that changes everything."

4. **Solutions Architect** — Multi-vendor integration, technical evaluation (Priority #4)
   - Title Variations: Solutions Architect, Solution Architect, Pre-Sales Architect, Technical Solutions Architect, Integration Architect, Platform Architect, Customer Solutions Architect, Enterprise Architect, Network Solutions Architect
   - Their Job: Designs solutions that span multiple carriers, integrates various vendor systems, handles the technical complexity of multi-carrier service delivery. The person who lives the "stitching together" reality daily.
   - What They Care About: Simplifying multi-carrier integration, unified management plane, reducing manual coordination, having data to troubleshoot when things break.
   - What Moves the Needle: "MaiaEdge treats owned fiber, leased capacity, and DIA as a single cohesive fabric under one control plane. You get hop-by-hop visibility across networks you don't own."

5. **Director of Engineering** — Integration owner, technical authority (Priority #5)
   - Title Variations: Director of Engineering, Director Engineering, Director of Integration, Director of Network Engineering, Director IT Engineering, VP Engineering, Director Platform Engineering
   - Their Job: Manages engineering team responsible for platform integration, service automation, and technical operations. Key decision-maker for infrastructure investments.
   - What They Care About: End-to-end visibility, troubleshooting across carriers, platform integration capabilities, reducing technical debt from manual processes.
   - What Moves the Needle: "We've built so much custom automation to work around carrier limitations. Show me something that actually solves the underlying problem."

**MaiaEdge Examples:** INDATEL, 11:11 Systems, Granite

### Pain Points (Their Language)

| Persona | Pain Points |
|---------|-------------|
| **CEO/President** | "Tier 1s are cutting us out. They're going direct to our customers with instant provisioning." "Our model depends on being faster and easier than going direct — but we're not." |
| **VP Operations** | "When something breaks, it's 3 carrier tickets and a week of finger-pointing." "We can't independently verify SLA compliance." |
| **VP Business Development** | "Onboarding a new carrier partner takes months." "We can't extend reach fast enough to win multi-region deals." |
| **VP Sales** | "Our provisioning is slower than going direct to the carrier. That's a problem." |

### Value Propositions by Persona

| Persona | Value Proposition | Impact Line |
|---------|-------------------|-------------|
| **CEO/President** | Tier 1 capabilities without Tier 1 infrastructure. Compete on speed and visibility while staying asset-light. | "Tier 1 capabilities, asset-light model." |
| **CFO** | Eliminate 40–60% CapEx burden. Better cash flow, improved unit economics. | "Shift from CapEx depreciation to predictable OpEx." |
| **VP Operations** | End-to-end visibility across all carrier relationships. Hop-by-hop telemetry, prove SLAs to customers. Stop the finger-pointing. | "Hop-by-hop visibility across all carriers — prove SLA compliance." |
| **VP Business Development** | Federation in minutes. Instant partner activation. Extend reach without building fiber. | "Federation in minutes, instant partner activation." |
| **VP Sales** | Instant activation instead of "depends on the carrier." Faster closes, same-day provisioning. Competitive with Tier 1s on speed. | "Instant activation instead of 'depends on the carrier.'" |

### MSP/Aggregator Discovery Deep Dive

After Universal questions, go deeper on MSP-specific pain points.

1. "How many underlying carriers do you work with? What does coordination look like?"
   - Good: "3-10 carriers... every circuit requires manual stitching"
   - Red Flag: "Automated orchestration across all carriers"

2. "When there's an outage, how do you troubleshoot across carrier networks?"
   - Good: "We're blind... responsible for SLA but can't see inside their networks"
   - Red Flag: "Visibility into all carrier paths"

3. "Are Tier 1 carriers going direct to your enterprise customers?"
   - Good: "Yes, they're offering instant connectivity we can't match"
   - Red Flag: "Not a threat to our business"

4. "What would it mean if you could offer the same provisioning speed as Tier 1s?"
   - Good: "Game changer... we win on relationships but lose on speed"
   - Red Flag: "We're already competitive on speed"

5. "When a customer needs a new circuit, what's your timeline versus what carriers quote direct?"
   - Good: "We're slower - we have to coordinate across multiple providers"
   - Red Flag: "Same or faster than direct"

6. "How do you differentiate when you're reselling the same underlying infrastructure as competitors?"
   - Good: "Service and relationships... but that only goes so far"
   - Red Flag: "Unique capabilities they can't match"

7. "What percentage of your margin goes to underlying carriers versus your managed services?"
   - Good: "Too much to carriers - that's commoditized, services are where we make money"
   - Red Flag: "Healthy margin on connectivity"

8. "When carriers change their pricing or terms, how does that impact your business?"
   - Good: "Significant - we're at their mercy" or "Constant pressure"
   - Red Flag: "Minimal impact, diversified"

9. "How do you handle SLA guarantees when you don't control the underlying network?"
   - Good: "It's a risk - we're on the hook but can't see or control the path"
   - Red Flag: "Contractual flow-down protects us"

10. "If you could see hop-by-hop telemetry across all your carrier partners, what would that change?"
    - Good: "Everything - we could actually troubleshoot, prove SLAs, hold carriers accountable"
    - Red Flag: "We already have that visibility"

11. "Are you losing deals to carriers who can provision faster than your multi-carrier coordination allows?"
    - Good: "Regularly - speed wins, and we're structurally slower"
    - Red Flag: "No, speed isn't the deciding factor"

12. "What's your strategy for competing as carriers build more direct-to-enterprise capabilities?"
    - Good: "That's the existential question... we need something they can't easily replicate"
    - Red Flag: "We have a clear differentiation strategy"

### MSP/Aggregator Objection Handling

| Objection | Rebuttal | Frequency | Why They Ask |
|-----------|----------|-----------|-------------|
| "We're asset-light — we don't want infrastructure" | MaiaEdge is OpEx, not CapEx. You're not building infrastructure — you're adding a visibility and control layer over your existing carrier relationships. Same asset-light model, better capabilities. | HIGH | Fundamental model question |
| "Our carrier relationships work fine" | But can you see inside their networks? Can you prove SLA compliance independently? Can you provision as fast as if the customer went direct? MaiaEdge gives you visibility and speed without replacing your carrier relationships. | HIGH | Defending status quo |
| "This is expensive for our margins" | What's the cost of losing deals to Tier 1s who can provision faster? What's the cost of finger-pointing during outages? MaiaEdge protects your customer relationships by making you faster and more transparent than the alternative. | MEDIUM | Cost-conscious about margin impact |

### What Change We're Asking

**Infrastructure Changes**
You deploy PBCs at your demarcation points - the locations where you take handoffs from your underlying carriers. This is typically your colo space, your PoPs, or anywhere you have physical presence at the carrier boundary. You're not deploying on carrier networks; you're deploying on your side of the handoff, in space you already control.

For an MSP working with 5-10 carriers, that might mean 10-30 PBCs at key handoff locations across your service area.

**Operational Process Changes**
This is transformational for the MSP model. Today, when a customer reports an issue on a circuit that crosses three carriers, you're blind and opening tickets. With PBCs at each carrier boundary, you get hop-by-hop telemetry across the entire path.

Your provisioning process changes too. Today it's coordinating across fragmented carrier systems. With MaiaEdge, you have unified orchestration across your carrier relationships — a single control plane instead of bouncing between carrier portals.

**Commercial Model Changes**
The visibility changes what you can sell: tighter SLA commitments, premium tiers with customer-facing dashboards, faster provisioning, value-add services built on visibility.

**Integration Requirements**
The PCE integrates with your existing systems via APIs. If you have a customer portal, you can surface path status and telemetry there. If you have ticketing systems, alerts can create tickets automatically.

**Team & Skills**
Your NOC team gets tools they've never had. Instead of "we opened a ticket with the carrier and we're waiting," they can say "we see the issue is in Carrier B's segment between Chicago and Detroit, we've already escalated with specifics."

**Carrier Relationship Implications**
When you have visibility into carrier performance, your conversations with carriers change. You have data. You can hold them accountable to SLAs with evidence.

### Why Change Statement

"Tier 1 carriers are going direct to your enterprise customers with instant, self-service connectivity. You win on relationships and service - but you're losing on speed and visibility. MaiaEdge lets you match their capabilities while keeping what makes you different."

### Proof Points

- INDATEL: Rural aggregator model, multi-carrier orchestration across member networks
- 11:11 Systems: Managed services provider validating unified visibility use case

### Expansion Path

- **Land:** Visibility across 2-3 primary carrier relationships
- **Expand 1:** All carrier relationships under single control plane
- **Expand 2:** Major customer sites (extend visibility to customer edge)
- **Expand 3:** Self-service portal for enterprise customers

---

## Segment 7: Enterprise (Dark Fiber / Private WAN)

### How This Business Works

Large enterprises that own or lease dark fiber or private WAN infrastructure for internal use. They are NOT selling connectivity services — the network exists to serve their own operations. This is a LOW PRIORITY segment because deal sizes are smaller and sales cycles are longer.

**Who Qualifies:** Universities with campus fiber networks, healthcare systems with inter-facility fiber, financial services firms with private trading networks (HFT), utilities with SCADA/grid networks, government/military with private networks.

**What They Own:** Dark fiber (IRU or owned), private WAN infrastructure, campus networks. May lease some capacity.

**Revenue Model:** Internal cost center. Network is an operational expense, not a revenue line.

**Pain Points:** Manual provisioning, VLAN complexity, project bottlenecks, limited visibility across leased segments.

**Value Proposition:** Cloud-like agility on infrastructure you already own. Provision paths in minutes for internal projects without routing protocol complexity.

**Why Low Priority:** Smaller deal sizes, longer enterprise procurement cycles (6–12 months), network is cost center not revenue center, harder to quantify ROI.

---

## Account Tiering Logic

| Tier | Criteria | Action |
|------|----------|--------|
| **Tier 1 (High Priority)** | Colo + Mid-Size + Hyperscaler <50mi OR Leadership Change; Neocloud with 5+ facilities; Fiber Operator in AI Corridor with stranded capacity | Active outreach, multi-touch sequence, executive engagement |
| **Tier 2 (Standard)** | Fiber/Colo + Mid-Size OR Network Operator + Large scale; Neocloud 2–4 facilities; MSP/Aggregator with significant scale | Standard outreach sequence, monitor for trigger events |
| **Tier 3 (Low Priority)** | Small scale OR MSP/Enterprise segments; Early-stage neocloud; Fiber operator outside AI corridors | Nurture, trigger-based outreach only |
| **Tier 4 (Disqualify)** | Software/Platform Vendors, Other/Unknown, outside North America (for now), matches any Exclusion criteria | No outreach — mark as excluded in HubSpot |

---

## Confidence Thresholds for Segmentation

| Confidence Level | Segments | Notes |
|-----------------|----------|-------|
| **High (90%+)** | Colocation Operator (very distinct keywords); Service Provider vs. Enterprise (clear business model difference); Fiber Operator with published route miles <10K | Classification reliable for automation |
| **Medium-High (80–89%)** | MSP/Aggregator (language patterns strong); Carrier/VNO with 10+ state coverage; Fiber Operator vs. Carrier (when route miles published) | Reliable but verify edge cases |
| **Medium (70–79%)** | Dark Fiber Enterprise (relies on news/press releases); Carrier/VNO vs. Fiber Operator (when route miles NOT published — use employee count as proxy) | Flag for manual review |
| **Low (<70%)** | Missing critical data (no services page, minimal web presence); Conflicting signals (MSP language + owned fiber); Company doesn't fit any pattern | Requires human classification |

### Flag for Manual Review When:

- No clear services page or website under construction
- Conflicting indicators (says "MSP" but mentions owned fiber)
- Company recently acquired — check parent company
- Very small headcount but significant infrastructure signals
- Software vendor with possible operator division
- "Consulting" firm that may also operate infrastructure

---

## Persona Classification Quick Reference

### Decision-Makers / Economic Buyers

| Titles | Primary Concerns |
|--------|-----------------|
| CEO, President, Managing Director, General Manager | Revenue growth, competitive positioning, M&A value |
| CFO, Chief Financial Officer, VP Finance | CapEx burden, cash flow, ROI, cost reduction |
| CRO, Chief Revenue Officer, VP Sales | Long sales cycles, losing deals on speed |
| COO, Chief Operating Officer | Operational efficiency, headcount, scale |

### Technical Contacts

| Titles | Primary Concerns |
|--------|-----------------|
| CTO, VP Engineering, VP Technology, VP Infrastructure | Protocol complexity, talent scarcity, architecture decisions |
| VP Network, VP Network Strategy, VP Network Architecture | Multi-domain orchestration, automation boundaries |
| Director Engineering, Director Network Engineering | Provisioning velocity, visibility, simplifying architecture |
| Sr. Network Engineer, Lead Network Engineer, Network Architect | Manual work, LOAs, VLAN coordination, troubleshooting |
| Principal Network Architect, Senior Network Architect | Technical validity, integration, scalability |

### Commercial Contacts

| Titles | Primary Concerns |
|--------|-----------------|
| VP Sales, VP Commercial, VP Business Development | Deal velocity, win rates, extending reach |
| VP Product, VP Product Management | Roadmap acceleration, time-to-market |
| Director Sales, Sales Director | Provisioning killing deals, competitive positioning |
| Director Business Development, VP Partnerships | Partnership friction, extending reach |

---

## Messaging Guardrails

### Infrastructure vs. NaaS — Quick Check

Before sending any message, verify:

| CORRECT (Infrastructure) | WRONG (Sounds like NaaS) |
|--------------------------|--------------------------|
| "Build your own fabric" | "Connect to our fabric" |
| "Infrastructure you deploy" | "Subscribe to our network" |
| "Your brand, your invoice" | "Join our ecosystem" |
| "Keep the customer and margin" | "Access our platform" |
| "Maintain sovereignty" | "Our network provides..." |

### Speed Claims — Quick Check

Speed claims must be paired with ownership language:

| WRONG (NaaS-sounding) | CORRECT (Infrastructure) |
|------------------------|--------------------------|
| "Provision in minutes" | "Your team provisions in minutes" |
| "Instant activation" | "Enable instant activation under your brand" |
| "On-demand connectivity" | "Offer on-demand through your portal" |
| "We reduce weeks to minutes" | "What takes weeks, your team does in minutes" |

### Customer References — Usage Rules

| Context | Named References OK? |
|---------|---------------------|
| Cold emails / LinkedIn | NEVER |
| Discovery calls (after engagement) | YES |
| Demos and proposals | YES |
| "Who else is using this?" objection | YES |
| Trade show conversations | YES |

**Credibility without name-dropping:** The founding team credibility IS appropriate in cold outreach: "Same team that built Acme Packet and 128 Technology" — this is company credibility, not customer name-dropping.

### Proof Points (Anonymized for Cold Outreach)

| Segment | Anonymized Proof Point |
|---------|----------------------|
| Colo (Standard) | "One colo operator described it as building their own fabric without the development project" |
| Colo (Standard) | "An operator we work with called it 'drop it in and it works'" |
| Colo — AI Infrastructure | "Even major fabric providers have validated the architecture" |
| Neoclouds | (Emerging segment — use general deterministic path messaging) |
| Fiber Operator | "A regional fiber operator went from 60-day NNIs to same-day activation" |
| Network Operator | "Tier 1 carriers are using this for network simplification" |
| MSP/Aggregator | "We're enabling multi-carrier orchestration at scale" |

---

## Sales Execution Reference

### Part 2: Sales Execution — Discovery & Objection Handling

This section is your in-call reference material. Use these discovery questions, objection handlers, and playbooks during live conversations.

### Universal Discovery Questions

**Start Here - Get Them Talking**

1. "Walk me through how a new enterprise site or cloud region gets connected today - from the first customer request to traffic actually flowing."
   - Good: "30-90 days... LOAs, VLAN coordination, BGP config, waiting on partners, multiple teams involved..."
   - Red Flag: "Pretty straightforward, we've got it down to days"

2. "In that process, where do things tend to slow down or generate the most internal friction?"
   - Good: "Partner coordination, protocol configuration, manual handoffs between teams, waiting on third parties..."
   - Red Flag: "Runs pretty smooth, no major pain points"

3. "If you could change one part of that workflow in the next 12-24 months, what would you change and why?"
   - Good: "Speed up provisioning, automate the manual stuff, get visibility into partner networks, self-service for customers..."
   - Red Flag: "We're pretty happy with how things work today"

4. "How do you decide when to use your own network versus partners, and what does that limit today in terms of reach or services you can offer?"
   - Good: "We have to partner outside our footprint... limits our speed, visibility, and margins on those deals..."
   - Red Flag: "We can serve everything we need with our own infrastructure"

5. "When a strategic customer asks for something you can't easily deliver today - new cloud region, new geography, tighter SLA - what usually happens?"
   - Good: "We scramble, or we pass. Sometimes we lose the deal to someone faster..."
   - Red Flag: "We can usually accommodate whatever they need"

**Probe Deeper - Quantify the Pain**

6. "When traffic leaves your network - to a partner carrier, Type 2 circuit, or cloud provider - what visibility do you have? When something breaks, how do you troubleshoot?"
   - Good: "Once it leaves our network, we're blind... finger-pointing with partners, opening tickets and waiting..."
   - Red Flag: "Full end-to-end visibility regardless of path"

7. "When your customers need AWS Direct Connect, Azure ExpressRoute, or Google Cloud Interconnect - how do you handle that today?"
   - Good: "We tell them to call Megaport... we lose that revenue and that relationship..."
   - Red Flag: "We have our own cloud on-ramps built out"

8. "What percentage of your fiber capacity or infrastructure is actually generating revenue right now? Do you have stranded or underutilized assets?"
   - Good: "Honestly, we're probably at 30-50% utilization... stranded capacity we can't easily monetize..."
   - Red Flag: "85%+ utilized, capacity is our constraint"

9. "Who are you losing deals to? When prospects choose someone else, what's usually the reason?"
   - Good: "Speed. Larger players can provision faster. Or they want capabilities we can't offer..."
   - Red Flag: "We win most competitive deals"

10. "How big is your network operations or engineering team? What's consuming most of their time?"
    - Good: "Small team, stretched thin. Most time goes to manual provisioning, troubleshooting, configuration management..."
    - Red Flag: "Large team, well-staffed, not a constraint"

11. "How have customer expectations changed in the last 2-3 years? What are they asking for that you struggle to deliver?"
    - Good: "They want cloud-like, on-demand, self-service. They're used to AWS provisioning in minutes. We're still at weeks or months..."
    - Red Flag: "We're meeting their expectations"

12. "What's your current approach to network automation and orchestration? What tools or platforms are you using?"
    - Good: "Traditional OSS/BSS, some custom scripts, a lot of manual work... nothing that spans our whole environment..."
    - Red Flag: "Comprehensive automation platform already in place"

**Qualify & Next Steps**

13. "What are your growth plans for the next 12-24 months? What infrastructure challenges are you anticipating?"
    - Good: "Expanding footprint, adding partners, need to scale services... but provisioning is a bottleneck to growth..."
    - Red Flag: "No major infrastructure challenges anticipated"

14. "If you found a solution that addressed these challenges, what would the decision process look like? Who else would need to be involved?"
    - Good: "I'd need to bring in our CTO/VP Engineering... probably a 3-6 month evaluation..."
    - Red Flag: "No budget or authority for new infrastructure"

**Key Signal to Listen For:**
Growth mindset vs. status-quo mindset. There's usually a fit in most accounts - the real question is timing. If they just completed a major network upgrade and have no appetite for change, it may be better to wait. Look for the person with the growth mindset who can become your internal coach.

### During / After Demo Questions

Use these during or after the demo to gauge interest and surface automation opportunities.

1. "When you need to stand up or change connectivity today - new site, new cloud, new partner - how much of that process is still manual tickets and CLI work versus fully automated?"
   - Good: "Mostly manual... tickets, CLI, coordination calls..."
   - Red Flag: "Fully automated end-to-end"

2. "If you look at the last few network changes you did, what percentage of the steps could only be done by a senior engineer versus safely pushed to a self-service or automated workflow?"
   - Good: "80%+ requires senior engineer touch... we're the bottleneck..."
   - Red Flag: "Most is automated or delegated already"

3. "On a good week, how many hours does your team spend just moving configs around - updating routes, ACLs, tunnels, VLANs - versus designing new services or offers?"
   - Good: "Too many hours on config management... not enough time for new things..."
   - Red Flag: "We've automated the routine stuff"

4. "If you had a push-button way to stand up paths and cloud on-ramps across your network and partners, what's the first workflow you'd automate that you don't automate today?"
   - Good: "NNI setup... cloud on-ramps... cross-connects... [specific use case they mention]"
   - Red Flag: "Can't think of anything we'd change"

**Two 'Aha Moments' to Watch For:**

1. When they see how quickly a new path can be automated - weeks of design and tickets reduced to a few clicks.
2. When they see a federated path come up between two different 'brands' in the UI and realize this isn't just automating their network - it's turning multi-network interconnect into a product.

---

## Good Fit vs. Bad Fit Signals

**Good Fit Signals** — Immediate Priority Signals

- "Our provisioning takes 60+ days"
- Multiple mentions of "visibility" or "blind spots"
- Stranded fiber/capacity they can't monetize
- New CTO/VP Engineering in last 12 months
- Expanding multi-facility or geographically
- Using Megaport/Equinix (revenue opportunity)
- Type 2 circuits or multi-carrier complexity mentioned
- Within 200 miles of hyperscaler announcement

**Bad Fit Signals** — Immediate Disqualification Criteria

If ANY of these are true, disqualify immediately:

- No owned or operated infrastructure (pure software company or Enterprise)
- Already deployed Lumen Private Connectivity Fabric (competitor lock-in)
- Budget holder says "we're not looking at this for 18+ months"
- Company in bankruptcy or acquisition limbo

---

## Sample Email Outreach by Segment

Real email examples for each segment. Three personas per segment: Decision Maker, Technical, Non-Technical.

**Email Structure Framework**

Every email follows: Observation → Warmth → Problem → Solution Hint → Credibility → Soft CTA

Rules: 60-90 words max. No flattery. No em dashes. Always include "Same team that built Acme Packet." Soft CTA only.

### Colocation Operator Emails

**Example: RevNet (Minnesota colo with two data centers)**

**Decision Maker Email**

Subject: RevNet's interconnection revenue

Two data centers plus Azure Stack HCI for Midwest clients, that's a combination that should command premium interconnection revenue. But if cross-connects still take weeks to provision, you're stuck competing on space and power. Deals go to whoever can deliver fastest.

We built carrier infrastructure specifically for regional colos. Fabric-like capabilities, instant activation, no development project required. Same team that built Acme Packet.

Is this relevant for RevNet right now?

**Technical Email**

Subject: Cross-connects at RevNet

Managing cross-connects manually between Braham and Cambridge, plus out to partners, that's a lot of LOAs, router configs, and zero visibility once traffic leaves your infrastructure. Every new interconnect adds headcount pressure on a team that's probably already stretched thin.

We built carrier infrastructure that automates path activation without routing protocols. API-driven, protocol-free, deterministic paths. Same team that built Acme Packet.

Dealing with something similar?

**Non-Technical Email**

Subject: Selling connectivity at RevNet

When a RevNet customer needs cloud connectivity or a cross-connect to another tenant, what's the timeline? If it's weeks, they're also talking to whoever can deliver faster.

We built infrastructure that lets regional colos offer instant activation under their own brand. One operator told us: "Imagine having Megaport capability between providers."

Same team that built Acme Packet.

Worth a conversation?

### Fiber Operator Emails

**Example: Pilot Fiber (NYC metro, 250 route miles, expanding to 900 buildings)**

**Decision Maker Email**

Subject: Beyond Pilot's 900 buildings

900 buildings across Manhattan and the Bronx, that's real momentum. But it also means more RFPs hitting your desk for enterprise locations just off your fiber path. Traditional partner provisioning takes 60-90 days. That's a long time to wait on revenue you've already invested to capture.

We built carrier infrastructure that extends your reach programmatically. Federate with partners instantly, not in months. Same team that built Acme Packet.

Is this relevant for Pilot right now?

**Technical Email**

Subject: Extending Pilot's Control Panel

Your Control Panel and API handle on-net provisioning well. The challenge is extending that automation off-net without manual BGP peering for every partner connection. Each new carrier interconnect adds complexity, breaks visibility, and takes weeks. That doesn't scale with 900 buildings generating off-net demand.

We built carrier infrastructure that lets you activate partner connections via API in minutes. Protocol-free, deterministic paths. Same team that built Acme Packet.

Dealing with something similar?

**Non-Technical Email**

Subject: Deals beyond Pilot's footprint

You're about to have 900 on-net buildings in NYC. That means more enterprise RFPs for locations just off your fiber path. Good problem to have, until quoting off-net circuits takes weeks. Prospects want the Pilot experience everywhere. When you can't deliver fast, they find someone who can.

We built infrastructure that gives you a pre-integrated ecosystem of partners and cloud on-ramps. Extend your reach without extending your timeline. Same team that built Acme Packet.

Worth a conversation?

### Network Operator Emails

**Example: Logix (Texas, 7,000 route miles, 300 POPs, 800G backbone)**

**Decision Maker Email**

Subject: Monetizing Logix's 7,000 miles

The 400G wavelengths you deployed last week on the 800G backbone, lighting that capacity fast is the difference between revenue and dark fiber sitting idle. 7,000 route miles is a lot of fiber to keep lit. Standard provisioning leaves too much capacity sitting dark for too long while competitors close deals faster.

We built carrier infrastructure that turns fiber into a programmable platform. Service activation in minutes, not weeks. Same team that built Acme Packet.

Is this relevant for Logix right now?

**Technical Email**

Subject: Provisioning across 300 POPs

You're running 7,000 route miles and 300 POPs with Equinox handling billing and orders. That's solid for back-office, but the gap is service activation, which still involves weeks of routing configuration per customer. That bottleneck doesn't scale with an 800G backbone and new 400G services waiting to be sold.

We built carrier infrastructure that adds what your OSS can't provide. API-driven path activation without protocol complexity. Deterministic paths, line-rate encryption. Same team that built Acme Packet.

Dealing with something similar?

**Non-Technical Email**

Subject: Selling Logix capacity faster

You have 7,000 miles of Texas fiber and new 400G services. When a carrier customer needs capacity lit, waiting weeks means they're also talking to competitors who can move faster. Provisioning timelines are where deals stall. The investment is already made, it's just a question of how fast you can turn it into revenue.

We built infrastructure that lets you provision in minutes. Turn backbone investment into deals closed, not deals pending. Same team that built Acme Packet.

Worth a conversation?

### MSP / Aggregator Emails

**Example: BCM One (7,000 channel partners, 14 POPs, national/international)**

**Decision Maker Email**

Subject: BCM One's carrier dependencies

7,000 channel partners selling managed connectivity, that's a big machine to keep running. But 40-60% of your costs are locked into AT&T and Verizon, and your provisioning timeline is dictated by theirs. You own the customer relationship but wait weeks for circuits. New leadership often looks at these dependencies differently.

We built carrier infrastructure that breaks that dependency. Instant provisioning, end-to-end visibility, OpEx model. Same team that built Acme Packet.

Is this relevant for BCM One right now?

**Technical Email**

Subject: Visibility across BCM One's carriers

You're stitching together circuits from AT&T, Verizon, and others to serve multi-site enterprises. That's not easy, and there's no visibility once traffic leaves your 14 POPs. Customer complains. You open tickets. Carriers point fingers. Nobody has data. Meanwhile, you own the SLA.

We built carrier infrastructure that treats all underlying networks as one fabric you control. Hop-by-hop visibility, automated provisioning. Same team that built Acme Packet.

Dealing with something similar?

**Non-Technical Email**

Subject: Closing faster at BCM One

Your channel partners close a multi-site deal. Then what? Weeks waiting on AT&T or Verizon to provision. Every delay is a delay in revenue recognition and a risk the customer second-guesses the decision. That's frustrating when you've done the hard work of winning the business.

We built infrastructure that lets you activate services the day you close. Tier 1 delivery speed on your asset-light model. Same team that built Acme Packet.

Worth a conversation?

---

## Segment-Specific Language Quick Reference

### Subject Line Patterns

- [Company]'s [topic] → "RevNet's interconnection revenue"
- Beyond [Company]'s [asset] → "Beyond Pilot's 900 buildings"
- [Topic] at [Company] → "Cross-connects at RevNet"
- [Verb]ing [Company]'s [asset] → "Monetizing Logix's 7,000 miles"
- [Company]'s [pain point] → "BCM One's carrier dependencies"

### Segment-Specific Language

| Segment | Their World | Pain Language |
|---------|-------------|---------------|
| Colocation | Facilities, tenants, cross-connects, meet-me rooms, cloud on-ramps | Competing on space/power, losing revenue to Megaport, manual cross-connect provisioning |
| Fiber | Route miles, dark fiber, NNIs, Type 2 circuits, carrier partnerships | 60-90 day NNI provisioning, dark fiber sitting idle, losing multi-state deals |
| Network | Backbone, POPs, OSS/BSS, wavelengths, carrier customers, wholesale | OSS/activation gap, manual provisioning despite automation, capacity sitting dark |
| MSP | Underlying carriers, multi-site deals, channel partners, SLAs | Carrier dependencies, no visibility beyond POPs, timeline dictated by AT&T/Verizon |

### Objection One-Liners Quick Reference

| Objection | One-Liner Response |
|-----------|-------------------|
| "Different from Megaport?" | "Megaport keeps your margin and your customer. We give you both back." |
| "Sounds complex" | "Arvig called it 'almost instantaneous.' No BGP, no MPLS, no CCIEs required." |
| "Sounds expensive" | "What's it costing you to lose deals that take 60 days to provision?" |
| "Want to build our own" | "That's 18-24 months. We're already done building it." |
| "Just invested in Cisco/Juniper" | "Perfect. We sit at the edge where your routers stop. Your core stays untouched." |
| "Who are you?" | "Our team built Acme Packet and 128 Technology - they've done this twice before at scale." |
| "Current process works" | "It works today, but your customers are comparing you to whoever can deliver fastest and expectations are only going up." |
| "What about Lumen PCF?" | "Lumen wants you as a customer. We want you as a competitor to Lumen." |
| "Different from SD-WAN?" | "SD-WAN is great for branch connectivity - we're focused on the middle mile between networks." |
| "Can you handle our scale?" | "We're working with Tier 1 carriers on exactly that question - the architecture handles it." |
| "OSS/BSS integration?" | "API-first. Your ordering triggers us; lifecycle events flow to your billing." |
| "Security requirements?" | "Line-rate AES-256 encryption on every path. No performance tradeoff." |
| "Mid-transformation" | "We're the edge layer your transformation is missing." |
| "Carriers won't let us deploy" | "Deploy at your demarcation. You're not touching their network." |
| "Switch carriers often" | "Switch carriers anytime. The PBC stays put; just update the path." |
| "No engineering resources" | "Centra called it 'fabric-in-a-box' - no routing protocols, no specialized expertise needed." |
| "MPLS/BGP works fine" | "MPLS for what needs MPLS. Instant paths for everything else." |
| "NNI process just takes time" | "Every multi-state deal you lose to provisioning delays is margin walking out the door." |
| "We compete on space/power" | "Don't just sell space and power. Sell what runs over it." |
| "Don't own infrastructure" | "You own the customer relationship. We give you visibility into everything behind it." |
| "Tier 1s going direct" | "Match their speed. Keep your relationships. That's how you win." |

### Signal / Why It Matters

| Signal | Why It Matters |
|--------|---------------|
| Provisioning takes 30-90+ days | Direct pain MaiaEdge solves - minutes vs months |
| Currently using Megaport/Equinix Fabric | Margin recapture + sovereignty opportunity |
| Mentions "visibility" or "blind spot" problems | Direct pain - hop-by-hop telemetry across boundaries |
| Has Type 2 circuits or partner NNIs | Federation value - visibility across leased capacity |
| Within 200 miles of hyperscaler announcement | Cloud connectivity demand incoming |
| Stranded fiber/underutilized capacity | Monetization opportunity - turn dark fiber into services |
| New CTO/VP Engineering in last 12 months | New leadership = new budget, new priorities |

### Use Case Reference

| Use Case | Primary Segments | Pain Addressed | Outcome |
|----------|-----------------|----------------|---------|
| Internal / DCI | Network, Fiber | Protocol complexity, slow PoP activation | Unified fabric, faster site activation |
| Fiber Monetization | Fiber | Stranded capacity, can't sell dark fiber | Turn idle fiber into deterministic services |
| Automated Cross-Connects | Colo | Hours per cross-connect, ticket backlogs | Instant tenant connectivity, self-service |
| Cloud On-Ramps | All | "Tell customers call Megaport" | AWS/Azure/GCP under your brand |
| Mobile Backhaul | Network | Cell tower connectivity at scale | Scalable backhaul without proportional complexity |
| Federation / NNI | All | 60-90 day NNI projects, lost deals | Instant partner connections, extend reach |

### Use Case by Segment Matrix

| Use Case | Colo | Fiber | Network | MSP |
|----------|------|-------|---------|-----|
| Internal / DCI | S | P | P | - |
| Fiber Monetization | - | P | S | - |
| Cross-Connects | P | - | - | - |
| Cloud On-Ramps | S | S | S | S |
| Mobile Backhaul | - | S | P | - |
| Federation / NNI | S | S | S | P |

**Legend:** P = Primary entry point | S = Secondary/expansion | - = Not applicable

### Persona / Email Style Quick Reference

| Persona | Focus | CTA |
|---------|-------|-----|
| Decision Maker | Revenue, margin, competitive positioning. Zero technical terms. | "Is this relevant for [Company] right now?" |
| Technical | Architecture, operational efficiency. Can mention PBC, API, protocol-free. | "Dealing with something similar?" |
| Non-Technical | Deal velocity, sales cycle, competitive positioning. No technical terms. | "Worth a conversation?" |

---

## Data Sources by Segment

| Segment | Primary Data Sources |
|---------|---------------------|
| **Neocloud** | Company website, press releases, funding announcements, facility expansion news, LinkedIn |
| **Colocation (Both)** | PeeringDB (facility count), Data Center Map (facility count), Website (services, tenant lists) |
| **Fiber Operator** | Website (route miles), NTCA Directory (member status), PeeringDB (PoP count), FCC CORES |
| **Network Operator** | Website (services, portal), PeeringDB, TeleGeography, press releases |
| **MSP/Aggregator** | Website (carrier partnerships), LinkedIn (employee count), press releases |
| **Enterprise** | Industry-specific directories (AHA, FDIC, NAM), news about private network investments |

---

*This document consolidates classification logic, personas, pain points, value propositions, discovery questions, objection handling, and exclusion criteria from the MaiaEdge Messaging Framework V4, ICP Playbook, 6-Segment Explanation, Cheat Sheets, 12-Property Architecture, AI Market Positioning Guide, and Cloud On-Ramp Business Case.*

*Last updated: February 2026*
