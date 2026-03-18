# PBC & PCE Datasheet

> Converted from: Draft PBC and PCE Datasheet.docx

Datasheet
Path Border Controller & Path Computation Engine 
Product Overview 
 
The MaiaEdge solution combines edge hardware, Path Border Controller (PBC), and a cloud-native orchestrator, Path Computation Engine (PCE), to deliver a new class of carrier network infrastructure, purpose-built for seamlessly interconnecting disparate networks. With MaiaEdge, operators can automate private path provisioning across fragmented internal infrastructure and federate with partner providers to extend service reach instantly over Type 2 connections.
 
Path Border Controller (PBC): A 1RU edge appliance deployed at carrier hotels, meet-me rooms, and PoPs. It merges L2 switching and L3 routing for flexible transport, automates private path provisioning, and encrypts every path for high throughput connectivity. 
Path Computation Engine (PCE): A cloud-native orchestrator that continuously computes optimal routes, automates deterministic path creation, and provides end-to-end visibility across network boundaries. 
 
Federated Private Networking 
 
The MaiaEdge PBC and PCE provide the foundational infrastructure for Federated Private Networking. Federated Private Networking transforms isolated network silos into a unified, operator-owned ecosystem where service providers, fiber operators, and colocation providers can share services to expand offerings and monetize spare capacity. With MaiaEdge, providers can establish automated NNIs in minutes, extending real-time visibility and control across network boundaries while maintaining complete operational sovereignty over their customer relationships. 
 
Key Features and Capabilities 
 
Automated Provisioning 
Speed time to service delivery. Activate encrypted private paths in minutes and automate NNI provisioning. Eliminate the traditional manual processes of establishing private connectivity across disparate domains without CLI commands, BGP, OSPF, or MPLS complexity. 
Transport Agnostic Fabric 
Merged L2 and L3 capabilities provide the flexibility to combine fiber and DIA connectivity types in one unified fabric. Reduce complexity and accelerate service delivery by starting with DIA for instant connectivity and adding fiber when available, keeping DIA for automatic failover.
Deterministic Path Engineering
The cloud-native Path Computation Engine (PCE) provides real-time deterministic route calculation based on latency, utilization, and policy metrics. SRLG-aware path selection ensures true physical redundancy by automatically avoiding shared trenches and carriers. Deterministic path control provides bandwidth allocation and traffic management over Type 2 circuits with data-backed SLA proof. 
Secure by Default 
Each path is secured automatically with line-rate AES-256-GCM IPsec encryption. 
End-to-End Visibility and Control 
Hop-by-hop telemetry (jitter, loss, latency) and SLA control across internal networks, partner networks, and cloud on-ramps. 
Sovereign Customer Experience Management
White-label dashboard offers customers a self-service portal with SLA transparency. Partner topology stays hidden, so customers see only their provider’s brand regardless of path traversal. Q-in-Q tagging ensures complete customer isolation.  
Automated Cloud On-Ramp 
Native API integrations with Equinix and Megaport enable direct access to AWS Direct Connect and Azure ExpressRoute. Provision cloud on-ramps without routing complexity. 
Open Ecosystem & BSS/OSS Integration
API-first design enables direct integrations with billing and operations systems. Built for industry-standard Mplify LSO Sonata interoperability and ecosystem extensibility. 
Turnkey Data Center Fabric  
 
Colocation providers can deliver a premium fabric experience without years of development. The PBC and PCE provide a fabric-in-a-box solution for providers to speed interconnection, expand their service catalogue and offer a branded self-service portal. Combine the PBC with the MaiaEdge Port Extender, integrated switch for 48 additional tenant ports.  

Path Border Controller Hardware Features
[Front view and back view of the PBC. With labeled parts.]


Subscription Licenses 
The Path Border Controller hardware and Orchestration Software are sold as a combined subscription. Available in 1, 3, or 5-year terms at 10G or 100G throughput tiers. Additional PBCs for high availability are sold at a discounted rate. Optional to add the Port Extender, integrated switch for additional port capacity.
About MaiaEdge 
MaiaEdge delivers a new class of carrier infrastructure, enabling operators to instantly interconnect isolated networks into a unified fabric. Combining hardware and cloud-native software, MaiaEdge empowers providers to activate private paths automatically across network boundaries with complete visibility and sovereignty. Founded by the industry veterans behind Acme Packet and 128 Technology, MaiaEdge helps providers monetize their assets and expand global reach. 

Category | Feature 
Performance | 
Throughput | Dual 100GbE
Encryption Throughput  | Line-rate AES-256-GCM IPsec
Latency | <2 μs overhead
Interfaces | 
Port Configurations  | Dual 100GbE Ethernet (QSFP28)
Management Ports  | 2x 1GB RJ45
External USB | 1x USB 2.0
Console Port  | RJ45 115.2 kbps
Physical | 
Form Factor | 1RU Rackmount 
Chassis (H x W x D) | 1.625 x 17.24 x 11.46 in
Dimensions with ears and tabs H x W x D 
 | 1.625 x 19.02 x 12.13 in

Weight | 9.5 lbs w/power supplies installed
Power/Environmental | 
Power Supply | Internal: AC, DC
Redundant Power Supply | Yes
Power Consumption | 
Operating Temperature  | 0°C to 50°C / (32 to 104°F)
Storage Temperature  | -40 to 70°C / (-40 to 158°F) 
Operating Humidity   | 
Cooling | Internal fan-based forced-air cooling
Airflow  | Front-to-Back (F2B) — intake at front bezel / port side, exhaust at rear (fan/PSU side)
Data center airflow | Standard hot-aisle/cold-aisle layouts: cold aisle at front (bezel/port side) intake, hot aisle at rear exhaust.