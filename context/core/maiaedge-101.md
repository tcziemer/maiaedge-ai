# MaiaEdge 101 — Product Knowledge Guide

> Converted from: MaiaEdge101.docx (OneDrive)


MaiaEdge 101
Product Knowledge Guide for Sales Enablement


Building the private internet, together.
December 2025 | Confidential

1.1 The 30-Second Pitch
Vision Statement
Federated Private Networking: where any network operator can instantly provide private connectivity anywhere, while maintaining sovereignty.
Mission Statement
Provide the infrastructure for network operators to build a Federated Private Network. With purpose-built infrastructure, we make it possible for service providers to work together, share reach, automate delivery, and expand coverage, without giving up their customer relationships. Federation with sovereignty intact, that's Federated Private Networking.
Category Definition
Carrier Infrastructure for enabling Federated Private Networking
Tagline (Hero Statement)
Private paths. Any network. Instantly.
One-Sentence Description (Sub-Hero)
Carrier automation stops at the network edge. With purpose-built infrastructure, MaiaEdge enables carriers to extend automation and visibility across their own fragmented footprint and across external network boundaries. With MaiaEdge, operators can share infrastructure to offer services no single provider could offer alone, while maintaining complete visibility and sovereignty over every customer relationship.
Positioning Statement
For network operators with fragmented networks, MaiaEdge delivers the only purpose-built infrastructure that automatically interconnects disconnected networks into one cohesive fabric, so they can activate private paths anywhere, instantly.
The "Only" Statement
Only MaiaEdge provides the infrastructure that enables network operators to extend services across domains instantly, over any transport, while maintaining complete visibility and sovereignty.
1.2 The Problem We Solve
Network Isolation is the $10 billion problem no one is talking about.
Network operators are all fighting the same invisible enemy. Inside your own walls, you have APIs, orchestration, and zero-touch provisioning. But that automation is blind beyond your edge. Once traffic leaves your domain, modern orchestration dissolves into the "polite chaos" of spreadsheets, emails, and manual coordination, while visibility and SLA control vanish. This friction results in 60-90 day turn-ups, stranded capacity, and expensive SLA penalties.
Before/After Comparison

Core Insight: "Customers don't need a new use case, they need to do what they're already doing, but faster, with more visibility, and without giving up control."
1.3 What We Sell
Two Core Components

Commercial Model Summary
Classification: Infrastructure as a Service (carrier infrastructure)
Pricing Model: Annual subscription, billed quarterly/monthly/annually – less frequent billing preferred 
Spend Type: OpEx (not CapEx),  hardware title remains with MaiaEdge
What's Included: PBC hardware, PCE access, software updates, support, white-label portal, API integrations, telemetry

1.4 PBC Deep Dive
The Path Border Controller (PBC) is the edge infrastructure, a single 1RU device that sits at network boundaries. It merges L2 switching and L3 routing to enable secure, high-throughput private ethernet paths without running routing protocols in the field.
Key Specifications

How the PBC Works
The PBC is a stateless forwarder. It doesn’t make routing decisions—all path computation happens centrally in the PCE. The PBC simply executes the instructions it receives. This stateless design means simpler failure recovery: if a PBC fails, there’s no complex state to rebuild. Traffic can be rerouted immediately by the PCE without waiting for routing protocols to reconverge.
Dual 100G Interfaces Explained
The two 100G interfaces provide both high throughput and redundancy. In a typical deployment, one interface connects to the customer/tenant side while the other connects to the network/transport side. This architecture supports failover scenarios and enables the PBC to handle traffic from multiple directions simultaneously.
Line-Rate Encryption
Every path through the PBC is encrypted end-to-end with AES-256-GCM IPsec. “Line-rate” means encryption happens at wire speed—there’s no throughput penalty for enabling security. Unlike traditional VPN approaches where encryption creates bottlenecks, the PBC encrypts all traffic without performance degradation. This is critical for latency-sensitive applications and high-bandwidth workloads.
Why <2μs Latency Matters
Traditional routers introduce milliseconds of latency overhead as they process packets through complex routing stacks. The PBC’s <2 microsecond overhead is orders of magnitude faster because there’s no routing protocol processing—just deterministic forwarding based on instructions from the PCE. For applications like financial trading, real-time video, or distributed AI workloads, this difference is significant.
Switch Pairing (Colocation Deployments)
In colocation environments, the PBC is paired with a fully managed switch that fans out to tenant cross-connect ports. Ports remain inactive until assigned to a tenant in the PCE, ensuring security and control. This “fabric-in-a-box” approach lets colo operators deploy interconnection capability without building complex infrastructure.
High Availability Architecture
PBCs support redundant active/standby architecture. HA units are priced at approximately 70% of standard units and can be added to any deployment for failover capability. Additionally, PBCs operate independently if the cloud control plane goes offline—they continue forwarding traffic based on their last received instructions until connectivity to the PCE is restored.
What PBCs Do NOT Do
NOT a router replacement: PBCs complement core routers, they don't replace Cisco/Juniper/etc
NOT SD-WAN: SD-WAN sits at enterprise branches; PBCs sit at carrier boundaries
NOT making routing decisions: All path decisions made by PCE; PBCs just execute
Key Point: After physical deployment, all provisioning happens remotely through PCE, no truck rolls.
1.5 PCE Deep Dive
The Path Computation Engine (PCE) is the cloud-based orchestrator. It calculates deterministic end-to-end paths across networks, enforces policy, and provides unified visibility regardless of underlying transport.
Key Capabilities
How the PCE Thinks
The PCE looks at network nodes, NOT protocols. It sees the source and destination and finds the best optical and transport paths dynamically. Unlike traditional routing where each device makes independent decisions based on protocol advertisements, the PCE has a global view of the entire network topology and computes paths centrally. This centralized approach eliminates the “distributed chaos” of traditional routing where changes propagate hop-by-hop and convergence can take seconds or minutes. With PCE, path changes are instantaneous and deterministic.
Path Tagging and Visibility
Every packet carries its origin and route, ensuring visibility and traceability across the network. This path tagging is what enables end-to-end observability even across networks you don’t own (Type 2 circuits, partner networks). Traditional routing loses visibility at network boundaries with MaiaEdge, you see every hop.
SLA-Aware Routing
The PCE optimizes paths based on actual performance metrics, not just shortest-path or lowest-cost calculations. It considers latency requirements, jitter sensitivity, packet loss thresholds, bandwidth needs, and policy constraints. When conditions change, the PCE automatically recalculates and reroutes without manual intervention.
Automatic Failover
With SLA-based monitoring, failover is automatic and maintains session integrity during outages. If a path degrades or fails, the PCE detects the issue via continuous telemetry, computes an alternate path meeting SLA requirements, reprograms affected PBCs, and reroutes traffic within seconds. No manual intervention. No ticket escalation. No waiting for routing protocols to converge.
What Telemetry is Collected
The PCE continuously monitors and reports: Real-time SLA metrics (latency, loss, jitter per path), path performance history for capacity planning and trend analysis, utilization data showing current bandwidth consumption across all paths, and health status for per-PBC and per-path availability. This data is available through the portal dashboard and via API for integration with existing monitoring systems.
Multi-Tenant Isolation
The PCE provides complete isolation between tenants through separate logical views per customer, role-based access controls, isolated telemetry and configuration, and API-first design for programmatic access. Operators maintain oversight and visibility across all tenants while customers see only their own paths and metrics.

1.6 How PBC + PCE Work Together
Technical Flow
Deploy PBC: Install 1RU appliance at network boundary
Claim in PCE: PBC phones home; operator claims device in dashboard
Define Topology: PCE discovers available paths and transport types
Configure Service: Operator/customer requests a path between endpoints
PCE Computes Path: Calculates optimal route based on latency, utilization, policy
PCE Programs PBCs: Instructions pushed to all PBCs - no local config needed
Traffic Flows: PBCs forward deterministically with line-rate encryption
Continuous Monitoring: PCE collects telemetry, auto-reroutes if needed
CRITICAL: After initial physical deployment, ALL subsequent provisioning happens remotely through PCE. No truck rolls. Path activation in minutes, not months.
The Layer 2.5 Foundation
MaiaEdge operates at what we call “Layer 2.5” extending Ethernet’s simplicity beyond the LAN into the WAN with added intelligence for multi-hop routing, encryption, and multi-tenancy. It’s Ethernet in, and Ethernet out. Cloud and AI data centers leverage Ethernet because it’s the most reliable and scalable standard in the world—we’re extending that same Ethernet scalability to the WAN.
Q-in-Q: Handles multi-tenant tagging so every customer remains isolated
Mac-in-Mac: Ensures the core network scales without the usual limitations of traditional carrier infrastructure
The result: Layer 3 reach with Layer 2 simplicity. No BGP. No OSPF. No MPLS complexity.
Dynamic Path Selection
If fiber conditions change or links fail, traffic is steered deterministically over alternate fiber or DIA paths within seconds. The PCE continuously monitors all paths and automatically reroutes based on real-time performance metrics, SLA requirements, policy constraints, and available capacity. This happens without manual intervention and without waiting for routing protocols to reconverge.
Zero-Touch Turn-Up
Services are created, validated, and activated automatically—no CLI sessions or ticket queues. Once PBCs are physically deployed, the entire service lifecycle is managed through the PCE: path creation, bandwidth changes, failover configuration, customer onboarding, and service decommissioning.
Mix Fiber + DIA Seamlessly
MaiaEdge lets operators combine leased lines, dark fiber, and DIA within a unified fabric—all encrypted end-to-end with AES-256-GCM IPsec. Start with DIA for instant connectivity, add fiber when available, and keep DIA as automatic failover. One fabric, any transport. The PCE abstracts the underlying transport type—customers see deterministic paths while operators choose the most cost-effective transport for each segment.
Resilience When PCE is Unreachable
PBCs operate independently if the cloud control plane goes offline. They continue forwarding traffic based on their last received instructions until connectivity to the PCE is restored. This means no service interruption during PCE maintenance, traffic continues flowing during network partitions, and local forwarding decisions don’t depend on real-time PCE communication.

1.7 Layer 2.5 / WAN-Ethernet Explained

How to Explain to Technical Buyers
"It's Ethernet in, and Ethernet out. Cloud and AI data centers leverage Ethernet because it's the most reliable standard - we're extending that same scalability to the WAN. All path computation happens centrally in the PCE. The PBCs are stateless forwarders. Layer 3 reach with Layer 2 simplicity."
How to Explain to Business Buyers
"Your engineering team spends weeks configuring routing protocols every time you add a new connection. With MaiaEdge, configuration happens centrally - not at each site. Rack, connect, and go. That's why provisioning that used to take 60-90 days now happens in minutes."

1.8 Three Value Pillars
Most conversations should connect to one of these pillars unless a niche use case is being discussed.
Pillar 1: Speed & Simplicity (AUTOMATE)
Activate deterministic private paths instantly, with protocol-free simplicity. No BGP, no MPLS.
Proof: Arvig (Fiber, MN): "Almost instantaneous" provisioning
Pillar 2: Visibility & Sovereignty (FEDERATE)
Extend reach through carrier partnerships while maintaining visibility and customer sovereignty.
Proof: Equinix: "Revolutionary and creative" - Josh Sordelet, Principal PM
Pillar 3: Revenue & Federation (MONETIZE)
Turn infrastructure into revenue. Monetize idle fiber and offer cloud connectivity under your brand.
Proof: RevNet (Colo, DFW): "Imagine having Megaport capability between providers"

### Marketplace Seeding Strategy

**Priority Order:**
1. **Ashburn** (70–80% of traffic) — Atlantec has ports
2. **Silicon Valley / LA** — Atlantec has ports
3. **Seattle / Dallas / Chicago** — Arvig covers Chicago
4. **European PoP** — CMC Networks, Ecotel, IENTC deployments

**Approach:** Marketplace needs inventory before it has value (iPhone analogy: ship with mail and browser before App Store). Free PBC gear until breakeven for seeders removes risk.

**ConnectBase Integration:** The phone book of fiber ownership. Billions of addresses showing which operators serve each building. Will show which operators have PBCs, enabling instant connectivity. Operators without PBCs lose deals.
1.9 Commercial Model & Contract Structure
The goal is to sell ONE Master Subscription Agreement (MSA) that serves as the framework for adding PBCs over time—without requiring sales negotiations for each addition.
Two-Document Structure

Why This Matters: Once MSA is signed, adding more PBCs is a simple Order Form - no legal review, no sales cycle. Customer can scale deployment without friction.
Key MSA Terms to Know
Equipment Ownership: Title remains with MaiaEdge (carrier infrastructure model). Customer has full control over installation and relocation
Payment Terms: Invoiced annually/quarterly/monthly in advance, Net 30 from invoice date – less frequent billing is preferred on our end
Auto-Renewal: Subscription auto-renews monthly unless 30-day written termination notice
Price Increases: Capped at greater of 5% or CPI annually (with 60-day notice)
Multi-Tenant OK: Customer may configure MaiaEdge in multi-tenant environment for their end customers
Support SLA: 99.9% Service Availability. Sev 1 acknowledgment within 2 hours. 24/7 ticket system

International Delivery Terms
For international customers (like IENTC in Mexico), the quote includes specific terms:
Delivery: FCA Burlington, MA (Incoterms 2020) - risk transfers to customer at carrier pickup
Importer of Record: Customer acts as Importer of Record-handles all customs documentation
Taxes/Duties: Customer responsible for all taxes, duties, tariffs, VAT - not included in quote
1.10 Pricing & SKU Reference
Current list prices as of December 2025. All prices USD.
Path Border Controller (PBC + PCE) — Standard

High Availability (Standby) Units
Note: HA units are priced at ~70% of standard units. Add to any deployment for failover capability.

Maia Path Port Extender (MPP) & POC

Pricing Notes & Dependencies
Key rules and constraints for quoting. Add this section after the SKU tables in MaiaEdge101.
SKU Configuration Rules
Not all SKU combinations are valid. The product has 192+ possible configurations across these dimensions:
Configuration Constraints:
1G bandwidth: Standard availability only (no HA option at 1G)
10G bandwidth: Requires Standard availability minimum
100G bandwidth: Available in both Standard and HA configurations
HA units are priced at ~70% of standard units and require a primary unit
Mid-Term Expansion Pricing
When a customer adds PBCs during an active contract term:
Honor existing pricing: Expansions use the pricing from the original Purchase Agreement (no renegotiation)
Co-termination: New PBCs align to the original contract end date, not a new 12/36/60-month term
Pro-rated billing: Customer pays for remaining months in the contract term only
Example: Customer signed a 36-month deal in January 2025 for 3 PBCs at $25,000/unit. In July 2025 they want to add 2 more PBCs. They pay $25,000/unit (original pricing), pro-rated for the 30 months remaining, co-termed to January 2028.
Example: IENTC Quote Breakdown
Real example from first customer (November 2025):
Key Notes: 
Prices exclude taxes, duties, shipping, and import fees
Payment: Billed quarterly in advance, Net 30
Hardware is service equipment—title remains with MaiaEdge
Quote valid 30 days, subject to credit approval

Discount Discussion Tips
"Term commitment is the primary lever. A 36 or 60-month commitment unlocks better per-unit pricing. Volume also matters - the more PBCs in the initial order, the better the discount. What's your planning horizon?"





Dimension | Traditional Approach | With MaiaEdge
Provisioning | 60-90 days of manual configuration, LOAs, VLAN negotiations, BGP configuration | Automated provisioning. Establish NNIs in minutes. No protocols in the field
Visibility | Traffic leaves boundary, visibility lost. Middle-mile blind spots | End-to-end visibility across boundaries. Hop-by-hop telemetry
SLA Enforcement | Limited ability to enforce SLAs over Type 2 circuits | Enforce SLAs across partner circuits automatically
Customer Sovereignty | Hand customers to NaaS fabrics, lose relationships | Cloud on-ramps without surrendering customers. Your brand
Path Border Controller (PBC) | Path Computation Engine (PCE)
The Edge Hardware
1RU device at network boundaries (carrier hotels, meet-me rooms, PoPs) | The Cloud Orchestrator
Cloud-native intelligence that calculates deterministic end-to-end paths
Specification | Detail
Form Factor | 1RU appliance
Interfaces | Dual 100 Gbps full-duplex interfaces
Encryption | Line-rate AES-256-GCM IPsec encryption
Latency Overhead | <2μs latency overhead
Forwarding Model | Stateless, protocol-free, deterministic forwarding
Protocols Required | None, no BGP, OSPF, or MPLS required
Capability | Description
Path Computation | Real-time calculation of optimal, deterministic paths
Multi-Domain Orchestration | Automate provisioning across owned + partner networks
Telemetry | Hop-by-hop visibility (jitter, loss, latency)
API Integrations | Equinix Fabric, Megaport, AWS, Azure, GCP
White-Label Portal | Self-service portal for customers under your brand
Layer | Characteristics
Layer 2 | Simple, fast, works great within a building. Limited to LANs
Layer 3 | Scalable across WANs using BGP, OSPF, MPLS. Complex configuration
Layer 2.5 | Ethernet simplicity extended to WAN. No protocols in field. Centralized computation
Document | Purpose
Master Subscription Agreement (MSA) | Sets the legal framework: licensing terms, IP, confidentiality, liability, support SLAs, indemnification. Signed once, governs all future orders within selected term length.
Order Form | Specifies commercial terms: SKUs, quantities, pricing, term length, discount. Simple add-on process—no legal renegotiation.
SKU | Bandwidth | Term | List Price
ME-PBC-PCE-100G-12M | 100G | 12 months | $29,900
ME-PBC-PCE-100G-36M | 100G | 36 months | $67,686
ME-PBC-PCE-100G-60M | 100G | 60 months | $112,317
ME-PBC-PCE-10G-12M | 10G | 12 months | $14,950
ME-PBC-PCE-10G-36M | 10G | 36 months | $33,843

ME-PBC-PCE-10G-60M | 10G | 60 months | $56,158
ME-PBC-PCE-1G-36M | 1G | 36 months | $16,922
ME-PBC-PCE-1G-60M | 1G | 60 months | $28,079
SKU | Bandwidth | Term | List Price
ME-PBC-PCE-100G-12M-HA | 100G | 12 months | $20,930
ME-PBC-PCE-10G-12M-HA | 10G | 12 months | $10,465
SKU | Description | List Price
ME-MPP-48-12M | Port Extender (12 mo) | $8,990
ME-MPP-48-12M-LAB | Lab Port Extender (12 mo) | $8,990
ME-MPP-48-36M | Port Extender (36 mo) | $19,987
ME-MPP-48-60M | Port Extender (60 mo) | $33,490
ME-PBC-PCE-POC60 | PBC POC License (60 days) | $2,490
ME-MPP-48-POC60 | MPP POC License (60 days) | $749
Dimension | Options
Bandwidth | 1G, 10G, 100G
Availability | Standard, High Availability (HA)
Term | 12 months, 36 months, 60 months
Item | Qty | Unit Price | Extended
ME-PBC-PCE-100G-12M | 3 | $29,900 | $89,700
Subtotal List Price |  |  | $89,700
Discount (35%) |  |  | ($31,395)
TOTAL |  |  | $58,305

---

## 2. FOUNDING TEAM BIOS

### Andy Ory — Executive Chairman

**Background:** Co-founded Acme Packet and 128 Technology. Harvard education. Brings institutional credibility and network experience spanning carrier and enterprise infrastructure markets.

**Acme Packet legacy:** Founded with Abilash and Timothy. Acme Packet became the Session Border Controller category leader, used by 90% of carriers for VoIP/unified communications. Sold to Oracle for $2.1 billion in 2013.

**128 Technology legacy:** Co-founded the company that pioneered session-aware networking and SD-WAN for carrier-scale deployments. Largest acquisition Juniper Networks ever made (~$450M). Built the foundation for modern intent-based networking.

**Role at MaiaEdge:** Executive Chairman. Provides strategic oversight, board relationships, and investor guidance. Represents the third act in solving fundamental carrier infrastructure problems.

**Credibility points:** Two exits totaling $2.5+ billion combined. Deep relationships across the carrier ecosystem. Personal experience with the exact problems MaiaEdge solves.

---

### Patrick MeLampy — CFO, Investor & Board Member

**Background:** Co-founded Acme Packet and 128 Technology alongside Andy Ory, Abilash Menon, and Timothy Ziemer. CFO at both exits. Deep experience in carrier infrastructure financing and scaling.

**Acme Packet:** Built the financial infrastructure for rapid growth, eventual Oracle acquisition.

**128 Technology:** Navigated Series funding rounds leading to Juniper acquisition.

**Role at MaiaEdge:** CFO and Board Member. Oversees financial strategy, capital allocation, and investor relations. Brings validation of business model and pathway to scale.

**Credibility points:** Proven ability to build repeatable, scalable business models. Direct experience taking carrier infrastructure companies from early stage to billion-dollar exits.

---

### Abilash Menon — CEO & Co-Founder

**Background:** 15+ years in carrier infrastructure. Deep technical expertise in routing, MPLS, SD-WAN. Built the technical architecture at both Acme Packet and 128 Technology.

**Acme Packet:** Lead architect of Session Border Controller. Solved critical problems in carrier-scale session management.

**128 Technology:** Chief Architect of SD-WAN and session-smart routing. Personally experienced the limitations of protocol-centric routing and built solutions that operators depended on.

**Why Abilash built MaiaEdge:** After two exits in this space, the one problem that never got fixed was cross-domain automation and federation. Inside operator networks, there's API-driven automation. At the boundaries, it breaks down into spreadsheets and manual coordination. That gap is what MaiaEdge solves.

**Role at MaiaEdge:** CEO and Lead Architect. Technical direction, product strategy, customer relationships for technical decisions.

**Credibility points:** Built two categories that became industry standards. Has 100+ patents in networking. Speaks from first-hand experience with the exact pain MaiaEdge solves.

---

### Timothy Ziemer — CRO & Co-Founder

**Background:** Commercial and go-to-market leader at Acme Packet and 128 Technology. Deep carrier sales experience. Understands the P&L pressure, competitive dynamics, and board conversations at carrier companies.

**Acme Packet:** Built the commercial organization from early stage to enterprise-scale sales. Led the go-to-market that made Acme Packet the market leader.

**128 Technology:** Scaled from first customer to Tier 1 carrier deployments. Navigated competitive positioning against both Cisco and smaller startups.

**Why Timothy built MaiaEdge:** Saw the same pattern twice: operators want to compete with Lumen and Equinix but lack the infrastructure layer to do it. They're losing interconnection revenue, losing deals to faster provisioners, losing customers to NaaS platforms. MaiaEdge is the infrastructure layer they can own.

**Role at MaiaEdge:** CRO and Co-Founder. Sales strategy, partnerships, go-to-market. International expansion.

**Credibility points:** $2.55 billion in combined exits. Built winning commercial organizations at two companies. Personal relationships with carrier C-suite across the industry.