# FiberOperator CheatSheet

> Converted from: FiberOperator_CheatSheet.pdf

> **Classification authority:** Sub-segment classification rules, anchors, and confidence thresholds live in `context/account-tiering/sub-segment-qualification.md` (pointer) and file 06 (`context/account-tiering/sub-segment-qualification-full.md`). Tier computation lives in `context/account-tiering/tier-compute-spec.md`. This cheatsheet covers selling angles, personas, pain points, and discovery.
>
> **Post-migration note (2026-05-13):** ~1,376 Fiber records in HubSpot post-migration (+327 from NetOp demotion). ~1,008 currently sit on the `Regional CLEC - Fiber operator` catch-all default; R2 + D7 will refine over time. The 6 active sub-segment values are verified live as of 2026-05-14.

Fiber Operator
Know Your Customer
Attribute Details
What They Physical fiber infrastructure, optical transport. Measure network in "route miles."
Own Often fragmented across disconnected fiber islands with different systems at each
location.
Revenue Dark fiber (IRUs), lit wavelengths, metro Ethernet, wholesale. 30-70% capacity
Model underutilized
Scale 50-2,000 employees, $50M-$1B revenue, regional focus (2-10 state footprint)
Competitive Internal provisioning across fiber islands is still manual. NNIs take 60-90 days. Type 2
Reality circuits are visibility black holes.
Problems We Solve
Problem How MaiaEdge Solves It
Internal fragmentation across fiber Unify disconnected fiber segments into one automated
islands fabric
60-90 day NNI provisioning Instant partner activation, no LOAs or BGP config
Type 2 visibility black holes Hop-by-hop telemetry across circuits you don't own
30-70% stranded fiber capacity Turn dark fiber into instantly sellable, deterministic services
Losing multi-state deals to speed Provision in minutes, win deals you're currently losing
Limited footprint losing multi-state deals Extend reach to new markets instantly without building there
Fiber or DIA, different provisioning workflows Deterministic paths over fiber or DIA, same quality, same speed
Top Pain Points (Their Words)
"NNIs take 60-90 days - LOAs, VLAN coordination, BGP config. We've lost deals because of it"
"Once traffic leaves our network onto Type 2, we're blind - can't troubleshoot, can't prove SLAs"
"We have 30-40% dark fiber sitting idle while we're under pressure to grow revenue"
"Provisioning across our own fiber segments still takes weeks - different systems, manual configuration
at each site"
Discovery Questions
Question Good Answer (Buying Signal) Red Flag
"What percentage of your fiber is "30-50%... we have stranded "85%+ utilized"
generating revenue?" capacity"
"When you extend reach through NNIs, "60-90 day process... we've "Automated NNI
what does that look like?" turned down deals" establishment"
"How do you handle Type 2 circuits? What "It's a black hole - responsible "Full visibility through
visibility?" but can't see" our OSS"
"How many multi-state deals lost to "Multiple - customers go with "We win most multi-
provisioning delays?" whoever's faster" state deals"

 |  |  |  |  | 

 | Attribute |  |  | Details | 

 |  |  |  |  | 

What They
Own |  |  | Physical fiber infrastructure, optical transport. Measure network in "route miles."
Often fragmented across disconnected fiber islands with different systems at each
location. |  | 

 |  |  |  |  | 

 | Revenue |  |  | Dark fiber (IRUs), lit wavelengths, metro Ethernet, wholesale. 30-70% capacity | 

 | Model |  |  | underutilized | 

 |  |  |  |  | 

Scale |  |  | 50-2,000 employees, $50M-$1B revenue, regional focus (2-10 state footprint) |  | 

 |  |  |  |  | 

 | Competitive |  |  | Internal provisioning across fiber islands is still manual. NNIs take 60-90 days. Type 2 | 

 | Reality |  |  | circuits are visibility black holes. | 

 |  |  |  |  | 

 |  |  |  |  | 

 | Problem |  |  | How MaiaEdge Solves It | 

 |  |  |  |  | 

Internal fragmentation across fiber
islands |  |  | Unify disconnected fiber segments into one automated
fabric |  | 

 |  |  |  |  | 

 | 60-90 day NNI provisioning |  |  | Instant partner activation, no LOAs or BGP config | 

 |  |  |  |  | 

Type 2 visibility black holes |  |  | Hop-by-hop telemetry across circuits you don't own |  | 

 |  |  |  |  | 

 | 30-70% stranded fiber capacity |  |  | Turn dark fiber into instantly sellable, deterministic services | 

 |  |  |  |  | 

Losing multi-state deals to speed |  |  | Provision in minutes, win deals you're currently losing |  | 

 |  |  |  |  |  |  |  | 

 | Question |  |  | Good Answer (Buying Signal) |  |  | Red Flag | 

 |  |  |  |  |  |  |  | 

"What percentage of your fiber is
generating revenue?" |  |  | "30-50%... we have stranded
capacity" |  |  | "85%+ utilized" |  | 

 |  |  |  |  |  |  |  | 

 | "When you extend reach through NNIs, |  |  | "60-90 day process... we've |  |  | "Automated NNI | 

 | what does that look like?" |  |  | turned down deals" |  |  | establishment" | 

 |  |  |  |  |  |  |  | 

"How do you handle Type 2 circuits? What
visibility?" |  |  | "It's a black hole - responsible
but can't see" |  |  | "Full visibility through
our OSS" |  | 

 |  |  |  |  |  |  |  | 

 | "How many multi-state deals lost to |  |  | "Multiple - customers go with |  |  | "We win most multi- | 

 | provisioning delays?" |  |  | whoever's faster" |  |  | state deals" | 

 |  |  |  |  |  |  |  | 

"What does NNI establishment look like "LOAs, VLAN coordination, "API-driven, days not
today?" BGP... weeks" weeks"
"How do you provision new paths within "Still manual - different systems "Fully automated end-
your own network?" at each site" to-end"
Objection Handling
Objection Rebuttal
"Our NNI process Works externally, but what about internally? Most operators have the same
works; it just takes friction provisioning across their own fiber islands. MaiaEdge unifies your network
time" first, then extends that automation to partners. Every 60-90 day delay, internal or
external, is a deal at risk.
"What about Type 2 is a visibility black hole. You're responsible for the SLA but can't see the
visibility into Type path. PBCs at each boundary give you hop-by-hop telemetry across circuits you
2 circuits?" don't own.
"This sounds The opposite. No routing protocols, no BGP sessions, no MPLS label distribution.
complex" That complexity is exactly what we eliminate.
"We want to build Most teams estimate 18-24 months and several million dollars. We've already
our own" done that work. Same team that built Acme Packet and 128 Technology. Why
rebuild what exists?
"Who are you?" Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M
to Juniper). SBC used by 90% of carriers. Two exits, $2.5B+ combined.
"We've automated Have you? Or do you have fiber islands with separate systems at each location?
our internal The pattern I'm watching with operators in growth mode is internal fragmentation
network" before they even get to cross-carrier complexity. MaiaEdge unifies both.
Competitive Quick Hits
Competitor Quick Positioning
Megaport / Equinix They own the fabric AND your customer. MaiaEdge = you own both. We integrate
Fabric with them via API for cloud reach.
Lumen PCF Lumen builds their empire; MaiaEdge empowers you to build yours.
SD-WAN SD-WAN = enterprise branch offices. MaiaEdge = carrier infrastructure for fiber
operators. Different layer.
Proof Points & Talk Tracks
Proof Points
Customer Quote When to Use
Arvig "Almost instantaneous" provisioning Speed objections,
automation
Arvig "MaiaEdge allows us to utilize unutilized fiber and provide Stranded fiber,
services rapidly" monetization

"What does NNI establishment look like
today?" |  |  | "LOAs, VLAN coordination,
BGP... weeks" |  |  | "API-driven, days not
weeks" |  | 

 |  |  |  |  |  |  |  | 

 | "How do you provision new paths within |  |  | "Still manual - different systems |  |  | "Fully automated end- | 

 | your own network?" |  |  | at each site" |  |  | to-end" | 

 |  |  |  |  |  |  |  | 

 |  |  |  |  | 

 | Objection |  |  | Rebuttal | 

 |  |  |  |  | 

"Our NNI process
works; it just takes
time" |  |  | Works externally, but what about internally? Most operators have the same
friction provisioning across their own fiber islands. MaiaEdge unifies your network
first, then extends that automation to partners. Every 60-90 day delay, internal or
external, is a deal at risk. |  | 

 |  |  |  |  | 

 | "What about |  |  | Type 2 is a visibility black hole. You're responsible for the SLA but can't see the | 

 | visibility into Type |  |  | path. PBCs at each boundary give you hop-by-hop telemetry across circuits you | 

 | 2 circuits?" |  |  | don't own. | 

 |  |  |  |  | 

"This sounds
complex" |  |  | The opposite. No routing protocols, no BGP sessions, no MPLS label distribution.
That complexity is exactly what we eliminate. |  | 

 |  |  |  |  | 

"We want to build
our own" |  |  |  | Most teams estimate 18-24 months and several million dollars. We've already | 

 |  |  |  | done that work. Same team that built Acme Packet and 128 Technology. Why | 

 |  |  |  | rebuild what exists? | 

 |  |  |  |  | 

"Who are you?" |  |  | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M
to Juniper). SBC used by 90% of carriers. Two exits, $2.5B+ combined. |  | 

 |  |  |  |  | 

 | "We've automated |  |  | Have you? Or do you have fiber islands with separate systems at each location? | 

 | our internal |  |  | The pattern I'm watching with operators in growth mode is internal fragmentation before | 

 | network" |  |  | they even get to cross-carrier complexity. MaiaEdge unifies both. | 

 |  |  |  |  | 

"We want to build

our own"

 |  |  |  |  | 

 | Competitor |  |  | Quick Positioning | 

 |  |  |  |  | 

Megaport / Equinix
Fabric |  |  | They own the fabric AND your customer. MaiaEdge = you own both. We integrate
with them via API for cloud reach. |  | 

 |  |  |  |  | 

 | Lumen PCF |  |  | Lumen builds their empire; MaiaEdge empowers you to build yours. | 

 |  |  |  |  | 

SD-WAN |  |  | SD-WAN = enterprise branch offices. MaiaEdge = carrier infrastructure for fiber
operators. Different layer. |  | 

 |  |  |  |  |  |  |  | 

 | Customer |  |  | Quote |  |  | When to Use | 

 |  |  |  |  |  |  |  | 

Arvig |  |  | "Almost instantaneous" provisioning |  |  | Speed objections,
automation |  | 

 |  |  |  |  |  |  |  | 

Arvig |  |  |  | "MaiaEdge allows us to utilize unutilized fiber and provide |  |  | Stranded fiber, | 

 |  |  |  | services rapidly" |  |  | monetization | 

 |  |  |  |  |  |  |  | 

Ocean Cross-carrier connectivity to INDATEL for mainland reach Geographic isolation,
Networks partners
Ecotel "Great for the fragmented fibre market" Fragmented markets, intl
(Germany)
Talk Tracks by Persona
VP Network / VP Operations
Titles: VP Network, VP Network Operations, VP Transport, VP Service Delivery, VP Network Engineering
"You've invested in fiber, but it's likely fragmented. Different systems at each location, manual
provisioning across your own network before you even get to partners. MaiaEdge unifies your fiber
islands into one automated fabric first. Then extends that automation to partners. PBCs at internal
boundaries and external handoffs. Partner activation in days, not months."
VP Sales / Business Development
Titles: VP Sales, VP Business Development, VP Commercial, VP Wholesale, VP Enterprise Sales
"What if you could provision across your own network in minutes, not weeks? And then say yes to every
multi-state RFP with the same speed? MaiaEdge automates your network first, then extends your reach
through cross-carrier connectivity. Customers go with whoever's faster. Now that's you, everywhere."
Director of Engineering / Sr. Network Engineer
Titles: Director of Engineering, Sr. Network Engineer, Transport Engineer, DWDM Engineer, Lead Network Engineer
"Provisioning across your own fiber segments probably looks a lot like your NNI process. Manual config
at each site, weeks to stand up new paths. MaiaEdge unifies your network first: PBCs at each internal
boundary, automated provisioning, end-to-end visibility. Then the same infrastructure extends to
partners. No routing protocols, hop-by-hop telemetry across the entire path."

Ocean
Networks |  |  | Cross-carrier connectivity to INDATEL for mainland reach | Geographic isolation,
partners

 |  |  |  | 

 | Ecotel |  | "Great for the fragmented fibre market" | Fragmented markets, intl

 | (Germany) |  |  | 

 |  |  |  | 
---

## Messaging Hierarchy (Updated)

1. **Monetize underutilized fiber** (lead): Turn idle lit, stranded laterals, and dark fiber into instantly sellable, deterministic services. Not just IRUs sitting idle  -  revenue-generating paths activated in minutes.
2. **Instant private fabric across your network** (default): Provision private connectivity across any transport  -  fiber, wave, DIA, 5G/fixed wireless, satellite  -  in minutes. No routing complexity: no VLAN stitching, no BGP, no MPLS, no SRv6.
3. **Extend reach beyond your footprint** (cross-carrier angle): Win multi-state deals without building there. PBC at a partner site, deterministic paths across partner networks the same way they extend across your own.
4. **Sell new services you couldn't before** (growth angle): Cloud on-ramp is the flagship  -  enable it if you don't offer it today, make it faster and higher-margin if you do. Same platform also productizes cross-connects, partner interconnects, and private paths.
5. **Visibility, automation, and SLA enforcement across Type 2** (use when research shows cross-carrier pain)

---

## Fiber Sub-Segments (match HubSpot `company_sub_segment` values)

Six active sub-segments drive buying motion, target titles, and messaging angle (verified live 2026-05-14). Use HubSpot values exactly. **Account Tier defaults vary by sub-segment**  -  see `context/account-tiering/tier-compute-spec.md` for tier computation. Default tiers: Tier 2 National Wholesale / Long Haul / Dark Fiber default Tier 2 (ceiling 1, floor 3); Regional CLEC / Regional Cable Operator default Tier 3 (ceiling 1, floor 4); Municipal / Cooperative default Tier 4 (ceiling 2, floor 5).

### Regional CLEC (`Regional CLEC - Fiber operator`)  -  catch-all default, ~1,008 records

**Who:** Multi-state competitive local exchange carriers and PE-backed regional fiber platforms whose primary business is selling fiber connectivity (lit Ethernet, wavelengths, dark fiber, DIA) directly to enterprises, mid-market, government, and education in their footprint. Built either via CLEC certification post-1996 Telecom Act or as fiber-overbuilders without ILEC heritage. The canonical "fiber-island unification" archetype  -  most have grown by acquiring smaller regional networks and operate disconnected fiber segments with different OSS/BSS at each site. Default sub-segment for ambiguous mid-size; framework catch-all.

**Quantitative markers:** Revenue $50M-$700M (PE roll-ups exceed $1B); 2,000-30,000 route miles; 3-12 states; 200-2,000 employees; 3,500-15,000 on-net buildings; direct-enterprise revenue share >40%.

**Anchors:** Consolidated Communications (upper edge  -  Searchlight take-private 2024, 23 states, ~58,000 route miles), Lumos, Bluebird Fiber (post-Everstream March 2026, 36,000+ route miles, 12 states, Kansas-Ohio-Canadian border), FirstLight (Antin, Northeast, ~25,000 route miles), Lit Communities, Ritter Communications (AR/TN/MO/TX, ~10,000 route miles), Hargray, Segra (Cox-acquired 2023, 47,000+ route miles, 17 states), MetroNet (Oak Hill/KKR FTTH overbuilder), Hotwire Communications (FL+11 states), Allo Communications (Nelnet), Ziply Fiber (BCE-owned post-2025), Arvig (MN, family-owned, MaiaEdge customer). **Stale anchors flagged:** Crown Castle Fiber (defunct April 2026, absorbed by Zayo, DO NOT use); GTT (legacy  -  moved to Managed Network Services - MSP, not Fiber).

**Target titles (by size):**
- **Sub-$500M revenue:** CTO / Chief Network Officer (technical champion, veto authority), COO (operational approver, owns service delivery + NNI process), CRO / VP Wholesale / VP Sales (monetization sponsor, cares about deal velocity), VP Network Operations / VP Transport / VP Service Delivery.
- **$500M+ or PE-backed:** Add CFO for >$1M OpEx approvals. PE sponsor's infrastructure investment director signs off on software-platform spend. Chief Product Officer / VP Product if NaaS/portal program exists.
- **Engineering tier:** Director of Engineering, Sr. Network Engineer, Transport Engineer, DWDM Engineer, Principal Architect.

Strongest pattern: VP Network + VP Wholesale + CRO as three-person buying committee.

**Lead angle:** "Your network is acquisitions stitched together. Each fiber island built differently, with different OSS at each site. MaiaEdge turns each of them into one asset class you can sell from  -  standardized services across every strand mile you own, then extends that automation to partner networks beyond your footprint. Monetize underutilized fiber, unify your network, and win the multi-state deals that go to whoever provisions fastest." Pair speed with ownership: "your team provisions in minutes."

### Tier 2 National Wholesale (`Tier 2 National Wholesale - Fiber operator`)  -  NEW, highest priority

**Who:** National or near-national wholesale-primary fiber operators selling dark fiber, lit transport, wavelengths, and IRUs to other carriers, hyperscalers, large enterprises, and ISPs. Smaller than Tier 1 Carriers (no retail consumer; no large-scale direct enterprise) but bigger and broader than Regional CLECs. The "metro + long-haul wholesale fabric" archetype. National US or pan-EU footprint, 80%+ revenue from wholesale, often PE-owned or recently consolidated.

**Quantitative markers:** Revenue $300M-$5B+; 20,000-300,000 route miles; national US (30+ states) or pan-EU; 1,000-5,000+ employees; PE / infrastructure fund-backed (DigitalBridge, EQT, I Squared, Stonepeak); wholesale revenue share >80%.

**Anchors:** Zayo Group (DigitalBridge, 224,000 route miles post-Crown Castle Fiber close April 2026, ~$2.5B+ combined revenue, canonical anchor), Lightpath ($468M FY2025 revenue + $362M AI contracts, 10,000+ route miles, Altice 50.01% + Morgan Stanley 49.99% JV), Uniti+Windstream merged (post-Aug 2025 close, 240,000 route miles, 300+ metros, 47 states, ~$5B annualized  -  largest pure-play fiber by route miles in US post-merger), EXA Infrastructure (I Squared, 174,500 km / 37 countries, 65,000 km 400G-enabled, €1.3B refinancing Oct 2025  -  boundary with Long Haul / International Backbone).

**Target titles:** Chief Product & Strategy Officer / Chief Commercial Officer, VP Wholesale / VP Carrier Relations / VP Network Automation, CTO / Chief Network Officer, VP Network Engineering / Principal Architect, CEO for strategy-level decisions on platform partnerships, PE sponsor's infrastructure investment director / operating partner.

Strongest pattern: CPO + VP Wholesale + CTO as buying committee.

**Lead angle:** "You're squeezed between Tier 1 carriers above and Regional CLECs below. You differentiate on relationships, route choice, and pricing flexibility  -  but your customers want orchestration, not just transport. MaiaEdge is the orchestration layer they expect from AWS Direct Connect, layered above your existing fabric. Your customers see a private, deterministic cloud on-ramp; you keep the customer, the margin, and the route." Pair with monetization velocity: "Every dark mile of fiber you own becomes a sellable, deterministic service in minutes  -  not 60-90 day NNI processes that lose deals."

### Long Haul / Backbone (`Long Haul / Backbone - Fiber operator`)  -  displacement-resistant federation

**Who:** National or multi-national fiber operators whose primary business is long-haul / inter-city backbone connectivity, typically 50,000+ route miles spanning major metros. Sell dark fiber, wavelengths (100G/400G/800G), and IP transit to carriers, hyperscalers, content providers, and large enterprises. Run sophisticated incumbent automation (Zayo DynamicLink, Lumen RapidRoutes) that already provides provisioning at scale. MaiaEdge does NOT replace these; it federates above them, extending automation across operator boundaries.

**Quantitative markers:** Revenue $500M-$15B+; 50,000-340,000+ route miles (Lumen at the high end); national US (40+ states) or pan-EU or pan-APAC; 1,500-30,000+ employees; primarily long-haul corridor + cross-metro.

**Anchors:** Lumen Technologies (NYSE:LUMN, 340,000 route miles, 47M intercity fiber miles planned by 2028  -  boundary with Tier 1 Carrier Network Op for the parent record), Cogent Communications (NASDAQ:CCOI, 20,200 miles dark fiber from Sprint assets + 19,000 inter-city wavelength network  -  boundary with Pure Wholesale Carrier Network Op), Zayo (post-CCF expansion, but classified Tier 2 National Wholesale per file 05 canonical resolution), FiberLight (Morrison & Co consortium, 11,000+ miles TX/Atlanta/VA Beach-Richmond corridor), Arelion / formerly Telia Carrier (Polhem Infra, pan-European long-haul + transatlantic). **Stale anchors flagged:** Crown Castle Fiber (defunct April 2026  -  Zayo acquired); GTT (now Managed Network Services - MSP after I Squared 2021 sale + Chapter 11 2022; no longer Long Haul).

**Buying motion:** MaiaEdge does NOT replace the incumbent automation (DynamicLink, RapidRoutes, Cisco Crosswork, Juniper Paragon Pathfinder, Ciena Blue Planet, Nokia NSP). It layers cross-carrier federation above it. Position as "extends what you already have beyond your borders" rather than "replaces what you built." Critical framing: displacement-resistant.

**Target titles (Public / $500M+):** Chief Product & Strategy Officer (owns automation-platform strategy), VP Network Engineering, Principal Architect, CEO for strategy-level shifts, VP Wholesale / VP Carrier Relations, Chief Network Officer / CTO. Engineering tier: Director of Network Architecture, Director of Optical Engineering, DWDM Engineer. Target size ≥1,000 employees.

**Lead angle:** "Your customers want your NNIs automated. They already are. The next question is whether your customers can reach cities you don't own. MaiaEdge is the cross-operator layer that extends your reach without you laying another strand  -  federation on top of your existing automation, not a replacement for it. Your customers see one fabric; you keep the customer, the margin, and the control."

### Dark Fiber Specialist (`Dark Fiber Specialist - Fiber Operator`)  -  capital "O", monetization-velocity

**Who:** Operators whose primary product line is dark fiber sales (IRUs) and wavelength services rather than lit Ethernet or DIA. Typically metro or regional in geographic scope with strand-rich routes that monetize through 20-year IRU contracts and shorter-term wavelength leases. Smaller in revenue than Long Haul / Backbone operators but with disproportionate strategic value because dark fiber is the lever for AI data center interconnect (36x more fiber per route than CPU racks) and hyperscaler buildouts. M&A multiples reflect 25-30x EV/EBITDA on AI-adjacent assets. **Note: HubSpot internal value uses capital "O" in "Operator"  -  the only Fiber sub-segment that breaks lowercase convention.**

**Quantitative markers:** Revenue $20M-$500M; 5,000-30,000 route miles; 1-10 metros OR single regional corridor; 50-500 employees; >50% revenue from IRU contracts + wavelength leases; 80%+ revenue from dark fiber IRUs in the strictest classification; higher strand-density-per-route than long-haul peers (144-432 strand counts on AI-corridor builds vs. 8-12 historically).

**Anchors:** FiberLight (Morrison & Co / Australian Retirement Trust / UBS, 11,000+ miles TX + Atlanta + 200-mile Virginia Beach-Richmond dark fiber corridor with Metro Fiber Networks acquisition April 2025 closed June 2025), Stealth Communications, Allied Fiber, ITS Fiber, Conterra Networks (Southeast US, <$100M est.), Wilcon / Pacific Lightwave (CA), INDATEL (700+ rural ILEC/CLEC consortium  -  hybrid with Municipal/Cooperative), Ocean Networks (HI/Pacific, MaiaEdge customer for INDATEL cross-carrier reach), Summit IG (Dallas metro).

**Target titles:** Wholesale / Business Development leadership (Head of Dark Fiber, VP Capacity, VP Wholesale), CRO / Chief Commercial Officer, CTO / Chief Network Officer, Director of Optical Engineering / DWDM Engineer (technical due diligence). For PE-backed: CEO + PE sponsor's infrastructure investment director.

Strongest pattern: VP Wholesale + Head of Dark Fiber + CTO.

**Lead angle:** "Dark strands depreciate every day they're unlit. MaiaEdge lights them as sellable, deterministic services on demand  -  without committing the strand to a single IRU customer. Productize wavelength-on-demand for hyperscaler AI interconnect, monetize unlit capacity in minutes, and turn every dark mile in your inventory into a sellable path." Pair with the AI DC fiber ratio framing: "AI data centers need 36x more fiber per rack  -  your team's dark strands are the inventory hyperscalers are bidding for."

### Regional Cable Operator (`Regional Cable Operator - Fiber operator`)  -  NEW

**Who:** Regional cable companies (smaller than national MSOs like Comcast, Charter, Cox) with growing commercial fiber arms. Parent is regional cable; the buying angle MaiaEdge sells to is the commercial / business fiber division. Parent's B2B scale puts them under $1.5B in commercial revenue (above that → Cable MSO Enterprise Division - Network Op). Mostly residential HFC plant with selective FTTH overbuild + commercial fiber expansion to chase enterprise revenue. The commercial fiber book is the growth engine because residential ARPU is plateauing under FWA + fiber overbuilder pressure.

**Quantitative markers:** Parent B2B revenue $30M-$1.5B; total parent revenue $200M-$3B; 3-22 states (regional or multi-state but NOT national); 500-5,000 employees; 100K-2M broadband subscribers; mixed HFC + fiber.

**Anchors:** Breezeline / Cogeco US (13 US states CT/DE/FL/ME/MD/MA/NH/NY/OH/PA/SC/VA/WV, Q3 2025 revenue $1.448B, 622,000+ broadband customers, 1.8M passings, ~28K new FTTP passings/quarter, 8th largest US cable operator), WideOpenWest / WOW! (NYSE:WOW, 2024 revenue $629M  -  borderline scale post-divestiture to Astound), Mediacom Business (22 states, 1.44M broadband subs, family-owned by Rocco Commisso), Midco Business (MN/SD/ND/KS/WI, ~13% of customers fiber-eligible), Service Electric (PA regional cable + fiber, independent), GCI (Alaska  -  Liberty Broadband owned, geographically isolated special case), Cable ONE / Sparklight (NYSE:CABO, ~$1.7B revenue  -  boundary case with Cable MSO Network Op), Astound Broadband (Stonepeak  -  pending merger with Alphabet's GFiber announced March 11, 2026, close Q4 2026; pre-close `manual_review_required`, post-close moves to Cable MSO Enterprise Division Network Op).

**Target titles:** VP Business / VP Commercial Services / President of Business Services (the commercial fiber arm leadership  -  distinct from residential), Chief Commercial Officer, VP Network Operations / VP Engineering, CTO (parent  -  sometimes shared between residential + business), Director of Wholesale / VP Carrier Relations (if commercial fiber wholesale book exists).

Strongest pattern: VP Business + VP Network + CTO.

**Lead angle:** "Residential ARPU is plateauing under FWA and fiber overbuilder pressure. Your commercial fiber book is the growth engine  -  but you compete with Comcast Business, AT&T Business, and the regional CLECs for the same mid-market customers. MaiaEdge is the SaaS fabric layer that lets your team tell commercial customers 'we connect you to AWS / Azure / GCP / Equinix the same way the big carriers do  -  no orchestration team required.' Monetize the commercial fiber you've built, win the multi-state SMB deals you're losing to slow provisioning, and productize cloud on-ramp without building a NaaS." Pair speed with ownership.

### Municipal / Cooperative (`Municipal / Cooperative - Fiber operator`)  -  RENAMED 2026-05-13, ~142 records

**Who:** Municipal utility fiber networks, electric cooperatives running broadband programs, telephone cooperatives (RLEC heritage), tribal broadband authorities, and multi-operator consortia. Community-owned, member-owned, or municipally-owned rather than investor-owned. Operating models include retail FTTH direct-to-subscribers, open-access wholesale platforms (UTOPIA Fiber model), and federation consortia where multiple member operators share infrastructure (Diamond State Networks, INDATEL model). The federation thesis MaiaEdge is ahead of carrier messaging on  -  these operators are already organized around shared infrastructure and need an operating layer for cross-boundary provisioning. **Renamed from `Co-op/consortium` 2026-05-13.** Includes the BEAD subgrant recipient cohort (Q2-Q4 2026 = peak award velocity with binding 4-year build obligations). ~142 records post-migration.

**Quantitative markers:** Revenue $5M-$300M typical; consortia like Diamond State Networks reach $1.66B fiber investment across 13 cooperative members; 500-50,000 route miles; typically single-state for munis/co-ops, 1-5 states for consortia; 50K-1.4M customers passed.

**Anchors:** EPB Chattanooga (city-owned electric utility, 9,000-mile fiber network, first 1 Gig city in Western Hemisphere 2010, $5.3B in net community benefits 2011-2026), UTOPIA Fiber (20 Utah cities + 3 operational partners, open-access wholesale, lowest latency of all 14 muni broadband providers at 6-8ms), Diamond State Networks / DSN (13 Arkansas electric co-ops + AECC, 50,000 miles covering 64% of Arkansas, 1.25M rural Arkansans, $1.66B invested  -  canonical large-consortium anchor), NEMR Telecom, NRECA member operators (~200 co-ops with broadband programs), NTCA member operators (~850 independent community-based RLECs/co-ops across 46 states), USDA RUS-funded co-ops, OzarksGo / Wave Rural Connect / Four States Fiber / Arkansas Fiber Network (DSN members, also standalone records), GVTC Communications (TX telephone co-op), Conexon-managed projects, CO-MO Connect (MO rural electric co-op), INDATEL (700+ rural ILEC/CLEC consortium  -  hybrid with Dark Fiber Specialist).

**Target titles:**
- **Municipal utility fiber:** CEO / President / Executive Director (utility leadership), VP Telecommunications / VP Broadband / Director of Fiber Operations, CTO, City Manager (technology committee).
- **Electric / Telephone Cooperative:** CEO / General Manager (small co-ops are CEO-led), COO / VP Broadband Services, CTO / Director of Network Operations, Board Chair / Technology Committee Chair (member governance), CFO (grant compliance + capital budget).
- **Consortium:** CEO / Managing Member / Co-Managing Members (Diamond State has co-Managing Members), CTO / VP Network Operations, VP Wholesale / Director of Carrier Services, Member co-op CEOs (consortium is governed by its members  -  individual member CEOs are gatekeepers).

Strongest pattern for consortia: Consortium CEO + 2-3 Member CEOs as a governance buying committee.

**Lead angle:** "You already operate as a federation  -  multiple member operators sharing infrastructure with manual coordination at every boundary. MaiaEdge is the operating layer for it. Deterministic provisioning across member operators, open-access partner onboarding in minutes (not the 60-90 day NNI process), and cross-boundary service activation that lets your federation sell commercial wholesale on the commercial strands while BEAD-funded strands stay compliant with grant terms." Two revenue models on the same physical plant, run separately. For BEAD/grant-funded subgrant recipients: "BEAD builds the last mile. MaiaEdge monetizes the middle mile you already own  -  and lets you commercialize the new builds the moment they're lit."

### Middle-mile-only  -  structural misfit (exclusion criteria, not a sub-segment)

Middle-mile-only operators that are purely grant-funded anchor-institution models (KentuckyWired, Project THOR, MassBroadband 123, Mid-Atlantic Broadband Communities Corporation archetypes) are **structurally incompatible with the MaiaEdge SaaS consumption model**. Revenue base is IRU + anchor contracts, not on-demand wholesale. Flag these for exclusion during qualification; do NOT put them in a sub-segment.

**Exception:** If the operator is also a consortium or has a commercial-strand wholesale arm with on-demand pricing, qualify on that basis and assign `Municipal / Cooperative - Fiber operator` or the appropriate commercial-strand sub-segment.

---

## Positioning: Work With Existing Infrastructure (Not Rip-and-Replace)

MaiaEdge does **not** replace the fiber operator's existing investments. This framing is especially critical for Long Haul / Backbone accounts where Cisco Crosswork, Juniper Paragon Pathfinder, Ciena Blue Planet, or Nokia NSP are already in production.

- **We keep their Ciena optics, Juniper routers, Cisco transport.** We orchestrate across the domains they don't own.
- **We layer above the incumbent PCE / OSS.** Vendor-neutral overlay, standards-aligned (MEF LSO, TM Forum ODA).
- **We don't replace Zayo DynamicLink or Lumen RapidRoutes.** We give the operator cross-operator paths their internal automation cannot reach.

Use this framing explicitly when a prospect says "we have internal automation already" or "we've invested in Blue Planet" or "we don't want another vendor in the stack."

---

## BEAD vs. Commercial Strand Distinction (objection reframe)

**Objection:** "BEAD grants lock us into open-access and anchor-institution pricing. Your on-demand SaaS model isn't compatible with our grant-funded segments."

**Reframe:** BEAD terms apply only to grant-funded strands. Commercial IRU, wholesale, and enterprise segments are unconstrained. MaiaEdge monetizes the commercial strands  -  the grant-funded strands stay compliant with BEAD terms. Two revenue models on the same physical plant, run separately.

Applies especially to Regional CLEC, Dark Fiber Specialist, and Municipal Co-op accounts that received BEAD subgrants.

---

## Industry Landscape (2025-2026)

### AI Is Reshaping Fiber Demand
AI data centers require 36x more fiber than traditional CPU racks. GPU cluster interconnects need 24-48 fiber pairs per route vs 1-2 traditionally. The US needs to more than double its fiber infrastructure from 159.6M to 372.9M fiber miles by 2029 (213M net new miles). The largest operators are signing multi-billion-dollar AI connectivity deals and building dedicated AI pipelines.

### Consolidation Wave
93% of the industry says consolidation is happening or imminent. Over $45B in fiber M&A in the last 18 months  -  mega-mergers, divestitures, and portfolio reshuffles. Some operators are exiting fiber entirely to focus on other infrastructure, signaling that fiber-only plays need scale to survive. You're either a consolidator or a target  -  there's no middle ground.

### Fiber Supply Crunch
Fiber prices up 30%+ since early 2025. Ribbon fiber lead times exceed 60 weeks. At least one major manufacturer has sold all inventory through 2026. Labor costs rising 6-8% annually. You can't build fast enough  -  must extract more revenue from existing fiber infrastructure.

### Dark Fiber Economics
Dark fiber market is $8.14B in 2025, growing 13.28% CAGR. Unlit fiber represents 54%+ of the total leased market. Owning dark fiber breaks even at approximately 40% utilization. Every dark strand is a depreciating asset until it's lit.

### BEAD & Regulatory
BEAD ($42.5B) is entering deployment phase  -  most subgrants to be awarded by mid-2026. But pole attachment is THE bottleneck: fees tripled from $30K to $90K/mile in some areas. Make-ready costs up 4x-10x. FCC adopted new 30-day response rules in 2025. 23 states manage pole attachment independently from FCC.

### Financial Pressures
Leverage is heavy across the sector  -  many operators carrying 4-6x net leverage. Debt restructuring through ABS instruments is common. Fiber projects target 10-15% IRRs with 10+ year paybacks. The capital intensity of building fiber is enormous, which is why monetizing EXISTING dark fiber faster is an urgent priority.

### Hyperscaler Buildout: Threat AND Tailwind
Hyperscalers already carry ~2/3 of global internet traffic and are building their own fiber routes, subsea cables, and edge PoPs. $600B+ in hyperscaler capex for 2026 (+36% over 2025), with 75% (~$450B) tied directly to AI infrastructure. Regional operators can't out-build Google, Meta, or AWS. They can out-differentiate them. The winning posture is being the sovereign middle-mile alternative  -  with cross-carrier partner reach  -  for workloads the hyperscalers can't host (regulated verticals, government, sovereign AI) and the last-mile middle-mile partner for workloads hyperscalers DO host. Route-mile competition is a losing game. Sovereign middle-mile is a winning one.

### AI DC Fiber Ratio as Valuation Lever
AI data centers need 36x more fiber than traditional CPU racks (24-48 fiber pairs per route vs. 1-2). Combined with 800Gbps-1.6Tbps capacity demands and 60-week lead times on ribbon fiber, this is inflating dark-fiber strategic value faster than operators can light it. Dark-fiber-rich operators in AI corridors are seeing M&A multiples reflect this: 25-30x EV/EBITDA on AI-adjacent infrastructure assets vs. 16x for broader infra. The board question has shifted from "should we sell dark fiber" to "how do we activate it fast enough to capture AI DC interconnect contracts before hyperscalers route around us."

### Pole Attachment: From Paperwork to Existential Blocker
BEAD ($42.5B) is entering deployment phase  -  most subgrants awarded by mid-2026  -  but 23 states manage pole attachment independently from FCC, each with different timelines, fees ($30K to $90K per mile in some areas), and make-ready cost rules (up 4x-10x). For any multi-state deployment, pole variance is no longer a timeline risk  -  it's an existential blocker that can kill a project before the first strand is lit. This is accelerating interest in monetizing middle-mile fiber operators already own (where poles are a solved problem) over betting on new builds.

### What the C-Suite Is Focused On
- M&A positioning: acquirer or target? At what multiple?
- Monetizing stranded/dark fiber before it depreciates further
- NaaS as the growth path (Zayo DynamicLink is the benchmark)
- AI demand as a once-in-a-generation revenue opportunity
- Provisioning speed as competitive survival  -  manual operators are losing deals
- BEAD money vs pole attachment reality

---

## Their Information Diet

### What They Read
- Light Reading, Fierce Network, Telecompetitor, Lightwave Online, Broadband Breakfast

### Analyst Firms They Trust
- Vertical Systems Group, Omdia, RVA LLC, TeleGeography, Cartesian

### Where They Gather
- Fiber Connect (5,000+ attendees  -  the flagship event), ISE EXPO, FTTH Conference

---

## Competitive Dynamics (Their Market)

These are who FIBER OPERATORS compete against  -  not MaiaEdge competitors.

### Other Fiber Operators
20% of new passings are competitive overbuilds. Cable operators losing ~33% share to fiber overbuilders. Scale matters  -  operators without enough route miles can't compete for multi-state enterprise deals.

### FWA / Wireless Alternatives
Wireless growing 18% vs 3% for fiber in H1 2025 (14.65M FWA subscribers). Primarily a residential/last-mile threat, not enterprise/wholesale  -  but it's eroding the base.

### Hyperscaler-Owned Fiber
Hyperscalers building their own fiber routes for data center interconnect. Operators compete for dedicated dark fiber contracts requiring 800Gbps-1.6Tbps capacity. Two-thirds of global internet traffic already traverses hyperscaler-owned infrastructure.

### NaaS Innovators Setting the Bar
The most advanced fiber operators now offer real-time provisioning via portal, APIs, and even AI-powered chat interfaces. This is the benchmark the segment measures against. If you can't provision in real-time, you're losing deals to operators who can.

---

## MaiaEdge Relevance Bridges

> **⚠️ Internal angle-selection guide.** Specific figures (Zayo 8-12 → 144-432 fiber jump, Windstream 864-fiber orders, Bluebird 36,000-mile post-Everstream footprint, Uniti ABS 2025-1, 21.4x Everstream leverage), named federation consortia (Beach Route Alliance, CanAm2, Diamond State Networks, UTOPIA), and Everstream-style cautionary framing are **internal triggers for picking which angle to lead with**. They are NOT customer-facing talking points. Do not cite operator names, route-mile numbers, or leverage figures in cold outreach or LinkedIn. Use them to determine which relevance bridge fits the account, then write in segment vocabulary.

How current industry trends connect to problems MaiaEdge solves. Use these in discovery, business cases, and proposals.

| Their Trend | Their Pain | MaiaEdge Angle |
|---|---|---|
| AI needs 36x more fiber per rack | Demand is exploding but NNI provisioning still takes 60-90 days  -  can't connect fast enough | "AI customers need fiber NOW. Your NNIs still take 60 days. MaiaEdge connects partners in minutes." |
| 54%+ of fiber is dark/unlit | Stranded assets depreciating while they can't monetize them fast enough | "Every dark strand is revenue waiting. MaiaEdge lights stranded fiber into sellable paths instantly." |
| NaaS leaders offering real-time provisioning | Competitors provisioning in real-time; manual operators losing multi-state deals | "Your competitors are provisioning in real-time. Your sales team is still waiting on NNI paperwork." |
| M&A consolidation (93% say it's imminent) | Must demonstrate revenue growth and differentiation or become an acquisition target at a discount | "Acquirers pay premiums for operators with automated, scalable connectivity platforms." |
| Fiber shortage (30%+ price increase, 60-week lead times) | Can't build fast enough  -  must extract more revenue from existing fiber infrastructure | "You can't lay fiber fast enough. MaiaEdge helps you sell what you already have." |
| BEAD $42.5B entering deployment | Pole attachment bottleneck will eat the timeline  -  need to monetize existing fiber while building | "BEAD builds the last mile. MaiaEdge monetizes the middle mile you already own." |
| Hyperscalers own 2/3 of internet traffic, $600B 2026 capex | Can't compete on route miles with Google/Meta/AWS  -  need to be the sovereign middle-mile alternative with cross-carrier partner reach | "You don't out-build the hyperscalers. You out-differentiate them. Sovereign middle-mile is a category they can't touch." |
| 36x more fiber per AI DC, 800Gbps-1.6Tbps demand | Dark-fiber strategic value is inflating faster than your team can light it  -  boards want activation speed, not more IRUs | "Every unlit strand is a bid you can't answer. MaiaEdge lets your team activate dark fiber as a deterministic, sellable service in minutes." |
| 23-state pole attachment variance killing multi-state deployments | Multi-state AI DC interconnect contracts are time-sensitive; pole paperwork can sink a 90-day commit | "Pole variance killed your build timeline. MaiaEdge monetizes what you already own in the ground while new builds are stuck in permit queues." |
| Sovereign AI demand (EU AI Act Aug 2026, national programs) | Enterprise/government customers are asking for provably sovereign middle-mile paths that BGP can't deliver | "Your fiber is the sovereign alternative to hyperscaler backbones. MaiaEdge turns that into policy-controlled paths with jurisdictional audit trails  -  a service you can sell." |
| PE-backed regional CLECs carrying heavy leverage | Operators that can't monetize fast enough face debt collapse. Monetization velocity is now a CFO-level urgency | "Monetization velocity prevents margin death. Operators that activate dark fiber + automate NNI faster capture AI contracts before the debt clock runs out." (Internal use only  -  do not reference specific PE collapses in outreach.) |
| Multi-operator federation consortia becoming a revenue model | Co-ops, munis, and regional federations are already organizing around shared infrastructure  -  federation-ready is the new baseline | "You already operate as a federation. MaiaEdge is the operating layer for it. Cross-boundary provisioning, open-access partner onboarding, deterministic SLA across member operators." |

---

## Insider Language Bank

Things fiber operators say internally  -  use these to demonstrate you understand their world.

### Board Meeting Language
- "We need to more than double our fiber infrastructure in the next 4 years just to keep up with AI demand"
- "Make-ready is eating our margins alive  -  $90K per mile before we even light a strand"
- "Our competitors are provisioning in real-time. Our NNIs still take 60 days."
- "Every dark strand is a depreciating asset until it's lit"
- "We're either a consolidation target or a consolidator  -  there's no middle ground at our scale"
- "BEAD money is coming but the pole attachment bottleneck will eat the timeline"
- "Our fiber utilization is sitting at 40% while AI demand is through the roof"
- "We can't out-build the hyperscalers. So what CAN we be  -  the sovereign alternative, or a target?"
- "23 states manage pole attachment independently  -  this isn't a paperwork problem anymore, it's a deal-killer"
- "AI data centers need 36x more fiber  -  we need to activate dark strands faster than we can lay new ones"

### KPIs They Report
route miles, fiber/strand miles, on-net buildings, on-net data centers, NNI count, fiber utilization rate, cost per passing, EBITDA margin, net leverage, mean time to provision, IRU backlog, strand density, lit vs dark utilization ratio

### Business Terms to Know
strand density, make-ready costs, overbuild, passings, take rate, ABS financing, cost per passing, fiber miles (vs route miles), MLA (master lease agreement), overlash, near-net, CLEC/ILEC/IXC distinction

---

## Segment Vocabulary Lock

### MUST-Use Terms (Fiber Operator)
route miles, NNI, lit vs dark, Type 2, fiber infrastructure, fiber islands, LOA, dark fiber, IRU, wavelength, provisioning, multi-state, stranded capacity, extend reach, sell into new markets, DIA, partner activation

### BANNED Terms (From Other Segments)
inference, jitter, GPU, tenant, meet-me room, attach rate, upstream carrier, finger-pointing, single pane of glass, asset-light, facility (as neocloud uses it), egress, training run, recompute tax, observability (neocloud context)

### Cold Outreach Rules
- Credibility anchors ("Same team that built Acme Packet" / "128 Technology" / Andy Ory etc.) are BANNED in cold emails and LinkedIn. The message does the talking in outreach. Allowed in live presentations, demos, proposals, and objection handling  -  the track record does the talking in rooms.
- NO sign-offs in emails. Signatures are auto-appended by the email platform.
- Pair speed with ownership: "Your team provisions in minutes" not just "provision in minutes." The operator keeps the customer, the margin, the control.
- Lead with "monetize underutilized fiber" and "instant private fabric across any transport, no routing complexity." Cloud on-ramp is a flagship new-service angle (enable it if not offered, improve margin if already offered)  -  NOT demoted. Extend reach to partner networks is the cross-carrier angle.
- Transport language: "any transport" means fiber, wave, DIA, 5G/fixed wireless, satellite. No-routing-complexity language: "no VLAN stitching, no BGP, no MPLS, no SRv6."

---

*Cross-references: Messaging Framework V4, ICP Sales Playbook (Complete Reference), Cloud On-Ramp Business Case, Competitive Positioning Guide, Terminology Glossary, `context/account-tiering/sub-segment-qualification.md`, `context/account-tiering/tier-compute-spec.md`*
*Updated: May 2026 (Phase 3 Account Tiering & Segmentation Overhaul: added Tier 2 National Wholesale + Regional Cable Operator sub-segments; renamed Co-op/consortium → Municipal / Cooperative - Fiber operator; refreshed anchors per Phase B research; flagged Crown Castle Fiber + GTT + Wave as stale; classification authority + tier computation moved to file 06 and tier-compute-spec.md).*
*Prior update: April 2026 (trend refresh: hyperscaler buildout posture, AI DC fiber ratio as valuation lever, 23-state pole attachment variance, sovereign middle-mile).*
