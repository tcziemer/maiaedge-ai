# Graphiant — Competitive Brief
**Prepared:** 2026-05-05 · **Audience:** MaiaEdge sales + product · **Trigger:** Tim Z's Mplify standards-call observation that Graphiant is "into connecting large GPU companies" and is working with Nscale + Canva on London ↔ US-East scale.

---

## 1. Snapshot

| Field | Value |
|---|---|
| Founded | 2020 |
| Founder | Khalid Raza (co-founder of Viptela / SD-WAN pioneer) — now President & Chief Strategy Officer |
| CEO | **Ali Shaikh**, appointed 27 Oct 2025 (founding team, ex-CPO) |
| HQ | Santa Clara, CA |
| Funding | Series B+, backers include Sequoia, Two Bear, Atlantic Bridge |
| Category they claim | "AI-Native Network-as-a-Service" / "Stateless Core" |
| Original category | SD-WAN successor / NaaS over Internet |

## 2. What Graphiant actually sells

Graphiant is a **software overlay** built around a proprietary control concept they call the **Stateless Core**: an ultra-high-speed pub-sub bus where forwarding metadata is embedded in each packet, so the core itself holds no per-customer state, no VRFs, no tunnel mesh. They run this fabric as a service on top of underlying transit / Internet capacity that they do **not** own.

Their three product surfaces:

1. **Network Edge Service** — branch / cloud / SaaS / B2B connectivity. The original SD-WAN-killer pitch. "MPLS-class performance with as-a-Service agility." Two-thirds cheaper than MPLS, provisioned in minutes.
2. **Backbone-as-a-Service** — turnkey global backbone for enterprises that don't want to buy MPLS or build their own.
3. **AI Networking portfolio** (newer, post-2024) — segments, prioritizes, and policy-routes AI traffic stages (ingest, train, infer); "predictable, high-throughput paths between GPU clusters, object storage, and edge capture points."

Stated customer logos in the AI/Neocloud segment: **Nscale**, plus several enterprise-AI deployments. Canva connection in the chat appears to be Nscale-mediated (Canva consumes Nscale GPU capacity; Graphiant connects the user-side traffic).

## 3. Why they showed up on a Mplify call talking about distributed training

Mplify (formerly MEF) is standardizing **NaaS service definitions, LSO APIs, and AI-WAN intent signaling**. Graphiant is leaning hard into that forum because:

- It legitimizes their overlay as a "carrier-grade" service category without them having to actually be a carrier.
- It gives them a route into telcos as a wholesale partner — the "surprising telco ally" angle they've been pushing in press since 2024.
- Ali Shaikh's public 2026 thesis is "the AI bubble pops, networks take the lead" — i.e. when GPU capex slows, the ROI conversation shifts to *connectivity efficiency*, where Graphiant claims to win.

Translation: they want to be the **NaaS overlay** that sits on top of every carrier's underlay, including ours.

## 4. Where Graphiant overlaps with MaiaEdge

| Vector | Overlap |
|---|---|
| Neocloud go-to-market | Both pitching Neoclouds (they have **Nscale** as a public reference; we have Crusoe / Nebius / etc. in pipeline) |
| "Minutes, not months" provisioning | Identical talk track |
| Multi-cloud / multi-DC AI fabric | Both claim to deliver one fabric across clouds, DCs, and edge |
| Sovereignty narrative | Graphiant pivoted to "sovereign networking" with the Khalid → CSO / GCC focus; we lead with sovereignty for everyone except Neoclouds |
| Telco / carrier partnerships | Both want carriers as channel and as underlay |

## 5. Where MaiaEdge wins (and how to position the gap)

**The single most important fact:** Graphiant is a Layer-3/4 overlay that does *not* own underlay fiber, subsea capacity, or carrier-grade L1/L2 transport. **MaiaEdge is the carrier infrastructure underneath that.** This is the entire pitch.

### 5a. Scale-across is a fiber problem, not an overlay problem
The Canva use case in the chat — **distributed training spanning London and US-East** — is exactly NVIDIA's "scale-across" definition: connecting geographically separated GPU clusters into one logical AI factory. NVIDIA's own reference design (Spectrum-XGS) calls for *deterministic, multi-Tbps, low-jitter DCI*. That requires:

- Owned or orchestrated dark fiber / wavelengths
- Sub-millisecond jitter budgets
- RDMA-friendly transport
- Deterministic capacity, not best-effort Internet

Graphiant cannot deliver any of those independently. A pub-sub overlay riding over commodity transit / IP transit cannot synthesize fiber that doesn't exist or guarantee jitter the underlay won't honor. **Their best case in this scenario is to ride MaiaEdge or a carrier underlay** — not displace it.

A useful confirmation from the research: in our queries, Graphiant **never uses the term "scale-across"** in their own materials. They talk about "predictable high-throughput paths" and "east-west bursts" — overlay-native language for east-west enterprise AI traffic, not for transatlantic GPU clustering.

### 5b. Stateless overlay still rents the underlay
Graphiant's "no VRFs, no tunnels, no state" pitch is genuinely clever for *enterprise* WAN. For an AI factory, the bottleneck is bandwidth × distance × jitter, not control-plane state. Removing VRFs does not buy you another 400 Gbps across the Atlantic. We do.

### 5c. "Two-thirds cheaper than MPLS" is the wrong unit economics for AI
Graphiant prices like an SD-WAN replacement. AI scale-across pricing is anchored to **GPU-hours saved by faster training**, which is one-to-two orders of magnitude more valuable than the MPLS line item Graphiant is undercutting. Our PBC-based on-ramp lets the Neocloud or end-customer recover the spend in training-time deltas, not just opex on a WAN bill.

### 5d. Sovereignty: theirs is policy, ours is physical
Graphiant's sovereign story is *encryption end-to-end + edge policy enforcement on a global pub-sub core*. That is a logical sovereignty argument. MaiaEdge sovereignty is **federated private networking with no shared US transit dependency** — physical sovereignty. For UK / EU / GCC AI regulators, "data never traverses a multi-tenant US-anchored core" is a stronger claim than Graphiant's.

### 5e. Mplify standards work — we should be in the room
Recommend Cooper / Aby / Tim Z confirm whether MaiaEdge is engaged with Mplify's AI-WAN / NaaS LSO working groups. If Graphiant is the only one shaping that vocabulary, the standards will codify their architecture as the reference model. We should be a co-author, not a respondent.

## 6. Talk tracks for live deals

### Talking to a Neocloud (Nscale-shaped account)
> "Graphiant gives you a pretty smart overlay so your customers can stitch a VPC to your GPU pods. That's a perfectly fine east-west tool for enterprise inference. The problem is when your anchor tenant says 'we want to train one model across London and Ashburn' — that's a fiber, jitter, and capacity question, and Graphiant doesn't own any of that. We do. So either we're underneath them as your carrier, or we're directly in front of you as the fabric. Either way, the overlay isn't the bottleneck."

### Talking to a SaaS / GPU-tenant (Canva-shaped account)
> "If your distributed training partner is pitching you a stateless overlay, ask them three questions: (1) what's the guaranteed jitter on London → Ashburn at 400 Gbps; (2) is the path you're using single-tenant or shared transit; (3) when capacity tightens during a global training run, who has SLA control over the lambda. Those are underlay questions. Graphiant rents the underlay. We are the underlay."

### Talking to a Network Operator / Telco
> "Graphiant wants to be your overlay partner so they can resell your underlay as their NaaS. We're the opposite. We give *you* the AI on-ramp product, you keep the customer relationship, you keep the margin on the connectivity. Graphiant disintermediates you. We multiply you."

## 7. What to watch

| Signal | Why it matters |
|---|---|
| Nscale public reference becoming a case study | If Graphiant publishes Nscale numbers (training-job latency, multi-region throughput), we need a head-to-head answer ready |
| Ali Shaikh's "AI bubble pops" thesis gaining traction | He's framing 2026 as the year networking takes lead in AI ROI — same wave we're surfing, but with a different physical model |
| Mplify AI-WAN spec drafts | If the LSO API spec assumes overlay-on-Internet semantics, the standard will tilt toward Graphiant |
| Khalid Raza GCC activity | Sovereignty plays in UAE / KSA / Qatar — that's our backyard for international (Tim Z) |
| Telco-partner announcements | If Graphiant signs a Tier-1 carrier as wholesale underlay, that carrier becomes harder for us to land |

## 8. HubSpot / CRM action items

1. Add **Graphiant** as a tracked competitor on every Neocloud and Network-Operator account where overlay/NaaS came up in discovery.
2. On the Nscale account specifically (international, Tim Z): log a note — "Graphiant referenced in 5 May standards-call chatter as connectivity partner; confirm whether they're production or POC; identify the Canva-on-Nscale workload owner."
3. Add a `competitor_mentioned` flag = `Graphiant` to any deal where the customer brought up "Stateless Core," "Network-as-a-Service overlay," or "two-thirds cheaper than MPLS."
4. Pre-build a one-page Graphiant battle-card from this brief — flag for `sales-enablement` skill in the maiaedge-ai repo.

## 9. Sources
- Graphiant — [Ali Shaikh appointed CEO](https://www.graphiant.com/resources/graphiant-appoints-ali-shaikh-as-ceo-to-lead-next-phase-of-ai-driven-growth)
- Graphiant — [Stateless Core for AI and Data Sovereignty](https://www.graphiant.com/resources/stateless-core-networking-for-ai-and-data-sovereignty)
- Graphiant — [AI-Native NaaS](https://www.graphiant.com/resources/creating-frameworks-for-ai-to-build-networks)
- Graphiant — [Network Edge Service brief](https://www.graphiant.com/resources/solutions-brief-network-edge-service)
- Graphiant — [Backbone-as-a-Service brief](https://www.graphiant.com/resources/solution-brief-graphiant-backbone-as-a-service)
- Graphiant — [Neo-Cloud use case](https://www.graphiant.com/use-cases/neo-cloud)
- Graphiant — [2026 AI Bubble thesis (Ali Shaikh)](https://www.graphiant.com/resources/ali-shaikh-2026-ai-bubble-pops-networks-take-lead)
- Pulse 2.0 — [Interview: Ali Shaikh on Graphiant NaaS](https://pulse2.com/graphiant-profile-ali-shaikh-interview/)
- SDxCentral — [Graphiant finds 'surprising' ally in telcos](https://www.sdxcentral.com/analysis/cloud-based-edge-service-provider-graphiant-finds-surprising-ally-in-telcos/)
- LightReading — [Graphiant's new spin on NaaS](https://www.lightreading.com/sd-wan/graphiant-s-new-spin-on-network-as-a-service)
- CB Insights — [Graphiant competitors: Arrcus, InsidePacket, Hedgehog, Cato, Aryaka](https://www.cbinsights.com/company/graphiant/alternatives-competitors)
- NVIDIA — [Scale-Across Networking for distributed AI factories](https://developer.nvidia.com/blog/how-to-connect-distributed-data-centers-into-large-ai-factories-with-scale-across-networking/)
- Nscale — [AI Infrastructure / Keflavik Blackwell deployment](https://www.nscale.com/ai-infrastructure)
