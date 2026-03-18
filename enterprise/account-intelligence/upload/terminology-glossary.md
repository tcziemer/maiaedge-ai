# MaiaEdge Terminology Glossary

> Originally converted from: MaiaEdge_Terminology_Glossary.docx (OneDrive)
> Updated: February 2026 (V4 alignment — carrier infrastructure terminology, neocloud terms, cloud on-ramp additions)

Terminology & Glossary
8.1 MaiaEdge Terms
Our vocabulary - terms specific to MaiaEdge products and positioning.

8.2 Infrastructure Terms
What customers own - physical and leased infrastructure vocabulary.

8.3 Network Terms
Technical concepts - routing protocols and network architecture vocabulary.

8.4 Business Terms
Commercial concepts - contract and billing vocabulary.

8.5 Competitor / Market Terms
Industry context - competitors and market players.

8.6 When to Use Technical vs. Business Language
Audience adaptation - matching vocabulary to buyer persona.
Technical Audience (CTO, VP Engineering, Network Ops)
Use precise technical terms. They want specifics.
Say: "PBC with dual 100G interfaces, stateless forwarding, line-rate AES-256-GCM encryption"
Say: "Deterministic paths computed by the PCE - no BGP/OSPF/MPLS required"
Say: "Hop-by-hop telemetry across Type 2 circuits for end-to-end SLA visibility"
Say: "Q-in-Q tagging for multi-tenant isolation, Mac-in-Mac for core scalability"
Say: "SRLG-aware path computation for physically diverse backup routes"
Technical Pain Language: "Every NNI is a 60-90 day project - LOAs, VLAN coordination, BGP config. By the time we're live, the opportunity has moved on."
Business Audience (CEO, CFO, VP Sales, VP Business Development)
Focus on outcomes. Translate technical capabilities to business impact.
Say: "Provision in minutes instead of 60-90 days"
Say: "Keep customer relationships and revenue instead of handing them to Megaport"
Say: "Your brand on the portal, your roadmap, your margin"
Say: "Win deals you're currently losing to slower competitors"
Say: "Monetize dark fiber that's currently a sunk cost"
Business Pain Language: "We're losing multi-state deals because we can't deliver outside our footprint fast enough. By the time we coordinate with partners, the customer has moved on."
Translation Quick Reference
Golden Rule: Technical buyers want to know HOW it works. Business buyers want to know WHY it matters to their revenue, customers, and competitive position.

Term | Definition
PBC | Path Border Controller. A 1RU hardware appliance deployed at network boundaries (meet-me rooms, carrier hotels, PoPs). Dual 100G interfaces, stateless forwarding, line-rate AES-256-GCM encryption, <2 microsecond latency overhead.
PCE | Path Computation Engine. Cloud-native orchestrator that computes optimal paths, manages telemetry, and provides the white-label customer portal. The "brain" of a MaiaEdge fabric.
Path | A deterministic, encrypted connection between two endpoints on a MaiaEdge fabric. Unlike traditional circuits, paths are computed centrally and can span multiple operators through federation.
Fabric | The network of PBCs interconnected and managed by a PCE. A fabric can span a single operator or federate across multiple operators.
Federation | Instant interconnection between MaiaEdge-enabled operators. Deploy PBCs at partner boundaries, exchange access codes, and the PCE computes paths across both networks. No BGP peering, no VLAN spreadsheets, no 60-90 day projects.
Sovereignty | Complete ownership of customer relationships, billing, brand, and roadmap. Unlike NaaS platforms where you're a supplier, MaiaEdge lets you maintain sovereignty while accessing federation benefits.
Layer 2.5 | MaiaEdge's position on the OSI model - merging Layer 2 (Ethernet simplicity) with Layer 3 (IP reach). Uses Q-in-Q for multi-tenant isolation and Mac-in-Mac for core scalability. No BGP/OSPF/MPLS required.
WAN-Ethernet | Extending Ethernet's simplicity beyond the LAN into the WAN. The technical foundation of MaiaEdge - deterministic paths with Ethernet-like ease of use across wide area networks.
Fabric-in-a-Box | Our positioning for the complete MaiaEdge solution - hardware (PBC) + software (PCE) + portal ready to deploy. Centra: "Drop it in and add water and it works."
Federated Marketplace | A carrier-neutral marketplace where providers can publish services and consume capacity from federated partners. The long-term vision for MaiaEdge network effects.
Federation Flywheel | The virtuous cycle: Automate → Speed → Visibility → Trust → Revenue → Automate. Each operator that joins the federation makes the network more valuable for all participants.
Inverted Messaging Hierarchy | Neocloud-specific messaging order: (1) Observability, (2) Cloud On-Ramp, (3) Deterministic Paths. Unlike all other segments where deterministic paths lead, neoclouds respond to "see why you're slow" before path engineering. See Messaging Framework V4, Section 3.3.

8.1a Neocloud & AI Terms
Neocloud | GPU cloud provider — owns massive GPU clusters distributed across multiple colo facilities, sells compute capacity (training and inference). Examples: CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI, Nebius, Groq, Cirrascale, DeepInfra, Vultr, DigitalOcean, Fluidstack, Modal, Nscale, Firmus, E2E Networks, Yotta. Key distinction: neoclouds ARE the end customer. Do NOT use "keep your customer" language. Sub-segments: Large-Scale GPU NeoClouds, Tier 1 Inference Providers, AI Infrastructure Providers, Sovereign AI Clouds, Crypto-to-AI Pivots. See Neocloud Cheatsheet for detailed profiles.
Recompute Tax | The cost of restarting distributed training jobs after a network interruption forces checkpoint rollback. At $4,800/GPU/month with a 30% interruption rate on 128K context Llama-3 70B, the recompute cost dwarfs any networking investment. MaiaEdge eliminates recompute tax with deterministic, jitter-free paths.
Crypto-to-AI Pivot | Companies transitioning from cryptocurrency mining to AI compute (e.g., IREN/Iris Energy, Core Scientific, Northern Data Group, TeraWulf). They have power and facilities but legacy crypto infrastructure wasn't built for AI traffic patterns. Minimal networking sophistication — lead with observability.
GPU-as-a-Service | The primary neocloud business model — renting GPU compute by the hour or via reserved instances. MaiaEdge relevance: deterministic paths between GPU clusters ensure consistent inference performance.
Inference | AI model execution (as opposed to training). Token-by-token generation is sequential, latency-sensitive, and intolerant of jitter. The network becomes part of the compute loop. MaiaEdge delivers the deterministic transport layer that makes distributed inference predictable.
Distributed Inference Fabric | Deterministic paths between GPU clusters across multiple colo facilities, creating a unified compute fabric with consistent performance regardless of facility location.
Sovereign AI | AI infrastructure where customers can prove data stays within specific geographic boundaries. MaiaEdge enables provably private paths with geographic routing guarantees.
RAG (Retrieval-Augmented Generation) | AI architecture that retrieves external data during inference. Requires multi-cloud data access — a cloud on-ramp use case for neoclouds.

8.1b Cloud On-Ramp Terms
Cloud On-Ramp (MaiaEdge) | Operators deliver cloud connectivity (AWS Direct Connect, Azure ExpressRoute, GCP Cloud Interconnect) under their own brand via MaiaEdge API integrations with Equinix Fabric and Megaport as backend infrastructure. Customers buy from the operator; Equinix/Megaport are invisible backend fabric.
Shared Port Economics | Multiple customers share a single Equinix Fabric or Megaport port, with bandwidth commitments and service tiers enforced per tenant by MaiaEdge. Each new customer adds higher-margin revenue against a fixed cost base.
Service Tiers (Cloud On-Ramp) | Gold (guaranteed bandwidth, strict QoS), Silver (high-priority with controlled oversubscription), Bronze (best-effort for SaaS, dev/test, backup). See Cloud On-Ramp Business Case for pricing.
Dynamic NNI | A temporary NNI over a DIA circuit that can be stood up immediately while a physical interconnect is being built. Enables revenue generation during the 90–120 day physical NNI build.

Term | Definition
Dark Fiber | Fiber optic cable that has been installed but is not yet "lit" with active electronics. The customer provides their own optical equipment. Often leased via IRU agreements.
Lit Fiber / Lit Services | Fiber with active electronics providing bandwidth services. The carrier manages the optical equipment and sells capacity (wavelengths, Ethernet services).
IRU | Indefeasible Right of Use. Long-term lease (typically 15-25 years) for dark fiber capacity. The lessee has exclusive use but doesn't own the physical asset.
Type 2 Circuit | Leased capacity from another carrier to extend reach beyond owned infrastructure. Key pain point: operators lose visibility once traffic enters a Type 2 circuit. MaiaEdge provides end-to-end visibility across Type 2s.
Route Miles | Total distance of fiber network measured along the route path. Industry benchmark: Regional operators typically have 1K-50K route miles. Lumen has ~340K, AT&T has 1M+.
PoP | Point of Presence. Physical location where a carrier has network equipment - typically in a carrier hotel, data center, or central office. PBCs deploy at PoPs.
Meet-Me Room | Secure area within a data center where different carriers interconnect. Cross-connects are made here. Primary deployment location for PBCs in colocation facilities.
Carrier Hotel | A data center specifically designed for carrier interconnection (e.g., 60 Hudson Street NYC, One Wilshire LA). High density of carriers makes these ideal for federation.
Cross-Connect | Physical cable linking two networks within a data center. Traditional cross-connects require manual provisioning and LOAs. MaiaEdge automates the logical equivalent.
Metro Ring | Fiber network connecting multiple sites within a metropolitan area. Typically provides redundancy through ring topology. Common infrastructure for colocation operators.
Cloud On-Ramp | Direct, private connectivity to hyperscaler cloud services (AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect). Key use case: MaiaEdge enables operators to offer cloud on-ramps under their own brand via API integrations with Equinix Fabric and Megaport.
Last Mile | The final leg of connectivity from a carrier's network to the end customer premises. Typically handled by local providers or enterprise equipment. SD-WAN operates here; MaiaEdge operates in the middle mile.
Middle Mile | The network segment between last mile access and long-haul backbone - where regional carriers, colos, and fiber operators interconnect. This is where MaiaEdge operates, solving middle-mile complexity that SD-WAN and enterprise tools cannot address.
Backhaul / Mobile Backhaul | Connectivity from cell towers or access points back to the carrier's core network. Key use case: IENTC uses MaiaEdge to connect 800+ cell towers to 20+ data centers in Mexico. High-scale, latency-sensitive application.
Term | Definition
NNI | Network-to-Network Interconnect. Connection between two carrier networks. Traditional NNIs require 60-90 days of LOAs, VLAN coordination, BGP configuration. MaiaEdge federation eliminates this friction.
UNI | User Network Interface. The service demarcation point where a carrier network connects to a customer's equipment. Defines the handoff point for SLA responsibility.
ENNI | External Network-to-Network Interface. Standardized interconnection point between carriers, defined by MEF. MaiaEdge PBCs can function as ENNI demarcation points.
BGP | Border Gateway Protocol. The routing protocol that runs the internet - exchanges routes between autonomous systems. Requires configuration at every hop, reconvergence time when things change. MaiaEdge eliminates BGP complexity.
OSPF | Open Shortest Path First. Interior routing protocol for finding paths within a network. Another protocol MaiaEdge eliminates with centralized path computation.
MPLS | Multi-Protocol Label Switching. Traditional carrier technology for traffic engineering and VPNs. Complex to configure, requires specialized expertise. MaiaEdge provides similar capabilities without MPLS complexity.
VLAN | Virtual Local Area Network. Method of segmenting network traffic. VLAN coordination between carriers is a major source of NNI provisioning delays that MaiaEdge eliminates.
DIA | Dedicated Internet Access. A direct internet connection with guaranteed bandwidth. Common service offering for fiber operators and colos.
Wavelength | A specific frequency of light on a fiber strand. DWDM (Dense Wavelength Division Multiplexing) puts 80-96 wavelengths on a single fiber. Selling wavelengths is a common fiber operator revenue model.
Layer 2 / Layer 3 | OSI model layers. Layer 2 = Ethernet switching (MAC addresses). Layer 3 = IP routing (IP addresses). MaiaEdge operates at "Layer 2.5" - Ethernet simplicity with IP reach.
EVC | Ethernet Virtual Connection. Logical Layer-2 circuit between two or more UNIs. MEF-defined service type. MaiaEdge paths can deliver EVC-equivalent services.
DCI | Data Center Interconnect. Connectivity between data centers for storage replication, disaster recovery, or distributed applications. High-bandwidth, low-latency use case.
VNO | Virtual Network Operator. Carrier that provides network services using leased infrastructure rather than owned fiber. VNOs depend on underlying carriers for capacity, making visibility across multiple networks a key pain point MaiaEdge solves.
Tier 1 / Tier 2 Carrier | Tier 1: Global carriers with settlement-free peering (Lumen, AT&T, Verizon). Tier 2: Regional carriers that peer with Tier 1s for global reach. Most MaiaEdge prospects are Tier 2 or regional operators competing against Tier 1s.
CIR / EIR | Committed Information Rate / Excess Information Rate. CIR is guaranteed bandwidth; EIR is burst capacity available when network permits. Key parameters in bandwidth profiles and service contracts.
Bandwidth Profile | Defines the traffic parameters for a service: CIR, EIR, and burst sizes applied at the UNI. Determines what the customer is paying for and what SLAs apply.
CoS (Class of Service) | Traffic prioritization based on PCP/DEI bits, mapped into queues for latency/jitter control. Allows different traffic types (voice, video, data) to receive appropriate handling.
E-Line / E-LAN | MEF-defined Ethernet service types. E-Line: Point-to-point connection between two UNIs (most common). E-LAN: Multipoint connection linking multiple UNIs (hub-and-spoke or mesh). MaiaEdge paths can deliver both service types.
Term | Definition
NaaS | Network-as-a-Service. On-demand network connectivity delivered as a service (Megaport, Equinix Fabric). Key positioning: NaaS providers own the customer relationship. MaiaEdge lets YOU own it.
Carrier Infrastructure | MaiaEdge's identity — purpose-built carrier infrastructure that network operators deploy to automate private path provisioning, gain end-to-end visibility, and federate with partners. NOT a NaaS platform, NOT a software overlay. Operators deploy PBC hardware and subscribe to the PCE platform. OpEx subscription model. DEPRECATED TERM: "IaaS" / "Infrastructure-as-a-Service" — do not use. Use "carrier infrastructure" instead.
SLA | Service Level Agreement. Performance commitments (latency, jitter, packet loss, availability). MaiaEdge telemetry enables proving SLA compliance across owned AND leased infrastructure.
LOA | Letter of Authorization. Document authorizing a carrier to make cross-connects on your behalf. LOA processing is a major bottleneck in traditional provisioning - often 2-4 weeks alone.
MRC | Monthly Recurring Cost. The recurring charge for a service. MaiaEdge uses MRC-based pricing for predictable OpEx.
NRC | Non-Recurring Cost. One-time charges (installation, activation). MaiaEdge minimizes NRCs through subscription model.
ARR / MRR | Annual / Monthly Recurring Revenue. Key SaaS/subscription metrics. MaiaEdge targets help customers grow their ARR through new connectivity services.
OAM | Operations, Administration, and Maintenance. Standards for managing carrier Ethernet services. PCE provides OAM-equivalent visibility.
MEF / Mplify | Metro Ethernet Forum. Industry standards body for Carrier Ethernet. Mplify is their LSO Sonata API certification program. PCE is MEF/Mplify compatible.
OSS / BSS | Operations Support Systems / Business Support Systems. The back-office platforms carriers use for service provisioning, billing, inventory, and customer management. MaiaEdge integrates via API - "Your ordering triggers us; lifecycle events flow to your billing." Key differentiator vs. orchestration platforms: no complex OSS/BSS integration project required.
Term | Description & MaiaEdge Positioning
Megaport | Global NaaS platform. Instant cloud connectivity. Position: Backend infrastructure that operators leverage via MaiaEdge API integrations. When used directly by operators, Megaport owns the customer relationship, pricing, and margin. With MaiaEdge, operators use Megaport's reach while keeping the customer, the brand, and the margin. "Own the on-ramp. Megaport becomes your backend infrastructure."
Equinix Fabric | Largest global interconnection platform. Data center + fabric combined. Position: Same as Megaport — backend infrastructure operators leverage via API. PCE integrates with Equinix Fabric APIs. Operators share a single fabric port across multiple customers with MaiaEdge enforcing per-tenant service tiers.
PacketFabric | Software-defined network platform. Self-service interconnection. Position: Another NaaS where customers become their customer, not yours.
Console Connect | PCCW Global's NaaS platform. Position: Another NaaS where customers become their customer, not yours.
Lumen PCF | Private Connectivity Fabric. AWS partnership announced Q4 2024; AWS Interconnect Last Mile in gated preview November 2025. ~340K route miles, 163K+ buildings, 400G backbone. Direct competitor going after enterprise connectivity. Position: "Lumen builds their empire. MaiaEdge empowers you to build yours." HubSpot tag: #COMPETITION_PRIVATE_FABRIC
SD-WAN | Cisco Viptela, VMware VeloCloud, Fortinet. Enterprise branch connectivity. Position: "SD-WAN is for enterprises managing branches. We're built for service providers at carrier-scale." MaiaEdge can be the fabric layer underneath managed SD-WAN services.
Ciena Blue Planet | Multi-vendor orchestration platform. Position: Complex integration project (6-12 months, $1-5M+) vs. MaiaEdge "fabric-in-a-box" (30-60 days, OpEx subscription).
Nokia NSP / Juniper Paragon | Network services orchestration platforms. Position: Same as Ciena - complex enterprise software vs. purpose-built fabric solution. 6-18 month deployments vs. weeks.
Hyperscalers | AWS, Azure, Google Cloud. Building direct enterprise connectivity (AWS Interconnect, Azure ExpressRoute). Threat: Going direct to enterprise, cutting regional operators out. Opportunity: Enterprises near new hyperscaler facilities need connectivity - fast.
Technical Version | Business Version
Path Border Controller (PBC) | Edge hardware that enables instant connectivity
Path Computation Engine (PCE) | Cloud platform that automates everything
Deterministic paths, protocol-free forwarding | Instant provisioning, no complexity
Line-rate AES-256-GCM IPsec encryption | Enterprise-grade security built in
Hop-by-hop telemetry across Type 2 circuits | See performance everywhere, prove SLAs
Eliminates BGP/OSPF/MPLS complexity | No specialized engineering required
API integration with Equinix/Megaport | Cloud connectivity under your brand
Instant NNI activation through federation | Partner with anyone in days, not months
Multi-tenant isolation with Q-in-Q | Each customer stays separate and secure