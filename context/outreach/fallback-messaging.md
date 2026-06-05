# Segment Fallback Messaging

Use when research doesn't provide company-specific details for synthesis fields.

## Fiber Operator
- primary_hook: "Monetize the fiber you already have. Stand up an instant private fabric across your network over any transport  -  no routing complexity  -  and start selling services you couldn't before, including cloud on-ramp."
- core_problem: "Underutilized fiber sitting idle while the board wants revenue growth. Standing up private paths still requires routing complexity (VLAN stitching, BGP, MPLS) the ops team doesn't want to run. Multi-state deals lost to provisioning timelines. Cloud on-ramp is a product they either can't offer or offer with thin margin."
- avoid_claiming: "Don't claim internal provisioning is slow without evidence. Focus on monetization, the instant private fabric (any transport, no routing complexity), reach via partners, and new services (cloud on-ramp flagship)."
- transport_language: "Any transport: fiber (lit or dark), wave, DIA, 5G / fixed wireless, satellite. Same paths, same quality, same portal."
- no-routing language: "No VLAN stitching, no BGP, no MPLS, no SRv6, no routing protocols at all."

## Colocation Standard
- primary_hook: "Build your own fabric. Automated virtual cross-connects, a services layer you can productize, and cloud on-ramp under your brand  -  without a multi-year development project or a hyperscale facility build."
- core_problem: "Every cross-connect is still a project (LOAs, truck rolls, VLAN config) and tenants expect portal-driven self-service. Standing up a services layer in-house is multi-year development. Cloud on-ramp is either not offered or offered through an arrangement that requires a hyperscale facility build. Multi-site operators have no easy way to stitch sites together for a tenant who wants capacity in more than one."
- avoid_claiming: "Don't claim internal cross-connects are slow without evidence. Don't lead with 'losing tenants to third-party fabric providers' as a pain  -  it's not the pain most operators articulate. Focus on automated virtual cross-connects, Build your own fabric (services layer), and cloud on-ramp as a product."
- gpu_tenant_readiness_hook (add when AI corridor or announced GPU tenants are present): "GPU cloud tenants evaluate facilities on connectivity, not just space and power. A facility that can provision deterministic cross-connects from a portal in minutes is a different kind of conversation than one that can't."
- multi_site_hook (add when operator has more than one site or is building a second): "When a tenant needs capacity in more than one of your sites, today that's a separate project per site. One fabric across your sites turns that into one order."
- revenue_leakage_hook (USE SPARINGLY  -  only when no other angle lands AND research confirms a third-party fabric referral is already happening): "When a tenant ends up on a third-party fabric for cloud connectivity, the relationship starts moving to that fabric. And that fabric provider now sells GPU compute directly." // Default to the positive framing ('offer cloud on-ramp as a native product') over this one.

## Colocation AI Infrastructure
- primary_hook: "You solved power and cooling. Now make the connectivity layer match. Deterministic paths between your AI sites, automated cross-connects for GPU tenant deployments, and cloud on-ramps for GPU workloads  -  under your brand."
- core_problem: "Connectivity layer hasn't caught up to the compute investment. Best-effort networking is the uncontrolled variable in inference performance. GPU tenants expect a deterministic fabric across sites and self-service interconnection, not a project per connection."
- avoid_claiming: "Don't use standard colo messaging. This is NOT a space and power conversation. Don't make specific quantified claims about cross-connect counts or latency SLAs the tenant needs  -  those numbers vary by tenant and workload. Keep the angle broader: deterministic paths, automated interconnection, cloud on-ramp for GPU workloads."
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

- **Large-Scale GPU NeoClouds (default: scaling-wall):** Hook: "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." Lead with instant customer on-ramp + deterministic paths. If latency variance is their stated problem, switch to in-pain-now: "Every network interruption forces a checkpoint rollback. At $4,800/GPU/month, the recompute tax dwarfs our subscription."
- **Tier 1 Inference Providers (default: in-pain-now, agentic angle strong):** Hook: "Your SLA guarantees depend on network determinism you can't see today. Ten inference hops across best-effort routing compounds into seconds of delay." Lead with predictable performance + agentic compounding latency.
- **AI Infrastructure Providers (default: in-pain-now, competitive angle strong):** Hook: "Private cloud connectivity so your customers pay less for data transfer. 2c/GB on private paths vs 9c/GB over public internet  -  that's a pricing advantage you sell to win." Lead with customer on-ramp + egress competitive advantage. Note: third-party fabric providers now sell GPU compute through their own platforms, so every customer sent to their portal discovers a competitor.
- **Sovereign AI Clouds (default: in-pain-now with sovereignty framing):** Hook: "Prove data stays within geographic boundaries  -  in transit, not just at rest. Sovereign by design with every hop logged." Lead with data sovereignty + visibility. Always qualify "sovereign."
- **Crypto-to-AI Pivots (default: early-growth):** Hook: "Bitcoin doesn't care about latency. Enterprise AI tenants do. The connectivity that worked for mining doesn't survive an inference SLA." Lead with tenant-readiness + observability.

## Network Operator Track A
- primary_hook: "Sell into markets beyond your footprint. Monetize the infrastructure you already own."
- core_problem: "Internal automation stops at the network boundary. Can't sell connectivity beyond the footprint without months of LOAs."
- avoid_claiming: "NEVER claim they're slow internally. Acknowledge what they've built FIRST. Then position reach and monetization."

## Network Operator Track B
- primary_hook: "Unify internally first, then extend your reach to new markets."
- core_problem: "Multi-domain orchestration complexity even within own network. No unified path beyond the footprint."
- avoid_claiming: "Don't assume they have internal automation."

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
| None Identified | FABRIC-IN-A-BOX | "Deploy your own connectivity fabric. No protocol complexity." |

## Value Proposition by Segment
- Fiber: "Extend your reach, monetize your fiber infrastructure"
- Colocation Standard: "Instant fabric, connectivity marketplace, reach beyond your facility"
- Colocation AI Infrastructure: "Deterministic paths and cloud on-ramps for GPU workloads"
- Neocloud: "Connect distributed AI infrastructure simply. Multi-tenancy, deterministic paths, private cloud connectivity."
- Network Operator Track A: "Sell beyond your footprint. Monetize existing infrastructure." (NEVER claim they're slow)
- Network Operator Track B: "Unify internally first, then extend your reach."
- MSP: "Visibility into carriers, reach into new markets, services to sell"
