# Segment Fallback Messaging

Use when research doesn't provide company-specific details for synthesis fields.

## Colocation Standard
- primary_hook: "Build your own fabric rather than joining someone else's. You keep the customer, the margin, the control."
- core_problem: "6+ week cross-connect provisioning. Losing tenants to third-party fabric providers."
- avoid_claiming: "Don't claim internal cross-connects are slow without evidence. Focus on EXTERNAL paths."

## Colocation AI Infrastructure
- primary_hook: "Deterministic intelligence delivery. Make the network predictable so inference systems can do their job."
- core_problem: "Best-effort networking breaks inference performance. Token-by-token generation is latency-sensitive."
- avoid_claiming: "Don't use standard colo messaging. Focus on deterministic paths and inference requirements."

## Neocloud
- primary_hook: "See why you're slow. Then fix it."
- core_problem: "Zero visibility into why things are slow. No WAN monitoring, no path visibility, no hop-by-hop telemetry. Compute companies that accidentally became networking companies."
- avoid_claiming: "They ARE the customer. NEVER use 'keep your customer' language. Lead with observability, NOT deterministic paths. Deterministic paths is message #3, not #1."

### Neocloud Sub-Segment Fallbacks
- **Large-Scale GPU NeoClouds:** Hook: "Every network interruption forces a checkpoint rollback. At $4,800/GPU/month, the recompute tax dwarfs our subscription." Lead with all three layers.
- **Tier 1 Inference Providers:** Hook: "Your SLA guarantees depend on network determinism you can't see today. Tail latency kills inference." Lead with observability + deterministic paths.
- **AI Infrastructure Providers:** Hook: "See why inference latency varies by facility. Own your paths — don't rent Megaport's." Lead with cloud on-ramp + observability. Note Megaport/Latitude.sh threat.
- **Sovereign AI Clouds:** Hook: "Prove data stays within geographic boundaries. Sovereign routing with compliance reporting." Lead with sovereign routing + observability.
- **Crypto-to-AI Pivots:** Hook: "Your crypto infrastructure wasn't built for AI traffic. See where the network is slowing you down." Lead with observability.

## Fiber Operator
- primary_hook: "Every multi-state deal you lose to provisioning delays is margin walking out the door."
- core_problem: "NNI provisioning takes weeks. Losing multi-state deals to whoever's faster. 30-70% stranded dark fiber."
- avoid_claiming: "Don't claim internal provisioning is slow without evidence. Focus on cross-carrier NNI delays."

## Network Operator Track A
- primary_hook: "You've automated internally. MaiaEdge extends that automation everywhere else."
- core_problem: "Internal automation stops at domain boundaries. Cross-carrier paths still take weeks."
- avoid_claiming: "NEVER claim they're slow internally. Acknowledge what they've built FIRST."

## Network Operator Track B
- primary_hook: "Unify internally first, then extend externally. One infrastructure for both."
- core_problem: "Multi-domain orchestration complexity even within your own network."
- avoid_claiming: "Don't assume they have internal automation."

## MSP/Aggregator
- primary_hook: "You own the customer relationship. We give you visibility into everything behind it."
- core_problem: "Blind to what happens inside carrier networks. Responsible for SLA but can't see the path."
- avoid_claiming: "Don't claim they have infrastructure issues. They're asset-light by design."

## Messaging Angles by Provisioning Approach

| Their Approach | Angle | Positioning |
|---|---|---|
| Megaport/PacketFabric | OWNERSHIP | "Why rent when you could own? Keep margin, brand, roadmap control." |
| Lumen PCF | INDEPENDENCE | "Own your fabric instead of renting theirs. Same capability, your control." |
| Homegrown Platform | FEDERATION | "Extend your platform beyond your network through instant partner connections." |
| Standard OSS/BSS | MISSING LAYER | "Add what your OSS can't provide—instant private path provisioning." |
| Manual/Legacy | SPEED | "Stop waiting 60-90 days. Provision private paths in minutes, not months." |
| None Identified | FABRIC-IN-A-BOX | "Deploy your own connectivity fabric—no protocol complexity." |

## Value Proposition by Segment
- Colocation Standard: "Build your own fabric rather than joining someone else's"
- Colocation AI Infrastructure: "Deterministic paths for inference workloads"
- Neocloud: "See why you're slow, then fix it — observability, cloud on-ramp, deterministic paths"
- Fiber: "Eliminate 60-90 day NNI delays"
- Network Operator Track A: "Extend internal automation to cross-carrier paths" (NEVER claim they're slow)
- Network Operator Track B: "Unify internally first, then extend externally"
- MSP: "Visibility into carrier networks behind your services"
