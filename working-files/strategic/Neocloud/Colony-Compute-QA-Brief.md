# Colony Compute: Internal Q&A Brief
**Prospect:** Colony Compute (Rocco Chappie)
**Stage:** Early / exploratory. Tech build on the OEM side is wrapping up.
**Prepared for:** Tim Lieto
**Date:** 2026-04-21
**Purpose:** Conceptual answers to Rocco's April 21 "ponderings" email. Written so Tim can lift answers straight into a reply, or use as talking points for a follow-up working session.

---

## How Colony frames their world (their vocabulary)

- **Honeycomb** = smallest compute unit. Today: 64 x B300 GPUs, one tank.
- **HIVE** = grid of multiple Honeycombs, sized around 1MW.
- **Colony** = the grid of multiple HIVES, sold by the GPU-hour or by the token.
- **Private HIVE / Private Honeycomb** = dedicated, isolated slice for a single enterprise customer.

Speak their language back to them. Don't translate into our vocabulary mid-paragraph; map ours to theirs in the sub-text.

---

## The frame to establish up front

MaiaEdge is the fabric between Honeycombs, between HIVES, and between any HIVE and a Colony customer. Think of it as a direct-connect alternative to the public internet, plus the management layer that lets Colony provision, isolate, and observe every path without a WAN team. For the intra-Honeycomb GPU-to-GPU mesh, Colony keeps whatever they're already doing (InfiniBand or lossless Ethernet). MaiaEdge starts where traffic leaves the tank.

This reframe matters because Rocco is asking six different questions that collapse into two architectural layers: the interconnect inside Colony, and the interconnect between Colony and the outside world. Both are MaiaEdge territory.

---

## Question 1: What does intra-HIVE and interconnected HIVE networking look like with MaiaEdge?

**Short answer for Rocco:** MaiaEdge sits at the HIVE boundary and above. Inside a Honeycomb, GPU-to-GPU stays on whatever lossless fabric the OEM build ships with. From the Honeycomb egress point, MaiaEdge delivers the interconnect.

**Three layers to walk him through:**

1. **Honeycomb to Honeycomb inside a HIVE.** A Path Border Controller (PBC, 1RU appliance) at the HIVE aggregation point creates encrypted L2 paths between Honeycombs. Sub-2μs overhead. AES-256-GCM at line rate. No routing protocols to run.
2. **HIVE to HIVE across Colony.** PBC at each HIVE, unified under one cloud-native Path Computation Engine (PCE). Deterministic paths computed in real time across whatever transport is available (dark fiber, waves, DIA). Automatic failover. Every hop observable end to end.
3. **Colony to the customer / cloud.** Native API integrations into Equinix Fabric and Megaport give Colony instant on-ramps to AWS Direct Connect, Azure ExpressRoute, and GCP, plus private paths to a customer's own data center.

**Why this matters to Colony's business:** Selling GPU time by the hour or by the token only works if token latency and training throughput are predictable. BGP best-effort routing across carriers is the single biggest silent killer of that predictability. MaiaEdge replaces "we hope this carrier has a good day" with deterministic paths and hop-by-hop telemetry.

**Analog they'll recognize:** Groq spun up 35 Equinix POPs in six months with a custom inference network. Colony gets the same class of networking outcome without building a network team.

---

## Question 2: Critical dependencies and desired infrastructure elements

**Minimum viable deployment per HIVE:**

- One PBC at each HIVE egress point (dual PBCs for HA is the recommended pattern)
- Access to the PCE (cloud-native, Colony does not run it themselves)
- Transport between HIVES: any combination of dark fiber, Carrier Ethernet / waves, or DIA. MaiaEdge is transport-agnostic, so Colony can start on DIA for instant reach and add fiber later with DIA as automatic failover.
- One Port Extender per HIVE if Colony wants additional tenant-facing ports (48 ports per Port Extender, integrated switch)

**On the customer-facing side:**

- Equinix or Megaport ports where Colony wants cloud on-ramp (or we help them use existing ones)
- A customer portal integration point (white-label widget, embedded iframe, or API calls from Colony's own portal)
- BSS/OSS integration for billing the network slice alongside GPU-hours

**What Colony does NOT need:**

- A WAN team or CCIEs on staff
- BGP, OSPF, MPLS, or routing protocol expertise
- Per-carrier portal access for each interconnect

**What we should confirm with Colony:**

- Expected power envelope and rack space at each HIVE for the PBC (1RU, <250W typical)
- Target throughput tier per HIVE: 10G or 100G subscription
- Which colos they plan to drop HIVES into (this determines whether they can federate through MaiaEdge hubs already seeded in Ashburn, SV, LA)

---

## Question 3: How do we create a Private HIVE or Private Honeycomb?

This is a strong question and it is exactly where MaiaEdge earns its keep as a commercial product, not just infrastructure.

**Private Honeycomb** = a 64-GPU tank dedicated to one enterprise customer, with a private path from that customer's environment (on-prem, another cloud, SaaS data source) straight into the Honeycomb. No shared egress, no public internet in the data path.

**Private HIVE** = same pattern scaled to a full 1MW HIVE. The customer sees an isolated slice with dedicated paths, policy-based routing, and jurisdictional controls if they need them.

**How MaiaEdge delivers this:**

- **Path-level isolation.** Q-in-Q tagging and stateless forwarding give each customer their own slice of the same physical fabric. One customer cannot see another customer's traffic, even on shared infrastructure.
- **Private cloud connectivity.** Customer gets 2c/GB egress through Direct Connect / ExpressRoute instead of 9c/GB over public internet. This is a pricing advantage Colony can sell, not just a cost they absorb.
- **White-label portal.** Customer clicks "connect my VPC to Private HIVE," path provisions in minutes. The customer sees Colony's brand, never sees MaiaEdge or a third-party NaaS.
- **Sovereign routing, optional.** If the customer needs "data never leaves Germany" or "paths stay in-country," PCE enforces it programmatically. Every hop logged with jurisdiction and timestamp. BGP cannot override the policy.

**The pitch to Rocco:** Private HIVE is a higher-margin SKU than shared GPU-by-the-hour. MaiaEdge makes it operationally trivial to sell. It's a product tier, not a custom integration project.

---

## Question 4: Are there certified network security compliance levels?

**Be careful and precise here.** MaiaEdge delivers capabilities that support compliance; formal third-party product certifications are a moving target and Tim should confirm the current list with Abilash or Kyle before sending anything in writing.

**What we can say with confidence today:**

- Every path is encrypted by default with line-rate AES-256-GCM IPsec. No optional encryption, no off-by-default.
- Hop-by-hop telemetry logs timestamp, carrier, geographic location, and latency for each hop. This is the raw material for audit trails.
- Policy-based sovereign routing lets Colony (or Colony's customer) declare jurisdictional constraints that PCE enforces programmatically. Useful for GDPR, India DPDP, EU AI Act (enforceable August 2026), and national AI program requirements.
- Q-in-Q isolation meets multi-tenant separation requirements.

**What to position as a collaborative question, not a closed answer:**

- Specific third-party attestations (SOC 2, ISO 27001, FedRAMP, etc.) should be confirmed with our team before Rocco pins Tim to a claim. The right framing: "We deliver the controls. Certifications that matter most for your customer mix are part of what we should align on in the design session."
- HIPAA, PCI, and FedRAMP Moderate / High are customer- and deployment-specific and need product + legal review.

**Recommended follow-up:** Tim asks Rocco which customer segments Colony is selling into (healthcare, federal, EU enterprise, financial services). That answer tells us which certification conversation matters most and lets us avoid promising a general-purpose certification list.

---

## Question 5: What is the management layer, and how does it coexist with DCIM, Orchestration, and the Customer Portal?

This is the answer most likely to unlock the technical champion inside Colony. Get it right.

**MaiaEdge management layer in one sentence:** PCE is a cloud-native orchestrator that handles the network slice, exposes everything through APIs, and provides a white-label customer portal that Colony can use as-is or embed into their own.

**How it coexists, layer by layer:**

- **DCIM (power, cooling, rack, physical inventory):** MaiaEdge does not overlap. DCIM manages Colony's building and tanks. PCE manages paths. Clean seam.
- **Orchestration (GPU scheduling, tenant lifecycle, billing events):** PCE integrates via API. When a customer provisions a Private Honeycomb in Colony's orchestrator, Colony calls PCE to spin up the matching path. When the GPU slice tears down, the path tears down. Event-driven, not a parallel system.
- **Customer Portal:** Colony has two patterns to choose from:
  - **Embed the MaiaEdge white-label portal** inside Colony's customer UI. Customer never sees two brands. Fastest path to production.
  - **Call PCE APIs directly** from Colony's own portal. Full brand control, slightly more integration work. This is what the more mature operators do.
- **Observability / NOC tools:** PCE's hop-by-hop telemetry streams via JSON API. Feeds into whatever monitoring stack Colony wants (Grafana, Datadog, custom). MaiaEdge becomes a data source, not a separate NOC.
- **BSS/OSS (billing, ordering):** API-first. Built for Mplify LSO Sonata interoperability, so the integration pattern is standard.

**The sentence Rocco can repeat to his team:** "MaiaEdge is the network slice and the portal for that slice. It plugs into our orchestration and billing, and our customer never has to learn about it."

---

## Question 6: The marketplace and federation

This is where Colony's question opens up the biggest strategic conversation, so treat it as a tease for a follow-up working session, not a full answer.

**The concept in one paragraph:** MaiaEdge turns every operator running a PBC into a potential federation partner. Two operators with MaiaEdge can provision a private path between their networks in minutes over standard DIA, no bilateral carrier agreements, no routing protocol exchange. That means Colony doesn't have to build presence in every city their customers care about. Colony federates through MaiaEdge hubs and reaches them.

**Why this matters for Colony specifically:**

- **Customer reach without building.** A customer in Dallas wants a Private HIVE path from their on-prem environment into Colony, but Colony doesn't have a HIVE in Dallas. If there's a MaiaEdge-enabled colo or fiber operator in Dallas, Colony federates through them. Customer gets a provisioned path in minutes.
- **Bursting and overflow.** If Colony sells a training run that needs more GPUs than one HIVE can deliver, federation gives a clean architectural pattern for bursting to a partner with spare capacity.
- **Instant customer on-ramp.** Customer buys a port at any MaiaEdge-enabled location and reaches Colony. They don't care about the middle.

**Where we are in marketplace seeding (for Tim's awareness, not for Rocco yet):**

- **Ashburn:** seeding with Atlantec. 70 to 80% of US DCI traffic touches this hub.
- **Silicon Valley and Los Angeles:** Atlantec extension.
- **Chicago / Midwest:** Arvig is already a deployed customer and reference.
- **Europe and LatAm:** Ecotel, CMC Networks, IENTC in early stages.

**For the reply to Rocco:** Frame this as "we've already seeded the hubs in the traffic centers that matter, and Colony plugs into that ecosystem rather than inheriting a cold start." Save the partner names and seed economics for the working session.

---

## What to put in Tim's reply email (suggested structure)

1. One-paragraph reframe: MaiaEdge is the fabric between Honeycombs, between HIVES, and between Colony and its customers. Intra-tank GPU mesh is out of scope.
2. Acknowledge all six question clusters and signal that each has a real answer.
3. Offer a 45-minute working session with Tim, Kyle (Sales Engineering), and whoever Rocco wants from the Colony side. Structure the agenda around his six questions, not ours.
4. Ask two clarifying questions that sharpen our answers:
   - Which customer segments is Colony targeting first (enterprise AI, research, sovereign, financial services)? This shapes the compliance and Private HIVE conversation.
   - Where are the first three HIVES physically going? This tells us federation reach on day one.
5. No credibility anchors in this email (Acme Packet / 128 Technology language). Reserve for the working session.

---

## Risks and what to watch for

- **Don't promise certifications we haven't confirmed.** Route compliance specifics through Abilash/Kyle before anything goes in writing.
- **Rocco says "OEM side" is wrapping up.** Worth clarifying whether he means his own GPU server OEM build or a specific NVIDIA reference architecture. Either way, MaiaEdge fits above that layer and is not affected by their OEM choice.
- **Early-stage prospect.** Don't over-architect in the first reply. Answer enough to earn the working session. Save the reference architecture diagrams and seed economics for when there's a real opportunity shape.
- **Neocloud rule reminder:** Colony IS the customer. We can and should use "your customer, your portal, your invoice" framing because Colony is the operator selling onward to enterprises. This is the white-label / "own the customer relationship" angle from the AI Infrastructure Providers sub-segment, not the pure Tier 1 Inference play.

---

## One-line summary Tim can open his reply with

"Quick answer to all six: MaiaEdge is the fabric between your Honeycombs, between your HIVES, and between Colony and any customer environment, with the management layer and white-label portal to sell it as a product. Longer answers below, and I'd rather walk through it live with Kyle on the call."
