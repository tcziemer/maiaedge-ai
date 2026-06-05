# Partner Cheat Sheet - Enterprise

**MaiaEdge for Enterprise IT and Network Teams**
*Use this when you're calling on multi-site enterprises, regulated industries, retail and distribution, manufacturing, financial services, healthcare systems, energy and utilities, or any enterprise running their own private network between data centers, branches, and clouds.*

> **Critical distinction:** Enterprises ARE the customer. They are not reselling MaiaEdge. They deploy it on their OWN corporate network as their private fabric. Drop the operator language ("your customer," "your portal," "your invoice"). Keep the ownership language ("your network," "your sites," "your team," "your control").

> **Lead use cases:** Dark fiber redundancy between data centers and cloud on-ramps under the enterprise's own control. Everything else is downstream of those two.

---

## Know Your Customer

| Attribute | Details |
|---|---|
| **What They Own** | Two or more data centers, plus distribution centers, plants, hospitals, branches, or regional hubs they care about. Often lease dark fiber between key sites. Run their own routing or SD-WAN overlay. Buy cloud connectivity through Megaport, Equinix Fabric, or carrier-managed services. |
| **Network Posture** | Heavy investment in branch SD-WAN (Cisco, Juniper SSR / 128T, Versa, Cato, Fortinet, Palo Alto). Far less mature on inter-DC determinism. Cloud on-ramps are usually outsourced or single-vendor. Type 2 fiber is a black hole. |
| **Scale** | Mid-market to Fortune 1000. $500M-$50B+ revenue. 2-10+ data center or critical sites. Multi-cloud (AWS + Azure + at least one of GCP / OCI / private). Network team of 5-100 engineers. |
| **Competitive Reality** | The carrier owns the path and the visibility. Megaport owns the cloud on-ramp experience. Their own network team owns the SLA when something breaks but cannot see across the boundary. AI workloads, multi-cloud architectures, and DR mandates are pulling more traffic through paths they do not control. |
| **Why They Buy MaiaEdge** | Own the private fabric across all sites instead of renting it from a carrier or a fabric vendor. Deterministic dark fiber redundancy without standing up routing protocols. Cloud on-ramps under their brand and their control. Hop-by-hop visibility everywhere their traffic goes. |

---

## Problems We Solve

| Problem | How MaiaEdge Solves It |
|---|---|
| Dark fiber between data centers is not actually redundant. One pair, one path, no automated failover | Their team runs diverse dark fibers into PBCs at each data center. Path computation handles failover automatically. Active-active or hot-standby, no routing protocols to tune |
| SD-WAN handles branches well but does nothing for deterministic inter-DC paths | MaiaEdge is the carrier-grade fabric underneath. SD-WAN keeps doing what it does at the edge. PBCs handle determinism between data centers and core sites |
| Cloud on-ramp goes through Megaport, Equinix Fabric, or a carrier portal that the enterprise does not control | Their team provisions on-ramps to AWS, Azure, GCP, OCI directly. Same fabric, same portal, same visibility as everything else on the network |
| Provisioning a new path between sites is a 6-12 week project across multiple vendors | Their team activates new paths in minutes. No LOAs, no BGP coordination, no carrier ticket queue |
| When traffic crosses a Type 2 circuit, visibility ends and finger-pointing starts | Hop-by-hop telemetry across every path, including circuits they do not own. Independent SLA proof for the first time |
| Adding a new data center, DR site, or cloud region is a months-long networking project | Drop a PBC at the new location, attach to the existing fabric, paths are live the same day |
| Sovereign and regulated workloads need provable path control that BGP best-effort cannot deliver | Policy-based routing with jurisdictional audit trails. The path stays where compliance says it has to stay |

---

## Top Pain Points (Their Words)

> "We pay for dark fiber between our data centers, but it is not really redundant. If something cuts that pair, we are taking an outage."

> "Our SD-WAN is great for the stores. It does nothing for our data center to data center traffic."

> "Cloud on-ramp goes through Megaport. We are at their mercy when something breaks."

> "Standing up a new DR site means six months of network engineering. We do not have six months."

> "We have AWS, Azure, and GCP. Each has its own connectivity story. We want one fabric across all three."

> "Our network team owns the SLA, but the moment traffic leaves our equipment we cannot see it."

> "Adding a new distribution center used to be a real estate project. Now the bottleneck is the network."

---

## Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|---|---|---|
| "How many data centers or critical sites are connected by paths you care about?" | "Two to ten. Inter-DC and DR are the ones that matter." | "One DC, everything else is branch SD-WAN." |
| "How is dark fiber redundancy handled between your data centers today?" | "Single pair, manual failover, or static routing. Painful." | "Fully diverse, automated failover, no issues." |
| "How do you reach the cloud today? Direct Connect through who?" | "Megaport, Equinix Fabric, or a carrier-managed service. Limited control." | "Native, fully owned by us." |
| "When something breaks on the path between two sites, how long until you know it is the network?" | "Hours. We are guessing between SD-WAN, the carrier, and the fiber provider." | "Minutes. Full observability." |
| "How long does it take to bring a new site or cloud region online?" | "Months. Multiple vendors, multiple tickets." | "Days. Self-service provisioning." |
| "How much of your network are you reliant on a carrier or a fabric vendor to provision and operate?" | "Most of the inter-site and cloud paths." | "Almost none. We own end to end." |
| "Do regulated workloads (financial, healthcare, government, AI) require provable path or jurisdictional control?" | "Yes, and we have no good answer today." | "Not in scope for us." |

---

## Objection Handling

| Objection | Rebuttal |
|---|---|
| "We have SD-WAN already" | "SD-WAN is the right answer for your branches. It does not give you deterministic dark fiber redundancy between data centers, and it does not give you a fabric you control across cloud regions. MaiaEdge is the carrier-grade layer underneath. SD-WAN keeps doing what it does at the edge." |
| "Our carrier handles redundancy" | "They handle the path you bought from them. They do not handle the path you have not bought yet, and they do not give you visibility into either one. MaiaEdge gives your team diverse dark fiber failover that you control, plus visibility on every hop." |
| "Megaport works fine for our cloud on-ramp" | "It does, until something breaks. You are on their portal, their invoice, their support queue. With MaiaEdge, the cloud on-ramp is part of your fabric. Same provisioning, same visibility, same control as everything else." |
| "We do not have the engineering depth for this" | "That is why enterprises like this. No routing protocols, no BGP, no MPLS to manage. Drop a PBC at each site, the cloud control plane handles path computation. Your team operates it the way they operate any other piece of infrastructure." |
| "We just signed a long carrier agreement" | "MaiaEdge sits over your existing transport. Your fiber, your DIA, your carrier circuits, your cloud direct connects. We do not replace any of that. We make it deterministic and visible end to end." |
| "This sounds expensive" | "Compare it to what is leaking. Carrier change orders. Megaport margin on every cloud on-ramp. Outages on dark fiber that was supposed to be redundant. New site projects that take six months. OpEx subscription that scales with your network." |
| "Who are you?" | "Same team that built Acme Packet (Oracle, $2.1B) and 128 Technology (Juniper, $450M). Two exits, $2.55B+ combined. We built the carrier-grade infrastructure your network team already runs in some form. Now we are giving the enterprise the same control." |

---

## Competitive Quick Hits

| Competitor | Quick Positioning |
|---|---|
| **Status quo (do nothing)** | The biggest competitor. Most enterprises live with carrier-managed everything because they assume the alternative is hiring a carrier-grade engineering team. MaiaEdge is the answer that does not require one. |
| **SD-WAN (Cisco, Juniper SSR / 128T, Versa, Cato, Fortinet, Palo Alto)** | SD-WAN is for the branch and the user. MaiaEdge is for the data center, the dark fiber, the cloud on-ramp. Different layer, different problem. The two are complementary, not competitive. |
| **Carrier-managed services (AT&T NetBond, Verizon SCI, Lumen, BT, NTT)** | The carrier owns the path, the visibility, and the timeline. MaiaEdge gives the enterprise back the ownership without forcing them to become a carrier. |
| **Megaport / Equinix Fabric / PacketFabric** | Great fabrics if you want someone else to operate yours. With MaiaEdge, the enterprise operates its own. The third-party fabrics become a transport option the enterprise leverages by API when it makes sense. |
| **Internal build (network team writes scripts)** | A few enterprises try this. It is fragile, hard to maintain, and one engineer leaving puts everything at risk. MaiaEdge is the productized version of what the best teams try to build. |
| **Cloud-native networking (AWS Cloud WAN, Azure Virtual WAN, Google NCC)** | Each cloud has its own. They do not federate well across clouds, and they do not solve the dark fiber redundancy problem at all. MaiaEdge is the cross-cloud, cross-DC answer. |

---

## Persona Talk Track Matrix

| Persona | Titles | The Pitch |
|---|---|---|
| **Network Architect / Principal** | Principal Network Architect, Network Architect, Distinguished Engineer, Sr. Network Architect | "Your dark fiber between data centers is one cut away from an outage. Drop a PBC at each DC, run diverse fibers in, the path computation handles failover automatically. No routing protocols to tune. Hop-by-hop telemetry across every path. The cleanest piece of infrastructure your team has put in this year." |
| **VP Network / Infrastructure** | VP Network, VP Infrastructure, VP Network Engineering, VP Platform | "Your team owns the SLA on every site-to-site path and on every cloud on-ramp. They cannot see most of those paths today. MaiaEdge gives them the same observability and the same control end to end. Projects that took six months take days. Carrier dependency drops without giving up the carrier." |
| **CIO / CTO** | CIO, CTO, SVP IT, EVP Technology | "Your network team is being asked to support multi-cloud, AI workloads, and a growing list of regulated requirements on a footprint that was designed for the last decade. MaiaEdge is the carrier-grade fabric under all of it. The same team that built the infrastructure your carriers run is now giving you the platform to run your own." |
| **Cloud Architecture** | VP Cloud Architecture, Sr. Director Cloud Infrastructure, Cloud Network Architect | "Cloud on-ramp through a third-party fabric works until you need to provision quickly, troubleshoot deeply, or move workloads between providers. MaiaEdge gives you native on-ramps to AWS, Azure, GCP, OCI under one fabric. Same provisioning experience as your inter-DC paths." |
| **Network Operations** | Director of Network Operations, NOC Manager, VP Service Delivery | "When something breaks on Type 2 fiber today, you are guessing. MaiaEdge gives your NOC hop-by-hop visibility on every path, including the carrier circuits you do not own. Mean time to identify drops from hours to minutes." |
| **Security / Compliance** | CISO, VP Information Security, Director of Compliance | "Sovereignty and data residency requirements are landing on enterprise networks that were built for performance, not policy. MaiaEdge enforces path policy with jurisdictional audit trails. The path stays where compliance says it has to stay, and you have proof." |

---

## Proof Points

| Source | Quote / Outcome | When to Use |
|---|---|---|
| **Multi-DC retail / distribution reference** | Enterprise replacing static dark fiber redundancy with deterministic, automated failover under their own control | Retail, distribution, manufacturing, multi-DC enterprise pattern |
| **Equinix** (Josh Sordelet, Principal PM) | "Revolutionary and creative. Abstracting complexity with their PBC approach." | Technical skeptics, "why have I not heard of you" |
| **Acme Packet / 128 Technology** | $2.55B+ combined exits. SBC used by 90% of carriers. Founders of the SD-WAN session-smart category. | "Who are you?" objection (live calls only, never in cold outreach) |
| **NTT, IENTC, Arvig, Centra, RevNet** | Carrier-grade deployments showing the same fabric carriers trust is now available to the enterprise | Credibility for technical and infrastructure leaders |

---

## Vertical Cheat Codes

**Retail and distribution:** Multi-DC plus distribution centers, regional hubs, large stores. Lead with dark fiber redundancy between primary DCs, then cloud on-ramp for SaaS and data analytics workloads. Extend to deterministic paths into the highest-traffic distribution centers.

**Manufacturing:** Plants connected to corporate DCs, often with operational technology requirements (latency-sensitive process control, machine vision, robotics). Lead with deterministic plant-to-DC paths and DR redundancy. Sovereign supply chain data is increasingly a buyer.

**Healthcare systems:** Hospital-to-hospital and EHR data center connectivity with strict uptime and PHI handling requirements. Lead with diverse dark fiber redundancy between EHR DCs, cloud on-ramps for radiology and analytics, and policy-based path control for HIPAA-sensitive flows.

**Financial services:** Low-latency between DCs, multi-cloud determinism, regulator-friendly path control. Lead with deterministic inter-DC paths, audit-ready policy enforcement, and cloud on-ramps under their control instead of through a fabric provider.

**Energy and utilities:** Operational networks (SCADA, substation, control center) plus corporate IT. Lead with deterministic, visible paths between control centers and substations, and dark fiber diversity on the most critical operational links.

**Government and regulated:** Sovereignty, jurisdictional control, and compliance audit trails are the entry. Lead with policy-based routing and the ability to prove where every packet went, in addition to the standard redundancy and on-ramp angles.

**Logistics and supply chain:** Hub-and-spoke between distribution centers and hubs. Lead with fast site-bring-up (new DCs and hubs go live in days, not months) and deterministic paths for warehouse management and IoT telemetry.

---

## Vocabulary Check (Enterprise-Specific)

**USE:** data center, DC, DR site, dark fiber, dark fiber redundancy, diverse paths, fiber pair, hot standby, active-active, cloud on-ramp, direct connect, multi-cloud, hop-by-hop visibility, deterministic paths, your network, your fabric, your team, your control, sovereignty, audit trail, PBC, port extender, fabric.

**BANNED for enterprises:** Operator-monetization language ("keep your customer," "your portal, your invoice," "build your own fabric to sell"). Enterprises do not resell. Wholesale and carrier-economics framing ("monetize stranded fiber," "wholesale activation," "NNI in minutes," "win multi-state deals," "extend reach to new markets") belongs to other segments. Also banned for cold outreach: founder credibility anchors (Acme Packet, 128T, Andy Ory). Reserve those for live calls and follow-ups.

**Tone:** Peer-to-peer with the network team. Operational, not commercial. Lead with the path, the redundancy, the visibility, the control. Avoid SD-WAN comparisons that sound dismissive. SD-WAN is doing its job. MaiaEdge is doing a different job, in a different layer.

---

## Special Cases

**Already running 128T / Juniper SSR:** Strong fit. The SSR / 128T overlay is exactly the kind of session-smart routing that benefits from deterministic, observable underlay paths. Position MaiaEdge as the dark-fiber and cloud-on-ramp layer underneath the SSR fabric. Diverse PBCs feeding the SSR HA interfaces is a clean pilot pattern.

**Heavy Cisco SD-WAN / Catalyst:** Same framing. SD-WAN handles branch and user. MaiaEdge handles inter-DC and cloud on-ramp. Complementary, not competitive.

**Already on Megaport / Equinix Fabric in production:** Do not ask them to rip it out. Position MaiaEdge as the layer they extend their own control onto, with Megaport / Equinix becoming a transport option the fabric leverages by API. The customer keeps every existing investment.

**Single-DC, branch-heavy enterprises:** Structural misfit. The dark fiber redundancy and inter-DC determinism story does not land. Flag and pass to SD-WAN partners.

**SMB / sub-$100M revenue:** Generally too small to operate a private fabric. Refer them to the carriers and MSPs that consume MaiaEdge upstream.
