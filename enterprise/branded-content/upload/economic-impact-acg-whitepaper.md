<!-- INTERNAL CONTEXT METADATA (HTML comment - does NOT render in any built PDF)
SEGMENT SCOPE: Fiber Operator, Network Operator, Colocation (the SP/colo "deliver + wholesale cloud on-ramp"
segments). Secondary: MSP/Aggregator (the federated-marketplace / partner-reach angle).
DO NOT use for Enterprise (cost-center buyer of cloud on-ramp, not a seller - the 67% margin / wholesale /
monetization framing is wrong for them) or NeoCloud (sells GPU compute, does not wholesale cloud on-ramp to
enterprises - use the GPU Cluster Connectivity brief instead). These are operator PROFIT-CENTER economics.
SOURCE: third-party (ACG Research) economic models. The 67% / ~67% / 53% figures are third-party model outputs -
attribute to ACG Research and re-verify before any external/customer use.
PROVENANCE: Economic white paper, dated 2026-06-15.
-->

# The Business Impact of MaiaEdge on Cloud On-Ramp, Cloud Partner Services, and Ethernet over DIA

*Figures 1–5 below are charts in the source document; shown here by caption.*

## Executive Summary

Enterprise demand for private cloud connectivity continues to accelerate as organizations increasingly rely on cloud-based applications, AI workloads, and hybrid multi-cloud architectures. Regional service providers and colocation providers are under growing pressure to deliver secure, high-performance cloud connectivity services rapidly and cost-effectively. However, many providers are missing revenue opportunities because they cannot deliver cloud connectivity and access to locations outside their footprint. This is complicated by the fact that cloud on-ramps and partner connectivity require manual processes which are resource-intensive and slow to deliver.

Regional service providers and colocation providers face two distinct challenges:

1.  Enterprises demand cloud connectivity, but not all providers can deliver it; the ones that do deal with manual and costly provisioning.

2.  Interconnecting with partner providers is labor intensive plus providers loose visibility and control once traffic leaves their network.

**Solution**: MaiaEdge provides a carrier neutral interconnection engine, automated private path provisioning across any underlying transport, and simplified cloud on-ramp connectivity through open APIs with Equinix and Megaport.

The economic benefits of the MaiaEdge solution are:

  - Expand network reach through partners.

  - A low barrier to entry for cloud on-ramp services.

  - Monetization of existing cloud connectivity through oversubscription with load balancing.

  - Monetization of existing cloud connections by easily selling it to partner providers.

  - Reducing cost by leveraging DIA to provide layer 2 services.

ACG Research developed three economic models showing MaiaEdge business impacts:

1.  Service provider cloud on-ramp TCO.

2.  Service provider wholesale services business case.

3.  Ethernet over DIA with MaiaEdge vs dedicated L2 Ethernet.

The results of the ACG business case analysis showed:

  - MaiaEdge cloud on-ramp resulted in a **67% TCO savings.**

  - Operators using MaiaEdge to wholesale cloud connectivity can generate **margins approaching 67% with payback in approximately six months.**

  - Ethernet over DIA with MaiaEdge resulted in a **53% TCO savings** over dedicated L2 Ethernet.

Overall, the analysis demonstrates that MaiaEdge is both a cost optimization and revenue growth platform that enables service providers to deliver scalable, automated, and economically efficient cloud interconnection services.

## MaiaEdge Solution

The MaiaEdge solution enables automated private path provisioning, cloud on-ramp monetization, partner reach expansion, and visibility across provider domains. MaiaEdge combines a 1RU Path Border Controller (PBC) deployed at key interconnection points with a cloud-native Path Computation Engine (PCE) that automates private path provisioning, traffic engineering, SLA policy, and visibility across both owned and partner networks. Together, these components allow operators to launch cloud on-ramp services, sell more capacity across existing cloud connections, offer wholesale cloud connectivity to partners, and deliver private Ethernet services over available transport options where appropriate.

## Economic and TCO Benefits of MaiaEdge

MaiaEdge delivers significant economic benefits across many use cases. This paper presents the business case for three use cases:

1.  Delivering and monetizing cloud on-ramp services.

2.  Selling wholesale access to existing cloud on-ramp services.

3.  Establishing Ethernet over DIA with MaiaEdge vs. traditional Carrier Ethernet.

This paper compares the Present Mode of Operation (PMO) with the MaiaEdge Future Mode of Operation (FMO) and quantifies the financial and operational advantages of the MaiaEdge solution.

## Cloud On-Ramp Use Case

Enterprise demand for private cloud connectivity continues to grow as organizations increasingly rely on cloud services from AWS, Azure, and GCP. Enterprises look to their partners for cloud on-ramp services:

  - Regional Communication Service Providers.

  - Data Center Colocation Providers.

Each of these partners must therefore deliver secure, high-performance cloud connectivity services quickly and cost-effectively.

### Cloud On-Ramp Present Mode of Operation (PMO)

In the PMO access and colocation providers need to connect to Equinix or MegaPort using an NNI which introduces complexity, delays, and additional expenses. Also, providers typically have low levels of port utilization (approximately 30%) because they lack advanced traffic engineering and SLA-aware path optimization capabilities.

Traditional architectures also often require dedicated routers in Equinix or Megaport facilities plus cloud routers for multi-cloud provisioning increasing capital and operational costs. MaiaEdge eliminates the needs for both. All the provider needs are a PBC and connections to Equinix or Megaport. Alternatively, the provider can connect to Equinix/Megaport through another provider using MaiaEdge marketplace. Provisioning happens automatically via APIs.

### Future Mode of Operation (FMO) with MaiaEdge

The MaiaEdge FMO architecture automates and simplifies cloud on-ramp provisioning while significantly improving infrastructure efficiency and operational scalability. In the MaiaEdge solution, enterprise access circuits including DIA, MPLS, and Carrier Ethernet are dynamically mapped to cloud on-ramp virtual circuits by the MaiaEdge PBC using automated orchestration and traffic engineering. The PCE continuously monitors real-time traffic metrics across a shared Equinix or Megaport port, so that when traffic bursts occur, the PCE dynamically load balances connections. The PCE is the central control plane engine that makes this oversubscription model operationally possible.

This capability enables providers to:

  - Increase utilization of expensive 100G cloud exchange ports.

  - Support customer bursting above committed information rates (CIR).

  - Dynamically prioritize traffic flows.

  - Optimize ingress and egress traffic engineering.

  - Reduce stranded bandwidth capacity.

  - Lower overall cost per delivered gigabit.

For example, a provider may offer a customer a 1 Gbps CIR service capable of bursting to 5 Gbps while still maintaining SLA performance through intelligent traffic engineering and dynamic path optimization.

## TCO Model for Cloud On-Ramp Services

To quantify the operational and economic benefits of MaiaEdge, ACG Research developed a five-year Total Cost of Ownership (TCO) model comparing the PMO with a MaiaEdge-based FMO cloud on-ramp architecture. The analysis period spans January 2026 through December 2030 and evaluates operational expenses (OpEx), network infrastructure costs, provisioning labor, and operational staffing requirements.

### TCO Model Assumptions

For both PMO and FMO scenarios, the model assumes:

  - 1,000 enterprise customer sites

  - 5% annual site growth

  - 500 Mbps average bandwidth per site

  - 15% annual traffic growth

  - Five-year TCO analysis period (2026–2030)

  - Connectivity through 100G Equinix cloud exchange ports

The model also assumes a five-year MaiaEdge PBC license.

### Cloud Connectivity Cost Assumptions

The following average recurring costs were used in the model:

  - Equinix 100G Port: $1,500 monthly recurring charge (MRC)

  - Equinix 500 Mbps virtual circuit: $150 MRC

  - Cross connects between the service provider and Equinix: $500 MRC per port

These costs were applied consistently across the PMO and FMO scenarios to isolate the operational and utilization benefits enabled by MaiaEdge.

### PMO Assumptions

The PMO model represents a traditional cloud on-ramp architecture using manual provisioning and limited traffic engineering capabilities.

Key assumptions include:

  - 30% average cloud exchange port utilization

  - Two hours of provisioning labor per customer site

  - One hour of annual network operations labor per customer site

The low utilization assumption reflects the operational limitations of traditional environments where providers typically avoid aggressive oversubscription because they lack SLA-aware traffic engineering and dynamic bandwidth management capabilities.

### FMO Assumptions

The MaiaEdge Future Mode of Operation (FMO) model assumes automated provisioning, advanced traffic engineering, and intelligent bandwidth optimization enabled by the MaiaEdge platform.

The base FMO scenario assumes:

  - 1.5X oversubscription enabled through traffic engineering

  - 15 minutes of provisioning labor per customer site

  - 10 minutes of annual network operations labor per customer site

### Cloud On-Ramp TCO Results

The TCO analysis demonstrates that the MaiaEdge Future Mode of Operation (FMO) delivers substantial economic advantages compared to the traditional Present Mode of Operation (PMO) cloud on-ramp architecture. Over the five-year analysis period, the PMO generated a total TCO of approximately $4.1 million, driven primarily by recurring Equinix port charges, cross connects, provisioning labor, and network operations costs. The MaiaEdge FMO with 150% oversubscription reduced total TCO to approximately $1.37 million, representing a 67% reduction versus PMO. The results of the TCO analysis are presented in Figure 1 and Figure 2.

*Figure 1 — MaiaEdge Cloud On-Ramp TCO Savings*

*Figure 2 — MaiaEdge Annual TCO Savings*

Figure 3 presents a breakdown of MaiaEdge cost savings. The largest contributor to savings was improved utilization of expensive 100G cloud exchange ports due to MaiaEdge traffic engineering and oversubscription capabilities. The PMO required significantly more Equinix ports and cross connects to support customer demand due to low average utilization. MaiaEdge reduced Equinix port costs from approximately $2.5 million in the PMO scenario to approximately $540,000 in the FMO scenario. Cross-connect costs were also reduced from approximately $840,000 to approximately $180,000.

*Figure 3 — Key Drivers of TCO Savings*

Operational savings were also significant. Automated provisioning and simplified operations reduced network management and provisioning labor costs by approximately 85% compared to the PMO model.

The results show that MaiaEdge not only lowers infrastructure and operational costs but also improves scalability and enables providers to support substantially more cloud connectivity traffic using fewer physical interconnections.

## Wholesale Cloud On-Ramp Business Case

In addition to reducing the cost of delivering cloud connectivity services, MaiaEdge enables service providers to create new wholesale revenue opportunities by monetizing shared cloud exchange infrastructure and expanding access to cloud on-ramp services.

Many regional and Tier 3 providers do not maintain direct connectivity into major cloud exchange facilities such as Equinix or Megaport because the cost and operational complexity of deploying dedicated NNIs, ports, and cross connects is too high. MaiaEdge addresses this challenge by allowing providers with existing cloud exchange infrastructure to wholesale connectivity services to other operators through a federated marketplace model.

The business case we created assumes an initial deployment of one 100G Equinix port with the addition of two new ports annually as demand grows. Under the 1.5X oversubscription model, a single 100G port can support 150 Gbps of capacity. The model assumes 75% average utilization of the bandwidth which is an effective sellable bandwidth of 113G.

Wholesale services are offered in multiple tiers ranging from 1G to 10G services targeted primarily at regional service providers. The model assumes an average blended wholesale selling price of approximately $200 per Gbps per month with 3% annual price escalation.

The financial results demonstrate a strong revenue and profitability profile:

  - Annual revenue grows from approximately $270,000 in Year 1 to approximately $2.7 million by Year 5

  - Five-year cumulative cash flow exceeds approximately $4.7 million

  - EBITDA margin improves from approximately 55% in Year 1 to nearly 67% by Year 5

  - EBITDA grows from approximately $150,000 in Year 1 to approximately $1.8 million in Year 5

*Figure 4 — MaiaEdge Wholesale Business Case*

The MaiaEdge marketplace model also enables participating providers to expand their service footprint without deploying infrastructure into every Equinix or Megaport location. Small or large providers can offer wholesale services using the MaiaEdge marketplace with a low barrier to entry.

## Ethernet over DIA vs Tradition Layer 2 Services

Many service providers offer L2 Ethernet services to their enterprise customers. Ethernet is cost effective in many metro areas; however, L2 Ethernet services can be more expensive for certain use cases such as traversing undersea cables and international connections. MaiaEdge has been used successfully by service providers to offer L2 Ethernet connections over DIA connections at a significantly lower price. This can also be used by providers to offer L2 services when Ethernet services are not available at a given site.

As an example, consider a service provider that needs to provide 1G Ethernet connections from New York to London. If a service provider provides fifty 1 Gbps circuits to enterprise customers, the growth rate is 10%, and average Ethernet and DIA expenses are incurred, the cost of Ethernet circuits vs Ethernet over DIA with MaiaEdge is presented below:

*Figure 5 — MaiaEdge DIA Savings over Ethernet*

The cumulative five-year savings of DIA using MaiaEdge over Ethernet is 53%.

## Conclusion

MaiaEdge enables service providers to simplify cloud interconnection, expand service reach, and improve profitability through automation, federation, and intelligent traffic engineering. By replacing manual provisioning and low-utilization cloud connectivity models with a software-driven architecture, providers can deliver cloud on-ramp, wholesale connectivity, and Ethernet services more efficiently and at lower cost.

ACG's analysis demonstrates that MaiaEdge can reduce cloud on-ramp TCO by more than 67%, generate profitable wholesale cloud connectivity services with margins approaching 67%, and reduce Layer 2 Ethernet delivery costs by 53% through Ethernet-over-DIA architectures. At the same time, MaiaEdge enables faster service activation, improved infrastructure utilization, and new revenue opportunities through partner ecosystems and cloud marketplace participation.

As cloud connectivity becomes increasingly strategic, MaiaEdge provides service providers with a practical path to building scalable, automated, and economically optimized interconnection services while maintaining control of the customer relationship and network experience.
