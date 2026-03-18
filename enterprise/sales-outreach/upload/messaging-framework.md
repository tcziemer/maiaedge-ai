# MaiaEdge Messaging Framework V4 - n8n Email Bot Reference

**Purpose:** Consolidated messaging rules for automated email/LinkedIn generation at scale
**Version:** 4.0 | Consolidated from all segment cheat sheets + Neocloud Strategy Brief + Cloud On-Ramp Positioning
**Last Updated:** February 2026

### What Changed in V4
- **Neocloud messaging rewritten:** Inverted messaging hierarchy per Datum.net intelligence. Lead with observability and cloud on-ramp, NOT deterministic paths. Neoclouds don't know they have a network problem. They know they're slow.
- **Cloud on-ramp positioning added:** Cross-segment use case. Operators deliver cloud connectivity (AWS Direct Connect, Azure ExpressRoute) under their own brand via MaiaEdge API integrations with Equinix Fabric and Megaport. The fabric providers are backend infrastructure.
- **Megaport/Equinix = backend infrastructure:** Not competitors, not partners in the traditional sense. They are backend fabric that operators leverage through MaiaEdge. Operator owns the customer, the pricing, the brand.
- **"Carrier infrastructure" as primary identity:** MaiaEdge is carrier infrastructure. Not IaaS, not NaaS, not a platform. Purpose-built carrier infrastructure that network operators deploy.
- **Segment priority updated:** Top 3 segments are Neocloud, Colocation (standard + AI), and Fiber Operators.

---

## âš ï¸ CRITICAL: INFRASTRUCTURE VS. NAAS POSITIONING

**This is the most important differentiation in every message. Get this wrong and we sound like another NaaS provider.**

### What MaiaEdge IS

MaiaEdge delivers **carrier infrastructure** that enables network operators to build and deliver their own private connectivity services while retaining complete customer ownership.

- **Carrier infrastructure** (hardware + cloud orchestration) — not a platform, not a service, not IaaS
- **Enables operators to CREATE their own fabric** capability
- **Does NOT own circuits, sell bandwidth, or compete with operators**
- **Operators keep**: the customer, the invoice, the brand, the margin, sovereignty

### What MaiaEdge is NOT

MaiaEdge is **NOT** a Network-as-a-Service (NaaS) provider.

| NaaS Model | MaiaEdge Model |
|------------|----------------|
| They own circuits and deliver services directly to enterprises | We provide infrastructure; operators deliver the services |
| You JOIN their fabric | You BUILD your own fabric |
| Their portal, their invoice, their brand | Your portal, your invoice, your brand |
| They own the customer relationship | You own the customer relationship |
| Sovereignty lost at their edge | Sovereignty maintained across all boundaries |
| They compete with operators | We empower operators |

**⚠️ CLOUD ON-RAMP & FABRIC INTEGRATION:**

MaiaEdge integrates with Equinix Fabric and Megaport via native API. These fabric providers function as **backend infrastructure** that operators leverage through MaiaEdge. The operator's brand, pricing, and customer relationship stay entirely in-house.

**The Cloud On-Ramp Use Case:**
Cloud connectivity has historically forced operators into a difficult position. Either they redirect customers to Equinix/Megaport (losing the relationship), or they build direct hyperscaler presence (expensive and slow). MaiaEdge eliminates this choice:

- Operators deploy a PBC at their network edge; the PCE handles orchestration via API integration with Equinix Fabric and Megaport
- Multiple customers share a single fabric port, with bandwidth and service tiers enforced per tenant
- The result: direct Layer 2 private paths into AWS, Azure, or GCP, under the operator's brand, at the operator's price
- Equinix and Megaport are invisible to the end customer unless the operator chooses otherwise

**Shared Port Economics:**
Once a port is in place, every new customer adds higher-margin revenue against a fixed cost base. Cloud connectivity becomes a product that gets more profitable as it scales, not a bespoke service with proportional cost.

**Why Cloud On-Ramp Matters in Every Segment:**
- **Colocation:** Tenants stop leaving for Equinix Fabric. The colo becomes the cloud on-ramp.
- **Fiber Operators:** Cloud connectivity becomes a new revenue stream from fiber they already own. Operators in markets without local fabric access can federate with a partner that already holds a port.
- **MSP/Aggregators:** White-label cloud on-ramp under their own brand. No Equinix/Megaport dependency visible to customers.
- **Neoclouds:** Accelerated cloud and hyperscaler connectivity across their multi-facility deployments.

**In cold outreach:** Use generic terms ("third-party fabric providers," "NaaS providers") rather than naming Megaport/Equinix specifically. Save specific names for when the prospect brings them up.

### Language That Reinforces This Differentiation

**USE these phrases:**
- "Build your own fabric" / "Create your own fabric capability"
- "Infrastructure you deploy on your network"
- "Keep the customer, the margin, the control"
- "Your brand, your invoice, your portal"
- "Maintain sovereignty across network boundaries"
- "Federate while maintaining sovereignty"
- "Fabric-in-a-box" (for colos)
- "Extend your reach while keeping customer ownership"
- "Purpose-built carrier infrastructure"

**AVOID these phrases (they sound like NaaS):**
- "Connect to our fabric" (implies MaiaEdge owns a fabric)
- "Subscribe to our network" (implies service, not infrastructure)
- "Join our ecosystem" (implies dependency)
- "Our platform provides connectivity" (implies we sell bandwidth)
- "Access our network" (implies we own infrastructure)
- Any language that positions MaiaEdge as the service provider vs. the enabler

### âš ï¸ CRITICAL: Talking About Speed Without Sounding Like NaaS

When provisioning speed is the value prop, we risk sounding exactly like NaaS providers. The outcome (speed) is the same. The difference is WHO owns that capability.

**The Speed Paradox:**

| NaaS Speed Pitch | MaiaEdge Speed Pitch |
|------------------|---------------------|
| "We provision fast" (use our speed) | "You provision fast" (own the capability) |
| Speed is the product you buy | Speed is the capability you build |
| Their portal, their workflow | Your portal, your workflow |
| You're a customer of their speed | You own the speed |

**Reframe:** MaiaEdge doesn't provision fast. MaiaEdge enables YOU to provision fast.

**WRONG (sounds like NaaS):**
- âŒ "Provision in minutes"
- âŒ "Instant activation"
- âŒ "On-demand connectivity"
- âŒ "We reduce provisioning from weeks to minutes"

**RIGHT (sounds like infrastructure):**
- âœ… "Give your team the ability to provision in minutes"
- âœ… "Enable instant activation under your brand"
- âœ… "Build on-demand capability into your network"
- âœ… "Your customers see your portal, your speed"
- âœ… "Turn weeks into minutes, on your infrastructure"
- âœ… "What takes weeks today, your team does in minutes"

**Speed + Sovereignty Pairings:**

Always pair speed language with ownership language:

| Speed Claim | Pair With |
|-------------|-----------|
| "Weeks to minutes" | "...under your brand" |
| "Instant provisioning" | "...that you control" |
| "Automated activation" | "...on your infrastructure" |
| "On-demand" | "...through your portal" |

**Example Transformations:**

| Before (NaaS-sounding) | After (Infrastructure-sounding) |
|------------------------|--------------------------------|
| "Provision cross-connects in minutes" | "Give your team the ability to provision cross-connects in minutes" |
| "Instant NNI activation" | "Enable instant NNI activation under your brand" |
| "Reduce provisioning from weeks to minutes" | "What takes weeks today, your team does in minutes" |
| "On-demand cloud connectivity" | "Offer on-demand cloud connectivity through your portal" |

### How This Plays in Each Segment

| Segment | NaaS Threat | MaiaEdge Positioning |
|---------|-------------|---------------------|
| **Colocation** | Third-party fabric providers calling on your tenants, capturing interconnection revenue | Build your own fabric capability. Keep the tenant relationship, the margin, the control. |
| **Fiber Operator** | Lumen PCF positioning you as their supplier | Extend your reach through federation while maintaining sovereignty. Your customers, your brand. |
| **Network Operator** | Hyperscalers going direct, NaaS providers capturing enterprise | Build the federation layer that lets you compete. Deliver off-net as seamlessly as on-net. |
| **MSP/Aggregator** | Tier 1s and NaaS going direct to your customers | Get Tier 1 capabilities without becoming dependent on them. Maintain customer ownership. |

### The "Lumen Line"

Use this competitive hook when NaaS/PCF comes up:

> "Lumen builds their empire; MaiaEdge empowers you to build yours."

### Integration, Not Competition

MaiaEdge **integrates** with third-party fabrics via API. This is a feature, not a contradiction:

- Operators can offer cloud on-ramps (AWS Direct Connect, Azure ExpressRoute) **under their brand**
- MaiaEdge handles the API integration complexity
- The operator keeps the customer relationship and invoice
- This is "reach through integration" not "surrender to their fabric"

**In emails:** Don't name specific NaaS providers unless the prospect brings them up first. Use "third-party fabric providers" or "NaaS providers" instead.

### âš ï¸ CRITICAL: Proof Points in Cold Outreach

**Never name-drop customers in cold emails or LinkedIn messages.**

Name-dropping in cold outreach:
- Immediately signals "sales email" - prospects pattern-match and delete
- Feels like bragging, not peer-to-peer conversation
- May require customer permission for marketing use
- Undermines authenticity - Tim wouldn't name-drop in a real peer conversation

#### Anonymized Proof Point Patterns

| Named Version (DON'T USE) | Anonymized Version (USE THIS) |
|---------------------------|-------------------------------|
| "Arvig told us provisioning is now almost instantaneous" | "A regional fiber operator we work with went from 60-day NNIs to same-day activation" |
| "RevNet said it's like having Megaport capability" | "One colo operator described it as building their own fabric without the development project" |
| "IENTC has 800+ towers on MaiaEdge" | "We're running mobile backhaul at 800+ tower scale" |
| "NTT validated enterprise scale" | "Tier 1 carriers are using this for network simplification" |
| "Centra called it fabric-in-a-box" | "One operator called it 'drop it in and it works'" |
| "Equinix called our approach revolutionary" | "Even major fabric providers have validated the architecture" |

#### When TO Use Customer Names

| Context | Named References OK? |
|---------|---------------------|
| Cold emails / LinkedIn | âŒ Never |
| Discovery calls (after engagement) | âœ… Yes |
| Demos and proposals | âœ… Yes |
| "Who else is using this?" objection | âœ… Yes |
| Case study requests | âœ… Yes |
| Trade show conversations | âœ… Yes |

#### No Name-Dropping in Cold Outreach

No customer names AND no credibility anchors in cold emails or LinkedIn. The message earns the reply, not our history.

---

## THE RELEVANCE PRINCIPLE

**Relevance beats personalization. Every time.**

Personalization is mentioning their funding round, complimenting their LinkedIn post, or dropping their company name three times. It proves you researched them. It does not earn a reply.

Relevance is naming the specific problem they deal with every week, in language they use internally, and showing, in two sentences, that you might have something worth their time.

Research is essential. But its purpose is to inform which problem to lead with and confirm you're talking to the right person. The research should be invisible in the email. The prospect should think "yep, that's my life" not "this person Googled me."

**What this means in practice:**
- The email leads with a problem statement, not an observation about their business
- Company details appear only when they make the problem more specific ("NNI provisioning across your 6-state fiber footprint" not "I see you operate across 6 states")
- The goal is for the reader to feel "this is relevant to me" not "this person knows about me"
- Research findings get absorbed into problem framing, not showcased as proof of homework
- If the email would still make sense with a different company name in the header, it's not relevant enough. If it reads like a LinkedIn stalker wrote it, it's too personalized.

**Anti-personalization rules (non-negotiable in all outbound copy):**
- No "I noticed" / "I saw" / "I came across"
- No "Congratulations on..." / "Impressive growth..." / "Your recent expansion..."
- No opening with company facts as standalone observations
- No referencing their LinkedIn activity, podcast appearances, conference talks
- No "I was researching companies in [industry] and..."
- The first sentence must be about a PROBLEM or what MaiaEdge is doing, never about the prospect's company
- If you remove the company name and the email still reads as pure flattery or research showcase, rewrite it

**The specificity test:** The old test was "could this email only go to one company?" The new test is "would this person read this and think 'yep, that's my life'?" The old test incentivizes stuffing in company details. The new test incentivizes nailing the problem.

---

## SECTION 1: CLASSIFICATION LOGIC

### 1.1 ICP Classification Decision Tree

```
START
 â†“
GPU cloud provider (CoreWeave, Lambda Labs, Crusoe, Voltage Park, etc.)? â†’ YES â†’ NEOCLOUD
 â†“ NO
Owns DC facilities + offers colo? â†’ YES â†’ Check AI signals
 â”‚                                         â”œâ”€â”€ AI signals STRONG â†’ COLOCATION - AI INFRASTRUCTURE
 â”‚                                         â””â”€â”€ AI signals NONE/WEAK â†’ COLOCATION (Standard)
 â†“ NO
Owns >500mi fiber + sells commercially? â†’ YES â†’ FIBER OPERATOR
 â†“ NO
Tier 1/2 carrier OR national/global scale? â†’ YES â†’ NETWORK OPERATOR
 â†“ NO
Aggregates 3+ carriers + minimal infrastructure? â†’ YES â†’ MSP/AGGREGATOR
 â†“ NO
Uses internally + doesn't sell services? â†’ YES â†’ ENTERPRISE (Low Priority)
 â†“ NO
Pure reseller/VAR/consultancy? â†’ YES â†’ EXCLUDE - LOW VALUE
END
```

### 1.2 Classification Keywords (Instant Triggers)

| Segment | Instant Classification Keywords |
|---------|--------------------------------|
| **Neocloud** | "GPU cloud," "GPU-as-a-service," "AI cloud provider," "inference cloud," "ML infrastructure provider," company names: CoreWeave, Lambda Labs, Crusoe Energy, Voltage Park, Together AI, Anyscale, RunPod, Paperspace |
| **Colocation - AI Infrastructure** | Colo keywords + "liquid cooling," "DeltaFlow," "GPU-ready," "AI-ready data center," "high-density colocation," "30kW racks," confirmed GPU cloud tenants |
| **Colocation (Standard)** | "colocation provider," "carrier hotel," "interconnection facility," "data center operator," "meet-me room," "carrier neutral," "interconnection fabric" |
| **Fiber Operator** | "lit fiber services," "fiber to the premise," "facilities-based broadband," "fiber network operator," "dark fiber provider," "wholesale fiber," "regional fiber operator," "route miles" |
| **Network Operator** | "Tier 1 carrier," "Tier 2 carrier," "national backbone," "global carrier," "incumbent carrier," "managed connectivity services," "multi-domain orchestration" |
| **MSP/Aggregator** | "carrier broker," "white label provider," "B2B marketplace," "carrier aggregator," "network aggregator" |

### 1.3 Segment Attributes Reference

| Segment | What They Own | Revenue Model | Scale | Example Companies |
|---------|---------------|---------------|-------|-------------------|
| **Neocloud** | GPU clusters distributed across multiple colo facilities, AI/ML software stack | GPU compute rental, inference-as-a-service, training clusters | Rapidly scaling, $50M-$5B+ revenue, multi-facility | CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI |
| **Colocation - AI Infrastructure** | Buildings, meet-me rooms, metro fiber + liquid cooling, high-density power | Space/power (premium for AI), cross-connects, AI infrastructure services | 1-50+ facilities, GPU cloud tenants, $50M-$1B+ revenue | Aligned, Cologix, EdgeConneX, QTS, Vantage, Stack |
| **Colocation (Standard)** | Buildings, meet-me rooms, metro fiber (NOT route miles) | Space/power (60-80%), cross-connects (10-20%), cloud on-ramps (0-5%) | 1-50+ facilities, $10M-$500M revenue | RevNet, Centra, ARK, DataBank, Flexential |
| **Fiber Operator** | Physical fiber, optical transport (measured in route miles) | Dark fiber (IRUs), lit wavelengths, metro Ethernet, wholesale | 500-100,000 route miles, $25M-$500M revenue | Arvig, Ocean Networks, Crown Castle Fiber, Fatbeam |
| **Network Operator** | National/global network, mix of owned fiber and leased capacity | Enterprise connectivity, MPLS, wavelengths, IP transit | 50+ PoPs, 500+ employees, national/global | NTT, IENTC, AT&T, Verizon, Lumen |
| **MSP/Aggregator** | Contracts (not infrastructure), aggregate 3+ carriers | Margin on resold connectivity, managed services fees | 50-500 employees, $20M-$500M revenue | INDATEL, 11:11 Systems, Granite |

---

## SECTION 2: PERSONA CLASSIFICATION

### 2.1 Persona Types

| Persona Type | Role Focus | What They Care About | Value Prop Focus |
|--------------|------------|----------------------|------------------|
| **Decision-Maker** | Revenue, strategy, competitive position | Strategic outcomes, market timing, competitive moat | Business impact, revenue, differentiation |
| **Technical** | Architecture, operations, reliability | Protocol complexity, automation, visibility | Technical differentiation, operational efficiency |
| **Commercial** | Sales, deals, customer relationships | Deal velocity, win rates, differentiation | Speed-to-close, competitive positioning |

### 2.2 Title â†’ Persona Mapping

#### Decision-Makers / Economic Buyers
| Titles | Primary Concerns |
|--------|------------------|
| CEO, President, Managing Director, General Manager | Revenue growth, competitive positioning, M&A value |
| CFO, Chief Financial Officer, VP Finance | CapEx burden, cash flow, ROI, cost reduction |
| CRO, Chief Revenue Officer, VP Sales | Long sales cycles, losing deals on speed |
| COO, Chief Operating Officer | Operational efficiency, headcount, scale |

#### Technical Contacts
| Titles | Primary Concerns |
|--------|------------------|
| CTO, VP Engineering, VP Technology, VP Infrastructure | Protocol complexity, talent scarcity, architecture decisions |
| VP Network, VP Network Strategy, VP Network Architecture | Multi-domain orchestration, automation boundaries |
| Director Engineering, Director Network Engineering | Provisioning velocity, visibility, simplifying architecture |
| Sr. Network Engineer, Lead Network Engineer, Network Architect | Manual work, LOAs, VLAN coordination, troubleshooting |
| Principal Network Architect, Senior Network Architect | Technical validity, integration, scalability |

#### Commercial Contacts
| Titles | Primary Concerns |
|--------|------------------|
| VP Sales, VP Commercial, VP Business Development | Deal velocity, win rates, extending reach |
| VP Product, VP Product Management | Roadmap acceleration, time-to-market |
| Director Sales, Sales Director | Provisioning killing deals, competitive positioning |
| Director Business Development, VP Partnerships | Partnership friction, extending reach |

---

## SECTION 3: SEGMENT-SPECIFIC MESSAGING

### ⚠️ SEGMENT VERIFICATION BEFORE MESSAGING (MANDATORY WORKFLOW)

**Problem:** Value prop mismatching — pitching the wrong segment's pain points or messaging to a company. This is a bad look and wastes the prospect's time.

**Rule:** NEVER compose outreach or craft messaging without first completing this verification workflow. Segment assignment drives everything — the wrong segment means the wrong message.

**Workflow:**

1. **Check HubSpot segment assignment.** Look up the company in HubSpot and identify the `customer_segment` property value. If no segment is assigned, proceed to step 2 anyway — research will determine the correct segment.

2. **Run account research to confirm segment.** Do NOT blindly trust HubSpot. Research the company to verify the segment is correct. Key signals to check:
   - What do they actually own vs. lease? (Separates colo from neocloud from fiber)
   - What is their primary revenue model? (GPU compute rental = neocloud. Space/power/cooling = colo. Bandwidth/wavelengths = fiber.)
   - Do they have owned fiber infrastructure? (Fiber operator signal)
   - Are they a carrier with an ASN? (Network operator signal)
   - Do they resell others' infrastructure? (MSP/aggregator signal)

   If research contradicts HubSpot, flag for segment reassignment and use the RESEARCH-CONFIRMED segment for messaging.

3. **If contact info is provided, research the contact.** Identify their role, title, LinkedIn activity, recent posts, conference appearances, and what they personally care about. Map to the correct persona within the confirmed segment.

4. **Map the best value proposition.** Using the confirmed segment + company context + contact persona, select the value proposition that will resonate most. Every segment has different pain language, different hooks, and different proof points. Use ONLY the value props, pain language, and proof points from the confirmed segment's section below.

**Quick Reference — Segment-Specific Value Prop Anchors:**
| Segment | Primary Value Prop Anchor | NEVER Use |
|---------|--------------------------|-----------|
| Neocloud | "See why you're slow" (observability-first) | "Keep your customer" (they ARE the customer) |
| Colocation (Standard) | "Build your own fabric" / "Keep the customer" | Inference/GPU language (unless AI signals present) |
| Colocation (AI Infra) | "Complete the AI story" / "Equinix-like fabric" | Generic colo messaging without AI angle |
| Fiber Operator | "Monetize dark fiber" / "Win multi-state deals" | Colo tenant language, GPU/inference language |
| Network Operator | "Prove you're not the bottleneck" / "Compete with Lumen" | "Keep your customer" (they're selling to enterprises) |
| MSP/Aggregator | "Extend your reach without Tier 1 dependency" | Infrastructure ownership language |

---

### 3.1 COLOCATION OPERATORS (Standard)

**Use for:** Colos WITHOUT strong AI signals (no GPU cloud tenants, no liquid cooling investments)

#### Primary Hook
"Build your own fabric rather than joining someone else's. You keep the customer, the margin, the control."

#### Core Problems
- 6+ week cross-connect provisioning
- Losing tenants to third-party fabric providers
- Can't match hyperscaler interconnection experience
- Competing on space and power alone (low margin)

#### Proof Points (Anonymized for Cold Outreach)

*Note: Never name-drop customers in cold emails. Use these anonymized versions instead.*

| Proof Point | How to Reference in Cold Outreach |
|-------------|-----------------------------------|
| Regional colo offering fabric capability | "One colo operator described it as building their own fabric without the development project" |
| Simplicity validation | "An operator we work with called it 'drop it in and it works'" |
| Industry credibility | "Even major fabric providers have validated the architecture" |

*Save named references (RevNet, Centra, Equinix quote) for discovery calls and demos.*

#### Pain Points by Persona

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/President** | "We're stuck competing on price for space and power." "Lower attach rates, M&A positioning concerns." |
| **CFO** | "CapEx for connectivity infrastructure doesn't match our model." "ROI justification for multi-year development projects." |
| **CTO/VP Engineering** | "Investment protectionâ€”no rip-and-replace." "We're essentially in the network service provider business now but don't have the tools." |
| **VP Sales/CRO** | "Right now, I've got a piece of real estate. I don't have a product." "Third-party fabric reps are calling on my tenants." |
| **Sr. Network Engineer** | "Every cross-connect is a projectâ€”LOAs, truck rolls, VLAN config." "Once traffic leaves our facility, visibility dies." |
| **Director DC Operations** | "Power, cooling, physical securityâ€”and now network complexity." "We've built infrastructure but can't match hyperscale service expectations." |

#### Value Props by Persona

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/President** | Compete with hyperscale fabric providers on speed without their capital investment. Move beyond space and power to recurring, high-margin revenue streams. | "Compete on interconnection without the infrastructure investment." |
| **CFO** | OpEx subscription model. Higher attach rates without infrastructure buildout. Clear payback period. | "Higher attach rates without the infrastructure buildout." |
| **CTO/VP Engineering** | "Fabric-in-a-box" simplicity without a multi-year development project. Deploy PBCs, automate cross-connects, offer cloud on-ramps under your brand. | "Fabric-in-a-box. No multi-year development project." |
| **VP Sales/CRO** | Sell interconnection services alongside space and power. Higher attach rates, faster sales, premium pricing. | "Turn 'we need 6 weeks' into 'it's live tomorrow.'" |
| **Sr. Network Engineer** | Eliminates manual cross-connect work. 1RU device, no routing protocols. Cloud PCE handles path computation. Minutes instead of weeks. | "Your team stops managing cross-connects manually." |
| **Director DC Operations** | Add connectivity services without operational complexity. Same footprint, no new protocols to manage. | "Add connectivity services without adding operational burden." |

#### Discovery Questions (Standard Colo)

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|----------------------------|----------|
| "How do you handle tenant requests for cloud connectivity?" | "We tell them to call a third-party fabric" | "We have our own cloud on-ramps" |
| "What's your revenue split: space/power vs. connectivity?" | "90% space/power, 10% cross-connects" | "Connectivity is 30%+ of revenue" |
| "When a tenant needs a cross-connect, what's the timeline?" | "Hours per connection, LOAs, manual config" | "Minutes, fully self-service" |

#### Objection Handling (Standard Colo)

*Note: Use specific names only when the prospect brings them up first. Otherwise use "third-party fabric" or "NaaS provider."*

| Objection | Rebuttal |
|-----------|----------|
| "[NaaS provider] already handles this for us" | When tenants use a third-party fabric, they're on someone else's portal, someone else's invoice, building a relationship with someone else. You become a landlord, not a connectivity provider. MaiaEdge lets you offer the same capabilitiesâ€”your brand, your invoice, your control. |
| "We don't have the engineering resources" | That's why colos love it. No routing protocols, no BGP to configure. Deploy PBCs, connect to PCE, provision from portal. One operator called it "drop it in and add water." |
| "This sounds expensive" | Compare to what you're losing: third-party margin on every tenant connection, deals lost to 6-week provisioning. Subscription pricing, starts at 1G, scales to 100G. |
| "This sounds complex" | The opposite. No routing protocols, no BGP, no MPLS. Rack a 1RU PBC in your meet-me room, connect to cloud PCE, provision from portal. Fabric-in-a-box. |
| "Who are you?" | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology ($450M to Juniper). Two exits, $2.5B+ combined. Major fabric providers have called our approach "revolutionary and creative." |

---

### 3.2 COLOCATION - AI INFRASTRUCTURE

**Use for:** Colos with STRONG AI signals (GPU cloud tenants, liquid cooling, high-density power investments)

#### Identifying This Segment

| Signal Strength | Indicators | Classification |
|-----------------|------------|----------------|
| **STRONG â†’ This Segment** | GPU cloud tenants (CoreWeave, Lambda Labs, Crusoe, Voltage Park), liquid cooling (DeltaFlow), 30kW+ rack density | Colocation - AI Infrastructure |
| **MEDIUM â†’ Probe Further** | "AI-ready" marketing, AI corridor location, high-density power announcements | Research deeper, may be this segment |
| **NONE â†’ Standard Colo** | Traditional enterprise tenants, standard density | Use Section 3.1 |

#### Priority Accounts (Pre-Flagged)

| Company | GPU Cloud Tenant | Notes |
|---------|------------------|-------|
| Aligned Data Centers | Lambda Labs | DeltaFlow liquid cooling (300kW/rack) |
| Cologix | Lambda Labs, CoreWeave | Columbus, Chicago, Dallas. 320MW+ committed |
| EdgeConneX | Lambda Labs | Distributed edge portfolio |
| QTS Data Centers | Hyperscaler AI workloads | Dallas-Fort Worth, Phoenix |
| Vantage Data Centers | Multiple GPU cloud | Phoenix, Dallas, Atlanta campuses |
| Stack Infrastructure | AI infrastructure buildouts | Hyperscale campus model |

#### Primary Hook
"Deterministic intelligence delivery. Make the network predictable so inference systems can do their job."

#### Core Problem
Best-effort networking breaks inference performance. Token-by-token generation is latency-sensitive and intolerant of jitter. Traditional IP routing introduces variance that compounds per token. Your GPU cloud tenants need network determinism, not just fast cross-connects.

#### The Positioning Shift (vs. Standard Colo)

| | Standard Colo Pitch | AI Infrastructure Pitch |
|---|---------------------|------------------------|
| **Problem** | 6+ week provisioning, losing to third-party fabrics | Best-effort networking breaks inference performance |
| **Pain** | Manual cross-connects, ticket backlogs | Jitter and latency variance compound per token |
| **Solution** | Automated fabric-in-a-box | Deterministic private Ethernet paths |
| **Outcome** | Compete on speed | Make the network predictable so inference works |

#### Pain Points by Persona

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/President** | "We've invested in AI infrastructure but can't differentiate on connectivity." "GPU cloud providers are evaluating facilitiesâ€”connectivity is part of that decision." |
| **CTO/VP Engineering** | "We've built the power and cooling for AI. But our network is still best-effort." "Inference is latency-sensitive at the token level. Traditional IP routing introduces jitter." |
| **VP Sales/CRO** | "GPU cloud providers are asking for latency guarantees we can't make." "We're winning on power density but losing when tenants ask about inference-grade connectivity." |
| **Sr. Network Engineer** | "Best-effort routing introduces micro-jitter that breaks inference performance." "Tenants complain about inference latency spikes, but I have no visibility across the path." |
| **Director DC Operations** | "We've built 30kW racks and liquid cooling for AI workloads, but connectivity is still the same as traditional enterprise." |

#### Value Props by Persona

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/President** | Complete the AI infrastructure story. Deterministic connectivity that matches your power and cooling investments. Win GPU cloud tenants on the full stack. | "AI tenants are evaluating now. When they ask about latency guarantees for distributed inference, you have an answer." |
| **CTO/VP Engineering** | Deterministic private Ethernet paths engineered for AI inference. Known hop count, known latency characteristics, controlled failure domains. | "Your GPU cloud tenants need network determinism, not best-effort. MaiaEdge makes the path predictable so inference systems can do their job." |
| **VP Sales/CRO** | Sell inference-grade connectivity alongside your AI infrastructure. Deterministic private paths with guaranteed latency characteristics. | "GPU cloud tenants aren't asking for faster cross-connects. They're asking for deterministic paths. That's a different conversation, and a different sale." |
| **Sr. Network Engineer** | Explicit private Ethernet paths with known hop count and controlled latency. No dynamic rerouting, no queueing variance. | "Inference latency issues are impossible to troubleshoot on best-effort paths. MaiaEdge gives you deterministic transport and the visibility to prove it." |
| **Director DC Operations** | Complete your AI infrastructure investment. Engineered the facility for high-density compute. Now engineer the network for inference-grade determinism. | "You've built AI-ready facilities. MaiaEdge makes your connectivity AI-ready too." |

#### Discovery Questions (AI Infrastructure Colo)

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|----------------------------|----------|
| "Do you have GPU cloud tenants like Lambda Labs, CoreWeave, or Crusoe?" | "Yes, they're our fastest-growing segment" | "No GPU/AI tenants" (â†’ use Standard Colo) |
| "Are you investing in liquid cooling or high-density power (30kW+ racks)?" | "Yes, we're building out AI-ready infrastructure" | "Standard density only" (â†’ use Standard Colo) |
| "What are GPU cloud tenants asking for that you can't deliver today?" | "Latency guarantees, deterministic paths, visibility" | "Just faster cross-connects" |
| "How do you differentiate from other AI-ready facilities?" | "Power and cooling, but connectivity is the same" | "We have differentiated connectivity" |

#### Objection Handling (AI Infrastructure Colo)

| Objection | Rebuttal |
|-----------|----------|
| "Our GPU cloud tenants haven't asked for this" | They will. Inference performance depends on network predictability. Best-effort introduces jitter that impacts token-by-token latency. When they start debugging inference performance issues, the network is the first place they'll look. |
| "We just provide the facilityâ€”networking is their problem" | GPU cloud tenants need network determinism as much as they need power and cooling. If you're investing in liquid cooling and high-density racks, network predictability is the missing piece. MaiaEdge lets you be the full-stack AI infrastructure partner. |
| "How is this different from just faster cross-connects?" | Speed is table stakes. Determinism is the differentiator. Best-effort paths optimize for throughput and averages. Inference cares about tail latency and jitter. MaiaEdge delivers explicit paths with known hop count and controlled latency characteristics. |

---

### 3.3 NEOCLOUDS (GPU Cloud Providers)

**Use for:** GPU cloud providers building distributed inference infrastructure (CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI, Anyscale, RunPod, Nebius, Groq, Cirrascale, DeepInfra, Vultr, DigitalOcean, Fluidstack, Modal, Nscale, Firmus, E2E Networks, Yotta, etc.)

> **⚠️ CoreWeave Targeting Note:** CoreWeave told Abilash at MetroConnect (Feb 2026) that they do not have the same challenges as other NeoClouds. **Not an active target right now.** Keep as reference company for market context and segment classification, but do not include in active outreach campaigns.

**⚠️ CRITICAL: INVERTED MESSAGING HIERARCHY**

Our previous messaging led with deterministic paths between GPU clusters. Per Datum.net intelligence (Feb 2026), **that hierarchy is inverted.** Neoclouds are compute companies that accidentally became networking companies. They don't know they have a network problem. They know they're slow.

**WRONG order (old):** Deterministic paths → Observability → Cloud on-ramp
**RIGHT order (new):** Observability ("see why you're slow") → Cloud on-ramp acceleration → Deterministic paths

#### Identifying This Segment

These are the GPU cloud providers themselves, not the colos hosting them. They're building distributed GPU infrastructure across multiple facilities and need connectivity between their clusters.

| Company | Focus | Scale Indicators |
|---------|-------|------------------|
| CoreWeave | GPU cloud, enterprise AI | Multi-billion valuation, 14+ data centers |
| Lambda Labs | GPU cloud, ML training/inference | Expanding across multiple colo partners |
| Crusoe Energy | Sustainable AI compute | Stranded energy sites + colo facilities |
| Voltage Park | GPU cloud infrastructure | Rapid buildout across facilities |
| Together AI | Inference platform | Distributed inference architecture |
| RunPod | GPU cloud, serverless inference | Multi-facility, developer-focused |
| Modal | Serverless GPU compute | Distributed infrastructure |

**Key characteristic:** No WAN teams, no Kentik, no PRTG. Most have IT admins, not network architects. Together.ai's network person recently quit. These are compute companies, not networking companies.

#### The Three-Layer Pain

| Layer | Pain | What They Say |
|-------|------|---------------|
| **Layer 1: Observability** (lead here) | Zero visibility into why things are slow. No WAN monitoring, no path visibility, no hop-by-hop telemetry. | "We don't know why training jobs take 3x longer on some paths." "We have no idea what happens between facilities." |
| **Layer 2: Cloud On-Ramp** | Slow, expensive cloud connectivity. Each hyperscaler relationship is manual. Egress costs compound. | "Getting into AWS/Azure is slow and expensive." "Every cloud connection is a project." |
| **Layer 3: Deterministic Paths** | Best-effort networking breaks inference. Jitter compounds per token. But they don't frame it this way. | "Performance varies by facility." "Some paths are just slower." |

#### Primary Hook
"See why you're slow. Then fix it."

This is NOT: "Deterministic paths between your GPU clusters." That's the solution, not the entry point. Neoclouds respond to observability because they experience the symptom (slowness) without understanding the cause (network).

#### Core Value Proposition (Updated Hierarchy)

1. **Observability first:** End-to-end visibility across paths you don't own. Hop-by-hop telemetry from your GPU cluster through the colo, across the carrier, into the cloud. See exactly where latency lives.
2. **Cloud on-ramp acceleration:** Native API integration with Equinix Fabric and Megaport means cloud connectivity provisions in minutes, not weeks. Shared port model means each new cloud connection is incremental, not a project.
3. **Deterministic paths (the deeper sell):** Once they see the path data, the conversation naturally moves to "can we control this?" Explicit private Ethernet paths with known hop count and controlled latency. No best-effort variance compounding per token.

#### Neocloud Sub-Segments

The core message applies to all neoclouds. Sub-segment determines which priority you lead with and how much networking sophistication you assume.

> **For detailed sub-segment profiles (architecture, pain points, walk-away statements, opening conversations), see the Neocloud Cheatsheet.**

> **Note:** AI Data Centers (e.g., IREN, Core Scientific, Northern Data Group, TeraWulf) are covered under Section 3.2 Colocation Operators — AI Infrastructure. Cross-reference when a prospect straddles both segments.

| Sub-Segment | Examples | Lead With | Networking Sophistication |
|-------------|----------|-----------|--------------------------|
| **Large-Scale GPU NeoClouds** | Crusoe, Voltage Park, Nebius, Lambda Labs | All three layers — highlight Recompute Tax ($4,800/GPU/month at 30% interruption rate) | Variable — some have networking staff |
| **Tier 1 Inference Providers** | Together AI, Groq, DeepInfra, Anyscale | Observability + deterministic paths (inference is their product, tail latency kills SLAs) | Moderate — may have some network awareness |
| **AI Infrastructure Providers** | Cirrascale, Vultr, Fluidstack, DigitalOcean, Nscale | Cloud on-ramp + observability (API-driven, multi-cloud) — note Megaport/Latitude.sh competitive threat | Minimal — developer-first |
| **Sovereign AI Clouds** | Firmus, E2E Networks, Yotta, Nscale (EU) | Sovereign routing + observability (GDPR, EU AI Act, DPDP, CLOUD Act) | Variable — compliance-driven |
| **Crypto-to-AI Pivots** | IREN (Iris Energy), Core Scientific, Northern Data Group, TeraWulf | Observability (learning networking as they go — legacy crypto infra wasn't built for AI traffic) | Minimal — learning curve |

#### Pain Points by Persona

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/Founder** | "We're scaling across multiple facilities but connectivity is inconsistent and expensive." "Cloud egress is eating our margins." "We don't have visibility into why some paths are slower than others." |
| **VP Infrastructure** | "Every new facility is a connectivity project. Each one takes weeks." "We have no WAN monitoring. When something is slow, we can't tell if it's compute or network." |
| **VP Engineering** | "Training jobs take 3x longer on some paths and we can't explain why." "We're debugging blind across the middle mile." |
| **Network/IT Admin** | "I'm not a network engineer but I'm responsible for connectivity between our sites." "Each colo has different options and I'm learning as I go." "I have zero visibility once traffic leaves our racks." |
| **Head of Platform** | "Our customers expect consistent inference performance. Some regions are just slower and we don't know why." "Egress costs are unpredictable." |

#### Value Props by Persona

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/Founder** | See exactly where latency lives across every path, then fix it. Cloud on-ramp that scales without proportional cost. Deterministic paths when you need them. | "You're scaling GPU infrastructure across multiple facilities. The network between them is a black box. MaiaEdge opens it up." |
| **VP Infrastructure** | Stop provisioning connectivity facility by facility. One control plane, one portal, visibility everywhere. New facility? Path in minutes. | "Every new facility doesn't have to be a connectivity project. See the path, provision in minutes." |
| **VP Engineering** | Hop-by-hop telemetry across paths you don't own. When training is slow, see exactly where latency lives. Not "probably the network" but proof. | "When training jobs are slow, you need to see the path. Not guess. See it." |
| **Network/IT Admin** | You don't need to become a network expert. MaiaEdge gives you the visibility and control without the protocol complexity. No BGP, no MPLS. | "You shouldn't need to be a network engineer to see why your paths are slow." |
| **Head of Platform** | Consistent performance everywhere because you can see and control the paths. Cloud connectivity that doesn't eat your margins. | "Consistent inference performance starts with seeing the path. MaiaEdge shows you exactly where latency lives." |

#### Discovery Questions (Neoclouds)

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|----------------------------|----------|
| "How many facilities are you deployed across?" | "Multiple, and scaling rapidly" | "Single facility" (limited need) |
| "What visibility do you have into paths between facilities?" | "None. We have no WAN monitoring." | "Full visibility end-to-end" |
| "When connectivity between sites is slow, how do you diagnose it?" | "We don't. We just move the workload." | "We have Kentik/PRTG/internal tools" |
| "How do you handle cloud connectivity (AWS, Azure, GCP)?" | "Painful. Each one is a separate project." | "We have direct connections everywhere" |
| "Who manages your inter-facility networking?" | "Our IT admin / no one dedicated" | "Dedicated network team" |
| "Are you experiencing cost pressure on cloud egress?" | "Yes, egress is a significant line item" | "Egress costs are manageable" |

#### Objection Handling (Neoclouds)

| Objection | Rebuttal |
|-----------|----------|
| "We're focused on GPU infrastructure, not networking" | Exactly. You shouldn't have to think about networking. But when training jobs are slow or inference latency varies by path, the network is the variable you can't see. MaiaEdge gives you visibility without requiring you to become network experts. |
| "Our colo partners handle connectivity" | Do you know what happens between your facilities? Can you see the path? When something is slow, can you tell if it's compute or network? Colo partners handle cross-connects. MaiaEdge gives you visibility and control across the paths between them. |
| "We're building our own network team" | Building a network team to manage multi-carrier complexity is expensive and slow. MaiaEdge gives you the visibility and control without the headcount. Your team sees the paths; we handle the protocol complexity. |
| "We don't have network problems" | How do you know? Without WAN monitoring, the network is invisible. Most neoclouds we talk to discover significant path variance once they can actually see it. The question isn't whether you have network problems. It's whether you can see them. |
| "Each facility is different, how does this work?" | That's the point. MaiaEdge PBCs at each location, unified under one control plane. Your team sees one fabric, regardless of which colo or carrier is underneath. Same visibility, same provisioning, everywhere. |

#### Datum.net Channel Partnership Context

Datum.net is both a customer and a channel partner for the neocloud segment. They solve Layer 7 (proxy, anycast, DDoS). MaiaEdge solves Layer 2/3 (paths, observability, encryption). Together = full-stack answer.

- CEO Zac Smith (former CEO of Packet, acquired by Equinix) has direct relationships with decision-makers at every Tier 1 neocloud
- Datum is actively selling into Together.ai, Inference.net, RunPod, and Modal
- Their intelligence informs our messaging hierarchy (observability first, not deterministic paths first)

---

### 3.4 FIBER OPERATORS

#### Primary Hook
"Every multi-state deal you lose to provisioning delays is margin walking out the door."

#### Airbnb Analogy
"Your fiber is like spare bedrooms before Airbnb. Sitting empty until someone figured out how to monetize them."

#### Core Problems
- NNI provisioning takes weeks (LOAs, VLAN coordination, BGP config)
- Losing multi-state deals to whoever's faster
- 30-70% stranded dark fiber
- Type 2 circuits = visibility black hole (middle-mile blind spot)
- Internal fragmentation across fiber islands with different systems

#### Proof Points (Anonymized for Cold Outreach)

*Note: Never name-drop customers in cold emails. Use these anonymized versions instead.*

| Proof Point | How to Reference in Cold Outreach |
|-------------|-----------------------------------|
| Speed transformation | "A regional fiber operator we work with went from 60-day NNIs to same-day activation" |
| Fiber monetization | "One operator told us they're finally monetizing fiber that was sitting dark for years" |
| Federation reach | "We're enabling inter-regional federationâ€”operators connecting to partners they couldn't reach before" |
| International validation | "European operators are using this to solve fragmented fiber market challenges" |

*Save named references (Arvig, Ocean Networks, Ecotel) for discovery calls and demos.*

#### Pain Points by Persona

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/President** | "What's my path to $100M?" "We win deals inside our footprint, lose deals that require partners." "Revenue plateauâ€”hard to grow without building more fiber." |
| **CFO** | "40% dark fiber sitting idle while under pressure to grow revenue." "CapEx for expansion doesn't pencil without guaranteed utilization." |
| **COO** | "Can't scale service delivery without scaling headcount proportionally." "Every NNI is a project that consumes engineering resources." |
| **CTO** | "Protocol complexity (BGP/MPLS) requires specialized talent we can't find." "Type 2 circuits are a visibility black holeâ€”responsible for customer but can't see the path." |
| **VP Sales/Commercial** | "6-week provisioning kills deals." "I can't sell what I can't deliver fast." "Every enterprise deal outside our region requires a partner we can't control." |
| **VP Network/Operations** | "Different systems at each location." "Manual provisioning across our own network before we even get to partners." |
| **Director Engineering** | "I need to see end-to-end, even on paths I don't own." "Every NNI is a 60-90 day projectâ€”LOAs, VLAN coordination, BGP config." |
| **Sr. Network/Transport Engineer** | "Hours per cross-connect, LOAs, VLAN coordination." "Once traffic leaves our network, we lose all visibility." "Configuration drift across multi-carrier paths is a nightmare." |

#### Value Props by Persona

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/President** | Transform fiber to revenue asset. New revenue streams from fiber you already own. Compete with Lumen's instant provisioning. | "New revenue streams from fiber you already own." |
| **CFO** | 80-90% reduction in provisioning OpEx. Monetize stranded capacity. Turn dark fiber into deterministic services. | "80-90% reduction in provisioning OpEx." |
| **COO** | Scale service delivery without scaling headcount. Automated provisioning eliminates manual NNI work. | "Scale service delivery without scaling headcount." |
| **CTO** | No MPLS or routing protocols to manage. End-to-end visibility across Type 2 circuits. Protocol-free forwarding eliminates configuration drift. | "No MPLS or routing protocols to manage." |
| **VP Sales/Commercial** | Win deals you're currently losing on provisioning timelines. What takes weeks today, your team does in minutes. | "Win deals you're currently losing on speed." |
| **VP Network/Operations** | Unify fiber islands into one automated fabric first. Then extend automation to partners. PBCs at internal boundaries and external handoffs. | "Unify your fiber islands into one automated fabric." |
| **Director Engineering** | Provision without waiting 60 days for a partner. Hop-by-hop visibility across network boundaries. Eliminate manual BGP configuration. | "Provision without waiting 60 days for a partner." |
| **Sr. Network/Transport Engineer** | Minutes instead of weeks. Automated provisioning eliminates manual config. Real-time visibility across every hop. | "What used to take weeks is now almost instantaneous." |

#### Discovery Questions (Fiber)

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|----------------------------|----------|
| "What percentage of your fiber is generating revenue?" | "30-50%... we have stranded capacity" | "85%+ utilized" |
| "When you extend reach through NNIs, what does that look like?" | "60-90 day process... we've turned down deals" | "Automated NNI establishment" |
| "How do you handle Type 2 circuits? What visibility?" | "It's a black holeâ€”responsible but can't see" | "Full visibility through our OSS" |
| "How many multi-state deals lost to provisioning delays?" | "Multipleâ€”customers go with whoever's faster" | "We win most multi-state deals" |
| "How do you provision new paths within your own network?" | "Still manualâ€”different systems at each site" | "Fully automated end-to-end" |

#### Objection Handling (Fiber)

| Objection | Rebuttal |
|-----------|----------|
| "Our NNI process works; it just takes time" | Works externally, but what about internally? Most operators have the same friction provisioning across their own fiber islands. MaiaEdge unifies your network first, then extends that automation to partners. Every 60-90 day delay, internal or external, is a deal at risk. |
| "What about visibility into Type 2 circuits?" | Type 2 is a visibility black hole. You're responsible for the SLA but can't see the path. PBCs at each boundary give you hop-by-hop telemetry across circuits you don't own. |
| "This sounds complex" | The opposite. No routing protocols, no BGP sessions, no MPLS label distribution. That complexity is exactly what we eliminate. |
| "We want to build our own" | Most teams estimate 18-24 months and several million dollars. We've already done that work. Same team that built Acme Packet and 128 Technology. Why rebuild what exists? |
| "We've automated our internal network" | Have you? Or do you have fiber islands with separate systems at each location? Most operators we talk to have internal fragmentation before they even get to cross-carrier complexity. MaiaEdge unifies both. |

---

### 3.5 NETWORK OPERATORS (TIER 1/2 CARRIERS)

#### âš ï¸ CRITICAL: TWO DISTINCT MESSAGING TRACKS

Network Operators require research to determine which messaging track to use. The key question: **Do they have internal automation already?**

**Research signals to determine track:**

| Signal | Indicates | Messaging Track |
|--------|-----------|-----------------|
| Branded self-service portal (NetBond, Express Waves, SDI) | Internal automation exists | **TRACK A: External Extension** |
| API documentation publicly available | Internal automation exists | **TRACK A: External Extension** |
| "Instant provisioning" in their marketing | Internal automation exists | **TRACK A: External Extension** |
| No portal, no API docs, manual quoting process | Internal automation lacking | **TRACK B: Internal + External Unification** |
| Multiple acquisitions with separate systems | Internal fragmentation | **TRACK B: Internal + External Unification** |
| Job postings for "network automation" roles | Building automation, not there yet | **TRACK B: Internal + External Unification** |

---

#### TRACK A: EXTERNAL EXTENSION (Has Internal Automation)

**Use when:** Research confirms they have internal automation (branded portals, APIs, instant provisioning marketing)

**âš ï¸ CRITICAL:** Never claim they're slow at what they're fast at. Acknowledge what they've built FIRST.

**Primary Hook:** "You've automated internally. MaiaEdge extends that automation everywhere else."

**Core Problem:** Internal automation stops at domain boundaries. Cross-carrier paths still take weeks. Customer expectations set by AWS/Azure instant provisioning.

**Positioning:** MaiaEdge is the missing federation layer that extends their existing automation beyond their footprint. PBCs sit at the boundaries where their automation currently stops.

**Pain Points (Track A):**

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/Strategy** | "Lumen and AWS just announced direct enterprise connectivity. We need to match that experience." "Cross-carrier deals are profitable but operationally painful." |
| **VP Network Strategy/Architecture** | "We've automated internally, but anything beyond our footprint still takes weeks." "The gap is cross-carrier, not internal." |
| **VP Sales/Enterprise** | "Enterprise team can only sell connectivity on-net." "Cross-carrier deals take too long to close." |
| **VP Product** | "Productizing cross-carrier paths requires a multi-year dev cycle." "Can't match AWS/Lumen instant provisioning experience." |

**Value Props (Track A):**

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/Strategy** | At your scale, this transforms your addressable market. National reach without proportional investment. Match hyperscaler speed. | "At [Company]'s scale, this transforms your addressable market." |
| **VP Network Strategy/Architecture** | Not replacing internal orchestrationâ€”it's the missing federation layer that extends it. PBCs sit at the boundaries where your automation currently stops. | "Extend your automation beyond [Company]'s borders." |
| **VP Sales/Enterprise** | Your enterprise team can sell connectivity anywhere, not just on-net. Same-day provisioning for cross-carrier paths. | "Your enterprise team can sell connectivity anywhere, not just on-net." |
| **VP Product** | Productize instant cross-carrier paths without a multi-year dev cycle. Launch new connectivity products in weeks. | "Productize instant cross-carrier paths without a multi-year dev cycle." |

---

#### TRACK B: INTERNAL + EXTERNAL UNIFICATION (No Internal Automation)

**Use when:** Research shows internal fragmentation, no self-service portals, manual processes, or recent M&A with unintegrated systems

**Primary Hook:** "Unify internally first, then extend externally. One infrastructure for both."

**Core Problem:** Multi-domain orchestration complexity even within their own network. Different systems across domains mean manual handoffs. Internal fragmentation before they even get to cross-carrier complexity.

**Positioning:** MaiaEdge provides a single fabric layer across ALL boundaries, internal and external. Streamline internally first, then federate everywhere with the same infrastructure.

**Pain Points (Track B):**

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/Strategy** | "We have pockets of automation, but it's not unified across domains." "Enterprise customers expect AWS-like provisioning. We're still quoting weeks." |
| **VP Network Strategy/Architecture** | "Multi-domain orchestration is complex even within our own network." "Different systems across domains mean manual handoffs." |
| **Principal Network Architect** | "We need to unify before we can federate." "Integration complexity across acquired networks." |
| **VP Sales/Enterprise** | "Provisioning timeline varies by which domains are involved." "Can't give customers a consistent experience." |

**Value Props (Track B):**

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/Strategy** | One infrastructure that unifies your internal domains AND extends to partners. Streamline internally, then federate externally. | "Unify your network, then extend your reach. Same infrastructure for both." |
| **VP Network Strategy/Architecture** | Single fabric layer across all internal domain boundaries. Then the same infrastructure extends to partners. No separate systems. | "Unify your domains first, then federate everywhere." |
| **Principal Network Architect** | PBCs at internal boundaries and external handoffs. Centralized path computation across all domains. One control plane. | "One control plane across all your domains, internal and external." |
| **VP Sales/Enterprise** | Consistent provisioning experience regardless of which domains are involved. Then extend that speed to cross-carrier. | "Same speed everywhere, on-net and off-net." |

---

#### Proof Points (Anonymized for Cold Outreach)

*Note: Never name-drop customers in cold emails. Use these anonymized versions instead.*

| Proof Point | How to Reference in Cold Outreach |
|-------------|-----------------------------------|
| Enterprise scale validation | "Tier 1 carriers are using this for network simplification and PoP acceleration" |
| Mobile backhaul at scale | "We're running mobile backhaul at 800+ tower scale across 20+ data centers" |
| Industry credibility | "Even major fabric providers have validated the architecture" |

*Save named references (NTT, IENTC, Equinix quote) for discovery calls and demos.*

#### Discovery Questions (Network Operators)

| Question | Good Answer (Buying Signal) | Determines Track |
|----------|----------------------------|------------------|
| "Is your internal automation unified across all network domains?" | "We have pockets of automation, but it's not unified." | â†’ Track B |
| "Is your internal automation unified across all network domains?" | "Yes, internally we're automated. The gap is cross-carrier." | â†’ Track A |
| "What's your provisioning timeline for enterprise requests?" | "Still quoting weeks... customers compare us to cloud" | Either track |
| "How do you handle multi-carrier paths today?" | "Painfulâ€”LOAs, manual coordination, weeks" | Either track |
| "Do you have a self-service portal or API for provisioning?" | "Yes, for on-net." | â†’ Track A |
| "Do you have a self-service portal or API for provisioning?" | "No, it's still manual." | â†’ Track B |

#### Objection Handling (Network Operators)

| Objection | Rebuttal |
|-----------|----------|
| "We have Cisco/Juniper investments" | PBCs complement, not replace, your core routers. They sit at domain boundaries, internal and external, where your existing automation stops. We're the unification layer, not a rip-and-replace. |
| "Cross-carrier coordination is painful but manageable" | Is your internal automation truly unified across all domains? Most carriers have fragmentation internally too. MaiaEdge unifies your internal boundaries first, then extends to partners. Same infrastructure, same speed everywhere. |
| "We're building our own orchestration" | For internal domains? Great. But what about paths that cross carrier boundaries? MaiaEdge handles the federation layer that internal orchestration can't solve. We plug into your OSS/BSS. |
| "This sounds expensive" | Compare to what you're losing: enterprise deals that go to faster competitors, SLA penalties on paths you can't see, engineering hours on manual provisioning. OpEx subscription, starts at 1G, scales to 100G. |

---

### 3.6 MSP/AGGREGATORS

#### Primary Hook
"You own the customer relationship. We give you visibility into everything behind it."

#### Core Problems
- Blind to what happens inside carrier networks
- Responsible for SLA but can't see the path
- Tier 1s going direct to customers
- CapEx burden doesn't match asset-light model
- "Depends on the carrier" kills deals

#### Proof Points (Anonymized for Cold Outreach)

*Note: Never name-drop customers in cold emails. Use these anonymized versions instead.*

| Proof Point | How to Reference in Cold Outreach |
|-------------|-----------------------------------|
| Federation at scale | "We're enabling MSPs to federate across multiple regional carriers in minutes" |
| Geographic expansion | "Operators are using federation to extend reach without building new infrastructure" |
| NaaS-like capability | "One aggregator described it as having fabric provider capability without the dependency" |

*Save named references (INDATEL, Ocean Networks, RevNet) for discovery calls and demos.*

#### Pain Points by Persona

| Persona | Pain Points (Their Language) |
|---------|------------------------------|
| **CEO/President** | "We're paying Tier 1 costs without Tier 1 capabilities." "Tier 1s are going direct to our customers. We need a better experience, not just a lower price." |
| **CFO** | "CapEx for network infrastructure doesn't match our asset-light model." "Carrier dependencies limit our margin and control." |
| **VP Operations/Service Delivery** | "We're responsible for the SLA but we can't see what's happening inside carrier networks." "When there's an issue, we're stuck between our customer and the carrier pointing fingers." |
| **VP Business Development** | "Can't extend reach fast enough." "Partnership frictionâ€”every new carrier is a weeks-long integration project." |
| **VP Engineering** | "Routing complexity across multiple carriers requires expensive talent we can't afford." "No visibility into what happens inside carrier networks." "Managing BGP relationships with five carriers using a team built for one." |
| **Director Carrier Relations** | "I spend half my time chasing carriers for updates." "Provisioning depends entirely on carrier timelines." |
| **Solutions Architect** | "Each deal is a custom integration project." "Manual stitching of isolated networks for every new customer." |
| **VP Sales** | "Long sales cycles due to provisioning uncertainty." "'Depends on the carrier' kills deals." "Can't offer instant activation." |

#### Value Props by Persona

| Persona | Value Proposition | Impact Line for Email |
|---------|-------------------|----------------------|
| **CEO/President** | Tier 1 capabilities on an asset-light model. Match their speed. Keep your relationships. That's how you win. | "Tier 1 capabilities on an asset-light model." |
| **CFO** | Shift from CapEx depreciation to predictable OpEx. Eliminate 40-60% CapEx burden. Better cash flow, improved unit economics. | "Shift from CapEx depreciation to predictable OpEx." |
| **VP Operations/Service Delivery** | End-to-end visibility across all carrier relationships. Hop-by-hop telemetry, prove SLAs to customers. Stop the finger-pointing. | "Hop-by-hop visibility across all carriersâ€”prove SLA compliance." |
| **VP Business Development** | Federation in minutes. Instant partner activation. Extend reach without building fiber. | "Federation in minutes, instant partner activation." |
| **VP Engineering** | Unified visibility across all carrier relationships. MaiaEdge treats owned fiber, leased capacity, and DIA as a single cohesive fabric. No routing overhead. | "Unified visibility across your carrier partners." |
| **Director Carrier Relations** | See the path yourself. Provision without waiting on carriers. End-to-end visibility across networks you don't own. | "See the path yourself. Provision without waiting on carriers." |
| **Solutions Architect** | MaiaEdge treats owned fiber, leased capacity, and DIA as a single cohesive fabric under one control plane. Hop-by-hop visibility across networks you don't own. | "Single control plane across all your carrier relationships." |
| **VP Sales** | Instant activation instead of "depends on the carrier." Faster closes, same-day provisioning. Competitive with Tier 1s on speed. | "Instant activation instead of 'depends on the carrier.'" |

#### Discovery Questions (MSP/Aggregator)

| Question | Good Answer (Buying Signal) | Red Flag |
|----------|----------------------------|----------|
| "What visibility do you have into carrier networks?" | "Noneâ€”we're blind once traffic enters their network" | "Full end-to-end visibility" |
| "How do you prove SLA compliance to customers?" | "We rely on carrier reportsâ€”can't independently verify" | "We have our own monitoring" |
| "What's your provisioning timeline vs. direct carrier relationships?" | "Slowerâ€”we depend on carrier timelines" | "Same or faster than direct" |
| "How do you handle multi-carrier troubleshooting?" | "Painfulâ€”multiple tickets, finger-pointing" | "Unified visibility and control" |
| "Are Tier 1s competing for your customers directly?" | "Yes, and they're faster than we are" | "We win on service, not speed" |

#### Objection Handling (MSP/Aggregator)

| Objection | Rebuttal |
|-----------|----------|
| "We're asset-lightâ€”we don't want infrastructure" | MaiaEdge is OpEx, not CapEx. You're not building infrastructureâ€”you're adding a visibility and control layer over your existing carrier relationships. Same asset-light model, better capabilities. |
| "Our carrier relationships work fine" | But can you see inside their networks? Can you prove SLA compliance independently? Can you provision as fast as if the customer went direct? MaiaEdge gives you visibility and speed without replacing your carrier relationships. |
| "This sounds expensive" | Compare to what you're losing: customers going direct to Tier 1s, SLA penalties you can't dispute, deals lost to "depends on the carrier" timelines. Subscription pricing, scales with your business. |
| "Our customers don't ask for this visibility" | They ask for faster provisioning and SLA guarantees. Visibility is how you deliver both. When Tier 1s can provision in days and you're quoting weeks, visibility becomes a competitive necessity. |

---

## SECTION 4: EMAIL & LINKEDIN PATTERNS

**Important:** The patterns below are structural guides, not fill-in-the-blank templates. Every email must be driven by a company-specific angle -- the ONE thing happening at that company right now that creates an urgent, MaiaEdge-relevant problem. These patterns show the arc of a good email; the angle provides the substance.

### âš ï¸ CRITICAL: Never Use Customer Names in Cold Outreach

**Name-dropping is a red flag that screams "sales email."** It breaks the peer-to-peer tone immediately.

| Context | Use Customer Names? |
|---------|---------------------|
| Cold email | âŒ NEVER |
| Cold LinkedIn | âŒ NEVER |
| Follow-up after they reply | âœ… OK if relevant |
| Live discovery call | âœ… OK |
| Proposal/demo | âœ… OK |

**How to Reference Proof Points Without Names:**

| DON'T (Name-dropping) | DO (Anonymized) |
|-----------------------|-----------------|
| "Arvig told us it's almost instantaneous" | "One fiber operator told us what used to take weeks is now almost instantaneous" |
| "RevNet's founder said..." | "A regional colo operator described it as..." |
| "IENTC runs 800+ towers" | "We're deployed at scale - hundreds of cell towers, 20+ data centers" |
| "NTT validated our approach" | "Tier 1 carriers are using this for network simplification" |

**No credibility anchors in cold outreach.** Team credibility (Acme Packet, 128 Technology) is reserved for live conversations, discovery calls, and proposals only.

âœ… OK: "Same team that built Acme Packet and 128 Technology"
âŒ NOT OK: "Arvig is seeing great results with MaiaEdge"

---

### 4.1 Email Structure (Universal)

| Section | Content | Length |
|---------|---------|--------|
| 1. Opening | Context, direct address by name | 1 sentence |
| 2. Observation | What they've built, market position | 1-2 sentences |
| 3. Pain Hypothesis | What's probably still painful ("I'd guess...") | 1-2 sentences |
| 4. Value Statement | How MaiaEdge changes equation | 1-2 sentences |
| 5. CTA | Curiosity-driven, easy to respond | 1 sentence |

**No signature** - Auto-appended by email platform.

### 4.2 Length Guidelines

| Segment/Persona | Word Count | Rationale |
|-----------------|------------|-----------|
| Tier 1 Carriers | 125-175 words | Acknowledge sophistication, explain cross-carrier gap |
| Regional Fiber | 75-125 words | Standard pain/solution |
| Colocation (Standard) | 100-150 words | Explain fabric-in-a-box, sovereignty |
| Colocation (AI-Focused) | 100-150 words | Explain deterministic paths, inference requirements |
| MSP/Aggregators | 75-125 words | Focus on visibility, asset-light |
| Technical Buyers | 100-150 words | Include technical differentiation |
| C-Suite | 75-125 words | Strategic focus, less technical |
| LinkedIn | â‰¤300 characters | Introduction + hook + credibility |

### 4.3 Email Patterns by Segment (Angle-Driven, Problem-First Structure)

All patterns follow the Relevance Principle: lead with a problem statement driven by the company-specific angle, not an observation. Research is fuel for problem framing, not content to showcase. These patterns show the structural arc -- your company-specific angle provides the actual content. If you find yourself filling in the bracketed sections with generic segment pain instead of company-specific details, the angle is missing.

#### Tier 1 Carrier Pattern (100-160 words, soft target)
```
[Problem statement: Cross-carrier paths beyond footprint still take weeks of manual coordination]
[Context bridge: Acknowledge what they've built, baked into the problem framing]
[MaiaEdge: Extend automation beyond borders, enable your team to provision cross-carrier in minutes]
[Impact: TAILOR TO CONTACT'S ROLE]
[CTA]
```

#### Regional Fiber Operator Pattern (60-120 words, soft target)
```
[Problem statement: NNI delays losing deals, revenue from fiber sitting dark]
[Context bridge: Problem made specific with their footprint details]
[MaiaEdge: Give your team the ability to provision in minutes, under your brand]
[Impact: TAILOR TO CONTACT'S ROLE]
[CTA]
```

#### Standard Colocation Pattern (80-140 words, soft target)
```
[Problem statement: Tenant expectations vs 6+ week provisioning, third-party fabric pressure]
[Context bridge: Problem made specific with their facility/tenant details]
[MaiaEdge: Instant interconnects via automated fabric, under your brand]
[Impact: TAILOR TO CONTACT'S ROLE]
[CTA]
```

#### AI-Focused Colocation Pattern (80-140 words, soft target)
```
[Problem statement: Best-effort networking breaks inference. GPU tenants need determinism.]
[Context bridge: Problem made specific with their AI infrastructure context]
[MaiaEdge: Deterministic private Ethernet paths for AI inference]
[Impact: TAILOR TO CONTACT'S ROLE]
[CTA]
```

#### MSP/VNO Pattern (75-125 words)
```
[Opening: Their services/market position]
[Financial Pain: CapEx burden, cash flow, can't compete on speed]
[MaiaEdge: OpEx model, instant provisioning]
[Impact: TAILOR TO CONTACT'S ROLE]
[CTA]
```

### 4.4 LinkedIn Connection Request (300 chars max)

**Structure:** Introduction, Problem statement or relevant hook, Credibility, CTA. Lead with segment problems, not company flattery.

**Pattern (adapt to company-specific angle):**
```
[Sender] from MaiaEdge. [Problem statement driven by company-specific angle]. We [value statement]. Worth connecting?
```

**AI-Focused Colo LinkedIn Example:**
```
Tim from MaiaEdge. Best-effort networking breaks inference. GPU tenants need 35+ cross-connects with sub-10ms latency, provisioned in minutes. We fix that gap. Worth connecting?
```

### 4.5 CTA Hierarchy

| Tier | CTA Type | Examples | When to Use |
|------|----------|----------|-------------|
| 1. Curiosity-Driven | Ask about their situation | "Is this something you're thinking about?" / "Dealing with something similar?" / "On your radar for this year?" | Default choice. Invites dialogue, not commitment. |
| 2. Value-Offer | Offer to share insights | "Happy to share what we're seeing with similar [segment] operators." / "Can walk you through how a few operators are approaching this." | When you have relevant proof points. |
| 3. Direct Ask | Simple meeting request | "Open to a quick call?" / "Worth 15 minutes?" | For warm signals or senior executives. |

### 4.6 CTA by Persona

| Persona | CTA Approach | Example |
|---------|--------------|---------|
| CEO/C-Suite | Direct, time-conscious | "Worth 15 minutes?" |
| VP/Director | Curiosity or value-offer | "Is this on your radar?" / "Happy to share specifics." |
| Technical (CTO/Engineer) | Value-offer with specifics | "Can walk you through the architecture if useful." |
| Commercial (Sales/BD) | Problem-focused | "Dealing with something similar on the sales side?" |

### 4.7 CTA Rules

1. **ONE question only** - Never stack CTAs
2. **No vendor language** - Avoid "I'd love to..." / "I'd be happy to..."
3. **No passive asks** - Avoid "Let me know if..."
4. **No calendar links** - Too aggressive for first cold email
5. **No "quick" qualifiers** - "Quick call" signals desperation

---

## SECTION 5: COMPETITIVE POSITIONING

### 5.1 What MaiaEdge Is NOT

| Competitor Type | Their Model | MaiaEdge Difference |
|-----------------|-------------|---------------------|
| **NaaS Providers** (Megaport, Equinix Fabric) | They own the portal, the invoice, and increasingly the customer relationship. Operators become landlords. | Carrier infrastructure YOU deploy. You own the fabric, customer, and margin. Equinix and Megaport function as backend infrastructure via native API integration. The operator's brand stays front. |
| **Lumen PCF** | You become their customer on their fabric. | Infrastructure you own and control. "Lumen builds their empire; MaiaEdge empowers you to build yours." |
| **SD-WAN** | Sits at enterprise branches (last mile). | Carrier infrastructureâ€”PBCs sit at network boundaries (middle mile). Different layer, different buyer. |
| **Router Replacement** | Rip-and-replace Cisco/Juniper. | We complement, not replace. PBCs sit at the edge. No rip-and-replace. |

### 5.2 Competitive Hooks

**âš ï¸ PARTNERSHIP NOTE:** Use generic language ("third-party fabric providers," "NaaS providers") in cold outreach. Only use specific competitor names when the prospect brings them up first or in internal training contexts.

| Context | Positioning Hook |
|---------|------------------|
| Third-party fabrics (generic) | "Build your own fabric rather than joining someone else's." |
| NaaS providers (generic) | "Keep the customer, the margin, the control." |
| Lumen PCF | "Lumen builds their empire; MaiaEdge empowers you to build yours." |
| AWS/Hyperscalers | "Match hyperscaler speed without surrendering customer relationships." |

---

## SECTION 6: WRITING STYLE & QUALITY RULES

### 6.1 Writing Style Rules

**DO:**
- âœ… Periods for sentence breaks (not em dashes)
- âœ… Direct address (no "As a product leader")
- âœ… Active voice
- âœ… Specific numbers for cost reduction (80-90%)
- âœ… Reference their actual business
- âœ… Acknowledge what they've built
- âœNo credibility anchors in cold emails (no Acme Packet, no 128 Technology)
- âœCompany-specific angle drives the email (not segment framework as template)
- âœ… **Pair speed claims with ownership language** ("your team," "under your brand," "on your infrastructure")
- âœ… Use "weeks to minutes" instead of specific day counts

**DON'T:**
- âŒ Em dashes (â€”) - NEVER use, replace with periods or commas
- âŒ Generic greetings ("hope this finds you well")
- âŒ "Just wanted to reach out"
- âŒ Role labels ("As a CEO...")
- âŒ "I noticed..." / "Saw your post..." / "Following your work..." (see The Relevance Principle: research is fuel, not content. Also no "Congratulations on..." / "Impressive...")
- âŒ Lead with "session-smart routing"
- âŒ Claim they're slow at what they're fast at (especially Tier 1s)
- âŒ "Revolutionary" or "game-changing" (show, don't tell)

### 6.2 Technical Terminology

**Always Use (Customer-Facing):**
- Automated provisioning / Zero-touch provisioning
- Protocol-free forwarding
- Centralized path computation
- API-driven activation
- Middle-mile blind spot (the core problem)
- Federated Private Networking (solution name)
- Deterministic paths (especially for AI-focused colos)
- Deterministic private Ethernet paths (AI inference positioning)

**Use Sparingly / With Context:**
- Session-smart routing (founder credibility, CTO deep-dives only)
- PBC / Path Border Controller (after explaining "1RU edge device")
- PCE / Path Computation Engine (after explaining "cloud orchestrator")

**Never Use in Cold Outreach:**
- Session-smart routing as a lead
- Internal product codenames
- "Revolutionary" or "game-changing"

### 6.3 Quality Checklist (Every Email)

- [ ] Research completed (company + contact)
- [ ] Segment correctly identified
- [ ] AI signals checked (for colos only)
- [ ] Network Operator track determined (A: External Extension vs. B: Internal + External)
- [ ] Correct value prop track selected
- [ ] Pain points match contact's role
- [ ] Claims based on research, not assumptions
- [ ] Within word limits
- [ ] No em dashes (â€”)
- [ ] No banned phrases / cheesy personalization
- [ ] **NO CUSTOMER NAMES:** Never name-drop customers in cold outreach (use anonymized proof points)
- [ ] **INFRASTRUCTURE POSITIONING CHECK:** Does the email position MaiaEdge as infrastructure you deploy (correct) or a service you subscribe to (wrong)?
- [ ] **SOVEREIGNTY CHECK:** Does the email reinforce that the operator keeps the customer, margin, and control?
- [ ] **SPEED/OWNERSHIP PAIRING CHECK:** If speed is mentioned, is it paired with ownership language? ("your team," "under your brand," "on your infrastructure")
- [ ] NO credibility anchors (no Acme Packet, no 128 Technology)
- [ ] Company-specific angle drives the email (not generic segment pain)
- [ ] CTA is low-friction and matches persona
- [ ] Sounds peer-to-peer, not vendor pitch

### 6.4 Common Failure Modes

| Failure | Description | Fix |
|---------|-------------|-----|
| **Customer Name-Dropping** | Using specific customer names (Arvig, RevNet, NTT) in cold emails | Anonymize: "One fiber operator" not "Arvig told us." Save names for live conversations. |
| **Sounding Like NaaS** | Using language that implies MaiaEdge owns a fabric or sells bandwidth | Use "build your own fabric" not "connect to our fabric." MaiaEdge is infrastructure, not a service. |
| **Unpaired Speed Claims** | Saying "provision in minutes" without ownership context | Always pair speed with ownership: "your team provisions in minutes" or "instant activation under your brand" |
| Wrong Segment Messaging | Using fiber messaging ("monetize dark fiber") for a colo | Match value prop to infrastructure type |
| Claiming Tier 1s Are Slow | AT&T, Verizon, Lumen have sophisticated internal automation | Determine Track A vs. B through research. Gap may be cross-carrier OR internal unification. |
| Wrong Network Operator Track | Using "extend your automation" when they don't have internal automation | Research their portal/API status first. Use Track B if fragmented internally. |
| Mismatched Pain/Role | Operational efficiency to CEO (they care about revenue) | Match pain to persona from matrices |
| Missing AI Signal Detection | Using standard colo messaging for Aligned or Cologix | Check AI signals for every colo account |
| Standard Messaging for AI Colo | "Compete with third-party fabrics" when they have Lambda Labs as a tenant | Use AI inference positioning |
| Skipping Research for "Small" Companies | Assuming regional operators don't need research | Research EVERY company. No assumptions are safe. |
| **Sovereignty Language Missing** | Not reinforcing that operator keeps customer/margin/control | Every email should reinforce ownership/sovereignty benefit |

---

## SECTION 7: RESEARCH PROCESS

### 7.1 Mandatory Research Queries

**Before writing ANY email, complete these searches:**

1. `[Company] cloud connectivity provisioning` / `network automation services`
2. `[Company] API portal self-service instant provisioning`
3. `[Company] cross-carrier paths multi-carrier connectivity`
4. `[Company] expansion announcement 2024 2025 2026`
5. **(If Colo or Fiber in AI Corridor):** `[Company] CoreWeave Lambda Labs Crusoe` / `[Company] liquid cooling high-density`

### 7.2 Research Output Format

```
Company: [Name]
Segment: [Colo | Fiber | Network Operator | MSP]
âœ… What They've Built: [Their fast services/automation, product names]
âŒ The Gap: [Where automation stops, cross-carrier challenges]
ðŸ¤– AI Signals: [Found / Noneâ€”determines messaging track]
ðŸŽ¯ MaiaEdge Positioning: [One sentence that respects what they've built]
FIT: EXCELLENT | STRONG | MODERATE | WEAK
```

### 7.3 Contact Research Output Format

```
CONTACT CONTEXT
Name: [Full Name]
Title: [Title]
Role Type: [Decision-Maker / Technical / Commercial / Operations]
Tenure: [X years at company]
Background: [Technical / Business / Hybrid]
Career Path: [Notableâ€”e.g., "came from Lumen", "promoted from engineering"]

ROLE-BASED PRIORITIES (from matrix)
This role typically cares about: [from matrix]
Lead with: [from matrix]
Avoid: [from matrix]

VALUE PROP MAPPING
Company Gap (from account research): [the specific problem]
How this role feels that gap: [operational pain / strategic concern / revenue impact]
Value prop to emphasize: [the one that maps to their priorities]
```

### 7.4 Research Signal -> Problem Framing (Relevance-First)

Research signals tell you WHICH PROBLEM to lead with, not which OBSERVATION to make. The email should lead with the problem, with research details absorbed into the framing.

| If Research Shows... | Problem to Lead With... |
|---------------------|--------------|
| Recent promotion/new role | Lead with the problem they’re likely prioritizing. Don’t open with "As you’re setting priorities." |
| Company just announced expansion | Lead with the provisioning problem expansion creates. "Multi-state deals are getting lost to provisioning timelines." Not "[Company]’s expansion is impressive." |
| Technical background, now in leadership | Balance: strategic outcome + one technical proof point. Lead with the problem, not their background. |
| Company hiring aggressively | "Scaling the team is one way. Scaling without headcount is another..." |
| Long tenure at company | They know the problem better than you. Lead with a specific pain point they’ve lived with. Don’t flatter their history. |
| Came from competitor/carrier | Cut to the chase, assume knowledge: "You know the provisioning challenge..." |
| Recent M&A activity | Lead with the complexity problem: "Network complexity compounds with every integration." |
| Competing in hyperscaler-dominated market | "Enterprise customers expect AWS-like speed..." |
| Dark fiber / underutilized assets | "Fiber sitting dark is margin waiting to happen..." |
| Multi-state footprint | "Every multi-state deal lost to provisioning delays is margin walking out..." |
| **GPU cloud tenants confirmed** | Lead with the infrastructure gap: "GPU cloud tenants need 35+ cross-connects per deployment with sub-10ms latency. Most colos can’t deliver that in minutes." |
| **Liquid cooling / AI infrastructure investment** | Lead with the connectivity gap: "AI inference density is going up. The question is whether the connectivity layer matches the compute investment." |
| **AI-ready marketing, no confirmed tenant** | "AI tenants are evaluating facilities now. When they ask about latency guarantees for distributed inference, what’s the answer?" |

---

## SECTION 8: n8n BOT DECISION LOGIC

### 8.1 Classification Flow (Bot 1)

```
INPUT: Company name, website, description

STEP 1: SEGMENT CLASSIFICATION
â”œâ”€â”€ Check for Neocloud indicators FIRST (GPU cloud provider, not colo)
â”‚   â””â”€â”€ If CoreWeave, Lambda Labs, Crusoe, Voltage Park, Together AI, etc. â†’ NEOCLOUD
â”œâ”€â”€ Check for instant classification keywords
â”œâ”€â”€ Apply decision tree logic
â””â”€â”€ OUTPUT: Segment [Neocloud | Colo - AI Infrastructure | Colo (Standard) | Fiber | Network Operator | MSP | Enterprise | Exclude]

STEP 2: SEGMENT-SPECIFIC TRACK DETERMINATION
â”œâ”€â”€ IF Neocloud â†’ No sub-track needed (they ARE the inference customer)
â”œâ”€â”€ IF Colo â†’ Check for AI signals (GPU tenants, liquid cooling, AI corridor)
â”‚   â”œâ”€â”€ AI signals STRONG â†’ Colo - AI Infrastructure
â”‚   â””â”€â”€ AI signals NONE/WEAK â†’ Colo (Standard)
â”œâ”€â”€ IF Network Operator â†’ Check for internal automation
â”‚   â”œâ”€â”€ Search for self-service portal, API docs, branded products
â”‚   â””â”€â”€ OUTPUT: has_internal_automation [True | False]
â”œâ”€â”€ IF Fiber â†’ No sub-track needed
â””â”€â”€ IF MSP â†’ No sub-track needed

STEP 3: COMPANY RESEARCH
â”œâ”€â”€ Run 4-5 mandatory search queries
â”œâ”€â”€ Document what they've built
â”œâ”€â”€ Document the gap (internal vs. external for Network Ops)
â”œâ”€â”€ FOR NEOCLOUDS: Focus on multi-facility deployment, connectivity challenges
â””â”€â”€ OUTPUT: Research summary

OUTPUT: {segment, has_internal_automation (network ops only), research_summary, fit_score}
```

### 8.2 Persona Classification Flow (Bot 2)

```
INPUT: Contact name, title, company segment, company track

STEP 1: TITLE â†’ PERSONA MAPPING
â”œâ”€â”€ Match title to persona type (Decision-Maker | Technical | Commercial)
â”œâ”€â”€ Identify specific role within persona type
â””â”€â”€ OUTPUT: persona_type, role_name

STEP 2: CONTACT RESEARCH
â”œâ”€â”€ LinkedIn tenure check
â”œâ”€â”€ Background analysis (Technical vs. Business)
â”œâ”€â”€ Career path signals
â””â”€â”€ OUTPUT: contact_context

STEP 3: VALUE PROP SELECTION
â”œâ”€â”€ Match segment + track + persona to value prop matrix
â”œâ”€â”€ Select impact line for email
â”œâ”€â”€ Select CTA based on persona
â””â”€â”€ OUTPUT: value_prop, impact_line, cta

OUTPUT: {persona_type, role_name, contact_context, value_prop, impact_line, cta}
```

### 8.3 Email Generation Flow (Bot 3)

```
INPUT: company_research, contact_research, segment, persona

STEP 1: SELECT EMAIL PATTERN
â”œâ”€â”€ Match segment to email pattern
â”œâ”€â”€ Apply segment-specific pattern:
â”‚   â”œâ”€â”€ Neocloud â†’ Neocloud Pattern (distributed inference, multi-facility)
â”‚   â”œâ”€â”€ Colo - AI Infrastructure â†’ AI Infrastructure Pattern (deterministic for tenants)
â”‚   â”œâ”€â”€ Colo (Standard) â†’ Standard Colo Pattern (fabric-in-a-box, third-party fabric competition)
â”‚   â”œâ”€â”€ Network Op + has_internal_automation=True â†’ Track A Pattern
â”‚   â””â”€â”€ Network Op + has_internal_automation=False â†’ Track B Pattern
â””â”€â”€ OUTPUT: email_pattern

STEP 2: SELECT PAIN POINTS
â”œâ”€â”€ Match persona + segment to pain points from matrix
â”œâ”€â”€ Incorporate research findings
â””â”€â”€ OUTPUT: pain_hypothesis

STEP 3: SELECT VALUE PROP
â”œâ”€â”€ Match persona + segment to value prop from matrix
â”œâ”€â”€ Select impact line
â”œâ”€â”€ **VERIFY:** Value prop reinforces infrastructure positioning (not NaaS)
â”œâ”€â”€ **FOR NEOCLOUDS:** Shift from "keep your customer" to "see your paths." Lead with observability, not deterministic paths. They know they're slow. They don't know why.
â””â”€â”€ OUTPUT: value_statement

STEP 4: SELECT CTA
â”œâ”€â”€ Match persona to CTA type
â”œâ”€â”€ Select specific CTA from hierarchy
â””â”€â”€ OUTPUT: cta

STEP 5: ASSEMBLE EMAIL
â”œâ”€â”€ Apply email structure
â”œâ”€â”€ Check word count limits
â”œâ”€â”€ **VERIFY:** Email includes sovereignty/ownership language
â”‚   â””â”€â”€ **FOR NEOCLOUDS:** Focus on observability and visibility, not deterministic paths or customer ownership
â”œâ”€â”€ Validate against quality checklist
â””â”€â”€ OUTPUT: final_email

STEP 6: QUALITY VALIDATION
â”œâ”€â”€ Check for banned phrases
â”œâ”€â”€ Check for em dashes
â”œâ”€â”€ **CHECK:** No NaaS-sounding language
â”œâ”€â”€ **CHECK:** Sovereignty/ownership reinforced (observability/visibility for Neoclouds)
â”œâ”€â”€ **CHECK:** Speed claims paired with ownership ("your team," "under your brand")
â”œâ”€â”€ Verify NO credibility anchors in cold outreach
â”œâ”€â”€ Verify within word limits
â””â”€â”€ OUTPUT: quality_score, issues_found

OUTPUT: {email, linkedin_message, quality_score, issues_found}
```

### 8.4 Fallback Messaging Matrix

When research is incomplete, use segment + track + persona defaults:

| Segment | Track | Persona | Fallback Hook | Fallback Pain | Fallback CTA |
|---------|-------|---------|---------------|---------------|--------------|
| Colo (Standard) | - | Decision-Maker | "Build your own fabric" | "Losing tenants to third-party fabrics" | "On your radar?" |
| Colo (Standard) | - | Technical | "Fabric-in-a-box" | "Manual cross-connect work" | "Dealing with something similar?" |
| Colo - AI Infrastructure | - | Decision-Maker | "Deterministic intelligence delivery" | "Connectivity doesn't match compute investment" | "Worth 15 minutes?" |
| Colo - AI Infrastructure | - | Technical | "Network predictability for inference" | "Best-effort breaks AI workloads" | "Dealing with latency challenges?" |
| Neocloud | - | Decision-Maker | "See why you're slow, then fix it" | "No visibility into paths between facilities" | "Worth a conversation?" |
| Neocloud | - | Technical | "See the path. Not guess. See it." | "Zero WAN monitoring across facilities" | "How do you diagnose slowness between sites?" |
| Fiber | - | Decision-Maker | "Multi-state deals walking out the door" | "NNI provisioning takes weeks" | "Is this relevant?" |
| Fiber | - | Technical | "Unify your fiber islands" | "Type 2 visibility black hole" | "Dealing with something similar?" |
| Network Op | Track A (Has automation) | Decision-Maker | "Extend automation everywhere else" | "Cross-carrier still takes weeks" | "Worth a conversation?" |
| Network Op | Track A (Has automation) | Technical | "Missing federation layer" | "Automation stops at your border" | "Can walk you through the architecture" |
| Network Op | Track B (No automation) | Decision-Maker | "Unify internally, then extend externally" | "Multi-domain orchestration complexity" | "Worth a conversation?" |
| Network Op | Track B (No automation) | Technical | "Single fabric across all boundaries" | "Internal fragmentation" | "Can walk you through the architecture" |
| MSP | - | Decision-Maker | "Tier 1 capabilities, asset-light" | "Tier 1s going direct to customers" | "On your radar?" |
| MSP | - | Technical | "Visibility into everything behind it" | "Blind to carrier networks" | "Dealing with something similar?" |

### 8.5 Value Prop Selection Logic

```
# Segment determines primary value prop matrix

IF segment = "Neocloud"
    â†’ Neocloud Track (distributed inference, deterministic paths between clusters, visibility across facilities)
    
IF segment = "Colo - AI Infrastructure"
    â†’ AI Infrastructure Track (deterministic paths for AI tenants, complete the AI story, inference-grade connectivity)

IF segment = "Colo (Standard)"
    â†’ Standard Colo Track (fabric-in-a-box, third-party fabric competition, tenant ownership)
    
IF segment = "Fiber"
    â†’ Fiber Track (NNI speed, dark fiber monetization, Type 2 visibility, sovereignty)
    
IF segment = "Network Operator" AND has_internal_automation = TRUE
    â†’ Track A: External Extension (extend automation beyond borders, federation layer)
    
IF segment = "Network Operator" AND has_internal_automation = FALSE
    â†’ Track B: Internal + External Unification (unify first, then federate)
    
IF segment = "MSP"
    â†’ MSP Track (visibility, asset-light, Tier 1 competition, customer ownership)

# ALWAYS reinforce:
# - Operator keeps customer, margin, control (except Neoclouds - they ARE the customer)
# - Infrastructure you deploy, not service you subscribe to
# - Sovereignty maintained across boundaries

# NEOCLOUD-SPECIFIC NOTE:
# Neoclouds are the GPU cloud providers themselves, not colos serving them.
# They're deploying THEIR infrastructure, connecting THEIR clusters.
# Sovereignty language shifts from "keep your customer" to "control your paths"
```

---

## APPENDIX: QUICK REFERENCE TABLES

### A.1 ICP â†’ Primary Hook

| ICP | Primary Hook |
|-----|--------------|
| Colocation (Standard) | "Build your own fabric rather than joining someone else's. You keep the customer, the margin, the control." |
| Colocation - AI Infrastructure | "Deterministic intelligence delivery. Make the network predictable so inference systems can do their job." |
| Neoclouds | "See why you're slow. Then fix it." (Lead with observability, not deterministic paths. They're compute companies, not networking companies.) |
| Fiber Operator | "Every multi-state deal you lose to provisioning delays is margin walking out the door." |
| Network Operator (Track A) | "You've automated internally. MaiaEdge extends that everywhere else." |
| Network Operator (Track B) | "Unify internally first, then extend externally. One infrastructure for both." |
| MSP/Aggregator | "You own the customer relationship. We give you visibility into everything behind it." |

### A.2 Segment â†’ Proof Point (Anonymized for Cold Outreach)

*Note: Never name-drop customers in cold emails. Save named references for discovery calls and demos.*

| Segment | Anonymized Proof Point for Cold Outreach |
|---------|------------------------------------------|
| Colocation (Standard) | "One colo operator described it as building their own fabric without the development project" |
| Colocation (Standard) | "An operator we work with called it 'drop it in and it works'" |
| Colocation - AI Infrastructure | "Even major fabric providers have validated the architecture" |
| Neoclouds | (Emerging segment - use general deterministic path messaging) |
| Fiber Operator | "A regional fiber operator went from 60-day NNIs to same-day activation" |
| Network Operator | "Tier 1 carriers are using this for network simplification" |
| MSP/Aggregator | "We're enabling multi-carrier orchestration at scale" |

### A.3 Infrastructure vs. NaaS Quick Check

Before sending any email, verify:

| âœ… CORRECT (Infrastructure) | âŒ WRONG (Sounds like NaaS) |
|----------------------------|----------------------------|
| "Build your own fabric" | "Connect to our fabric" |
| "Infrastructure you deploy" | "Subscribe to our network" |
| "Your brand, your invoice" | "Join our ecosystem" |
| "Keep the customer and margin" | "Access our platform" |
| "Maintain sovereignty" | "Our network provides..." |

### A.3.1 Speed Claims Quick Check

Speed claims must be paired with ownership language:

| âŒ WRONG (NaaS-sounding) | âœ… CORRECT (Infrastructure) |
|--------------------------|----------------------------|
| "Provision in minutes" | "Your team provisions in minutes" |
| "Instant activation" | "Enable instant activation under your brand" |
| "On-demand connectivity" | "Offer on-demand through your portal" |
| "We reduce weeks to minutes" | "What takes weeks, your team does in minutes" |
| "Fast provisioning" | "Build fast provisioning capability into your network" |

### A.4 Network Operator Track Determination

| Research Finding | Track | Hook |
|------------------|-------|------|
| Self-service portal exists | Track A | "Extend your automation beyond your borders" |
| API documentation available | Track A | "Extend your automation beyond your borders" |
| Branded instant provisioning products | Track A | "Extend your automation beyond your borders" |
| No portal, manual quoting | Track B | "Unify internally, then extend externally" |
| Recent M&A with unintegrated systems | Track B | "Unify internally, then extend externally" |
| Job postings for automation roles | Track B | "Unify internally, then extend externally" |

### A.5 Team Credibility

**Acme Packet**: Created the Session Border Controller (SBC), used by 90% of carriers. Sold to Oracle for $2.1 billion.

**128 Technology**: Largest acquisition Juniper ever made. Routing brain behind Juniper Mist.

**Combined exits**: $2.55B in telecom infrastructure

**How to weave in (live conversations and proposals ONLY, never in cold outreach):**
- "The team that built Acme Packet and 128 Technology is now solving [problem]..."
- "Same team that built carrier infrastructure used by 90% of operators..."

### A.6 The Sovereignty Principle

Every email should reinforce that the operator maintains:

1. **Customer ownership** - Their customer, their relationship
2. **Invoice/brand** - Their portal, their invoice, their brand
3. **Margin** - They capture the value, not a third party
4. **Control** - Policy control across all boundaries
5. **Visibility** - End-to-end, even across Type 2 circuits

This is the fundamental difference from NaaS. Never let an email go out without reinforcing at least one of these elements.

---

*End of Document*
*Version 4.0 | Consolidated Messaging Framework + Neocloud Strategy + Cloud On-Ramp Positioning | February 2026*
