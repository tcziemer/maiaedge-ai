# MaiaEdge 101 - Partner Edition

**Everything you need to position, qualify, and start selling MaiaEdge.**
*If you only read one document, read this one.*

---

## The 30-Second Pitch (Memorize This)

> **"MaiaEdge is carrier infrastructure for federated private networking. Programmable private paths form an instant network fabric across owned and partner networks. PBC hardware at the edge, PCE software in the cloud, white-label portal under the operator's brand. Operators build their own fabric instead of joining someone else's. Customers, margin, and brand stay with them."**

**Tagline:** Private paths. Any network. Instantly.

**Category:** Carrier infrastructure for federated private networking.

**What it is NOT:** NaaS. IaaS. A platform you join. SD-WAN. A router replacement. An orchestration project that takes 12 months.

---

## Why MaiaEdge Exists

Network operators have automation inside their own networks. APIs, orchestration, zero-touch provisioning. But that automation stops at the edge. Once traffic leaves their domain, it dissolves into spreadsheets, emails, and manual coordination. Visibility and SLA control vanish. The result: 60-90 day turn-ups, stranded capacity, expensive SLA penalties, and deals lost to whoever provisions faster.

MaiaEdge turns owned and leased infrastructure into an instant network fabric. Programmable private paths, automated provisioning, full visibility - across the operator's network AND across partner networks they don't own.

**Core insight:** Customers don't need a new use case. They need to do what they're already doing - but faster, with more visibility, and without giving up the customer relationship.

---

## What MaiaEdge Sells (Three Components)

### Path Border Controller (PBC) - The Edge Hardware

A 1RU appliance deployed at network boundaries (carrier hotels, meet-me rooms, PoPs, customer demarcation). Stateless forwarder - no routing decisions, just executes instructions from the PCE.

| Spec | Detail |
|---|---|
| Form factor | 1RU appliance |
| Interfaces | Dual 100 Gbps full-duplex |
| Encryption | Line-rate AES-256-GCM IPsec |
| Latency overhead | Less than 2 microseconds |
| Forwarding model | Stateless, protocol-free, deterministic |
| Routing protocols required | None. No BGP, no OSPF, no MPLS |

### Path Computation Engine (PCE) - The Cloud Orchestrator

Cloud-native, carrier-neutral NNI engine. Calculates deterministic end-to-end paths across networks, enforces policy, provides unified visibility.

| Capability | Description |
|---|---|
| Path computation | Real-time calculation of optimal, deterministic paths |
| Multi-domain orchestration | Automate provisioning across owned and partner networks |
| Telemetry | Hop-by-hop visibility (latency, jitter, loss) |
| API integrations | Equinix Fabric, Megaport, AWS, Azure, GCP |
| White-label portal | Self-service portal for customers under the operator's brand |
| Multi-tenancy | Complete isolation between tenants. Each customer sees only their own paths and metrics |
| Standards | Mplify LSO Sonata, TM Forum ODA conformance |

### Port Extender - The Tenant Fan-Out Switch

48-port integrated switch that pairs with the PBC for high-density meet-me room and colocation deployments. 48 SFP28 (10/25 GbE) ports + 8 QSFP28 (100 GbE) uplinks. Less than 500ns port-to-port latency. Common control plane with the PBC.

### How They Work Together

1. Deploy PBC at network boundary (1RU rack install)
2. PBC phones home; operator claims it in PCE dashboard
3. PCE discovers available paths and transport types
4. Operator or customer requests a path between endpoints
5. PCE computes optimal route based on latency, utilization, policy
6. PCE programs PBCs with instructions; no local config
7. PBCs forward deterministically with line-rate encryption
8. PCE collects telemetry continuously and auto-reroutes if needed

**Critical:** After the initial physical deployment, ALL provisioning happens remotely through the PCE. No truck rolls. Path activation in minutes, not months.

---

## Layer 2.5 - How to Explain It

**For technical buyers:**
"Ethernet in, Ethernet out. Cloud and AI data centers run Ethernet because it's the most reliable and scalable standard. We extend that simplicity to the WAN. All path computation is centralized in the PCE - PBCs are stateless forwarders. Layer 3 reach with Layer 2 simplicity. No BGP. No OSPF. No MPLS."

**For business buyers:**
"Your engineering team spends weeks configuring routing protocols every time you add a new connection. With MaiaEdge, configuration is centralized - not at each site. Rack, connect, and go. That's why provisioning that used to take 60-90 days now happens in minutes."

---

## Three Value Pillars

These match the public-facing positioning on maiaedge.io. Every conversation should connect to one of these.

### Pillar 1 - Automate Your Network

Transform fiber islands into a unified network fabric. Provision encrypted private paths in minutes over fiber or DIA. No BGP, no MPLS, no routing protocols in the field. Push-button easy and hardwire simple.
- **Proof:** Arvig (regional fiber, MN) - "almost instantaneous" provisioning per Scott Shekels, Network Engineer.

### Pillar 2 - Federate with Partners

Extend service reach while maintaining sovereignty across network boundaries. Automate NNI provisioning, eliminate manual LOAs, speed service delivery. Reach beyond the network edge. Monetize spare capacity. Interconnect with partners, NaaS fabrics, and clouds while keeping customer ownership in-house.
- **Proof:** Equinix endorsement - "Revolutionary and creative" per Josh Sordelet, Principal PM, Physical Interconnection.

### Pillar 3 - Deliver Cloud On-Ramps

Instantly connect customers to AWS Direct Connect, Azure ExpressRoute, and other major cloud on-ramps without routing complexity. Cloud connectivity becomes a high-margin revenue stream under the operator's brand. Megaport and Equinix Fabric are backend infrastructure leveraged via API - invisible to the end customer.
- **Proof:** RevNet (colo) - "Imagine having Megaport capability between providers."

---

## Fabric of Fabrics

Once an operator has their own fabric, MaiaEdge enables them to extend it through a carrier-neutral marketplace. Three capabilities compound:

- **DCI** - Create an instant private fabric between distributed sites
- **Virtual Cross-Connects** - Spin up cross-connects and private paths in minutes
- **Marketplace** - Extend reach to clouds, SaaS, and AI services. Launch your own connectivity marketplace under the operator's brand.

The strategic compounding effect: every new operator on MaiaEdge expands the reach available to every other operator. Federation creates network effects that no single competitor can replicate.

---

## The Five ICPs (Who Buys MaiaEdge)

Each segment has its own partner cheat sheet. This is the quick map.

| Segment | What they own | What hurts | What MaiaEdge fixes |
|---|---|---|---|
| **Colocation** (standard + AI) | Buildings, meet-me rooms | Stuck on space and power. Tenants leave for Megaport. Cross-connects take weeks | Fabric-in-a-box. Cloud on-ramps under the colo's brand. Self-service cross-connects |
| **Fiber Operator** | Route miles, lit waves, dark fiber | NNIs take 60-90 days. 30-70% of fiber sits dark. Type 2 visibility black holes | Instant partner activation. Dark fiber lit as on-demand services. Hop-by-hop visibility across Type 2 |
| **Network Operator** (Tier 1/2) | National/global infrastructure | Internal automation not unified across domains. Cross-carrier still 60-90 days | Single fabric across internal and partner boundaries. AWS-like provisioning |
| **Neocloud** (GPU cloud) | GPU clusters in leased colos | Inference latency varies by facility. Each enterprise customer is a manual project | Hop-by-hop observability. Deterministic paths between facilities. Instant customer on-ramp |
| **MSP / Aggregator** | Carrier contracts, asset-light | Blind to carriers. Tier 1s going direct. "Depends on the carrier" loses deals | End-to-end visibility. Match Tier 1 speed without capex. AI-ready upstream |

**Priority:** Top 3 are Neocloud, Colocation, Fiber Operator. Network Operator and MSP/Aggregator are secondary.

### How Partner Cheat Sheets Map to maiaedge.io's Three Segments

The public website rolls these five into three buyer audiences. Use the cheat sheet that matches the sales motion, not the website button.

| Website segment (maiaedge.io) | Cheat sheets to use |
|---|---|
| **Service Providers** | Fiber Operator + Network Operator + MSP/Aggregator |
| **AI Cloud and Data Center** | Neocloud + AI Colo signals (in Colocation cheat sheet) |
| **Colocation** | Colocation cheat sheet (standard + AI signals sub-section) |

The five-segment split exists because each has a different buying motion, persona stack, and pitch hook. The website rolls them up for visitor clarity.

---

## Audience-Macro Openers

Three primary audiences. Each opens with a different scene. Pick the one that matches who you're calling on.

### For Service Providers (Fiber, Network Operators, MSPs)
"Ethernet is deployed in islands. There's no simple way to connect them. NNIs take months. Visibility ends at the network edge. MaiaEdge unifies your network first, then extends across operators with one fabric, one control plane. Reach beyond your footprint. Monetize spare capacity."

### For Colocation Operators
"Cross-connects are still manual projects. Tenants want self-service. There's no simple way to connect distributed DCs. End-user demands escalating - especially around AI workloads. MaiaEdge gives you fabric-in-a-box: automated cross-connects, cloud on-ramps under your brand, and a service marketplace your tenants will actually use."

### For AI Cloud / Data Center Operators (Neoclouds + AI Colos)
"Distributed AI factories. The network is the bottleneck. Public internet routes and indirect paths kill inference SLAs. Building a private fiber mesh is months per connection. MaiaEdge gives you an instant private fabric: deterministic paths, hop-by-hop visibility, and instant tenant onboarding across distributed GPU clusters."

---

## What MaiaEdge is NOT - Three Anti-Positions Partners Need to Know

These are the most common partner mistakes. Avoid them.

### NOT a NaaS provider (vs. Megaport, Equinix Fabric, PacketFabric, Console Connect)

NaaS owns the fabric. Customers connect TO their network. NaaS owns the customer relationship and captures interconnection revenue. MaiaEdge is the opposite: infrastructure operators deploy on their OWN network. Operator owns fabric, customer, brand, margin. **Megaport and Equinix Fabric integrate with MaiaEdge as backend infrastructure for cloud on-ramps - they're invisible to the end customer.**

### NOT SD-WAN (vs. Cisco Viptela, VMware VeloCloud, Fortinet)

SD-WAN is for enterprise branches. MaiaEdge is for service providers at carrier scale. Different layer, different buyer. PBCs sit at carrier boundaries, not at branch offices.

### NOT a Router Replacement (vs. Cisco, Juniper, Arista)

Cisco / Juniper / Arista cores stay where they are. PBCs sit at the edge, at customer and partner boundaries, where existing routers can't speed up provisioning. Complementary, not competitive. Centra called it "fabric-in-a-box. Drop it in and add water."

---

## #1 Competitor: Status Quo

Most deals are NOT lost to Megaport or Lumen. They're lost to inertia. The "we'll figure it out next year" answer is what kills more deals than any vendor. Partners who can create urgency around the cost of waiting - deals lost, margin leaking, hyperscaler pressure mounting - are the partners who win.

**Status quo creators:**
- "What deals did you lose last quarter because you couldn't deliver fast enough?"
- "AWS just announced a data center 50 miles from you. Your enterprise customers will need connectivity. Can you deliver before Equinix does?"
- "Every month you wait is another month of margin going to Megaport instead of staying with you."

---

## Commercial Model - How MaiaEdge Sells

**Classification:** Carrier infrastructure (Infrastructure-as-a-Service category, but operators deploy it themselves - they aren't subscribing to MaiaEdge's network).

**Pricing model:** Annual subscription, billed quarterly / monthly / annually. Less frequent billing preferred.

**Spend type:** OpEx, not capex. Hardware title remains with MaiaEdge.

**What's included:** PBC hardware, PCE access, software updates, support, white-label portal, API integrations, telemetry.

### Two-Document Contract Structure

| Document | Purpose |
|---|---|
| **Master Subscription Agreement (MSA)** | Sets the legal framework: licensing, IP, confidentiality, liability, support SLAs, indemnification. Signed once. Governs all future orders. |
| **Order Form** | Specifies commercial terms: SKUs, quantities, pricing, term length, discount. Simple add-on process - no legal renegotiation for additional PBCs. |

**Key MSA terms:**
- Equipment ownership: Title remains with MaiaEdge
- Payment: Net 30 from invoice date. Less frequent billing preferred
- Auto-renewal: Monthly unless 30-day written termination
- Price increases: Capped at greater of 5% or CPI annually (60-day notice)
- Multi-tenant OK: Customer may configure for end customers
- Support SLA: 99.9% availability. Sev 1 acknowledgment within 2 hours. 24/7 ticket system

### SKU Map (List Pricing - Always Confirm Current)

| SKU Category | Bandwidth Options | Term Options |
|---|---|---|
| PBC + PCE Standard | 1G, 10G, 100G | 12 / 36 / 60 months |
| PBC + PCE High Availability | 10G, 100G | 12 months (~70% of standard) |
| Maia Path Port Extender (MPP) | 48-port | 12 / 36 / 60 months |
| POC License | PBC + MPP | 60 days |

**SKU rules:**
- 1G: Standard availability only (no HA)
- 10G: Requires Standard minimum
- 100G: Available in Standard and HA
- HA units priced ~70% of standard, require a primary unit
- Mid-term expansion: existing pricing honored, co-termed to original end date

**Discount discussion:** "Term commitment is the primary lever. 36 or 60-month commitments unlock better per-unit pricing. Volume also matters - more PBCs in the initial order, better discount. What's your planning horizon?"

---

## Founding Team - Use in Live Calls and Proposals

**Reminder for partners:** Credibility anchors are BANNED in cold emails and LinkedIn. They're allowed and recommended in live presentations, demos, proposals, objection handling, and discovery calls.

| Name | Role | Pedigree |
|---|---|---|
| Andy Ory | Executive Chairman | Co-founded Acme Packet ($2.1B to Oracle) and 128 Technology (~$450M to Juniper). Two exits totaling $2.5B+ |
| Patrick MeLampy | CFO and Board Member | CFO at both Acme Packet and 128 Technology exits |
| Abilash Menon | CEO and Co-Founder | Lead architect Acme Packet SBC. Chief Architect 128 Technology SD-WAN. 100+ patents |
| Timothy Ziemer | CRO and Co-Founder | Built commercial orgs at Acme Packet and 128 Technology. Carrier C-suite relationships across the industry |

**The 30-second pedigree pitch:** "MaiaEdge was founded by the same team that built Acme Packet - the Session Border Controller used by 90% of carriers, sold to Oracle for $2.1B - and 128 Technology - the largest acquisition Juniper ever made. Two exits, $2.5B+ combined. The technology that carriers like Lumen rely on was built by this team."

---

## Top Partner Objections (Quick Answers)

| Customer says | Your response |
|---|---|
| "We already use Megaport / Equinix Fabric" | "Right - and those are now backend infrastructure you can leverage by API. MaiaEdge gives you Megaport's reach under your brand. The end customer sees your portal, your invoice." |
| "We don't have engineering for this" | "No routing protocols, no BGP, no MPLS. PBCs are stateless. The PCE handles all path computation. One operator called it 'drop it in and add water.'" |
| "We could build this ourselves" | "Most teams quote 18-24 months and several million in development. MaiaEdge has already done that work - same team that built Acme Packet and 128 Technology. Why rebuild what exists?" |
| "Sounds expensive" | "Compare to what's leaking. Margin going to Megaport on every customer cloud connection. Deals lost to 6-week provisioning. OpEx subscription, scales with the business." |
| "Why haven't I heard of you?" | "Equinix called us 'revolutionary and creative.' We're carrier infrastructure - sold to operators, not enterprises. The team has $2.5B in combined exits in this space." |

---

## How Partners Engage MaiaEdge

| Action | How |
|---|---|
| Register a deal | Partner page deal registration. 30-day protection. AM-approved within 24 hours |
| Request a quote | cooperkennedy@maiaedge.io |
| Co-sell support, technical questions | timziemer@maiaedge.io |
| Schedule a customer demo | Through deal registration or by emailing the relevant lead above |
| Get the latest sales deck | Partner page (current version) |

---

## What's Next

Read the segment cheat sheet that matches the customer you're calling on. Each one has the discovery questions, hooks, objections, and personas specific to that segment.

- **Colocation Operator** - including AI Colo
- **Fiber Operator** - regional CLEC, long haul, dark fiber, muni/co-op
- **Network Operator** - Tier 1 / Tier 2 carriers
- **Neocloud** - GPU cloud providers
- **MSP / Aggregator** - TSDs, TAs, NaaS Platform Operators

---

*MaiaEdge - Carrier infrastructure for federated private networking. Private paths. Any network. Instantly.*
