# LMaaS — Last Mile as a Service
## Strategic Brief | March 2026 | Confidential

---

## The Core Idea

Abilash met with an executive from Equinix who observed that fiber operators are ideally positioned to deliver cloud onramp and direct low-latency connectivity to NeoCloud providers — but they resist adopting new technology. Classic closed mindset.

To date, MaiaEdge has been resolute about being an infrastructure provider, not a NaaS. But LMaaS asks a different question: **what if instead of trying to sell to fiber operators, we became their customer?**

Instead of selling PBCs to fiber operators, MaiaEdge buys eLines when enterprise customers purchase cloud onramp, Type 2, and other services. MaiaEdge sets the product, pricing, oversubscription model, and engineering. The fiber operator does what they already know: deliver circuits to customers and buildings they already serve.

---

## Why This Is a Different Kind of Business

### The relationship flip

Right now MaiaEdge approaches fiber operators as a vendor — asking them to learn new technology, change their sales motion, and accept technology risk. That is a hard sell in a conservative industry.

The moment MaiaEdge becomes a buyer of their eLines, the conversation inverts completely. MaiaEdge is now revenue to them. Their account team has an incentive to call us. Their procurement process knows exactly how to handle us. We are not disrupting anything — we are a new enterprise customer ordering circuits, which is exactly what fiber operators do every day.

**We go from vendor to customer. That changes everything.**

### The three-layer architecture

**Leg 1 — Last mile (clean):**
Customer building → fiber operator NID → private eLine → MaiaEdge metro PBC

The eLine runs privately from the customer's NID straight to our PBC. Dedicated, deterministic, SLA-backed. No internet, no exchange points, no latency variability. The fiber operator is just delivering a point-to-point Ethernet circuit — the same thing they do for enterprise customers every day.

**Leg 2 — Mid mile (the key insight):**
MaiaEdge metro PBC → fiber operator's owned long-haul fiber (wave) → fiber operator's rack at cloud exchange → cross-connect → cloud onramp

This is where the model becomes exceptional. Fiber operators like Arvig in Minneapolis already own long-haul fiber routes to major cloud exchange facilities (e.g., Chicago Equinix) and maintain racks there. A wholesale wave on their existing lit infrastructure is nearly pure margin for them — they sell it cheap because the incremental cost is minimal.

MaiaEdge buys that wave wholesale. The entire path from customer NID to AWS Direct Connect is private, deterministic, and low-latency — and we never had to build any of it.

**The full path:**
Customer NID → eLine → Metro PBC → fiber operator wave → fiber operator rack at Equinix → cross-connect → Equinix Fabric → AWS / Azure / NeoCloud

**Leg 3 — Cloud onramp:**
Cross-connect into Equinix Fabric or dedicated Direct Connect port at the cloud exchange.

---

## The Compounding Fiber Operator Relationship

Each fiber operator relationship creates value across multiple product lines simultaneously:

- **eLines** — one per enterprise customer, recurring MRC, triggered on customer order
- **Long-haul waves** — mid-mile backhaul on their existing owned fiber, very low incremental cost to them
- **Rack / cross-connect** — use their existing data center presence at the cloud exchange

This makes MaiaEdge a strategic account for the fiber operator's sales team across three revenue lines at once. They are motivated to bring us new buildings and new customers because every new enterprise customer generates more spending across all three product lines.

**The supplier-as-channel dynamic:** Fiber operators become simultaneously our wholesale infrastructure provider and our motivated distribution channel. Their sales team earns on every circuit they feed us.

---

## Business Model Comparison

### Current PBC subscription model
- Partner (e.g., Atlantech) buys PBC at ~$680/mo (after 30% partner discount)
- Partner builds and operates cloud onramp service
- Partner captures the service margin
- MaiaEdge earns $680/mo per deployment — asset-light, but revenue capped by partner adoption

### LMaaS model
- MaiaEdge owns the full infrastructure stack per POP
- MaiaEdge sells directly to enterprise at managed service pricing
- MaiaEdge captures the full service margin

**Revenue comparison at base case (10 Standard 1G customers, Ashburn):**

| Model | MaiaEdge Monthly Revenue | MaiaEdge Monthly GP |
|-------|--------------------------|---------------------|
| PBC subscription (Atlantech) | $680 | $680 (subsidized) |
| LMaaS direct | $5,600 | $2,752 (Phase 2) |

**At 100G port, 50% fill (87 customers, Ashburn):**

| Scenario | Monthly Revenue | Monthly GP | Annual GP |
|----------|----------------|------------|-----------|
| 25% fill (44 customers) | $25,250 | $15,762 | $189K |
| 50% fill (87 customers) | $51,600 | $42,112 | $505K |
| 80% fill (138 customers) | $82,400 | $72,912 | $875K |

Per-POP gross margins at scale: **82–88%**. This is software-like margin on carrier infrastructure.

---

## The Hybrid Model

MaiaEdge does not have to choose between LMaaS and the existing PBC subscription model. The right structure is geographic segmentation:

**Major hub markets (MaiaEdge-owned):**
Ashburn, LA, Chicago, Dallas, NYC — the top 5-8 AWS Direct Connect metros where customer density is achievable. MaiaEdge deploys capital here, owns the full stack, runs LMaaS directly.

**Secondary and obscure markets (partner PBC subscriptions):**
Carriers and resellers buy PBC subscriptions and build their own onramps in markets MaiaEdge hasn't prioritized. They have every incentive to go where MaiaEdge isn't. Channel conflict disappears.

**The policy question to lock down:**
Partners need geographic clarity — if they invest in building out a market, MaiaEdge should not enter that geography without notice. Right-of-first-refusal or territory exclusivity language in partner agreements protects the channel in non-hub markets.

**An important note on cloud onramp specifically:** For the main AWS onramp locations, MaiaEdge likely owns these directly. For more obscure onramp locations globally, partners can build via PBC subscription — and can federate with MaiaEdge's hub PBCs to provide their customers access to the full network.

---

## Capital Requirements

### What capital actually buys

**Infrastructure (modest):**
A 100G Ashburn POP costs $9,488/mo all-in at steady state ($8,150 subsidized). PBC hardware is a one-time CapEx per POP. eLines and fiber operator waves are variable costs triggered only when a customer signs — largely self-funding from MRC day one. No pre-commitment to dark fiber or long-term capacity.

**Working capital gap (manageable):**
From zero customers to break-even on a 100G Ashburn POP requires roughly 15-17 Standard 1G customers. At a 90-day enterprise sales cycle, that's approximately 3-5 months of fixed infrastructure costs before gross profit turns positive — approximately $40-50K per POP in working capital. Across 5 major metro POPs: $200-250K in infrastructure working capital. Modest for a B-round.

**Headcount (the real capital deployment):**
Direct enterprise sales motion, provisioning operations, and BD to sign fiber operator wholesale agreements. This is the majority of what the B-round funds.

### Capital efficiency ratio
Five major metro POPs at 50% fill generates ~$2.5M/year gross profit from approximately $500K in infrastructure working capital. That is very difficult to find in infrastructure businesses.

### Phase approach
- **Phase 1 (prove):** 1 POP (Ashburn), 3 fiber operator wholesale agreements, 10-20 enterprise customers
- **Phase 2 (expand):** 3-5 major metro POPs, 15-20 fiber operator relationships, top 10 markets covered
- **Phase 3 (scale):** National coverage via fiber operator partner network, international via IENTC/carrier-partner model

---

## Investor Framing — Business Model Comps

### Primary comp: Twilio

Twilio took carrier infrastructure — telephone numbers, SMS routes, voice circuits — that had been locked inside telcos for decades, bought it wholesale, wrapped it in a programmable managed layer, and sold it to businesses at dramatically higher margins than the raw underlying capacity would suggest. Carriers became suppliers, not competitors.

LMaaS does exactly this for enterprise private connectivity — a market Twilio never addressed — with fiber operators as the carrier layer and the PBC stack as the technology moat.

**Twilio's returns:** Series A at ~$3M valuation (2009) → IPO at $1.2B (2016) → peak $60B market cap (2021). Early investors made thousands of percent returns — not because Twilio built a better phone network, but because they repositioned carrier infrastructure as a software-enabled managed service and captured SaaS-level multiples.

### The multiple expansion argument

| Business type | Typical revenue multiple |
|---------------|--------------------------|
| Traditional fiber operator / CLEC | 5-8x |
| Managed services company | 8-12x |
| SaaS / high-margin recurring revenue | 15-25x ARR |
| Platform with network effects | 20-40x ARR |

LMaaS has 80%+ gross margins at scale, fully recurring MRC revenue, and a land-and-expand motion as enterprise customers add circuits and locations. The market should value that like software, not like a carrier.

**The framing:** We are taking a commodity product — fiber operator eLine capacity — and wrapping it in a software-defined managed service layer that commands a 3-5x revenue multiple premium over the underlying infrastructure. Every dollar of fiber operator wholesale cost we buy generates $3-5 in MRC revenue. That spread is the business.

### Supporting comps

**Cloudflare** — Built a distributed network of networks without owning the underlying physical infrastructure. Software-defined, asset-light, valued at 30-40x revenue at peak. LMaaS aggregates fiber operator infrastructure the same way Cloudflare aggregated internet infrastructure and made it intelligent via software.

**Zayo Group** — Aggregated fiber through M&A, went private at $14.5B. LMaaS achieves the same infrastructure aggregation commercially, with a fraction of the capital. The returns to equity holders are dramatically better because you're not buying physical assets.

**Megaport / PacketFabric** — Closest direct market comps. Megaport trades at ~$400M market cap on ~$100M revenue with high gross margins. PacketFabric acquired by Lumen. Critical differentiation: neither solves the last mile. The enterprise customer still has to get their building to the exchange. LMaaS owns that end-to-end.

**Vonage / Bandwidth.com** — CPaaS companies that wrapped carrier infrastructure in software, generated strong early investor returns, both acquired at significant premiums by strategic buyers who needed the capability and couldn't build it.

### The one-liner for investors

*"Twilio proved that when you sit between carriers and enterprises and abstract the complexity, the market values your revenue like software even though your raw material is carrier infrastructure. We are doing that for enterprise private connectivity — a market Twilio never addressed — with fiber operators as our carrier layer and a PBC stack that no one else has. And unlike Twilio, our suppliers are also our distribution channel, because the fiber operator's sales team earns on every circuit they feed us."*

### Strategic acquirer story

The obvious acquirers for a built-out LMaaS network are the same names consolidating connectivity assets: Lumen (bought PacketFabric), EQT/Digital Bridge (took Zayo private), Equinix (expanding services layer). A nationally distributed LMaaS network with fiber operator relationships across 20+ markets is exactly what any of them would prefer to acquire rather than build.

---

## The Ecosystem Play — Why LMaaS Is Really a Platform

### Cloud onramp is the entry point, not the end state

LMaaS cloud onramp revenue is the near-term business that funds operations and proves the model. But what LMaaS actually builds underneath that revenue is far more valuable: a federated network of independent fiber operators, all interconnected through MaiaEdge PBCs, forming a private networking marketplace that no single carrier can replicate.

Every fiber operator MaiaEdge signs for LMaaS adds their footprint to the federation. Arvig gives you Minneapolis metro + Chicago. Segra gives you the mid-Atlantic and Southeast. Consolidated gives you northern New England. Within 10-15 fiber operator relationships, MaiaEdge has a patchwork of private, federated coverage across a significant portion of the US — all connected through PBCs that can route traffic between any two points on the network.

### The marketplace emerges from the network

Once multiple fiber operators are on the federation, services become possible that none of them could offer alone:

- An enterprise in Arvig's Minneapolis footprint can get a private, deterministic path to another enterprise in Segra's Virginia footprint — routed across the federation without ever touching the public internet. Neither Arvig nor Segra could offer this independently. It only exists because both are on the MaiaEdge fabric.

- A NeoCloud provider in one market can offer private GPU cluster access to enterprise customers in any other market on the federation — low-latency, encrypted, SLA-backed.

- Multi-cloud routing between AWS, Azure, and Google Cloud across federated POPs, managed as a single service through MaiaEdge.

- Inter-enterprise private connectivity for regulated industries (healthcare, financial services) that need deterministic paths between locations served by different regional fiber operators.

These are all marketplace services — they only exist because the network has enough participants to make them valuable. Each new fiber operator makes the network more valuable for every existing fiber operator's customers. Each new enterprise customer creates demand that pulls the next fiber operator in.

### Metcalfe's law applied to carrier infrastructure

The value of the federated network scales with the square of the number of participants. This is the same network effect that powered Visa's growth: Visa didn't replace the banks, they built the network that made every bank more valuable and took a margin on every transaction that crossed the network. MaiaEdge doesn't replace the fiber operators — it builds the federation that makes each operator's infrastructure more valuable and earns on every service that traverses the fabric.

At 5 fiber operators, LMaaS is a managed cloud onramp service. At 20+ fiber operators with hundreds of enterprise customers, it's a private networking marketplace. The economics shift from per-circuit MRC to platform transaction revenue — and the valuation multiples shift accordingly.

### Why this is defensible against AWS Interconnect Last Mile

AWS Interconnect Last Mile (in gated preview with Lumen, AT&T joining Q2 2026) solves a point-to-point problem: get the enterprise connected to AWS. That's a spoke-and-hub model with AWS at the center. MaiaEdge is building a mesh — any-to-any private connectivity across a federated network of independent fiber operators. AWS cannot replicate this because they are not in the business of federating competing carriers. Lumen cannot replicate it because they are a single carrier. Megaport is closer structurally but lacks the last-mile fiber operator relationships and the PBC federation technology.

The "nobody else solves the last mile" messaging has a shelf life as AWS Interconnect matures. The durable positioning is: **"We are the only platform that delivers fully private, deterministic connectivity across a federated network of independent fiber operators — any building to any cloud, any building to any building — with carrier-grade SLAs, through a marketplace that no single carrier can replicate."**

### The B-round narrative shifts

The near-term pitch: LMaaS cloud onramp generates $500K-$875K annual gross profit per major metro POP, growing with each fiber operator relationship. Real revenue, real margins, provable unit economics.

The platform pitch: LMaaS is the customer acquisition flywheel for building the first federated private networking marketplace. The cloud onramp revenue is what funds the network build. The marketplace — where every transaction across the federation generates margin for MaiaEdge — is what investors are really buying into. That's where the company stops being compared to Megaport ($400M) and starts being compared to platform businesses with network effects.

---

## Distributed AI — The Macro Trend That Makes LMaaS Inevitable

### The industry is moving toward MaiaEdge

The shift from centralized AI training to distributed AI inference is the most significant infrastructure trend in the industry right now — and it creates massive demand for exactly what LMaaS provides.

**The numbers:**
- Inference workloads will account for roughly two-thirds of all compute by end of 2026, up from one-third in 2023 (Deloitte)
- IDC expects 80% of enterprises to deploy distributed edge AI infrastructure by 2027
- Edge computing spend forecast: $378 billion by 2028 (IDC)
- NeoCloud GPUaaS revenue: $42 billion in 2025, forecast to surpass $250 billion by 2030
- Early benchmarks from Comcast's distributed AI grid show cost-per-token reductions of up to 76% vs. centralized deployments

**What happened in March 2026 alone:**
- NVIDIA announced AI Grid at GTC (March 19) — a reference architecture for distributing inference across telecom networks. AT&T, Spectrum, and four other major operators are already deploying. The architecture explicitly requires low-latency, deterministic connectivity between distributed inference nodes and enterprise end-users.
- Equinix launched Distributed AI Hub (March 11) — a framework for enterprises to discover and connect to NeoCloud providers, GPU clouds, and AI infrastructure through private, low-latency interconnection at 280 data centers. Equinix explicitly calls out that enterprises need to "unify inherently distributed workflows across public clouds, private data centers, edge environments, and a rising wave of specialized neoclouds."
- HPE announced AI Grid — connecting distributed AI factories and inference clusters across regional and far-edge sites.
- Verizon publicly positioned metro fiber and private 5G as the connectivity layer for enterprise AI inference.

The entire industry is converging on a single conclusion: distributed AI inference needs private, low-latency, deterministic connectivity from enterprise locations to GPU compute — and nobody has solved the last-mile piece of that connectivity.

### Why NeoCloud providers need LMaaS

NeoCloud providers (Together.ai, RunPod, Lambda, Inference.net, Modal, CoreWeave) are sitting on a growing problem: their enterprise customers need private paths to GPU clusters, but the NeoCloud's core competency is compute, not networking.

The pain points are real and documented:
- **Egress costs** add 20-40% to enterprise bills at hyperscalers. Most neoclouds offer free egress, but that only works if the customer can get private connectivity to the neocloud in the first place.
- **Network performance** is the hidden bottleneck. Enterprises spending $50K+/mo on GPU compute experience slow training, expensive egress, and inconsistent inference — often because their network path to the GPU cluster is over public internet with unpredictable latency.
- **Security and compliance** requirements (SOC2, HIPAA, financial regulations) increasingly demand private, encrypted connectivity. Public internet paths don't qualify.

LMaaS solves all three of these problems for the NeoCloud — and positions MaiaEdge as the enterprise access layer that NeoCloud providers can offer their customers.

### The alternate GTM: sell to NeoCloud providers directly

Instead of only approaching NeoCloud providers as potential PBC customers (the current Datum.net strategy), LMaaS enables a fundamentally different sales conversation:

**Current approach:** "Buy our PBC to improve your network observability and path determinism."
**LMaaS approach:** "We bring you enterprise customers on private, low-latency paths. Your customers get better performance, lower egress costs, and compliance-ready connectivity. You get stickier customers and a differentiation point against other NeoClouds."

In this model, the NeoCloud doesn't buy a PBC — they become a destination on the MaiaEdge federation. Enterprise customers connect to the NeoCloud through the LMaaS fabric, the same way they connect to AWS through the cloud onramp. The NeoCloud's value proposition to their enterprise customers improves because they can now offer private connectivity as a feature, powered by MaiaEdge.

This also creates a powerful demand-generation loop: the NeoCloud's sales team is telling enterprise prospects "you can get private, dedicated access to our GPU clusters through our MaiaEdge partnership." Those enterprise customers need an eLine from a fiber operator to connect. The fiber operator earns revenue. MaiaEdge earns MRC. The NeoCloud gets a stickier customer. Everyone wins.

### NVIDIA AI Grid — the wind at MaiaEdge's back

NVIDIA's AI Grid reference architecture is designed to distribute inference workloads across telecom networks — regional POPs, central offices, metro hubs, and edge locations. Six major operators (including AT&T and Spectrum) are already deploying.

The AI Grid control plane routes workloads based on latency, sovereignty, and cost. But the connectivity between the enterprise and the inference node is assumed to exist — NVIDIA is not building the network layer. Someone has to provide the private, deterministic path from the enterprise building to the nearest AI Grid inference node.

That is LMaaS. The fiber operator's eLine connects the enterprise to the metro PBC. The PBC connects to the nearest inference node — whether that's a NeoCloud at an Equinix facility, an AI Grid node at a telco POP, or a hyperscaler cloud region. The MaiaEdge federation routes across all of them.

As distributed AI inference scales from early adopters (2026) to mainstream enterprise deployment (2027-2028), the demand for private last-mile connectivity to distributed compute will grow exponentially. LMaaS is positioned to be the infrastructure layer that makes distributed AI work for enterprises.

### TAM expansion

Cloud onramp to AWS/Azure/GCP is the initial LMaaS use case. But distributed AI connectivity — enterprise to NeoCloud, enterprise to AI Grid inference node, enterprise to private GPU cluster — is a potentially much larger TAM. The $378 billion edge computing market and $250 billion NeoCloud market both require connectivity that doesn't exist today at the last mile. LMaaS is the delivery mechanism.

---

## Competitive Landscape

### Megaport
Virtual cross-connects (VXCs) between 700+ data centers globally. Pay-as-you-go, bandwidth from 1 Mbps to 100 Gbps. Pricing is relatively high on a per-Mbps basis (~$1,000/mo for 1G Hosted Connection to AWS including port charge). **Does not touch the last mile** — enterprise must get themselves to a Megaport-enabled facility.

### Lumen (PacketFabric)
NaaS platform with 1,500+ enterprise customers, growing 50% QoQ. Expanded Internet On-Demand to 10M+ off-net locations by partnering with last-mile providers. **Launch partner for AWS Interconnect Last Mile** (gated preview Nov 2025). Automates last-mile partner discovery, cross-connects, VLANs, BGP peering. Provisions four redundant connections across two Direct Connect locations. 99.99% SLA, MACsec by default, 1G-100G bandwidth.

### AT&T NetBond
Carrier-grade multi-cloud connectivity with guaranteed SLAs and georedundancy. Pricing based on minimum bandwidth commitment with overage charges. **Requires customer to be on AT&T's MPLS VPN** — value-add to existing WAN, not standalone. Joining AWS Interconnect Last Mile in Q2 2026.

### Verizon Secure Cloud Interconnect
Layers on top of Verizon Private IP MPLS, Ethernet E-Line, or Internet Dedicated. Consumption-based, up to 10 Gbps, 200+ CSPs. **Requires existing Verizon network relationship** — not standalone.

### LMaaS differentiation

- **End-to-end private path:** Only LMaaS delivers a fully private, deterministic circuit from the customer's NID to the cloud exchange via a single commercial relationship. Every competitor leaves the last mile to someone else.
- **No prerequisite WAN:** AT&T requires MPLS. Verizon requires Private IP. Megaport requires customer to reach a Megaport facility. LMaaS requires nothing except a fiber drop to the building.
- **Fiber operator channel:** Embedded, motivated distribution through fiber operator sales teams who earn across multiple product lines. No other competitor has this.
- **Oversubscription economics:** PBC multi-tenant slicing enables 2:1 oversubscription that delivers Standard 1G at $550 wholesale — ~45% below Megaport equivalent. Structural cost advantage from the technology.
- **Federation / marketplace:** Any-to-any mesh connectivity across independent fiber operators. AWS, Lumen, Megaport all operate spoke-and-hub or single-carrier models.

### Pricing implication

LMaaS delivers a premium service (end-to-end private, fully managed, no prerequisites) compared to Megaport where the customer still solves their own last mile. Price at or near Megaport parity for the cloud onramp component, with a separate last-mile component bundled into the MRC. The total can still be lower than the customer's combined cost of Megaport + their own last-mile circuit, but the onramp piece alone should not be discounted 45% below Megaport. The value proposition is "we solve the entire problem in a single MRC" — that is a premium, not a discount.

---

## Key Questions Still Being Researched

1. **eLine wholesale pricing** — What fiber operators charge MaiaEdge wholesale vs. what they charge enterprise retail. Research in progress.

2. **Fiber operator long-haul profile** — How many US fiber operators have the full Arvig profile: metro fiber + owned long-haul route to a major cloud exchange + existing rack at the destination? This determines how broadly the cleanest version of the model scales.

3. **Wholesale agreement structure and timeline** — How long does it take to execute a fiber operator wholesale agreement? Who signs it on their side? This is the key variable in the ramp-to-revenue timeline.

4. **Geographic boundary definition for partner agreements** — Need explicit language in PBC partner agreements defining which markets MaiaEdge reserves the right to enter directly, to protect channel partners who invest in secondary markets.

5. **DIA tier viability** — For markets where a fiber operator doesn't have owned long-haul to a cloud exchange, DIA on leg 2 may be a viable lower-price tier. IENTC's Mexico-Miami deployment at 22ms confirms this can work. Reliability and consistency need further validation for domestic US routing across exchange points.

---

## Open Strategic Questions

- Does MaiaEdge allow Datum.net and similar partners to handle cloud connectivity at the exchange end while MaiaEdge focuses exclusively on last mile? In those cases MaiaEdge could sell Datum the ability to federate with our hub PBCs, giving their customers access without MaiaEdge needing to own the cloud exchange infrastructure.

- What is the rev share structure with fiber operator sales teams? One-time spiff vs. ongoing percentage of MRC? Ongoing is more motivating but has margin implications that need to be modeled.

- How does MaiaEdge handle the operational lift of becoming a service provider — SLA management, provisioning, billing, customer support — that partners like Atlantech currently handle themselves?

---

*Document based on strategic discussion, March 25, 2026. For internal use only.*
