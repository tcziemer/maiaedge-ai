---
name: sales-enablement
description: "MaiaEdge sales enablement content generator. Creates consistent, on-brand sales collateral and messaging frameworks. Use when creating battle cards, discovery guides, one-pagers, email sequences, objection responses, competitive positioning, sales playbooks, talking points, proof points, or any customer-facing sales content. Ensures all content aligns with core positioning (Private paths. Any network. Instantly.) and segment-specific value pillars. Segments content by persona and customer segment. Includes technical messaging specs, proof points, team credibility anchors, and differentiation narratives vs competitors like Lumen PCF and NaaS providers."
---

# MaiaEdge Sales Enablement Skill

This skill ensures consistent, on-brand sales enablement content for MaiaEdge.

## Reference Files

- **`context/copy-strategy/segment-language.md`** - Insider vocabulary and conversational patterns per segment. Read before creating any segment-specific collateral to use their language, not ours.
- **Segment cheatsheets** (`context/segments/colocation.md`, `context/segments/fiber-operator.md`, `context/segments/neocloud.md`, `context/segments/network-operator.md`, `context/segments/msp-aggregator.md`, `context/segments/enterprise.md`, `context/segments/enterprise-use-cases.md`)
- **`context/core/competitive-positioning.md`** - Battle cards and positioning vs competitors
- **`context/core/messaging-framework.md`** - Core messaging pillars and segment positioning
- **`context/product/proof-points.md`** - Named customer references (for internal enablement only, anonymize for cold outreach)
- **`context/core/icp-playbook.md`** - Full ICP definitions, buyer personas, and qualification criteria. Ground battle cards and discovery guides in these personas and gates rather than re-deriving them.
- **`context/product/economic-impact-acg-whitepaper.md`** - ACG Research economic impact study; use for ROI and cost-justification sections in battle cards and business cases.
- **`context/product/cloud-onramp-business-case.md`** - Cloud on-ramp cost and performance models; reference for cloud connectivity angles in discovery guides and one-pagers.
- **`context/partner-assets/product-quick-reference.md`** - Concise product specs and capability summary; use for quick-reference sections and technical one-pagers.
- **`context/partner-assets/maiaedge-101.md`** - Partner-facing 30-second pitch and full product narrative; use for positioning language in new collateral.
- **`context/partner-assets/cheatsheet-colocation.md`** - Colocation segment objection handling and persona matrix.
- **`context/partner-assets/cheatsheet-neocloud.md`** - NeoCloud segment objection handling and persona matrix.
- **`context/partner-assets/cheatsheet-enterprise.md`** - Enterprise segment objection handling and persona matrix.
- **`context/partner-assets/cheatsheet-fiber-operator.md`** - Fiber operator segment objection handling and persona matrix. (MEDIUM)
- **`context/partner-assets/cheatsheet-network-operator.md`** - Network operator segment objection handling and persona matrix. (MEDIUM)
- **`context/partner-assets/cheatsheet-msp-aggregator.md`** - MSP/Aggregator segment objection handling and persona matrix. (MEDIUM)
- **`context/partner-assets/use-case-gpu-cluster-connectivity.md`** - GPU cluster connectivity use case; reference for NeoCloud and AI Colo collateral. (MEDIUM)
- **`context/copy-strategy/outbound-playbook.md`** - Outbound sequence structure and angle-selection logic. (MEDIUM)
- **`context/outreach/voice-gold-standard.md`** - Voice and tone standards; apply to any outreach-adjacent collateral. (MEDIUM)

## Core Positioning

**Hero Statement:** Private paths. Any network. Instantly.

**Category:** Carrier Infrastructure for Federated Private Networking

**Positioning Statement:** For network operators with fragmented networks, MaiaEdge delivers the only purpose-built infrastructure that automatically interconnects disconnected networks into one cohesive fabric, so they can activate private paths anywhere, instantly.

**Only Statement:** Only MaiaEdge provides the infrastructure that enables network operators to extend services across domains instantly, over any transport, while maintaining complete visibility and sovereignty.

<!-- Canonical source: context/copy-strategy/segment-messaging.md -->
## Three Core Business Outcomes

**For full value prop matrices per segment, see context/copy-strategy/segment-messaging.md**

Pillars are segment-specific. Always frame value around the correct set for the target segment:

| Segment | Pillars |
|---------|---------|
| Fiber | MONETIZE \| AUTOMATE \| EXTEND REACH |
| Network Op / MSP | AUTOMATE \| EXTEND REACH \| MONETIZE |
| Colo | INSTANT \| MONETIZE \| REACH |
| AI Colo | DETERMINISTIC \| INSTANT \| MONETIZE |
| Neocloud | DETERMINISTIC \| PRIVATE \| INSTANT |
| Enterprise (Multi-DC ICP) | REDUNDANT \| SOVEREIGN \| AUTOMATED |

**Pillar definitions:**
1. **Automate** – Activate deterministic private paths over fiber or DIA instantly. No BGP, no MPLS, no routing complexity.
2. **Extend Reach** – Extend reach through seamless carrier-to-carrier partnerships while maintaining visibility and customer sovereignty.
3. **Monetize** – Turn infrastructure into revenue. Provide services beyond your footprint, monetize idle fiber, offer cloud connectivity under your brand.
4. **Deterministic** – Deterministic paths that eliminate the network as a variable for AI workloads.
5. **Private** – Private cloud connectivity that cuts egress costs 60-80% vs public internet.
6. **Instant** – Instant customer on-ramp. New facilities go live in minutes, not weeks.

## Product Components

- **Path Border Controller (PBC)** – 1RU edge hardware at network boundaries. Dual 100G interfaces, line-rate AES-256-GCM IPsec, stateless forwarding, <2μs latency overhead.
- **Path Computation Engine (PCE)** – Cloud-native orchestrator. Real-time path computation, multi-domain orchestration, policy enforcement, hop-by-hop telemetry.

## Customer Segments

For segment-specific messaging, personas, and pain points, see **`context/core/icp-playbook.md`**.

| Segment | Profile | Primary Value Prop |
|---------|---------|-------------------|
| Neocloud | GPU cloud providers across multiple colo facilities | Deterministic performance + private connectivity + instant on-ramp |
| Colocation | Data centers, meet-me rooms | (Live / proposal language) Fabric-in-a-box without multi-year development. **Cold-email lead** (Sidecar §4.1.A) for Standard Colo: "Interconnection attach rate is what separates colos from being landlords. New services on top of space and power, under your brand, without a multi-year build." For AI Signals Colo (Lambda/Crusoe/Nebius tenant, liquid cooling, 30kW+ racks): "deterministic paths between GPU clusters and cloud on-ramps that match the power and cooling spend." |
| Service Provider | Tier 1/2 carriers | Extend reach, monetize existing assets, automate beyond network boundary |
| MSP/Aggregator | Asset-light, multi-carrier | Unified visibility across fragmented carriers |
| Fiber Operator | Regional fiber owners | Extend reach, monetize existing fiber infrastructure |
| Enterprise (Multi-DC ICP) | $1B+ enterprises with multi-DC corporate networks + in-house net eng (4 sub-segments: Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services). Anchor: Meijer. Promoted to ICP 2026-05-11. | Dark fiber redundancy that is actually redundant + cloud on-ramps under enterprise control + audit-ready paths. Pair speed with data sovereignty (NOT operator sovereignty). |

## Competitive Positioning

For detailed objection handling and competitor responses, see **`context/core/competitive-positioning.md`**.

**What MaiaEdge is NOT:**
- NOT NaaS (Megaport/Equinix) – They own customers; MaiaEdge enables YOU to own customers
- NOT SD-WAN – Built for carriers at carrier-scale, not enterprise branches
- NOT Router Replacement – Complements Cisco/Juniper at the edge

**Key Differentiation vs Lumen PCF:**
"Lumen builds their empire; MaiaEdge empowers you to build yours."

## Document Creation Workflows

### Battle Cards
1. Lead with segment-specific pain points (see `context/core/icp-playbook.md`)
2. Frame MaiaEdge value using the segment-specific pillars (see segment pillar table above)
3. Include persona-specific talk tracks
4. Add competitive objection responses
5. End with proof points and customer quotes

**Enterprise battle cards** carry different objections than operator segments. Build Enterprise battle cards around these four reframes:
- **"We already have SD-WAN"** - Different layer. SD-WAN handles branch/user; MaiaEdge handles inter-DC and cloud on-ramp. The two run together; SD-WAN is the overlay that benefits from a deterministic, observable underlay.
- **"Megaport works fine"** - Until the team owns the SLA. Portal is theirs, support is theirs, cloud bill is theirs. MaiaEdge integrates with Megaport via API where it makes commercial sense - customer relationship and SLA stay with the enterprise team.
- **"We just signed a long carrier agreement"** - Use it. MaiaEdge sits over the existing transport; the carrier keeps providing the circuit, MaiaEdge gives the team determinism + visibility + control over whatever's underneath.
- **"AWS Direct Connect handles our cloud paths"** - Per cloud. AWS Cloud WAN / Azure vWAN / GCP NCC don't federate across clouds, and they don't solve dark fiber redundancy at all. MaiaEdge is the cross-cloud, cross-DC layer that does.

Source: `context/core/competitive-positioning.md` §3.6 Enterprise Competitive Context.

### Discovery Guides
1. Open with segment-identifying questions
2. Probe for core pain points: provisioning delays, visibility gaps, sovereignty concerns
3. Quantify the problem: "How long does provisioning take today?"
4. Identify buying triggers: hyperscaler proximity, Lumen competition
5. Map to MEDDPICC qualification

**Enterprise discovery guides** lead with different probes than operator discovery - Enterprises are the customer, not selling connectivity to anyone:
- "How is your dark fiber between DCs redundant today?" (Looking for: one pair, one path, no automated failover.)
- "When you need AWS Direct Connect or Azure ExpressRoute, who handles it?" (Looking for: Megaport / Equinix Fabric, their portal, their SLA.)
- "How do you prove to compliance / audit where data went between DCs?" (Looking for: can't, beyond BGP routing tables.)
- "How long does a new DC or DR site take to come online from a networking perspective?" (Looking for: months.)
- "Direct carrier contracts or all through a reseller / MSP?" (Disqualifier signal if 100% reseller/MSP - no Enterprise ICP path.)
- "What does your network team look like - where are you hiring?" (Confirms in-house net eng team via VP Network / Director Network Eng / Principal roles.)

### One-Pagers
1. Hero statement + segment-specific hook at top
2. 3 pain points in customer's language
3. MaiaEdge solution mapped to each pain
4. One proof point or customer quote
5. Clear CTA and next steps

### Email Sequences
1. Subject lines: problem-focused, not product-focused
2. First line: reference trigger event or pain point
3. Body: one core value prop, one proof point
4. CTA: specific, low-friction next step
5. Tone: peer-to-peer, not salesy

## Key Technical Messages

When creating technical content:
- Layer 2.5 / WAN-Ethernet: Extends Ethernet's simplicity to WAN without BGP/OSPF
- Protocol-free: No routing protocols in the field
- Deterministic routing: Stateless forwarding, predictable paths
- SRLG-aware: True physical redundancy, not just logical
- 100G throughput, <2μs latency overhead
- Line-rate encryption without performance degradation

## Proof Points

Reference these validated customer experiences:
- **Arvig:** "Almost instantaneous" provisioning
- **RevNet:** "If you're familiar with MegaPort... imagine having that capability between providers"
- **Equinix:** "Revolutionary and creative" – Josh Sordelet, Principal PM
- **IENTC:** Mobile backhaul, 800+ cell towers

## Team Credibility

- **Founded by leaders behind Acme Packet** ($2.1B exit to Oracle) and 128 Technology (Juniper). $2.55B combined exits.
- **Series A funded**  -  $20M from tier 1 investors who back infrastructure at scale.
- **Team that understands carrier ops**  -  not software engineers building routers, but people who've built at scale.

## When to Use This Skill

Trigger on any of these patterns:
- "Create a battle card for [segment]"
- "Write a discovery guide" or "Sales playbook"
- "One-pager for [company]" or "[persona]"
- "Email sequence for [segment]"
- "How do we position against [competitor]?"
- "Talking points for [objection]"
- "Proof points for [use case]"
- Any mention of: sales content, enablement, messaging, positioning, competitive objection, discovery, battle card, one-pager, email sequence

