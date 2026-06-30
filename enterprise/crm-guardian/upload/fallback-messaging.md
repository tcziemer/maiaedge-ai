# Segment Fallback Messaging

Use when research doesn't provide company-specific details for synthesis fields.

> ## ⚠ STRUCTURE EXEMPLARS, NOT SEND COPY (2026-06-12)
>
> Every template below defines the ARGUMENT (lead positioning, what to avoid claiming) — never the wording. **Paraphrase every sentence; no phrase longer than 6 words may ship verbatim.** The May 2026 "The version that works/compounds…" skeleton shipped word-for-word from this file 9+ times and became the campaign's template fingerprint; the Batch Fingerprint Gate (email-writing-rules.md) now fails any batch where two emails share a sentence from this file.
>
> When converting a block to send copy, apply the **craft structure** (email-writing-rules.md § Craft Voice): structural truth of their world → craft line ("that leg is the layer I work on" + one concrete mechanic) → show-me give → soft call-ask statement. The blocks below supply the segment's ARGUMENT for slot 1 and the mechanics for slot 2. Worked conversion: the Fiber E1 below.

## Fiber Operator (Sidecar §4.4)

**Lead positioning:** Activation-velocity gap. Service Assurance is a secondary E2 angle, NOT the E1 lead.

**Sub-segment routing:** Default for Regional CLEC, Long Haul / Backbone, and Dark Fiber Specialist sub-segments. For Municipal / Co-op / Consortium accounts, see `context/segments/fiber-operator.md` § Fiber Sub-Segments - the federation-ready angle leads instead.

### E1 — ARGUMENT (activation velocity) + worked craft conversion

**The argument:** the revenue gap isn't route miles, it's activation — NNIs take weeks, dark strands depreciate unlit, multi-state deals walk to whoever provisions faster.

**Worked craft conversion (imitate the moves, paraphrase the words):**

> [First name],
>
> Nobody in your seat loses deals on route miles anymore, you lose them on the activation clock, since the cross-carrier leg still turns up at someone else's pace while the dark strands sit there depreciating. That leg is the layer I work on, the same services going sellable same-day on paths your team turns up itself.
>
> Fifteen minutes and I can show you a path coming up end to end. Happy to set up time if it's worth seeing.

*(Legacy template retired 2026-06-12: "The version that compounds is…" shipped verbatim 9+ times in May 2026 and is now a fingerprint-gate failure.)*

### E2 (53 words)

> [First name],
>
> Wholesale customers buy on price and speed now, and since price is competitive across the market, speed is the only place you can actually pull ahead. The customer notices when one operator turns it up in days and another quotes weeks, and the same-day operators are taking the multi-carrier deals.
>
> On your radar?

### E3 (2 sentences — must carry ONE actionable ask; zero-ask closers banned)

> [First name],
>
> Reached out because the activation-clock problem felt close to what you're building. Worth a conversation, or wrong moment?

### Supporting fields

- primary_hook: "The revenue gap on most fiber networks isn't more route miles in the ground. It's on the activation side. NNIs that take weeks to turn up, dark strands depreciating every day they're unlit, multi-state deals walking to whoever can provision faster. The fix is infrastructure that turns underutilized fiber into instantly sellable, deterministic services under your brand."
- core_problem: "Underutilized fiber sitting idle while the board wants revenue growth. Standing up cross-carrier paths still takes weeks of LOAs, BGP config, VLAN coordination. Multi-state deals walking to whoever can provision faster. Cloud on-ramp is a product they either can't offer or offer with thin margin."
- avoid_claiming: "Don't claim internal provisioning is slow without evidence. Focus on activation velocity (NNIs in minutes, not weeks), monetization of dark / underutilized fiber, multi-state-deal speed, and new services (cloud on-ramp flagship). Service Assurance is a SECONDARY E2 angle - don't lead with it on E1."
- transport_language: "Any transport: fiber (lit or dark), wave, DIA, 5G / fixed wireless, satellite. Same paths, same quality, same portal."
- no-routing language: "No VLAN stitching, no BGP, no MPLS, no SRv6, no routing protocols at all."
- service_assurance_e2_angle (supporting only, NOT E1 lead): "Type 2 circuits stop being a black hole. Hop-by-hop telemetry across circuits you don't own. SLA compliance you can prove on the first call."

## Colocation Standard (no confirmed AI signals - Sidecar §4.1.A)

**Sub-segment routing:** Use this block when no STRONG AI signals are present. STRONG AI signals (confirmed GPU cloud tenants like Lambda / Crusoe / Nebius, liquid cooling deployment, 30kW+ racks per `context/partner-assets/cheatsheet-colocation.md` § AI Signal Detection) route to the **Colocation AI Infrastructure** block below.

### E1 (71 words, Sidecar §4.1.A)

> [First name],
>
> Saw [public signal - DCD attendance, new facility announcement, expansion press].
>
> What separates a colo from a landlord is the interconnection attach rate, and the operators pulling ahead are the ones layering cloud on-ramps, multi-site reach, and self-service interconnection on top of space and power, so they turn up new services under their own brand without a multi-year build. The fix is infrastructure that adds that layer in weeks, with no routing protocols to run.
>
> Worth a quick conversation?

### E2 (44 words, Sidecar §4.1)

> [First name],
>
> The colos staying ahead on AI tenants aren't the ones with the densest power, they're the ones whose tenants can reach cloud and GPU compute without leaving the building, so the interconnection layer is what's actually doing the differentiating.
>
> Open to a quick conversation?

### E3 (2 sentences, Sidecar §4.1 — must carry ONE actionable ask; zero-ask closers banned)

> [First name],
>
> Sounds like the timing might be off, or the angle missed the mark. Worth a conversation, or wrong moment?

### Supporting fields

- primary_hook: "Interconnection attach rate is what separates colos from being landlords. Cloud on-ramps, multi-site reach, and self-service interconnection layered on top of space and power, under your brand, without a multi-year build."
- core_problem: "Every cross-connect is still a project (LOAs, truck rolls, VLAN config) and tenants expect portal-driven self-service. Standing up a services layer in-house is multi-year development. Cloud on-ramp is either not offered or offered through an arrangement that requires a hyperscale facility build. Multi-site operators have no easy way to stitch sites together for a tenant who wants capacity in more than one."
- avoid_claiming: "Don't claim internal cross-connects are slow without evidence. Don't lead with 'losing tenants to third-party fabric providers' as a pain  -  it's not the pain most operators articulate. Don't use 'fabric-in-a-box' in cold body (banned per email-writing-rules.md - cheatsheet/live-conversation language only). Focus on the interconnection-attach-rate-vs-landlord frame and the layered services on top of space and power."
- multi_site_hook (add when operator has more than one site or is building a second): "When a tenant needs capacity in more than one of your sites, today that's a separate project per site. One fabric across your sites turns that into one order."
- revenue_leakage_hook (USE SPARINGLY  -  only when no other angle lands AND research confirms a third-party fabric referral is already happening): "When a tenant ends up on a third-party fabric for cloud connectivity, the relationship starts moving to that fabric. And that fabric provider now sells GPU compute directly." // Default to the positive framing ('offer cloud on-ramp as a native product') over this one.

## Colocation AI Infrastructure (Sidecar §4.1.B)

**Sub-segment routing:** Use this block when STRONG AI signals are confirmed: GPU cloud tenants like Lambda / Crusoe / Nebius announced, liquid cooling deployment, 30kW+ racks. See `context/partner-assets/cheatsheet-colocation.md` § AI Signal Detection.

### E1 (71 words, Sidecar §4.1.B)

> [First name],
>
> Saw [public signal - Lambda / Crusoe / Nebius tenant announcement, liquid cooling deployment, 30kW+ rack buildout].
>
> You've put the spend into liquid cooling and high-density power, so as the AI tenants come on they start asking for deterministic paths between GPU clusters and cloud on-ramps that match it, and best-effort networking is usually the one line on the bill of materials that hasn't caught up. The fix is deterministic Ethernet paths between your sites with hop-by-hop visibility, no routing complexity.
>
> Worth a quick conversation?

### E2 (44 words, shared with Standard Colo per Sidecar §4.1)

> [First name],
>
> The colos staying ahead on AI tenants aren't the ones with the densest power, they're the ones whose tenants can reach cloud and GPU compute without leaving the building, so the interconnection layer is what's actually doing the differentiating.
>
> Open to a quick conversation?

### E3 (2 sentences — must carry ONE actionable ask)

> [First name],
>
> Sounds like the timing might be off, or the angle missed the mark. Worth a look, or should I move on?

### Supporting fields

- primary_hook: "You've invested in liquid cooling and high-density power. Your AI tenants are now asking for deterministic paths between GPU clusters and cloud on-ramps that match the power and cooling spend. The connectivity layer is the gap on the bill of materials."
- core_problem: "Connectivity layer hasn't caught up to the compute investment. Best-effort networking is the uncontrolled variable in inference performance. GPU tenants expect a deterministic fabric across sites and self-service interconnection, not a project per connection."
- avoid_claiming: "Don't use standard colo messaging. This is NOT a space and power conversation. Don't make specific quantified claims about cross-connect counts or latency SLAs the tenant needs  -  those numbers vary by tenant and workload. Don't use 'fabric-in-a-box' in cold body (banned per email-writing-rules.md). Keep the angle broader: deterministic paths between GPU clusters, automated interconnection, cloud on-ramp for GPU workloads."
- cold_cto_hook: "GPU tenants need deterministic paths and fast interconnection. Best-effort breaks inference. The compute investment is massive; the connectivity gap is where the SLA breaks."
- category_positioning (live-only, CEO/VP Sales, discovery calls and proposals  -  NOT cold email): "You built the cooling and the power density. Your GPU tenants' enterprise customers will choose the facility that provisions private paths in minutes. That connectivity layer is yours to own or someone else's to capture."

### Modular DC Variant (Nodiac, Colony Compute, containerized-capacity-at-power-sites)
- primary_hook: "Every new pod at a new power site is either a separate networking project or a day-one join to your fabric. MaiaEdge makes it the second one."
- core_problem: "Scaling by adding modular sites at partner power locations. Each new pod is an opportunity for a separate networking lift. GPU tenants expect a deterministic fabric across every pod, not per-pod connectivity."
- avoid_claiming: "Don't describe them as a neocloud. They sell space and power to GPU tenants, not compute. Use AI colo messaging with the modular distribution angle."

### Greenfield Colo Variant
- research_first: "Read their plans before you write. AI-ready build (liquid cooling / high-density power / announced GPU tenants / 'AI campus' language) = use AI Colo messaging. Standard build = use Standard Colo messaging. The difference matters."
- ai_ready_hook: "Build the connectivity layer alongside the compute layer. Second site onward, it's one fabric across all of them  -  not N separate networking projects."
- standard_hook: "Build your own fabric from day one. Automated virtual cross-connects and cloud on-ramp as native products  -  without the multi-year development project."
- shared_hook (both variants): "The day your second site comes online, it joins the same fabric as your first. Tenants who want capacity in both get one interconnection order, not two."

## Neocloud
- primary_hook (angle-agnostic default): "One device. Instant private fabric between your AI sites." (Master pitch: connecting distributed AI infrastructure simply.)
- core_problem: "Distributed AI infrastructure without visibility, predictable performance, or simple customer onboarding. Compute companies that don't want to become networking companies."
- avoid_claiming: "They ARE the customer. NEVER use operator sovereignty language ('keep your customer,' 'your portal, your invoice'). DATA sovereignty ('sovereign by design,' 'paths you control') IS allowed. No network jargon (VLAN, Q-in-Q, BGP). Always qualify 'sovereign'  -  never use it bare in writing."

### Neocloud Angle Selection (Research-Driven)

Two angles, selected by maturity + customer mix. Same product, different door:

- **In-pain-now** (mid-growth, 5-15 sites, latency variance dominant, network person lost or never had one): Lead with observability under the DETERMINISTIC pillar. "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between."
- **Scaling-wall** (scale, 15+ sites, hyperscaler-heavy 80%+, building network team, enterprise ramp in growth plan): Lead with INSTANT (customer-onboarding velocity). "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will."
- **Early-growth / crypto-to-AI** (2-5 sites, basic connectivity still being figured out): Lead with tenant-readiness. "Bitcoin doesn't care about latency. Enterprise AI tenants do. The connectivity that worked for mining doesn't survive an inference SLA."

### Neocloud Sub-Segment Fallbacks

- **`Large Scale GPU - Neocloud` (default: scaling-wall):** Hook: "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." Lead with instant customer on-ramp + deterministic paths. If latency variance is their stated problem, switch to in-pain-now: "Every network interruption forces a checkpoint rollback. At $4,800/GPU/month, the recompute tax dwarfs our subscription."
- **`Tier 1 Inference - Neocloud` (default: in-pain-now, agentic angle strong):** Hook: "Your SLA guarantees depend on network determinism you can't see today. Ten inference hops across best-effort routing compounds into seconds of delay." Lead with predictable performance + agentic compounding latency.
- **`AI Infrastructure providers - Neocloud` (default: in-pain-now, competitive angle strong):** Hook: "Private cloud connectivity so your customers pay less for data transfer. 2c/GB on private paths vs 9c/GB over public internet, and that's a pricing advantage you sell to win." Lead with customer on-ramp + egress competitive advantage. Note: third-party fabric providers now sell GPU compute through their own platforms, so every customer sent to their portal discovers a competitor.
- **`Sovereign AI Clouds - Neocloud` (default: in-pain-now with sovereignty framing):** Hook: "Prove data stays within geographic boundaries  -  in transit, not just at rest. Sovereign by design with every hop logged." Lead with data sovereignty + visibility. Always qualify "sovereign."
- **`Crypto to AI - Neoclouds` (default: early-growth; inclusive of operator AND landlord per Cooper 2026-05-14):** Hook: "Bitcoin doesn't care about latency. Enterprise AI tenants do. The connectivity that worked for mining doesn't survive an inference SLA." Lead with tenant-readiness + observability.

## Network Operator - Tier 1 Global / Tier 1 National (Track A - Sidecar §4.2)

**Tier definition (for messaging purposes):**
- **Tier 1 Global** ($10B+ public): AT&T, Verizon, Lumen, NTT, BT, Deutsche Telekom, Orange, PCCW Global, Tata Communications.
- **Tier 1 National** ($1-10B with own backbone): national-footprint carriers with their own wholesale-product organizations and PCE-class internal automation.

For Tier 2/3 Regional Wholesale ($500M-$1B) and below, see the Tier 2/3 block below.

**Track assumption:** This template assumes Track A (operator has internal automation, the dominant case among Tier 1 carriers). The opener "The hard part isn't the core" carries the mandatory Track A acknowledgment. For confirmed Track B Tier 1 accounts (research shows fragmented internal automation across regions or acquired businesses, no public evidence of automation product), use the Track B block below.

### E1 (70 words, Sidecar §4.2)

> [First name],
>
> Saw [public signal - tower expansion, mobile-backhaul announcement, transport partnership, wholesale product launch, BEAD subgrant].
>
> The hard part isn't the core, it's extending L2 services to every endpoint you serve when the transport between you and that endpoint isn't always yours, so tower backhaul, enterprise drops, and partner last-mile each end up with their own provisioning and visibility process. The fix is infrastructure that extends deterministic L2 services across any transport, with the same provisioning you already get on-net.
>
> Worth a conversation?

### E2 (44 words, Sidecar §4.2)

> [First name],
>
> Enterprise customers expect AWS-like speed no matter which transport carries their traffic, so the Tier 1s taking enterprise share right now are the ones extending on-net L2 services across mixed transport with the same provisioning. Same asset base, less per-transport complexity.
>
> On your radar?

### E3 (2 sentences)

> [First name],
>
> Sounds like the timing might be off for this planning cycle. Worth a conversation when it opens, or wrong problem?

### Supporting fields

- primary_hook: "The hard part isn't the core. It's extending L2 services to every endpoint you serve when the transport between you and the endpoint isn't always yours. Tower backhaul, enterprise customer drops, partner-network last-mile."
- core_problem: "Internal automation is real for on-net traffic. But every endpoint not on their own fiber requires a different transport (tower backhaul fiber/microwave, enterprise drop, partner-network last-mile), and each transport type has a separate provisioning, configuration, and visibility process."
- avoid_claiming: "NEVER claim they're slow internally. Acknowledge what they've built FIRST via 'The hard part isn't the core.' Then position the per-transport boundary pain. Don't lead with 'reach' - that's Tier 2/3 framing. The Tier 1 lead is L2 services across mixed transport they don't fully own."

## Network Operator - Tier 2/3 Regional Wholesale (extend-reach framing - existing)

### E1 (72 words, extend-reach framing)

> [First name],
>
> Saw [public signal - expansion announcement, new market lit, wholesale partnership, BEAD subgrant].
>
> Internal automation works fine on-net, but the moment a customer needs a path beyond your own footprint you're back to LOAs and BGP sessions, so the 60-day cross-carrier clock tends to be where the multi-state and adjacent-market deals quietly slip away to whoever can turn them up faster. The fix is infrastructure that extends that same on-net provisioning speed to off-net paths through standards-aligned partner activation.
>
> Worth a conversation?

### E2 (46 words)

> [First name],
>
> Enterprise customers compare regional carriers to AWS now, and "depends on the carrier" is the answer that loses the deal. The operators taking enterprise share extend on-net provisioning speed to off-net paths through standards-aligned partner activation, with the same monitoring stack across both.
>
> On your radar?

### E3 (2 sentences)

> [First name],
>
> Sounds like the timing might be off for this planning cycle. Worth me staying in touch on this, or should I move on?

### Supporting fields

- primary_hook: "Sell into markets beyond your footprint. Monetize the infrastructure you already own."
- core_problem: "Internal automation may work on-net but every customer beyond the footprint is months of LOAs and BGP sessions. Enterprise customers expect AWS-like speed regardless of whose carrier carries the path."
- avoid_claiming: "Acknowledge what they've built first. Don't lead with 'extending L2 services across mixed transport' - that's the Tier 1 frame. Tier 2/3 lead is reach: how to sell into markets beyond their own footprint."

## Network Operator - Track B (any tier, confirmed fragmented internal automation)
- primary_hook: "Unify internally first, then extend your reach to new markets."
- core_problem: "Multi-domain orchestration complexity even within own network. No unified path beyond the footprint."
- avoid_claiming: "Don't assume they have internal automation. Use only when research shows no public evidence of portal/API automation product."

## Enterprise (Multi-DC ICP) Playbook

**Status as of 2026-05-11:** Enterprise was promoted to ICP on 2026-05-11. The cheatsheet, signals catalog, and Worldpay call validation are in place. **This is the launch playbook.** Zero Enterprise cold emails had shipped before this rollout.

**Pilot batch direction:** Financial Services + Outsourcing Services sub-segments first, 50-80 contacts, M&A network integration anchor. Healthcare Systems and Retail/Distribution sub-segments are batch 2.

**Vocabulary lock (mandatory, more critical here than any other segment):**
- **BANNED in Enterprise cold body** (these signal the wrong business model - enterprises don't resell connectivity): "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "wholesale activation," "extend reach to new markets," "tenant," "meet-me room," "interconnection revenue," "aggregator," "TSD," "fabric-in-a-box," "Federation" as a verb.
- **ALLOWED in Enterprise cold body:** data center, DC, DR site, dark fiber redundancy, diverse paths, fiber pair, hot-standby, active-active, cloud on-ramp, direct connect, multi-cloud, your network, audit trail, deterministic paths between data centers, hop-by-hop visibility, "policy-based path control," "paths you can prove."
- **HIPAA / PCI-DSS / SOX / GDPR / HITRUST** mentions are appropriate when the buyer's persona (CISO, Compliance, regulated-vertical CIO) implies regulatory exposure.

### E1 - Dark Fiber Redundancy Anchor (70 words, default for Retail/Distribution and Healthcare; also works for FS/OS)

> [First name],
>
> Saw [public signal - recent acquisition, DR site addition, new DC announcement, sovereignty/compliance announcement].
>
> Most multi-DC enterprises pay for dark fiber between their primary sites, but a lot of the time that comes down to a single pair, so the redundancy holds on the architecture diagram and not under load. The fix is running diverse fibers into a fabric layer with automated failover, plus hop-by-hop visibility on every path including the carrier circuits you don't own.
>
> Open to a quick conversation?

### E1 alt - M&A Anchor (70 words, default for Financial Services + Outsourcing Services)

> [First name],
>
> Saw [public signal - recent acquisition, divestiture, integration milestone].
>
> Every M&A event in your industry turns into a network integration project, since connecting two existing DC footprints, the legacy MPLS, and the cloud on-ramps without dropping service tends to become an 18-month effort by default. The fix is infrastructure that compresses that, with one fabric across both footprints, deterministic paths to cloud, and hop-by-hop visibility on every leg.
>
> Worth a few minutes on what compresses that?

### E2 - DR / Multi-Cloud Angle (54 words, secondary to E1 Dark Fiber Redundancy)

> [First name],
>
> Multi-cloud sounds clean on the architecture diagram, but in practice it's three different on-ramp models, three monitoring stacks, three blast radii. The fix is one fabric across all of them under your team's control, so you get the same visibility, policy, and failover behavior on every cloud you reach.
>
> Open to a quick walkthrough?

### E3 (2 sentences)

> [First name],
>
> Sounds like the timing might be off. Worth a conversation as you plan next year, or wrong moment?

### Supporting fields

- primary_hook (dark-fiber default): "Most multi-DC enterprises pay for dark fiber between their primary sites, and most of that fiber is one cut away from an outage. The fix is diverse fibers into a fabric layer with automated failover, plus hop-by-hop visibility on every path including the carrier circuits you don't own."
- primary_hook (M&A alt for FS/OS): "Every M&A event creates a network integration project. Two existing DC footprints, legacy MPLS, cloud on-ramps. The fix is one fabric across all of it, deterministic paths to cloud, hop-by-hop visibility."
- core_problem: "Dark fiber between primary DCs is fragile (single fiber pair = single cut away from outage). DR sites have stale routing protocols and undertested failover. Multi-cloud connectivity is three different on-ramp models, three monitoring stacks, three blast radii. Compliance can't prove the path. M&A network integration turns into 18-month efforts."
- avoid_claiming: "Enterprises are NOT operators. Don't pitch operator-monetization language. Don't pitch 'extend reach to new markets' - they don't have markets, they have a network. Don't use 'tenant,' 'meet-me room,' 'fabric-in-a-box,' 'wholesale activation,' or 'Federation'-as-a-verb. The cheatsheet vocabulary lock is the most important guardrail in this playbook."
- persona_specific_notes:
  - **CIO / CTO:** lead with multi-cloud / cloud on-ramp / competitive framing.
  - **VP Network Infrastructure / Director Network Engineering:** lead with operational burden ("no headcount to run BGP across the WAN," "every new DC is a six-month networking project").
  - **CSO / CISO / Compliance:** lead with audit-trail / data-sovereignty framing. HIPAA / PCI-DSS / SOX / GDPR appropriate.
  - **Network Architect / Principal Network Engineer:** lead with technical specificity ("HAsync and HAfabric on the SSRs share a single fiber pair," "Type 2 is a black hole").
- ab_test_alignment: First Enterprise A/B test (Sidecar §5 #4) compares M&A anchor vs dark-fiber-redundancy anchor head-to-head within FS/OS sub-segments. See `context/copy-strategy/ab-test-plan.md`.

## MSP/Aggregator
- primary_hook: "You own the customer relationship. We give you visibility into everything behind it, reach into new markets, and services to sell."
- core_problem: "Blind to what happens inside carrier networks. Responsible for SLA but can't see the path. Limited to whatever markets your carriers cover."
- avoid_claiming: "Don't claim they have infrastructure issues. They're asset-light by design."

## Messaging Angles by Provisioning Approach

| Their Approach | Angle | Positioning |
|---|---|---|
| Megaport/PacketFabric | OWNERSHIP | "Why rent when you could own? Keep margin, brand, roadmap control." |
| Lumen PCF | INDEPENDENCE | "Own your fabric instead of renting theirs. Same capability, your control." |
| Homegrown Platform | REACH | "Extend your platform beyond your network. Reach new markets instantly." |
| Standard OSS/BSS | MISSING LAYER | "Add what your OSS can't provide. Instant private path provisioning." |
| Manual/Legacy | SPEED | "Stop waiting 60-90 days. Provision private paths in minutes, not months." |
| None Identified | BUILD-YOUR-OWN | "Build your own interconnection layer. Deterministic paths, no routing protocols." (Note: "fabric-in-a-box" is cheatsheet/live-conversation language only - banned in cold body per email-writing-rules.md.) |

## Value Proposition by Segment
- Fiber: "Activation velocity, monetize the fiber you already own"
- Colocation Standard: "Interconnection layer that separates you from being a landlord. Cloud on-ramps, multi-site reach, self-service interconnection on top of space and power."
- Colocation AI Infrastructure: "Deterministic paths between GPU clusters and cloud on-ramps that match the power and cooling spend"
- Neocloud: "Connect distributed AI infrastructure simply. Multi-tenancy, deterministic paths, private cloud connectivity."
- Network Operator Tier 1 (Global + National, Track A): "Extend L2 services across mixed transport you don't own - tower backhaul, partner last-mile, enterprise drops - with the same provisioning as on-net." (NEVER claim they're slow internally)
- Network Operator Tier 2/3 Regional Wholesale: "Sell beyond your footprint. Monetize existing infrastructure."
- Network Operator Track B (any tier, fragmented internal automation): "Unify internally first, then extend your reach."
- MSP: "Visibility into carriers, reach into new markets, services to sell"
- Enterprise (Multi-DC ICP, Financial Services + Outsourcing Services pilot): "M&A network integration that compresses the 18-month default into one fabric." (E1 alt anchor.) Default E1 for Retail/Distribution + Healthcare: dark fiber redundancy that is actually redundant.
