# Partner Cheat Sheet - Network Operator

**MaiaEdge for Tier 1 / Tier 2 Carriers and Network Operators**
*Use this when you're calling on national or global carriers, MPLS providers, or wholesale connectivity operators.*

---

## Know Your Customer

| Attribute | Details |
|---|---|
| **What They Own** | National or global network infrastructure. Mix of owned fiber, leased capacity, PoPs. Often with different orchestration systems across internal domains. |
| **Revenue Model** | Enterprise connectivity, MPLS services, wavelengths, IP transit, managed services. High-margin enterprise deals. |
| **Scale** | 1,000-50,000+ employees, $500M-$50B+ revenue, national or global footprint. |
| **Competitive Reality** | Internal automation may be fragmented across domains. Cross-carrier paths still manual. Enterprise customers expect AWS/Azure-like provisioning speed. Lumen signed ~$13B in PCF deals; every other board is asking "what's our PCF answer?" |
| **Why They Buy MaiaEdge** | Cross-carrier federation as the asset-light alternative to building a Lumen-scale fabric. ODA-conformant. Sits above incumbent OSS/BSS. |

---

## Problems We Solve

| Problem | How MaiaEdge Solves It |
|---|---|
| Internal automation isn't unified across all domains | Single fabric layer at every internal domain boundary |
| Cross-carrier paths still take 60-90 days, even when internal provisioning is fast | Their team activates partners in minutes. Same-day provisioning beyond their footprint |
| Enterprise customers compare them to AWS/Azure, not other carriers | Cloud-like speed for enterprise connectivity requests, under their brand |
| Visibility ends at network boundaries | End-to-end telemetry across owned and partner networks |
| East-west AI traffic destroys north-south architectures | Deterministic east-west paths between data centers. Hitless failover. Bounded path variance |
| No "PCF answer" for the board | Cross-carrier federation in weeks, not the years and billions Lumen spent |
| Footprint limits what they can sell | Extend reach to new markets through partners. Activate paths in minutes |

---

## Top Pain Points (Their Words)

> "We have automation, but it's not unified across all our domains. Beyond our footprint? Still 60-90 days."

> "Multi-domain orchestration is complex even within our own network. Different systems mean manual handoffs."

> "Enterprise customers expect AWS-like provisioning. We're still quoting weeks."

> "Our competitors are signing billion-dollar AI networking deals. What's our answer?"

> "Two-thirds of internet traffic already runs on hyperscaler-owned infrastructure."

> "PacketFabric launched natural-language provisioning. Our sales team is still doing LOAs."

---

## Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|---|---|---|
| "Is your internal automation unified across all network domains?" | "Pockets of automation, not unified." | "Fully unified, API-driven everywhere." |
| "What's your provisioning timeline for enterprise requests?" | "Still quoting weeks. Customers compare us to cloud." | "Same-day for most requests." |
| "How do you handle multi-carrier paths today?" | "Painful. LOAs, manual coordination, weeks." | "Automated NNI activation." |
| "What happens when customers need connectivity beyond your footprint?" | "We say no, or it takes months." | "Partnerships that activate quickly." |
| "What visibility do you have across internal domains?" | "Varies by domain. Beyond our network it's a black hole." | "Full end-to-end visibility everywhere." |
| "What's your AI networking answer? What does east-west capable mean for your network?" | "We're working on it / no answer yet." | "Programmable wholesale live in production across every market." |
| "Are you evaluating fabric solutions from Tier 1 carriers?" | "Yes, looking at Lumen PCF or building proprietary." | "Already built, going to market." |

---

## Objection Handling

| Objection | Rebuttal |
|---|---|
| "We have Cisco / Juniper / Ciena investments" | "PBCs complement, not replace, your core routers and incumbent PCEs. They sit at domain boundaries, internal and external, where existing automation stops. Unification layer, not rip-and-replace." |
| "Cross-carrier coordination is painful but manageable" | "Is your internal automation truly unified across all domains? Most carriers have fragmentation internally too. MaiaEdge unifies your boundaries first, then extends to partners. Same speed everywhere." |
| "We're building our own orchestration" | "For internal domains, great. But what about paths that cross carrier boundaries? MaiaEdge handles the cross-carrier layer that internal orchestration can't solve. Plugs into your OSS/BSS." |
| "This sounds expensive" | "Compare it to what's leaking. Enterprise deals lost to faster competitors. SLA penalties on paths you can't see. Engineering hours on manual provisioning. OpEx subscription, scales from 1G to 100G." |
| "Capex is tight this year" | "Capex isn't smaller, it's reallocating. Boards are moving spend from legacy MPLS transport to AI-fabric automation. MaiaEdge accelerates reallocation velocity instead of adding to capex." |
| "We're working with NVIDIA on AI Grids" | "AI Grids is your 2028 AI infrastructure (18-24 month retrofit). Your enterprise customers need deterministic paths today. MaiaEdge runs in parallel. Weeks to deploy, not years." |
| "Who are you?" | "Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper). Two exits, $2.55B+ combined. Deployed at scale by carriers including NTT." |

---

## Competitive Quick Hits

| Competitor | Quick Positioning |
|---|---|
| **Megaport / Equinix Fabric** | They own the fabric AND the customer. MaiaEdge means the operator owns both. Backend infrastructure leveraged via API. |
| **Lumen PCF** | Lumen builds their empire. MaiaEdge empowers the operator to build theirs. PCF took years and billions. Cross-carrier federation takes weeks. |
| **PacketFabric / NaaS innovators** | Their AI-native NaaS sets the bar. MaiaEdge gives the operator the platform to match it under their brand. |
| **Cisco / Juniper expansion** | Bigger core routers don't fix the customer-boundary bottleneck. PBCs sit at the edge. Complementary. |
| **Orchestration platforms (Ciena Blue Planet, Nokia NSP, Juniper Paragon)** | 6-12 month integration projects, multi-million dollar investments. MaiaEdge is fabric-in-a-box. 30-60 days to production. |
| **Status quo** | Two-thirds of internet traffic already on hyperscaler-owned infrastructure. The window to stay relevant is the 2026 planning cycle. |

---

## Persona Talk Track Matrix

| Persona | Titles | The Pitch |
|---|---|---|
| **C-Suite Strategy** (Tier 1) | CEO, CRO, Chief Product & Strategy Officer, Chief Digital Officer, Chief Transformation Officer | "Lumen signed ~$13B in PCF deals. Every Tier 1 board is asking 'what's our PCF answer?' Building a Lumen-scale fabric takes years and billions. Cross-carrier federation is the asset-light answer. MaiaEdge makes it real in weeks. The 2026 planning cycle is the window." |
| **Network Strategy** | VP Network Strategy, VP Network Architecture, VP Transport, SVP Network, VP Global Network, CTO, CNO | "Your internal automation is impressive. The moment a customer needs a path that crosses a partner carrier boundary, that automation hits someone else's timeline. MaiaEdge is the cross-operator layer that extends it. ODA-conformant, MEF-aligned, vendor-neutral." |
| **Principal / Architect** | Principal Network Architect, Distinguished Engineer, Network Architect, Chief Architect | "Think of MaiaEdge as a unification and cross-carrier extension layer. PBCs at domain boundaries (internal and external), centralized path computation, hop-by-hop telemetry across the entire path. The missing layer between your internal orchestration and the rest of the world." |
| **Wholesale / Product** | VP Wholesale, VP Product (wholesale / NaaS), Head of Wholesale Products, VP Wholesale Platforms | "Enterprise customers compare you to AWS, not to other carriers. They expect instant. MaiaEdge unifies provisioning across your entire network, then extends speed to partners. Win the deals you're currently losing to provisioning delays." |
| **Sales / Commercial** | VP Sales, VP Enterprise Sales, VP Commercial, VP Business Development | "Every 'depends on the carrier' answer is a deal at risk. Match Tier 1 speed and visibility under your brand. Same asset base, faster commercial cycle." |

---

## Proof Points

| Customer | Quote / Outcome | When to Use |
|---|---|---|
| **NTT** | Network simplification, PoP acceleration | Scale objections, Tier 1 credibility, multi-domain orchestration |
| **IENTC** (Carlos Arguimbau, CEO) | "We're going to have a MaiaEdge device in our core network so you can peer with us through them. Very simple." | Mobile backhaul (800+ towers to 20+ DCs), federation, peering |
| **Equinix** (Josh Sordelet, Principal PM) | "Revolutionary and creative. Abstracting complexity with their PBC approach." | Technical skeptics, credibility |
| **Acme Packet / 128 Technology** | $2.55B+ combined exits. SBC used by 90% of carriers. | "Who are you?" objection, founder credibility |

---

## Track A vs Track B

**Track A (Operator already has internal automation):** PCCW Console Connect, Tata IZO, Orange Wholesale MEF Sonata. Acknowledge their sophistication first. Lead with extending automation beyond their borders.

**Track B (Internal automation fragmented across regions or acquired businesses):** Lead with internal unification, then cross-carrier extension.

Always research which track applies before writing. Getting this wrong kills credibility.

---

## Geographic Positioning

**EU Tier 1s** (Orange, DT, PCCW, Tata): "Your wholesale is already programmable. MaiaEdge extends it across partner operators you don't own."

**US Tier 1s** (Verizon, AT&T, Lumen): "Proprietary silos are the slow path. Standards-aligned federation is how US operators skip the catch-up cycle."

**BEAD winners** (AT&T, Frontier, Charter, Comcast): "BEAD obligations require cross-carrier path computation in rural geographies you don't own entirely. MaiaEdge is the BEAD orchestration layer."
