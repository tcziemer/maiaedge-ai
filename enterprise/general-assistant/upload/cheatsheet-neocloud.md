# Partner Cheat Sheet - Neocloud

**MaiaEdge for GPU Cloud Providers**
*Use this when you're calling on Lambda, Crusoe, Voltage Park, Together AI, RunPod, Nebius, Groq, Cirrascale, Fluidstack, Modal, Nscale, Firmus, E2E Networks, Yotta, IREN, Core Scientific, and similar GPU-as-a-service operators.*

> **Critical distinction:** Neoclouds ARE the customer. Do NOT use "keep your customer" or "your portal, your invoice" language. They aren't reselling MaiaEdge to anyone. They're deploying it to run their own infrastructure better.

> **Market context (drop in CEO / CTO / CFO conversations):** Inference will account for ~67% of all AI compute by end of 2026 (up from 33% in 2023, 50% in 2025). 74% of service providers expect enterprises to drive the most AI traffic growth. 54% of enterprises cite sovereignty as a top AI deployment factor. The buyers driving this shift can't accept best-effort routing - and most neoclouds aren't ready.

---

## Know Your Customer

| Attribute | Details |
|---|---|
| **What They Own** | GPU clusters across multiple colo facilities, AI/ML software stacks, orchestration platforms. They do NOT own buildings. They lease from colos. |
| **Revenue Model** | GPU compute rental (hourly/reserved), inference-as-a-service, training cluster access, managed AI infrastructure. |
| **Scale** | Rapidly scaling. $50M-$5B+ revenue. Multi-facility (3-30+ locations). Expanding from 3 to 30+ in 1-2 years is common. |
| **Competitive Reality** | Compute companies that accidentally became networking companies. No WAN team, no Kentik, no PRTG. Network is an afterthought until inference latency becomes unpredictable. |
| **Why They Buy MaiaEdge** | Hop-by-hop observability across facilities. Deterministic paths between GPU clusters. Instant customer on-ramp for the enterprise ramp ahead. |

---

## Problems We Solve

| Problem | How MaiaEdge Solves It |
|---|---|
| Inference latency varies by facility and they can't diagnose why | Hop-by-hop observability across every path between GPU clusters. They see the network for the first time |
| Each new facility is a 6-week connectivity project | Deterministic paths between facilities in minutes, not weeks. New site online in days |
| Every enterprise customer onboarding is a manual provisioning project across different carriers | Multi-tenancy and instant customer on-ramp. Customer buys a port, MaiaEdge handles the rest |
| Best-effort routing introduces jitter that breaks inference and burns GPU utilization | Deterministic Ethernet paths with controlled latency. 128 H100s at 35% utilization across 3 AZs becomes a fixable problem |
| Egress bleeding ($0.05-$0.09/GB on public internet vs $0.02/GB Direct Connect) | Private cloud connectivity as a competitive advantage they sell to win and retain customers |
| Sovereign AI: can't prove data path stays in jurisdiction | Policy-based sovereign routing. In-country PCE deployment. Hop-by-hop audit trail with timestamp, carrier, geographic location |

---

## Top Pain Points (Their Words)

> "We're scaling to 30+ facilities and connectivity is our biggest operational bottleneck."

> "Inference latency varies by facility because every path is different."

> "We can't see what happens between our facilities. It's a black box."

> "Provisioning connectivity to a new facility takes weeks. We need it in days."

> "We're a compute company that accidentally became a networking company."

> "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will."

> "Our CFO wants to know where gross-to-net margin is going. Egress, recompute tax, and inter-AZ latency."

---

## Discovery Questions

| Question | Good Answer (Buying Signal) | Red Flag |
|---|---|---|
| "How many facilities are you deployed across?" | "Multiple, scaling rapidly." | "Single facility." |
| "How do you handle connectivity between GPU clusters in different facilities?" | "It's painful, each facility is different, takes weeks." | "Dedicated network team handling it well." |
| "What visibility do you have into paths between facilities?" | "None once traffic leaves our infrastructure." | "Full visibility end-to-end." |
| "Are you experiencing inference latency variance across paths?" | "Yes, hard to debug." | "Performance is consistent." |
| "Who on your team manages network connectivity between facilities?" | "It's kind of everyone and no one." | "Dedicated WAN team." |
| "When inference performance degrades, how do you determine if it's GPU, software, or network?" | "It's usually a guessing game." | "Full-stack observability." |
| "When an enterprise customer needs a private path to your inference endpoint across three facilities, what's that process today?" | "Manual carrier coordination, takes weeks." | "Self-service in the customer portal." |
| **Sovereign AI:** "Do enterprise customers require proof that data stays within specific geographic boundaries?" | "Yes, and we can't provide it today." | "Not a requirement." |

---

## Objection Handling

| Objection | Rebuttal |
|---|---|
| "We're focused on GPU infrastructure, not networking" | "Exactly why. You shouldn't have to be networking experts. MaiaEdge gives your team the ability to see why inference is slow across facilities and provision deterministic paths in minutes, without routing complexity. Focus on inference, not interconnects." |
| "Our colo partners handle connectivity" | "Do they deliver deterministic paths with end-to-end visibility, or best-effort cross-connects? Inference performance depends on network predictability. If you're debugging latency issues, the network is the variable you can't see." |
| "We're building our own network team" | "Building one to manage multi-carrier complexity is expensive and slow. Networking talent is scarce. MaiaEdge gives you the capability without the headcount. Your team provisions paths, we handle the protocol complexity." |
| "Each facility is different. How does this work?" | "That's exactly what MaiaEdge solves. PBCs at each location, unified under one control plane. Doesn't matter if it's Aligned in Dallas or Cologix in Columbus. Same deterministic paths, same visibility, same provisioning speed." |
| "We don't have this problem yet" | "You do, you just can't see it. Inference latency variance is invisible without cross-facility observability. Once you can see the network between your GPU clusters, you'll find the variance that's been there all along." |
| "Who are you?" | "Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper). Two exits, $2.55B+ combined. We built the carrier infrastructure your colo partners deploy." |

---

## Competitive Quick Hits

| Competitor | Quick Positioning |
|---|---|
| **Status quo (do nothing)** | #1 competitor. They don't know they have a network problem. They experience it as distributed AI infrastructure that's hard to connect. We help them see it. |
| **DriveNets** | Network OS that requires a dedicated network team. MaiaEdge is operable by IT admins. Capability without headcount. |
| **Internal build (network team)** | Expensive, slow to hire, networking talent is scarce. MaiaEdge gives capability without headcount. Engineering stays focused on GPU infrastructure. |
| **Megaport / Latitude.sh bundle** | Megaport wants to be your GPU provider AND your network provider. That's a lot of control to hand one vendor. MaiaEdge gives you deterministic paths under YOUR control. |
| **Colo partners handling it** | Each facility is different, no cross-facility visibility. MaiaEdge unifies the control plane across all facilities and carriers. |

---

## Persona Talk Track Matrix

| Persona | Titles | The Pitch |
|---|---|---|
| **CEO / Founder** | CEO, Co-Founder, President, Founder | "The compute is funded. The facilities are expanding. The growth plan depends on serving customers who aren't hyperscalers. Each enterprise customer is a manual connectivity project right now. That math stops working as you scale. MaiaEdge fixes it before the wall hits." |
| **Technical Champion** | CTO, VP Engineering, VP Platform, Head of Networking, Network Architect, Principal Engineer | "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between. Drop a PBC at each facility, unified under one control plane. Hop-by-hop visibility across paths between GPU clusters. See why you're slow, then fix it." |
| **Infrastructure Operations** | SVP / VP Infrastructure Engineering, VP Infrastructure, VP Data Center Operations, VP Cloud Infrastructure | "The last 3 enterprise customer onboardings each took how many weeks? Different carrier at each site, different provisioning process, different timeline. Multiply that by your pipeline. MaiaEdge gives you instant customer on-ramp under one control plane." |
| **Network/IT Admin** | Network Admin, IT Admin, Infrastructure Engineer, DevOps Lead | "You didn't sign up to debug carrier routing across 15 facilities. PBCs are stateless forwarders. PCE handles all path logic. No BGP, no MPLS. The network becomes operable without a CCIE on staff." |
| **Head of Platform** | Head of Platform, VP Product, Director Platform Engineering | "Customers expect consistent inference SLAs regardless of which facility serves them. Best-effort paths introduce variance. Deterministic Ethernet paths with controlled latency give you the predictability your platform commits to." |
| **CFO** | CFO, VP Finance | "Enterprise customers on private paths pay 2c/GB instead of 9c/GB over public internet. That's not just your cost savings, it's a pricing advantage you sell to win the contract. Multi-tenancy means you serve them without spinning up dedicated hardware per customer." |
| **Commercial Leader** | VP Sales, VP BD, CRO | "When a mid-market customer asks how fast they can get private connectivity to your inference endpoint, that answer is your close rate. Right now it's measured in weeks. Competitors quoting days win. MaiaEdge gives you days." |

---

## Proof Points

| Source | Quote / Outcome | When to Use |
|---|---|---|
| **Datum.net** (channel partner, Zach Smith / ex-Packet CEO) | Direct relationships with Together.ai, Inference.net, RunPod, Modal, Groq | Channel-led intro, neocloud market validation |
| **Together.ai** | Network person quit. Biggest pain is data movement from object stores. | "Compute companies accidentally networking" framing |
| **Groq** | 35 Equinix POPs in 6 months, sub-100ms inference latency targets | Tier 1 inference / distributed POP scale |
| **Acme Packet / 128 Technology** | $2.55B+ combined exits, SBC used by 90% of carriers | "Who are you?" objection (live calls only) |

---

## Sub-Segment Cheat Codes

**`Large Scale GPU - Neocloud` (Nebius, Lambda, Crusoe):** Lead with deterministic paths between facilities for distributed training. The "recompute tax" angle. Network jitter during a 40TB training run causes session failures (~$4,800/GPU/month rebuilding KV cache).

**`Tier 1 Inference - Neocloud` (Together.ai, Groq, Cirrascale, DeepInfra):** Lead with real-time telemetry to diagnose latency. Sub-100ms token latency SLAs need observable paths. White-label customer portal for enterprise self-service.

**`AI Infrastructure providers - Neocloud` (Vultr, DigitalOcean, Fluidstack, Modal, RunPod):** Lead with multi-cloud bridge. Deterministic L2 paths to AWS, Azure, GCP. White-label portal so they own the customer relationship. High-margin port arbitrage on shared 100G ports.

**`Sovereign AI Clouds - Neocloud` (Nscale, Firmus, E2E, Yotta):** Lead with policy-based sovereign routing. Jurisdictional audit trails. In-country PCE deployment. The compute is multi-tenant; the connectivity isn't. That's the gap.

**`Crypto to AI - Neoclouds` (IREN, Core Scientific, Northern Data, TeraWulf - operator AND landlord):** Lead with the uptime trap. Tier 1 tenants won't sign leases without Tier 3+ network reliability. MaiaEdge upgrades a power-rich facility from "mining shed" to "AI-grade data center."

---

## Vocabulary Check (Neocloud-Specific)

**USE:** inference latency, jitter, middle mile, facility, observability, training run, recompute tax, egress, GPU cluster, deterministic paths, best-effort, carrier routing, WAN, paths, programmable, visible, multi-tenancy, instant customer on-ramp, sovereign by design, paths you control, provably private, private cloud connectivity, extend reach.

**BANNED for neoclouds:** Operator-sovereignty language ("keep your customer," "your portal, your invoice," "build your own fabric"). Data sovereignty IS allowed ("sovereign by design," "paths you control," "provably private"). Also banned: VLAN / Q-in-Q (network jargon, neoclouds are compute people).
