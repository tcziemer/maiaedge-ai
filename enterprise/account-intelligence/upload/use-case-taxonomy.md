# MaiaEdge Use Case Taxonomy

> Last updated: March 2026
> **Standardized vocabulary for classifying use cases discussed in sales calls. Use this taxonomy for consistent tracking across all call analysis and reporting.**

---

## Canonical Use Case List

### 1. POC / Deployment Logistics
**Definition:** Discussions about proof-of-concept planning, hardware deployment, site readiness, shipping, installation, and POC execution.
**Trigger Keywords:** POC, proof of concept, deployment, install, ship, site readiness, hardware, PBC, configuration, test unit, pilot
**Primary Segments:** All segments (universal)

### 2. Partner / Reseller Channel
**Definition:** Discussions about channel partnerships, reseller models, wholesale distribution, white-label offerings, and partner onboarding.
**Trigger Keywords:** partner, reseller, channel, wholesale, white-label, distribution, referral, co-sell, agent, VAR, INDATEL
**Primary Segments:** Fiber Operator, MSP/Aggregator, Colocation

### 3. Cloud On-Ramp / Cloud Connectivity
**Definition:** Discussions about enabling cloud connectivity (AWS, Azure, GCP), cloud on-ramp services, multi-cloud access, and cloud-under-your-brand models.
**Trigger Keywords:** cloud on-ramp, AWS, Azure, GCP, cloud connectivity, direct connect, ExpressRoute, multi-cloud, cloud access, hyperscaler
**Primary Segments:** Fiber Operator, Colocation, MSP/Aggregator

### 4. Carrier / SP Federation
**Definition:** Discussions about interconnecting with other carriers/service providers, NNI automation, cross-carrier provisioning, and federation topology.
**Trigger Keywords:** federation, NNI, cross-carrier, interconnect, service provider, carrier, peering, Type 2, off-net, partner network
**Primary Segments:** Fiber Operator, Network Operator, MSP/Aggregator

### 5. Data Center Interconnection
**Definition:** Discussions about connecting within and between data center facilities, cross-connects, meet-me room automation, and fabric deployment.
**Trigger Keywords:** data center, cross-connect, meet-me room, fabric, interconnection, colo, facility, Equinix, campus, inter-facility
**Primary Segments:** Colocation, Neocloud

### 6. Network Automation / Provisioning
**Definition:** Discussions about automating network provisioning, reducing manual configuration, self-service portals, and API-driven operations.
**Trigger Keywords:** automation, provisioning, self-service, portal, API, orchestration, manual, configuration, minutes not weeks, instant
**Primary Segments:** All segments (universal)

### 7. Fiber Monetization
**Definition:** Discussions about turning dark fiber or underutilized capacity into sellable services, stranded asset activation, and new revenue streams.
**Trigger Keywords:** dark fiber, monetize, stranded, underutilized, capacity, revenue, fiber islands, IRU, wavelength, lit services
**Primary Segments:** Fiber Operator

### 8. Wholesale Connectivity
**Definition:** Discussions about wholesale transport, bulk connectivity services, and carrier-grade service delivery to downstream customers.
**Trigger Keywords:** wholesale, transport, bulk, carrier-grade, downstream, transit, backbone, wavelength services
**Primary Segments:** Fiber Operator, Network Operator

### 9. Multi-Cloud Access
**Definition:** Discussions specifically about connecting to multiple cloud providers simultaneously, cloud arbitrage, and hybrid/multi-cloud architectures.
**Trigger Keywords:** multi-cloud, hybrid cloud, cloud arbitrage, multiple providers, cloud diversity, cloud fabric
**Primary Segments:** Colocation, Neocloud, MSP/Aggregator

### 10. Customer Portal / Self-Service
**Definition:** Discussions about providing end-customer portals, branded self-service interfaces, and customer-facing provisioning tools.
**Trigger Keywords:** portal, self-service, customer-facing, branded, white-label portal, dashboard, visibility, customer experience
**Primary Segments:** Colocation, Fiber Operator, MSP/Aggregator

### 11. NaaS / Managed Services
**Definition:** Discussions about Network-as-a-Service models, managed connectivity, and subscription-based network offerings.
**Trigger Keywords:** NaaS, managed services, subscription, as-a-service, managed network, OpEx model, consumption-based
**Primary Segments:** MSP/Aggregator, Fiber Operator, Network Operator

### 12. Sovereignty / Brand Control
**Definition:** Discussions about maintaining brand ownership of connectivity services, avoiding dependency on third-party fabrics, and keeping customer relationships.
**Trigger Keywords:** sovereignty, brand, ownership, control, Megaport dependency, customer relationship, margin, lock-in, fabric-in-a-box
**Primary Segments:** Colocation, Fiber Operator

### 13. End-to-End Visibility / Telemetry
**Definition:** Discussions about network observability, hop-by-hop telemetry, troubleshooting visibility, and monitoring across boundaries.
**Trigger Keywords:** visibility, telemetry, observability, monitoring, troubleshooting, end-to-end, hop-by-hop, Type 2, black hole, latency
**Primary Segments:** Neocloud, Network Operator, MSP/Aggregator

### 14. Marketplace / Service Discovery
**Definition:** Discussions about the MaiaEdge marketplace, ConnectBase integration, service discovery, and ecosystem participation.
**Trigger Keywords:** marketplace, ConnectBase, service discovery, ecosystem, catalog, available services, network exchange
**Primary Segments:** All segments

### 15. AI / GPU Networking
**Definition:** Discussions about GPU cluster connectivity, AI inference networking, training run optimization, deterministic paths for AI workloads, and recompute tax.
**Trigger Keywords:** GPU, AI, inference, training, deterministic, jitter, latency variance, recompute, cluster, NVIDIA, H100, B200
**Primary Segments:** Neocloud, Colocation (AI sub-segment)

### 16. Security / Encryption
**Definition:** Discussions about AES-256 encryption, data sovereignty, secure multi-tenancy, and compliance requirements.
**Trigger Keywords:** encryption, AES-256, security, compliance, sovereign, data sovereignty, multi-tenancy, isolation, zero trust
**Primary Segments:** Neocloud (Sovereign AI), Network Operator

### 17. Cross-Connect Optimization
**Definition:** Discussions about reducing cross-connect costs, replacing physical cross-connects with virtual connections, and port economics.
**Trigger Keywords:** cross-connect, LOA, port, virtual connection, VLAN, one-port-unlimited, $350/month, cost per connection
**Primary Segments:** Colocation, Fiber Operator

### 18. Egress Cost Reduction
**Definition:** Discussions about reducing cloud egress costs, optimizing data transfer paths, and avoiding hyperscaler egress pricing.
**Trigger Keywords:** egress, data transfer, cloud costs, bandwidth costs, egress pricing, cost reduction, direct peering
**Primary Segments:** Neocloud, Colocation

### 19. Geographic Expansion
**Definition:** Discussions about extending network reach to new markets, international expansion, and multi-state/multi-country coverage.
**Trigger Keywords:** expansion, new markets, geographic, international, multi-state, coverage, reach, footprint, new cities
**Primary Segments:** Fiber Operator, Network Operator, Neocloud

### 20. Competitive Displacement
**Definition:** Discussions specifically about replacing or competing with incumbent solutions (Megaport, Equinix Fabric, PacketFabric, Zayo, etc.).
**Trigger Keywords:** Megaport, Equinix Fabric, PacketFabric, Zayo, Lumen, replace, compete, switch, migrate, alternative, displacement
**Primary Segments:** Colocation, Fiber Operator

### 21. Revenue Pull-Forward (DIA-to-Fiber)
**Definition:** Discussions about starting with DIA (Dedicated Internet Access) immediately and upgrading to fiber later, accelerating time-to-revenue.
**Trigger Keywords:** DIA, dedicated internet, pull-forward, start now, upgrade later, immediate revenue, bridge, interim
**Primary Segments:** Fiber Operator

---

## Use Case x Segment Matrix

| Use Case | Colo | Fiber | Network Op | Neocloud | MSP |
|----------|------|-------|-----------|----------|-----|
| POC / Deployment Logistics | X | X | X | X | X |
| Partner / Reseller Channel | X | X | | | X |
| Cloud On-Ramp | X | X | | | X |
| Carrier / SP Federation | | X | X | | X |
| Data Center Interconnection | X | | | X | |
| Network Automation | X | X | X | X | X |
| Fiber Monetization | | X | | | |
| Wholesale Connectivity | | X | X | | |
| Multi-Cloud Access | X | | | X | X |
| Customer Portal | X | X | | | X |
| NaaS / Managed Services | | X | X | | X |
| Sovereignty / Brand Control | X | X | | | |
| E2E Visibility / Telemetry | | | X | X | X |
| Marketplace | X | X | X | X | X |
| AI / GPU Networking | X* | | | X | |
| Security / Encryption | | | X | X* | |
| Cross-Connect Optimization | X | X | | | |
| Egress Cost Reduction | X | | | X | |
| Geographic Expansion | | X | X | X | |
| Competitive Displacement | X | X | | | |
| Revenue Pull-Forward | | X | | | |

*X = primary segment for this use case. X* = sub-segment specific (AI Colo, Sovereign AI).*

---

## Classification Rules

1. **Multi-use-case calls are normal.** A single call typically maps to 2-5 use cases. Tag all that apply.
2. **Use the trigger keywords as a guide, not a strict filter.** Context matters -- a mention of "AWS" in passing is not a Cloud On-Ramp discussion.
3. **POC/Deployment Logistics is a meta-use-case.** It often co-occurs with the substantive use case (e.g., Cloud On-Ramp + POC Logistics).
4. **When in doubt between two similar use cases** (e.g., Cloud On-Ramp vs. Multi-Cloud Access), tag both. The reporting layer can consolidate.
5. **New use cases:** If a call discusses a topic not in this taxonomy, flag it for taxonomy review rather than forcing it into an existing category.
