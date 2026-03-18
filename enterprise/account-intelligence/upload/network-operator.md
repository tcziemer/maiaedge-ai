# NetworkOperator CheatSheet

> Converted from: NetworkOperator_CheatSheet.pdf

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
Cross-carrier paths take 60-90 days Instant federation, same-day provisioning beyond your
footprint
Can't match AWS/Azure instant Cloud-like speed for enterprise connectivity requests
provisioning
Multi-domain orchestration complexity PCE handles path computation across all domains via API
Visibility ends at network boundaries End-to-end telemetry across owned and partner networks
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

Cross-carrier paths take 60-90 days |  |  |  | Instant federation, same-day provisioning beyond your | 

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
orchestration" boundaries? MaiaEdge handles the federation layer that internal
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
boundaries? MaiaEdge handles the federation layer that internal
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
partner boundaries. Unify your domains first, then federate everywhere. Same infrastructure, same
speed, same visibility."
Principal Network Architect
Titles: Principal Architect, Distinguished Engineer, Network Architect, Chief Architect
"Think of MaiaEdge as a unification and federation layer. PBCs at domain boundaries, both internal and
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

## Network Operator Approach: Track A vs Track B

**Track A (Has Internal Automation):** Acknowledge their sophistication first. Lead with extending automation beyond their borders. "Your internal automation is impressive. On-net provisioning is fast and productized. But the moment a customer needs a path that crosses a carrier boundary..."

**Track B (No Internal Automation):** Lead with internal unification first. "Even within your own network, provisioning across domain boundaries is manual. MaiaEdge unifies your internal domains first, then extends to partners."

Always research which track applies before writing. Getting this wrong kills credibility instantly.

---

## Segment Vocabulary Lock

### MUST-Use Terms (Network Operator)
multi-domain, on-net/off-net, configuration drift, LOA, BGP, PoPs, orchestration, domain boundaries, federation, enterprise deals, MPLS, wavelengths, carrier boundary, path computation

### BANNED Terms (From Other Segments)
tenant, attach rate, meet-me room, cross-connect (colo context), dark fiber (fiber context), upstream carrier, finger-pointing (MSP context), single pane of glass, asset-light, inference, jitter, GPU, middle mile, training run, recompute tax, egress (neocloud context)

### Cold Outreach Rules
- NO credibility anchors in cold emails (no "Same team that built Acme Packet" / "128 Technology"). The message does the talking, not our history. Credibility anchors are reserved for live objection handling only.
- NO sign-offs in emails. Signatures are auto-appended by the email platform.
- For Track A: MUST acknowledge their internal automation before positioning MaiaEdge. Skipping this feels tone-deaf.
- For Track B: Lead with internal unification, then cross-carrier extension.
- Pair speed with ownership: "Your team extends that automation beyond your borders" not just "faster provisioning."

---

*Cross-references: Messaging Framework V4, ICP Sales Playbook (Complete Reference), Cloud On-Ramp Business Case, Competitive Positioning Guide, Terminology Glossary*
*Updated: March 2026 (Phase 5 messaging update)*
