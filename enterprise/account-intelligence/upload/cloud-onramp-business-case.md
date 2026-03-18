# MaiaEdge Cloud On-Ramp: Native Cloud Access for Network Operators

**Purpose:** Positioning, use case definition, and business case for cloud on-ramp via MaiaEdge
**Last Updated:** February 2026

---

## The Problem: Cloud Connectivity Forces a Difficult Choice

Cloud connectivity has historically forced network operators into a difficult position, and most haven't found a clean way out.

### Operators Without Cloud Access Today

For many regional fiber operators and colocation providers, offering cloud connectivity isn't an option today. The capability requires direct builds to hyperscalers or fabric access, specialized engineering resources, and a commercial model that most operators haven't built. When a customer asks for AWS Direct Connect, Azure ExpressRoute or Google Cloud Interconnect, the standard response is to redirect them to Equinix, Megaport, or a nearby colocation with a direct presence. The operator exits the conversation, and with it, the revenue and the relationship.

What compounds this is that operators rarely have a clear picture of the demand they're quietly turning away. Customers who know their provider can't deliver tend to stop asking, which means the gap stays invisible until a competitor fills it.

### Operators Already Delivering Cloud Access (The Margin Problem)

Other operators have built some version of cloud access by routing customers through Equinix Fabric or Megaport directly. Both platforms offer genuine reach, and for operators without a hyperscale facility presence, they solve a real access problem. The commercial consequences, however, accumulate over time. Customers establish accounts with the fabric provider, learn its portals, and build their workflows there. Published pricing on those platforms limits how operators can bundle and differentiate their own services. The operator's role gradually narrows to access provider, while the customer relationship and pricing power migrate toward the fabric.

The operational burden compounds the margin problem. Traditional cloud on-ramp architectures require a dedicated port per customer, manual VLAN coordination for each new connection, and cloud routers to handle multi-cloud routing, with licensing and compute costs that scale with every customer added.

---

## The Solution: Native Cloud Access with MaiaEdge

MaiaEdge offers a better way to deliver cloud connectivity, one that uses the reach of Equinix and Megaport without surrendering the customer relationship to them.

Operators deploy a MaiaEdge Path Border Controller (PBC) at their network edge, while the cloud-based Path Computation Engine (PCE) handles orchestration, policy and end-to-end visibility. Through direct API integrations with Equinix Fabric and Megaport, the PCE coordinates VLAN assignment, cloud provider provisioning, and per-customer path management from a single control plane.

The result is a direct Layer 2 private path into the customer's cloud environment, without BGP configuration or cloud routers on either end. Multiple customers share a single fabric port, with bandwidth commitments and service tiers enforced per tenant. Equinix and Megaport function as backend infrastructure. The operator's brand, pricing, and customer relationship stay entirely in-house.

### Multi-Cloud Without BGP Complexity

In most Equinix Fabric architectures today, enabling a single end customer to access multiple clouds introduces a Layer 3 routing requirement. Providers typically deploy managed cloud routers or customer-managed routing appliances and configure BGP to stitch together AWS, Azure, and private infrastructure.

MaiaEdge removes this requirement in many common multi-cloud access scenarios:

- Direct Layer 2 private paths into cloud environments (AWS VPCs, Azure VNets, or equivalent where supported)
- Deterministic, encrypted connectivity per tenant
- Platform-level policy enforcement without exposing routing complexity to the customer
- No cloud router to deploy or license, no BGP sessions to configure or maintain

### Multi-Cloud Cost Elimination
MaiaEdge eliminates **$2,500–$5,000/month per customer** in cloud routing costs:
- No cloud router required
- No BGP configuration or monitoring
- No routing appliances or additional cloud compute instances
- No duplicate HA instances for routing
Multi-cloud access becomes a service capability, not a networking project.

---

## Path to Market

### For Operators Not Currently Offering Cloud Connectivity

Getting to market doesn't require building hyperscale facility presence from scratch. Operators can either establish a port on Equinix Fabric or Megaport directly, or partner with a PBC-holding operator that already has one. Both routes enable a fully branded cloud access product and scale with customer demand.

**Direct port establishment:** MaiaEdge handles provisioning, VLAN management, and cloud API integration from there. Where a physical fabric connection doesn't yet exist, a dynamic NNI over a DIA circuit can be stood up immediately, enabling revenue generation while a physical interconnect is built, rather than waiting the 90 to 120 days a traditional NNI build typically requires.

**Federation with a partner:** For operators in markets without local fabric access, federation with a MaiaEdge partner that already holds a port removes the infrastructure requirement entirely. The partner's infrastructure is invisible to the end customer. The originating operator sells a fully branded service, sets the price, and owns the relationship. A regional fiber operator with a wave to a major market can effectively become the cloud on-ramp for its region, competing for business that would otherwise require customers to contract directly with a fabric provider.

### For Operators Already Delivering Cloud Connectivity

MaiaEdge addresses the margin, sovereignty, and operational problems that accumulate in conventional architectures, without requiring a rebuild of the customer-facing product.

- **Compounding economics:** Once a port is in place, every new customer adds higher-margin revenue against a fixed cost base rather than proportional infrastructure spend.
- **Automated provisioning:** New customer connections activate through the platform without engineering involvement at each step.
- **Hop-by-hop SLA telemetry:** Operations teams get visibility from the customer site through the operator's network and into the cloud environment, with the ability to enforce SLA commitments across network boundaries.
- **Transport independence:** The customer-facing experience stays entirely the operator's. If a more favorable transport option comes to market, the operator can make a change without altering the customer's portal or service structure.

---

## The Business Case

### Revenue: A Product That Gets More Profitable as It Scales

Cloud on-ramp has historically been a cost-heavy, margin-thin offering because each new customer adds proportional infrastructure and engineering cost. The shared port model changes that structure. Once a port is in place, every incremental customer beyond breakeven generates higher-margin revenue against a fixed cost base. Cloud connectivity starts behaving like a product rather than a bespoke service.

### Simplicity: Automated from Order to Activation

MaiaEdge automates the full provisioning workflow, including VLAN coordination, cloud provider API calls, and path activation, without engineering involvement at each step. Hop-by-hop SLA visibility from the customer site into the cloud environment means operations teams have the data to diagnose issues rather than estimate where they are.

### Sovereignty: The Operator Owns the Customer, the Pricing, and the Brand

Customers access cloud services through the operator's portal, under the operator's brand, with pricing the operator sets. The fabric providers powering the service in the background can remain invisible to the customer or be disclosed at the operator's discretion. Either way, the commercial and strategic relationship stays with the operator, not the fabric.

---

## Segment-Specific Cloud On-Ramp Relevance

| Segment | Cloud On-Ramp Angle |
|---------|---------------------|
| **Colocation** | Tenants stop leaving for Equinix Fabric. The colo becomes the cloud on-ramp. Offer AWS/Azure/GCP direct access under your brand. Higher attach rates, premium pricing alongside space and power. |
| **Fiber Operators** | Cloud connectivity becomes a new revenue stream from fiber already owned. Operators in markets without local fabric access federate with a partner. Regional fiber operators become the cloud on-ramp for their region. |
| **MSP/Aggregators** | White-label cloud on-ramp under their own brand. No Equinix/Megaport dependency visible to customers. Asset-light cloud access product. |
| **Neoclouds** | Accelerated cloud and hyperscaler connectivity across multi-facility deployments. Cloud on-ramp is Layer 2 of the neocloud pain hierarchy (after observability). |
| **Network Operators** | Extend cloud access beyond their own PoP footprint via federation. Cloud on-ramp as a cross-carrier product. |

---

## Recommended Growth Path

1. Start with 10G ports in new or regional markets to validate demand with minimal risk
2. Upgrade to 100G ports once customer density reaches 15 to 20 per metro
3. Replicate the model market by market
4. Add DIA or leased-line diversity behind MaiaEdge for resilience and cost optimization

---

## SALES SUPPLEMENT: Financial Models and Pricing

*Note: This section contains pricing and financial modeling data for Sales use only. Not for inclusion in marketing or external content without approval.*

### Service Tiers

**100G Deployments (Metro / Hub Markets)**

| Tier | Bandwidth | Price | Description |
|------|-----------|-------|-------------|
| Gold | Guaranteed 5G | $2,500/mo | Committed bandwidth, strict QoS, lowest latency |
| Silver | High-priority 5G | $1,800/mo | Priority scheduling with controlled oversubscription |
| Bronze | Best-effort 2G | $600/mo | SaaS access, dev/test, backup, non-critical workloads |

**10G Deployments (Starter / Regional / Edge Markets)**

| Tier | Bandwidth | Price | Description |
|------|-----------|-------|-------------|
| Gold | Guaranteed 2G | $1,200/mo | Committed bandwidth, strict QoS |
| Silver | High-priority 2G | $900/mo | Priority scheduling with controlled oversubscription |
| Bronze | Best-effort 1G | $400/mo | Standard access |

### Scenario 1: 10G Unlimited Port (Starter / Regional)

**Monthly infrastructure cost:**
- 10G Unlimited Local Fabric port: $1,663
- MaiaEdge PBC subscription (10G): $2,125
- **Total fixed cost: $3,788/month**

**Capacity design (conservative):**

| Tier | Design | Oversubscription | Customers |
|------|--------|-----------------|-----------|
| Gold | 2G reserved | None | 1 |
| Silver | 4G design capacity | 2:1 | 4 |
| Bronze | 2G design capacity | 3:1 | 6 |
| Headroom | 1G | - | - |
| **Total** | **16G logical** | **~160% on 10G physical** | **11 max** |

**Financial performance:**

| Utilization | Customers | Revenue | Gross Margin |
|-------------|-----------|---------|--------------|
| Breakeven | ~4 | ~$3,900 | 0% |
| 60% | 7 | $4,600 | ~18% |
| 100% | 11 | $7,200 | **~47%** |

The 10G model is a low-risk, capital-efficient entry point. Breakeven occurs quickly, and margins improve steadily as demand ramps. Ideal for pilots, new metros, and regional edge deployments.

### Scenario 2: 100G Unlimited Port (Metro / Hub)

**Monthly infrastructure cost:**
- 100G Unlimited Local Fabric port: $11,400
- MaiaEdge PBC subscription (100G): $4,250
- **Total fixed cost: $15,650/month**

**Capacity design (high statistical efficiency):**

| Tier | Design | Oversubscription | Customers |
|------|--------|-----------------|-----------|
| Gold | 30G reserved | None | 6 |
| Silver | 40G design capacity | 2:1 | 16 |
| Bronze | 20G design capacity | 3:1 | 30 |
| Headroom | 10G | - | - |
| **Total** | **170G logical** | **170% on 100G physical** | **52 max** |

**Financial performance:**

| Utilization | Customers | Revenue | Gross Margin |
|-------------|-----------|---------|--------------|
| Breakeven | ~7 | ~$16,800 | 0% |
| 60% | 31 | $38,200 | **~59%** |
| 100% | 52 | $61,800 | **~75%** |

The 100G model is the primary economic engine. Even at partial utilization, margins are strong. At full utilization, a single port generates over $46,000/month in contribution.

### Side-by-Side Comparison

| Metric | 10G @ Full | 100G @ Full |
|--------|-----------|-------------|
| Gross Margin | ~47% | ~75% |
| Monthly Profit | ~$3,400 | ~$46,000 |

The 100G model delivers roughly 13x more profit for ~4x the cost, validating the scale-up strategy once demand density exists.

---

*End of Document*
*Cloud On-Ramp Positioning + Financial Models | February 2026*
