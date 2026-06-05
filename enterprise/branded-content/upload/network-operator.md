# NetworkOperator CheatSheet

> Converted from: NetworkOperator_CheatSheet.pdf

> **Classification authority:** Sub-segment classification rules, anchors, and confidence thresholds live in `context/account-tiering/sub-segment-qualification.md` (pointer) and file 06 (`context/account-tiering/sub-segment-qualification-full.md`). Tier computation lives in `context/account-tiering/tier-compute-spec.md`. This cheatsheet covers selling angles, personas, pain points, and discovery.

> **Post-migration footprint (2026-05-13):** ~315 Network Operator records active post-migration. ~263 are international wholesale arms of Tier 1 parents held on the NetOp parent record via `hs_is_target_account = true` (single-record-per-DUNS policy, per file 06 §4 / D2 wholesale-arm policy). Wholesale activity within a single parent entity is captured via `network_op_track` + notes, not a separate record.

> **Tier reference:** See `context/account-tiering/tier-compute-spec.md` for tier computation. Most Network Operator sub-segments default to Tier 1 (ceiling 1, floor 2); Subsea cable operator defaults to Tier 2 (ceiling 1, floor 3).

Network Operator
Know Your Customer
Attribute Details
What They National/global network infrastructure. Mix of owned fiber, leased capacity, PoPs.
Own Often with different orchestration systems across internal domains.
Revenue Model Enterprise connectivity, MPLS services, wavelengths, IP transit, managed services.
High-margin enterprise deals.
Scale 1,000-50,000+ employees, $500M-$50B+ revenue, national or global footprint
Competitive Even internal automation may be fragmented across domains. Cross-carrier paths still
Reality manual. Enterprise customers expect AWS/Azure-like provisioning speed.
Problems We Solve
Problem How MaiaEdge Solves It
Internal automation not unified across Single fabric layer across all internal domain boundaries
domains
Cross-carrier paths take 60-90 days Instant cross-carrier activation, same-day provisioning beyond your
footprint
Can't match AWS/Azure instant Cloud-like speed for enterprise connectivity requests
provisioning
Multi-domain orchestration complexity PCE handles path computation across all domains via API
Visibility ends at network boundaries End-to-end telemetry across owned and partner networks
Footprint limited to owned infrastructure Extend reach to new markets. Activate paths to partners in minutes, not months.
PoPs and capacity generating less revenue than they could Monetize existing infrastructure. Turn PoPs into instantly sellable, deterministic services.
Top Pain Points (Their Words)
"We have automation, but it's not unified across all our domains. Beyond our footprint? Still 60-90 days."
"Multi-domain orchestration is complex, even within our own network. Different systems across domains
mean manual handoffs."
"Enterprise customers expect AWS-like provisioning. We're still quoting weeks."
Discovery Questions
Question Good Answer (Buying Signal) Red Flag
"Is your internal automation unified "We have pockets of "Fully unified, API-driven
across all network domains?" automation, but it's not unified." everywhere"
"What's your provisioning timeline for "Still quoting weeks... customers "Same-day for most
enterprise requests?" compare us to cloud" requests"
"How do you handle multi-carrier paths "Painful - LOAs, manual "Automated NNI
today?" coordination, weeks" activation"
"What happens when customers need "We either say no or it takes "We have partnerships
connectivity beyond your footprint?" months" that activate quickly"

 |  |  |  |  | 

 | Attribute |  |  | Details | 

 |  |  |  |  | 

What They
Own |  |  | National/global network infrastructure. Mix of owned fiber, leased capacity, PoPs.
Often with different orchestration systems across internal domains. |  | 

 |  |  |  |  | 

Revenue Model |  |  |  | Enterprise connectivity, MPLS services, wavelengths, IP transit, managed services. | 

 |  |  |  | High-margin enterprise deals. | 

 |  |  |  |  | 

Scale |  |  | 1,000-50,000+ employees, $500M-$50B+ revenue, national or global footprint |  | 

 |  |  |  |  | 

 | Competitive |  |  | Even internal automation may be fragmented across domains. Cross-carrier paths still | 

 | Reality |  |  | manual. Enterprise customers expect AWS/Azure-like provisioning speed. | 

 |  |  |  |  | 

 |  |  |  |  | 

 | Problem |  |  | How MaiaEdge Solves It | 

 |  |  |  |  | 

Internal automation not unified across
domains |  |  | Single fabric layer across all internal domain boundaries |  | 

 |  |  |  |  | 

Cross-carrier paths take 60-90 days |  |  |  | Instant cross-carrier activation, same-day provisioning beyond your | 

 |  |  |  | footprint | 

 |  |  |  |  | 

Can't match AWS/Azure instant
provisioning |  |  | Cloud-like speed for enterprise connectivity requests |  | 

 |  |  |  |  | 

 | Multi-domain orchestration complexity |  |  | PCE handles path computation across all domains via API | 

 |  |  |  |  | 

Visibility ends at network boundaries |  |  | End-to-end telemetry across owned and partner networks |  | 

 |  |  |  |  |  |  |  | 

 | Question |  |  | Good Answer (Buying Signal) |  |  | Red Flag | 

 |  |  |  |  |  |  |  | 

"Is your internal automation unified
across all network domains?" |  |  | "We have pockets of
automation, but it's not unified." |  |  | "Fully unified, API-driven
everywhere" |  | 

 |  |  |  |  |  |  |  | 

 | "What's your provisioning timeline for |  |  | "Still quoting weeks... customers |  |  | "Same-day for most | 

 | enterprise requests?" |  |  | compare us to cloud" |  |  | requests" | 

 |  |  |  |  |  |  |  | 

"How do you handle multi-carrier paths
today?" |  |  | "Painful - LOAs, manual
coordination, weeks" |  |  | "Automated NNI
activation" |  | 

 |  |  |  |  |  |  |  | 

 | "What happens when customers need |  |  | "We either say no or it takes |  |  | "We have partnerships | 

 | connectivity beyond your footprint?" |  |  | months" |  |  | that activate quickly" | 

 |  |  |  |  |  |  |  | 

"What visibility do you have across "Varies by domain. Beyond our "Full end-to-end visibility
internal domains?" network, it's a black hole." everywhere"
Objection Handling
Objection Rebuttal
"We have Cisco/Juniper PBCs complement, not replace, your core routers. They sit at domain
investments" boundaries, internal and external, where your existing automation stops.
We're the unification layer, not a rip-and-replace.
"Cross-carrier Is your internal automation truly unified across all domains? Most carriers
coordination is painful have fragmentation internally too. MaiaEdge unifies your internal
but manageable" boundaries first, then extends to partners. Same infrastructure, same speed
everywhere.
"We're building our own For internal domains? Great. But what about paths that cross carrier
orchestration" boundaries? MaiaEdge handles the cross-carrier layer that internal
orchestration can't solve. We plug into your OSS/BSS.
"This sounds expensive" Compare to what you're losing: enterprise deals that go to faster
competitors, SLA penalties on paths you can't see, engineering hours on
manual provisioning. OpEx subscription, starts at 1G, scales to 100G.
"Who are you?" Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology
($450M to Juniper). Deployed by carriers including NTT. Two exits, $2.5B+
combined.
Competitive Quick Hits
Competitor Quick Positioning
Megaport / Equinix They own the fabric AND the customer relationship. MaiaEdge = you own both. We
Fabric integrate with them via API when you need cloud reach.
Lumen PCF Lumen builds their empire; MaiaEdge empowers you to build yours.
SD-WAN SD-WAN = enterprise branch offices. MaiaEdge = carrier infrastructure for network
operators. Different layer, different buyer.
Proof Points & Talk Tracks
Proof Points
Customer Quote When to Use
NTT Network simplification, PoP acceleration Scale objections, Tier 1
credibility
IENTC Mobile backhaul, 800+ cell towers to 20+ data centers Mobile/wireless use cases,
scale
Equinix "Revolutionary and creative... abstracting complexity with Technical skeptics,
their PBC approach" credibility
Talk Tracks by Persona

"What visibility do you have across
internal domains?" | "Varies by domain. Beyond our
network, it's a black hole." | "Full end-to-end visibility
everywhere"

 |  |  |  |  | 

 | Objection |  |  | Rebuttal | 

 |  |  |  |  | 

"We have Cisco/Juniper
investments" |  |  | PBCs complement, not replace, your core routers. They sit at domain
boundaries, internal and external, where your existing automation stops.
We're the unification layer, not a rip-and-replace. |  | 

 |  |  |  |  | 

"Cross-carrier
coordination is painful
but manageable" |  |  |  | Is your internal automation truly unified across all domains? Most carriers | 

 |  |  |  | have fragmentation internally too. MaiaEdge unifies your internal | 

 |  |  |  | boundaries first, then extends to partners. Same infrastructure, same speed | 

 |  |  |  | everywhere. | 

 |  |  |  |  | 

"We're building our own
orchestration" |  |  | For internal domains? Great. But what about paths that cross carrier
boundaries? MaiaEdge handles the cross-carrier layer that internal
orchestration can't solve. We plug into your OSS/BSS. |  | 

 |  |  |  |  | 

"This sounds expensive" |  |  |  | Compare to what you're losing: enterprise deals that go to faster | 

 |  |  |  | competitors, SLA penalties on paths you can't see, engineering hours on | 

 |  |  |  | manual provisioning. OpEx subscription, starts at 1G, scales to 100G. | 

 |  |  |  |  | 

"Who are you?" |  |  | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology
($450M to Juniper). Deployed by carriers including NTT. Two exits, $2.5B+
combined. |  | 

"Cross-carrier

coordination is painful

but manageable"

 |  |  |  |  | 

 | Competitor |  |  | Quick Positioning | 

 |  |  |  |  | 

Megaport / Equinix
Fabric |  |  | They own the fabric AND the customer relationship. MaiaEdge = you own both. We
integrate with them via API when you need cloud reach. |  | 

 |  |  |  |  | 

 | Lumen PCF |  |  | Lumen builds their empire; MaiaEdge empowers you to build yours. | 

 |  |  |  |  | 

SD-WAN |  |  | SD-WAN = enterprise branch offices. MaiaEdge = carrier infrastructure for network
operators. Different layer, different buyer. |  | 

 |  |  |  |  |  |  |  | 

 | Customer |  |  | Quote |  |  | When to Use | 

 |  |  |  |  |  |  |  | 

NTT |  |  | Network simplification, PoP acceleration |  |  | Scale objections, Tier 1
credibility |  | 

 |  |  |  |  |  |  |  | 

IENTC |  |  | Mobile backhaul, 800+ cell towers to 20+ data centers |  |  |  | Mobile/wireless use cases, | 

 |  |  |  |  |  |  | scale | 

 |  |  |  |  |  |  |  | 

Equinix |  |  | "Revolutionary and creative... abstracting complexity with
their PBC approach" |  |  | Technical skeptics,
credibility |  | 

VP Network Strategy / Architecture
Titles: VP Network Strategy, VP Network Architecture, VP Transport, SVP Network, VP Global Network
"You have automation, but is it truly unified across all internal domains? Most carriers we talk to have
fragmentation even within their own network. MaiaEdge provides a single fabric layer at internal AND
partner boundaries. Unify your domains first, then extend reach everywhere. Same infrastructure, same
speed, same visibility."
Principal Network Architect
Titles: Principal Architect, Distinguished Engineer, Network Architect, Chief Architect
"Think of MaiaEdge as a unification and cross-carrier extension layer. PBCs at domain boundaries, both internal and
external, with centralized path computation. No routing protocols in the field, hop-by-hop telemetry
across the entire path. It's the missing layer between your internal orchestration and the rest of the
world."
VP Sales / Product
Titles: VP Sales, VP Product, VP Enterprise Sales, VP Wholesale, VP Commercial
"Enterprise customers compare you to AWS and Azure. They expect instant. How fast can you provision
paths within your network? What about paths crossing internal domain boundaries? MaiaEdge unifies
provisioning across your entire network, then extends that speed to partners. Win the deals you're
currently losing to provisioning delays."
---

## Network Op Tracks

Tracks now live in a dedicated `network_op_track` HubSpot field, NOT in `company_sub_segment`. The two legacy sub-segment values `External Extension - Network operator` and `Internal + external unification - Network Operator` were archived 2026-05-13. Use the field values below.

- **Track A = `external_extension`** (Has Internal Automation): Acknowledge their sophistication first. Lead with extending automation beyond their borders. "Your internal automation is impressive. On-net provisioning is fast and productized. But the moment a customer needs a path that crosses a carrier boundary..." Pattern of operators running this shape: PCCW Console Connect Private Label SaaS, Tata IZO DC Dynamic Connectivity, Orange Wholesale MEF Sonata APIs (all live in production).

- **Track B = `internal_external_unification`** (No Internal Automation): Lead with internal unification first. "Even within your own network, provisioning across domain boundaries is manual. MaiaEdge unifies your internal domains first, then extends to partners." Pattern of operators here: fragmented internal automation across regions / acquired businesses, often visible in job postings for "domain unification" or "OSS consolidation."

Always research which track applies before writing. Getting this wrong kills credibility instantly.

**Strategic framing (applies to both tracks):** The "why" for network operators is now reach and monetization. Track A/B determines HOW to position, but the lead angle for both tracks is: "Sell connectivity beyond your footprint. Monetize the infrastructure you already own."

---

## Network Operator Sub-Segments

Five `company_sub_segment` values sit under `customer_segment = Network Operator(Tier 1 / VNO)`. Definitions, anchors, and confidence thresholds are authoritative in file 06 §6.1 (deep-dive: `context/account-tiering/icp-deep-dives/B-and-C-network-op.md`). Below: selling-side summary of each.

### `Tier 1 Carrier - Network Op`

State-protected former incumbents and post-Bell-System nationals. Vertically integrated retail + enterprise + wholesale + (typically) international. Distinguished from Pure Wholesale by retail consumer presence; from International Backbone Specialist by dominant home-market retail; from Cable MSO by telephone/wireless legacy (not cable/HFC).

- **Quantitative markers:** consolidated parent revenue $20B+; 50+ countries of meaningful wholesale/enterprise presence; subsea cable ownership or co-ownership typical; ASN count 10-100+; 50,000+ employees; pre-1990 founding (or post-Bell-breakup US).
- **Top anchors:** AT&T, Verizon, Deutsche Telekom, NTT Group, Orange, KDDI, BT, Telstra, China Telecom (also China Mobile / China Unicom as separate records).
- **`hs_is_target_account`:** true on the parent record holds the international wholesale arm (Orange International, T-Wholesale, BT Wholesale, NTT Communications, Telstra International, etc.) unless the arm has its own separate DUNS / tax ID.
- **Selling angle:** Operational scale to negotiate with hyperscalers as equals. Position MaiaEdge as the fabric layer between their footprint and the hyperscalers their enterprise customers are buying from. Reference NTT's PCF partnership template. Track A (Orange / DT / PCCW / NTT / Tata) lead: "your team extends that automation beyond your borders without rebuilding." Track B (Verizon / AT&T / T-Mobile) lead: "your team gets where Orange and NTT already are without a 3-year build."

### `Pure Wholesale Carrier - Network Op`

Wholesale-only carriers. Sell capacity, IP transit, ports, dedicated connectivity to other carriers, hyperscalers, large enterprises. No consumer retail. Often spun from larger carriers (Arelion from Telia, EXA from GTT InfraCo, Sparkle from TIM) or built wholesale-first (Hurricane Electric, Cogent).

- **Quantitative markers:** revenue $100M-$5B; 100% B2B / B2B2x (no consumer); BGP Tier 1 or markets as Tier 1 IP transit; 30,000-300,000 route miles fiber; 200-5,000 employees; PE-owned or publicly traded.
- **Top anchors:** Cogent, Arelion (formerly Telia Carrier), EXA Infrastructure, Hurricane Electric, Sparkle (TIM), Liberty Networks. Removed per Phase B: Lumen Wholesale (no separable entity); GTT (now Managed Network Services); Zayo (now Tier 2 National Wholesale Fiber Operator post-CCF).
- **Selling angle:** Their margin is wholesale spread. Position MaiaEdge as inventory that improves their customer-facing fabric without touching their core backbone. "We give your customers a private path on top of your transit; you keep the relationship. They buy fabric experience from us through you." For Tier 1 IP transit sellers: "your wholesale customers want orchestration on top of routes they already get from you; we deliver that without you having to build it."

### `Cable MSO Enterprise Division - Network Op`

Business / enterprise / commercial fiber arm of a national cable parent. Sells fiber, Ethernet, MPLS, SD-WAN to mid-market and enterprise. Distinct from residential parent (Comcast Business, not Comcast residential).

- **Quantitative markers:** B2B revenue $1.5B+; parent residential cable in 10+ states; 5,000+ route miles fiber + HFC; distinct B2B sales org and brand. National cable + B2B ≥$1.5B is the decisive cut from Regional Cable Operator (Fiber Operator segment).
- **Top anchors:** Comcast Business ($9.7B), Spectrum Enterprise (~$7-9B; pending Charter-Cox), Cox Business (~$3-4B; pending Charter merger), Optimum Business (Altice USA).
- **Selling angle:** They're the "second carrier" to enterprise procurement. AT&T / Verizon won the first contract; Comcast Business / Spectrum Enterprise sell the diverse path. MaiaEdge gives them programmable cross-carrier reach so the diverse-path conversation extends beyond the Northeast / their cable footprint. Vertical Systems Group Leaderboard recognition is a credibility hook.

### `International Backbone Specialist - Network Op`

Carriers whose primary business is international long-haul / subsea backbone WITH significant terrestrial component. The anchor between continents. Distinct from Subsea cable operator (terrestrial-light pure-play) and from Tier 1 Carrier (no dominant home-market retail).

- **Quantitative markers:** revenue $100M-$5B; HQ outside the US; subsea ownership or IRU positions on ≥3 cable systems; 60-80% revenue from international wholesale; significant terrestrial backbone alongside subsea.
- **Top anchors:** Tata Communications, PCCW Global, Telstra International, HGC Global, Epsilon (KT-owned per Phase B correction), Console Connect (HKT-owned; Infratil deal cancelled Oct 2024), Bharti Airtel International, EXA Infrastructure, Sparkle.
- **Tiebreaker vs Subsea cable operator:** Subsea + significant terrestrial = International Backbone Specialist. Subsea-only with minimal terrestrial = Subsea cable operator.
- **Selling angle:** They already federate across continents via subsea cables and partner agreements. MaiaEdge productizes that federation programmatically so they sell "instant cross-continental private fabric" instead of "long-cycle subsea capacity." Track A is the default here; most have programmable wholesale live in production (Tata IZO, PCCW Console Connect Private Label, NTT Communications, EXA Federation).

### `Subsea cable operator` (NEW 2026-05-14)

Pure-play subsea cable operators whose primary business is owning, operating, and selling capacity on submarine fiber cables. Minimal or no terrestrial backbone. Distinct from International Backbone Specialist (significant terrestrial + subsea hybrid).

- **Quantitative markers:** revenue $20M-$500M; owns ≥1 named cable system (verifiable via TeleGeography Submarine Cable Map); landing stations as facilities; customer base = hyperscalers + content providers + regional carriers buying wet-plant capacity.
- **Top anchors:** Aqua Comms (pre-EXA acquisition; flag if record post-acquisition), Seaborn Networks, BW Digital, Hawaiki Submarine Cable, Telxius (borderline; some terrestrial). Hyperscaler subsea SPVs (Anjana, Cap-1) flag for D1 review whether they're sellable entities.
- **D1 boundary:** Pure consortia without an operating entity (FLAG, SEA-ME-WE 4/5/6, ACE) are D1.4 disqualifiers, NOT this sub-segment.
- **Default tier:** Tier 2 (ceiling 1, floor 3). Lower default than the other four NetOp sub-segments because the federation use case is thinner. Their product is wet-plant capacity, not orchestration-needing services.
- **Selling angle:** They're being squeezed by hyperscaler subsea builds and need to add fabric-on-top services to defend ARPU. MaiaEdge gives them a programmable terrestrial extension that turns landing-station capacity into instant private fabric for regional carrier customers, without them having to build a terrestrial backbone.

---

## Target Personas (title-based, no names)

Network operators skew large  -  target size ≥ 1,000 employees. Below that, the account likely fits Fiber Operator or MSP/Aggregator segmentation better.

| Tier | Revenue Band | Primary Targets | Secondary |
|------|--------------|-----------------|-----------|
| **Tier 1 Global** | Public / $10B+ | CEO (strategy-level pivots), Chief Product & Strategy Officer (automation / wholesale product direction), SVP Global Connectivity / VP Wholesale, CTO / CNO, VP Network Strategy | Principal Network Architect (technical validator), VP Wholesale Platforms |
| **Tier 1 National** | Public / $1-10B | CTO / CNO (primary technical signer), VP Network Strategy, VP Wholesale, VP Product (wholesale / NaaS product) | Chief Digital Officer / Chief Transformation Officer (platformization mandate) |
| **Tier 2 Regional Wholesale** | $500M-$1B | CTO, VP Network, Head of Wholesale Products | VP Business Development |

**Unique title to watch:** **CTrO / CDO (Chief Transformation Officer / Chief Digital Officer)** distinct from CTO/CNO. When this role is newly created or filled, the operator has a platformization mandate and a consolidated budget authority that the CTO/CNO does not. 12-18 month charter window; high signal for cross-domain automation + federation pitches.

---

## US vs. EU Geographic Positioning

The programmable-wholesale maturity gap between EU and US Tier 1s is a geographic dimension, not a sub-segment. Use it to pick the right entry angle.

**EU Tier 1s lead on programmable wholesale (live in production):**
- Orange Wholesale International  -  MEF 3.0 Sonata-compliant EVPL Online API, 29 countries, ~80 partner PoPs, real-time quote/order.
- Deutsche Telekom T Wholesale  -  CAMARA APIs (SIM Swap, Number Verification) live with Nokia Network as Code.
- PCCW Global / Console Connect  -  Private Label SaaS (ITW 2025), 60+ countries, 1,000+ DCs, 200+ cloud on-ramps.
- Tata Communications  -  IZO DC Dynamic Connectivity with deterministic multi-path routing across 44 DCs.
- **Angle for EU Tier 1s:** "Your wholesale is already programmable. MaiaEdge extends it across partner operators you don't own  -  cross-carrier federation as a product you sell to enterprise customers."

**US Tier 1s lag on public programmable wholesale:**
- Verizon / AT&T  -  no public MEF Sonata or NaaS wholesale API in current 10-Ks.
- Lumen  -  building proprietary Private Connectivity Fabric (PCF), disclosed $400-500M annualized recurring revenue target by 2028 (Q3/Q4 2025 earnings).
- AT&T  -  Express Waves launched; proprietary direction.
- **Angle for US Tier 1s:** "Proprietary silos are what your competitors are building. Standards-aligned federation is how you avoid rebuilding every carrier integration. MaiaEdge lives above whatever proprietary stack you choose  -  ODA-conformant, MEF-aligned, vendor-neutral."

**Lumen PCF anchor framing:** PCF is the revenue anchor every carrier board is now asking about. The board question "what's our PCF answer?" has three valid answers: (1) out-capex Lumen (rarely feasible), (2) build a proprietary equivalent from scratch (years), or (3) cross-carrier federation (weeks, asset-light). MaiaEdge makes #3 real.

---

## Positioning: Work With Existing Infrastructure (Not Rip-and-Replace)

MaiaEdge does **not** replace the operator's incumbent investments. This is critical for Tier 1 conversations where Cisco Crosswork, Juniper Paragon Pathfinder, Ciena Blue Planet, or Nokia NSP are the installed PCE / orchestration.

- **We keep their Cisco IP core, Juniper routers, Ciena optics, Nokia transport.** We orchestrate across domains they don't own  -  where vendor PCEs can't reach.
- **We layer above incumbent OSS / BSS.** Vendor-neutral, standards-aligned (MEF LSO, TM Forum ODA, CAMARA).
- **TM Forum ODA conformance** = zero friction on their existing RFP canvas. 38 CSP signatories, 148 vendor CTKs  -  the ODA framework is the common procurement language, and we speak it.

Use this framing when a prospect says "we have Crosswork" or "we've invested in Blue Planet" or "we don't want another vendor." We're not replacing; we're extending across where their incumbent PCE cannot reach.

---

## Capex Reallocation Framing (counter to "capex is tight")

Operator capex isn't shrinking  -  it's reallocating. Orange Q3 2025 reported 14.7% capex/sales in line with target. BT guided "over peak capex" at £4.8B. AT&T / Verizon / Lumen have disclosed AI-network reallocation on earnings. Capex that used to go to legacy MPLS transport, SDH migration, and consumer broadband is now flowing to AI-fabric automation, multi-carrier orchestration, and east-west DCI capacity.

**Reframe:** "Capex is not smaller this year. It's different. The reallocation from legacy transport to AI-fabric automation is where MaiaEdge fits  -  platform spend that accelerates reallocation velocity rather than adding to it."

Use this explicitly when a prospect objects on capex discipline or budget tightening.

---

## BEAD Winner Cross-Carrier Play (US Tier 1s + regional winners)

BEAD restructured June 2025; 53 of 56 eligible entities submitted final proposals by December 2025. Named Tier 1/Tier 2 winners (AT&T, Brightspeed, Frontier, Charter, Comcast) must deliver multi-gig fiber across fragmented rural geographies that span their existing footprints. BEAD delivery is inherently cross-carrier for any national winner  -  no single operator owns every county in their BEAD footprint.

**Angle:** "BEAD obligations require cross-carrier path computation in rural geographies you don't own entirely. MaiaEdge is the BEAD orchestration layer  -  policy-controlled paths across partner operators where your own fiber doesn't reach."

Applies only to BEAD-winner accounts. Confirm the operator has received BEAD subgrants before using this framing.

---

## Industry Landscape (2025-2026)

### The PCF Benchmark
The largest carriers are pivoting hard to AI infrastructure. The most visible example: one major carrier signed nearly $13B in private connectivity fabric deals, grew NaaS customers to 2,000+, divested consumer assets to go all-in on enterprise/AI, and is tripling its intercity fiber miles. This is the strategic template every other carrier watches  -  and the question every board is asking: "What's OUR AI networking answer?"

### Hyperscalers Bypassing Carriers
Over two-thirds of global internet traffic already traverses hyperscaler-owned network infrastructure. Hyperscaler capex exceeding $600B in 2026 (+36% over 2025), with 75% (~$450B) directly tied to AI infrastructure. Google, Meta, AWS building their own fiber backbones, subsea cables, and edge PoPs. The window for carriers to remain relevant is narrowing.

### AI Traffic Reshaping Networks
AI generates east-west traffic between data centers (GPU-to-GPU), not traditional north-south (client-server). Volatile, bursty, machine-to-machine patterns that current networks weren't built for. DCI market growing from $16.24B (2025) to $42.45B (2032). "Scaling across" strategy: hyperscalers linking multi-hundred-thousand GPU clusters across buildings/campuses within a region, treating connected facilities as one AI factory.

### Autonomous Networking Emerging
Industry moving toward "Level 4" autonomous networks  -  AI self-optimizing and self-healing. PacketFabric launched first AI-native NaaS platform with natural-language provisioning. MEF LSO APIs emerging as standardization framework. Mplify's Kylie SDK adding MCP integration for AI-native service automation. Distributed architectures replacing centralized monolithic automation.

### The "Beyond Connectivity" Opportunity
Deloitte estimates $1.7 trillion in "beyond connectivity" services by 2029. 92% of telco CEOs view NaaS as critical growth driver. Network APIs market predicted to reach $6.7B by 2028. ARPU declining/stagnating through 2029  -  operators anchored in legacy connectivity risk becoming low-margin wholesale pipes.

### Financial Reality
Legacy voice and MPLS revenue declining across the sector. Enterprise ARPU stagnating through 2029. The carriers winning are those pivoting to AI infrastructure, NaaS, and programmable connectivity  -  signing multi-billion-dollar deals while legacy-focused operators watch revenue erode.

### Sovereign Mandates Reach the Carrier Layer
Sovereign data requirements used to be a Neocloud/government topic. In 2026, they are a carrier procurement requirement. EU AI Act fully enforceable August 2026 (fines up to 7% of global revenue). India DPDP Act has extraterritorial scope with phased enforcement through May 2027. US CLOUD Act creates direct legal conflict with GDPR for any traffic transiting US carriers. 18 US state privacy laws now in force with mismatched enforcement. Carriers are being asked by regulated customers (healthcare, energy, financial services, government) to prove path sovereignty  -  not just data-at-rest compliance. BGP routing to the cheapest path is a disqualifier for these workloads. The ability to route deterministically, avoiding specific jurisdictions or carrier infrastructure, is becoming a procurement requirement, not a nice-to-have. This is the growth edge every enterprise/government sales team is now being asked to answer.

### East-West AI Traffic, Operationalized
The "AI generates east-west traffic" talking point needs to get concrete for carriers to act on it. What east-west actually means in carrier terms: non-blocking fabric topologies between data center campuses (not oversubscribed cores); sustained 99.99% path uptime with hitless failover (AI workload interruption events are millions-of-dollars expensive for the customer); bounded path variance, not just low average latency; and BGP opacity that regulated customers now treat as a procurement disqualifier. The hyperscalers are building their own non-blocking DCI because they can't buy it from carriers. The DCI market is growing from $16.24B (2025) to $42.45B (2032). The carriers that build AI-native east-west capacity now are the ones hyperscalers and regulated enterprises will actually buy from. Everyone else is selling north-south pipes into a world that runs east-west.

### Telco Retrofit Is the Slow Path
NVIDIA AI Grids initiative partners with telcos to deploy AI infrastructure inside carrier facilities. The public framing is "AI factories in your network." The reality on the ground: retrofitting telco infrastructure around compute infrastructure requires substantial change management  -  integration work running 18-24 months for most carriers, with capex running into the hundreds of millions before the first commercial workload lands. This matters as competitive positioning. When a prospect says "we're working with NVIDIA on AI Grids," the answer is not "don't do that." It's "that's your 2028 AI infrastructure. Your enterprise customers need deterministic paths now. You don't have to choose between the long build and serving the market today." Carrier-grade programmable infrastructure can deploy in weeks on top of the network you already run, while the retrofit is happening in parallel. The operators that capture the 2026 enterprise AI networking budget are not waiting for the retrofit to finish.

### Post-PCF: The Board Question is Now Urgent
Lumen's ~$13B in private connectivity fabric deals reset the benchmark. Every Tier 2 carrier board is now being asked "what's our PCF answer?"  -  and increasingly, so are Tier 1 boards that haven't made the pivot. Building a Lumen-scale fabric takes years and billions in capex. Cross-carrier partnerships are the asset-light answer: partner with other operators using a shared programmable fabric, keep the customer relationship and brand, skip the capex. The window to establish this posture before Lumen locks in more of the enterprise AI networking budget is the 2026 planning cycle. Waiting for 2027 is losing.

### What the C-Suite Is Focused On
- "What's our AI networking answer?"  -  every carrier board is asking
- Enterprise revenue growth inflection  -  when does the pivot pay off?
- NaaS/programmable networking as the growth path
- Hyperscaler relationship: partner or being bypassed?
- Cross-carrier provisioning speed vs enterprise expectations set by AWS
- Network API monetization as a new revenue category
- Cost reduction to fund the AI infrastructure pivot

---

## Their Information Diet

### What They Read
- Light Reading, Fierce Network, RCR Wireless, Telecoms.com, SDxCentral

### Analyst Firms They Trust
- Deloitte, PwC, EY (industry outlooks), Omdia, TeleGeography, IDC

### Where They Gather
- MWC Barcelona (March), PTC (January, Honolulu), ITW (May, National Harbor), Capacity events, ECOC (September)

---

## Competitive Dynamics (Their Market)

These are who NETWORK OPERATORS compete against  -  not MaiaEdge competitors.

### Hyperscaler Networks
Two-thirds of internet traffic on hyperscaler-owned infrastructure. AWS Direct Connect, Azure ExpressRoute (going 400G in 2026), Google Cloud Interconnect  -  each expansion is another path that bypasses carrier networks.

### Private Connectivity Fabric (PCF) Category
The largest carriers are creating a new competitive category with multi-billion-dollar AI networking deals. Carriers without an AI networking story are being left behind.

### SD-WAN Vendors
Dis-intermediating carriers for enterprise WAN. Fortinet, Palo Alto Prisma, Cato Networks selling direct managed offerings. Enterprise choosing SD-WAN vendors over carrier-managed WAN.

### PacketFabric / NaaS Innovators
Setting new expectations with instant, AI-native provisioning. Natural-language commands to design, price, and provision connectivity. The bar for what "fast" means just moved.

### Each Other
Consolidation continues. Smaller carriers face scale disadvantages in capital, interconnection density, and AI infrastructure investment.

---

## MaiaEdge Relevance Bridges

> **⚠️ Internal angle-selection guide.** Specific figures (Lumen ~$13B PCF, $400-500M annualized recurring target by 2028, DCI market $16.24B → $42.45B, Orange 14.7% capex/sales, $1.7T "beyond connectivity" opportunity, 38 CSP / 148 vendor ODA counts) are **internal triggers for picking which angle to lead with**. They are NOT customer-facing talking points. Do not cite these figures in cold outreach or LinkedIn. Use them to determine which relevance bridge fits the account, then write in segment vocabulary.

How current industry trends connect to problems MaiaEdge solves. Use across the full sales motion.

| Their Trend | Their Pain | MaiaEdge Angle |
|---|---|---|
| Competitors signing $B+ AI networking deals | Others have an AI networking story; they don't. Losing enterprise deals to speed narratives | "The top carriers built private connectivity fabrics. You need YOUR version  -  your brand, your customers, your margin. MaiaEdge is how." |
| Hyperscalers own 2/3 of internet traffic | Traffic increasingly bypasses carrier networks entirely  -  existential relevance risk | "Hyperscalers are building around you. Cross-carrier automation lets you stay in the path." |
| AI east-west traffic patterns | Networks architected for north-south can't serve GPU cluster interconnect demands | "AI traffic doesn't follow your network's design. Deterministic east-west paths are the new requirement." |
| Enterprise expects AWS-like provisioning | 60-90 day cross-carrier provisioning vs instant cloud  -  losing enterprise credibility | "Your enterprise customers compare you to AWS, not to other carriers. MaiaEdge closes that gap." |
| $1.7T "beyond connectivity" opportunity | NaaS is the growth path but requires automation they don't have | "The beyond-connectivity opportunity requires programmable infrastructure. MaiaEdge delivers it in weeks, not years." |
| Level 4 autonomous networking emerging | PacketFabric offering natural-language provisioning  -  raising the bar | "The bar just moved. Autonomous provisioning isn't a 2030 thing anymore." |
| EU AI Act Aug 2026 + 18 US state privacy laws + DPDP Act | Regulated customers (healthcare, energy, financial services, government) demanding provable path sovereignty  -  BGP is now a disqualifier | "Your regulated customers are inheriting sovereignty requirements. BGP routes to cheapest path, ignoring jurisdictions. MaiaEdge enforces policy-driven paths with jurisdictional audit trails. That's the answer they're looking for." |
| AI east-west traffic + $16B to $42B DCI market | Networks architected north-south oversubscribe on east-west. Hitless failover and bounded path variance are the new bar. | "Hyperscalers are building their own non-blocking DCI because they can't buy it. Your team builds the AI-native east-west carriers will sell, and we give you the control plane to do it." |
| Lumen ~$13B PCF benchmark | Every board is asking "what's our PCF answer?" Building from scratch takes years you don't have | "PCF took Lumen years and billions. Cross-carrier activation takes weeks. You don't need to out-capex Lumen. You need to out-partner them." |
| NVIDIA AI Grids retrofit path | 18-24 month retrofit timeline lets competitors capture the enterprise AI networking budget NOW | "AI Grids is your 2028 AI infrastructure. Your enterprise customers need deterministic paths today. You don't have to pick between the long build and the market that's moving right now." |
| BEAD winners required to deliver multi-gig across rural geographies they don't own entirely | No single operator owns every county in their BEAD footprint  -  cross-carrier orchestration is inherent to delivery | "BEAD obligations need cross-carrier path computation where your fiber doesn't reach. MaiaEdge is the orchestration layer  -  policy-controlled paths across partner operators." |
| Capex reallocating from legacy transport to AI-fabric automation | Boards are reading tight capex guidance; the reallocation signal is already public but the path to execute it isn't | "Your capex isn't smaller this year. It's different. MaiaEdge accelerates reallocation velocity instead of adding to it." |
| TM Forum ODA adoption (38 CSPs, 148 vendor CTKs) | Procurement language is converging on ODA; non-conformant products create RFP friction | "We're ODA-conformant. Zero friction on your existing RFP canvas. Standards-aligned isn't a checkbox  -  it's how you avoid rebuilding every vendor integration." |
| Programmable wholesale gap: EU Tier 1s live, US Tier 1s building proprietary silos | US operators face a 3-5 year catch-up vs. Orange / DT / PCCW / Tata programmable-wholesale products already in production | "Proprietary silos are the slow path. Standards-aligned federation is how US operators skip the catch-up cycle and land AI / enterprise budgets this planning cycle." |

---

## Insider Language Bank

Things network operator executives say internally  -  use these to demonstrate you understand their world.

### Board Meeting Language
- "Our competitors are signing billion-dollar AI networking deals. What's our answer?"
- "Two-thirds of internet traffic already runs on hyperscaler-owned infrastructure"
- "Our enterprise customers don't compare us to other carriers anymore  -  they compare us to AWS"
- "We've automated on-net, but beyond our footprint it's still 60-90 days of spreadsheets and emails"
- "The beyond-connectivity opportunity is $1.7 trillion by 2029. We need programmable infrastructure."
- "East-west AI traffic doesn't follow the north-south patterns our network was built for"
- "PacketFabric launched natural-language provisioning. Our sales team is still doing LOAs."
- "Our regulated customers want to prove where packets traveled  -  BGP can't answer that question"
- "What's our PCF answer? We can't wait for the 2027 planning cycle to decide"
- "Hyperscalers are building non-blocking DCI because they can't buy it from us  -  what does that tell you?"
- "AI Grids is an 18-24 month retrofit. We don't have that runway before the enterprise AI networking budget gets spent."

### KPIs They Report
enterprise revenue growth %, NaaS customer count, PCF deal backlog, intercity fiber miles, PoP count, on-net buildings, EBITDA margin, FCF, net leverage, capex intensity ratio, churn rate, ARPU, cost reduction run rate

### Business Terms to Know
PCF, east-west traffic, scaling across, DCI, coherent optics, photonic switching, Level 4 autonomous network, agentic network operations, LSO APIs, NaaS, TelcOS, beyond-connectivity revenue, network API monetization, programmable transport, intent-based networking, SRv6, disaggregation

---

## Segment Vocabulary Lock

### MUST-Use Terms (Network Operator)
multi-domain, on-net/off-net, configuration drift, LOA, BGP, PoPs, orchestration, domain boundaries, cross-carrier reach extension, enterprise deals, MPLS, wavelengths, carrier boundary, path computation, extend reach, sell beyond your footprint, monetize existing infrastructure, new markets

### BANNED Terms (From Other Segments)
tenant, attach rate, meet-me room, cross-connect (colo context), dark fiber (fiber context), upstream carrier, finger-pointing (MSP context), single pane of glass, asset-light, inference, jitter, GPU, middle mile, training run, recompute tax, egress (neocloud context)

### Cold Outreach Rules
- Credibility anchors ("Same team that built Acme Packet" / "128 Technology" / Andy Ory etc.) are BANNED in cold emails and LinkedIn. The message does the talking in outreach. Allowed in live presentations, demos, proposals, and objection handling  -  the track record does the talking in rooms.
- NO sign-offs in emails. Signatures are auto-appended by the email platform.
- For Track A: MUST acknowledge their internal automation before positioning MaiaEdge. Skipping this feels tone-deaf.
- For Track B: Lead with internal unification, then cross-carrier extension.
- Pair speed with ownership: "Your team extends that automation beyond your borders" not just "faster provisioning."
- Lead with reach and monetization. "Sell connectivity beyond your footprint" and "monetize existing infrastructure" are the primary strategic angles. Track A/B determines the tactical approach.

---

*Cross-references: Messaging Framework V4, ICP Sales Playbook (Complete Reference), Cloud On-Ramp Business Case, Competitive Positioning Guide, Terminology Glossary*
*Updated: April 2026 (trend refresh: sovereign mandates at the carrier layer, east-west AI traffic operationalized, post-PCF urgency, cross-carrier partnerships as asset-light answer, telco retrofit as slow path)*
