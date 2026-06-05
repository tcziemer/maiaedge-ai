---
name: segment-classification
description: Classify companies into MaiaEdge customer segments and apply segment-specific messaging. Use when determining what type of company a prospect is (fiber operator, colocation, neocloud, network operator, MSP) and what messaging angle to use. Includes exclusion list and segment-specific pain points, angles, and positioning.
---

# MaiaEdge Segment Classification & Messaging

## Reference Files (read before executing)

- `context/account-tiering/sub-segment-qualification.md` (file 06 in the Phase 3 primary references) - the consolidated sub-segment qualification reference. Authoritative for:
  - §3 D1 Global Disqualifiers (hyperscaler / equipment vendor / government / academic / OTT / pure-software / logistics-shipping patterns)
  - §4 D2 Wholesale-arm policy (which record gets which sub-segment for split-book operators)
  - §5 D3 Disambiguation flowcharts (one per ICP - Colo, Fiber, NeoCloud, Network Op, MSP/Aggregator, Enterprise)
  - §6 Per-sub-segment classification rules with anchor accounts and confidence calibration
- `context/account-tiering/enrichment-protocols.md` - D5 v2 operational layer (confidence calibration, catch-all guard rules, R2 / D7 routing). Read alongside file 06 when applying classification.
- `context/hubspot/property-schema.md` - `customer_segment` / `company_sub_segment` enum values, `segmentation_confidence` definitions, `hs_is_target_account` semantics.
- `context/copy-strategy/segment-messaging.md` - segment messaging framework (full version of the angles below).

## Step 0: D1 Global Disqualifier Check (run FIRST, before any segment routing)

Before invoking any ICP-specific flowchart, run the D1 Global Disqualifier check from file 06 §3. Match the company's domain, name, and one-line description against the D1 patterns:

| D1 Category | Examples | Resolution |
|---|---|---|
| Hyperscaler / cloud platform | AWS, Azure, GCP, Oracle Cloud, IBM Cloud, Alibaba Cloud | `customer_segment = "Other"` (competitive / partner reference) |
| Equipment vendor | Cisco, Juniper, Arista, Nokia, Ciena, Nvidia, Dell, HPE, Supermicro | `customer_segment = "Other"` (competitive / partner reference) |
| Government / public sector entity | Federal agencies, state/local government, military, public-sector primes operating in classified env | `customer_segment = "Flagged for deletion"` unless commercial arm verified (FedRAMP-gated otherwise) |
| Academic / research institution | Universities, national labs, research consortia (NREN equivalents) | `customer_segment = "Flagged for deletion"` |
| OTT / content / streaming | Netflix, Disney+, Hulu, Spotify, social-media platforms | `customer_segment = "Other"` |
| Pure software / SaaS (no owned network or compute) | App vendors, ERP, CRM, dev tools, "AI software" with no GPU infra | `customer_segment = "Flagged for deletion"` (or `Other` if a known partner / competitor) |
| Logistics / shipping carrier | FedEx, UPS, DHL, USPS, freight brokers, shipping platforms | `customer_segment = "Flagged for deletion"` |

If a D1 match is found:
1. Set `customer_segment` per the table above (`Other` if useful as competitive / partner reference, `Flagged for deletion` if no MaiaEdge value).
2. Skip sub-segment classification - leave `company_sub_segment` blank.
3. Add a HubSpot note citing the D1 rule: `D1 disqualifier - [category] - file 06 §3`.
4. **Halt rule:** if the disqualifier would evict a record that has `type = "Customer"` OR any associated deal past `closedwon` (won or lost), HALT. Do not write `customer_segment = "Flagged for deletion"`. Flag for Cooper review with the rule citation and customer/deal context. (When the write does NOT halt and proceeds, the `flagged_for_deletion_reason` companion write in step 5 applies.)
5. **`flagged_for_deletion_reason` companion write (REQUIRED when the write sets `Flagged for deletion`):** In the SAME HubSpot update that sets `customer_segment = "Flagged for deletion"`, also set `flagged_for_deletion_reason` (multi-line text). For a D1 disqualifier eviction (gov / academic / pure-SaaS / logistics rows above), lead with `D1 disqualified (no reference value):` followed by the cited D1 rule + one sentence of what the entity is. No em dashes - use a colon. The scannable code lives in `flagged_for_deletion_reason`; the 2-4 sentence prose rationale stays in `account_brief`. **Clear-on-exit:** if a record ever moves OFF `Flagged for deletion` back into an active segment, clear `flagged_for_deletion_reason` to empty in the same write. Canonical 7-code spec: `context/hubspot/property-schema.md` §2.1.

If no D1 match: proceed to the ICP routing below.

## Classification Decision Framework (file 06 §5 flowcharts)

After Step 0, route to one of six ICP flowcharts per file 06 §5:

1. **Colocation flowchart** - `Standard - colo` / `AI Signals - colo` / `Modular - colo` / `Hyperscale Wholesale - colo` / `Greenfield` (cross-segment - pairs with colo parent)
2. **Fiber Operator flowchart** - `Regional CLEC - Fiber operator` / `Long Haul / Backbone - Fiber operator` / `Dark Fiber Specialist - Fiber Operator` (capital O) / `Tier 2 National Wholesale - Fiber operator` / `Regional Cable Operator - Fiber operator` / `Municipal / Cooperative - Fiber operator`
3. **NeoCloud flowchart** - `Large Scale GPU - Neocloud` / `Tier 1 Inference - Neocloud` / `AI Infrastructure providers - Neocloud` (lowercase p) / `Sovereign AI Clouds - Neocloud` / `Crypto to AI - Neoclouds` (trailing s) / `Greenfield` (cross-segment - pairs with neocloud parent)
4. **Network Operator flowchart** - `Tier 1 Carrier - Network Op` / `Pure Wholesale Carrier - Network Op` / `Cable MSO Enterprise Division - Network Op` / `International Backbone Specialist - Network Op` / `Subsea cable operator` (NEW 2026-05-14, no `- Network Op` suffix)
5. **MSP / Aggregator flowchart** - `Telecom Aggregator - MSP` / `Managed Network Services - MSP` / `TSD Technology Services Distributor - MSP` / `Master Agent - MSP` / `Cloud + Telecom Hybrid MSP - MSP`
6. **Enterprise (Multi-DC ICP) flowchart** - `Financial Services - Enterprise` / `Healthcare Systems - Enterprise` / `Retail and Distribution - Enterprise` / `Outsourcing Services - Enterprise`

Each flowchart is anchored on the per-sub-segment rules in file 06 §6 (anchor accounts and confidence thresholds).

## Best-Fit Classification Policy (Cooper directive 2026-05-14)

`manual_review_required` is NOT the default. Classify to the best-fit sub-segment with calibrated confidence:

| Confidence | When to use | Audit trail |
|---|---|---|
| `high_90` | Strong positive evidence on 2+ anchor signals from file 06 §6 for one sub-segment. Public confirmation (website, press, regulatory filing, named anchor pattern). | Cite anchor signals in HubSpot note. |
| `medium_7089` | Positive evidence on 1 anchor signal + reasonable inference from adjacent signals. One credible source. | Cite the anchor signal + the inference. |
| `low_5069` | Thin anchor verification - single soft signal, no public confirmation, but no contradicting evidence. Includes Master Agent classify-best-fit (see below). | Cite the soft signal. R2 + D7 weekly re-validates. |
| `manual_review_required` | RESERVED. Use ONLY when 2+ sub-segments have CLEAR positive evidence AND the file 06 §5 tiebreaker fails. NOT a default for thin records. | Cite both candidate sub-segments and the failed tiebreaker. |

**Target:** `manual_review_required` < 5% of records per run. If a run exceeds 5%, the classifier is being too cautious - re-review with best-fit + `low_5069` defaults.

**Flagged for deletion:** When no positive evidence exists for ANY ICP sub-segment AND no D1 disqualifier applies, set `customer_segment = "Flagged for deletion"` (do not park in `manual_review_required`). In the SAME write, set `flagged_for_deletion_reason` leading with `No ICP fit:` + one sentence on what the entity is and why it has no ICP fit (no em dashes - use a colon). Hand off to pre-deletion-audit for cascade handling. Canonical 7-code spec: `context/hubspot/property-schema.md` §2.1.

### Master Agent classify-best-fit (Cooper 2026-05-14)

Master Agent records (X4 Solutions, CyberNet Communications, and similar TSD / agent-channel operators) are classified best-fit, NOT defaulted to `manual_review_required`:

- **X4 Solutions** - confirmed `Telecom Aggregator - MSP`, confidence `high_90` (named anchor in file 06 §6).
- **CyberNet Communications** - best-fit `Telecom Aggregator - MSP`, confidence `medium_7089` (single anchor signal, public TSD positioning).
- **Other Master Agents with thin public footprints** - best-fit to closest sub-segment, confidence `low_5069`. D7 weekly re-validates against fresh signal scans.

### Split-Book Operator Tiebreaker (file 06 §4 D2)

When a parent operator runs both a standard / retail colo book AND a hyperscale wholesale arm (Equinix parent vs xScale child, Vantage, Aligned, NTT, Iron Mountain, QTS, CyrusOne, Compass, EdgeConneX), apply file 06 §4 D2:

- **Parent record** (the corporate / brand-level HubSpot record) -> `company_sub_segment = "Standard - colo"` by majority revenue. Confidence `high_90` when revenue split is publicly disclosed; `medium_7089` when inferred from named-tenant patterns.
- **Wholesale / xScale child record** (separate HubSpot record for the wholesale arm - e.g., Equinix xScale, Vantage Hyperscale, Aligned Wholesale) -> `company_sub_segment = "Hyperscale Wholesale - colo"`. Confidence `high_90` (public positioning).
- **Do NOT** default split-book parents to `manual_review_required`. Classify both records best-fit and let the wholesale-arm record carry the hyperscale messaging.

### Catch-All Guard Rule (file 06 D5 §1 #2)

The following sub-segments are catch-all defaults inside their flowcharts and require POSITIVE-evidence questions, not just negative-exclusion:

- `Regional CLEC - Fiber operator` (Fiber flowchart catch-all)
- `Standard - colo` (Colo flowchart catch-all)
- `Telecom Aggregator - MSP` (MSP flowchart catch-all)

For each catch-all assignment, the classifier MUST answer one positive-evidence question from file 06 §6 (e.g., "Does this fiber operator have a public CLEC tariff filing or PUC certification?"). If the answer is "no" or "uncertain" - i.e., the only basis for the catch-all is the absence of more-specific signals - downgrade confidence to `low_5069`, write the catch-all classification, and route to R2 + D7 for weekly re-validation. Do NOT escalate to `manual_review_required` on negative-only evidence; that's what `low_5069` is for.

## Active Sub-Segment Internal Values (case-sensitive - verify exact strings)

These are the 30 active `company_sub_segment` enum values (verified live via HubSpot MCP 2026-05-14). Case and punctuation are load-bearing - HubSpot enum writes fail silently on mismatch. Full reference: `context/account-tiering/sub-segment-qualification.md`.

**Network Operator(Tier 1 / VNO) - 5 sub-segments:**
- `Tier 1 Carrier - Network Op` (replaces retired `Tier 1 Global Incumbent - Network Op`)
- `Pure Wholesale Carrier - Network Op`
- `Cable MSO Enterprise Division - Network Op`
- `International Backbone Specialist - Network Op`
- `Subsea cable operator` (NEW 2026-05-14, 30th sub-segment; lowercase, no `- Network Op` suffix)

**Fiber Operator - 6 sub-segments:**
- `Regional CLEC - Fiber operator` (catch-all default for ambiguous mid-size fiber)
- `Long Haul / Backbone - Fiber operator`
- `Dark Fiber Specialist - Fiber Operator` (note: capital "O" - the only Fiber sub-segment that capitalizes "Operator")
- `Tier 2 National Wholesale - Fiber operator`
- `Regional Cable Operator - Fiber operator`
- `Municipal / Cooperative - Fiber operator` (renamed from `Co-op/consortium` 2026-05-13)

**Data Center Colo Provider - 4 sub-segments:**
- `Standard - colo` (catch-all default)
- `AI Signals - colo`
- `Modular - colo`
- `Hyperscale Wholesale - colo`

**NeoCloud - 5 sub-segments:**
- `Large Scale GPU - Neocloud`
- `Tier 1 Inference - Neocloud`
- `AI Infrastructure providers - Neocloud` (note: lowercase "p" in "providers")
- `Sovereign AI Clouds - Neocloud`
- `Crypto to AI - Neoclouds` (note: trailing "s" on "Neoclouds")

**MSP/Aggregator - 5 sub-segments:**
- `Telecom Aggregator - MSP` (catch-all default)
- `Managed Network Services - MSP` (Phase 1.7c.1 - legacy `- Network Operator` suffix archived 2026-05-13)
- `TSD Technology Services Distributor - MSP`
- `Master Agent - MSP`
- `Cloud + Telecom Hybrid MSP - MSP`

**Enterprise-CustomerSegment - 4 sub-segments:**
- `Financial Services - Enterprise`
- `Healthcare Systems - Enterprise`
- `Retail and Distribution - Enterprise`
- `Outsourcing Services - Enterprise`

**Cross-segment - 1 sub-segment:**
- `Greenfield` - pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` parent `customer_segment`. Pre-operational / actively-in-build companies (Series A-C funded, sites under construction, <2 operational sites). Per Cooper 2026-05-14: REAL sub-segment, not deprecated.

**Total: 30 active values.**

**Archived 2026-05-13 (do NOT use - replace with current values if encountered on legacy records):**
- `Co-op/consortium` - re-route to `Municipal / Cooperative - Fiber operator`
- `External Extension - Network operator` - migrate to `network_op_track = external_extension` (dedicated field)
- `Internal + external unification - Network Operator` - migrate to `network_op_track = internal_external_unification` (dedicated field)
- `Managed Network Services - Network Operator` (pre-Phase 1.7c.1 suffix) - re-route to `Managed Network Services - MSP`

### Greenfield (cross-segment pairing rule)

`Greenfield` pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` as the parent `customer_segment`. Use when the operator has funded / announced sites but no operational facility live yet (no first-power, no tenant move-ins). R2 auto-migrates the record to the appropriate operational sub-segment (`Standard - colo`, `AI Signals - colo`, `Modular - colo`, `Hyperscale Wholesale - colo`, or one of the 5 NeoCloud sub-segments) when the first operational site goes live.

### Subsea cable operator (NEW 2026-05-14)

Anchors: Aqua Comms, Seaborn Networks, BW Digital, Hawaiki, Telxius. Sub-segment of `Network Operator(Tier 1 / VNO)` parent (not Fiber Operator).

**Tiebreaker vs `International Backbone Specialist - Network Op`:** subsea-primary operators with minimal terrestrial presence (cable-landing stations + minimal backhaul) -> `Subsea cable operator`. Operators with subsea cables AS PART OF a broader terrestrial backbone (Tata, Telxius arguable, NTT submarine arm) -> `International Backbone Specialist - Network Op`. Confidence `high_90` on subsea-primary; `medium_7089` on mixed.

### Crypto to AI - Neoclouds (inclusive definition, Cooper 2026-05-14)

`Crypto to AI - Neoclouds` is inclusive of ANY Bitcoin / crypto mining past with an AI pivot, regardless of operator vs landlord model. All of the following land here:

- IREN (operator pivot)
- Core Scientific (operator with CoreWeave landlord deal)
- Galaxy (operator + investor)
- Bitfarms (operator)
- TeraWulf (operator)
- APLD / Applied Digital (mixed operator + landlord)

Do NOT split landlords into `Hyperscale Wholesale - colo` for the AI-pivot site - the crypto heritage is the load-bearing signal and routes them to `Crypto to AI - Neoclouds` regardless of current GTM model. Confidence `high_90` when both crypto history AND AI pivot are publicly confirmed.

### No NaaS Platform Operator policy (Cooper 2026-05-14)

NaaS platforms (Megaport, Equinix Fabric, PacketFabric, Console Connect, Console, Epsilon Fabric, Console Connect, alkira, Prosimo) do NOT classify as an MSP/Aggregator sub-segment. They are either:

- `customer_segment = "Other"` - when useful as competitive / partner reference (Megaport, Equinix Fabric, PacketFabric - primary competitors)
- `customer_segment = "Flagged for deletion"` - when no MaiaEdge value (small / regional NaaS plays with no overlap). Set `flagged_for_deletion_reason` in the same write, leading with `No ICP fit:` + one evidence sentence (no em dashes - use a colon). 7-code spec: `context/hubspot/property-schema.md` §2.1.

There is NO `NaaS Platform Operator` sub-segment. Do not invent one.

## What MaiaEdge IS

MaiaEdge is an infrastructure provider. We give network operators the tools to build and deliver their own private connectivity services. The operator keeps the customer, the invoice, the brand, the margin. We're the infrastructure behind their service, not the service itself.

**The product:**
- **PBC (Path Border Controller):** 1RU edge device. Dual 100 Gbps. AES-256-GCM encryption. Protocol-free forwarding. Merged L2/L3.
- **Port Extender:** 1RU switch. 48 x 10/25GbE tenant ports. Built for colo meet-me rooms.
- **PCE (Path Computation Engine):** Cloud orchestrator. Computes optimal paths, automates provisioning, hop-by-hop telemetry. White-label multi-tenant portal. API-first.

**The model:** IaaS subscription. 1/3/5-year terms. 10G or 100G tiers.

**Key numbers:** Traditional provisioning: 60-90 days. MaiaEdge: under 10 minutes. Cost reduction: 80-90%.

**The team:** Founded by the team behind Acme Packet (sold to Oracle for $2.1B) and 128 Technology (acquired by Juniper). $2.55B combined exits. Just raised $20M Series A.

### What MaiaEdge is NOT

| They (NaaS: Megaport, Equinix Fabric) | Us (MaiaEdge) |
|----------------------------------------|----------------|
| Own circuits, deliver services to enterprises | Provide infrastructure. Operators deliver services. |
| You join THEIR fabric | You build YOUR OWN fabric |
| Their portal, their invoice, their brand | Your portal, your invoice, your brand |
| They own the customer | You own the customer |

Not SD-WAN. Not a router replacement. We integrate with Equinix Fabric and Megaport via API. In cold outreach, say "third-party fabric providers" not specific names.

### Sovereignty: The Thread in Every Message

Every email should reinforce that the operator keeps the customer, the margin, and control. If you mention speed, pair it with ownership: "your team provisions in minutes" not just "provision in minutes." Exception: Neoclouds -- OPERATOR sovereignty banned. DATA sovereignty ("sovereign by design", "paths you control") allowed. Lead with deterministic performance, private connectivity, instant on-ramp.

### The Relevance Principle

Relevance beats personalization. Research is fuel, not content. It tells you WHICH problem to lead with. The email itself should not display the research. The prospect should think "yep, that's my life," not "this person Googled me." No "I noticed," no "Congratulations on," no company facts as standalone sentences. See cold-email skill for full anti-personalization rules.

## Qualified Segments

Classification requires PROOF, not just keywords. Each segment has a Quick Classification Test. If the answer is uncertain, flag for manual review rather than auto-classifying.

| Segment | Description | Quick Classification Test |
|---------|-------------|--------------------------|
| Fiber Operator | Regional/national fiber operators. Own physical fiber infrastructure. $20M-$500M revenue sweet spot. ~1,700-1,900 US operators. | "Does this company own fiber in the ground and sell connectivity services to businesses or carriers?" |
| Colocation Operator | Data center / colocation providers. Multi-site operators preferred. ~700-750 main US facilities. | "Does this company own a building where other companies put their servers, with carrier interconnection available?" |
| AI Colocation Operator | Colos with confirmed GPU cloud tenants or heavy AI infrastructure investment. Liquid cooling, 30kW+ racks, neocloud partnerships. | Same as Colo + "Does this facility have confirmed GPU cloud tenants, liquid cooling, or 30kW+ density?" |
| Neocloud | GPU cloud providers themselves (Lambda Labs, Crusoe, Voltage Park, Together AI). They ARE the inference customer. | "Does this company own (or have committed funding to build) GPU hardware in physical facilities and sell compute capacity to other companies?" |
| Network Operator | Tier 1/2 carriers with 50+ PoPs, complex multi-domain networks. Sophisticated internal automation (usually). | "Is this a national/global carrier with 50+ PoPs that sells enterprise connectivity?" |
| MSP / Aggregator | Managed service providers and VNOs that aggregate connectivity across multiple upstream carriers. NOT IT MSPs. | "Does this company buy circuits from multiple telecom carriers and resell bundled connectivity to enterprises?" |
| Enterprise (Multi-DC ICP) | $1B+ enterprises that own and operate multi-DC corporate networks with in-house network engineering teams. Four sub-segments only: Financial Services, Healthcare Systems, Retail and Distribution, Outsourcing Services. Priority 5 (lowest ICP). Anchor: Meijer. | "Is this a $1B+ enterprise in financial services, healthcare, retail/distribution, or operational BPO, with 3+ data centers and an in-house network engineering team, that holds direct carrier contracts?" |

## Exclusion List

EXCLUDE if any of the following apply:

| Exclude Category | Why |
|------------------|-----|
| Internet Exchange Point (IXP) | Infrastructure marketplace, not an operator |
| Tower REIT | Real estate, not network operations |
| IT MSP (managed IT services, helpdesk, break-fix) | Wrong type of MSP. Apply the IT MSP Test: if website lists helpdesk, endpoint management, cybersecurity, backup/DR with no carrier circuit aggregation, it's an IT MSP. |
| Retail ISP (verified no wholesale business) | Consumer broadband, not our buyer |
| Software vendor (including AI software platforms) | Not an operator. "AI cloud" marketing without physical GPU infrastructure = software vendor. |
| Hyperscaler (AWS, Azure, GCP, Meta) | Not our customer |
| Enterprise - Disqualified (not the four ICP sub-segments) | Multi-DC enterprises in Manufacturing, Energy/Utilities, Logistics/Supply Chain → Watch List (not ICP). Government/Defense → FedRAMP-gated. Sub-$1B mid-market → hold as `Other`. Single-DC, single-geo, network outsourced to single MSP, or no direct carrier contracts → fails Enterprise gates. Note: $1B+ enterprises in Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services with in-house net eng are ICP - see Qualified Segments table above. |
| Under 10 employees (verified from 2+ sources) | Too small (unless holding company with operator subsidiaries) |
| Vendor / Contractor / Manufacturer | Equipment maker, not operator. Includes fiber construction contractors. |
| Consulting firm | Advisory, not operator |
| Trade organization | Industry body, not operator |
| Defunct / Acquired (absorbed into parent) | No longer exists as independent entity |
| IT hosting / managed hosting (no physical colo) | Uses "colocation" or "data center" language but doesn't own/operate multi-tenant facilities with interconnection |
| Cloud GPU reseller (no owned infrastructure) | Resells hyperscaler GPU instances, not a neocloud |

### Exclude Verdict Routing

An `EXCLUDE` verdict from this skill does **not** directly write `customer_segment = "Flagged for deletion"` to HubSpot. The verdict is passed to the **pre-deletion-audit** skill (see `skills/pre-deletion-audit/SKILL.md`), which gates the decision through:

1. Open-deal hard stop (companies with any non-closed deal are never flagged)
2. Duplicate detection against existing ICP records (if the excluded company is a duplicate of a real ICP primary, its contacts are reassociated to the primary before the duplicate is flagged)
3. Per-contact activity check - any contact with `notes_last_contacted` within the last 90 days, a `notes_last_updated` within the last 90 days, or an association to an open deal is preserved and never receives `flagged_for_deletion = true`

This routing applies whether segment-classification is invoked standalone, from the enrichment pipeline, or under CRM Guardian Job 7. The classification verdict is the input to the audit; the audit is the only path that writes `customer_segment = "Flagged for deletion"`.

## Common False Positive Patterns

These company types frequently match segment keywords but should NOT be classified:

| Company Type | Keyword Match | Correct Action |
|---|---|---|
| IT hosting provider | "colocation," "data center" | Exclude: no multi-tenant facility with interconnection |
| Residential-only ISP | "fiber," "network operator" | Exclude unless wholesale/enterprise division verified |
| Cable MSO (residential) | "fiber network" | Exclude unless wholesale/transport division verified |
| Municipal broadband | "fiber operator" | Exclude unless commercial services arm verified |
| SD-WAN vendor | "network operator" | Exclude: software, not carrier infrastructure |
| VoIP/UCaaS provider | "carrier," "network services" | Exclude: application provider, not transport |
| IT MSP | "managed services," "MSP" | Exclude: IT services, not telecom aggregation |
| AI software platform | "AI cloud," "GPU cloud" | Exclude: software, not GPU infrastructure owner |
| AI consulting firm | "AI infrastructure" | Exclude: services, not compute provider |
| Fiber construction contractor | "fiber," "network infrastructure" | Exclude: builds for others, doesn't operate |

## Segment Messaging

**For full messaging framework, see context/copy-strategy/segment-messaging.md**

### Fiber Operators

**The situation:** Own fiber. Good regional business. Margins tightening. Significant fiber underutilized (lit, dark, and stranded laterals). Standing up private paths still requires routing complexity the ops team doesn't want to run. Cloud on-ramp is either not offered or offered with thin margin.

**The angle:** Monetize underutilized fiber. Stand up an instant private fabric across your network over any transport (fiber, wave, DIA, 5G/fixed wireless, satellite) with no routing complexity. Sell new services you couldn't before  -  cloud on-ramp flagship.

**Pillars:** MONETIZE | AUTOMATE | EXTEND REACH

**What to lead with:**
- **CEO/President:** Monetize underutilized fiber. New services (cloud on-ramp) you couldn't offer before. Competitive positioning.
- **CFO:** 80-90% provisioning cost reduction. OpEx model. New revenue from existing assets.
- **CTO/VP Engineering:** No VLAN stitching, no BGP, no MPLS, no SRv6. Any transport, any site. API-driven.
- **VP Sales/Commercial:** Win deals they're currently losing on provisioning timelines. Cloud on-ramp as a product to sell.
- **COO:** Scale delivery without scaling headcount.

**Pain points:** "Every NNI is a 60-90 day project" / "Once traffic leaves our network, visibility dies" / "We've got fiber sitting idle while the board wants revenue growth" / "Cloud on-ramp would be a product if we could stand it up without a hyperscale facility build" / "Our ops team isn't a routing team  -  we don't want to run MPLS/BGP just to stand up private paths"

### Colocation Operators

**Pillars:** INSTANT | MONETIZE | REACH

**The situation:** Every cross-connect is still a manual project (LOAs, truck rolls, VLAN coordination). Tenants expect portal-driven self-service the operator hasn't built. Standing up a services layer in-house is years of development. Cloud on-ramp is either not offered or offered through an arrangement that requires a hyperscale facility build. Multi-site operators have no easy way to stitch sites together for a tenant who wants capacity in more than one.

**The angle:** Build your own fabric without a multi-year development project. Automated virtual cross-connects, a services layer you can productize, and cloud on-ramp as a native product under your brand.

**What to lead with:**
- **CEO:** Build your own fabric. New high-margin services layer without a multi-year development project.
- **CTO:** Build your own interconnection layer in weeks, not years. Automated virtual cross-connects, virtual meet-me room across sites, deterministic paths to cloud and partner DCs. (Note: "fabric-in-a-box" is cheatsheet / live-conversation language only - banned in cold body per email-writing-rules.md.)
- **VP Sales:** Turn "we need 6 weeks" into "it's live today." Cloud on-ramp becomes a native product to sell.
- **CFO:** Higher attach rates without infrastructure buildout. New revenue from services, not more cabinets.

**Pain points:** "Every cross-connect is a project. LOAs, truck rolls, VLAN config" / "Tenants expect portal-driven self-service we haven't built" / "Building our own connectivity services is a multi-year project" / "Cloud on-ramp would be a product if we could stand it up without a hyperscale facility build" / "We have multiple sites and no easy way to connect them for a tenant who wants more than one"

> **Sparingly:** "Losing tenants to third-party fabric providers" is still allowed as a supporting hook, but only when research confirms a third-party fabric referral is already happening and no stronger angle is available. Don't lead with it.

### AI Colocation Operators

Same as Colocation but with AI-specific messaging when strong AI signals are found.

**Pillars:** DETERMINISTIC | INSTANT | MONETIZE

**The situation:** Invested heavily in AI-ready infrastructure: liquid cooling, high-density racks, power density. GPU cloud tenants bring interconnection demand and latency expectations best-effort networking doesn't meet. The connectivity layer hasn't caught up to the compute investment. Distributed and modular operators have multiple sites that need to behave like one fabric.

**Messaging lead:** Deterministic paths between distributed AI sites + automated cross-connects for GPU tenant deployments + cloud on-ramps for GPU workloads. NOT generic colo messaging. AI colo has its own messaging identity.

**Core hook:** "GPU tenants deploy dense interconnection fast. The connectivity layer either keeps up or it becomes the gap in the facility."

**Additional angles:**
- "You've built the compute and cooling infrastructure. Now complete the AI story with a connectivity layer that matches."
- "Best-effort networking is the uncontrolled variable in inference performance. Your tenants feel it."

**Do NOT use:** "35+ cross-connects per deployment," "sub-10ms latency," "33% of AI/ML latency is attributable to network slowness." These specific quant claims are retired  -  broader framing lands better because the numbers vary by tenant and workload.

**Modular DC variant** (Nodiac, Colony Compute, containerized-capacity-at-power-sites operators): Use AI Colo messaging with the multi-site angle front-and-center. "Every new pod at a new power site is either a separate networking project or a day-one join to your fabric. MaiaEdge makes it the second one." See [context/segments/colocation.md](context/segments/colocation.md) "Modular DC Variant" section for full treatment.

**Greenfield colo disambiguation:** Read their plans before writing. AI-ready build (liquid cooling / high-density power / announced GPU tenants / "AI campus" language) → AI Colo messaging. Standard build (traditional colo, no AI-ready signals) → Standard Colo messaging. Shared angle across both: multi-site fabric from the day the second site comes online.

### Neoclouds

These are NOT colos. Neoclouds (Lambda Labs, Crusoe, Voltage Park, Together AI) are GPU cloud providers that operate compute across multiple facilities. They ARE the inference customer.

**Pillars:** DETERMINISTIC | PRIVATE | INSTANT

**Critical messaging shift:** Drop "keep your customer" language. OPERATOR sovereignty banned. DATA sovereignty ("sovereign by design", "paths you control") allowed. No network jargon (VLAN, Q-in-Q). Lead with deterministic performance, private cloud connectivity (egress savings for their customers), and instant customer on-ramp.

**Master pitch:** Connecting distributed AI infrastructure simply. Benefits: multi-tenancy, deterministic performance, private cloud connectivity (egress savings for their customers), instant customer on-ramp. Observability is a supporting benefit under DETERMINISTIC, NOT the universal lead.

**Angle selection by maturity** (research-driven; same pillars, different door):

| Stage | Profile | Angle | Opening hook |
|-------|---------|-------|--------------|
| Pre-revenue / single site | Modular pre-tenant | **Watch list.** Too early. | N/A - flag on 2nd site or 1st GPU tenant. |
| Early growth (2-5 sites, crypto-to-AI pivots) | Duos Edge AI, IREN, TeraWulf, Core Scientific | **Early-growth.** Tenant-readiness framing. | "Bitcoin doesn't care about latency. Enterprise AI tenants do." |
| Mid-growth (5-15 sites, mixed customers, network person lost or never had one) | Together.ai, RunPod, Modal, Baseten, DeepInfra | **In-pain-now** (observability under DETERMINISTIC). | "Inference latency varies by facility and your team is guessing whether it's the carrier, the colo, or something in between." |
| Scale (15+ sites, hyperscaler-heavy 80%+, enterprise ramp plan) | Lambda, Crusoe, Voltage Park, Nebius | **Scaling-wall** (lead with INSTANT). | "The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will." |

**Flagship DETERMINISTIC proof point (all angles):** Agentic compounding latency. Ten inference hops across best-effort routing compounds into tens of seconds of delay. "Training tolerates retries. Inference doesn't. Agentic workflows tolerate neither." (Source: Montauk Capital April 2026 "Last Millisecond" thesis.)

**Neocloud Sub-Segments** (assign `customer_sub_segment` in enrichment research summary, import-processor maps to HubSpot `company_sub_segment`):

| HubSpot `company_sub_segment` | Examples | Default Angle | Entry Point |
|-------------|----------|---------------|-------------|
| `Large Scale GPU - Neocloud` | Lambda, Crusoe, Voltage Park, Nebius | Scaling-wall (default). In-pain-now only if latency variance is their stated pain. | Enterprise onboarding velocity. |
| `Tier 1 Inference - Neocloud` | Together.ai, Fireworks, Baseten | In-pain-now (agentic angle lands hard). | Real-time telemetry + agentic compounding latency. |
| `AI Infrastructure providers - Neocloud` | Vultr, DigitalOcean, Fluidstack, Modal, RunPod | In-pain-now. | Multi-cloud bridge + egress competitive advantage. |
| `Sovereign AI Clouds - Neocloud` | Nscale, Firmus, E2E Networks, Yotta | In-pain-now with sovereignty framing. | Policy-based sovereign routing (always qualify "sovereign"). |
| `Crypto to AI - Neoclouds` | IREN, Core Scientific, TeraWulf | Early-growth. Inclusive of operator AND landlord per Cooper 2026-05-14 - Bitcoin mining past + AI pivot is the defining trait regardless of current GTM model. | Tenant-readiness + basic connectivity. |

**Pain points:** "Best-effort paths introduce jitter that breaks AI workloads" / "No visibility across the middle mile between clusters" / "Public internet egress costing $0.05-0.09/GB vs $0.02/GB Direct Connect" / "Every new facility is a multi-week connectivity project" / "Enterprise customers don't bring their own connectivity - every onboarding is a manual project"

### HubSpot Segment Mapping

NeoCloud is its own segment value in HubSpot  -  it is NOT mapped under "Colocation Operator."

| Classification | HubSpot `customer_segment` | HubSpot `company_sub_segment` |
|---------------|---------------------------|-------------------------------|
| Large-scale GPU compute neocloud (bare-metal training) | `NeoCloud` | `Large Scale GPU - Neocloud` |
| Distributed inference neocloud (edge cities, sub-100ms SLA) | `NeoCloud` | `Tier 1 Inference - Neocloud` |
| Mid-market cloud adding GPU compute | `NeoCloud` | `AI Infrastructure providers - Neocloud` |
| Sovereign AI cloud (GDPR/DPDP/national program) | `NeoCloud` | `Sovereign AI Clouds - Neocloud` |
| Crypto-to-AI pivot (operator OR landlord with Bitcoin mining past) | `NeoCloud` | `Crypto to AI - Neoclouds` |
| Colo with AI infrastructure signals | `Data Center Colo Provider` | `AI Signals - colo` |
| Standard colo (catch-all default - interconnection / per-rack retail) | `Data Center Colo Provider` | `Standard - colo` |
| Modular / prefab / edge-pod colo operator | `Data Center Colo Provider` | `Modular - colo` |
| Hyperscale wholesale colo (xScale-pattern child record) | `Data Center Colo Provider` | `Hyperscale Wholesale - colo` |
| Greenfield (announced / funded, not operational yet) - colo parent | `Data Center Colo Provider` | `Greenfield` |
| Greenfield (announced / funded, not operational yet) - neocloud parent | `NeoCloud` | `Greenfield` |
| Regional CLEC / fiber operator catch-all default | `Fiber Operator` | `Regional CLEC - Fiber operator` |
| Long-haul / backbone fiber operator | `Fiber Operator` | `Long Haul / Backbone - Fiber operator` |
| Dark fiber specialist (80%+ IRU revenue) | `Fiber Operator` | `Dark Fiber Specialist - Fiber Operator` |
| Tier 2 national wholesale fiber (Zayo / Lightpath / Uniti+Windstream archetype) | `Fiber Operator` | `Tier 2 National Wholesale - Fiber operator` |
| Regional cable operator with growing fiber arm | `Fiber Operator` | `Regional Cable Operator - Fiber operator` |
| Municipal / Cooperative fiber (muni / co-op / consortium) | `Fiber Operator` | `Municipal / Cooperative - Fiber operator` |
| Tier 1 incumbent carrier (AT&T / Verizon / NTT / Orange archetype) | `Network Operator(Tier 1 / VNO)` | `Tier 1 Carrier - Network Op` |
| Pure-wholesale carrier (Cogent / Arelion / EXA Infrastructure archetype) | `Network Operator(Tier 1 / VNO)` | `Pure Wholesale Carrier - Network Op` |
| Cable MSO enterprise division (Comcast Business / Spectrum Enterprise) | `Network Operator(Tier 1 / VNO)` | `Cable MSO Enterprise Division - Network Op` |
| International backbone specialist (Tata / PCCW Global / Telstra International) | `Network Operator(Tier 1 / VNO)` | `International Backbone Specialist - Network Op` |
| Subsea cable operator (subsea-primary, minimal terrestrial - Aqua Comms / Seaborn / BW Digital) | `Network Operator(Tier 1 / VNO)` | `Subsea cable operator` |
| Telecom aggregator (Granite / Nitel archetype - catch-all default) | `MSP/Aggregator` | `Telecom Aggregator - MSP` |
| Managed network services provider | `MSP/Aggregator` | `Managed Network Services - MSP` |
| TSD (100+ sub-agents, $1B+ gross billings - Telarus / AVANT / Intelisys / AppDirect) | `MSP/Aggregator` | `TSD Technology Services Distributor - MSP` |
| Master Agent (smaller / regional / vertical-focused agency with sub-agent network) | `MSP/Aggregator` | `Master Agent - MSP` |
| Cloud + Telecom hybrid MSP (AWS Premier + 30%+ cloud revenue + network managed services) | `MSP/Aggregator` | `Cloud + Telecom Hybrid MSP - MSP` |
| Enterprise (Multi-DC ICP) - financial services | `Enterprise-CustomerSegment` | `Financial Services - Enterprise` |
| Enterprise (Multi-DC ICP) - healthcare systems | `Enterprise-CustomerSegment` | `Healthcare Systems - Enterprise` |
| Enterprise (Multi-DC ICP) - retail and distribution | `Enterprise-CustomerSegment` | `Retail and Distribution - Enterprise` |
| Enterprise (Multi-DC ICP) - outsourcing services / BPO | `Enterprise-CustomerSegment` | `Outsourcing Services - Enterprise` |

### Network Operators (Tier 1/2 Carriers)

**Pillars:** AUTOMATE | EXTEND REACH | MONETIZE (same as fiber)

**The situation:** Sophisticated internal automation. Not slow. But all of that stops at their network boundary. Cross-carrier paths beyond their footprint still take 60-90 days.

**Messaging lead:** Extend your reach, monetize existing assets. Same lead as fiber operators.

**CRITICAL: Never claim they're slow at what they're fast at.** Research what they've built. Acknowledge it. Then position MaiaEdge as extending their automation beyond their borders.

**Two tracks:**
- **Track A (Has internal automation):** "You've automated internally. MaiaEdge extends that everywhere else." Use when research shows self-service portal, API docs, branded products.
- **Track B (Fragmented internally):** "MaiaEdge unifies your internal boundaries first, then extends to partners." Use when research shows no evidence of portal/API automation.

**Pain points (Track A):** "Automated internally, but beyond our footprint still takes 60-90 days" / "No visibility once traffic leaves our network" / "Enterprise customers expect AWS-like speed" / "Lumen + AWS announced direct enterprise connectivity"

### MSPs / Aggregators

**The situation:** Own the customer relationship but rely on 3+ upstream carriers for transport. Can't see inside carrier networks. Responsible for SLAs they can't verify. Provisioning depends on whichever carrier is slowest. Tier 1s going direct to their customers.

**The angle:** MaiaEdge gives them end-to-end visibility across all upstream providers and instant provisioning. They compete on capability, not just relationship.

**What to lead with:**
- **CEO/President:** Tier 1 capabilities on an asset-light model. Compete on speed, not just price.
- **CFO:** Shift from CapEx to predictable OpEx.
- **VP Engineering:** Unified visibility across all carrier partners. No more blind spots.
- **VP Sales:** Instant activation instead of "depends on the carrier."

**Pain points:** "Blind to what happens inside carrier networks" / "Responsible for SLA but can't see the path" / "'Depends on the carrier' kills deals" / "Tier 1s are going direct to our customers"

### Enterprise (Multi-DC ICP)

**HubSpot:** `customer_segment = "Enterprise-CustomerSegment"`. Promoted to ICP 2026-05-11. Priority 5 (lowest ICP). Tier 2 ceiling - no Tier 1 path unless an exceptional trigger emerges.

**The four sub-segments (and only these four):** `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Anchor: Meijer (retail/distribution).

**Hard gate (BOTH must pass):**
- **Vertical gate:** one of the four sub-segments above.
- **Scale gate:** $1B+ revenue AND (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house network engineering team via NOC presence or VP/Director/Principal Network Engineering job postings).

**Hard disqualifiers (any one disqualifies):** network fully outsourced to single MSP with no internal engineering ownership; single DC or single geography; no direct carrier contracts (100% reseller/MSP).

**Sub-segment assignment rules:**
- `Financial Services - Enterprise` - banks, investment firms, insurers, payment networks, capital-markets infrastructure. Defense contractors that procure commercially (Lockheed, RTX, Northrop, BAE, L3Harris) land here on commercial profile, not gov work.
- `Healthcare Systems - Enterprise` - multi-hospital IDNs and large health systems. Single-hospital regional systems below the scale gate fail.
- `Retail and Distribution - Enterprise` - national retailers with multi-DC corporate IT + distribution-center networks. Multi-warehouse alone does NOT qualify; the qualifier is multi-DC corporate IT.
- `Outsourcing Services - Enterprise` - BPO / outsourced operations providers running multi-site delivery centers on an ongoing operational basis. Project-based consulting (Deloitte, McKinsey, BCG, Bain) is EXCLUDED. Dual-arm firms (Cognizant) classify on operational delivery revenue mix.

**Out of scope (Watch List - do NOT assign Enterprise sub-segments):** Manufacturing (plant networks are OT, not IT), Energy/Utilities (NERC CIP long-tail), Logistics/Supply Chain (multi-warehouse ≠ multi-DC). Government/Defense (FedRAMP-gated). SaaS-only with no owned DCs.

**Pillars:** REDUNDANT | SOVEREIGN | AUTOMATED

**The situation:** Mature on branch SD-WAN, less mature on inter-DC determinism. Dark fiber between DCs is rarely truly redundant. Cloud on-ramps usually outsourced to Megaport/Equinix Fabric - the portal is theirs, the SLA stays with the enterprise team. Type 2 fiber is a black hole. Network team scope is growing faster than headcount.

**The angle:** Productized fabric across all DCs. Dark fiber redundancy that is actually redundant (PBCs at each end, diverse fibers, automated failover, no routing protocols). Cloud on-ramps under enterprise control. Hop-by-hop visibility everywhere. Audit-ready policy enforcement for HIPAA / PCI-DSS / SOX / GDPR.

**Critical sovereignty distinction:** Enterprises ARE the customer - not selling connectivity to anyone. Sovereignty framing pairs with **data sovereignty + regulatory audit language**, NOT operator sovereignty. **BANNED phrases for Enterprise**: "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "tenant," "meet-me room," "interconnection revenue," "aggregator," "TSD." Federation is internal language - never customer-facing for Enterprise.

**Lead angles by sub-segment:**
- **Retail and Distribution:** "Your dark fiber between corporate DCs is one cut from an outage. Fix it without routing-protocol complexity."
- **Financial Services:** "Your inter-DC paths are best-effort. Compliance is asking you to prove the path. With MaiaEdge, the path itself is the audit artifact." Frame audit-readiness for SOX/PCI-DSS/GDPR.
- **Healthcare Systems:** "Your EHR DC redundancy depends on a single fiber pair. PHI rides that path." Frame HIPAA-aligned redundancy.
- **Outsourcing Services:** "Your clients' regulators are asking where their data went. With MaiaEdge, the path is the audit artifact across every delivery center."

**What to lead with (by persona):**
- **VP Network Infrastructure / Director Network Engineering** (primary technical champion): Productized fabric, no BGP across the WAN, deterministic dark fiber redundancy without routing protocols.
- **CIO** (economic buyer at most enterprises): Unified private connectivity, no added routing complexity, AI infrastructure access, cloud on-ramps under their brand.
- **CSO / CISO**: Line-rate AES-256-GCM encryption by default, hop-by-hop path visibility, audit-ready policy enforcement, data sovereignty.
- **Network Architect / Principal Network Engineer** (technical influencer): "HAsync and HAfabric on the SSRs share a single dark fiber pair. That is not redundancy." "Type 2 is a black hole."

**Pain points:** "Our DR strategy assumes the dark fiber is redundant. It is not." / "Every new DC is a six-month networking project." / "We do not have the headcount to run BGP across the WAN." / "Megaport works until it does not. We need our own answer." / "Compliance asked us to prove where the data went. We could not." / "Type 2 is a black hole. We cannot troubleshoot what we cannot see." / "Cloud on-ramp is owned by Megaport. Our team owns the SLA."

**Cold outreach rules (Enterprise):** No em dashes. No credibility anchors (Acme Packet / 128 Technology / Andy Ory) in cold emails or LinkedIn - reserve for discovery calls and follow-ups. Lead with the problem in their language; don't lead with technical detail (SSR / HAsync / 100GigE specifics - that's for the design call). HIPAA / PCI-DSS / SOX / GDPR / HITRUST mentions are fine in Enterprise emails where the persona implies regulatory exposure.

## Post-Research Segment Verification (MANDATORY)

After completing web research, verify the segment classification against proof-based criteria. This prevents writing colo messaging for a company that's actually an IT hosting provider, or sending neocloud outreach to an AI software platform.

**Step 0  -  D1 Global Disqualifier Check (file 06 §3):**
Before anything else, run the D1 check from the "Step 0" section above. If the company matches a D1 pattern, resolve to `Other` or `Flagged for deletion` per the D1 table, skip the rest of verification, and respect the customer / closed-deal halt rule.

**Step 1  -  Quick Classification Test:**
Run the Quick Classification Test from the segment table above. If the answer to the test question is "no" or "uncertain," the company may be misclassified.

**Step 2  -  Check for False Positive Patterns:**
Does the company match any pattern in the Common False Positive Patterns table? If yes, research further before proceeding with outreach.

**Step 3  -  Verify HubSpot Classification:**
- Does the HubSpot `customer_segment` match what research found?
- For colos: Did you find strong AI signals? If yes, sub-segment should be "AI Infrastructure" not "Standard." BUT also verify they actually own/operate the facility (not managed hosting).
- For network operators: Did you find portal/API evidence? Determines Track A vs Track B. BUT also verify carrier-scale infrastructure (50+ PoPs, enterprise connectivity).
- For neoclouds: Did you confirm they OWN physical GPU infrastructure? "AI cloud" marketing alone is not sufficient.
- For MSPs: Did you confirm telecom carrier aggregation? Apply the IT MSP Test if unclear.
- For Enterprise: Did you confirm BOTH the vertical gate (one of four sub-segments) AND the scale gate ($1B+ revenue + 3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house network engineering)? Did you check for hard disqualifiers (network outsourced to single MSP, single DC, no direct carrier contracts)? Verify sub-segment assignment is one of the four ICP values, not a Watch List vertical.
- Is this company actually on the exclusion list? (Check for acquisitions, defunct status, wrong category, hosting-not-colo, software-not-neocloud)

**If mismatch:** Flag clearly: `SEGMENT MISMATCH: HubSpot says [X], research says [Y]. Using [Y] for messaging.`
**If false positive detected:** Flag: `QUALIFICATION CONCERN: Company classified as [segment] but [specific concern]. Verify before sending outreach.`
**If confirmed:** Note: `Segment verified: [segment] / [sub-segment]`

Always use the CORRECT segment for email writing, regardless of what HubSpot says. If qualification is uncertain, skip the company rather than send misaligned outreach.

## Segment Change Cascade Rules

When `customer_segment` is changed on a company record  -  whether from new classification, re-enrichment, correction, or deprecated enum migration  -  the following cascade MUST be applied:

1. **Re-derive `company_sub_segment`:** Apply sub-segment assignment rules from hubspot-values.md for the new segment. If the old sub-segment doesn't belong to the new segment, it MUST change. For example, if segment changes from `MSP/Aggregator` to `Fiber Operator`, sub-segment must change from `Telecom Aggregator - MSP` to one of the Fiber sub-segments.

2. **Re-derive `account_tier`:** Apply tier criteria from property-schema.md. A segment change may upgrade or downgrade tier:
   - Moving from MSP to Fiber Operator with HIGH confidence → upgrade to Tier 2
   - Moving from NeoCloud to Data Center Colo Provider → may downgrade from Tier 1 if no AI signals
   - Any segment change resets tier evaluation from scratch

3. **Re-derive `segmentation_confidence`:** If the segment changed, confidence should reflect the evidence for the NEW segment, not the old one. If the change was a correction without new research, set to MEDIUM unless strong evidence exists.

4. **Re-derive `infrastructure_profile`:** Only if new research was performed during the segment change. If this is a field correction or enum migration without new research, leave `infrastructure_profile` as-is.

5. **Sync to contacts:** Update `customer_segment` on all associated contacts to match the new company segment. Company record is source of truth.

6. **Update `last_enriched_date`:** Set to today's date (YYYY-MM-DD).

7. **Clear `flagged_for_deletion_reason` on exit:** If the OLD segment was `"Flagged for deletion"` and the NEW segment is an active ICP segment (or `Other` / `Partner Target`), clear `flagged_for_deletion_reason` to empty in the same write. The reason code must never linger on a record that is no longer flagged.

### Special Case: Segment Changing TO "Flagged for deletion"

When the new segment is `"Flagged for deletion"`, the cascade above does NOT apply. Instead, hand the candidate to the **pre-deletion-audit** skill (Step 0 input) and let it run its own workflow. The audit decides per-contact whether to reassociate, preserve, or flag  -  it does not blindly sync `customer_segment = "Flagged for deletion"` to associated contacts.

Specifically: skip steps 1-5 of the cascade for this case, and do NOT write the company's new segment until pre-deletion-audit has resolved all associated contacts. The audit writes the company segment itself once contacts are resolved.

**This section is the single source of truth for cascade behavior.** CRM Guardian references this section  -  it does not redefine cascade logic.

**When running under CRM Guardian:** This cascade executes automatically. The Guardian's safety tier system applies  -  see crm-guardian skill for tier definitions and deal protection rules.

**In standalone mode:** Produce the cascade recommendation without writing:
```
SEGMENT CHANGE CASCADE  -  [Company]
Segment: [old] → [new]
Sub-segment: [old] → [recommended new]
Tier: [old] → [recommended new]
Confidence: [old] → [recommended new]
Contacts to sync: [N]
```

---

## Emerging Context (2026)

**AI Infrastructure:** Training is concentrated. Inference is distributed. Tenants need low-latency paths between GPU clusters across multiple facilities. MaiaEdge enables the orchestration layer.

**Hyperscalers Going Direct:** AWS + Lumen delivering "last mile" connectivity directly to enterprises. Regional operators risk being cut out. Cross-carrier connectivity lets operators compete.

**Mplify Alliance:** MaiaEdge is engaged with Mplify Alliance (formerly MEF) on standards. Use selectively with sophisticated buyers.

## Technical Terminology

**Use in Emails:** Automated provisioning, zero-touch provisioning, protocol-free forwarding, API-driven activation, deterministic paths, hop-by-hop telemetry, end-to-end visibility, sovereignty, middle-mile blind spot, transport agnostic, white-label portal.

**Use Sparingly:** Session-smart routing (founder credibility only), PBC (after explaining: "1RU edge device"), PCE (after explaining: "cloud orchestrator").

**Never in Cold Outreach:** Session-smart routing as a lead. Internal codenames. "Revolutionary." "Game-changing." **"Fabric-in-a-box"** (Sidecar Rule 1, 2026-05-11 - cheatsheet / live-conversation only; use "interconnection layer," "service fabric," or "build your own fabric" in cold). **"Federated Private Networking"** as a noun phrase (Sidecar Decision 7 - partner-facing materials only: 101, cheatsheets, deck, datasheets, marketing site). "Federation" as a verb ("federate with partners," "federation creates network effects") is banned in cold-email and LinkedIn body; translate to "extend your reach," "sell into new markets," "connect to partners instantly."
