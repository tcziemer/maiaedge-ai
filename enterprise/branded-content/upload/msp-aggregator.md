# MSP Aggregator CheatSheet

> Converted from: MSP_Aggregator_CheatSheet.pdf

> **Classification authority:** Sub-segment classification rules, anchors, and confidence thresholds live in `context/account-tiering/sub-segment-qualification.md` (pointer) and file 06 (`context/account-tiering/sub-segment-qualification-full.md`). Tier computation lives in `context/account-tiering/tier-compute-spec.md`. This cheatsheet covers selling angles, personas, pain points, and discovery.
>
> **Tier defaults:** See `context/account-tiering/tier-compute-spec.md` for tier computation. `Telecom Aggregator`, `Managed Network Services`, `Cloud + Telecom Hybrid` default to Tier 2 (ceiling 1, floor 4). `TSD Technology Services Distributor`, `Master Agent` default to Tier 3 (ceiling 1, floor 5).

MSP / Aggregator
Know Your Customer
Attribute Details
What They Own Contracts, not infrastructure. Aggregate capacity from multiple carriers to serve
enterprise customers. Asset-light model.
Revenue Model Margin on resold connectivity, managed services fees, SLA guarantees. Value comes
from aggregation, simplification, single invoice.
Scale 50-500 employees, $20M-$500M revenue, national/regional coverage through carrier
relationships
Competitive Blind to what happens inside carrier networks. Responsible for SLA but can't see or
Reality prove path performance. Tier 1s going direct to their customers.
Problems We Solve
Problem How MaiaEdge Solves It
Blind to what happens inside carrier networks End-to-end visibility across all carrier relationships
Responsible for SLA but can't see the path Hop-by-hop telemetry, prove SLAs to customers
CapEx burden doesn't match asset-light model OpEx subscription, no infrastructure buildout required
Tier 1s going direct to your customers Match Tier 1 speed and capabilities, keep relationships
"Depends on the carrier" kills deals Instant activation, same-day provisioning
Reach limited to markets where your carriers operate Reach beyond your carriers. Connect to partners and providers in new markets instantly.
No way to monetize spare capacity Turn spare capacity into sellable services. Deterministic paths, cloud on-ramps, connectivity marketplace.
Top Pain Points (Their Words)
"We're responsible for the SLA but we can't see what's happening inside carrier networks"
"When there's an issue, we're stuck between our customer and the carrier pointing fingers"
"Tier 1s are going direct to our customers with faster provisioning than we can offer"
Discovery Questions
Question Good Answer (Buying Signal) Red Flag
"What visibility do you have into carrier "None - we're blind once traffic "Full end-to-end
networks?" enters their network" visibility"
"How do you prove SLA compliance to "We rely on carrier reports - can't "We have our own
customers?" independently verify" monitoring"
"What's your provisioning timeline vs. "Slower - we depend on carrier "Same or faster than
direct carrier relationships?" timelines" direct"
"How do you handle multi-carrier "Painful - multiple tickets, finger- "Unified visibility and
troubleshooting?" pointing" control"
"Are Tier 1s competing for your customers "Yes, and they're faster than we "We win on service,
directly?" are" not speed"

 |  |  |  |  | 

 | Attribute |  |  | Details | 

 |  |  |  |  | 

What They Own |  |  | Contracts, not infrastructure. Aggregate capacity from multiple carriers to serve
enterprise customers. Asset-light model. |  | 

 |  |  |  |  | 

Revenue Model |  |  |  | Margin on resold connectivity, managed services fees, SLA guarantees. Value comes | 

 |  |  |  | from aggregation, simplification, single invoice. | 

 |  |  |  |  | 

Scale |  |  | 50-500 employees, $20M-$500M revenue, national/regional coverage through carrier
relationships |  | 

 |  |  |  |  | 

 | Competitive |  |  | Blind to what happens inside carrier networks. Responsible for SLA but can't see or | 

 | Reality |  |  | prove path performance. Tier 1s going direct to their customers. | 

 |  |  |  |  | 

 |  |  |  |  | 

 | Problem |  |  | How MaiaEdge Solves It | 

 |  |  |  |  | 

Blind to what happens inside carrier networks |  |  | End-to-end visibility across all carrier relationships |  | 

 |  |  |  |  | 

 | Responsible for SLA but can't see the path |  |  | Hop-by-hop telemetry, prove SLAs to customers | 

 |  |  |  |  | 

CapEx burden doesn't match asset-light model |  |  | OpEx subscription, no infrastructure buildout required |  | 

 |  |  |  |  | 

 | Tier 1s going direct to your customers |  |  | Match Tier 1 speed and capabilities, keep relationships | 

 |  |  |  |  | 

"Depends on the carrier" kills deals |  |  | Instant activation, same-day provisioning |  | 

 |  |  |  |  |  |  |  | 

 | Question |  |  | Good Answer (Buying Signal) |  |  | Red Flag | 

 |  |  |  |  |  |  |  | 

"What visibility do you have into carrier
networks?" |  |  | "None - we're blind once traffic
enters their network" |  |  | "Full end-to-end
visibility" |  | 

 |  |  |  |  |  |  |  | 

 | "How do you prove SLA compliance to |  |  | "We rely on carrier reports - can't |  |  | "We have our own | 

 | customers?" |  |  | independently verify" |  |  | monitoring" | 

 |  |  |  |  |  |  |  | 

"What's your provisioning timeline vs.
direct carrier relationships?" |  |  | "Slower - we depend on carrier
timelines" |  |  | "Same or faster than
direct" |  | 

 |  |  |  |  |  |  |  | 

 | "How do you handle multi-carrier |  |  | "Painful - multiple tickets, finger- |  |  | "Unified visibility and | 

 | troubleshooting?" |  |  | pointing" |  |  | control" | 

 |  |  |  |  |  |  |  | 

"Are Tier 1s competing for your customers
directly?" |  |  | "Yes, and they're faster than we
are" |  |  | "We win on service,
not speed" |  | 

Objection Handling
Objection Rebuttal
"We're asset-light - we MaiaEdge is OpEx, not CapEx. You're not building infrastructure - you're
don't want adding a visibility and control layer over your existing carrier relationships.
infrastructure" Same asset-light model, better capabilities.
"Our carrier But can you see inside their networks? Can you prove SLA compliance
relationships work fine" independently? Can you provision as fast as if the customer went direct?
MaiaEdge gives you visibility and speed without replacing your carrier
relationships.
"This sounds expensive" Compare to what you're losing: customers going direct to Tier 1s, SLA
penalties you can't dispute, deals lost to 'depends on the carrier' timelines.
Subscription pricing, scales with your business.
"Our customers don't They ask for faster provisioning and SLA guarantees. Visibility is how you
ask for this visibility" deliver both. When Tier 1s can provision in days and you're quoting weeks,
visibility becomes a competitive necessity.
"Who are you?" Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology
($450M to Juniper). Two exits, $2.5B+ combined. We understand carrier
infrastructure - now we're helping aggregators compete.
Competitive Quick Hits
Competitor Quick Positioning
Megaport / Backend infrastructure you leverage via API. Without MaiaEdge, they own your customer
Equinix Fabric relationship. With MaiaEdge, you use their reach while keeping the brand and margin.
Lumen PCF Lumen builds their empire; MaiaEdge empowers you to build yours.
Tier 1 Direct Match their speed and visibility. Add your value: single invoice, multi-carrier
simplification, managed services. Now you compete on capability, not just
relationship.
Proof Points & Talk Tracks
Proof Points
Customer Quote When to Use
INDATEL Partnership enabling reach for regional Aggregation model, partner
carriers reach
Ocean Uses MaiaEdge to extend reach to INDATEL for Geographic expansion,
Networks mainland connectivity partner reach
RevNet "Imagine having Megaport capability between NaaS comparison, multi-
providers" carrier
Talk Tracks by Persona
CEO / President
Titles: CEO, President, Managing Director, General Manager

 |  |  |  |  | 

 | Objection |  |  | Rebuttal | 

 |  |  |  |  | 

"We're asset-light - we
don't want
infrastructure" |  |  | MaiaEdge is OpEx, not CapEx. You're not building infrastructure - you're
adding a visibility and control layer over your existing carrier relationships.
Same asset-light model, better capabilities. |  | 

 |  |  |  |  | 

"Our carrier
relationships work fine" |  |  |  | But can you see inside their networks? Can you prove SLA compliance | 

 |  |  |  | independently? Can you provision as fast as if the customer went direct? | 

 |  |  |  | MaiaEdge gives you visibility and speed without replacing your carrier | 

 |  |  |  | relationships. | 

 |  |  |  |  | 

"This sounds expensive" |  |  | Compare to what you're losing: customers going direct to Tier 1s, SLA
penalties you can't dispute, deals lost to 'depends on the carrier' timelines.
Subscription pricing, scales with your business. |  | 

 |  |  |  |  | 

"Our customers don't
ask for this visibility" |  |  |  | They ask for faster provisioning and SLA guarantees. Visibility is how you | 

 |  |  |  | deliver both. When Tier 1s can provision in days and you're quoting weeks, | 

 |  |  |  | visibility becomes a competitive necessity. | 

 |  |  |  |  | 

"Who are you?" |  |  | Same team that built Acme Packet ($2.1B to Oracle) and 128 Technology
($450M to Juniper). Two exits, $2.5B+ combined. We understand carrier
infrastructure - now we're helping aggregators compete. |  | 

"Our carrier

relationships work fine"

"Our customers don't

ask for this visibility"

 |  |  |  |  | 

 | Competitor |  |  | Quick Positioning | 

 |  |  |  |  | 

Megaport /
Equinix Fabric /
Lumen PCF |  |  | Backend infrastructure you can leverage via API  -  and increasingly, direct competitors for your customers' GPU compute spend. Without MaiaEdge, every tenant you send to their portal for connectivity discovers their compute offering. With MaiaEdge, you offer the same reach and on-demand experience under your brand, keep the customer relationship, and don't expose them to a competitor's portal. In cold outreach, reference them as "third-party fabric providers"  -  never by name. |  | 

 |  |  |  |  | 

 | Lumen PCF |  |  | Lumen builds their empire; MaiaEdge empowers you to build yours. | 

 |  |  |  |  | 

Tier 1 Direct |  |  | Match their speed and visibility. Add your value: single invoice, multi-carrier
simplification, managed services. Now you compete on capability, not just
relationship. |  | 

 |  |  |  |  |  |  |  | 

 | Customer |  |  | Quote |  |  | When to Use | 

 |  |  |  |  |  |  |  | 

INDATEL |  |  | Partnership enabling reach for regional
carriers |  |  | Aggregation model, partner
reach |  | 

 |  |  |  |  |  |  |  | 

 | Ocean |  |  | Uses MaiaEdge to extend reach to INDATEL for |  |  | Geographic expansion, | 

 | Networks |  |  | mainland connectivity |  |  | partner reach | 

 |  |  |  |  |  |  |  | 

RevNet |  |  | "Imagine having Megaport capability between
providers" |  |  | NaaS comparison, multi-
carrier |  | 

"Tier 1s are going direct to your customers with faster provisioning. You need to match their speed
without building infrastructure. MaiaEdge gives you visibility and control across all your carrier
relationships - OpEx model, no CapEx buildout. Compete on capability, not just relationship."
VP Operations / Service Delivery
Titles: VP Operations, VP Service Delivery, VP Network Operations, Director of Operations
"You're responsible for SLAs but blind to what's happening inside carrier networks. When there's an
issue, you're stuck between your customer and carriers pointing fingers. MaiaEdge gives you hop-by-hop
visibility across all carriers - prove SLA compliance, troubleshoot faster, stop the finger-pointing."
VP Sales / Business Development
Titles: VP Sales, VP Business Development, VP Partnerships, VP Commercial
"When you quote 'depends on the carrier' timelines, customers go direct to Tier 1s. What if you could
provision as fast as they can? MaiaEdge gives you instant activation across your carrier network. Same
asset-light model, same relationships - now with the speed to win."
---

## Sub-Segments Within This Segment (HubSpot enum values)

The MSP/Aggregator segment splits into **5 explicit sub-segments** matching HubSpot `company_sub_segment` enum values (case-sensitive). Each has its own vocabulary, target personas, anchor accounts, and competitive lens. Keep the file unified - every talk track, proof point, and objection rebuttal below is flagged with its sub-segment scope so the copy engine picks the right register.

**Classification rules, anchors, confidence thresholds:** See file 06 §6.5 and `context/account-tiering/icp-deep-dives/B-and-C-msp-aggregator.md`.

### Sub-segment 1: `Telecom Aggregator - MSP`

- **CRM volume:** ~288 records.
- **Tier:** default Tier 2 (ceiling 1, floor 4).
- **Who they are:** Traditional channel aggregators / telecom brokers reselling carrier connectivity to enterprises. Direct sales, no sub-agent layer.
- **Scale:** $20M-$2B revenue, 30-100 carrier vendors, US-focused.
- **Anchors:** Granite Telecommunications ($1.85B 2024), Nitel (post-Hypercore 2022).
- **Exclude (D1.5 disqualifier):** IoT/eSIM platforms (Aeris, EMnify, Wireless Logic). They operate mobile packet cores and ride GSMA-layer interconnects, not fixed-line L2/L3 NNIs.
- **Vocabulary:** carrier line-card, single invoice, multi-carrier procurement, enterprise direct sales, SLA aggregation.

### Sub-segment 2: `Managed Network Services - MSP`

- **CRM volume:** ~26 records.
- **Tier:** default Tier 2 (ceiling 1, floor 4).
- **Who they are:** MSPs, integrators, and VARs whose primary offering is managed network services (NOT commission resell). 70%+ managed services contracts.
- **Scale:** $50M-$10B revenue.
- **Anchors:** Open Systems; Hughes Network Systems (EchoStar; pending DISH merger); Logicalis (Datatec); Presidio (BC Partners 2019, ~$5B+); GTT (post-2021 divestiture managed services); IT integrators CDW, Insight, ePlus, WWT are boundary cases.
- **Note:** Post-Phase 1.7c.1 the suffix is `- MSP` (legacy `- Network Operator` suffix archived 2026-05-13).
- **Vocabulary:** managed SD-WAN, NOC operations, MTTR, ITIL change control, managed services contract, co-managed network, vCIO.

### Sub-segment 3: `TSD Technology Services Distributor - MSP`

- **CRM volume:** 0 records currently. Canonical TSD brands (TD SYNNEX, ScanSource, Intelisys, AppDirect) are not yet sourced into CRM and are flagged for follow-up sourcing.
- **Tier:** default Tier 3 (ceiling 1, floor 5).
- **Who they are:** Distribution-tier orgs with sub-agent / 1099 channels of 100+ active agents. Gross billings $1B+.
- **Scale:** 100+ carrier vendors, US national plus Canada / EU.
- **Anchors (per Omdia CY2024):** Telarus ($2.9B GB), AVANT ($2.1B), Intelisys/ScanSource ($2.7B; net agency $84.7M ScanSource), AppDirect ($2.0B), Sandler Partners (~$209M revenue - UPWARD revision from prior $25M), Bridgepointe ($755M GB; firmly TSD-tier post April 2026 Charlesbank+Carlyle recap at $1B+ valuation).
- **Vocabulary:** TSD, Technology Advisor, master supplier agreement, residual commissions, SPIFF, line-card, deal registration, quoting platform, partner enablement.

### Sub-segment 4: `Master Agent - MSP`

- **CRM volume:** ~3 records.
- **Tier:** default Tier 3 (ceiling 1, floor 5).
- **Who they are:** Smaller, often regional or vertical-focused master agencies with sub-agent networks. Boutique cousins of TSDs.
- **Scale:** Net commission $5M-$100M, 10-50 sub-agents.
- **Anchors (post-consolidation, per Phase B):** X4 Solutions (confirmed independent 2025; 35+ carriers, founded 2004); CyberNet Communications (medium confidence; regional, scale unverified). Only 2 verified independents per Phase B.
- **Default policy (Cooper feedback 2026-05-14):** Classify best-fit (no default `manual_review_required`). REVERSED from prior policy that defaulted to manual review. Use `low_5069` confidence for thin anchor verification; D7 weekly routine re-validates.
- **Vocabulary:** sub-agent network, master agency, regional carrier panel, vertical specialization, residual book.

### Sub-segment 5: `Cloud + Telecom Hybrid MSP - MSP`

- **CRM volume:** ~24 records.
- **Tier:** default Tier 2 (ceiling 1, floor 4).
- **Who they are:** MSPs whose business spans cloud reselling AND telecom managed services. 30-60% cloud / 30-60% network.
- **Scale:** $30M-$5B revenue, AWS Premier / Azure Expert / GCP Premier partner.
- **Anchors:** AHEAD ($3B 2024 est., reportedly exploring sale); CDW (post-Mission Cloud Dec 2024 - boundary case); Insight Enterprises (post-SADA Dec 2023 - boundary case); WWT; ePlus; Effectual Cloud; RapidScale (Cox/RapidScale; pending Charter merger).
- **Exclude (D1.5 disqualifier):** Pure cloud MSPs without network services (post-acquisition Mission Cloud standalone, SADA standalone).
- **Vocabulary:** cloud landing zone, hyperscaler partner tier, multi-cloud networking, managed cloud + connectivity, cloud-adjacent network managed services.

### NaaS Platform Operator subtype - RETIRED (2026-05-14)

Per Cooper 2026-05-14: NaaS platforms (CBC Tech, Epsilon, Console Connect, Arelion wholesale, Sparkle Sparkhub) are **no longer mapped to any MSP sub-segment**. Classify as:
- `customer_segment = "Other"` when the org is a competitive reference / platform peer we want visibility on but won't sell to.
- `customer_segment = "Flagged for deletion"` when no commercial or competitive value remains.

The NaaS Platform Operator talk tracks, proof point archetypes, and anti-patterns below remain in the file as historical reference. Do NOT use them on `customer_segment = "MSP/Aggregator"` records. They may still inform competitive intel work routed through the `competitive-intel` skill.

---

## Talk Track: Credit the Platform (NaaS Platform Operator subtype only)

Highest-performing first-touch angle for NaaS platform operators with their own proprietary fabric or portal. Structure is three moves.

1. **Name their platform.** Use its actual product name if known (eNet Fabric, Infiny, Conexa, Console Connect, etc.). If unknown, reference the platform generically ("your NaaS platform," "your customer portal"). Signals research and respects the asset they've built.
2. **Acknowledge what it does well.** The platform itself is fast, automated, on-demand. Don't pitch them on attributes they already own.
3. **Name where the platform ends.** Every deal that requires partner carriers for delivery hits a timeline the platform can't solve. That partner-boundary gap is where MaiaEdge fits.

### Template sentence patterns

- "[Platform name] is what you control end-to-end. The moment a deal requires partner carriers, your automation hits someone else's timeline."
- "[Platform name]'s click-to-order experience meets their activation queue."
- "The overlay scales fast. The underlying carrier capacity in each market doesn't scale with it."
- "Every deal outside your direct PoP footprint rides partner carriers."

### Anti-patterns (do NOT do)

- Don't pitch "visibility" or "automation" as primary value. They have those. The gap is at the partner boundary, not inside their platform.
- Don't imply the platform is slow. It isn't. The partner-NNI cycle behind it is.
- Don't use "break carrier dependency" or "cut out carriers." Their business IS multi-carrier orchestration. MaiaEdge extends their reach through partners, not around them.
- Don't position as platform-replacement. They built the platform; we extend it.

---

## TSD Landscape (verified anchors, for Subtype 1 targeting)

Tier 1 TSDs (US channel):
- **Telarus** (Sandy, UT)  -  #1 market share per Omdia/Canalys. GeoQuote + Telarus Hub platform.
- **AppDirect** (CDPQ-backed)  -  10K advisors, 1,000+ providers. 2025-26 M&A: NXTSYS, vCom Solutions, Tackle.io, PartnerStack. ⚠️ Building in-house orchestration post-vCom  -  competitive risk.
- **Upstack** (Berkshire Partners-backed)  -  36 acquisitions through 2025.
- **AVANT** (Pamlico / Court Square recapitalization Dec 2025)  -  300+ providers. Pathfinder decision platform.
- **Bridgepointe** (Charlesbank / Carlyle AlpInvest recap April 2026, >$1B valuation)  -  400+ IT Strategists. "The Signal" portal processes 100% of orders. Scott Kinka positioning: "competitor to the big five consulting firms, not to TSDs."
- **ScanSource Intelisys** (NASDAQ SCSC)  -  FY25 $3.04B total. Recurring revenue mix 29.3% → 36.0% Q3 FY25 (public earnings-disclosed shift from bandwidth reselling to platform / recurring services).

Tier 2 TSDs:
- **Sandler Partners** (independent)
- **TD SYNNEX** (NYSE SNX)  -  connectivity is secondary to IT hardware motion.

### Technology Advisor (TA) Persona Split

**Owner-operator TA** (1-5 person agency): Multi-TSD on average (per Channel Futures Q3 2024: 2.9 TSDs per TA; 24% single-TSD, 32% dual). Residual-driven. Full autonomy on vendor selection. Risk-averse because churn hits paycheck directly.

**W-2 TA at large TSD** (Bridgepointe IT Strategist, AVANT Trusted Advisor, Intelisys AE): Approved-vendor gated. Single-organization loyalty. Can deploy new vendors rapidly once TSD onboards them. Enterprise logo scale.

### Target Priority (for MSP line-card entry)

CRO / VP Supplier Strategy / VP Platform / Head of AI Practice / VP Solutions Engineering at the TSD drive line-card onboarding. Target these first. TAs are secondary  -  once a TSD onboards MaiaEdge, TAs can pull it into deals via the quoting platform.

### Discovery Mechanism (for TSD line-card entry)

- **Podcasts:** Telarus "Next Level BizTech" (weekly, Josh Lupresto host), Bridgepointe "The Bridgecast with Scott Kinka" (biweekly), Telecom Reseller (Doug Green host), TalkingPointz / TalkingHeadz (Dave Michels).
- **Events:** Channel Partners Expo (April 13-16, 2026, Las Vegas), AVANT Special Forces, Telarus Partner Summit, Sandler Partners National Summit, Bridgepointe Tech Summit.
- **LinkedIn influencers:** Scott Kinka (Bridgepointe), Drew Lydecker (AVANT), Adam Edwards (Telarus), Patrick Oborn (Telarus).

### Entry Motion

TSD master supplier agreement is the path. Line-card onboarding, not direct-to-TA bypass. TAs work off TSD-gated approved-vendor lists.

---

## ICP Exclusion List (NOT MaiaEdge ICP)

Companies that pattern-match "aggregator" by name or positioning but are NOT MaiaEdge ICP. Filter these out of outreach:

- **Voice termination wholesalers.** LD / VoIP / SIP-termination businesses managing voice routes (LCR tables, ASR/ACD quality, PDD), not L2/L3 data paths. Title tells: "Network Profitability," "Route Management," "Voice Operations." Examples: iBasis voice, Tata voice, IDT, BICS voice, Intelepeer, Sangoma, Flowroute, Vinculum, Telstar Express, SIPSTATUS.
- **SMS / A2P / CPaaS aggregators.** Message routing over SMPP/SS7/HTTP, not connectivity. Examples: Sinch, Infobip, Bird/MessageBird, Twilio, Bandwidth, Route Mobile, Monty Mobile, Telnyx, Vonage, TeleSign, Soprano, BICS Messaging, Go4Mobility.
- **Cellular IoT MVNOs.** Operate their own mobile packet core (5G Core / EPC), ride GSMA-layer interconnects (roaming, IPX, eSIM), not L2/L3 fixed-line NNIs. Examples: Wireless Logic, Kore Wireless, 1NCE, EMnify, Aeris, Transatel, Telit Cinterion, Soracom, Cisco Jasper, floLIVE, Truphone/1GLOBAL.
- **Roaming hubs / IPX providers** (not data transit). Examples: BICS, Syniverse, TATA IPX, Orange IPX, iBasis roaming.
- **eSIM / SIM platform vendors.** Examples: Thales, Giesecke+Devrient, IDEMIA, Valid.

### Self-Filtering Copy Rule

If Email 1 vocabulary reads coherent to any of the above categories, the copy is too generic. Fixed-line-specific terms (Ethernet NNI, IP transit, wavelength, L2/L3 path, cross-connect, Direct Connect, ExpressRoute, dark fiber, cloud on-ramp) filter these out because voice/SMS/IoT MVNO recipients don't operate in that vocabulary. **Aim for copy that sounds unintelligible to voice wholesalers.** That's how you know it's hitting the right ICP.

---

## Proof Point Archetypes (anonymized  -  cold outreach rule)

Existing US-channel proof points (INDATEL, Ocean Networks, RevNet) remain available for Subtype 1 (US TSD/TA). For Subtype 2 (NaaS Platform Operator), use these anonymized archetypes:

| Customer Archetype | Anonymized Frame | When to Use |
|---|---|---|
| Global NaaS platform with proprietary fabric | "A NaaS platform operator with a proprietary customer portal uses MaiaEdge to extend their portal's activation experience across partner carriers in markets where they don't own PoPs." | CBC Tech / Epsilon / Console Connect-style prospects |
| International wholesale carrier with multi-region expansion | "A regional wholesale carrier operating in three countries uses MaiaEdge to automate partner-NNI activation at every cross-border handoff." | Media Commerce / regional LatAm or APAC operators |
| Subsea / landing-station operator | "A global carrier with transatlantic landings uses MaiaEdge for terrestrial extension from landing stations into customer networks across EMEAA." | Telxius / subsea-wholesale prospects |

All remain anonymized per the cold-outreach rule.

---

## Industry Landscape (2025-2026)

### Channel Rebranding & Growth
The channel hit $16B in 2025 (Bain estimate), up from $12B in 2024, with industry leaders setting $100B 10-year ambitions. The rebranding is complete: "Master agents" are now "Technology Services Distributors" (TSDs). "Agents" are "Technology Advisors" (TAs). Use THEIR new terminology  -  calling someone an "agent" signals you're behind.

### SD-WAN Is Table Stakes
~90% of companies using or adopting SD-WAN. Market: $7.91B (2025) to $21.67B (2030). No longer a differentiator  -  not offering it is a competitive disadvantage. SASE cannibalizing MPLS: ~$4B (2024) to ~$17B (2030) at 25-30% CAGR.

### The AI Readiness Gap
58% of buyers identified AI as their top priority (up from 13% in 2023), but only 13% of TAs feel "very prepared" to sell AI solutions. This is the single biggest opportunity-gap in the channel right now.

### AI-Augmented Operations
AI automating up to 70% of routine NOC tasks. "Dark NOC" concept = fully autonomous network operations powered by agentic AI. Major vendors pushing "NOCless" operations. Incident response times cut by 50%, 30% operational cost reduction. Leading MSPs already have AI-powered NOC dashboards in production.

### What the Leaders Are Doing
The most advanced MSPs are launching unified service portals, AI-powered NOC dashboards, and on-demand networking models that eliminate fixed contracts and ETFs. TSDs are acquiring CX and AI specialty firms to expand their offering. Deal sizes are growing  -  top TAs increasingly selling six-figure deals into upper-midmarket and enterprise.

### Cybersecurity as Growth Engine
Fastest-growing MSP category at 18% annual growth (outpacing overall MSP growth of 14%). UCaaS, networking, and cybersecurity are the top-three TA revenue categories. vCIO, compliance-as-a-service, and automation consulting emerging as premium offerings.

### Enterprise Bypass Accelerating
Azure ExpressRoute going 400G in 2026. AWS Direct Connect expanding. Google Cloud Interconnect growing. Each expansion is another path for enterprises to bypass MSP/carrier relationships entirely. Mid-market outpacing enterprise in AI adoption  -  92% expect IT budget increases.

### Financial Pressures
MSP M&A surged 20% to 466 deals in 2025 ($4.3B disclosed value). Margin compression from carrier direct sales, hyperscaler bypass, and SD-WAN vendors going direct (Fortinet, Palo Alto, Cato). Well-run telecom resellers still capturing 50-75% gross margins on voice/UCaaS bundles. White-label solutions providing 30-50% margins on MRR.

### AI Supply Constraints Flow Through to Your Customers
NVIDIA B200/GB200 allocation is tightly managed, CoWoS advanced packaging has 60-week lead times, and mid-2026 compute supply won't meaningfully ease until late 2026. That isn't just an AI cloud problem  -  it's why your customers can't get AI capacity on demand from AWS, Azure, or direct AI clouds when they need it. The 58/13 gap (58% of buyers want AI, 13% of TAs feel prepared) isn't just a readiness story. It's a capacity-access story. MSPs who can guarantee AI capacity to mid-market customers through upstream partnerships with sovereign AI clouds, regional AI clouds, and AI-ready colos win the deals Fortune 500-focused hyperscalers can't serve fast enough. This is the AI-as-a-service conversation you are positioned to capture  -  if you have the upstream relationships and the visibility layer to deliver on the promise.

### Forced Modernization from Regulation Is a Pipeline Driver
STIR/SHAKEN enforcement, TDM sunset timelines, copper retirement mandates, and 18 US state privacy laws are creating reluctant-buyer demand you can convert. Customers who weren't planning to modernize are now legally required to  -  and they're looking for a Technology Advisor who can run the transition, not just quote circuits. Frame compliance-forced projects as the pipeline driver they are, not as paperwork. EU AI Act enforcement (August 2026) starts reaching US MSP customers through extraterritoriality and the contracts they sign with EU subsidiaries. DPDP Act enforcement (May 2027) does the same for customers with Indian users. Regulation is a demand creation engine for MSPs willing to sell the transition, not just the circuit.

### Sovereignty Pass-Through: Your Customers Are Inheriting It
Sovereign data requirements are no longer a "government and healthcare only" problem. Your mid-market customers are inheriting data-residency and path-sovereignty requirements from their OWN customers (EU subsidiaries, regulated industry contracts, government procurement passthrough). They don't have the sophistication to answer these requirements  -  they need a Technology Advisor who can. MSPs who can deliver sovereign-capable upstream fabric (paths with policy control and jurisdictional audit trails, not just BGP best-effort) keep these deals. MSPs who send customers to Megaport/Equinix portals for connectivity lose the touchpoint AND can't answer the sovereignty question at all.

### What the C-Suite Is Focused On
- AI readiness: 58% of buyers want it, only 13% of TAs feel prepared
- Differentiation beyond resale  -  what can you offer that carriers going direct can't?
- Platform consolidation: unified PSA + RMM + monitoring + security + reporting
- The "Technology Advisor" identity  -  moving from order-taker to strategic partner
- Cybersecurity and AI as new revenue pillars beyond UCaaS/networking
- Enterprise bypass risk from hyperscaler direct interconnects

---

## Their Information Diet

### What They Read
- Channel Futures, CRN, Channel Partners, SDxCentral

### Analyst Firms They Trust
- Bain (channel sizing), Canalys, IDC

### Where They Gather
- AVANT Special Forces, Telarus Partner Summit, Channel Partners Conference & Expo

---

## Competitive Dynamics (Their Market)

These are who MSPs/AGGREGATORS compete against  -  not MaiaEdge competitors.

### Carrier Direct Sales
Tier 1s increasingly selling directly to enterprise, bypassing the channel for large/complex deals. Aggressive bundling and SaaS disintermediation.

### Hyperscaler Networking
AWS Direct Connect, Azure ExpressRoute (400G in 2026), Google Cloud Interconnect. Each lets enterprises bypass traditional carrier/MSP relationships entirely.

### SD-WAN Vendors Going Direct
Broadcom VeloCloud, Fortinet, Palo Alto Prisma, Cato Networks selling their own managed offerings. Customers choosing vendor-managed SD-WAN over MSP-managed.

### MSP/TA Convergence
Both compete for the "single provider" relationship. Clients demanding all-in-one service delivery from a single vendor.

### PE-Backed Competitors
35% of new US passes are PE-funded, bringing aggressive pricing and acquisition-driven scale that organic-growth MSPs can't match.

---

## MaiaEdge Relevance Bridges

> **⚠️ Internal angle-selection guide.** Specific figures (channel $16B, SD-WAN market sizing, 58/13 AI readiness gap, 70% NOC automation, $4.3B MSP M&A value, ScanSource 29.3% → 36.0% recurring-revenue mix) are **internal triggers for picking which angle to lead with**. They are NOT customer-facing talking points. Do not cite these figures in cold outreach or LinkedIn. Use them to determine which relevance bridge fits the account, then write in segment vocabulary with the subtype-appropriate register.

How current industry trends connect to problems MaiaEdge solves. Use across the full sales motion.

| Their Trend | Their Pain | MaiaEdge Angle |
|---|---|---|
| Carrier direct sales bypassing channel | Losing enterprise deals to carriers who sell direct  -  need differentiation beyond resale | "Carriers are going direct. You need something they can't offer  -  real-time visibility into THEIR networks." |
| Azure ExpressRoute going 400G | Another path for enterprises to bypass MSP/carrier relationships entirely | "Every new hyperscaler interconnect option is one more reason your customers might not need you. Visibility is your moat." |
| Dark NOC / AI-augmented operations | Competitors automating 70% of NOC tasks  -  manual operations becoming a cost disadvantage | "Your competitors are automating their NOC. MaiaEdge gives you the visibility layer to do the same." |
| Finger-pointing during outages | Responsible for SLA but blind to carrier networks  -  customer trust erodes with every "depends on the carrier" | "Stop saying 'depends on the carrier.' MaiaEdge shows you exactly where the problem is, in real time." |
| Channel rebranding to "Technology Advisor" | Expected to advise on AI, cybersecurity, cloud  -  not just resell circuits | "Your customers expect a Technology Advisor. MaiaEdge lets you advise on network performance with data, not guesses." |
| Mid-market AI adoption outpacing enterprise | Fastest-growing buyer segment wants AI-powered networking but MSPs aren't ready | "Mid-market is buying AI solutions faster than enterprise. They're looking for an advisor who can deliver." |
| NVIDIA/CoWoS AI supply constraints (60-week lead times, allocation scarcity) | Customers can't get AI capacity from hyperscalers fast enough  -  the 58/13 gap is partly an access problem, not just a readiness problem | "Your customers can't get AI capacity when they need it. MSPs with robust upstream partner access guarantee capacity. That's the AI-as-a-service conversation, not 'we can resell your Azure bill.'" |
| TDM sunset + STIR/SHAKEN + 18 state privacy laws | Regulation forcing modernization pipeline  -  customers need a Technology Advisor to run the transition, not a circuit quote | "Compliance deadlines are a pipeline. Reframe 'we have to migrate off TDM' from paperwork to project  -  and be the advisor who runs it." |
| TSD recurring-revenue mix shifting from bandwidth reselling to platform / recurring services | The bandwidth-residual model is compressing; platforms are where growth is | "Existing residuals stay flat. MaiaEdge adds an OpEx tier on top of the bandwidth revenue chain  -  white-label platform you can sell, not another bandwidth line-card." |
| TSD platform / portal / quoting-engine replatforming (integration team hiring) | Connector-building window opens when TSDs hire supplier strategy / platform engineering / developer experience roles | "Replatforming windows are connector-building windows. MaiaEdge slots in as an OpEx platform you white-label during the rebuild." |
| NaaS platform operators facing portal-speed vs. partner-NNI delivery-gap problem | The click-to-order experience ends the moment a deal rides partner carriers | "Credit their platform. Extend its activation experience across partner carriers in markets where they don't own PoPs." (NaaS subtype only) |
| AI Practice / AI Solutions launches at TSDs (58/13 readiness gap) | Buyer demand outpaces TA readiness to sell AI; TSDs launching AI practices are looking for pre-integrated platforms | "Audio Codes Live Platform pattern: provisioning weeks → hours, OpEx -30%. MaiaEdge is the multi-operator equivalent your AI Practice can white-label." |
| Sovereignty pass-through to mid-market | Customers inheriting data-residency requirements from THEIR customers (EU subsidiaries, regulated industry contracts) and have no answer | "Your customers are about to be asked to prove path sovereignty. You either have a sovereign-capable fabric to deliver it, or you lose the touchpoint to a third-party fabric that can." |
| EU AI Act Aug 2026 + DPDP extraterritorial enforcement | US mid-market customers facing EU/India compliance obligations through their own contracts | "EU AI Act fines reach 7% of global revenue. Your customers with EU users need you to have an answer now, not in Q3." |

---

## Insider Language Bank

Things MSP/aggregator executives say internally  -  use these to demonstrate you understand their world.

### Board Meeting Language
- "58% of our customers want AI solutions. Are we ready to sell them?"
- "The leading MSPs just launched on-demand networking with no fixed contracts. Our customers are going to ask."
- "The Dark NOC isn't science fiction  -  autonomous network operations are going mainstream"
- "Azure ExpressRoute goes 400G this year. Another path for our customers to bypass us."
- "Our buyers rebranded us from 'agent' to 'Technology Advisor.' Are we advising on AI yet?"
- "UCaaS got us here. Cybersecurity and AI will get us to the next level."
- "We're blind to what happens inside carrier networks but we own the SLA"
- "'Depends on the carrier' is losing us deals"
- "The 58/13 gap isn't just about readiness  -  our customers can't GET AI capacity from hyperscalers on demand"
- "Compliance deadlines (TDM, STIR/SHAKEN, state privacy laws) are a pipeline, not paperwork"
- "Our mid-market customers are inheriting sovereignty requirements from THEIR customers. We need an answer."

### KPIs They Report
MRR, churn rate, TCV per deal, residual commission rates, MTTR, SLA compliance %, ticket resolution time, NOC utilization, customer acquisition cost, revenue per TA

### Business Terms to Know
TSD (replacing "master agent"), TA (replacing "agent"), Dark NOC, agentic AI operations, quote-to-cash, zero trust, ZTNA, FWaaS, CASB, MDR, CX platforms, CCaaS, CPaaS, deal registration, SPIFF, MDF, partner portal, E-Rate, STIR/SHAKEN, TDM sunset, POTS replacement, copper retirement, residual commissions, TCV

---

## Segment Vocabulary Lock

### MUST-Use Terms (MSP / Aggregator)

**General (both subtypes):** finger-pointing, SLA compliance, asset-light, single pane of glass, carrier relationships, Tier 1, aggregation, multi-carrier, provisioning timeline, managed services, OpEx, reach beyond your carriers, turn spare capacity into sellable services, connectivity marketplace.

**NaaS Platform Operator subtype (additions):** platform speed, click-to-order, customer portal, self-service ordering, on-demand connectivity, platform experience, underlying carrier, partner boundary, partner-NNI, activation queue, activation cycle.

**Proprietary-fabric awareness (NaaS subtype):** When the prospect's platform has a product name (eNet Fabric, Infiny, Conexa, Console Connect, etc.), ALWAYS use the actual product name in the copy  -  never generic "your platform."

**Cross-border / international expansion (NaaS subtype):** cross-border activation, new-market expansion, partner extension, reach beyond your footprint, monetize internationally, region-to-region corridor.

**Downgraded:** `upstream carrier` is acceptable only when paired with L2/L3-specific context. It reads coherent to voice wholesalers today. Prefer "partner carrier," "downstream carrier handoff," or "cross-carrier handoff" in NaaS aggregator copy.

### BANNED Terms (From Other Segments + exclusion-category filters)

**From other MaiaEdge segments:** route miles, NNI (fiber/network operator context), tenant, meet-me room, cross-connect, attach rate, dark fiber, plant, fiber islands, inference, jitter, GPU, facility (colo context), middle mile, training run, recompute tax, egress (neocloud context), LOA (fiber/network operator context).

**Voice / SMS terminology** (filters out voice wholesaler + CPaaS false positives): ACD, ASR, PDD, CLI, SIP trunking, A2P, SMPP, SS7, LCR, route margin, per-minute margin, call completion, CNAM, STIR/SHAKEN.

**Cellular / mobile terminology** (filters out IoT MVNO false positives): eSIM, IMSI, multi-IMSI, MNO, MVNO, roaming agreement, GSMA, IPX, IR.21, IR.85, SIM profile, AITRAS, 5G Core, EPC, PGW, UPF.

### Cold Outreach Rules
- Credibility anchors ("Same team that built Acme Packet" / "128 Technology" / Andy Ory etc.) are BANNED in cold emails and LinkedIn. The message does the talking in outreach. Allowed in live presentations, demos, proposals, and objection handling  -  the track record does the talking in rooms.
- NO sign-offs in emails. Signatures are auto-appended by the email platform.
- Respect the asset-light model. Never use "build infrastructure" or "deploy hardware" language. MaiaEdge is a visibility and control layer, not an infrastructure buildout.
- Pair speed with ownership where it fits, but the MSP's value is aggregation and simplification, not infrastructure ownership. Lead with visibility and speed.
- New angles: reach (extend coverage to new markets through partners without new carrier contracts) and monetization (turn spare capacity into sellable services, not just resell carrier circuits).

---

*Cross-references: Messaging Framework V4, ICP Sales Playbook (Complete Reference), Cloud On-Ramp Business Case, Competitive Positioning Guide, Terminology Glossary*
*Updated: April 2026 (trend refresh: AI supply constraints flow-through, regulation as pipeline driver, sovereignty pass-through to mid-market)*
