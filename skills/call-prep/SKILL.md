# Call Prep Skill

Triggers automatically when preparing for meetings or calls with MaiaEdge prospects.

## When This Skill Activates

- User mentions an upcoming meeting or call with a prospect
- User asks to prepare for a conversation
- User asks for discovery questions or talk tracks
- User mentions "call prep," "meeting prep," or "preparing for [company]"

## Reference Files

For deeper context during call preparation, consult:
- **Segment cheatsheets:** `colocation.md`, `fiber-operator.md`, `neocloud.md`, `network-operator.md`, `msp-aggregator.md`
- **competitive-positioning.md** — Battle cards, objection handling by competitor
- **proof-points.md** — Customer stories and public quotes (Arvig, RevNet, NTT, IENTC, Ocean Networks)
- **pricing-reference.md** — PBC/PCE SKUs, term pricing, discount policy
- **call-intelligence.md** — Patterns from past calls organized by segment

## Meeting Prep Framework

### 1. Acknowledge What They've Built
Always start by understanding and respecting what the prospect has accomplished. Never lead with what's broken. Lead with what's impressive, then identify the gap.

### 2. Discovery Questions by Segment

**Fiber Operators:**
- "What percentage of your fiber is generating revenue?" (Signal: 30-50% = buying signal)
- "When you extend reach through NNIs, what does that look like?" (Signal: 60-90 days = buying signal)
- "How do you handle Type 2 circuits? What visibility?" (Signal: "black hole" = buying signal)
- "How many multi-state deals have you lost to provisioning delays?"
- "What does NNI establishment look like today?" (Signal: LOAs, VLAN coordination, BGP = buying signal)
- "How do you provision new paths within your own network?" (Signal: manual, different systems = buying signal)

**Red flags (poor fit):** 85%+ fiber utilized, automated NNI establishment, fully automated end-to-end, API-driven in days.

**Colocation:**
- "When tenants need interconnection or cloud connectivity, what happens today?"
- "How do you handle cross-connect provisioning?"
- "Are you seeing demand for self-service connectivity from tenants?"
- "How often do tenants go to Equinix or Megaport for connectivity you could provide?"
- "What does your interconnection revenue look like vs. space and power?"

**Network Operators:**
- "Is your internal automation unified across all network domains?" (Signal: pockets, not unified = buying signal)
- "What's your provisioning timeline for enterprise requests?" (Signal: weeks, compared to cloud = buying signal)
- "How do you handle multi-carrier paths today?" (Signal: painful, LOAs, weeks = buying signal)
- "What happens when customers need connectivity beyond your footprint?"
- "What visibility do you have across internal domains?"

**MSP/Aggregators:**
- "What visibility do you have into carrier networks?" (Signal: none, blind = buying signal)
- "How do you prove SLA compliance to customers?" (Signal: rely on carrier reports = buying signal)
- "What's your provisioning timeline vs. direct carrier relationships?"
- "How do you handle multi-carrier troubleshooting?"
- "Are Tier 1s competing for your customers directly?"

**Neoclouds (sub-segment determines entry):**

*Universal discovery (all neocloud sub-segments):*
- "How do you move data between object storage and your GPU clusters?" (Signal: public internet, slow = buying signal)
- "What does your network observability look like across facilities?" (Signal: none, blind = buying signal)
- "When you spin up a new facility, how long does connectivity take?" (Signal: weeks, multi-week project = buying signal)
- "What's your egress cost profile?" (Signal: $0.05-0.09/GB, don't know Direct Connect = buying signal)

*Tier 1 Inference (Together.ai, Inference.net, Fireworks):*
- "Where does data pipeline latency actually come from? Is it compute or the network?" (Signal: can't tell = buying signal)
- "Do you have anyone dedicated to the network side?" (Signal: lost the person, IT admin only = buying signal)

*Serverless GPU (RunPod, Modal, Vast.ai):*
- "When a customer complains about performance, can you tell if it's the supplier's network?" (Signal: blind = buying signal)
- "How many GPU suppliers are you managing connectivity across?" (Signal: 15+ in random facilities = buying signal)

*Crypto-to-AI (Applied Digital, Hut 8, TeraWulf):*
- "Your power and space are the asset. What does the connectivity look like?" (Signal: enterprise switches, single uplinks = buying signal)
- "Bitcoin doesn't care about latency, but AI does. How are you handling that transition?"

*Large-Scale GPU (CoreWeave, Lambda, Crusoe):*
- "Your network team is building. What tooling do they have for cross-carrier orchestration?"
- "At 30+ facilities, are you automating connectivity or managing each site individually?"

**Red flags (neocloud poor fit):** Already built 35+ PoPs with dedicated networking team (Groq model), fully solved with unlimited VC, acquired by hyperscaler.

### 3. Pain Validation (Dig Deeper)

After initial discovery, validate with specific operational questions:
- "Where does provisioning slow down?"
- "What happens when a deal requires cross-carrier paths?"
- "How many people touch a new circuit activation?"
- "What's the cost of a provisioning delay in terms of deals or SLA penalties?"

### 4. Value Prop Mapping

Map MaiaEdge value to THEIR specific situation:

**Three pillars:** Automate, Federate, Monetize.

- **Automate:** "Activate deterministic private paths over fiber or DIA instantly. No BGP, no MPLS, no routing complexity."
- **Federate:** "Extend reach through seamless carrier-to-carrier partnerships while maintaining visibility and customer sovereignty."
- **Monetize:** "Turn infrastructure into revenue. Provide services beyond your footprint, monetize idle fiber, offer cloud connectivity under your brand."

### 5. Proof Points (When to Use Each)

| Proof Point | Best For | Trigger |
|-------------|----------|---------|
| Arvig — "almost instantaneous" provisioning | Speed objections, fiber operators | "How fast can you really provision?" |
| RevNet — "Megaport capability between providers" | NaaS comparison, multi-carrier | "Why not just use Megaport?" |
| NTT — Network simplification, PoP acceleration | Tier 1 credibility, scale | "Who else at our scale uses this?" |
| IENTC — 800+ cell towers, 20+ data centers | Mobile backhaul, massive scale | "Can this handle our volume?" |
| Equinix — "Revolutionary and creative" | Technical skeptics, credibility | "Is this proven technology?" |
| Ocean Networks — Federation to INDATEL | Geographic isolation, partnership | "How does federation actually work?" |

### 6. Talk Tracks by Persona

**VP Network / VP Operations (technical leadership):**
"You've invested in fiber/infrastructure, but it's likely fragmented. Different systems at each location, manual provisioning across your own network before you even get to partners. MaiaEdge unifies your network first, then extends that automation to partners."

**VP Sales / Business Development (commercial):**
"What if you could provision across your own network in minutes, not weeks? And then say yes to every multi-state RFP with the same speed? Customers go with whoever's faster. Now that's you, everywhere."

**Director of Engineering / Sr. Network Engineer (technical IC):**
"Provisioning across your own segments probably looks a lot like your NNI process. Manual config at each site, weeks to stand up new paths. MaiaEdge unifies your network first: PBCs at each internal boundary, automated provisioning, end-to-end visibility. No routing protocols, hop-by-hop telemetry across the entire path."

**CEO / President (strategic):**
"You're sitting on infrastructure that should be generating more revenue. MaiaEdge lets you monetize what you already own and extend your reach without building new infrastructure."

**Neocloud CEO / Founder:**
"Groq built 35 Equinix POPs in 6 months. You need the same result without the budget or the network team. MaiaEdge gives you end-to-end visibility across every facility, private cloud on-ramps that cut egress 60-80%, and deterministic paths. No WAN team required."

**Neocloud CTO / VP Eng:**
"You're probably seeing 15-40ms of network variance that nobody's measuring. That compounds per token on inference. We give you hop-by-hop telemetry across paths you don't own, and deterministic paths that eliminate the network as a variable."

**Neocloud VP Infrastructure:**
"Every new facility is a multi-week connectivity project right now. With MaiaEdge, your team provisions paths in minutes. Same connectivity at any colo, unified fabric across all your locations."

**Neocloud CFO / Finance:**
"Public internet egress at $0.05-0.09/GB vs $0.02/GB via private paths. For training runs moving TBs, that's 60-80% savings. OpEx model, no CapEx."

### 7. Technical Deep Dive (If Needed)

**Product summary for technical conversations:**
- PBC: 1RU, dual 100G, AES-256-GCM, protocol-free forwarding, merged L2/L3, <2μs latency overhead
- PCE: Cloud-native, deterministic path computation, SRLG-aware, hop-by-hop telemetry, white-label portal, API-first
- Port Extender: 48x 10/25GbE, 8x 100GbE, <500ns port-to-port, for colo meet-me rooms
- Integrations: Equinix Fabric API, Megaport API, MEF/Mplify LSO Sonata compatible
- Model: IaaS subscription, 1/3/5-year terms, 10G or 100G tiers

**What PBC is NOT:** Not a router replacement. Complements Cisco/Juniper. Sits at domain boundaries where existing automation stops.

### 8. Cloud On-Ramp Business Case (If Relevant)

For colos and fiber operators interested in cloud connectivity:
- 10G deployment: Breaks even at ~4 customers, ~47% gross margin at full utilization
- 100G deployment: ~59% gross margin at 60% utilization, ~75% at full utilization
- Single 100G port generates 46K+ USD/month contribution at full utilization
- Multi-cloud without BGP complexity — no cloud routers needed
- Provider keeps full sovereignty: their portal, pricing, SLAs, customer relationships
