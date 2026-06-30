<!-- INTERNAL CONTEXT METADATA (HTML comment - does NOT render in any built PDF)
SEGMENT SCOPE: NeoCloud (primary) + AI-colo (Data Center Colo Provider / "AI Signals - colo" sub-segment).
DO NOT use for Fiber Operator, Network Operator, MSP/Aggregator, or Enterprise - they do not run GPU clusters
for AI tenants and this use case + its economics (per-cluster ASN/IP, Layer 2 cluster assignment, scale-up/scale-out
bridging, marketplace capacity resale) do not apply. NeoclouD messaging rule: profit-center framing is fine; drop
OPERATOR sovereignty (they are the compute customer), data sovereignty is allowed.
PROVENANCE: Customer-facing use-case brief; source markdown for partner docs/final/Use-Case-Brief-GPU-Cluster-Connectivity.pdf.
-->

**USE CASE BRIEF**

# Simplifying GPU Cluster Connectivity for AI Infrastructure Operators

*How MaiaEdge eliminates per-cluster BGP, ASN, and IP complexity so you can scale GPU infrastructure without scaling your network operations overhead.*

## The Problem: GPU Clusters Are Networking Islands

AI infrastructure operators building GPU clusters for private equity investors, monetization platforms, and enterprise tenants face a compounding set of network operations problems that get worse with every cluster added.

### Per-Cluster Network Credentials

Every new cluster requires its own ASN and public IP block. For operators serving private equity investors or non-technical cluster owners, this means the infrastructure team must obtain and manage these credentials on their behalf. Customers who do not understand what an ASN is cannot be expected to get one.

### Node-by-Node Customer Assignment

When assigning an entire cluster to a single tenant, there is no mechanism to hand it over as a logical unit. Each node must be individually booked. For any cluster beyond a few dozen nodes, this is not a scalable workflow. It also makes reassigning capacity to a new tenant operationally expensive.

### BGP at Every Edge

The standard deployment model puts BGP peering between ISP uplinks and core switches at every site. Managing BGP configuration across multiple dispersed clusters means managing variability in every provider's BGP implementation. Each site is its own troubleshooting domain.

### Connectivity Between Sites Requires Layer 3 Complexity

Each cluster island operates independently. Bridging a scale-up cluster and a scale-out cluster at different sites, or giving a customer coordinated access to both, requires NAT, IP address planning, and Layer 3 configuration that add friction and limit flexibility.

### NaaS Providers Fund Competitors

Using Megaport as the fabric layer is convenient, but Megaport has moved aggressively into competing GPU and inference infrastructure — acquiring bare-metal compute provider Latitude.sh and raising A$827M to build a distributed AI inference cloud. Operators who depend on Megaport for connectivity are directing revenue toward a direct competitor while also ceding control of the customer experience.

### Cloud Connectivity Is a Manual Patchwork

AI startups increasingly run front-end services in public cloud while placing GPU compute in colocation to control cost. Connecting the two today means managing Direct Connect or ExpressRoute separately from the rest of the network, with no shared visibility. When something breaks, troubleshooting turns into a blame game between the colo provider, the ISP, and the cloud provider.

## The MaiaEdge Approach: Path Border Controller

MaiaEdge is a network infrastructure vendor, not a network-as-a-service provider. MaiaEdge does not sell circuits or a shared network. It sells hardware and software that operators deploy to build and control their own programmable fabric.

The core product is the Path Border Controller (PBC) and its companion Path Computation Engine (PCE) running in the cloud. The PBC provides Ethernet in and Ethernet out. Between devices, all traffic is AES-256 GCM encrypted. The PCE acts as a carrier-neutral routing engine that maps paths across all deployed PBCs without relying on BGP or any routing protocol.

**What this means in practice:**

- No BGP configuration at any edge. The PCE handles path selection based on cost or latency.
- Layer 2 fabric across geographically dispersed sites. Customers see a virtual LAN, not an IP hop.
- End-to-end visibility from the cluster through any intermediate hops into the customer's cloud VPC or VNet.
- Programmable connections to Equinix, Megaport, and other fabric APIs — without Megaport being in your revenue path as a competing AI infrastructure provider.
- Multi-tenant from the ground up, with separate MSP and customer views in the same UI.

## Use Cases for GPU Cluster Operators

### Centralized Internet Presence Across Multiple Sites

Deploy one or two MaiaEdge PoPs at well-connected exchange points. All clusters connect back over DIA or wave. A single ASN and IP block covers the entire footprint. No per-cluster ASN. No per-customer IP block. Customers connect to the fabric through those central entry points regardless of which site their workload runs on.

This is particularly valuable for operators running clusters in multiple colocation facilities owned by different private equity customers, each monetized by the same platform. The clusters remain independently owned and contracted, but the network operations are centralized.

### Layer 2 Cluster Assignment

Assign an entire GPU cluster to a tenant as a single Layer 2 segment rather than booking nodes individually. From the customer's perspective, the cluster appears as on-premises infrastructure on their LAN. No NAT. No public IP assignment per node. No per-customer VLAN management on the switch.

When a cluster needs to be reassigned to a new tenant, the change is made at the PBC. The switch configuration does not need to be touched.

### Bridging Scale-Up and Scale-Out GPU Clusters

A customer running scale-up training on one cluster and scale-out inference on another can have both appear as a single logical fabric. The PCE stitches paths between clusters at different sites with no NATting required. The customer coordinates across both without leaving their own address space.

### Cloud Onramp for AI Workloads

AI startups running front-end services in Azure or AWS and GPU compute in colocation can connect the two through MaiaEdge's native Equinix integration. The PBC stitches a Direct Connect or ExpressRoute path from the cluster through an Equinix port directly into the customer's VNet or VPC.

This requires no VM deployed in the cloud for a VPN endpoint. Data transfer happens on demand, training results flow back to cloud storage when needed, and the entire path is visible in a single pane of glass including inside the cloud boundary.

### Building a Fabric Service and Selling Excess Capacity

Operators can advertise connectivity services to partners via the built-in marketplace. Other PBC operators can peer with a simple partnership code exchange. Wholesale capacity can be bought and sold at arbitrage pricing, similar to how Megaport today resells ISP capacity at prices below direct purchase.

This turns infrastructure investment into a potential revenue stream rather than a pure cost center, and builds competitive moat against NaaS platforms.

## Reference Deployment Architecture

### HA at the Edge

Two PBCs are deployed per cluster edge: one per ISP uplink. Each PBC connects to both spine switches, forming an MLAG pair. There is no state synchronization between PBCs. If one device fails, traffic fails over to the other. This preserves the full redundancy model of a cluster built with no single points of failure.

### Port Extender

The PBC ships with 100G uplinks and can be paired with a port extender that presents many 100G and 10G access ports. Customer racks, individual compute nodes, or sub-clusters connect directly into the port extender. No VLAN configuration is required on the downstream switch. The PBC handles customer and service tagging via inner and outer VLAN tags (C-tags and S-tags), so segmentation is defined in the management UI, not the switch CLI.

### Path Provisioning

Adding a new PBC requires scanning a QR claim code or selecting from inventory in the management UI. No CLI. No manual configuration of routing protocols. After assigning a site and defining the uplink capacity, paths between any two sites are created through the UI by selecting source and destination. The PCE computes the optimal route. A backup path that avoids all intermediate nodes can be designated for fast protection.

**Operational summary:**

- New cluster onboarding: scan QR code, name the device, define ISP links, assign customer and site.
- New customer: create customer record, assign ports or VLAN ranges, create path A to Z.
- New cloud connection: add cloud profile (account ID, region, access keys for telemetry), create path through Equinix.
- Troubleshooting: single-pane view of path status hop by hop including inside AWS and Azure.

## Conclusion

GPU infrastructure operators face a compounding operations problem: every new cluster adds another island, another BGP configuration, another ASN, and another set of per-node bookings. The tools designed for traditional enterprise networking were not built for an environment where clusters are owned by different investors, monetized by third-party platforms, and expected to connect seamlessly to public cloud on demand.

MaiaEdge addresses this directly. By replacing BGP-based edge connectivity with a Layer 2 programmable fabric, operators can centralize their internet presence, assign entire clusters as a single logical unit, and stitch cloud onramps without touching switch configurations or provisioning network credentials for every customer. The result is a network operations model that scales with the business rather than against it.
