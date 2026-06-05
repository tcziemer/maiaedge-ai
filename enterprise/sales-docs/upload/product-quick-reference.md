# Product Quick Reference - Partner Edition

**The technical detail you need to handle a customer's "show me the architecture" question.**
*Pair this with MaiaEdge 101 for the business framing. This document goes deep on the product.*

---

## The System in One Picture

```
                    [Customer Portal - White Label, Operator's Brand]
                                       |
                                       | (HTTPS / API)
                                       |
        +------------------------- [PCE - Path Computation Engine] -------------------------+
        |   Cloud-native, carrier-neutral NNI engine. Computes deterministic paths.        |
        |   Hop-by-hop telemetry. Policy enforcement. Multi-tenant isolation.              |
        |   API integrations: Equinix Fabric, Megaport, AWS, Azure, GCP.                   |
        |   Mplify LSO Sonata + TM Forum ODA conformant.                                   |
        +----------------------------------------------------------------------------------+
                              |                                |
                  (Programs PBCs via secure channel)
                              |                                |
        +-------------- [PBC] ---------------+        +------------- [PBC] -------------+
        | 1RU appliance at network boundary  |        | 1RU appliance at network        |
        | Stateless forwarder                |        | boundary                        |
        | Dual 100G, line-rate AES-256 IPsec |        | Forwards deterministically per  |
        | (Optional Port Extender for tenant |        | PCE instructions                |
        |  fan-out: 48 x SFP28 + 8 x QSFP28) |        | (Optional Port Extender)        |
        +------------------------------------+        +---------------------------------+
                |                  |                                  |              |
        Customer side       Network/transport               Customer side    Network/transport
        (tenant, customer    (operator backbone,             (tenant)        (DIA, fiber, wave,
        demarcation)         partner network, DIA)                            partner network)
```

Three product lines work together: **PBC** at the edge, **PCE** in the cloud, **Port Extender** for high-density tenant fan-out (colo and meet-me room deployments).

---

## PBC - Path Border Controller (The Edge Hardware)

### Specifications

| Spec | Detail |
|---|---|
| Form factor | 1RU appliance |
| Power | Standard rack power (data center friendly) |
| Interfaces | Dual 100 Gbps, full-duplex |
| Encryption | Line-rate AES-256-GCM IPsec (no throughput penalty) |
| Latency overhead | Less than 2 microseconds |
| Forwarding model | Stateless, protocol-free, deterministic |
| Routing protocols required | None. No BGP, no OSPF, no MPLS |
| Configuration model | All path config from PCE. PBC executes only |

### Why Each Spec Matters

**Dual 100G interfaces:** One side typically faces the customer/tenant; the other faces the network/transport. Supports failover and bidirectional traffic.

**Line-rate AES-256-GCM IPsec:** Encryption happens at wire speed. No throughput penalty for security - unlike traditional VPN approaches where encryption creates bottlenecks. Critical for latency-sensitive applications and high-bandwidth workloads.

**Less than 2 microseconds of latency overhead:** Traditional routers add milliseconds processing packets through routing stacks. PBCs forward deterministically based on PCE instructions - orders of magnitude faster. Critical for AI inference, financial trading, distributed workloads.

**Stateless forwarding:** PBCs don't make routing decisions and don't hold complex state. If a PBC fails, there's no state to rebuild. Traffic reroutes immediately by the PCE without waiting for routing protocols to reconverge.

**No routing protocols required:** Field engineers don't configure BGP, OSPF, or MPLS at each site. Configuration is centralized in the PCE. Push-button easy and hardwire simple. Rack, connect, and the PCE does the rest.

### What the PBC Does NOT Do

- **NOT a router replacement** - Cisco/Juniper/Arista cores stay where they are. PBCs sit at boundaries (meet-me rooms, carrier handoffs, customer demarcation).
- **NOT SD-WAN** - SD-WAN sits at enterprise branches. PBCs sit at carrier boundaries.
- **NOT making routing decisions** - All path decisions are made by the PCE; PBCs just execute.

### High Availability Options

Active/standby HA architecture. HA units priced at approximately 70% of standard units. Can be added to any deployment.

PBCs operate independently if the cloud control plane is unreachable - they continue forwarding traffic based on the last received instructions until PCE connectivity is restored. **Service does not interrupt during PCE maintenance or network partition.**

---

## PCE - Path Computation Engine (The Cloud Orchestrator)

The PCE is a **carrier-neutral NNI engine** - it computes paths across operators without requiring those operators to share a common transport vendor or routing protocol stack. Cloud-native. Multi-tenant by default. Standards-conformant.

### Capabilities

| Capability | Description |
|---|---|
| Path computation | Real-time calculation of optimal, deterministic paths |
| Multi-domain orchestration | Automate provisioning across owned and partner networks |
| Hop-by-hop telemetry | Latency, jitter, loss reported per path, per hop |
| SRLG-aware path selection | Avoids shared trenches and carriers; ensures true physical redundancy |
| API integrations | Equinix Fabric, Megaport, AWS, Azure, GCP |
| White-label portal | Self-service portal under the operator's brand |
| Multi-tenant isolation | Separate logical views, RBAC, isolated telemetry per customer |
| Policy enforcement | SLA-aware routing, jurisdictional / sovereign routing, bandwidth tiers |
| Auto-failover | SLA-based path monitoring with hitless reroute |
| Standards conformance | Mplify LSO Sonata interoperability, TM Forum ODA conformant |
| OSS/BSS Integration | API-first design for direct billing and operations integration |

### How the PCE Thinks (Different from BGP)

The PCE looks at network nodes, NOT protocols. It sees source and destination, then computes optimal paths dynamically. Traditional BGP routes hop-by-hop, propagating advertisements; convergence takes seconds to minutes. The PCE has a global view of the topology and computes paths centrally - instantaneous and deterministic.

### Path Tagging and End-to-End Visibility

Every packet carries its origin and route. This is what enables hop-by-hop observability across networks the operator doesn't own (Type 2 circuits, partner networks). Traditional routing loses visibility at network boundaries - with MaiaEdge, every hop is visible.

### SRLG-Aware Path Selection

Beyond shortest-path routing, the PCE understands Shared Risk Link Groups - it avoids paths that share the same physical trench, fiber bundle, or carrier infrastructure. This delivers true physical redundancy: when an operator promises customer A and customer B don't share a single point of failure, the PCE can prove it programmatically.

### SLA-Aware Routing

The PCE optimizes paths based on actual performance metrics, not just shortest-path or lowest-cost. Considers:
- Latency requirements
- Jitter sensitivity
- Packet loss thresholds
- Bandwidth needs
- Policy constraints (jurisdictional, sovereignty, customer-specific)
- SRLG diversity

### Automatic Failover

If a path degrades or fails:
1. PCE detects the issue via continuous telemetry
2. Computes an alternate path meeting SLA requirements
3. Reprograms affected PBCs
4. Reroutes traffic - within seconds

No manual intervention. No ticket escalation. No waiting for routing protocols to converge.

### Multi-Tenant Isolation Architecture

- Separate logical views per customer
- Role-based access controls (RBAC)
- Isolated telemetry and configuration per tenant
- API-first design for programmatic access
- Operator sees everything; customer sees only their own paths and metrics

### Sovereign / Policy-Based Routing

Define policy in the PCE: "Traffic MUST stay within EU." "Traffic MUST avoid US carriers subject to CLOUD Act." "India-only paths." The PCE enforces jurisdictional constraints programmatically. **BGP cannot do this.**

Audit trail: every hop logged with timestamp, carrier identifier, geographic location, latency. Hand to regulators when EU AI Act or GDPR auditors ask "prove this data never left jurisdiction."

### Standards Conformance

- **Mplify LSO Sonata** - The MEF wholesale orchestration standard for inter-carrier provisioning. PCE speaks LSO Sonata APIs natively, which means cross-operator NNI activation can happen programmatically with any other Mplify-conformant operator.
- **TM Forum ODA** - The reference architecture most carriers procure against. PCE is ODA-conformant, which means zero friction on existing carrier RFP canvases.

---

## Port Extender (Maia Path Port Extender / MPP)

The integrated switch designed exclusively for the PBC. Delivers high-density tenant ports without operational overhead. Provisioned through the same PCE as the PBC, so operators add ports without adding orchestration complexity.

### Specifications

| Spec | Detail |
|---|---|
| Form factor | 1RU |
| Tenant ports | 48 x SFP28 (10/25 GbE) |
| Uplinks | 8 x QSFP28 (100 GbE) |
| Latency | Less than 500ns port to port |
| Management | Rear CPU/BMC shared Ethernet (RJ45), Serial Console (RJ45) |
| Reliability | Hot-swappable redundant power supplies and fans, 150,000+ hour MTBF |
| Airflow | Front-to-back or back-to-front |

### Why Each Spec Matters

**48 SFP28 ports + 8 QSFP28 uplinks:** Up to 48 tenants per unit at 10/25 GbE, with 8x100G uplinks back to the PBC. Designed for colocation meet-me rooms where port density is the operational constraint.

**Less than 500ns port-to-port latency:** Switch fabric is built for the inter-tenant traffic patterns of a meet-me room without adding meaningful latency overhead.

**Hot-swappable, 150,000+ MTBF:** Carrier-grade reliability. Redundant power and fans keep the switch live during component failures. Choose airflow direction based on rack configuration.

**Common control plane with PBC:** Provisioned through the same PCE. Tenant turn-up flows through the same self-service portal as private path activation. Operators add ports without learning a separate orchestration system.

### Where the Port Extender Fits

- **Colocation meet-me rooms** - 48 tenant ports per unit, scaled across the facility
- **Carrier hotels** - High-density cross-connect fan-out without rack-space pressure
- **Multi-tenant edge facilities** - Wherever a single PBC needs to serve more than two customer-facing connections

---

## Layer 2.5 - How MaiaEdge Operates

| Layer | Characteristics |
|---|---|
| Layer 2 | Simple, fast, works great within a building. Limited to LANs |
| Layer 3 | Scalable across WANs using BGP, OSPF, MPLS. Complex configuration |
| **Layer 2.5 (MaiaEdge)** | **Ethernet simplicity extended to WAN. No protocols in field. Centralized computation. Layer 3 reach with Layer 2 simplicity.** |

**Key technical primitives:**
- **Q-in-Q** - Multi-tenant tagging keeps every customer isolated
- **Mac-in-Mac** - Core network scales beyond traditional Ethernet's ~4,094 VLAN ID limit
- **Result:** Layer 3 reach with Layer 2 simplicity. No BGP. No OSPF. No MPLS complexity.

---

## How a Path Gets Activated (End to End)

```
1. Deploy PBC at network boundary (rack install, plug in, power up)
   |
2. PBC phones home; operator claims it in the PCE dashboard
   |
3. PCE discovers available paths and transport types (fiber, wave, DIA, partner)
   |
4. Operator (or end customer via portal) requests a path between two endpoints
   |
5. PCE computes optimal path: latency, utilization, policy, bandwidth, SRLG diversity
   |
6. PCE programs the PBCs (no local config - just instructions)
   |
7. Path is live. Encrypted end-to-end with AES-256-GCM IPsec
   |
8. PCE collects telemetry continuously and auto-reroutes if needed
```

**Critical:** After the initial physical deployment, ALL provisioning happens remotely through the PCE. No truck rolls. Path activation in minutes, not months.

---

## Transport Flexibility - One Fabric, Any Underlay

MaiaEdge operates over any transport: leased lines, dark fiber, lit waves, DIA (Dedicated Internet Access), 5G/fixed wireless, satellite. The PCE abstracts transport from the customer experience.

**Common deployment combinations:**
- **Fiber + DIA** - Start with DIA for instant connectivity, add fiber when available, keep DIA as automatic failover
- **Owned + partner** - PCE computes paths across owned infrastructure and partner networks seamlessly
- **Hybrid** - Mix all of the above in one fabric

All paths encrypted end-to-end with AES-256-GCM IPsec regardless of underlay.

---

## Cloud On-Ramp Architecture (Equinix / Megaport / Hyperscalers)

This is the most common high-margin use case for colos, fiber operators, and MSPs.

```
[Operator's Customer]
        |
        | (private path, operator's brand)
        |
   [PBC at operator boundary]
        |
        | (API integration)
        |
   [PCE orchestrates path through Megaport / Equinix Fabric]
        |
        | (backend infrastructure - invisible to end customer)
        |
   [AWS Direct Connect / Azure ExpressRoute / GCP Cloud Interconnect]
```

**Shared port economics:** Once a port is in place at Megaport or Equinix Fabric, every new customer adds higher-margin revenue against a fixed cost base. Cloud connectivity becomes a product that gets more profitable as it scales - not a bespoke service with proportional cost.

**The operator's brand stays in front.** Megaport and Equinix Fabric are invisible to the end customer unless the operator chooses otherwise.

**Four cloud-on-ramp deployment models** (per the deck):
1. **Private Wavelength** - PBC at operator edge + wave to Equinix PoP. Automated cloud provisioning.
2. **DIA** - PBC at operator edge + PBC at Equinix PoP. Instant cloud access over DIA.
3. **Partnership** - Federate with partner providers for cloud connectivity. Leverage partner reach.
4. **Full Marketplace** - Offer any service in the Equinix fabric, not just cloud connectivity.

---

## Common Deployment Patterns by Segment

### Colocation Operator (Fabric-in-a-Box)

PBC + Port Extender in the meet-me room. Tenants get virtual cross-connects through the operator's portal. Cloud on-ramp via Megaport/Equinix backend integration.

### Fiber Operator (Internal Unification + Cross-Carrier)

PBCs at internal domain boundaries (each fiber island) + at NNI handoffs to partners. Same infrastructure unifies the operator's network and extends to partners.

### Network Operator (Tier 1 / Tier 2)

PBCs deployed at PoPs and partner handoffs. Layered above incumbent automation (Cisco Crosswork, Juniper Paragon, Ciena Blue Planet, Nokia NSP). MaiaEdge does NOT replace incumbent OSS/BSS - it orchestrates across domains the incumbent PCE can't reach. Mplify LSO Sonata conformance means cross-carrier integration is standards-based.

### Neocloud (Multi-Facility AI Infrastructure)

PBCs at each GPU facility + at hyperscaler / cloud on-ramp points. PCE unifies the control plane across all facilities and carriers. Multi-tenancy supports serving multiple end customers from the same infrastructure.

### MSP / NaaS Platform Operator

For visibility-only motion: PCE telemetry layered above existing carrier relationships, no PBC deployment required at every customer. For full deployment: PBCs at strategic partner-NNI boundaries to extend platform speed across markets where the operator doesn't own PoPs.

---

## What's Included in the Subscription

| Component | What's Included |
|---|---|
| Hardware | PBC appliance and Port Extender (title remains with MaiaEdge) |
| Software | PCE access, software updates |
| Portal | White-label customer portal under operator's brand |
| API Integrations | Equinix Fabric, Megaport, AWS, Azure, GCP |
| Telemetry | Hop-by-hop latency, jitter, loss data via portal and API |
| Standards | Mplify LSO Sonata, TM Forum ODA conformance |
| Support | 99.9% Service Availability. Sev 1 acknowledgment within 2 hours. 24/7 ticket system |

**Hardware ownership:** Title stays with MaiaEdge. Customer has full control over installation and relocation. This is the carrier infrastructure model - equipment is a service, not a purchase.

---

## SKU Reference

### Standard PBC + PCE

| SKU Pattern | Bandwidth | Term | Notes |
|---|---|---|---|
| ME-PBC-PCE-100G-12M | 100G | 12 months | Standard |
| ME-PBC-PCE-100G-36M | 100G | 36 months | Better per-unit pricing |
| ME-PBC-PCE-100G-60M | 100G | 60 months | Best per-unit pricing |
| ME-PBC-PCE-10G-12M | 10G | 12 months | Standard |
| ME-PBC-PCE-10G-36M | 10G | 36 months | |
| ME-PBC-PCE-10G-60M | 10G | 60 months | |
| ME-PBC-PCE-1G-36M | 1G | 36 months | 1G is 36/60-month only |
| ME-PBC-PCE-1G-60M | 1G | 60 months | |

### High Availability (Standby) Units

| SKU Pattern | Bandwidth | Term | Notes |
|---|---|---|---|
| ME-PBC-PCE-100G-12M-HA | 100G | 12 months | ~70% of standard |
| ME-PBC-PCE-10G-12M-HA | 10G | 12 months | ~70% of standard |

**HA rules:** HA units require a primary unit at the same site. Available for 10G and 100G only.

### Port Extender (MPP) - For Colocation Cross-Connect Fan-Out

| SKU | Description |
|---|---|
| ME-MPP-48-12M | 48-port Port Extender, 12 months |
| ME-MPP-48-36M | 48-port Port Extender, 36 months |
| ME-MPP-48-60M | 48-port Port Extender, 60 months |
| ME-MPP-48-12M-LAB | Lab/test Port Extender, 12 months |

### POC Licenses (60-Day Trial)

| SKU | Description |
|---|---|
| ME-PBC-PCE-POC60 | PBC + PCE, 60 days |
| ME-MPP-48-POC60 | Port Extender, 60 days |

### Pricing Rules

- **Term commitment is the primary discount lever.** 36 or 60-month deals unlock significantly better per-unit pricing than 12-month.
- **Volume matters.** More PBCs in the initial order, better the discount.
- **Mid-term expansion:** Adding PBCs during an active contract uses the original Order Form's pricing, pro-rated, co-termed to the original end date. No renegotiation.
- **HA pricing:** ~70% of standard. Add to any deployment for failover.

**Example:** A 36-month deal for 3 x 100G PBCs at $25,000/unit. Six months in, customer adds 2 more PBCs. They pay $25,000/unit (original), pro-rated for the 30 months remaining, co-termed to the original end date.

### International Delivery (Outside US)

- **Delivery:** FCA Burlington, MA (Incoterms 2020). Risk transfers to customer at carrier pickup.
- **Importer of Record:** Customer acts as Importer of Record. Handles customs documentation.
- **Taxes / Duties:** Customer responsible for taxes, duties, tariffs, VAT. Not included in quote.

---

## What MaiaEdge Hardware Does Not Need

| Common requirement | MaiaEdge requirement |
|---|---|
| Routing protocols (BGP, OSPF, MPLS) configured at each site | None. PBCs are stateless. PCE handles all path logic |
| OSS/BSS integration project (6-12 months for orchestration platforms) | API-ready. Optional integration. PBCs run independently. ODA-conformant |
| Specialized SDN engineering team | None. Operate via white-label portal or API |
| Truck rolls for path provisioning | None after initial physical install |
| Custom hardware per customer / tenant | None. Multi-tenancy is built in. Same fabric serves multiple customers with isolation |

---

## Quick FAQ for Partner Calls

**"How long to get to production?"** 30-60 days from contract signature, including PBC deployment and PCE onboarding. Not 6-12 months like orchestration platforms.

**"What if the cloud (PCE) goes down?"** PBCs continue forwarding based on last instructions. Service does not interrupt. PBCs reconnect to PCE when control plane returns.

**"Can my customer's customers have isolated views?"** Yes. Multi-tenant isolation is built in. Each end customer sees only their own paths, telemetry, and configuration.

**"Does this work with my existing Cisco / Juniper investment?"** Yes. PBCs sit at the edge, complementary to core routers. We don't replace BGP, OSPF, or MPLS in the core.

**"Can I integrate with my existing automation (Crosswork, Paragon, Blue Planet, NSP)?"** Yes. MaiaEdge is API-first and standards-aligned (TM Forum ODA, Mplify LSO Sonata). Layer it above incumbent OSS/BSS.

**"What's the security story?"** Line-rate AES-256-GCM IPsec encryption on every path. End-to-end. No throughput penalty.

**"Can the PCE be deployed in-country for sovereign use cases?"** Yes. The PCE itself can run in customer-controlled cloud (AWS GovCloud, Azure Government, sovereign cloud platforms). Routing decisions never leave jurisdiction.

**"How does the Port Extender relate to the PBC?"** It's a 1RU integrated switch designed exclusively for the PBC. 48 SFP28 tenant ports plus 8 QSFP28 uplinks back to the PBC. Same PCE control plane. Drop-in for high-density colocation deployments.

---

## Where to Get Help

- **Technical questions for partners:** timziemer@maiaedge.io
- **Pricing and quotes:** cooperkennedy@maiaedge.io
- **Customer demos and POCs:** Through deal registration on the partner page
