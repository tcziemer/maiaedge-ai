# Segment Language Guide

This is the most important reference file in this skill. Read it before writing or critiquing anything.

This file teaches you to sound like someone who has lived inside each segment. Not someone who researched them. Someone who has sat in their meetings, heard their frustrations, and knows the words they actually use when talking to their team on a Tuesday afternoon.

---

## How to Use This File

For each segment, you'll find:

1. **Their vocabulary** — The actual words and phrases these people use. Not our words translated into theirs. Their words.
2. **Their daily reality** — What their day actually looks like. What frustrates them at 3pm on a Wednesday. What keeps coming up in their staff meetings.
3. **How they talk about problems** — The conversational patterns. How they'd describe their pain to a peer at a bar after a trade show. Not how a sales deck frames it.
4. **How an insider writes vs. how an outsider writes** — Side-by-side examples showing the difference between sounding like you've been there and sounding like you googled them.

When you write or critique copy, the test is simple: **Would someone who's spent 15 years in this segment read this email and think "this person gets it"?**

---

## 1. Fiber Operators

### Their Vocabulary

These words should feel natural in your emails. If you use them correctly, the recipient stops reading a sales email and starts reading a note from someone in their world.

**Infrastructure terms they use every day:**
- **Route miles** — How they measure their network. "We have 12,000 route miles across four states." Not "fiber kilometers" or "network footprint."
- **Lit vs. dark** — Lit fiber has active electronics pushing traffic. Dark fiber is installed but unused. "40% of our plant is sitting dark" is how they say "stranded assets."
- **Plant** — Their fiber infrastructure. "We've invested heavily in plant." Not "network assets" or "infrastructure."
- **NNI** — Network-to-Network Interconnect. The connection between two carrier networks. "Every NNI is a 60-90 day project" is a sentence that gets a head nod from every fiber operator CEO in America.
- **Type 2 circuit** — Leased capacity from another carrier. The moment traffic hits a Type 2, visibility dies. They call it "a black hole." Use that phrase.
- **IRU** — Indefeasible Right of Use. How dark fiber is typically leased. Long-term (15-25 year) agreements.
- **Fiber islands** — Disconnected segments of their own network that don't talk to each other well. Different systems at each location. Manual provisioning between them. This is an internal pain most outsiders don't know about.
- **LOA** — Letter of Authorization. The paperwork that starts the 60-90 day clock on a new NNI. Everyone in the industry groans at this acronym.

**How they describe what they sell:**
- Wavelengths, metro Ethernet, wholesale, dark fiber, lit services
- NOT "connectivity solutions" or "network services" (that's vendor talk)

**How they talk about competitors and the market:**
- "Hyperscalers" (AWS, Azure, GCP) — not "cloud providers"
- "Tier 1s" or "the big guys" (AT&T, Verizon, Lumen)
- They respect Lumen's fiber reach but resent their market power
- They talk about "winning" and "losing" deals, not "market share"

### Their Daily Reality

A fiber operator CEO's week includes conversations about:
- Which markets to expand into next (and whether the economics justify the build)
- Enterprise deals that fell through because provisioning took too long
- Whether to invest in lighting more dark fiber or focus on operational improvements
- Competition from Tier 1s who can offer national coverage
- Board/investor pressure to demonstrate ROI on fiber investment

A VP of Operations is dealing with:
- Manual provisioning workflows that involve truck rolls and on-site configuration
- Different OSS systems at different locations that don't integrate
- A team that spends 70% of their time on break-fix instead of strategic projects
- Type 2 circuits where they're responsible for the SLA but can't see the path

A VP of Sales is frustrated about:
- Multi-state RFPs they can't respond to because provisioning commitments are 60-90 days
- Watching deals walk to whoever can deliver faster
- Explaining to customers why the carrier on the other end of an NNI is the bottleneck
- Having no competitive answer for cloud-like instant provisioning

### How They Talk About Problems (Conversational Patterns)

**At a trade show bar, fiber operator to fiber operator:**
- "We've got 15,000 route miles and half of it is sitting dark. Board wants to know when it'll generate revenue."
- "I lost another multi-state deal last week. Customer went with whoever could provision fastest. We quoted 60 days. They quoted two weeks."
- "Once traffic leaves our network onto a Type 2, we're blind. Customer calls with a latency issue and all I can do is open a ticket with the other carrier."
- "We've got fiber islands. Four states, four different systems. Provisioning across our own network takes weeks before we even get to the NNI."

**In a staff meeting:**
- "How many deals did we lose to provisioning delays this quarter?"
- "What's our dark fiber utilization rate? Are we tracking it?"
- "When's that NNI with [partner] going to be live? We've been waiting three months."

### Insider vs. Outsider

**Outsider (sounds like a salesperson who read their website):**
> "I noticed Fatbeam has been expanding its fiber infrastructure across multiple states. As network complexity grows, many operators face challenges with provisioning timelines and monetizing underutilized assets."

**Insider (sounds like someone who's been in the room):**
> "Fatbeam's expansion into Montana means more cross-carrier circuits. I'd guess every new NNI is still a 60-90 day project, and every one of those delays is a multi-state deal at risk."

The difference: the insider uses "NNI," "cross-carrier circuits," and "multi-state deal at risk" — the actual words they use. The outsider uses "provisioning timelines" and "underutilized assets" — sanitized versions that signal "I don't actually work in this world."

---

## 2. Colocation Operators

### Their Vocabulary

**Infrastructure terms they use every day:**
- **Meet-me room** — The secure area inside their data center where carriers interconnect. PBCs deploy here. This is sacred space.
- **Cross-connect** — Physical cable linking two networks within the facility. "Every cross-connect is a project. LOAs, truck rolls, VLAN config." That's how they say "provisioning is manual."
- **Attach rate** — How many services a tenant consumes. Higher attach = stickier tenant. Colos obsess over this metric.
- **Tenant** — Their customer. Not "client" or "user." Tenants lease space, power, and connectivity.
- **Space and power** — The commodity they're stuck selling. "We're just selling space and power" is the frustrated admission that they know they should be selling more.
- **Carrier hotel** — A data center with high carrier density (60 Hudson, One Wilshire). These are the crown jewels of interconnection.
- **LOA** — Same as fiber operators but even more painful here. Every cross-connect starts with an LOA.

**How they talk about the competitive landscape:**
- "Equinix" is spoken with a mix of respect and frustration. Equinix sets the bar for what tenants expect.
- "NaaS" or they'll name Megaport/Equinix Fabric directly. "When tenants need cloud, they call Megaport" is a common admission.
- "Landlord" is the insult. "We've become a landlord, not a connectivity provider." That stings. Use it carefully.
- They measure themselves in **facilities** and **markets**, not route miles.

### Their Daily Reality

A colo CEO's concerns:
- Tenant churn because competitors offer better interconnection
- Revenue concentration in low-margin space/power (60-80% of revenue)
- How to compete with Equinix without Equinix's capital
- Whether to build connectivity in-house (2+ years) or partner

A VP Sales at a colo:
- Losing deals because provisioning cross-connects takes 6+ weeks
- Tenants who ask for cloud connectivity and get told "call Megaport"
- Competing on square footage instead of services
- RFPs that require instant interconnection capabilities they don't have

A CTO/VP Engineering:
- No engineering resources to build fabric from scratch
- The gap between what tenants expect (self-service, instant) and what they can deliver
- Evaluating build-vs-buy for interconnection capabilities
- Managing a grab bag of vendor solutions that don't integrate

### How They Talk About Problems

**At a NANOG afterparty:**
- "We just lost a tenant to the colo down the street because they have better interconnection. Not more power, not cheaper space. Better interconnection."
- "Our best tenants are building relationships with Megaport. That scares me. Once they're on Megaport's portal, we're just the building."
- "I want to offer what Equinix offers. I just don't have three years and ten million dollars to build it."

**In a sales team meeting:**
- "When a tenant asks for cloud, what do we tell them? Because right now we're sending them to someone else."
- "Six-week provisioning is killing our win rate. The tenant signed with us for space, but they'll leave for interconnection."

### Insider vs. Outsider

**Outsider:**
> "DataBank is expanding its colocation footprint across the US. With increasing tenant demands for cloud connectivity, there's an opportunity to differentiate through enhanced interconnection services."

**Insider:**
> "DataBank's expansion puts more tenants in your facilities. But when those tenants ask for cloud on-ramps and you say 'call Megaport,' the relationship starts moving next door. I'd guess interconnection revenue is still single digits as a percentage."

The insider knows: "cloud on-ramps" (their term), "call Megaport" (their painful reality), and that revenue split matters more to them than "enhanced interconnection services."

---

## 3. AI Colocation Operators

### Their Vocabulary

Everything from standard Colo, PLUS:

- **Liquid cooling** — CDU (Coolant Distribution Unit), direct-to-chip, rear-door heat exchangers. If they've invested here, they're serious about AI.
- **Rack density** — Measured in kW per rack. Standard racks: 5-8kW. AI racks: 30-100kW+. "30kW+ racks" is the signal.
- **GPU cloud tenants** — CoreWeave, Lambda Labs, Crusoe, Voltage Park. These are their fastest-growing (and most demanding) tenants.
- **Inference latency** — How long it takes for an AI model to generate a response. Network jitter kills inference. They're starting to learn this.
- **Deterministic paths** — Paths with predictable, consistent performance. The opposite of "best-effort" routing. GPU workloads need this.

### Their Daily Reality

These operators made a bet on AI infrastructure. They built (or are building) liquid cooling, high-density power, and the physical facilities that GPU cloud providers need. But the connectivity layer hasn't kept up.

Their GPU cloud tenants are asking for things the colo hasn't thought about:
- 35+ cross-connects per deployment with sub-10ms latency
- Deterministic paths between GPU clusters (not just fast cross-connects)
- Network performance guarantees that match the compute investment

The painful realization: they've spent millions on cooling and power but the network connecting it all is still best-effort.

### How They Talk About It

- "We've built the compute and cooling infrastructure. The network is the missing piece."
- "Our GPU tenants need dozens of cross-connects per deployment. We can't provision them fast enough."
- "Best-effort networking breaks inference. 33% of AI/ML latency is attributable to network slowness."
- "We invested in liquid cooling and 50kW racks. If we can't deliver deterministic connectivity, we're still just selling power."

### Insider vs. Outsider

**Outsider:**
> "AI infrastructure requires high-performance networking to complement GPU compute capabilities."

**Insider:**
> "You've got liquid cooling and 50kW racks. Your GPU tenants are asking for deterministic paths between clusters, not just faster cross-connects. The compute investment is massive. The connectivity gap is where the SLA breaks."

---

## 4. Neoclouds

### CRITICAL: Messaging Shift

Neoclouds are NOT operators. They ARE the customer. They run GPU clusters across multiple colo facilities. Drop ALL sovereignty language:
- NO "keep your customer"
- NO "your portal, your invoice"
- NO "build your own fabric"

They don't have downstream customers buying connectivity from them. They're buying compute from GPUs and selling it to enterprises. The network between their facilities is the problem, not the product.

### Their Vocabulary

**What they talk about every day:**
- **Inference latency** — Token-by-token generation speed. Measured in milliseconds. This is their product quality metric.
- **Jitter** — Variation in latency. Kills inference performance unpredictably. "Best-effort paths introduce jitter" is how they'd describe the network problem.
- **Middle mile** — The network between their facilities. They don't own it. They can't see it. They can't control it. This is where performance dies.
- **Facility** — Where their GPU clusters live. Not "data center" from their perspective (they lease from colos). "We're scaling to 30+ facilities."
- **Deterministic paths** — What they need but probably don't have yet. Predictable, consistent network performance between GPU clusters.
- **Observability** — Can they see what's happening on the network between their facilities? Almost always the answer is no.
- **Training run** / **training job** — Multi-day GPU compute tasks. If the network hiccups, the entire job can crash. At thousands of dollars per GPU per month, that's expensive.
- **Recompute tax** — The cost of restarting a training job after a network interruption. This is money burning.
- **Egress** — Data transfer costs from cloud providers. They're paying $0.05-0.09/GB on public internet when Direct Connect is $0.02/GB.

**How they think about themselves:**
- They're compute companies that accidentally became networking companies
- Most don't have a network team. They have IT admins, maybe 1-2 people who "also handle networking"
- They don't think of themselves as having a networking problem. They experience it as "inference is slow and we can't figure out why."

### Their Daily Reality

A neocloud CTO's week:
- Debugging inference latency variance across facilities
- Planning deployment at the next 3 colo facilities (connectivity is always the bottleneck)
- Getting complaints from enterprise customers about inconsistent performance
- Trying to figure out if a performance issue is GPU, software, or network (usually a guessing game)

A VP Infrastructure's frustrations:
- Each new facility is a 6-week connectivity project
- Coordinating multiple carriers for each site (different carrier, different topology, different performance)
- No visibility once traffic leaves their facility
- They're responsible for SLA but can't diagnose when it breaks

### How They Talk About Problems

**At a neocloud peer event:**
- "We're at 12 facilities, going to 30 by end of year. Every new site is a connectivity headache."
- "Inference latency varies by 40% between facilities and I can't tell you why. Is it the carrier? Is it the colo? I literally can't see."
- "Our network team is two people. Neither of them is really a network engineer. They're server people who got stuck with the networking."
- "I spent a week debugging a latency issue. Turned out to be a carrier rerouting through a different city. We had zero visibility."

**In an engineering standup:**
- "Facility 7 is slow again. Same symptoms as last month. No idea what changed."
- "We need to onboard the Dallas site. Last time it took 8 weeks. Can we do it in 4?"
- "Customer support says inference SLAs are slipping on the West Coast POPs. Network team says they can't see anything wrong."

### Insider vs. Outsider

**Outsider:**
> "As a leading GPU cloud provider, you need reliable network connectivity between your distributed facilities to ensure consistent inference performance."

**Insider:**
> "You're scaling to 30+ facilities and every new site is a connectivity project. Inference latency varies by facility and your team can't diagnose whether it's the carrier, the colo, or something in between. I'd guess you've got maybe two people managing networking, and neither of them signed up to be WAN architects."

The insider knows: they're scaling fast, they don't have a network team, and the pain shows up as "inference is slow" not "we need better networking." Lead with the symptom, not the diagnosis.

### Inverted Messaging Hierarchy

Unlike every other segment, neoclouds respond to:
1. **Observability first** — "See why you're slow." They need to see the problem before they'll buy the fix.
2. **Cloud on-ramp second** — Cost savings on data movement between hyperscalers and their clusters.
3. **Deterministic paths third** — Once they can see the variance, they want to fix it.

### Credibility Anchors for Neoclouds

- "Same team that built Acme Packet" still works, but for a different reason. Acme Packet was about QoS and session control. That maps to what neoclouds need (deterministic performance).
- 128 Technology is less relevant here (that's a carrier routing story). Use it sparingly.
- The strongest proof point is scale: "Deployed across 800+ cell towers and 20+ data centers."

---

## 5. Network Operators (Tier 1/2 Carriers)

### Their Vocabulary

**CRITICAL: These are sophisticated buyers. They know networking better than we do. Respect that.**

- **Multi-domain orchestration** — Managing paths across different internal network segments. Each domain may have its own systems, its own team, its own processes.
- **Configuration drift** — When network configs across domains get out of sync. A nightmare for large carriers.
- **Self-service portal** — Many already have one. AT&T, Verizon, Lumen all have customer-facing portals. Acknowledging this is essential.
- **On-net vs. off-net** — On-net: within their network (fast, controlled). Off-net: beyond their footprint (slow, manual, painful).
- **LOA, BGP, VLAN** — Same vocabulary as fiber operators but they manage these at massive scale. Hundreds or thousands of BGP sessions.
- **PoPs** — Points of Presence. They have 50 to 500+. The automation varies by PoP.

### Their Daily Reality

**The key insight that most salespeople get wrong:** These carriers are NOT slow internally. Many have sophisticated automation for their own network. The problem is at the boundary. When a customer needs connectivity beyond their footprint, everything stops.

A VP Network Strategy:
- Trying to unify automation across internal domains that were built (or acquired) at different times
- Managing the gap between what enterprise customers expect (cloud-like speed) and what cross-carrier coordination allows (weeks to months)
- Watching AWS + Lumen announce direct enterprise connectivity and wondering how to compete

A Principal Network Architect:
- Dealing with fragmented orchestration (pockets of automation but no unified layer)
- Managing BGP sessions with hundreds of partners
- Evaluating whether to build or buy cross-domain orchestration

### How They Talk About Problems

- "We have automation, but it's not unified across all our domains. Different teams built different systems. Beyond our footprint? Still 60-90 days."
- "Enterprise customers compare us to AWS. They want instant. We're still quoting weeks for cross-carrier paths."
- "Multi-domain orchestration is complex even within our own network. Manual handoffs between domains, different ticketing systems, different provisioning workflows."
- "We can light up a new customer on-net in hours. The moment it crosses a carrier boundary, we're back to LOAs and BGP config."

### Two Tracks (Research-Dependent)

**Track A — Has internal automation (most common for large carriers):**
The approach: "You've automated internally. MaiaEdge extends that everywhere else."
- Acknowledge what they've built. Reference their portal, their API, their branded products.
- Position MaiaEdge as the federation layer that extends their sophistication beyond their borders.
- The gap: cross-carrier, not internal.

**Track B — Fragmented internally:**
The approach: "MaiaEdge unifies your internal boundaries first, then extends to partners."
- Use when research shows no evidence of portal/API automation.
- The gap: both internal domain boundaries AND external carrier boundaries.

**NEVER default to Track A without research. Getting this wrong — claiming a large carrier is slow at something they're fast at — destroys credibility instantly.**

### Insider vs. Outsider

**Outsider:**
> "Enterprise customers increasingly demand faster provisioning times. Your current cross-carrier processes may be limiting your competitive position."

**Insider:**
> "Your internal automation is impressive. But the moment a customer needs a path that crosses a carrier boundary, you're back to LOAs and BGP sessions. I'd guess that gap is costing you enterprise deals where speed is the differentiator."

The insider: acknowledges what they've built (critical), names the specific gap (cross-carrier, not internal), uses their vocabulary (LOAs, BGP sessions), and frames the business impact the way they'd frame it (enterprise deals, speed as differentiator).

---

## 6. MSPs / Aggregators

### Their Vocabulary

**NOT IT MSPs (helpdesk, break-fix). These are network aggregators who resell upstream carrier connectivity.**

- **Upstream carriers** / **upstream providers** — The carriers whose capacity they aggregate. They might have 3-5 carrier relationships.
- **Single pane of glass** — What they sell to their customers. One portal, one invoice, one support team. Behind the scenes, it's a different story.
- **Finger-pointing** — The nightmare. Customer has an issue. The MSP opens a ticket with the carrier. The carrier says it's not their problem. Everyone points at everyone else. This is the MSP's daily life.
- **Asset-light** — Their business model. They don't own fiber or data centers. They aggregate capacity from carriers. This is a point of pride AND a vulnerability.
- **SLA compliance** — They guarantee SLAs to their customers but can't independently verify what's happening inside carrier networks. They're "responsible for the SLA but blind to the path."
- **Tier 1 disintermediation** — Tier 1 carriers going direct to the MSP's customers, cutting them out. The existential threat.

### Their Daily Reality

An MSP CEO's concerns:
- Tier 1 carriers selling directly to their enterprise customers with faster provisioning
- Margins being squeezed because carriers keep raising wholesale prices
- Differentiation: "If we're just reselling the same carriers, why do customers need us?"
- The shift from relationship-based selling to capability-based competition

A VP Operations at an MSP:
- Getting a support call at 2am and having to wait until 8am when the carrier's NOC responds
- Opening tickets with three different carriers for one customer issue
- Proving SLA compliance with carrier reports they can't independently verify
- Provisioning timelines dictated by whichever carrier is slowest

A VP Sales at an MSP:
- Quoting "depends on the carrier" for provisioning timelines and watching the deal walk
- Competing against Tier 1 direct sales teams with faster delivery
- Selling the "single pane of glass" story while knowing the back end is held together with manual processes

### How They Talk About Problems

**At an INCOMPAS event:**
- "We had a customer issue last week. Opened tickets with three carriers. Two said it wasn't them. The third didn't respond for four days. Meanwhile my customer is calling me every hour."
- "AT&T is selling directly to three of my top 20 accounts. They can provision in days. I'm quoting 'four to six weeks, depends on the carrier.'"
- "I'm responsible for the SLA but I can't see inside any of my carriers' networks. When something breaks, it's a guessing game."
- "We're supposed to be asset-light. But if I can't see or control the path, what am I actually selling?"

### Insider vs. Outsider

**Outsider:**
> "Managing multiple carrier relationships creates operational complexity. MaiaEdge provides unified visibility across your carrier partners."

**Insider:**
> "You own the customer relationship but you're blind to everything behind it. When a customer calls with a latency issue, you're stuck between them and three carriers pointing fingers. And when Tier 1s can provision in days, 'depends on the carrier' is losing you deals."

The insider uses: "pointing fingers" (their exact phrase), "depends on the carrier" (what their sales team actually says to customers), and "blind to everything behind it" (how they describe the visibility gap). The outsider uses "operational complexity" and "unified visibility" — words from our world, not theirs.

---

## Cross-Segment Language Rules

### Words That Signal "Insider"
- NNI, LOA, Type 2 (fiber operators)
- Meet-me room, attach rate, cross-connect (colo)
- Inference latency, jitter, middle mile (neocloud)
- Multi-domain, on-net/off-net, configuration drift (network operator)
- Upstream carriers, finger-pointing, SLA compliance (MSP)
- "Dark fiber sitting idle" instead of "underutilized assets"
- "Margin walking out" instead of "revenue leakage"
- "Deal at risk" instead of "business impact"

### Words That Signal "Outsider" (Avoid in Cold Email)
- "Connectivity solutions" (nobody calls it that)
- "Network optimization" (vague vendor speak)
- "Digital transformation" (executive buzzword bingo)
- "Underutilized assets" (say "dark fiber sitting idle")
- "Revenue leakage" (say "margin walking out the door")
- "Enhanced capabilities" (say what you actually mean)
- "Streamline operations" (say "do in minutes what takes weeks")
- "Leverage" as a verb (just... no)

### The Sovereignty Pairing Rule

For every segment EXCEPT neoclouds, speed must be paired with ownership:
- "Your team provisions in minutes" — not just "provision in minutes"
- "Your portal, your invoice, your customer" — always anchor back to them
- "Build your own fabric" — not "connect to a fabric"

For neoclouds: DROP sovereignty entirely. Lead with observability and path control.

### Credibility Anchors

"Same team that built Acme Packet" works everywhere. Keep it short. Drop it in and move on. Don't explain what Acme Packet was. If they know, it builds instant credibility. If they don't, it still signals "these people have done this before."

For technical buyers, you can add "128 Technology" (Juniper acquisition). For business buyers, the $2.55B in combined exits is the number that matters. But never lead with it. It's a supporting fact, not the hook.
