# Neocloud Strategy Brief

## Source: Datum.net Call Insights + Updated Messaging (February 2026, Confidential)

**THIS IS THE SOURCE OF TRUTH FOR ALL NEOCLOUD MESSAGING. Supersedes prior neocloud positioning.**

---

## Executive Summary

The February 2026 call with Datum.net gave us the clearest picture yet of what neoclouds actually experience. Datum is actively selling into Together.ai, Inference.net, RunPod, and Modal. Their insights aren't hypothetical. Three takeaways that change how we go to market:

1. **Our messaging hierarchy was inverted.** We've been leading with deterministic paths between GPU clusters. The actual entry point is observability and cloud on-ramp acceleration. Neoclouds don't know they have a network problem. They know they're slow. Lead with "see why you're slow," not "make your paths predictable."

2. **Datum is a channel partner, not just a customer.** They solve Layer 7 (proxy, anycast, DDoS). We solve Layer 2/3 (paths, observability, encryption). Together we're the full-stack answer. Zac Smith has direct relationships with decision-makers at every Tier 1 neocloud. GTC in March is the next action.

3. **Neocloud end customers are a new TAM.** Companies spending $50K+/mo on GPU compute are in pain: slow training, expensive egress, inconsistent inference. They don't deploy MaiaEdge, but they create demand for it. Different message, different timeline.

---

## Datum.net Context

**Who:** Virtual telco. 18 Equinix POPs via partner NetActuate, scaling to 40+. Cloudflare-like anycast proxy architecture for neocloud and enterprise traffic.

**Key people:**
- Zac Smith (CEO) — former CEO of Packet (acquired by Equinix). Personally connected to leadership at Together.ai, Inference.net, RunPod, Modal, and Groq. Board member at Koya (now Mistral).
- Drew Raines — technical lead
- Brett Mertens — BD, source of most pain articulation
- Manish Singh — engineering
- Shelby Lindsey — joining from Equinix to run Datum backbone

**Partnership model:** Datum = Layer 7 (proxy, anycast, DDoS). MaiaEdge = Layer 2/3 (paths, observability, encryption). Full-stack answer together.

---

## What We Were Getting Wrong

| We Assumed | Reality |
|---|---|
| Primary pain is inference latency between GPU clusters | Primary entry is data movement from object storage + observability. Inference latency is end-state value, not the door opener. |
| Neoclouds know they have a network problem | Most don't. They know they're slow. They have no tooling to diagnose it. |
| All neoclouds have the same pain | Four distinct sub-segments with different operational models and different entry points. |
| End customers aren't our TAM | $50K+/mo neocloud customers are a demand creation opportunity. |

---

## The Three-Layer Pain

| Pain | What's Happening | MaiaEdge Fix |
|---|---|---|
| Too Slow | Data transfer from S3/GCP/Azure to remote GPU clusters over public internet. Training runs that should take hours take days. Can't diagnose why. | Private cloud on-ramps via Equinix Fabric / Megaport API. Deterministic paths eliminate variable latency. |
| Too Expensive | Public internet egress at $0.05-0.09/GB. Direct Connect costs $0.02/GB. Most neoclouds don't know Direct Connect exists. | Automated Direct Connect provisioning. 60-80% egress cost reduction. |
| Invisible | Zero network observability. No tools to see if the problem is a saturated switch, bad transit route, or MTU issue. | End-to-end hop-by-hop telemetry across paths the neocloud doesn't own. |

---

## Updated Messaging Hierarchy

**Lead with symptoms they recognize, not infrastructure they don't understand.**

| # | Message | Why It Resonates | MaiaEdge Capability |
|---|---|---|---|
| 1 | See why you're slow. End-to-end visibility across paths you don't own. | Meets them where they are. They know they're slow, can't diagnose it. | Hop-by-hop telemetry, per-path metrics, JSON API. |
| 2 | Move data faster and cheaper. Private paths into AWS/Azure/GCP. Cut egress 60-80%. | Object storage to GPU cluster is THE use case. Egress savings are tangible. | Equinix Fabric / Megaport API integration. Direct Connect automation. |
| 3 | Groq-quality networking without the Groq budget. Deterministic paths, controlled latency. | Every neocloud wants what Groq built. Nobody can afford to replicate it. | PCE path computation, stateless forwarding, line-rate encryption. |
| 4 | Every new facility online in minutes. Unified fabric across any colo. | Scaling from 5 to 30 facilities means 25 connectivity projects. Or one. | Federation, instant NNI, zero-touch provisioning. |

---

## Core Value Proposition (Neocloud)

Your GPU clusters are scattered across facilities you don't control, connected by networks you can't see. MaiaEdge gives you end-to-end visibility, private cloud on-ramps that cut egress costs 60-80%, and deterministic paths that eliminate the network as a variable in inference performance. No network team required. Same team that built Acme Packet.

---

## By Persona

| Persona | Lead With | Avoid |
|---|---|---|
| CEO / Founder | Competitive positioning. Groq built 35 POPs. You need the same result without the budget. Doesn't require a network team. | Technical architecture. Protocol details. Anything that sounds like a project. |
| CTO / VP Eng | Inference latency has a 15-40ms network component nobody measures. Deterministic paths + hop-by-hop telemetry. | Revenue metrics. Business strategy framing. |
| VP Infrastructure | Every new facility is a multi-week project. Your team provisions paths in minutes. Same connectivity at any colo. | Strategic vision. Stay operational. |
| Head of Platform | SLAs depend on network predictability you can't control. Private paths = predictable performance regardless of facility. | Infrastructure details. Keep it about outcomes. |
| CFO / Finance | Egress at $0.05-0.09/GB vs $0.02/GB via private paths. For training runs moving TBs, 60-80% savings. OpEx, no CapEx. | Technical anything. Keep it about dollars. |

---

## Neocloud Sub-Segments

The unified message applies to all neoclouds. Sub-segment determines which priority you lead with and how much networking sophistication you assume.

| Sub-Segment | Examples | Situation | Entry Point | Don't |
|---|---|---|---|---|
| Tier 1 Inference | Together.ai, Inference.net, Fireworks, Baseten | 5-30+ facilities. Had or lost a network person. Object storage data movement is biggest pain. | Observability + cloud on-ramp. "See why your data pipeline is slow." | Don't assume they have a team to evaluate architecture. |
| Serverless GPU | RunPod, Modal, Vast.ai, SaladCloud | Marketplace. 15+ suppliers in random facilities. On hook for SLA, blind to supplier network. | Supplier visibility. "Stop taking blame for problems you can't see." | Don't use operator language. They're asset-light. |
| Crypto-to-AI | Applied Digital, Hut 8, TeraWulf, Bitdeer | Former miners. Have power/space. Terrible connectivity. Enterprise switches, single uplinks. | Basic connectivity + observability. "Bitcoin doesn't care about latency. AI does." | Don't be condescending. Don't assume networking terms. |
| Large-Scale GPU | CoreWeave, Lambda, Crusoe, Voltage Park | $1B+ valuations. Building network teams. 30+ facilities. Sophisticated. | Cross-carrier orchestration. "Infrastructure your network team needs." | Don't oversimplify. We're tooling, not team. |

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
| Multi-Cloud | Head of Platform | Data in S3, models on CoreWeave, serving from GCP. Every hop is public internet. | "Open to talking unified connectivity?" |

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

| Sub-Segment | Our List | Est. TAM | Coverage |
|---|---|---|---|
| Tier 1 Inference | 15-20 | 20-25 | 75-85% |
| Large-Scale GPU Cloud | 15-20 | 25-30 | 60-70% |
| Crypto-to-AI Pivots | 11 | 20-25 | ~50% |
| Serverless / Inference-as-a-Service | 10-12 | 25-35 | 35-45% |
| GPU Marketplaces / Aggregators | 8-10 | 15-20 | ~50% |
| Sovereign AI / Telco GPU Clouds | 8-10 | 30-40 | ~25% |
| AI Chip + Cloud | 8-10 | 10-15 | ~65% |
| Regional / Emerging Market | 20-25 | 50-70 | ~35% |

---

## Discovery Signals for Finding Missing Companies

1. **NVIDIA GPU Allocation Announcements** — Single best leading indicator. Monitor newsroom, GTC keynotes, regional AI factory announcements.
2. **Crypto Mining Pivot Announcements** — SEC filings (10-K pivot language), hyperscaler lease announcements, WGMI ETF holdings. Watch: Applied Digital, Galaxy Digital, Stronghold, Argo, Mawson, Northern Data Group, Cathedra Bitcoin, Soluna.
3. **Venture Capital / Growth Equity Rounds** — Crunchbase/PitchBook: 'GPU cloud', 'AI infrastructure', 'inference platform'. Any Series A+ is a potential target.
4. **Sovereign AI National Initiatives** — Canada ($2B), India ($1.25B), EU AI Factories (13+ sites), Saudi Arabia (HUMAIN), UAE (Core42/Stargate), South Korea, Japan.
5. **AI Colocation Tenant Lists** — Our colo segment is a direct feeder. Every colo conversation should generate neocloud intelligence.
6. **Industry Trackers** — SemiAnalysis ClusterMAX, Neocloud.world, CoinShares Mining Reports, NVIDIA Newsroom, DataCentre Magazine.
7. **Conference Intelligence** — NVIDIA GTC, OCP Global Summit, SC/Supercomputing, AI Infrastructure Day, Data Centre World.

---

## Specific Intelligence (Datum-sourced, requires Ziemer/Abilash approval before actioning)

| Company | Intel | Implication |
|---|---|---|
| Together.ai | Network person quit. Biggest pain is data movement from object stores. Zac has direct relationship. | Highest-priority warm intro via Datum. |
| Inference.net | Same data movement problem. Zac has direct relationship. | Second warm intro. |
| RunPod | 200K+ users. 15+ GPU suppliers in random facilities. On hook for SLA, blind to supplier networks. | Supplier visibility play. |
| Modal | Serverless. Same issues as RunPod. Zac has lunch meeting. | CNAME/proxy via Datum. |
| Groq | Built 35 Equinix POPs in 6 months. Unlimited VC. Acquired by NVIDIA. Solved it. | Benchmark, not prospect. |
