# Colocation CheatSheet

> Converted from: Colocation_CheatSheet.pdf

> **Classification authority:** Sub-segment classification rules, anchors, and confidence thresholds live in `context/account-tiering/sub-segment-qualification.md` (pointer) and file 06 (`context/account-tiering/sub-segment-qualification-full.md`). Tier computation lives in `context/account-tiering/tier-compute-spec.md`. This cheatsheet covers selling angles, personas, pain points, and discovery.

Colocation Operator
Know Your Customer
Attribute Details
What They Buildings, meet-me rooms, metro fiber. NOT route miles. AI-focused colos may have
Own liquid cooling, high-density power (30kW+ racks), GPU cloud tenant relationships.
Revenue Space/power (60-80%, low margin) → Cross-connects (10-20%) → Cloud on-ramps (0-
Model 5%). AI-focused colos: Infrastructure services for GPU cloud providers (Lambda Labs,
Crusoe, Nebius).
Scale 1-10+ facilities, 20-500 employees, $10M-$500M revenue
Competitive Tenant expectations set by Equinix/Digital Realty. Cloud revenue going to NaaS
Reality providers. GPU cloud tenants expect deterministic connectivity, not just fast cross-
connects.
Problems We Solve
Problem How MaiaEdge Solves It
6+ week cross-connect provisioning Automated virtual cross-connects in minutes, fully self-service
Stuck selling space and power with no services Build your own fabric  -  cross-connects, private paths,
layer on top cloud on-ramp, partner interconnects  -  as automated products
Can't match Equinix interconnection experience Fabric-in-a-box without years of development
Cloud on-ramp is either not offered or is thin- Offer it natively under your brand without a
margin hyperscale facility build
AI-focused: Best-effort networking breaks inference Deterministic private paths with controlled
latency
No connectivity beyond the physical facility Virtual meet-me room extends interconnection beyond the building. Reach other DCs, partners, clouds.
Tenants want a marketplace of services, not just space Service fabric with cloud on-ramps, SaaS, AI services, partner interconnects under your brand
Limited reach compared to Equinix Extend reach beyond your facility to other DCs and partners without building there
Top Pain Points (Their Words)
"Every cross-connect is still a project  -  LOAs, truck rolls, VLAN config  -  and tenants expect portal-driven self-service"
"Building our own connectivity services takes years of development and specialized teams we don't have"
"Cloud on-ramp would be a product if we could stand it up without a hyperscale facility build"
"We have multiple sites and no easy way to connect them for a tenant who wants capacity in more than one"
"GPU cloud tenants are asking for latency guarantees we can't make with traditional networking" (AI-focused colos)
Discovery Questions
Question Good Answer (Buying Signal) Red Flag
"How do you handle tenant requests "We refer them out to a third- "We have our own cloud
for cloud connectivity?" party fabric" on-ramp"
"What's your revenue split: space/power "90% space/power, 10% cross- "Connectivity is 30%+ of
vs. connectivity?" connects" revenue"
"When a tenant needs a cross-connect, "Hours per connection, LOAs, "Minutes, fully self-
what's the timeline?" manual config" service"
"When a tenant asks for capacity in a second "We handle it as a separate "Already stitched together
site, what does that look like today?" project, site by site" via our own fabric"

 |  |  |  |  | 

 | Attribute |  |  | Details | 

 |  |  |  |  | 

What They
Own |  |  | Buildings, meet-me rooms, metro fiber. NOT route miles. AI-focused colos may have
liquid cooling, high-density power (30kW+ racks), GPU cloud tenant relationships. |  | 

 |  |  |  |  | 

Revenue
Model |  |  |  | Space/power (60-80%, low margin) → Cross-connects (10-20%) → Cloud on-ramps (0- | 

 |  |  |  | 5%). AI-focused colos: Infrastructure services for GPU cloud providers (Lambda Labs, | 

 |  |  |  | Crusoe, Nebius). | 

 |  |  |  |  | 

Scale |  |  | 1-10+ facilities, 20-500 employees, $10M-$500M revenue |  | 

 |  |  |  |  | 

Competitive
Reality |  |  |  | Tenant expectations set by Equinix/Digital Realty. Cloud revenue going to NaaS | 

 |  |  |  | providers. GPU cloud tenants expect deterministic connectivity, not just fast cross- | 

 |  |  |  | connects. | 

 |  |  |  |  | 

Revenue

Model

Competitive

Reality

 |  |  |  |  | 

 | Problem |  |  | How MaiaEdge Solves It | 

 |  |  |  |  | 

6+ week cross-connect provisioning |  |  | Automated provisioning in minutes, not weeks |  | 

 |  |  |  |  | 

 | Pushing margin & customer relationships to NaaS |  |  | Offer cloud on-ramps under your brand, keep the | 

 | providers |  |  | margin | 

 |  |  |  |  | 

Can't match Equinix interconnection experience |  |  | Fabric-in-a-box without years of development |  | 

 |  |  |  |  | 

Competing on space/power alone (low margin) |  |  |  | Add high-margin connectivity services to your | 

 |  |  |  | portfolio | 

 |  |  |  |  | 

 |  |  |  |  | 

AI-focused: Best-effort networking breaks inference |  |  |  | Deterministic private paths with controlled | 

 |  |  |  | latency | 

 |  |  |  |  | 

 |  |  |  |  |  |  |  | 

 | Question |  |  | Good Answer (Buying Signal) |  |  | Red Flag | 

 |  |  |  |  |  |  |  | 

"How do you handle tenant requests for
cloud connectivity?" |  |  | "We tell them to call
Megaport" |  |  | "We have our own cloud
on-ramps" |  | 

 |  |  |  |  |  |  |  | 

 | "What's your revenue split: space/power vs. |  |  | "90% space/power, 10% cross- |  |  | "Connectivity is 30%+ of | 

 | connectivity?" |  |  | connects" |  |  | revenue" | 

 |  |  |  |  |  |  |  | 

"When a tenant needs a cross-connect,
what's the timeline?" |  |  | "Hours per connection, LOAs,
manual config" |  |  | "Minutes, fully self-
service" |  | 

"When tenants need services you can't "Megaport, Equinix - we lose "We provide
provide, where do they go?" the relationship" everything"
"How many deals have you lost to "Several - six-week timelines "None, we provision
provisioning delays?" kill deals" quickly"
"Do you have GPU cloud tenants like Lambda "Yes, they're our fastest- "No GPU/AI tenants"
Labs, Crusoe, or Nebius?" growing segment"
"Are you investing in liquid cooling or high- "Yes, we're building out AI- "Standard density only"
density power (30kW+ racks)?" ready infrastructure"
AI Signal Detection Quick Reference
Signal Indicators Action
Strength
STRONG GPU cloud tenants (Lambda, Crusoe, Lead with AI/inference messaging,
Nebius), liquid cooling, 30kW+ racks deterministic paths
MEDIUM AI mentioned in marketing, building high- Probe for GPU tenants, mention AI use
density capacity, hyperscaler proximity case
NONE Traditional enterprise tenants, standard density Standard colo messaging (fabric-in-a-
box, Equinix competition)
Objection Handling
Objection Rebuttal
"Megaport already When tenants use Megaport, they're on Megaport's portal, Megaport's
handles this for us" invoice, building a relationship with Megaport. You become a landlord, not a
connectivity provider. MaiaEdge lets you offer the same capabilities - your
brand, your invoice, your control.
"We don't have the That's why colos love it. No routing protocols, no BGP to configure. Deploy
engineering resources" PBCs, connect to PCE, provision from portal. Centra called it 'drop it in and add
water.'
"This sounds expensive" Compare to what you're losing: Megaport margin on every tenant connection,
deals lost to 6-week provisioning. Subscription pricing, starts at 1G, scales to
100G.
"This sounds complex" The opposite. No routing protocols, no BGP, no MPLS. Rack a 1RU PBC in your
meet-me room, connect to cloud PCE, provision from portal. Fabric-in-a-box.
"Who are you?" Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology
($450M to Juniper). Two exits, $2.5B+ combined. Equinix called our approach
'revolutionary and creative.'
"Our GPU cloud tenants They will. Inference performance depends on network predictability. Best-
haven't asked for this" effort introduces jitter that impacts token-by-token latency. Deterministic
paths with hop-by-hop visibility let you guarantee the performance their
workloads need.
"We just provide the GPU cloud tenants need network determinism as much as they need power
facility - networking is and cooling. If you're investing in liquid cooling and high-density racks,
their problem"

 |  |  |  |  |  |  |  | 

 | "When tenants need services you can't |  |  | "Megaport, Equinix - we lose |  |  | "We provide | 

 | provide, where do they go?" |  |  | the relationship" |  |  | everything" | 

 |  |  |  |  |  |  |  | 

"How many deals have you lost to
provisioning delays?" |  |  | "Several - six-week timelines
kill deals" |  |  | "None, we provision
quickly" |  | 

 |  |  |  |  |  |  |  | 

 | "Do you have GPU cloud tenants like Lambda |  |  | "Yes, they're our fastest- |  | "No GPU/AI tenants" |  | 

 | Labs, Crusoe, or Nebius?" |  |  | growing segment" |  |  |  | 

 |  |  |  |  |  |  |  | 

 |  |  |  |  |  |  |  | 

 | "Are you investing in liquid cooling or high- |  |  | "Yes, we're building out AI- |  | "Standard density only" |  | 

 | density power (30kW+ racks)?" |  |  | ready infrastructure" |  |  |  | 

 |  |  |  |  |  |  |  | 

 |  |  |  |  |  |  |  | 

 | Signal |  | Indicators |  |  | Action |  | 

 | Strength |  |  |  |  |  |  | 

 |  |  |  |  |  |  |  | 

 |  |  |  |  |  |  |  | 

STRONG |  |  |  | GPU cloud tenants (Lambda, Crusoe, |  |  | Lead with AI/inference messaging, | 

 |  |  |  | Nebius), liquid cooling, 30kW+ racks |  |  | deterministic paths | 

 |  |  |  |  |  |  |  | 

 |  |  |  |  |  |  |  | 

MEDIUM |  |  |  | AI mentioned in marketing, building high- |  |  | Probe for GPU tenants, mention AI use | 

 |  |  |  | density capacity, hyperscaler proximity |  |  | case | 

 |  |  |  |  |  |  |  | 

NONE |  |  | Traditional enterprise tenants, standard density |  |  | Standard colo messaging (fabric-in-a-
box, Equinix competition) |  | 

 |  |  |  |  | 

 | Objection |  |  | Rebuttal | 

 |  |  |  |  | 

"Megaport already
handles this for us" |  |  | When tenants use Megaport, they're on Megaport's portal, Megaport's
invoice, building a relationship with Megaport. You become a landlord, not a
connectivity provider. MaiaEdge lets you offer the same capabilities - your
brand, your invoice, your control. |  | 

 |  |  |  |  | 

"We don't have the
engineering resources" |  |  |  | That's why colos love it. No routing protocols, no BGP to configure. Deploy | 

 |  |  |  | PBCs, connect to PCE, provision from portal. Centra called it 'drop it in and add | 

 |  |  |  | water.' | 

 |  |  |  |  | 

"This sounds expensive" |  |  | Compare to what you're losing: Megaport margin on every tenant connection,
deals lost to 6-week provisioning. Subscription pricing, starts at 1G, scales to
100G. |  | 

 |  |  |  |  | 

"This sounds complex" |  |  |  | The opposite. No routing protocols, no BGP, no MPLS. Rack a 1RU PBC in your | 

 |  |  |  | meet-me room, connect to cloud PCE, provision from portal. Fabric-in-a-box. | 

 |  |  |  |  | 

"Who are you?" |  |  | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology
($450M to Juniper). Two exits, $2.5B+ combined. Equinix called our approach
'revolutionary and creative.' |  | 

 |  |  |  |  | 

"Our GPU cloud tenants
haven't asked for this" |  |  |  | They will. Inference performance depends on network predictability. Best- | 

 |  |  |  | effort introduces jitter that impacts token-by-token latency. Deterministic | 

 |  |  |  | paths with hop-by-hop visibility let you guarantee the performance their | 

 |  |  |  | workloads need. | 

 |  |  |  |  | 

 |  |  |  |  | 

 | "We just provide the |  | GPU cloud tenants need network determinism as much as they need power
and cooling. If you're investing in liquid cooling and high-density racks, |  | 

 | facility - networking is |  |  |  | 

 | their problem" |  |  |  | 

 |  |  |  |  | 

"We don't have the

engineering resources"

"Our GPU cloud tenants

haven't asked for this"

GPU cloud tenants need network determinism as much as they need power

and cooling. If you're investing in liquid cooling and high-density racks,

network predictability is the missing piece. MaiaEdge lets you be the full-stack
AI infrastructure partner.
Competitive Quick Hits
Competitor Quick Positioning
Megaport / Equinix They own the fabric AND your customer. MaiaEdge = you own both. We integrate
Fabric with them via API for cloud reach.
Lumen PCF Lumen builds their empire; MaiaEdge empowers you to build yours.
SD-WAN SD-WAN = enterprise branch offices. MaiaEdge = carrier/colo infrastructure.
Different layer, different buyer.
Proof Points & Talk Tracks
Proof Points
Customer Quote When to Use
RevNet "If you're familiar with MegaPort... imagine having that NaaS comparison,
capability between providers" partner connectivity
Centra "Fabric in a box, just drop it in and add water and it works" Complexity objection
Equinix "Revolutionary and creative... abstracting complexity with Credibility, technical
their PBC approach" skeptics
AI Deterministic paths for GPU cloud tenant connectivity GPU cloud tenants, AI
Infrastructure workloads
Talk Tracks by Persona
CTO / VP Engineering
Titles: CTO, VP Engineering, VP Technology, VP Infrastructure, VP Platform
"Most colos sell space and power while Equinix captures interconnection revenue. Deploy PBCs in your
meet-me rooms - fabric services, automated cross-connects, cloud on-ramps. Weeks to deploy, not
years. Build your own fabric. Keep the customer, margin, and control. Virtual meet-me room extends your interconnection beyond the physical facility. Your tenants get a marketplace of services, not just a building."
AI variant: "For GPU cloud tenants, add: Deterministic private Ethernet paths with known hop count and
controlled latency. The network predictability that matches your power and cooling investment."
VP Sales / CRO
Titles: VP Sales, CRO, VP Business Development, VP Commercial, VP Partnerships
"What if instead of saying 'call Megaport,' you offered cloud on-ramps yourself - your brand, your
invoice? Deploy MaiaEdge and sell interconnection services within weeks. Same facility - now the margin
stays with you."
AI variant: "GPU cloud tenants are asking for deterministic paths and latency guarantees, not just faster
cross-connects. MaiaEdge lets you say yes."
Sr. Network Engineer
Titles: Sr. Network Engineer, Lead Network Engineer, Network Architect, Infrastructure Architect
"Your team spends hours on each cross-connect - LOAs, VLAN coordination, routing config. Drop a PBC in
your meet-me room - 1RU, no routing protocols. Cloud PCE handles path computation automatically."
AI variant: "Inference cares about tail latency and jitter. Best-effort paths introduce variance.
Deterministic paths with hop-by-hop visibility give you the control GPU workloads need."

 |  |  | 

 |  | network predictability is the missing piece. MaiaEdge lets you be the full-stack | 

 |  | AI infrastructure partner. | 

 |  |  | 

 |  |  |  |  | 

 | Competitor |  |  | Quick Positioning | 

 |  |  |  |  | 

Megaport / Equinix
Fabric |  |  | They own the fabric AND your customer. MaiaEdge = you own both. We integrate
with them via API for cloud reach. |  | 

 |  |  |  |  | 

 | Lumen PCF |  |  | Lumen builds their empire; MaiaEdge empowers you to build yours. | 

 |  |  |  |  | 

SD-WAN |  |  | SD-WAN = enterprise branch offices. MaiaEdge = carrier/colo infrastructure.
Different layer, different buyer. |  | 

 |  |  |  |  |  |  |  | 

 | Customer |  |  | Quote |  |  | When to Use | 

 |  |  |  |  |  |  |  | 

RevNet |  |  | "If you're familiar with MegaPort... imagine having that
capability between providers" |  |  | NaaS comparison,
partner connectivity |  | 

 |  |  |  |  |  |  |  | 

 | Centra |  |  | "Fabric in a box, just drop it in and add water and it works" |  |  | Complexity objection | 

 |  |  |  |  |  |  |  | 

Equinix |  |  | "Revolutionary and creative... abstracting complexity with
their PBC approach" |  |  | Credibility, technical
skeptics |  | 

 |  |  |  |  |  |  |  | 

 | AI |  | Deterministic paths for GPU cloud tenant connectivity |  |  |  | GPU cloud tenants, AI | 

 | Infrastructure |  |  |  |  |  | workloads | 

 |  |  |  |  |  |  |  | 

AI variant: "For GPU cloud tenants, add: Deterministic private Ethernet paths with known hop count and

controlled latency. The network predictability that matches your power and cooling investment."

AI variant: "GPU cloud tenants are asking for deterministic paths and latency guarantees, not just faster

cross-connects. MaiaEdge lets you say yes."

AI variant: "Inference cares about tail latency and jitter. Best-effort paths introduce variance.

Deterministic paths with hop-by-hop visibility give you the control GPU workloads need."

### Cross-Connect Economics
- Individual cross-connects cost approximately **$400/month** each
- Costs scale linearly with customers  -  no arbitrage opportunity
- A single PBC ($2,125–$4,250/month) replaces multiple cross-connects AND unlocks dynamic NNI creation over DIA

---

## Colo Sub-Segments (match HubSpot `company_sub_segment` values)

Four colo sub-segments plus one cross-segment (`Greenfield`) drive buying motion, target titles, and messaging angle. Use the HubSpot values exactly  -  research agents and skills key off these strings. Full classification rules in `context/account-tiering/sub-segment-qualification.md` and file 06.

See `context/account-tiering/tier-compute-spec.md` for tier computation. `AI Signals - colo`, `Modular - colo`, `Hyperscale Wholesale - colo` default to Tier 1 (ceiling 1, floor 3). `Standard - colo` defaults to Tier 3 (ceiling 1, floor 5). `Greenfield` (cross-segment) defaults to Tier 2 (ceiling 1, floor 3).

### Standard Colocation (`Standard - colo`) - ~318 records

**Who:** Traditional interconnection colos. Retail cross-connect margin focus. Equinix parent record, Digital Realty parent record, CoreSite, Cologix, Iron Mountain (retail side), DataBank (retail side), Switch.

**Buying motion:** Interconnection revenue protection. Margin stacking via SLA-backed cross-connect upsell. Self-service portal parity with Equinix Fabric.

**Target titles (by size):**
- **Large public / Tier 1** (Equinix-class): VP Interconnection / Head of Fabric Services (primary), VP Data Center Operations, CRO.
- **Regional multi-facility** ($100M–$500M revenue): VP Operations, VP Commercial / Head of Wholesale, CTO / VP Engineering.

**Lead angle (live conversations / cheatsheet only):** "Fabric-in-a-box in months, not years. Self-service cross-connect portal your tenants already expect." Retail yield thesis: high XC volume × SLA-backed upsell margin = incremental revenue without capex.

> **Cold-email translation:** "Fabric-in-a-box" is banned in cold-email and LinkedIn body. The cold-email lead for Standard Colo is the **interconnection-attach-rate-vs-landlord frame** per `context/outreach/fallback-messaging.md` § Colocation Standard (Sidecar §4.1.A). The phrase here stays canonical for cheatsheet use, sales-enablement collateral, and live discovery conversations.

### AI Signals Colocation (`AI Signals - colo`) - ~160 records

**Who:** AI-native or AI-retrofit colos. Confirmed GPU tenants, liquid cooling, 30kW+ racks. Anchors (verified 2026-05-14, NO Bitcoin mining heritage): Colovore (Santa Clara, liquid-cooled, GPU-tenant-anchored), NTT Global Data Centers Americas (AI side), Nexus Data Centers. Also traditional colos with anchor AI tenants and no mining history.

> **Crypto-to-AI classification carve-out (Cooper 2026-05-14):** Operators with a Bitcoin mining past who pivoted to AI (whether operator OR landlord model) classify as `Crypto to AI - Neoclouds` per `context/account-tiering/sub-segment-qualification.md`. **Companies that previously appeared in C2 anchor lists but route to NC5 because of mining heritage: Crusoe Energy (flared-gas BTC), Applied Digital / APLD (hosted Marathon Digital), Prometheus Hyperscale / Hut 8 lineage, IREN, Core Scientific.** The defining trait is mining history + AI pivot, regardless of current business model. C2 anchor pool is intentionally thin as a result; quarterly anchor refresh 2026-08-14 will expand the no-mining-history list as more pure-play AI colos reach commercial scale.

**Buying motion:** Anchor-tenant economics. 10-15 year lease commitments, tenant-backed financing, embedded networking SLA as a price add-on rather than a standalone product. Tenants (hyperscaler or enterprise) require deterministic multi-region paths, cross-facility failover, orchestrated traffic steering.

**Target titles (by size):**
- **Anchor-tenant model** (Colovore archetype; or Applied Digital / Crusoe archetype if they were NC5 classification - note both are NC5 not C2): Chief Network Engineer / VP Infrastructure (primary technical buyer), CFO (material co-signer on anchor leases, since the MaiaEdge OpEx embed is priced into tenant MSA), CTO (strategic validation).
- **AI-retrofit regional** (traditional colo with AI tenants): VP Interconnection + VP Data Center Operations.

**Lead angle:** "Deterministic paths between your AI tenants' clusters. Multi-region GPU-to-GPU, GPU-to-cloud, and inter-facility failover  -  as a marketed SLA, not a best-effort cross-connect."

### Modular Colocation (`Modular - colo`) - ~10 records

**Who:** Distributed, prefabricated, or edge-pod operators. Growth is site count, not campus size. Anchors: Nodiac (500+ sites pipeline, 800+ MW), EdgePresence/Ubiquity, Armada, Colony Compute.

**Buying motion:** First-multi-site-design moment. Pod #1 → pod #2 is the inflection  -  each new site is either a separate networking project or a day-one join to the same fabric. Centralized decision authority at founder/CEO level; technical delegation often to systems integrators or hyperscaler partners.

**Target titles (by size):**
- **Early-stage** (<50 employees, 1-2 pods): Founder / CEO or COO.
- **Mid-growth** (50-250, 3-10 pods): COO + VP Engineering + Head of Infrastructure.

**Lead angle:** "Every new pod at a new power site is either a separate networking project or a day-one join to your fabric. Make it the second one. One fabric across every pod, whatever the location."

**Tier default:** Tier 1 (ceiling 1, floor 3).

### Hyperscale Wholesale Colocation (`Hyperscale Wholesale - colo`) - ~12 records

**Who:** Wholesale-only or wholesale-anchored colos. 10MW+ standard deployments, 5-15 year terms, 60%+ revenue from hyperscalers (AWS / Azure / Google / Meta / Oracle), per-MW sales (vs Standard per-rack). Anchors: Compass, Aligned (Macquarie; BlackRock H1 2026 pending), Stack Infrastructure (IPI + Blue Owl), NTT Global Data Centers Americas, QTS (Blackstone, 4,752 MW), CyrusOne (KKR + GIP), Vantage (DigitalBridge + Silver Lake $25B Frontier campus), DataBank, Iron Mountain, Equinix xScale (child record), EdgeConneX (EQT), AirTrunk (Blackstone 2024).

**Split-book operator handling:** Several operators run dual books (retail + wholesale). The HubSpot parent record reflects the majority revenue line; a separate child record (if it exists) carries the wholesale book. Equinix parent record = `Standard - colo` (majority revenue retail interconnection); Equinix xScale child record (if separate) = `Hyperscale Wholesale - colo`. Same logic for Vantage, Aligned, NTT, Iron Mountain, QTS  -  classify each record by its book, not by the umbrella brand.

**Buying motion:** Per-MW commercial framing, multi-year tenant MSA embeds, fabric-as-anchor-tenant-benefit. Network determinism and isolated tenant paths sold into the lease structure, not retrofitted post-occupancy. Decision authority concentrated in VP Wholesale / Head of Hyperscale Sales + CFO (lease economics) + Chief Network / Infrastructure Officer (tenant SLA).

**Target titles:** VP Wholesale Sales, Head of Hyperscale / Strategic Accounts, VP Infrastructure, CFO, Chief Network Engineer.

**Lead angle:** "Hyperscale tenants buy per MW and expect cross-facility determinism baked into the lease. Make the fabric a marketed line item in the MSA, not a post-occupancy networking project."

**Tier default:** Tier 1 (ceiling 1, floor 3).

### Greenfield (`Greenfield`) - cross-segment

**Who:** Pre-operational colo or NeoCloud builds. Series A-C funded, sites under construction, fewer than 2 operational sites. Per Cooper 2026-05-14, Greenfield is a real sub-segment that pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` as the parent `customer_segment`. Anchors are announced AI campus builds mid-construction in 2025-26 that don't yet have operational sites.

**Auto-migration rule:** When the first operational site goes live, the record auto-migrates to its operational sub-segment (`AI Signals - colo`, `Modular - colo`, `Hyperscale Wholesale - colo`, or `Standard - colo` on the colo side; the appropriate NeoCloud sub-segment on the compute side).

**Tiebreaker vs Crypto-to-AI:** Bitcoin mining history + AI pivot → `Crypto to AI - Neoclouds` (NOT Greenfield, even if pre-operational). Greenfield is for net-new builds without a mining past.

**Buying motion:** Design-phase fabric selection. The decision to commit to a fabric layer happens during site-design and capital-planning  -  not after the first rack lights up. Founders, CTOs, and lead infrastructure architects are the buyers; financing-stage co-signers (CFO / Head of Strategic Finance) often participate.

**Target titles:** Founder / CEO, CTO, VP Infrastructure / Chief Network Architect, CFO (financing co-sign).

**Lead angle:** "Pick the fabric while you're picking the racks. The day your first site lights up, the second site is already a day-one join, not a separate networking project."

**Tier default:** Tier 2 (ceiling 1, floor 3).

---

## Power-Queue Leverage Play (any sub-segment in constrained markets)

Virginia / Dominion has ~25,000 MW of data-center power requests pending and ~70,000 MW total outstanding (year-long waits common). Tier 1 markets are saturated; tenants are stuck in interconnection queues with power-first developers.

**Reframe:** "MaiaEdge lets you pack more tenants into the MW you already have by using the network as the scarcity control layer, not power. Isolated paths per tenant means you onboard additional hyperscalers in the same physical building without waiting on utility build-out. Tenant diversification without additional capex."

**When to use:** Colo is in a power-constrained market (NoVA, Phoenix, Dublin, Singapore, Frankfurt, Santa Clara). Tenant concentration is a publicly discussed risk. New tenants would require utility queue time the colo can't afford.

**When NOT to use:** Greenfield colo in a power-abundant market. Colo already has substantial unused capacity. The message lands flat when power isn't the binding constraint.

---

## Tenant Concentration Risk Reframe

Public AI-signals colos (anchor-tenant model) are increasingly disclosing customer concentration in their filings  -  a single hyperscaler or neocloud at 60-80%+ of future revenue is now common. Leverage is slipping toward the tenant.

**Reframe for AI Signals colo CFO / CRO:** "MaiaEdge lets you onboard 2-3 additional hyperscalers into the same physical building by guaranteeing them isolated network paths from your existing tenant. Tenant diversification with the same capex base. Concentration risk declines; revenue per MW goes up."

**Pair with:** Power-queue leverage play when the colo can't build out to diversify naturally.

---

## Industry Landscape (2025-2026)

### The Power Constraint
Power replaced space as the binding constraint. North America colocation vacancy hit an all-time low of 1.4% (CBRE, year-end 2025). Northern Virginia sits at 0.72%. Wholesale rates reached $195.94/kW/month nationally (+6.5% HoH). Ashburn breached $215/kW/month  -  highest on record. 81.5% of capacity under construction is pre-leased through 2027+.

### AI Reshaping the Facility
Legacy 5-7kW racks are obsolete for AI workloads. Current AI standard is 50-100kW/rack. NVIDIA GB200 NVL72 runs at 120kW/rack. Vera Rubin NVL144 targets 600kW/rack by 2026. Direct-to-chip (D2C) liquid cooling is now the default for new AI racks. Operators without liquid cooling are losing deals  -  Equinix reports 60% of their largest Q4 2025 deals were AI-driven, with 33% higher density than non-AI.

### Market Bifurcation
The market has split: power-dense wholesale/AI facilities vs. low-latency connectivity/enterprise workloads. Regional operators must pick a lane. Hyperscalers and neoclouds are leasing entire buildings (build-to-suit), crowding out traditional enterprise tenants and shifting the colo model away from multi-tenant roots.

### Capital & M&A
Record M&A: 113 deals in 2025, $69B+ total value. Valuations at 25-30x EV/EBITDA (vs 16x for broader infrastructure). Implied cap rates 4.4%  -  lowest across all asset classes. Capital is tightening  -  the gap between ambitious announcements and financial reality is widening. Only top-tier operators will secure favorable financing. Everyone else is either a buyer or a target at these multiples.

### Community Opposition
Material business risk: $64B of projects blocked or delayed. 188 organized opposition groups across 40 states. Moratorium bills in 14+ states. Water use is the #1 community concern. Germany mandates 100% renewable energy for DCs from 2027. 74% of providers report customers now demand contractual PUE/carbon commitments. If you can't build out, you must monetize existing footprint harder.

### Sovereign Tenant Requirements
Data-residency and jurisdictional audit trails are no longer a Neocloud-only concern. Enterprise and regulated-industry colo tenants (healthcare, financial services, government, defense) are inheriting sovereignty requirements from their own customers and regulators. EU AI Act fully enforceable August 2026 (fines up to 7% of global revenue). GDPR extraterritoriality and US CLOUD Act create direct legal conflict for any tenant whose traffic might transit the "wrong" jurisdiction. 18 US state privacy laws now in force, with mismatched enforcement triggers. Regional colos that can offer tenants provable, policy-controlled paths between facilities (not just BGP best-effort) will win regulated workloads their competitors can't touch.

### Inference-Profile Shift Reshaping the Colo
H100 rental prices crashed 64-75% between Q4 2024 and Q1 2026 ($8-10/hr to $2.99/hr). The neocloud tenant economics that were "training-first" are now "inference-first"  -  inference was 33% of AI spend in 2023, 55% in early 2026, projected 75-80% by 2030. That shift changes what neocloud tenants ask of a colo: lower sustained power with spikier draw profiles, dense east-west cross-connects between GPU tenants in the same building (inference clusters synchronize, not just exfiltrate), and cloud on-ramps tuned for token-latency SLAs, not bulk training dataset ingest. Colos whose connectivity stack was built for north-south hyperscaler egress aren't ready for this.

### Colo vs. Neocloud: Where the Line Blurs
Modular edge operators and crypto-to-AI pivots straddle segment boundaries. Classification drives messaging  -  so getting it right matters. Key question: are they selling space, or selling compute?
- **Sells space/power/cooling to GPU tenants** → AI Colo (this segment). Example: Nodiac deploys modular containerized DCs at renewable energy sites and hosts GPU tenants (500+ sites pipeline, 800+ MW). Their GPU tenants are separate neocloud prospects. Use colo messaging  -  connectivity is a service they offer TENANTS, not a problem they own themselves.
- **Sells compute** (GPUaaS, inference-as-a-service) → Neocloud. Example: Duos Edge AI deploys modular edge pods and sells GPU capacity. They ARE the customer for connectivity. Use neocloud messaging.
- **Crypto-to-AI split** (Cooper 2026-05-14): Bitcoin mining past + AI pivot = `Crypto to AI - Neoclouds`, inclusive of operator AND landlord models. IREN (Microsoft $9.7B landlord deal) and Core Scientific (CoreWeave host) are `Crypto to AI - Neoclouds`, NOT AI colo. A former miner launching their own GPUaaS product is also `Crypto to AI - Neoclouds`. The defining trait is mining history + AI pivot, regardless of current business model.
- **Does both**: Lead with primary revenue model. If unclear, the colo angle is usually safer  -  it positions MaiaEdge as an enabler for their tenants, not a dependency for the facility itself.

### Modular DC Variant (AI Colo sub-segment)
Modular DC operators scale by deploying containerized capacity at partner power sites instead of expanding a single campus. Nodiac, Colony Compute, and similar operators are the archetype. They're AI Colo, not Neocloud (they don't sell compute; GPU tenants are separate neocloud prospects).

**What's different from a traditional AI colo:**
- Growth is site-count, not campus-size. Each new site is an opportunity for a separate networking project  -  or a day-one join to the same fabric.
- Connectivity BETWEEN modular sites is the emerging operational challenge, not connectivity within a single facility.
- Their GPU tenants expect a deterministic fabric across every pod, not per-pod connectivity handled individually.

**Modular-specific angles:**
- "Every new pod at a new power site is either a separate networking project or a day-one join to your fabric. MaiaEdge makes it the second one."
- "Your GPU tenants don't want to care which of your pods they're in. One fabric across all of them makes that true."
- "Power is solved at the site level. Connectivity between sites is the part that decides whether you keep the tenant."

### Greenfield Colo Disambiguation
Greenfield colos are net-new builds, pre-operational or with fewer than 2 operational sites. Per Cooper 2026-05-14, `Greenfield` is now a formal cross-segment sub-segment (`company_sub_segment = Greenfield`) that pairs with either `Data Center Colo Provider` or `NeoCloud`. The record auto-migrates to its operational sub-segment when the first site goes live. While the build is mid-construction, classify as `Greenfield` and pick messaging based on what they're building, not that they're building. Read their plans before writing.

- **AI-ready greenfield** (liquid cooling, high-density power, announced GPU tenants, "AI campus" language on their site, partnerships with neoclouds): use AI Colo messaging. Lead: "Build the connectivity layer alongside the compute layer. Second site onward, it's one fabric across all of them  -  not N separate networking projects."
- **Standard greenfield** (traditional colo build, no AI-ready signals in the plans): use Standard Colo messaging. Lead: "Build your own fabric from day one. Automated virtual cross-connects and cloud on-ramp as native products  -  without the multi-year development project."
- **Shared across both**: "The day your second site comes online, it joins the same fabric as your first. Tenants who want capacity in both get one interconnection order, not two."
- **Tiebreaker vs Crypto-to-AI:** Bitcoin mining history + AI pivot → `Crypto to AI - Neoclouds`, NOT `Greenfield`, even when the AI build is pre-operational.

### Vertical Integration: Your Fabric Referral Is Now a Compute Competitor
The connectivity layer is integrating into compute. Third-party fabric providers have acquired or launched native bare-metal GPU offerings, and hyperscaler interconnect products (Direct Connect, ExpressRoute) bundle GPU capacity on the other end. The referral you send for cloud on-ramp is no longer just an interconnection-margin giveaway. It now introduces your AI tenants to a platform actively selling the same GPU compute they sell. Regional colos that don't own their own fabric are increasingly exposed to fabric providers whose business model competes with their tenants, not just with their interconnection revenue. Owning the connectivity layer is now about tenant retention, not just margin capture.

### Metro-Edge Diffusion
Power constraints in Tier 1 markets (Northern Virginia 0.72% vacancy, moratorium bills in 14+ states) are pushing AI into secondary metros  -  DFW, Columbus, Atlanta, Phoenix, Chicago. Montauk Capital's April 2026 thesis: 26% of planned data center projects facing delays, 75% of enterprise data captured at the edge by 2025 (Gartner), and "modular edge compute at hundreds of kilowatts per deployment" (Crusoe Spark) is the shape of the next wave. Regional colos with sub-megawatt to mid-megawatt footprints in these metros are the actual delivery mechanism  -  if they can offer deterministic paths between distributed inference sites. Cologix-class hyperscale facilities explicitly underserve sub-megawatt distributed clusters, leaving that entire layer open to regional operators who can move fast.

### What the C-Suite Is Focused On
- Power procurement strategy and "time-to-power" as the new metric
- AI readiness: retrofit existing facilities vs. new purpose-built
- Interconnection revenue as % of total  -  what separates "landlords" from "connectivity providers"
- Customer mix risk: hyperscaler concentration vs. enterprise diversification
- M&A positioning: buyer or target at 25-30x multiples?
- How to compete with Equinix's 500,000+ cross-connects and 18% interconnection revenue

---

## Their Information Diet

### What They Read
- Data Center Dynamics, Data Center Knowledge, Data Center Frontier, InterGlobix

### Analyst Firms They Trust
- CBRE (semi-annual trends), JLL (annual outlook), Cushman & Wakefield, Structure Research, 451 Research/S&P Global, DC Byte, Omdia, Uptime Institute

### Where They Gather
- PTC (January, Honolulu), Data Center World, Datacloud USA (September, Austin), Datacloud Global Congress (June, Cannes), infra/STRUCTURE Summit (October, Las Vegas)

---

## Competitive Dynamics (Their Market)

These are who COLOCATION OPERATORS compete against  -  not MaiaEdge competitors.

### Other Colos
Consolidation favors capitalized operators. Regional operators face pressure from better-funded competitors who can secure power, build AI-ready facilities, and offer interconnection platforms.

### Hyperscalers Self-Building
Hyperscalers outpacing colo growth in some markets but still rely on colo for speed-to-market in new regions. Build-to-suit deals lock in revenue but crowd out enterprise tenants.

### Neoclouds as Customers AND Competitors
Lambda, Crusoe, Nebius are simultaneously the biggest demand driver and a competitive threat  -  they may vertically integrate or demand terms that commoditize the colo.

### NaaS Providers (Megaport, Equinix Fabric)
Every tenant that uses Megaport is a relationship the colo loses  -  margin, data, control. Equinix Fabric surpassed 500,000 cross-connects. Regional colos without their own interconnection platform are becoming landlords.

### Alternative Power Providers
Companies like GridFree AI promising off-grid, rapid-deployment facilities. Power-first development models bypassing traditional colo entirely.

---

## MaiaEdge Relevance Bridges

> **⚠️ Internal angle-selection guide.** Specific figures (Northern Virginia 0.72% vacancy, Ashburn $215/kW/month, 113 M&A deals / $69B, 25-30x EV/EBITDA, $64B blocked projects, 500K+ Equinix cross-connects) are **internal triggers for picking which angle to lead with**, not customer-facing talking points. Do not cite these numbers in cold outreach or LinkedIn. Use them to determine which relevance bridge fits the account, then write the outreach in segment vocabulary.

How current industry trends connect to problems MaiaEdge solves. Use these in discovery, business cases, and proposals  -  not just cold outreach.

| Their Trend | Their Pain | MaiaEdge Angle |
|---|---|---|
| Power is the constraint, not space | Differentiating beyond space/power is existential  -  AI tenants need deterministic connectivity, not just racks | "You solved power. Now your AI tenants need deterministic paths between facilities  -  that's the next differentiator." |
| Megaport/Equinix Fabric dominating interconnection | Every tenant that uses Megaport is a relationship the colo loses  -  margin, data, control | "Build your own fabric. Keep the tenant relationship, the margin, the roadmap." |
| 25-30x EV/EBITDA valuations | Interconnection revenue % is what drives premium multiples  -  colos without it are "just landlords" | "The top colos get 18%+ of revenue from interconnection. What's yours? MaiaEdge gets you there without years of development." |
| Community opposition blocking $64B in projects | Can't build new facilities fast enough  -  must monetize existing footprint harder | "If you can't build out, build UP. Turn every existing meet-me room into a revenue engine." |
| Liquid cooling as table stakes for AI | AI tenants arrive with connectivity demands as intense as their cooling demands | "Liquid cooling gets them in the door. Deterministic paths keep them." |
| Hyperscaler/neocloud build-to-suit crowding out enterprise | Customer concentration risk + losing the diverse enterprise base that provides stable MRR | "Enterprise tenants stay when you offer Equinix-level connectivity. MaiaEdge gives you the platform to compete." |
| EU AI Act enforcement Aug 2026 + 18 US state privacy laws | Regulated tenants (healthcare, financial services, government) demanding data-residency and jurisdictional audit trails that BGP can't prove | "Your tenants are about to be asked to prove where their packets traveled, not just where data sits. Policy-driven paths with jurisdictional audit trails are the answer. BGP isn't." |
| Inference overtaking training (55% of AI spend, 75-80% by 2030) | Neocloud tenants shifting to spikier power profiles and east-west traffic patterns your north-south connectivity stack wasn't built for | "Your tenants are getting repriced. Inference changes the shape of their workload  -  and what they need from your building. Deterministic east-west paths between their clusters are the new cross-connect." |
| Metro-edge diffusion into secondary markets | Sub-megawatt distributed inference sites are landing in regional colos  -  but they need deterministic paths between facilities to actually work | "Edge AI is coming to your market. Compute without the connectivity is a shed. MaiaEdge makes your facility the inference delivery point, not the square footage." |
| Modular-edge and crypto-to-AI operators straddling colo/neocloud | Misclassifying a compute-seller as a colo (or vice versa) burns credibility on the first call | "If they sell GPU capacity, they're a neocloud customer of yours. If they sell space to GPU operators, they're a colo. Classify before pitching." |
| Tenant concentration disclosed in filings | Anchor-tenant model is efficient capex but fragile revenue  -  one tenant exit collapses the building's P&L | "MaiaEdge lets you onboard additional hyperscalers into the same building via isolated paths. Concentration risk declines without additional capex." |
| Power queue + utility build-out times (NoVA, Phoenix, Frankfurt, Dublin, Singapore) | Tenants stuck waiting on utility  -  no way to onboard them without fresh MW | "Use the network as the scarcity control layer, not power. Pack more tenants into existing MW via isolated paths." |

---

## Insider Language Bank

Things colocation operators say internally  -  use these to demonstrate you understand their world.

### Board Meeting Language
- "We've become a power company that happens to do colocation"
- "Time-to-power is the only metric that matters right now"
- "Build-to-suit is great until it crowds out your retail tenants"
- "If you can find power, they will come"
- "We're picking a lane  -  wholesale AI or enterprise connectivity"
- "Our interconnection attach rate is what separates us from being a landlord"
- "Megaport is eating our lunch on cloud connectivity"
- "Our regulated tenants are about to start asking us to prove where their traffic went, not just where it sits"
- "The next wave of inference is going to secondary markets  -  do we have the connectivity story for it?"
- "H100 prices collapsed  -  our neocloud tenants are repricing, and their workload profile is changing under us"

### KPIs They Report
vacancy rate, pre-lease rate, MRR per cabinet, AFFO per share, gross bookings, net cabinets billed, cross-connect counts, interconnection revenue %, churn rate (2.2-2.4%), PUE, WUE, utilization rate, MW under development, kW per rack density, cash-on-cash return on gross PP&E, available to renew (ATR)

### Business Terms to Know
time-to-power, speed to power, delivery certainty, powered land, powered shell, power-advantaged markets, MRR per cabinet yield, interconnection attach rates, net cabinets billing added, stabilized assets utilization, annualized gross bookings, build-to-suit, carrier-neutral, network-dense

---

## Segment Vocabulary Lock

### MUST-Use Terms (Colocation)
meet-me room, cross-connect, attach rate, tenant, space and power, LOA, facility, fabric, portal, interconnection, cloud on-ramp, PBC, 1RU, virtual meet-me room, virtual MMR, service fabric, connectivity marketplace, reach beyond your facility, multi-tenancy

### BANNED Terms (From Other Segments)
route miles, NNI, dark fiber, plant, fiber islands, upstream carrier, finger-pointing, single pane of glass, asset-light, inference (unless AI colo signals present), middle mile, training run, recompute tax, egress (neocloud context)

### Cold Outreach Rules
- Credibility anchors ("Same team that built Acme Packet" / "128 Technology" / Andy Ory etc.) are BANNED in cold emails and LinkedIn. The message does the talking in outreach. Allowed in live presentations, demos, proposals, and objection handling  -  the track record does the talking in rooms.
- NO sign-offs in emails. Signatures are auto-appended by the email platform.
- Pair speed with ownership: "Your meet-me room becomes a self-service exchange" not just "faster cross-connects." The operator keeps the customer, the margin, the control.
- AI colo variant: When GPU cloud tenant signals are STRONG, layer in deterministic path / inference latency language. But this is an ADD to the core colo messaging, not a replacement.
- New value props: virtual MMR (extend meet-me room beyond the building), service fabric/marketplace (cloud on-ramps, SaaS, partner interconnects under your brand), reach (connect tenants to other DCs/partners/clouds without building there), multi-tenancy (multiple tenants on same fabric, better unit economics).

---

*Cross-references: Messaging Framework V4, ICP Sales Playbook (Complete Reference), Cloud On-Ramp Business Case, Competitive Positioning Guide, Terminology Glossary*
*Updated: 2026-05-14 (Phase 3 Account Tiering & Segmentation Overhaul: classification authority pointer added; `Hyperscale Wholesale - colo` sub-segment added with split-book operator handling; `Greenfield` cross-segment formalized with auto-migration rule; Crypto-to-AI classification carve-out applied to IREN / Core Scientific landlord-model accounts; sub-segment record counts surfaced; tier defaults pointed at `context/account-tiering/tier-compute-spec.md`).*
