# Neocloud Strategy Brief

## Source: Datum.net Call Insights + April 2026 Deck + Montauk Capital Thesis

**THIS IS THE SOURCE OF TRUTH FOR ALL NEOCLOUD MESSAGING. Supersedes prior neocloud positioning.**

*April 2026 update: Reframes messaging lead from "see why you're slow" to "connecting distributed AI infrastructure simply." Adds maturity-based angle selection (in-pain-now vs. scaling-wall) and agentic compounding latency as the new flagship DETERMINISTIC proof point.*

---

## Executive Summary

The February 2026 Datum.net call gave us the first clear picture of what mid-growth neoclouds experience. The April 2026 deck and Montauk Capital's "Last Millisecond" thesis pushed the framing further. Four takeaways that shape how we go to market:

1. **Master pitch: "Connecting distributed AI infrastructure simply."** Observability was the 2024-early 2026 entry point for pain-now neoclouds ("see why you're slow") and it still is. But it's a supporting benefit under the DETERMINISTIC pillar, not the universal lead. The master pitch opens the door; research selects the angle.

2. **Angle selection is a maturity question, not a segmentation question.** Neoclouds at 5-15 facilities debugging latency variance get the in-pain-now angle. Neoclouds at 15+ facilities with hyperscaler-heavy mixes aren't in pain today  -  their growth plan just depends on enterprise customers who don't bring their own connectivity. That's the scaling-wall angle. Same product, different door.

3. **Datum is a channel partner, not just a customer.** They solve Layer 7 (proxy, anycast, DDoS). We solve Layer 2/3 (paths, observability, encryption). Together we're the full-stack answer. Zac Smith has direct relationships with decision-makers at every Tier 1 neocloud.

4. **Agentic latency is the new flagship DETERMINISTIC proof point.** Montauk's April 2026 thesis: agentic workflows chain 10+ sequential inference calls. Each best-effort hop adds 200ms to 2 seconds. Across ten hops, that's tens of seconds of compounding lag. "Training tolerates retries. Inference doesn't. Agentic workflows tolerate neither."

---

## Datum.net Context

**Who:** Virtual telco. 18 Equinix POPs via partner NetActuate, scaling to 40+. Cloudflare-like anycast proxy architecture for neocloud and enterprise traffic.

**Key people:**
- Zac Smith (CEO)  -  former CEO of Packet (acquired by Equinix). Personally connected to leadership at Together.ai, Inference.net, RunPod, Modal, and Groq. Board member at Koya (now Mistral).
- Drew Raines  -  technical lead
- Brett Mertens  -  BD, source of most pain articulation
- Manish Singh  -  engineering
- Shelby Lindsey  -  joining from Equinix to run Datum backbone

**Partnership model:** Datum = Layer 7 (proxy, anycast, DDoS). MaiaEdge = Layer 2/3 (paths, observability, encryption). Full-stack answer together.

---

## What We Were Getting Wrong

| We Assumed | Reality |
|---|---|
| One universal pain across all neoclouds | Two angles, selected by maturity. Mid-growth (5-15 sites) is in pain  -  latency varies by facility, nobody can diagnose it. Scale (15+ sites, hyperscaler-heavy) isn't in pain yet  -  but their growth plan depends on enterprise customers who don't bring their own connectivity. |
| Lead universally with "see why you're slow" | Master pitch is "connecting distributed AI infrastructure simply." Observability is a benefit under DETERMINISTIC, not the lead. Use "see why you're slow" only for prospects already feeling latency variance. |
| Hyperscaler-heavy scale neoclouds aren't prospects | They are  -  the door is enterprise scaling, not latency debugging. Hyperscalers bring their own connectivity. Mid-market enterprise customers don't. |
| All neoclouds have the same pain | Five sub-segments with different operational models. Maturity determines the angle within each. |
| End customers aren't our TAM | $50K+/mo neocloud customers are a demand creation opportunity. |

---

## The Three-Layer Pain

| Pain | What's Happening | MaiaEdge Fix |
|---|---|---|
| Too Slow | Data transfer from S3/GCP/Azure to remote GPU clusters over public internet. Training runs that should take hours take days. Can't diagnose why. | Private cloud on-ramps via Equinix Fabric / Megaport API. Deterministic paths eliminate variable latency. |
| Too Expensive | Public internet egress at $0.05-0.09/GB. Direct Connect costs $0.02/GB. Most neoclouds don't know Direct Connect exists. | Automated Direct Connect provisioning. 60-80% egress cost reduction. |
| Invisible | Zero network observability. No tools to see if the problem is a saturated switch, bad transit route, or MTU issue. | End-to-end hop-by-hop telemetry across paths the neocloud doesn't own. |

---

## The Builder / Reseller Archetype

Not every neocloud rents GPU-hours under its own brand. A large and growing slice are **builders and resellers**: they build and operate clusters on behalf of capital owners (often private equity treating GPU as an asset class), or they sell dedicated capacity plus cloud access to their own downstream customers. For these accounts the front door is NOT latency debugging. It is cloud interconnect and owning the WAN. Two live builder/reseller calls (a build-for-PE integrator and a dedicated-bare-metal private-AI provider) both converged on the same hooks.

**What's actually different about them:**

| Dimension | Builder / Reseller reality |
|---|---|
| Who buys | A hands-on Infrastructure Lead who owns cluster + network + customer access, or a commercial/BD exec who treats MaiaEdge as a co-sell wedge. Both are gated buyers (one said "we don't want to go direct," the other "I have to take it back to the team"). |
| The scaling tax | Not "6 weeks of carrier coordination." It is per-customer networking primitives: every new customer needs its own ASN and IP block, and the end customers (PE owners, enterprises) do not know what an ASN is, so the builder sources them by hand every time. Handoff is per-node, not per-cluster, so they cannot point a whole cluster at one buyer in a single move. |
| The wedge | Consolidate per-customer ASNs and IP blocks into one operator-owned layer fronted by one or two entry and exit points, so networking becomes part of their offering instead of a per-customer project. Make data movement across clouds something their customer does from one place, on paths they control. |
| The channel rule | These accounts resell to their own customers, so respect the boundary. Position as the enablement layer behind their offer ("you become the value proposition"), never as a vendor going direct to their customers. The egress advantage (2c/GB vs 9c/GB) is ammunition they resell to justify the spend, not just a cost saving. |

**Lead hook:** "Your customers move data across clouds from one place, on paths you control, and you stop sourcing an ASN and IP block for every customer by hand." Then expand to deterministic paths, observability, and instant onboarding.

**Sequencing caution:** in one call the buyer put broad enterprise demand for remote/DIA access to bare metal at "mid to late next year." Treat that as one operator's read of their own customers, not a market date. The safe sequence is cloud interconnect now, remote/enterprise-access onboarding as the later expansion.

---

## Updated Messaging Hierarchy

**Master pitch: "Connecting distributed AI infrastructure simply." Three pillars underneath. Research selects the angle; pillars don't change.**

| Pillar | What It Means | Proof Points |
|--------|---------------|--------------|
| **DETERMINISTIC** | Predictable performance between sites. Agentic workflows chain 10+ hops; best-effort routing compounds into seconds of lag. Deterministic paths eliminate the compounding. Hop-by-hop telemetry shows exactly where latency comes from. | PCE path computation, hop-by-hop observability, per-path metrics, JSON API, Montauk agentic thesis. |
| **PRIVATE** | Private cloud on-ramp cuts egress 60-80% (2c/GB vs 9c/GB public). That's not just cost savings  -  it's a pricing advantage your customers get. Sovereign by design: data stays on paths you control. | Equinix Fabric / Megaport API integration, Direct Connect automation, policy-based sovereign routing, jurisdictional audit trails. |
| **INSTANT** | New facility online in minutes, not weeks. Instant customer on-ramp  -  enterprise customer buys a port, you take care of everything else. Multi-tenancy: serve multiple customers from the same infrastructure. | Zero-touch provisioning, instant NNI, self-service portal, multi-tenancy. |

**Angle selection by maturity** (see "Neocloud Angle by Maturity" in segments/neocloud.md for the full framework):

| If research shows... | Lead with | Opening hook |
|----------------------|-----------|--------------|
| 5-15 sites, mixed customers, network person lost or never had one, latency varies by facility | **In-pain-now angle.** DETERMINISTIC with observability as the supporting benefit. | "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between." |
| 15+ sites, hyperscaler-heavy customer mix, enterprise growth plan, building a network team | **Scaling-wall angle.** INSTANT as the lead (speed of customer onboarding), DETERMINISTIC and PRIVATE supporting. | "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." |
| 2-5 sites, crypto-to-AI pivot, early first tenants | **Early-growth angle.** Basic connectivity + tenant-readiness framing. | "Bitcoin doesn't care about latency. Enterprise AI tenants do. The connectivity that worked for mining doesn't survive an inference SLA." |
| Single site, pre-revenue | **Watch list.** Too early for outreach. | N/A |

---

## Core Value Proposition (Neocloud)

Your GPU clusters are scattered across facilities you don't control, connected by networks you can't see and customers you can't onboard fast enough. MaiaEdge is the automation layer that makes distributed AI infrastructure viable  -  deterministic paths so inference performance doesn't vary by facility, private cloud on-ramps that cut egress 60-80%, and instant customer provisioning so every enterprise onboarding isn't a six-week carrier project. No network team required.

---

## By Persona

Persona leads are angle-aware. In-pain-now framing assumes latency variance is already hurting them. Scaling-wall framing assumes growth plan depends on enterprise customers who don't bring their own connectivity.

### In-Pain-Now Persona Leads (5-15 sites, latency variance dominant)

| Persona | Lead With | Avoid |
|---|---|---|
| CEO / Founder | The network between your GPU clusters is the one part of your infrastructure you can't see, can't control, can't diagnose when it breaks. Every latency complaint is a guessing game. | Protocol terms. Keep it about business risk and blind spots. |
| CTO / VP Eng | Inference latency varies by facility and your team can't tell if it's the carrier, the colo, or something in between. Hop-by-hop visibility across paths you don't own is the missing piece. | Business metrics. Keep it technical and diagnostic. |
| VP Infrastructure | Every new facility is a 6-week connectivity project. Different carrier, different topology, different performance baseline. Your team is rebuilding the same thing from scratch every time. | Strategy. Stay operational and specific. |
| CFO / Finance | Egress at $0.05-0.09/GB over public internet when private paths cost $0.02. For training runs moving TBs, 60-80% savings. OpEx, no CapEx. | Technical terms. Keep it about dollars. |
| Network/IT Admin | You didn't sign up to be a WAN architect. But here you are, managing connectivity across 15 facilities with no monitoring, no path control, different carrier at each site. | Don't oversell. Keep it simple. |
| Head of Platform | Customers expect consistent inference performance regardless of facility. The network between facilities is the uncontrolled variable  -  some regions are just slower, nobody can explain why. | Keep it about outcomes and SLAs. |

### Scaling-Wall Persona Leads (15+ sites, hyperscaler-heavy, enterprise ramp)

| Persona | Lead With | Avoid |
|---|---|---|
| CEO / Founder | The compute is funded, the facilities are expanding, and the growth plan depends on serving customers who aren't hyperscalers. Each of those enterprise customers is a manual connectivity project right now. That math stops working as you continue to scale. | Technical anything. Protocol names. Don't frame as a networking problem  -  frame as a scaling constraint. |
| CTO / VP Eng | When an enterprise customer needs deterministic paths to your GPU clusters across three facilities, that's either 6 weeks of carrier coordination or it's automated. One of those scales. The other is why you're about to hire 4 network engineers you can't find. | Revenue or strategy framing. Keep it about engineering trade-offs and operational reality. |
| VP Infrastructure | The last 3 enterprise customer onboardings each took how many weeks? Different carrier at each site, different provisioning process, different timeline. Multiply that by the next 30 customers on the pipeline. | Vision or strategy. Stay operational. |
| CFO / Finance | Enterprise customers on private paths pay 2c/GB instead of 9c/GB over public internet. That's not your cost savings  -  that's a pricing advantage you sell to win the contract. And multi-tenancy means you serve them without spinning up dedicated hardware per customer. | Technical terms. Dollars, unit economics, competitive pricing advantage only. |
| VP Sales / BD | When a mid-market customer asks how fast they can get private connectivity to your inference endpoint, the answer is your close rate. Right now that answer is measured in weeks. The competitors quoting days win that deal. | Architecture or infrastructure. This persona cares about deal velocity and win rate. |

---

## Neocloud Sub-Segments

The master pitch and pillars apply to all neoclouds. Sub-segment shapes vocabulary and use-case framing; maturity (see above) shapes the angle.

| Sub-Segment | Examples | Situation | Angle Default | Entry Point | Don't |
|---|---|---|---|---|---|
| Tier 1 Inference | Together.ai, Inference.net, Fireworks, Baseten | 5-30+ facilities. Had or lost a network person. Object storage data movement is the live pain. | In-pain-now (default). Scaling-wall if hyperscaler-heavy + enterprise ramp signals. | Observability + cloud on-ramp. "See why your data pipeline is slow." Agentic angle lands hard for inference SLAs. | Don't assume they have a team to evaluate architecture. |
| Serverless GPU | RunPod, Modal, Vast.ai, SaladCloud | Marketplace. 15+ suppliers in random facilities. On hook for SLA, blind to supplier network. | In-pain-now. | Supplier visibility. "Stop taking blame for problems you can't see." | Don't use operator language. They're asset-light. |
| Crypto-to-AI | Applied Digital, Hut 8, TeraWulf, Bitdeer, IREN, Core Scientific | Former miners. Have power/space. Terrible connectivity. Enterprise switches, single uplinks. | Early-growth. | Basic connectivity + tenant-readiness. "Bitcoin doesn't care about latency. Enterprise AI tenants do." | Don't be condescending. Don't assume networking terms. |
| Large-Scale GPU | Lambda, Crusoe, Voltage Park, Nebius | $1B+ valuations. Building network teams. 15-30+ facilities. Hyperscaler-heavy today, enterprise ramp ahead. | **Scaling-wall (default).** In-pain-now only if latency variance is their stated problem. | Enterprise onboarding velocity. "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." | Don't oversimplify. Don't lead with latency-debugging  -  they'll tell you their GPUs are performing fine. |
| Sovereign AI | Nscale, Firmus, E2E Networks, Yotta | Built for GDPR/DPDP/national AI programs. Hard restrictions on data storage AND transit. | In-pain-now with sovereignty framing. | Policy-based sovereign routing. "Prove packets never left jurisdiction  -  in transit, not just at rest." | Don't use operator-sovereignty language. DATA sovereignty only. |

---

## End Customer Messaging

End customers don't deploy MaiaEdge. They benefit through their neocloud or Datum. We're creating demand or connecting them to providers that deliver it. Different message, different tone, later timeline.

| Dimension | To Neoclouds | To End Customers |
|---|---|---|
| We are | Infrastructure peer. "Here's what you need to build." | Ecosystem advisor. "Here's what your providers should offer." |
| Pain framing | "Can't see the network. No team. Provisioning takes weeks." | "Training slow. Egress expensive. Inference inconsistent." |
| Credibility | "Same team behind Acme Packet" | "Working with leading GPU providers" |
| CTA | "Open to a conversation?" | "Worth seeing which providers are ahead?" |
| Timeline | Phase 1+2: Now. | Phase 3: After deployment footprint. |

### End Customer Angles

| Angle | Persona | Pain | Ask |
|---|---|---|---|
| Egress Cost | CFO, VP Finance | $0.05-0.09/GB over public internet vs $0.02/GB private. 60-80% savings. | "Worth seeing what private paths do to your egress bill?" |
| Training Speed | VP ML Eng | Bottleneck isn't GPU, it's data ingestion speed over public internet. | "Interested in what this does to your pipeline?" |
| Inference | CTO, VP Eng | 15-40ms network variance. Compounds per token. Nobody measuring it. | "Worth a conversation?" |
| Multi-Cloud | Head of Platform | Data in S3, models on Lambda, serving from GCP. Every hop is public internet. | "Open to talking unified connectivity?" |

---

## Neocloud TAM

**Estimated Global Neocloud TAM: 250-350 companies**

| Source | Estimate | Scope |
|---|---|---|
| McKinsey (Nov 2025) | 100+ neoclouds globally | 10-15 at meaningful scale in US alone |
| Neocloud.world directory | 187 companies tracked | Broadest public tracker |
| SemiAnalysis ClusterMAX 2.0 | 60-80 rated providers | Only companies with live, benchmarkable GPU clusters |
| Crypto-to-AI pivots | 15-25 active pivots | Bitcoin miners converting to GPU cloud |
| Sovereign AI / Telco GPU clouds | 18+ telco-led AI factories | NVIDIA counts 18 across 5 continents |

### Current Coverage

| Metric | Current State |
|---|---|
| Our identified universe | 142 companies |
| In HubSpot CRM | 125 tagged NeoCloud |
| Estimated global TAM | 250-350 companies |
| Coverage estimate | ~40-55% |
| Gap to close | ~100-200 companies |

### Coverage by Sub-Segment

| Sub-Segment (HubSpot `company_sub_segment` where canonical) | Our List | Est. TAM | Coverage |
|---|---|---|---|
| `Tier 1 Inference - Neocloud` | 15-20 | 20-25 | 75-85% |
| `Large Scale GPU - Neocloud` | 15-20 | 25-30 | 60-70% |
| `Crypto to AI - Neoclouds` | 11 | 20-25 | ~50% |
| `AI Infrastructure providers - Neocloud` (incl. serverless / inference startups, GPU marketplaces) | 18-22 | 40-55 | 35-45% |
| `Sovereign AI Clouds - Neocloud` (incl. telco GPU clouds) | 8-10 | 30-40 | ~25% |
| AI Chip + Cloud | 8-10 | 10-15 | ~65% |
| Regional / Emerging Market | 20-25 | 50-70 | ~35% |

---

## Discovery Signals for Finding Missing Companies

1. **NVIDIA GPU Allocation Announcements**  -  Single best leading indicator. Monitor newsroom, GTC keynotes, regional AI factory announcements.
2. **Crypto Mining Pivot Announcements**  -  SEC filings (10-K pivot language), hyperscaler lease announcements, WGMI ETF holdings. Watch: Applied Digital, Galaxy Digital, Stronghold, Argo, Mawson, Northern Data Group, Cathedra Bitcoin, Soluna.
3. **Venture Capital / Growth Equity Rounds**  -  Crunchbase/PitchBook: 'GPU cloud', 'AI infrastructure', 'inference platform'. Any Series A+ is a potential target.
4. **Sovereign AI National Initiatives**  -  Canada ($2B), India ($1.25B), EU AI Factories (13+ sites), Saudi Arabia (HUMAIN), UAE (Core42/Stargate), South Korea, Japan.
5. **AI Colocation Tenant Lists**  -  Our colo segment is a direct feeder. Every colo conversation should generate neocloud intelligence.
6. **Industry Trackers**  -  SemiAnalysis ClusterMAX, Neocloud.world, CoinShares Mining Reports, NVIDIA Newsroom, DataCentre Magazine.
7. **Conference Intelligence**  -  NVIDIA GTC, OCP Global Summit, SC/Supercomputing, AI Infrastructure Day, Data Centre World.

---

## Specific Intelligence (Datum-sourced, requires Ziemer/Abilash approval before actioning)

| Company | Intel | Implication |
|---|---|---|
| Together.ai | Network person quit. Biggest pain is data movement from object stores. Zac has direct relationship. | Highest-priority warm intro via Datum. |
| Inference.net | Same data movement problem. Zac has direct relationship. | Second warm intro. |
| RunPod | 200K+ users. 15+ GPU suppliers in random facilities. On hook for SLA, blind to supplier networks. | Supplier visibility play. |
| Modal | Serverless. Same issues as RunPod. Zac has lunch meeting. | CNAME/proxy via Datum. |
| Groq | Built 35 Equinix POPs in 6 months. Unlimited VC. Acquired by NVIDIA. Solved it. | Benchmark, not prospect. |

---

## Macro Validation: Montauk Capital "Last Millisecond" Thesis (April 2026)

Montauk Capital published a public thesis arguing the next phase of AI infrastructure value is at the edge, where inference meets action. For distributed inference to work, paths between compute locations must be deterministic. Moving inference to the edge doesn't help if the network between edge sites introduces the same variance centralized routing did  -  you've just moved the bottleneck from the DC to the middle mile.

**What this changes for our neocloud pitch:**

1. **Agentic compounding latency is the flagship DETERMINISTIC proof point.** Each inference hop adds 200ms to 2 seconds. Across a 10-step agentic workflow, that compounds into tens of seconds of cumulative lag. Layer this into scaling-wall and in-pain-now messaging for Large-Scale GPU and Tier 1 Inference sub-segments: "Training tolerates retries. Inference doesn't. Agentic workflows tolerate neither. Ten inference hops across best-effort routing compounds into seconds of delay. Deterministic paths eliminate the compounding."

2. **Sovereignty is no longer a compliance checkbox.** Montauk frames sovereignty as a first-order infrastructure requirement, not a regulatory afterthought. Strengthens our Sovereign AI Clouds positioning and the Sovereignty Stack (sovereign routing, data sovereignty, operational sovereignty).

3. **Metro-edge is the deployment model. Regional operators are the delivery mechanism.** Montauk notes Cologix's 80MW hyperscale facilities leave "sub-megawatt distributed clusters underserved." That's our colocation and fiber operator segments in one sentence  -  and it's where neocloud tenants are actually landing.

4. **Crusoe Spark is a potential dual-sale.** Montauk names Crusoe Spark specifically as modular edge compute at hundreds of kilowatts per deployment. If Crusoe Spark sites appear in regional colos where we have relationships, there's a dual-sale: MaiaEdge for the colo (fabric-in-a-box, tenant retention) and for Crusoe (deterministic paths between modular sites).

**How to use it:** The article is urgency ammunition from a capital allocator. When a prospect says "our current process works fine," the counter is: "The investment community is pricing in the shift. Operators who can't provision deterministic paths to distributed inference sites will watch revenue flow to those who can."

**Shareable:** Van Zijl's paper is shareable with prospects as an industry thesis. The MaiaEdge internal brief (`messaging rework/the-last-millisecond-maiaedge-perspective.md`) is internal only.
