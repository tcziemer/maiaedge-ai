---
name: bizcase
description: Generate customized business case Excel models for MaiaEdge cloud on-ramp prospects. Use when asked to build a business case, financial model, or ROI analysis for a prospect deploying MaiaEdge PBC-powered connectivity. Covers three segments: NeoClouds (GPU cloud providers), Fiber Operators, and Wholesale Carriers / Network Operators.
---

# MaiaEdge Cloud On-Ramp Business Case Generator — V2

Generate customized business case Excel models for prospects deploying MaiaEdge PBC-powered cloud on-ramp and connectivity services. Three primary segment templates: **NeoClouds (GPU Cloud Providers)**, **Fiber Operators**, and **Wholesale Carriers / Carrier's Carrier (Network Operators)**.

---

## CRITICAL: Read Before Starting

1. **KEEP IT SIMPLE** — Every model should be a 4-5 tab Excel file that a non-technical executive can follow in 10 minutes. If you're building more than 6 tabs, you're overcomplicating it. Consolidate.
2. **Always ask for prospect details first** (use AskUserQuestion) before building any model
3. **Understand the prospect's segment CORRECTLY** — see Segment Identification below
4. **Base financial models on the Atlantech reference model** for structure and formula logic — adapt pricing to the prospect's situation
5. **Cloud on-ramp is ONE value stream** — but the business case should be focused on what matters most to THIS prospect, not every possible value stream
6. **Mark unconfirmed assumptions clearly** — `UNCONFIRMED` in red/warning cells
7. **Never present over-capacity scenarios** — always include a capacity check
8. **Template source**: `/sessions/lucid-optimistic-wright/mnt/uploads/atlantech_cloud_onramp_v9.xlsx` — read for formula logic

### THE SIMPLICITY RULE

The goal is a business case a prospect can open, understand, and say "yes" to — not a comprehensive reference document. Follow these rules:

- **4-5 tabs maximum** per model. Core tabs: Executive Summary, Assumptions (editable inputs), P&L Model, Competitive Comparison. Add ONE segment-specific tab if needed.
- **One number per concept.** Don't show 4 pricing contexts — show the one that applies to this prospect with a footnote that pricing is negotiable.
- **Executive Summary fits on one printed page.** If it doesn't, cut it.
- **Every table has <= 6 rows.** If you need more, you're showing too much detail for an executive audience.
- **Assumptions tab is the ONLY place with editable inputs.** Everything else is formula-driven from there.
- **Competitive comparison: 3-4 rows max.** Pick the capabilities that matter to THIS prospect.
- **Federation arbitrage, sovereignty, and competitive matrix sections below are REFERENCE MATERIAL for you.** Pull from them selectively — don't dump everything into the model.

---

## SEGMENT IDENTIFICATION — GET THIS RIGHT

The most common mistake is confusing NeoClouds with Colocation operators. They are DIFFERENT segments with different pain points, messaging, and economics.

| Prospect Type | Segment | Key Signal | Who Buys MaiaEdge? |
|--------------|---------|------------|-------------------|
| GPU cloud provider (CoreWeave, Lambda, RunPod, Together AI, Crusoe) | **NeoCloud** | They DEPLOY GPUs. They ARE the customer. | They deploy PBC for their own connectivity |
| Data center / colocation provider (Aligned, Stack, QTS, EdgeConneX) | **Colocation** (use Colo cheatsheet, NOT this skill) | They RENT space to tenants. They don't deploy GPUs. | They deploy PBC to offer connectivity to tenants |
| Regional fiber carrier (Arvig, Windstream, Consolidated, Uniti) | **Fiber Operator** | They OWN fiber. Measure network in "route miles." | They deploy PBC to monetize existing fiber |
| National/global carrier selling to other carriers (Zayo, EXA, Lumen Wholesale) | **Wholesale Carrier** | They sell to OTHER CARRIERS who sell to enterprises | They deploy PBC for multi-carrier federation |
| MSP / connectivity aggregator (asset-light, resells capacity) | **MSP/Aggregator** (use MSP cheatsheet, NOT this skill) | They DON'T own infrastructure | They deploy PBC for visibility across carrier networks |

---

## REFERENCE MODEL — ATLANTECH CLOUD ON-RAMP (BASE CASE)

The Atlantech model is a **Wholesale Carrier** business case (Atlantech sells wholesale to partner carriers). Use it as the structural template for all segments, but adapt pricing and value propositions per segment.

### MaiaEdge Pricing Context — IMPORTANT

The Atlantech model shows a **negotiated** PBC price. Know the full pricing picture:

| Pricing Context | 10G Monthly | 100G Monthly | Source |
|----------------|-------------|--------------|--------|
| **MaiaEdge list price** (12-mo term) | ~$1,246/mo ($14,950/yr) | ~$2,492/mo ($29,900/yr) | MaiaEdge 101 SKU table |
| **Atlantech negotiated** (30% partner discount) | $680/mo | $1,338/mo | Atlantech model, confirmed |
| **Cloud on-ramp doc pricing** (PBC subscription) | $2,125/mo | $4,250/mo | Cloud On-Ramp Sales Supplement |
| **Market development subsidy** (Phase 1) | $0/mo | $0/mo | PBC = $0 until profitable |

> **RULE:** When building prospect models, use the Atlantech negotiated price ($680/mo 10G, $1,338/mo 100G) as the BASE CASE. Note that actual pricing depends on term length, volume, and negotiation. Flag exact PBC cost as requiring confirmation unless using list pricing.

### Infrastructure Costs (Monthly, Per Location — Atlantech Reference)

| Item | Ashburn | Los Angeles | Status |
|------|---------|-------------|--------|
| MaiaEdge PBC — 10G (net after 30% discount) | $680 | $680 | CONFIRMED |
| Switch license | $150 | $150 | UNCONFIRMED (may be $0 if in PBC) |
| AWS Direct Connect 10G Dedicated port | $1,643 | $1,643 | CONFIRMED ($2.25/hr x 730 hrs) |
| Equinix cross-connect (to AWS DX cage) | $375 | $550 | CONFIRMED (LA premium) |
| Coresite cross-connect (LA only) | — | $325 | CONFIRMED |
| LA fiber transport (Coresite to Equinix LA) | — | $500 | CONFIRMED |
| **Total (full, PBC included)** | **$2,848** | **$3,848** | |
| **Total (PBC subsidized = $0)** | **$2,168** | **$3,168** | |

### Cloud On-Ramp Financial Models (from Sales Supplement)

**10G Deployment — Service Tier Model:**

| Tier | Bandwidth | MRC | Description |
|------|-----------|-----|-------------|
| Gold | Guaranteed 2G | $1,200 | Committed BW, strict QoS |
| Silver | High-priority 2G | $900 | Priority with controlled oversubscription |
| Bronze | Best-effort 1G | $400 | Standard access |

**10G total fixed cost:** $3,788/mo (port $1,663 + PBC $2,125)
**10G breakeven:** ~4 customers | Full utilization: 11 customers, ~47% gross margin

**100G Deployment — Service Tier Model:**

| Tier | Bandwidth | MRC | Description |
|------|-----------|-----|-------------|
| Gold | Guaranteed 5G | $2,500 | Committed BW, strict QoS, lowest latency |
| Silver | High-priority 5G | $1,800 | Priority with controlled oversubscription |
| Bronze | Best-effort 2G | $600 | SaaS, dev/test, backup |

**100G total fixed cost:** $15,650/mo (port $11,400 + PBC $4,250)
**100G breakeven:** ~7 customers | Full utilization: 52 customers, ~75% gross margin
**100G monthly profit at full utilization:** ~$46,000

### Atlantech Wholesale Pricing Tiers (Partner Carrier model)

| Tier | Committed BW | Wholesale MRC | Megaport Equiv. | Savings |
|------|-------------|---------------|-----------------|---------|
| Starter | 0.5G | $350 | $700 | 50% |
| Standard | 1G | $550 | $1,000 | 45% |
| Business | 2G | $900 | $1,400 | 36% |
| Enterprise | 5G | $1,800 | $2,200 | 18% |

### Oversubscription & Capacity

- **Base case:** 2:1 oversubscription -> 20G sellable on 10G port
- **Avg peak utilization assumption:** 40% (conservative; enterprise cloud typical 20-50%)
- **Expected peak load at 2:1 + 40%:** 8G on 10G port (safe)
- **Safety rule:** Peak load MUST stay below physical port capacity

### PBC Subsidy Terms (Atlantech-specific — adapt per prospect)

- MaiaEdge subsidizes PBC at $0/mo until prospect's monthly gross profit > $0
- PBC cost reinstated ALL AT ONCE (step-function cliff) — always show Phase 1 and Phase 2 P&L
- **Requires signed LOI/term sheet with MaiaEdge before sharing externally**
- Note: Subsidy terms are deal-specific. Not all prospects get subsidy. Confirm with Tim Ziemer.

---

## REFERENCE MATERIAL — PULL FROM SELECTIVELY, DO NOT DUMP INTO MODELS

> **The sections below (Federation Arbitrage, Sovereignty, Competitive Matrix) are YOUR knowledge base.** Use them to inform what you put in the business case, but DO NOT copy entire sections into the Excel model. Pick the 2-3 most relevant points per prospect.

---

## THE FEDERATION ARBITRAGE — WHY THIS MODEL GETS BETTER WITH SCALE

A powerful economic argument. Include the core table in models where federation volume is relevant (Fiber Operators, Wholesale Carriers). For NeoClouds, mention federation as a future benefit, not a primary driver.

### How It Works

A carrier deploys PBCs to serve their own customers. But that same PBC infrastructure also makes them a wholesale supplier to every other MaiaEdge-connected operator. This creates a dual-revenue model:

**Revenue Stream 1: Retail** — Sell cloud on-ramp and connectivity to your own enterprise customers under your brand, at your pricing.

**Revenue Stream 2: Wholesale** — Other MaiaEdge operators who need paths through your geography buy capacity from you. You become a wholesale supplier automatically through federation.

### Why This Matters Financially

The fixed infrastructure cost (PBC + AWS port + cross-connects) is the same whether you serve 5 customers or 50. Each additional circuit — whether retail or wholesale — drops almost entirely to gross profit. The more operators in the federation, the more wholesale demand flows to each participant.

| Scenario | Your Customers | Wholesale from Federation | Total Circuits | Revenue | Cost Floor | Gross Margin |
|----------|---------------|--------------------------|----------------|---------|------------|-------------|
| Retail only | 5 | 0 | 5 | $2,750 | $2,168 | 21% |
| Retail + light wholesale | 5 | 3 | 8 | $4,400 | $2,168 | 51% |
| Retail + active wholesale | 5 | 10 | 15 | $8,250 | $2,168 | 74% |
| Federation hub | 5 | 20 | 25 | $13,750 | $2,168* | 84% |

*At 20+ circuits, may need capacity expansion — model accordingly.

### The Arbitrage

Higher volume means lower per-circuit cost. Operators who participate in federation can price below Megaport ($700-$2,200/circuit) while maintaining strong margins because their cost floor is shared across more circuits. This is the arbitrage: federation volume subsidizes retail competitiveness.

**How to include:** Add a "Federation Revenue" SECTION (not a separate tab) within the P&L Model tab. Show 2-3 rows: retail-only margin vs. retail + wholesale margin. Keep it to one small table — the arbitrage concept is powerful precisely because it's simple.

---

## SOVEREIGNTY & CUSTOMER CONTROL — THE EUROPEAN IMPERATIVE

Sovereignty is not just about data at rest — it's about data in transit. Include sovereignty content ONLY for European prospects or sovereign AI companies. For US-only prospects, mention customer control (white-label, Q-in-Q) but skip the regulatory table.

### The Sovereignty Problem No One Else Solves

When a packet travels from London to Amsterdam, BGP routes it through the cheapest path. That path might transit New York (subject to the US CLOUD Act), Singapore, or any jurisdiction where a government could compel data access. No carrier today — not Megaport, not Equinix, not Lumen — guarantees where packets travel in transit.

MaiaEdge is the only infrastructure that enforces jurisdictional routing policy at the path level. The PCE computes routes that obey geographic constraints: "traffic MUST stay within EU" or "data MUST NOT transit US-controlled infrastructure." Every hop is logged with timestamp, carrier, and geographic location.

### Three Dimensions of Sovereignty

**1. Path Sovereignty:** Control WHERE your data travels. Define geographic constraints the PCE enforces. BGP cannot override jurisdictional routing policy.

**2. Customer Sovereignty:** Your customers see YOUR brand, YOUR portal, YOUR pricing. Partner topology stays hidden via Q-in-Q tagging. No customer ever sees Megaport, Equinix, or any underlying infrastructure provider — unless you choose to expose it.

**3. Commercial Sovereignty:** You set the price. You own the contract. You control the roadmap. You are not a tenant on someone else's platform with no say in pricing changes or feature direction.

### Regulatory Context for European Business Cases

| Regulation | Requirement | MaiaEdge Capability |
|-----------|-------------|-------------------|
| **GDPR** (Articles 44-50) | Data transfers outside EEA require adequate safeguards | Policy-based routing keeps data within EEA borders. Hop-by-hop audit trail proves compliance. |
| **EU AI Act** (Aug 2026 enforcement) | Infrastructure-level proof of data control. Fines up to 7% global revenue. | Jurisdictional metadata logged at every hop. Hand to regulators on demand. |
| **CLOUD Act** (US) | US entities can compel data access regardless of physical location | Sovereign routing avoids US-controlled carriers entirely. PCE routes around CLOUD Act exposure. |
| **Schrems II** implications | Standard Contractual Clauses not sufficient if data transits non-adequate jurisdictions | Path control eliminates the transit risk SCCs can't address |
| **SecNumCloud** (France) | Refuses providers subject to non-European law | MaiaEdge infrastructure deployed BY the operator (European entity) — not a US SaaS platform |

### What Competitors Cannot Offer

- **Megaport:** Does NOT guarantee EU-only traffic paths. Uses Standard Contractual Clauses for transfers outside EU. US-headquartered. No path sovereignty.
- **Equinix Fabric:** GDPR-compliant via Binding Corporate Rules, but US-headquartered parent company creates CLOUD Act exposure. No guaranteed EU-only routing.
- **Lumen PCF:** No sovereign path guarantees. US carrier.
- **PacketFabric, Console Connect, Zayo:** No sovereignty controls documented.
- **Colt:** Named AWS European Sovereign Cloud partner, but no explicit in-transit path control guarantees.

**Only MaiaEdge provides operator-level, policy-enforced sovereign routing with cryptographic proof of path compliance.**

### How to Model Sovereignty Value

For European prospects, add a "Sovereignty & Compliance" sheet:
- Cost of GDPR non-compliance (fines up to 4% global revenue or EUR 20M)
- Cost of EU AI Act non-compliance (up to 7% global revenue)
- Value of audit-ready path documentation (legal/compliance hours saved)
- Customer acquisition advantage ("we can prove where your data travels")
- Premium pricing opportunity for sovereignty-guaranteed services (15-25% above standard)

---

## COMPETITIVE ADVANTAGE MATRIX — REFERENCE TABLE (DO NOT INCLUDE FULL MATRIX)

This is your reference. The actual business case should have a 3-4 row comparison tailored to the prospect's situation. Never include the full 12-row matrix — it overwhelms executives.

### MaiaEdge vs. The Alternatives

| Capability | MaiaEdge | Megaport | Equinix Fabric | Lumen PCF | Build Your Own |
|-----------|----------|----------|---------------|-----------|---------------|
| **Who owns the customer?** | YOU own the customer, brand, invoice | Megaport owns portal + relationship | Equinix owns portal + relationship | Lumen owns relationship | You own it (if you finish) |
| **Who sets the price?** | YOU set pricing freely | Megaport's rates, you markup | Equinix's ICB pricing, no reseller control | Lumen's fixed rates | You set it |
| **Can you white-label?** | Yes — your brand, your portal | No true white-label | No white-label | No | Yes (if built) |
| **Provisioning speed** | Minutes (PCE automated) | ~60 seconds (hosted) | Hours (API-driven) | 20+ days (wavelength) | Months (per partner) |
| **Federation with other carriers** | Instant — PBC to PBC | Not possible — Megaport is hub | Limited — Equinix-centric | Not possible | 60-90 day NNI per partner |
| **End-to-end path visibility** | Hop-by-hop, every hop, every carrier | Service logs + usage reports only | Traceroute + BGP state | Console visibility | Only your own network |
| **Sovereign routing (EU path control)** | Yes — policy-enforced, auditable | No — no path guarantees | No — US parent, CLOUD Act | No — US carrier | Only your own network |
| **Data sovereignty proof** | Hop-by-hop jurisdictional audit trail | None | BCRs + SCCs (not path control) | None | Manual (if instrumented) |
| **Wholesale revenue opportunity** | Yes — federation makes you a supplier | No — you're a buyer/tenant | No — you're a buyer/tenant | No — you're a buyer | No federation network |
| **Multi-cloud (AWS + Azure + GCP)** | Same PBC, shared cost across all clouds | Per-VXC charges per cloud | Per-connection charges | AWS-centric | Separate build per cloud |
| **Lock-in risk** | Low — you own the PBC, choose carriers | Medium — ETFs, platform dependency | High — 36mo terms, auto-renew, ETFs | High — Lumen fiber dependency | Low (but huge build cost) |
| **Time to production** | 30-60 days | Days (port provisioning) | Days-weeks | Months | 18-24 months |
| **Cost at scale (100G, full util.)** | ~$46K/mo profit, 75% margin | Platform fees scale linearly | Port + per-VXC costs add up | Opaque enterprise pricing | Capex amortization |

### Competitive Pricing Comparison (1G Cloud On-Ramp Circuit)

| Provider | Monthly Cost to End Customer | What's Included | What's Missing |
|----------|-------|-----------------|----------------|
| **Megaport Hosted Connection** | $1,000 | AWS port + Megaport port + VXC | No path visibility, no sovereignty, no white-label, customer on Megaport portal |
| **Equinix Fabric (Standard)** | $1,200+ | Unlimited 10G VCs, FCR routing | No white-label, Equinix lock-in, US parent CLOUD Act exposure |
| **PacketFabric** | $250-$400 | Hosted connection, API provisioning | No white-label, no path visibility, no sovereignty |
| **Lumen PCF** | Not disclosed (enterprise) | Managed fiber + AWS integration | 20-day delivery, no operator control, no white-label |
| **MaiaEdge operator (at Atlantech wholesale pricing)** | $550 (wholesale) / $798 (partner retail) | Full path visibility, sovereignty, white-label, federation wholesale upside | Operator must deploy PBC (30-60 day setup) |

### How to Present This in Business Cases

Do NOT include the full matrix above — it's overwhelming. Instead, pick the 3-4 rows most relevant to the prospect's pain and build a simple side-by-side. For example:

**For a Fiber Operator losing customers to Megaport:**
Focus on: Customer ownership, pricing control, white-label, federation revenue

**For a NeoCloud CEO worried about costs:**
Focus on: Total cost comparison, multi-cloud savings, no per-VXC fees, egress reduction

**For a European wholesale carrier:**
Focus on: Sovereignty, federation, path visibility, regulatory compliance

---

## STEP 0 — IDENTIFY SEGMENT AND GATHER PROSPECT DATA

Before building any model, use AskUserQuestion to collect:

**For ALL segments:**
- Prospect company name
- Primary PoP location(s) (Ashburn VA, LA, Chicago, Dallas, NYC, etc.)
- Are they co-located in an Equinix facility? (yes/no — determines cross-connect model)
- Target timeline
- Port size (10G to start, or planning 100G?)

**Segment-specific questions:**

**NeoClouds:** How many facilities? Which cloud providers do they use most (AWS, Azure, GCP)? How much are they spending on data egress today? Do they have a network team or are IT admins managing connectivity? What's their primary pain — slow data movement, high egress costs, or inconsistent inference latency?

**Fiber Operators:** Do they own fiber to the AWS Direct Connect PoP? What percentage of their fiber is generating revenue vs. dark/stranded? How long do NNIs take today? How many enterprise customers? Are they losing deals to provisioning speed?

**Wholesale Carriers:** How many partner carriers? What's their provisioning timeline today (days, weeks, months)? Is internal automation unified across all domains? Are enterprise customers comparing them to cloud speed? Do partners currently use Megaport or Equinix Fabric?

---

## SEGMENT 1 — NEOCLOUD (GPU CLOUD PROVIDER) BUSINESS CASE

### Who They Are

GPU cloud providers: CoreWeave, Lambda Labs, Crusoe Energy, Together AI, RunPod, Modal, Groq, Vultr, DigitalOcean, Nebius, Nscale, Firmus, E2E Networks, IREN, Core Scientific, Northern Data Group, TeraWulf. They deploy GPU clusters across multiple colocation facilities. They ARE the end customer — they need connectivity for their OWN workloads.

**Scale:** $50M-$5B+ revenue. Rapidly scaling from 3 to 30+ facilities. Multi-billion dollar valuations. Spending $4,800/GPU/month.

**Critical distinction:** NeoClouds are NOT data center operators selling to tenants. They are compute companies that accidentally became networking companies. They don't have WAN teams. Network is an afterthought until inference latency becomes unpredictable.

### IMPORTANT: NeoCloud Decision-Makers Are NOT Networking People

NeoCloud CEOs, founders, and VPs of Infrastructure think about GPU utilization, training throughput, and customer SLAs — not about BGP, VLAN tagging, or cross-connects. The business case must speak their language.

**Rules for NeoCloud messaging:**
- NEVER lead with networking terminology (PBC, PCE, BGP, MPLS, VLAN, oversubscription)
- ALWAYS lead with business outcomes they care about (speed, cost, reliability, scale)
- Frame everything as removing bottlenecks to their core business (GPU compute)
- Use dollar amounts and time savings, not technical specifications
- If you must explain the technical "how," do it in an appendix or architecture notes tab — not the executive summary

### The "Why" — In Their Language

**For the CEO/Founder:** "Your GPUs are your most expensive asset. Every minute they sit idle waiting for data costs you money. MaiaEdge makes data move faster between your facilities and the cloud, cuts your bandwidth bill by 60-80%, and gives you a dashboard that shows exactly where slowdowns happen — without hiring a network team."

**For the VP of Infrastructure:** "Every new facility is a multi-week connectivity project with a different carrier, different setup, different performance. MaiaEdge makes every facility work the same way. One dashboard. Minutes to connect a new site. No carrier finger-pointing when something's slow."

**For the CFO:** "You're paying $0.05-$0.09 per gigabyte to move data over the public internet. Private paths cost $0.02. For training runs moving terabytes, that's 60-80% off your bandwidth bill. MaiaEdge is a subscription — no capital expenditure, no network team to hire."

### Pain Points — What They Experience (Not Technical Root Causes)

| What They Say | What's Actually Happening | Dollar Impact |
|--------------|--------------------------|---------------|
| "Training is slow and we don't know why" | Data transfer from cloud storage to GPU clusters bottlenecked on public internet | GPU idle time at $4,800/GPU/month. 30% training interruption rate |
| "Our bandwidth bill is out of control" | Paying retail internet egress ($0.05-$0.09/GB) instead of private path rates ($0.02/GB) | $10K-$100K+/month in unnecessary egress costs |
| "When things break, nobody can tell us what happened" | Zero visibility once traffic leaves their facility. Carriers point fingers at each other. | $1M+/hour when training stalls. Weeks of support tickets. |
| "Connecting a new facility takes forever" | Each new site is a 6-week carrier coordination project | Expansion from 5 to 30+ facilities bottlenecked by connectivity |
| "We can't hire network engineers" | Networking talent is scarce. They have IT admins, not WAN architects. | $200K+/year per senior network engineer they can't find |

### INVERTED MESSAGING HIERARCHY (CRITICAL)

Unlike every other segment, NeoCloud messaging follows an **inverted** order. Lead with symptoms they recognize, NOT infrastructure they don't understand.

| Priority | Message | Hook |
|----------|---------|------|
| **1. LEAD** | **"See why you're slow"** | End-to-end visibility — diagnose slowdowns in minutes, not weeks |
| **2. SECOND** | **"Move data faster and cheaper"** | Private cloud paths cut egress 60-80%. Training data arrives in hours, not days. |
| **3. THIRD** | **"Every new facility in minutes"** | One platform across all facilities. Same performance everywhere. No carrier projects. |

**Why inverted?** NeoClouds don't think they have a networking problem. They think they have a performance problem. Lead with "see why you're slow," not "we provide deterministic Layer 2 paths with encrypted forwarding."

### NeoCloud Business Case Model — What to Build (4 TABS ONLY)

The NeoCloud model is a **cost savings + ROI model**, not a revenue model. The NeoCloud IS the customer.

**Tab 1 — Executive Summary** (one page, printable)
- Company profile: name, facilities, GPU count, cloud providers
- Three-line ROI summary: Egress Savings + Training Efficiency + Operational Savings
- Total monthly/annual value vs. MaiaEdge cost
- Payback period (typically month 1-2)
- 3-row competitive comparison (MaiaEdge vs. Megaport vs. Status Quo)

**Tab 2 — Assumptions** (editable inputs — yellow cells)
- Monthly data volume (TB), current egress rate, Direct Connect rate
- GPU count, cost per GPU/month ($4,800), training interruption rate
- Facility count (current + planned), PBC cost per facility
- AWS DX port + cross-connect costs per facility

**Tab 3 — Savings Model** (ALL savings consolidated into one tab)
- Section A: Egress savings (current vs. Direct Connect, monthly/annual)
- Section B: Training efficiency (GPU idle time recovered, interruption reduction)
- Section C: Operational savings (headcount avoidance, faster provisioning)
- Section D: Total value vs. total MaiaEdge cost, net savings, ROI %
- Section E: Multi-facility scale (5/10/20/30 facility projections — 4 rows)

Reference egress savings scenarios:

| Scenario | Monthly Data | Current Cost | With DX | Savings |
|----------|-------------|-------------|---------|---------|
| Conservative | 50 TB | $4,500 | $1,000 | $3,500 |
| Base Case | 200 TB | $18,000 | $4,000 | $14,000 |
| High Volume | 1 PB | $90,000 | $20,000 | $70,000 |

**Tab 4 — Competitive Comparison** (3-4 rows max)
- MaiaEdge vs. Megaport: flat subscription vs. port + per-VXC fees. Note Latitude.sh acquisition — Megaport now sells competing GPU services.
- MaiaEdge vs. Equinix Fabric: $1,200/mo standard, no white-label, high lock-in
- MaiaEdge vs. Status Quo: cost of doing nothing (egress bleed, GPU idle time, slow expansion)

> **Optional 5th tab — Sovereignty** (add ONLY for European or sovereign AI prospects): Regulatory compliance table, path control value, premium pricing opportunity.

### NeoCloud Sub-Segment Adjustments

| Sub-Segment | Key Difference | Model Focus |
|-------------|---------------|-------------|
| Large-Scale GPU Cloud (CoreWeave, Lambda, Nebius) | 20-50+ facilities, building network teams, sophisticated | Cross-carrier orchestration, multi-facility scale model |
| Tier 1 Inference (Together.ai, Groq, Cirrascale, DeepInfra) | 20-50+ edge locations, sub-100ms SLA, no network team | Latency diagnosis value, SLA compliance cost of failure |
| AI Infrastructure Provider (Vultr, DigitalOcean, RunPod, Modal) | Mid-market, adding GPU compute, existing customer base | White-label portal value, Megaport displacement, MTTI |
| Sovereign AI Cloud (Nscale, Firmus, E2E Networks) | GDPR/DPDP compliance, data must stay in-jurisdiction in transit | Sovereign routing value, compliance audit cost avoidance |
| Crypto-to-AI (IREN, Core Scientific, Northern Data, TeraWulf) | Former miners, cheap power, terrible networking | Basic connectivity upgrade, tenant audit pass value |

### NeoCloud Competitive Framing

- **#1 Competitor: Status Quo** (do nothing). They don't know they have a network problem. They know they're slow.
- **#2 Competitor: Megaport/Latitude.sh** — now bundled GPU + networking. Creates lock-in. "Megaport wants to be your GPU provider AND your network provider. That's a lot of control to hand one vendor."
- **#3 Competitor: Internal Build** — 18-24 months, $2-5M+, no federation capability
- **Key win:** MaiaEdge delivers observability + deterministic paths + cloud on-ramp without requiring a network team. IT admins can manage it.

---

## SEGMENT 2 — FIBER OPERATOR BUSINESS CASE

### Who They Are

CLECs, ILECs, regional fiber operators, and competitive carriers with physical fiber infrastructure. Measure their network in "route miles." Often fragmented across disconnected fiber islands with different systems at each location.

**Scale:** 50-2,000 employees, $50M-$1B revenue, regional focus (2-10 state footprint). ~1,900 small-scale fiber companies in the US. 2,200+ regional operators in North America.

**Revenue model:** Dark fiber (IRUs), lit wavelengths, metro Ethernet, wholesale. **30-70% capacity underutilized.**

### Pain Points (Research-Validated)

| Pain | Detail | Financial Impact |
|------|--------|-----------------|
| **Internal fragmentation** | Disconnected fiber islands with different systems at each location. Provisioning across own network still manual. | Weeks to provision internal paths |
| **60-90 day NNIs** | LOAs, VLAN coordination, BGP config. Lost deals because "customers go with whoever's faster." | Multi-state deals lost to speed |
| **Type 2 visibility black holes** | Responsible for SLA but can't see the path. 35% of Type 2 orders fail. | SLA penalties (2-10% of MRC), customer churn |
| **30-70% stranded fiber** | Dark fiber sitting idle while under pressure to grow revenue | Revenue potential: $200K-$5M+ annually per operator |
| **Cloud connectivity gap** | When customer asks for Direct Connect, operator says "call Megaport." Customer, revenue, and relationship leave. | Cloud connectivity revenue lost entirely |
| **Lumen PCF / AWS Interconnect threat** | Lumen offers enterprise-to-cloud directly, cutting regionals out | Market share erosion in enterprise segment |
| **Provisioning speed gap** | 30-90 days vs. NaaS platforms (Megaport/PacketFabric) at < 48 hours | Losing RFPs on speed alone |

### Fiber Operator Value Proposition — MULTI-LAYERED

Cloud on-ramp is ONE of FOUR value streams for fiber operators. The business case should model ALL of them:

**Value Stream 1: Internal Automation (AUTOMATE)**
- Unify disconnected fiber segments into one automated fabric
- Provision internal paths in minutes, not weeks
- Value: Operational savings + faster time to revenue on new circuits

**Value Stream 2: Federation with Partners (FEDERATE)**
- Instant NNIs with partner carriers (minutes vs. 60-90 days)
- Extend reach beyond footprint without infrastructure buildout
- Value: Win multi-state deals currently lost to speed

**Value Stream 3: Cloud On-Ramp Revenue (MONETIZE)**
- Offer AWS Direct Connect / Azure ExpressRoute under operator's own brand
- Customers see operator portal, not Megaport/Equinix
- Value: New high-margin recurring revenue stream

**Value Stream 4: Observability & SLA Control (PROVE)**
- Hop-by-hop telemetry across Type 2 circuits
- Prove SLAs to customers with data, not carrier reports
- Value: Reduced SLA penalties, faster troubleshooting, customer trust

### Cost Structure Adjustments for Fiber Operators

**Key advantage: Fiber operators own the transport.**

| Item | Non-Fiber Operator | Fiber Operator | Savings |
|------|--------------------|----------------|---------|
| Fiber transport to PoP | $500/mo (leased) | **$0/mo** (owned) | $500/mo |
| Colo cross-connect (if own PoP) | $325/mo | **$0/mo** | $325/mo |
| Equinix XC (to AWS DX cage) | $375-$550/mo | $375-$550/mo | Same |
| AWS Direct Connect 10G port | $1,643/mo | $1,643/mo | Same |
| MaiaEdge PBC 10G | $680/mo | $680/mo | Same |
| **Net savings per location** | — | — | **$500-$825/mo** |

### Fiber Operator Excel Model Structure (5 TABS)

**Tab 1 — Executive Summary** (one page, printable)
- Prospect name, fiber footprint, PoP locations
- Four-pillar value summary (Automate / Federate / Monetize / Prove) — one line each
- Infrastructure cost: subsidized with fiber-owner advantage
- Revenue projection and break-even
- 3-row competitive comparison
- Proof point: Arvig — "Almost instantaneous provisioning... utilize unutilized fiber"

**Tab 2 — Assumptions** (editable inputs — yellow cells)
- Infrastructure costs with fiber-owned transport toggle ($0 if owned)
- Oversubscription ratio (default 2:1)
- Service tier pricing (Gold/Silver/Bronze)
- Enterprise customer count, NNI timeline (current vs. MaiaEdge)
- PBC subsidy terms, Type 2 SLA penalty rate

**Tab 3 — P&L Model** (costs + revenue + margin in one view)
- Section A: Monthly cost (Full vs. Subsidized vs. Fiber-Owner). Fiber operators save $500-$825/mo per location on transport.
- Section B: Revenue by tier mix (Gold/Silver/Bronze), Phase 1 and Phase 2
- Section C: Gross margin and break-even (Phase 1 subsidized + owned fiber: ~2 customers; Phase 2: ~3 customers)
- Section D: Capacity check (REQUIRED)
- Section E: Federation wholesale revenue — additional circuits from other MaiaEdge operators on same infrastructure

**Tab 4 — Growth Opportunities** (stranded fiber + federation + operational savings consolidated)
- Section A: Stranded fiber monetization — current utilization %, revenue at 5/10/20% increase scenarios
- Section B: Federation revenue — federated partners x circuits x avg MRC (e.g., 5 partners x 3 circuits x $900 = $13,500/mo)
- Section C: Operational savings — SLA penalty reduction, NNI engineering hours saved, troubleshooting time

**Tab 5 — Competitive Comparison** (3-4 rows max)
- MaiaEdge vs. Megaport: "They own the fabric AND your customer. You own both with MaiaEdge."
- MaiaEdge vs. Lumen PCF: "Lumen builds their empire; MaiaEdge empowers you to build yours."
- MaiaEdge vs. Status Quo: Every month at 60-90 day provisioning = lost deals

> **Optional additions** (add ONLY if relevant to this prospect): Sovereignty tab for European fiber operators. Detailed stranded fiber analysis if prospect has significant dark fiber inventory.

### Fiber Operator Proof Points

- **Arvig** (Fiber, MN): "Almost instantaneous" provisioning. "MaiaEdge allows us to utilize unutilized fiber and provide services rapidly." Use for: speed objections, stranded fiber monetization.
- **Ocean Networks:** Federation to INDATEL for mainland reach. Use for: geographic isolation, partner expansion.
- **Ecotel** (Germany): "Great for the fragmented fibre market." Use for: international prospects, fragmented networks.

### Fiber Operator Competitive Framing

- **#1 Competitor: Status Quo** (most deals lost to inertia, not to other vendors)
- **#2 Competitor: Megaport/Equinix Fabric** — they capture the interconnection revenue AND the customer relationship
- **#3 Competitor: Lumen PCF + AWS Interconnect** — Lumen going direct to enterprise, cutting regionals out
- **Key win:** Fiber operator controls the fiber AND the on-ramp. One flat MRC, no per-VXC surcharge. Federation extends reach beyond footprint instantly.

### Fiber Operator Break-Even & Scale Comparison

| Metric | 10G @ Full | 100G @ Full |
|--------|-----------|-------------|
| Monthly infra cost | ~$2,023 (fiber owner, subsidized) | ~$8,550 (est.) |
| Monthly revenue at capacity | ~$7,200 | ~$61,800 |
| Gross margin | ~72% | ~86% |
| Monthly profit | ~$5,177 | ~$53,250 |

---

## SEGMENT 3 — WHOLESALE CARRIER / CARRIER'S CARRIER (NETWORK OPERATOR) BUSINESS CASE

### Who They Are

National or global network operators with owned fiber, leased capacity, and PoPs. Sell wholesale connectivity to partner carriers, ISPs, and service providers — who then sell to enterprises. Mix of internal domains often with different orchestration systems.

**Scale:** 1,000-50,000+ employees, $500M-$50B+ revenue, national or global footprint.

**Revenue model:** Enterprise connectivity, MPLS, wavelengths, IP transit, managed services. High-margin enterprise deals.

**Example companies:** Zayo ($4.25B acquiring Crown Castle fiber, 90,000+ route miles), EXA Infrastructure (160,000+ km across 37 countries), Windstream Wholesale (400G capacity expansion), Lumen (retained enterprise/wholesale after $5.75B consumer fiber sale to AT&T).

### Pain Points (Research-Validated)

| Pain | Detail | Financial Impact |
|------|--------|-----------------|
| **Internal fragmentation** | Automation not unified across internal domains. Different orchestration systems per domain. | Manual handoffs add days/weeks to provisioning |
| **Cross-carrier provisioning: 3-9 months** | Industry standard for wholesale Ethernet circuit provisioning. MEF standards exist but adoption patchy. | Enterprise customers compare to cloud (instant) and leave |
| **Can't match cloud speed** | AWS/Azure provision in minutes. Carriers quote weeks. Enterprise expectations now set by hyperscalers. | Lost enterprise deals, margin pressure |
| **Multi-domain orchestration** | End-to-end service delivery across multiple domains requires coordination between separate orchestrators, controllers, and assurance systems. | Most CSPs lack commercial-grade domain orchestration despite standards |
| **Visibility ends at boundaries** | Internal observability may exist per domain but stops at domain/carrier boundaries. | SLA enforcement impossible on cross-carrier paths |
| **Lumen/AWS vertical integration** | Lumen PCF + AWS Interconnect Last Mile goes direct to enterprise. $45B+ in fiber M&A in 18 months signals Tier 1 consolidation. | Regional operators cut out of value chain |
| **NaaS market share capture** | Megaport, Equinix Fabric, PacketFabric capturing cloud on-ramp revenue at < 48 hour provisioning speed | NaaS market: $33B (2025) -> $115B (2030), 42% CAGR. Wholesale = 26% by 2029 |

### Wholesale Carrier Value Proposition — PLATFORM ECONOMICS

The wholesale carrier model is a PLATFORM play. Each new partner carrier brings their book of enterprise customers onto the wholesale carrier's infrastructure. The business case should model platform-scale economics:

**Value Stream 1: Cloud On-Ramp as Wholesale Product**
- AWS Direct Connect / Azure ExpressRoute provisioned via MaiaEdge
- Partners sell cloud connectivity under THEIR brand through white-label portal
- Wholesale carrier captures recurring revenue per circuit

**Value Stream 2: Federation Revenue (Partner Carrier Activation)**
- MaiaEdge PBCs enable instant NNI with partner carriers
- Partners activate in minutes vs. 60-90 days traditional NNI
- Each new partner = incremental revenue with near-zero marginal cost
- Network effects: each new partner increases value for all participants

**Value Stream 3: Multi-Domain Unification**
- Single fabric layer across all internal domain boundaries
- Unified provisioning: same speed internally and externally
- Reduce operational complexity and headcount

**Value Stream 4: Enterprise Speed Parity**
- Match AWS/Azure instant provisioning speed
- Win enterprise deals currently lost to "quoting weeks"
- Cloud-like provisioning API for partner carriers

### Cost Structure (Atlantech Reference, Scaled Up)

Use Atlantech reference model for per-location cost structure. Key adjustments for scale:

| Deployment Stage | 10G Ashburn | 10G Multi-PoP (3 locations) | 100G Hub Market |
|-----------------|-------------|----------------------------|-----------------|
| Monthly infra cost (full) | $2,848 | $8,544 | ~$15,650 |
| Monthly infra cost (subsidized) | $2,168 | $6,504 | ~$8,550 (est.) |
| Max circuits at 2:1 | 20 | 60 | 200 |
| Revenue ceiling (Standard 1G) | $11,000 | $33,000 | $110,000 |

### Wholesale Revenue Model — Two-Layer Economics

**Layer 1: Wholesale Carrier -> Partner Carrier**

| Tier | BW | Wholesale MRC | Megaport Equiv. | Partner Savings |
|------|-----|--------------|-----------------|-----------------|
| Starter | 0.5G | $350 | $700 | 50% |
| Standard | 1G | $550 | $1,000 | 45% |
| Business | 2G | $900 | $1,400 | 36% |
| Enterprise | 5G | $1,800 | $2,200 | 18% |

**Layer 2: Partner Carrier -> Enterprise Customer**

| Tier | Partner Retail (45% markup) | Enterprise Savings vs. Megaport |
|------|----------------------------|--------------------------------|
| Starter | $508 | 27% below Megaport |
| Standard | $798 | 20% below Megaport |
| Business | $1,305 | 7% below Megaport |
| Enterprise | $2,610 | 19% ABOVE Megaport |

> **Enterprise 5G tier exceeds Megaport at 45% markup.** Adjust to 22% for price parity. Model should show both standard and adjusted markup scenarios.

### Wholesale Carrier Excel Model Structure (5 TABS)

**Tab 1 — Executive Summary** (one page, printable)
- Prospect name, network footprint, PoP locations
- Two-layer value: wholesale revenue from partner carriers + federation wholesale from MaiaEdge network
- Infrastructure cost per location (full vs. subsidized)
- Partner growth scenario (Pilot -> Growth -> Scale — 3 rows)
- 3-row competitive comparison
- Proof points: Equinix ("revolutionary and creative"), Centra ("fabric in a box")

**Tab 2 — Assumptions** (editable inputs — yellow cells)
- Per-location infrastructure costs (PBC, AWS DX, cross-connects)
- Wholesale tier pricing (Starter/Standard/Business/Enterprise)
- Partner count and avg circuits per partner
- Oversubscription ratio, PBC subsidy terms
- Multi-cloud toggle (AWS only vs. AWS + Azure + GCP)

**Tab 3 — P&L Model** (costs + revenue + partner economics in one view)
- Section A: Monthly cost per location (Full vs. Subsidized)
- Section B: Wholesale revenue by tier mix, Phase 1 and Phase 2
- Section C: Partner carrier P&L — what YOUR partners make per circuit (validates the value prop for them)
- Section D: Capacity check + 100G upgrade trigger (crossover at ~6-8 10G ports)
- Section E: Federation arbitrage — wholesale circuits from other MaiaEdge operators on same infrastructure

Partner growth scenarios (reference):

| Scale | Partners | Circuits | Monthly Revenue | Monthly GP (subsidized) |
|-------|----------|----------|-----------------|------------------------|
| Pilot | 3 | 6 | ~$3,300 | ~$1,132 |
| Growth | 10 | 40 | ~$22,000 | ~$19,832 |
| Scale | 25 | 100 | ~$55,000 | ~$52,832 |

**Tab 4 — Partner Value Calculator** (show partners what THEY make)
- Per-circuit economics at each tier for the partner carrier
- Enterprise savings vs. Megaport at each tier
- Partner markup sensitivity (30% / 45% / 60% — 3 columns)
- Illustrative: Partner with 5 Standard 1G circuits — annual gross profit

> This tab is critical — it's the tool YOUR sales team uses to recruit partner carriers. Keep it dead simple.

**Tab 5 — Competitive Comparison** (3-4 rows max)
- MaiaEdge vs. Megaport/Equinix: "They own the fabric AND the customer relationship. You own both with MaiaEdge."
- MaiaEdge vs. Lumen PCF: 20-day delivery, no operator control, no white-label
- MaiaEdge vs. Orchestration platforms (Ciena, Nokia, Juniper): 6-12mo integration, $1-10M+. MaiaEdge = 30-60 days.
- Note: 100G delivers ~13x more profit for ~4x the cost. Include upgrade economics as a one-line callout, not a separate tab.

> **Optional additions** (add ONLY if relevant): Sovereignty tab for European carriers. Multi-cloud expansion tab if prospect serves multi-cloud enterprises. Federation flywheel diagram if prospect is network-effects oriented.

### Wholesale Carrier Competitive Framing

- **#1 Competitor: Status Quo / Do Nothing** (inertia is the #1 competitor for all segments)
- **#2 Competitor: Lumen PCF** — "Lumen builds their empire; MaiaEdge empowers you to build yours." Own vs. rent.
- **#3 Competitor: Orchestration platforms** (Ciena Blue Planet, Nokia NSP, Juniper Paragon) — 6-12 month integration, $1-10M+. MaiaEdge is "fabric-in-a-box, deploy in 30-60 days."
- **#4 Competitor: Megaport/Equinix Fabric** — "They own the fabric AND the customer relationship. MaiaEdge = you own both."
- **Key win:** Federation capability cannot be replicated even with unlimited budget. NaaS providers won't help you federate with their competitors. Only MaiaEdge provides instant federation as a core capability.

### Wholesale Carrier Proof Points

- **NTT:** Network simplification, PoP acceleration. Use for: Tier 1 credibility, scale objections.
- **IENTC:** Mobile backhaul, 800+ cell towers to 20+ data centers. Use for: mobile/wireless, scale proof.
- **Equinix:** "Revolutionary and creative... abstracting complexity with their PBC approach." Use for: technical skeptics, credibility.
- **RevNet** (Colo, DFW): "If you're familiar with MegaPort... imagine having that capability between providers." Use for: NaaS comparison, federation value.
- **Centra:** "Fabric in a box, just drop it in and add water and it works." Use for: complexity objections, simplicity proof.

---

## EXCEL GENERATION INSTRUCTIONS

### Setup

```python
# pip install openpyxl --break-system-packages
import openpyxl
from openpyxl.styles import (Font, PatternFill, Border, Side, Alignment, numbers)
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1
from openpyxl.utils import get_column_letter
```

### Design Standards

**Colors:**
- Header background: `#1F4E79` (dark blue) or `#2E75B6` (medium blue)
- Header text: White (`#FFFFFF`)
- Section headers: `#D6E4F0` (light blue fill)
- Warning/UNCONFIRMED: `#FFD700` fill (yellow) with `#FF0000` text
- Positive values / savings: `#E2EFDA` (light green fill)
- Negative / cost / risk: `#FCE4EC` (light red fill)
- Editable input cells: `#FFF2CC` (light yellow fill) — shows user where to change assumptions

**Fonts:** Calibri 11pt default. Headers/labels bold. Sheet titles 14pt bold.

**Number Formats:** Currency `$#,##0`, Percentage `0.0%`, Integers `#,##0`

**Borders:** Thin on data cells, medium on section dividers.

### Tab Color Coding
- Executive Summary: Blue (`#1F4E79`)
- Architecture Notes: Gray (`#808080`)
- Assumptions: Orange (`#ED7D31`) — editable inputs
- Cost Model: Red (`#C00000`)
- Capacity Model: Purple (`#7030A0`)
- Revenue Model: Green (`#00B050`)
- Partner/Tenant Economics: Teal (`#00B0F0`)
- Competitive / ROI: Dark Yellow (`#BF8F00`)

### Formulas vs. Hardcoded Values
- **All cost inputs**: Hardcoded in Assumptions tab ONLY
- **All calculations**: Cell references/formulas — never duplicate hardcoded numbers across sheets
- **Capacity check**: REQUIRED in every revenue scenario (see formula below)

### Capacity Check (REQUIRED)
```
=IF(committed_gbps <= sellable_capacity,
   "OK: "&TEXT(committed,"0.0")&"G of "&TEXT(sellable,"0")&"G",
   "INVALID: "&TEXT(committed,"0.0")&"G EXCEEDS "&TEXT(sellable,"0")&"G")
```

### PBC Subsidy — ALWAYS Show Both Phases
- **Phase 1** (PBC = $0, subsidized by MaiaEdge)
- **Phase 2** (PBC reinstated all at once when GP > $0)
- Clear warning: "PBC reinstatement creates a P&L step-down cliff"

### UNCONFIRMED Items
- Yellow fill (`#FFD700`) on cell
- "UNCONFIRMED" in notes column
- Action item in Executive Summary pre-external checklist

---

## OUTPUT FILE NAMING

```
[ProspectShortName]_CloudOnramp_BusinessCase_v[N].xlsx
```

Save to user's workspace folder.

---

## MARKET DATA FOR REFERENCE IN MODELS

Include these data points where relevant:

**NaaS Market:** $33.2B (2025) -> $115.4B (2030), 42% CAGR. Wholesale = 26% by 2029 (~$3.8B).

**GPU-as-a-Service Market:** $4.3B (2024) -> $49.8B (2032), 35.8% CAGR.

**AWS Direct Connect:** $0.02/GB egress vs. $0.09/GB public internet = 78% savings.

**Fiber Operators in US:** ~1,900 small-scale, 2,200+ regional. 30-70% fiber utilization typical. Dark fiber at 40% utilization = tipping point for economics.

**Provisioning Speed:** Traditional carrier 30-90 days. NaaS platforms < 48 hours. MaiaEdge: minutes.

**Lumen Scale:** 340,000 route miles, 163,000+ buildings, 2,200+ data centers. $45.5B in fiber M&A in 18 months.

**Type 2 Failure Rate:** 35% of all Type 2 network orders fail. $10M+/year aggregate cost from unused physical NNIs maintained "just in case."

**VLAN Limitation:** ~4,094 usable VLAN IDs per Ethernet segment without MAC-in-MAC. Hard ceiling on customer density.

---

## PRE-EXTERNAL CHECKLIST (All Segments)

| Item | Required Status |
|------|----------------|
| PBC pricing confirmed (list vs. negotiated vs. subsidy) | Confirmed with MaiaEdge / Tim Ziemer |
| PBC subsidy commercial terms | Signed LOI or term sheet (if applicable) |
| Switch license cost | Confirmed ($0 if in PBC, or $150/mo separate) |
| Prospect cross-connect pricing | Confirmed with prospect's colo/network team |
| AWS Direct Connect port pricing | AWS list: $2.25/hr (10G), $4.50/hr (100G) |
| Fiber transport cost | Confirmed (owned = $0, leased = actual quote) |
| Capacity check | ALL presented scenarios pass |
| Over-capacity scenarios | Removed or clearly marked INVALID |
| Segment correctly identified | NeoCloud vs. Colo vs. Fiber Op vs. Wholesale |

---

## COMMON QUESTIONS AND ANSWERS

**Q: What if the prospect wants Azure ExpressRoute or GCP instead of / in addition to AWS?**
A: Add Multi-Cloud tab. Azure ExpressRoute Direct 10G: ~$6,000-$8,500/mo. GCP Interconnect 10G: ~$1,800/mo. Same PBC serves all — cost is shared, dramatically improving unit economics. 60%+ of enterprises use 2+ clouds.

**Q: What if the prospect is a colocation provider, not a NeoCloud?**
A: Use the Colocation cheatsheet, not this skill. Colos sell to tenants; NeoClouds ARE the tenant. The business case structure is different (tenant revenue model for colos, cost savings/ROI model for NeoClouds).

**Q: What about Megaport's Latitude.sh acquisition?**
A: Critical for NeoCloud and AI Infrastructure sub-segments. Megaport now bundles GPU + networking. Frame MaiaEdge as sovereignty: "own your paths, own your data, own your roadmap." Highlight lock-in risk of Megaport bundle.

**Q: What if the prospect says "Megaport already handles this for us"?**
A: Most common objection across all segments. Reframe: "Megaport handles it, but they own the customer relationship, capture the margin, and your brand disappears. When tenants need cloud connectivity, they see Megaport's portal, not yours."

**Q: 100G upgrade economics?**
A: 100G delivers ~13x more profit for ~4x the cost. 10G at full = ~$3,400/mo profit. 100G at full = ~$46,000/mo profit. Crossover point when customer density hits 15-20 per metro. See Cloud On-Ramp Sales Supplement for full 100G model.

**Q: What if the prospect's #1 competitor is "do nothing"?**
A: Status quo is the #1 competitor in EVERY segment. Create urgency: "Your competitors are talking to us too. When they provision in minutes and you take 6 weeks, who wins the deal?" Use trigger events: hyperscaler announcement nearby, leadership change, lost deal, competitor move.
