# Partner Cheat Sheet - Colocation Operator

**MaiaEdge for Colocation Providers (Standard + AI Signals)**
*Use this when you're calling on data center operators, carrier hotels, interconnection facilities, or AI-ready colos.*

---

## Know Your Customer

| Attribute | Details |
|---|---|
| **What They Own** | Buildings, meet-me rooms, metro fiber. NOT route miles. AI-focused colos may have liquid cooling, high-density power (30kW+ racks), GPU cloud tenant relationships. |
| **Revenue Model** | Space and power (60-80%, low margin), cross-connects (10-20%), cloud on-ramps (0-5%). AI-focused colos add infrastructure services for GPU cloud providers (Lambda Labs, Crusoe, Nebius). |
| **Scale** | 1-10+ facilities, 20-500 employees, $10M-$500M revenue. |
| **Competitive Reality** | Tenant expectations set by Equinix and Digital Realty. Cloud revenue going to NaaS providers. GPU cloud tenants expect deterministic connectivity, not just fast cross-connects. |
| **Why They Buy MaiaEdge** | Build their own fabric instead of pushing tenants to Megaport. Keep the customer, the margin, the brand. AI tenants get deterministic paths as a marketed service. |

---

## Problems We Solve

| Problem | How MaiaEdge Solves It |
|---|---|
| 6+ week cross-connect provisioning (LOAs, truck rolls, VLAN config) | Their team provisions virtual cross-connects in minutes through their own self-service portal |
| Stuck selling space and power with no service layer on top | Their team builds a fabric with cross-connects, private paths, cloud on-ramps, and partner interconnects as automated products |
| Can't match Equinix interconnection experience | Fabric-in-a-box. PBC in the meet-me room, PCE in the cloud, portal under their brand. Live in weeks, not years |
| Cloud on-ramp is either not offered or is thin-margin | Their team offers cloud on-ramps natively under their own brand. Megaport / Equinix Fabric become backend infrastructure they leverage by API |
| Tenants want a marketplace of services, not just space | Service fabric with cloud on-ramps, partner interconnects, and SaaS routing under the operator's brand |
| Limited reach beyond the physical facility | Virtual meet-me room extends interconnection beyond the building to other DCs, partners, and clouds |
| AI Colo: best-effort networking breaks inference | Deterministic private paths with controlled latency. Hop-by-hop visibility for the GPU tenant's SLA |

---

## Top Pain Points (Their Words)

> "Every cross-connect is still a project. LOAs, truck rolls, VLAN config. Tenants expect portal-driven self-service."

> "Building our own connectivity services takes years of development and specialized teams we don't have."

> "Cloud on-ramp would be a product if we could stand it up without a hyperscale facility build."

> "We have multiple sites and no easy way to connect them for a tenant who wants capacity in more than one."

> "GPU cloud tenants are asking for latency guarantees we can't make with traditional networking." *(AI-focused colos)*

---

## Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|---|---|---|
| "How do you handle tenant requests for cloud connectivity?" | "We refer them out to a third-party fabric." | "We have our own cloud on-ramp." |
| "What's your revenue split: space and power vs. connectivity?" | "90% space and power, 10% cross-connects." | "Connectivity is 30%+ of revenue." |
| "When a tenant needs a cross-connect, what's the timeline?" | "Hours per connection, LOAs, manual config." | "Minutes, fully self-service." |
| "When a tenant needs capacity in a second site, what does that look like?" | "We handle it as a separate project, site by site." | "Already stitched together via our own fabric." |
| "How many deals have you lost to provisioning delays?" | "Several. Six-week timelines kill deals." | "None. We provision quickly." |
| **AI Colo:** "Do you have GPU cloud tenants like Lambda, Crusoe, or Nebius?" | "Yes, fastest-growing segment." | "No GPU/AI tenants, no plans." |
| **AI Colo:** "Are you investing in liquid cooling or 30kW+ racks?" | "Yes, building AI-ready infrastructure." | "Standard density only." |

---

## Objection Handling

| Objection | Rebuttal |
|---|---|
| "Megaport already handles this for us" | "When tenants use Megaport, they're on Megaport's portal, Megaport's invoice, building loyalty to Megaport. You become a landlord, not a connectivity provider. MaiaEdge gives you the same capability under your brand, your invoice, your control." |
| "We don't have the engineering resources" | "That's why colos love it. No routing protocols, no BGP. Rack a 1RU PBC in the meet-me room, connect to the cloud PCE, provision from the portal. Centra called it 'drop it in and add water.'" |
| "This sounds expensive" | "Compare it to what's leaking. Megaport margin on every tenant connection. Deals lost to 6-week provisioning. Subscription pricing, starts at 1G, scales to 100G." |
| "This sounds complex" | "The opposite. No routing protocols, no BGP, no MPLS. PBC + PCE + portal. That's it. Fabric-in-a-box." |
| "We've considered building our own" | "Most teams quote 18-24 months and several million in development. Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper) already did the work." |
| "Our GPU cloud tenants haven't asked for this" | "They will. Inference performance depends on network predictability. Best-effort introduces jitter that breaks token-by-token latency. Deterministic paths with hop-by-hop visibility let you guarantee what their workloads need." |
| "We just provide the facility, networking is the tenant's problem" | "GPU tenants need network determinism the same way they need power and cooling. If you're investing in liquid cooling and high-density racks, network predictability is the missing piece. MaiaEdge lets you be the full-stack AI infrastructure partner." |

---

## Competitive Quick Hits

| Competitor | Quick Positioning |
|---|---|
| **Megaport / Equinix Fabric** | They own the fabric AND the customer. MaiaEdge means the colo owns both. We integrate with them by API for cloud reach. |
| **Lumen PCF** | Lumen builds their empire. MaiaEdge empowers the colo to build theirs. |
| **SD-WAN** | SD-WAN is for enterprise branches. MaiaEdge is for carrier and colo infrastructure. Different layer, different buyer. |
| **Internal build** | 18-24 months and several million in development. The MaiaEdge team has already done that work. |
| **Status quo (do nothing)** | Six-week cross-connect timelines lose deals. Equinix is at 500,000+ cross-connects. The gap is the threat. |

---

## Persona Talk Track Matrix

| Persona | Titles | The Pitch |
|---|---|---|
| **Technical / Engineering Leader** | CTO, VP Engineering, VP Technology, VP Infrastructure, VP Platform | "Most colos sell space and power while Equinix captures interconnection revenue. Drop a 1RU PBC in the meet-me room. Your team offers fabric services, automated cross-connects, and cloud on-ramps. Weeks to deploy, not years. Build your own fabric. Keep the customer, the margin, and the control." |
| **Commercial Leader** | CRO, VP Sales, VP Business Development, VP Commercial, VP Partnerships, VP Interconnection | "Your tenants ask for cloud connectivity and you say 'call Megaport.' That's a relationship and a margin going to Megaport. With MaiaEdge, your team offers cloud on-ramps yourself. Your brand, your invoice, your portal. Same facility, now the margin stays with you." |
| **Network Engineering** | Sr. Network Engineer, Lead Network Engineer, Network Architect, Infrastructure Architect | "Your team spends hours on each cross-connect: LOAs, VLAN coordination, routing config. Drop a PBC in the meet-me room. 1RU. No routing protocols. The cloud PCE handles path computation. Hop-by-hop telemetry across every path." |
| **AI Colo Technical** | Chief Network Engineer, VP Infrastructure (with GPU tenants), Head of Platform Engineering | "Inference cares about tail latency and jitter. Best-effort paths introduce variance. Deterministic Ethernet paths with controlled latency and hop-by-hop visibility give the GPU tenants the predictability their workloads need. Sell it as a marketed SLA, not a best-effort cross-connect." |
| **AI Colo CFO / Strategic** | CFO, CEO (anchor-tenant model), VP Strategy | "Your AI tenants disclose customer concentration in their filings. MaiaEdge lets you onboard 2-3 additional hyperscalers into the same building with isolated paths. Tenant diversification on the same capex base. Concentration risk down. Revenue per MW up." |

---

## Proof Points

| Customer | Quote | When to Use |
|---|---|---|
| **RevNet** | "Imagine having Megaport capability between providers" | NaaS comparison, partner connectivity, cloud on-ramp |
| **Centra** | "Fabric in a box. Drop it in and add water and it works." | Complexity objection, engineering capacity objection |
| **Equinix** (Josh Sordelet, Principal PM) | "Revolutionary and creative. Abstracting complexity with their PBC approach." | Technical skeptics, credibility, "why haven't I heard of you?" |
| **AI infrastructure** | Deterministic paths for GPU cloud tenant connectivity | GPU cloud tenants, AI workloads, inference SLAs |

---

## AI Signal Detection

| Signal Strength | Indicators | Action |
|---|---|---|
| **STRONG** | Confirmed GPU cloud tenants (Lambda, Crusoe, Nebius), liquid cooling, 30kW+ racks | Lead with AI / inference messaging, deterministic paths, marketed SLA framing |
| **MEDIUM** | AI mentioned in marketing, building high-density capacity, hyperscaler proximity | Probe for GPU tenants, mention AI use cases as add-on |
| **NONE** | Traditional enterprise tenants, standard density only | Standard colo messaging (fabric-in-a-box, Equinix interconnection competition) |
