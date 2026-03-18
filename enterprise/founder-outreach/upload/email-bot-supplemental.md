# MaiaEdge Email Bot - Supplemental Reference

Content pulled from the original SKILL.md and EXAMPLES.md that adds value beyond the main prompt. No duplication.

---

## 1. MARKET SIZE

- Private connectivity market: $1.2B → $21B by 2030 (61% CAGR)
- Use selectively with CFOs or strategy-oriented buyers who want to know the market opportunity

---

## 2. AI SIGNAL STRENGTH TABLE

Use this to decide whether to use AI messaging or standard segment messaging.

| Signal Type | Specific Signals | Strength |
|-------------|-----------------|----------|
| GPU Cloud Tenants | CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI as tenants | 🔥 Strong |
| Infrastructure | Liquid cooling, 30kW+ racks, DeltaFlow cooling, power upgrades for AI | 🔥 Strong |
| Partnerships | Announced deals with GPU cloud providers, hyperscaler AI workloads | 🔥 Strong |
| Marketing | "AI-ready," "GPU cloud," "AI infrastructure," "inference hosting" in messaging | Medium |
| Geographic | Facilities in Dallas-Fort Worth, Columbus, Atlanta, Phoenix, Chicago | Medium |
| Hiring | Job posts for GPU cluster engineers, AI infrastructure roles, ML platform | Medium |

**Decision**: Strong signals → AI messaging track. Medium only → Probe further or use standard messaging with light AI angle. None → Standard segment messaging.

---

## 3. AI CORRIDOR REFERENCE

| Market | Why It Matters | Key Players |
|--------|---------------|-------------|
| Dallas-Fort Worth | Power availability, hyperscaler campuses | Lambda Labs, Crusoe, CoreWeave |
| Columbus, OH | Lambda Labs buildout, Intel Chips Act facility | Lambda Labs, AWS |
| Atlanta, GA | 176% planned capacity increase | Lambda Labs, hyperscaler expansion |
| Phoenix, AZ | Power availability, favorable climate | Vantage, QTS |
| Chicago | Lambda Labs presence, carrier density | Lambda Labs, Cologix |
| Memphis | 4,300% bandwidth growth 2023-2024 | Emerging secondary market |

---

## 4. PRE-FLAGGED AI PRIORITY ACCOUNTS

### Tier 1 (Confirmed GPU Cloud Tenant Relationships)

| Company | GPU Cloud Tenant | Notes |
|---------|------------------|-------|
| Aligned Data Centers | Lambda Labs | DeltaFlow liquid cooling (300kW/rack) |
| Cologix | Lambda Labs, CoreWeave | Columbus, Chicago, Dallas. 320MW+ committed |
| EdgeConneX | Lambda Labs | Distributed edge portfolio |
| QTS Data Centers | Hyperscaler AI workloads | Dallas-Fort Worth, Phoenix |
| Vantage Data Centers | Multiple GPU cloud | Phoenix, Dallas, Atlanta campuses |
| Stack Infrastructure | AI infrastructure buildouts | Hyperscale campus model |

### Tier 2 (AI-Ready Infrastructure, No Confirmed GPU Tenant)

Digital Realty, DataBank, T5 Data Centers, Flexential, Stream Data Centers

---

## 5. AI MESSAGING TRIGGERS BY SEGMENT

### Fiber Operators

| Signal | Messaging Approach |
|--------|-------------------|
| Dark fiber near AI corridor | "GPU cloud providers are building 2GW+ across these markets. Is your fiber positioned?" |
| Partnerships with hyperscalers or AI companies | "AI workloads need deterministic paths you can't provision fast enough" |
| Routes connecting data center clusters | Position as AI training-to-inference connectivity |
| None of the above | Use standard NNI/dark fiber messaging |

### Colocation Operators

| Signal | Messaging Approach |
|--------|-------------------|
| GPU cloud tenants (CoreWeave, Lambda Labs, Crusoe, Voltage Park) | "GPU cloud providers require 35+ cross-connects per deployment with sub-10ms latency. Are you delivering that in minutes?" |
| Liquid cooling / 30kW+ racks / DeltaFlow | "You've built the infrastructure. Now complete the AI story with instant interconnection." |
| AI-ready marketing but no confirmed tenants | "AI tenants are coming. Will your provisioning be ready?" |
| None of the above | Use standard Equinix/provisioning messaging |

### Neoclouds (GPU Cloud Providers)

**INVERTED HIERARCHY: Lead with observability, NOT deterministic paths.**

**⚠️ Sub-segment routing — match messaging to the specific neocloud type:**

| Sub-Segment | Signal | Messaging Approach |
|-------------|--------|-------------------|
| **Large-Scale GPU NeoClouds** (Crusoe, Voltage Park, Nebius, Lambda Labs) | Multi-facility GPU deployments, 100MW+ capacity, rapid expansion | "Every network interruption forces a checkpoint rollback. At $4,800/GPU/month, the recompute tax dwarfs our subscription." |
| **Tier 1 Inference Providers** (Together AI, Groq, DeepInfra, Anyscale) | Inference-as-a-service, real-time API SLAs | "Your SLA guarantees depend on network determinism you can't see today. Tail latency kills inference." |
| **AI Infrastructure Providers** (Cirrascale, Vultr, Fluidstack, DigitalOcean, Nscale) | Multi-cloud GPU platform, API-driven, developer-first | "See why inference latency varies by facility. Then fix it. Own your paths — don't rent Megaport's." |
| **Sovereign AI Clouds** (Firmus, E2E Networks, Yotta, Nscale EU) | Regulatory requirements, national AI initiatives, data sovereignty | "Prove data stays within geographic boundaries. Sovereign routing with compliance reporting." |
| **Crypto-to-AI Pivots** (IREN, Core Scientific, Northern Data Group, TeraWulf) | Former crypto mining, transitioning to AI compute | "Your crypto infrastructure wasn't built for AI traffic. See where the network is slowing you down." |

**General neocloud signals (any sub-segment):**

| Signal | Messaging Approach |
|--------|-------------------|
| Multi-facility GPU deployments (3+ locations) | "See why inference latency varies by facility. Then fix it." |
| Rapid expansion (adding facilities quarterly) | "Every new facility doesn't have to be a connectivity project." |
| Single facility expanding | Too early — monitor for second facility |

> **⚠️ CoreWeave Targeting Note:** Not an active target (MetroConnect Feb 2026 intel). Do not include in outreach campaigns.

### Network Operators

| Signal | Messaging Approach |
|--------|-------------------|
| Announcements about AI/enterprise services | "AI workloads span multiple carriers. 33% of inference latency is network. Can you prove you're not the bottleneck?" |
| Partnerships with cloud/AI companies | Emphasize multi-carrier AI paths with deterministic latency |
| Marketing about low-latency enterprise services | "Deterministic paths for AI workloads" |
| None of the above | Use standard cross-carrier/AWS-Lumen threat messaging |

---

## 6. TECHNICAL TERMINOLOGY — WHEN TO USE EACH TERM

The main prompt lists approved terms. This adds context on when each one lands best.

| Term | Best Context |
|------|-------------|
| Transport agnostic | When they ask about L2 vs L3. Merges both. |
| SRLG-aware path selection | True physical redundancy. Use with technical buyers who care about diverse routing. |
| Configuration drift | The problem protocol-free forwarding prevents. Use with network engineers managing multi-carrier paths. |
| Line-rate encryption | AES-256-GCM. Security without performance penalty. Use when security comes up. |
| White-label portal | Self-service under their brand. Use with commercial buyers and colos. |
| Layer 2.5 / WAN-Ethernet | Deep technical conversations only. Not for cold outreach. |

---

## 7. HANDLING "WHY NOT JUST USE MEGAPORT/EQUINIX?"

Three-step framework for when this comes up in conversation (not for cold emails):

1. **Acknowledge**: "They've built impressive platforms."
2. **Differentiate**: "The difference is who owns the customer relationship."
3. **Position**: "With their model, your tenant becomes their customer. With MaiaEdge, you build that capability yourself and keep the margin, the relationship, and the roadmap control."

---

## 8. CTA EFFECTIVENESS DATA

Use these stats internally to justify CTA choices, not in emails:

- Emails with clear CTAs see 28% higher response rates
- Single CTA outperforms multiple asks
- Curiosity-driven CTAs outperform meeting requests by 2-3x

---

## 9. POWER GRID CONSTRAINT USE CASE (2026)

- Texas (ERCOT): 205 GW power requests, 70% from data centers
- Facilities forced to shut down during peak demand
- MaiaEdge angle: When facilities go offline during peak demand, can workloads migrate automatically? Federation enables seamless portability.
- Use with: AI colo operators in Texas/Southwest markets

---

## 10. BUYING COMMITTEE (Fiber Operators)

Useful for multi-threading into accounts:

- CEO (economic buyer)
- VP Product/Sales (champion)
- CTO (technical validation)
- COO (operational sign-off)
- CFO (influencer)

---

## 11. MEMORABLE ANALOGIES

Use sparingly. Best for thought leadership, follow-up conversations, or when a concept isn't landing. NOT in short cold outreach.

| Analogy | Context | Use For |
|---------|---------|---------|
| "Self-driving car that only works in your driveway" | Automation stops at border | Middle-mile blind spot |
| "Fiber is like spare bedrooms before Airbnb" | Underutilized capacity | Fiber operators with dark fiber |
| "Data centers becoming Marriotts" | Can't extend reach = just real estate | Colos losing to Equinix |
| "Five chefs cooking one meal in different kitchens" | Multi-carrier chaos | MSPs/VNOs |
| "Shopify meets Uber for networks" | Marketplace participation | Federation economics |

---

## 12. THE FEDERATION FLYWHEEL

Automation → Speed → Visibility → Trust → Revenue → Automation

Each turn makes the network smarter, faster, and more valuable. Use in strategic conversations, not cold emails.

---

## 13. VISION STATEMENTS (Thought Leadership)

- "By 2030, private connectivity will behave like cloud compute — instant, elastic, deterministic."
- "Enterprises will stop buying 'lines.' They'll subscribe to reach."
- "The Internet connected everything except the networks themselves. Federation fixes that."

---

## 14. FULL SAMPLE EMAILS WITH RESEARCH (Problem-First)

These samples follow the Relevance Principle: lead with a problem statement, not an observation. Research is fuel for problem framing, not content to showcase. The prospect should think "yep, that's my life" not "this person Googled me."

### Sample 1: Fiber Operator -- CCO, Fatbeam (Tim Lieto)

**Research Summary:**
- Company: Fatbeam. Regional Fiber. 150,000 fiber miles, 8 states.
- Built: Extensive footprint, enterprise focus, hyperscaler relationships
- Gap: Provisioning likely doesn't match hyperscaler expectations, cross-carrier paths beyond footprint
- Contact: Paul, CCO. Came from Lumen (hyperscaler sales). Cares about revenue, deal velocity.
- Angle: Provisioning across an 8-state footprint still takes weeks. Enterprise customers expect better.
- Fit: EXCELLENT

**Email** (~85 words):

Subject: Fatbeam provisioning

Paul,

I'd guess NNI provisioning across an 8-state fiber footprint still takes your team weeks. Enterprise customers are starting to expect hyperscaler-speed activation, and most regional operators are still quoting 60-90 days for cross-carrier circuits.

We built infrastructure that lets your team activate services in minutes, under your brand. No routing protocols, no manual coordination. Same team that built Acme Packet.

Is this something you're thinking about?

**Why this works:** Leads with the problem (provisioning speed gap), not a personal observation. Research (8-state footprint, Lumen background) is absorbed into the problem framing, not showcased. Speed paired with ownership. One idea. Credibility dropped in naturally.

---

### Sample 2: Colocation -- CEO, KIO Networks (Tim Lieto)

**Research Summary:**
- Company: KIO Networks. Colocation. 20+ data centers, 2,000+ enterprises, LATAM.
- Built: Carrier-neutral ecosystem, significant tenant base
- Gap: Tenant connectivity requests likely go to third parties, revenue/control walking out
- Contact: Octavio, CEO. Cares about competitive positioning, customer ownership.
- Angle: Build your own fabric rather than joining someone else's.
- Fit: STRONG

**Email** (~85 words):

Subject: KIO Networks interconnection

Octavio,

When tenants across 20+ data centers ask for instant cloud connectivity, I'd guess the answer is either "call a third-party fabric provider" or "give us a few weeks." That's revenue and control walking out the door.

We help operators build their own connectivity fabric rather than joining someone else's. You keep the customer relationship, the margin, and the roadmap control. Your team provisions in minutes, not weeks.

Same team that built Acme Packet.

On your radar for this year?

**Why this works:** Leads with the problem (tenant connectivity requests going to third parties), not a company description. The "20+ data centers" detail is baked into the problem framing, not displayed as a standalone observation. No "impressive" flattery. Strong sovereignty language. CEO-appropriate strategic framing.

---

### Sample 3: Metro Dark Fiber -- CCO, BIG Fiber (Tim Lieto)

**Research Summary:**
- Company: BIG Fiber. Metro Dark Fiber / Regional Fiber. 600+ route miles, 100+ data centers.
- Built: Bay Crossing subsea route (first under Bay in decades), purpose-built 100% underground, AI-ready positioning
- Gap: Provisioning still manual. Cross-connect scheduling, VLAN coordination, LOAs. Fiber can carry 400G but activation takes weeks.
- Contact: Patton, CCO. Cares about revenue, deal velocity, differentiation.
- Angle: Infrastructure is differentiated. Provisioning isn't. That's the gap.
- Fit: EXCELLENT

**Email** (~100 words):

Subject: BIG Fiber provisioning

Patton,

I'd guess the provisioning side hasn't caught up to what you've built physically. When a hyperscaler or enterprise signs up, it's still manual. LOAs, VLAN coordination, scheduling. Fiber that can carry 400G, but activation takes weeks.

For a company marketing AI-ready infrastructure with a subsea Bay crossing, that gap matters. The infrastructure is differentiated. The provisioning isn't, yet.

We built infrastructure that lets your team provision in minutes. Protocol-free, API-driven. No routing complexity. Same team that built Acme Packet.

Dealing with something similar?

**Why this works:** Leads with the provisioning problem, not the Bay Crossing observation. Research details (400G capacity, subsea route, AI-ready positioning) are woven into the problem framing, not displayed as standalone flattery. Speed paired with ownership. One idea: great infrastructure deserves matching provisioning.

---

### Sample 4: Tier 1 Carrier -- VP Sales (Tim Lieto)

**Research Summary:**
- Company: Tier 1 Carrier. National footprint, 50+ PoPs.
- Built: SDI (Software Defined Infrastructure), same-day provisioning internally, sophisticated automation
- Gap: Cross-carrier paths beyond footprint = 60-90 days, manual LOAs, hyperscalers winning on speed
- Contact: VP Sales. Cares about deal velocity, win rates, competitive differentiation.
- Angle: You've automated internally. Extend that automation everywhere else.
- Fit: STRONG

**Email** (~95 words):

Subject: Winning cross-carrier enterprise deals

[Name],

Enterprise deals are going to hyperscalers on speed alone, even when network quality isn't there. It's a pattern we're seeing across the industry.

[Company]'s SDI delivers same-day provisioning within your footprint. The challenge is when enterprise customers need locations beyond your network. Those cross-carrier paths still take 60-90 days of coordination.

MaiaEdge extends your SDI-level automation to any carrier infrastructure. Paths that span multiple carriers provision in under 10 minutes. Your team can sell connectivity anywhere, not just on-net.

Happy to share what we're seeing with other carriers if useful.

**Why this works:** Leads with the industry problem (enterprise deals lost to hyperscalers), not a company observation. Research (SDI capability) is baked into the context bridge, not the opening line. Track A executed correctly: acknowledges internal automation, positions the cross-carrier gap. Speed paired with ownership ("your team can sell").
