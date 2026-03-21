# Colocation CheatSheet

> Converted from: Colocation_CheatSheet.pdf

Colocation Operator
Know Your Customer
Attribute Details
What They Buildings, meet-me rooms, metro fiber. NOT route miles. AI-focused colos may have
Own liquid cooling, high-density power (30kW+ racks), GPU cloud tenant relationships.
Revenue Space/power (60-80%, low margin) → Cross-connects (10-20%) → Cloud on-ramps (0-
Model 5%). AI-focused colos: Infrastructure services for GPU cloud providers (Lambda Labs,
CoreWeave, Crusoe).
Scale 1-10+ facilities, 20-500 employees, $10M-$500M revenue
Competitive Tenant expectations set by Equinix/Digital Realty. Cloud revenue going to NaaS
Reality providers. GPU cloud tenants expect deterministic connectivity, not just fast cross-
connects.
Problems We Solve
Problem How MaiaEdge Solves It
6+ week cross-connect provisioning Automated provisioning in minutes, not weeks
Pushing margin & customer relationships to NaaS Offer cloud on-ramps under your brand, keep the
providers margin
Can't match Equinix interconnection experience Fabric-in-a-box without years of development
Competing on space/power alone (low margin) Add high-margin connectivity services to your
portfolio
AI-focused: Best-effort networking breaks inference Deterministic private paths with controlled
latency
Top Pain Points (Their Words)
"Tenants expect instant cross-connects and self-service - the Equinix experience"
"Building connectivity services requires years of development and specialized teams we don't have"
"When tenants need cloud, they call Megaport - we lose the relationship and recurring revenue"
"GPU cloud tenants are asking for latency guarantees we can't make with traditional networking"
Discovery Questions
Question Good Answer (Buying Signal) Red Flag
"How do you handle tenant requests for "We tell them to call "We have our own cloud
cloud connectivity?" Megaport" on-ramps"
"What's your revenue split: space/power vs. "90% space/power, 10% cross- "Connectivity is 30%+ of
connectivity?" connects" revenue"
"When a tenant needs a cross-connect, "Hours per connection, LOAs, "Minutes, fully self-
what's the timeline?" manual config" service"

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

 |  |  |  | CoreWeave, Crusoe). | 

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
Labs, CoreWeave, or Crusoe?" growing segment"
"Are you investing in liquid cooling or high- "Yes, we're building out AI- "Standard density only"
density power (30kW+ racks)?" ready infrastructure"
AI Signal Detection Quick Reference
Signal Indicators Action
Strength
STRONG GPU cloud tenants (Lambda, CoreWeave, Lead with AI/inference messaging,
Crusoe), liquid cooling, 30kW+ racks deterministic paths
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

 | Labs, CoreWeave, or Crusoe?" |  |  | growing segment" |  |  |  | 

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

STRONG |  |  |  | GPU cloud tenants (Lambda, CoreWeave, |  |  | Lead with AI/inference messaging, | 

 |  |  |  | Crusoe), liquid cooling, 30kW+ racks |  |  | deterministic paths | 

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
capability between providers" federation
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
years. Build your own fabric. Keep the customer, margin, and control."
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
federation |  | 

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
- Costs scale linearly with customers — no arbitrage opportunity
- A single PBC ($2,125–$4,250/month) replaces multiple cross-connects AND unlocks dynamic NNI creation over DIA

---

## Segment Vocabulary Lock

### MUST-Use Terms (Colocation)
meet-me room, cross-connect, attach rate, tenant, space and power, LOA, facility, fabric, portal, interconnection, cloud on-ramp, PBC, 1RU

### BANNED Terms (From Other Segments)
route miles, NNI, dark fiber, plant, fiber islands, upstream carrier, finger-pointing, single pane of glass, asset-light, inference (unless AI colo signals present), middle mile, training run, recompute tax, egress (neocloud context)

### Cold Outreach Rules
- NO credibility anchors in cold emails (no "Same team that built Acme Packet" / "128 Technology"). The message does the talking, not our history. Credibility anchors are reserved for live objection handling only.
- NO sign-offs in emails. Signatures are auto-appended by the email platform.
- Pair speed with ownership: "Your meet-me room becomes a self-service exchange" not just "faster cross-connects." The operator keeps the customer, the margin, the control.
- AI colo variant: When GPU cloud tenant signals are STRONG, layer in deterministic path / inference latency language. But this is an ADD to the core colo messaging, not a replacement.

---

*Cross-references: Messaging Framework V4, ICP Sales Playbook (Complete Reference), Cloud On-Ramp Business Case, Competitive Positioning Guide, Terminology Glossary*
*Updated: March 2026 (Phase 5 messaging update)*
