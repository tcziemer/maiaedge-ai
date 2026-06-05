# MSP/Aggregator — Industry Taxonomy Alignment + 5 Sub-Segment Deep Dives

**Scope:** MSP/Aggregator ICP only (HubSpot `customer_segment = MSP/Aggregator`, 345 records).
**Sub-segments covered (all 5 active values from HubSpot enum verification 2026-05-14):**

1. `Telecom Aggregator - MSP`
2. `Managed Network Services - MSP`
3. `TSD Technology Services Distributor - MSP`
4. `Master Agent - MSP`
5. `Cloud + Telecom Hybrid MSP - MSP`

**Source basis:** File `05 - Sub-segment definitions for cheatsheets.md` (v2.1, validated 2026-05-13), `context/segments/msp-aggregator.md`, `context/signals/msp-aggregator-signals.md`, Omdia 2024 TSD Market Report (published Jan 2026; covers CY2024), Channel Futures MSP 501 (2025), CRN Solution Provider 500 (2025), Gartner MQ Managed Network Services (2025/2026), public press releases (CDW/Mission Cloud, Insight/SADA, Bridgepointe/Charlesbank/Carlyle), and ChannelE2E / Channel Dive coverage 2024-2026.

**HubSpot enum architectural note:** Per `00-hubspot-enum-verification.md`, the value `Managed Network Services - MSP` is the live HubSpot enum (post-Phase-1.7c.1 rename; legacy `- Network Operator` suffix archived). File 05 still references `Managed Network Services - Network Operator`; **THIS DOCUMENT TREATS `Managed Network Services - MSP` AS CANONICAL** per the live enum verification.

---

## TOP SECTION — Industry Taxonomy Alignment (~500 words)

### Channel Futures MSP 501 vs MaiaEdge mapping

The Channel Futures MSP 501 (2025 edition) ranks "Managed Service Providers" without distinguishing TSD from Master Agent from Telecom Aggregator from Managed Network Services from Cloud+Telecom Hybrid. The list aggregate is $13.8B with ~$29M average revenue per ranked MSP and ~$16M average recurring (up 14% YoY). Top 5 (Ensono, Zayo, Expedient, Assured Data Protection, Personified Tech) cross MaiaEdge segment lines — Zayo is a Fiber Operator (Tier 2 National Wholesale), Ensono / Expedient / Assured Data Protection are Managed Network Services or Cloud + Telecom Hybrid by our taxonomy, and many MSP 501 entries fail MaiaEdge ICP entirely (pure IT helpdesk, pure cybersecurity MSPs). **Treat MSP 501 as a discovery list — it surfaces candidates — but every classification must be re-derived against our 5-value enum.**

### Omdia TSD Market Report vs MaiaEdge mapping

Omdia's January 2026 report sized the TSD market at **$16.6B in CY2024 gross billings (+14.5% YoY)**, with the **top 6 TSDs controlling 72.3% share**. Verified gross billings (CY2024):

| TSD | CY2024 GB | YoY |
|---|---|---|
| Telarus | $2.9B | +11% |
| Intelisys (ScanSource brand) | $2.7B | +4.5% |
| AVANT Communications | $2.1B | +19.5% |
| AppDirect | $2.0B | +12.0% |
| Sandler Partners | ~$209M revenue (24% growth — net commission, not gross billings) | +24% |
| Bridgepointe | $755M | +32% |

Omdia's category cleanly maps to MaiaEdge's `TSD Technology Services Distributor - MSP` value. Sandler is a top-6 TSD by Omdia despite reporting in net commission revenue rather than gross billings (industry norms split here — gross billings is the standard, but Sandler discloses differently). **Bridgepointe was recapitalized April 2026** ($1B+ valuation, Charlesbank-led with Carlyle AlpInvest) — confirms TSD-tier status and removes any "boundary case with Master Agent" framing.

### The 2018-2024 consolidation narrative

Independent master agents have been systematically rolled up: **WTG → AppDirect/AppSmart (2018)**, **MicroCorp → AppDirect/AppSmart (Dec 2020)**, **CNSG → AppDirect/AppSmart (earlier)**, **Telegration → AppDirect/AppSmart (earlier)**, **PlanetOne → AVANT (May 2022)**, **TBI → Telarus (2021)**, **CarrierSales → Telarus (2021)**, **Chorus Communications → Telarus (2021)**, **TCG → Telarus (2022)**, **Americomm → Telarus (2023)**, **Clover Communications → Bridgepointe (earlier)**. **The independent master agent category is structurally thin in 2025-26.** See per-sub-segment treatment under "Master Agent - MSP" below.

### Exclusion gates

- **IoT / eSIM platforms:** Aeris (acquired Ericsson IoT business 2023, manages 93M+ IoT devices), EMnify, Wireless Logic, Kore Wireless, 1NCE, Soracom, Telit Cinterion — these pattern-match "aggregator" by name but operate cellular MVNOs and are NOT in scope. EXCLUDE.
- **Voice termination wholesalers / SMS-A2P / CPaaS:** iBasis voice, Sinch, Infobip, Twilio, Bandwidth, Telnyx — voice/messaging route management, not L2/L3 data path. EXCLUDE.
- **Roaming hubs / IPX providers:** BICS, Syniverse — GSMA-layer interconnects, not fixed-line NNIs. EXCLUDE.
- **Pure cloud MSPs (no network services):** AWS/Azure/GCP MSPs without explicit network managed services offering — EXCLUDE. The qualifying signal for `Cloud + Telecom Hybrid MSP - MSP` is meaningful network managed services book alongside cloud reselling.

### Reverse-mapping concerns — IT integrators (CDW, Insight, ePlus, WWT)

CRN Solution Provider 500 ranks IT integrators above all MaiaEdge MSP/Aggregator anchors by revenue: CDW ~$22B, WWT ~$20B (with $500M AI lab investment), Insight ~$11B (post-SADA), ePlus ~$2.2B. Three of these companies actively pursued cloud + network consolidation through 2024-2025:

- **Insight + SADA (Dec 2023, $410M):** SADA was a 6-time Google Cloud Partner of the Year. Now Insight's Google Cloud practice (850 professionals into Insight's 14,500-team global ops). Cloud+Telecom Hybrid signal.
- **CDW + Mission Cloud (Dec 2024):** Mission was AWS Premier Tier + AWS Security Partner of the Year. Now CDW's dedicated AWS practice. Cloud+Telecom Hybrid signal.
- **AHEAD + Computer Design & Integration (Feb 2024):** Earlier AHEAD acquisition; reportedly exploring sale 2024-25 at ~$3B revenue. Cloud+Telecom Hybrid.

**Policy recommendation for IT integrators ≥$10B revenue (see "Critical clarifications" section below):** Default classification is `Cloud + Telecom Hybrid MSP - MSP` IF the company has clearly disclosed AWS Premier / Azure Expert / Google Cloud Premier status AND a network services book (SD-WAN, managed circuits, MNS). Default to `Managed Network Services - MSP` IF the cloud component is absent or de minimis. Boundary cases (e.g., where the cloud book is rapidly growing post-acquisition like CDW post-Mission) get `manual_review_required` and reasoning note "Cloud + Telecom Hybrid candidate pending integration."

---

# SUB-SEGMENT DEEP DIVES

---

## 1. `Telecom Aggregator - MSP`

### Definition

Traditional channel aggregators / telecom brokers that resell carrier connectivity products (MPLS, SD-WAN, dedicated internet, dark fiber, voice/UCaaS) to enterprises through a primarily-W-2 or hybrid (1099 + W-2) direct sales force. Multi-vendor agency model that aggregates carrier contracts and bills the customer directly. **No (or minimal) sub-agent / 1099 channel network** — that's the boundary against TSDs and Master Agents. The legacy "telecom broker" archetype that pre-dated the TSD rebranding.

### Quantitative markers

- **Revenue:** $20M – $2B (widened from file 05's prior $50M-$500M; Granite at $1.85B is canonical scale anchor, the segment spans more than the original draft acknowledged)
- **Sales force:** W-2 dominant with possible 1099 hybrid; NOT a sub-agent network model
- **Customer segments:** SMB and mid-market primary; some enterprise multi-location
- **Vendor portfolio:** 30-100 carriers (smaller than TSD portfolios which run 100-300+)
- **Geographic scope:** US-primary with possible Canada/Mexico extension for multi-location enterprise plays
- **Revenue mix:** ~70-90% reselling carrier connectivity products + ~10-30% managed services / value-add layered on top
- **Headcount:** 50-2,000 employees (Granite is the scale outlier at 1,000-5,000)

### Required signals

- **Marketing language** emphasizing "carrier-neutral," "multi-carrier," "single invoice," "aggregation," "one throat to choke" — NOT "sub-agent network" or "Technology Advisor channel"
- **Customer-facing portal** that orders carrier products directly (not a sub-agent-facing quoting platform)
- **Direct enterprise / mid-market sales team** with named account executives, not a 1099 referral network
- **Vendor list page** prominently featured (30-100 carriers visible)
- **Multi-location bias** — copy aimed at multi-site enterprises ("manage all your sites with one invoice")

### Disqualifiers

- Sub-agent / 1099 channel of 30+ active agents → likely TSD or Master Agent
- IT helpdesk / break-fix as primary business → not telecom aggregator, may be MSP 501 IT MSP (not ICP)
- IoT / cellular MVNO / eSIM as primary business → EXCLUDE per ICP exclusion list
- Voice-only / SIP-trunking only → EXCLUDE (voice wholesaler)
- Cloud reselling as primary book (>40% revenue) → likely `Cloud + Telecom Hybrid MSP - MSP`

### Anchor companies (10-15, verified 2026)

1. **Granite Telecommunications** — independent (founded 2002). 2024 revenue $1.85B. Hit $1.85B revenue goal late 2024. Scale anchor — exceeds typical band but archetype-clean.
2. **Nitel** — independent. SD-WAN-first aggregator. Acquired Hypercore Networks June 2022.
3. **Lightyear** — newer-generation telecom aggregator with software-led procurement layer; founder-led.
4. **CCS Global Tech** — smaller aggregator; verify before high-conviction tier.
5. **Comm One** — smaller aggregator; verify.
6. **Onvoy / Sinch (US wholesale)** — borderline (voice-heavy); may EXCLUDE.
7. **TeleQuality Communications** — healthcare-focused aggregator.
8. **Expereo** — international (Netherlands HQ); global enterprise WAN aggregator. Tim Z territory.
9. **Wavenet** (UK) — UK enterprise aggregator. Tim Z territory.
10. **Lumen Channel program** (Lumen's resold channel — NOT Lumen itself; this would be a vendor relationship, not an anchor company entry).

**Anchor count: ~6-9 verified US independents + 2 EMEA. Mid-density anchor segment.**

### Confusable-with comparison

| Compared sub-segment | Boundary test |
|---|---|
| `TSD Technology Services Distributor - MSP` | If company has a sub-agent / 1099 channel of 50+ active agents AND a quoting platform / line card focus → it's a TSD, not a Telecom Aggregator. Telecom Aggregator owns customer relationships directly. |
| `Master Agent - MSP` | Master Agents also have sub-agent networks (smaller than TSDs). If no sub-agent network → Telecom Aggregator. |
| `Managed Network Services - MSP` | If >70% revenue from managed services contracts (not commission resell of carrier products) → MNS. Telecom Aggregator's primary revenue is the resold carrier product, with managed services as value-add. |
| `Cloud + Telecom Hybrid MSP - MSP` | If >30% revenue from cloud reselling (AWS / Azure / GCP licensing or migration services) → Cloud + Telecom Hybrid. Telecom Aggregator is connectivity-primary. |

### Selling angle

Telecom Aggregators sell carrier connectivity products on margin. They wear the SLA but are blind to carrier-internal performance. Tier 1 carriers are increasingly going direct to their enterprise customers with faster provisioning timelines, and that's their #1 competitive pain.

**Lead angle:** "You're responsible for the SLA but can't see inside the carrier network. When something breaks you're stuck between your customer and the carrier with no path-level data. MaiaEdge gives you hop-by-hop telemetry across every carrier on your line card — visibility you can monetize and provisioning you control."

**Secondary angle (Tier 1 bypass):** Tier 1s provision in days; you quote weeks because you depend on carrier timelines. MaiaEdge lets you match Tier 1 speed without buying infrastructure.

**Cloud on-ramp angle:** Their customers are stitching VPCs in CloudShell. Position MaiaEdge as a cross-cloud private fabric they can wrap on top of their carrier resell.

### HubSpot fields R1/R2 must populate

- `customer_segment` = `MSP/Aggregator`
- `company_sub_segment` = `Telecom Aggregator - MSP`
- `segmentation_confidence` per the sub-segment confidence rubric (anchor-pattern match + ≥2 quantitative markers + explicit company self-positioning = `high_90`)
- `account_tier` per `compute_tier` spec (Tier 1 = highest priority; Granite-scale anchors typically Tier 1 or Tier 2)
- `recent_news_or_trigger_event` populated by R1/Signal Scan (M-A2 carrier dropped, M-A3 new carrier added, M-A4 AI Practice launch, M-A5 exec hire)
- `account_brief` regenerated on every R2 full pass per 2026-05-03 freshness mechanism
- `last_enriched_date` stamped on R1 LIKELY_ICP full enrichment + gate pass per unified stamping policy
- `hubspot_owner_id` per HQ state mapping (Tim Lieto East / Ken Cunningham West / Tim Ziemer International)

### Signal source coverage

Per `context/signals/msp-aggregator-signals.md`:
- **Tier A:** M-A1 (PE acquisition / roll-up), M-A2 (carrier dropped from line card), M-A3 (new carrier added), M-A5 (CRO / VP Solutions Engineering / VP Product hires)
- **Tier B:** M-B1 (layoffs), M-B5 (enterprise customer win)
- **Tier C:** M-C1 (Channel Partners Expo speaking slot), M-C4 (vertical expansion announcement)

Primary scrape sources: Channel Futures M&A tag, ChannelE2E, individual aggregator press pages, StockTitan for any public-company filings.

### Contact personas (multi-threaded outreach)

| Tier | Title patterns | Pain frame |
|---|---|---|
| **Primary (Economic Buyer)** | CRO, VP Sales, Founder/CEO | Tier 1 bypass + deal-loss to "depends on the carrier" |
| **Technical Champion** | VP Network Operations, VP Service Delivery, Director of Operations | SLA visibility, finger-pointing, MTTR |
| **Business Sponsor** | COO, President | Margin compression + asset-light positioning preservation |
| **Procurement (later)** | CFO, VP Finance | OpEx model, scaling with business |

Multi-threaded sequence: open with CRO (revenue angle), thread VP Operations (visibility angle), close-thread with COO (board-level competitive narrative).

### Confidence scoring rules

- **`high_90`:** Granite / Nitel / Lightyear archetype match AND explicit "multi-carrier" / "single invoice" positioning on website AND ≥2 quantitative markers (revenue band + W-2 dominant sales structure + 30+ carrier line card)
- **`medium_7089`:** 2 of 3 above
- **`low_5069`:** 1 of 3 OR ambiguous between Telecom Aggregator and TSD (e.g., company has a quoting platform but unclear sub-agent count)
- **`manual_review_required`:** Sub-agent count unclear OR cloud-reselling share unclear OR boundary case with MNS

### Industry sources

- Channel Futures aggregator coverage (`channelfutures.com`)
- ChannelE2E individual press
- Lightyear blog ("Telecom Agents: The Good, The Bad, and The Ugly")
- Individual aggregator press pages

---

## 2. `Managed Network Services - MSP`

### Definition

MSPs / integrators / VARs whose primary offering is **managed network services** (operating the customer's network as a managed service) rather than reselling carrier products on commission. Includes SD-WAN management, NOC services, firewall-as-a-service, SASE management, managed Wi-Fi, network performance management. Vendor-neutral OR vendor-specific (Cisco Gold/Platinum Partner, Fortinet Expert, Palo Alto NextWave).

**Architectural note:** HubSpot enum value is `Managed Network Services - MSP` per live verification 2026-05-14 (post-Phase-1.7c.1 rename; legacy `- Network Operator` suffix archived). File 05 references the old suffix; this document treats `- MSP` as canonical.

### Quantitative markers

- **Revenue:** $50M – $10B (widened from file 05's prior $50M-$1B because Presidio at $5B+, Logicalis $1.7B, Hughes $1.5B managed network book all exceed the original upper bound)
- **Revenue mix:** ≥70% from managed services contracts; not commission resell
- **Customer base:** mid-market and enterprise; multi-site is the sweet spot
- **Vendor concentration:** Cisco-heavy (Cisco Partner Summit Managed Services Partner of the Year is a strong tell), Fortinet, Palo Alto, HPE Aruba, Juniper, VMware/Broadcom
- **Headcount:** 200-15,000 employees
- **Gartner MQ:** appearance in Gartner Magic Quadrant for Managed Network Services as Leader / Challenger / Visionary / Niche Player

### Required signals

- **Marketing language:** "managed network services," "NOC," "SD-WAN managed," "managed SASE," "network operations as a service" — NOT "agent network" or "commission" or "line card"
- **Service catalog page** explicitly listing managed network services SKUs (MSL contracts, NOC tier definitions)
- **Vendor certifications** (Cisco Master, Fortinet Expert, HPE Platinum, Palo Alto Diamond) prominently displayed
- **Case studies** referencing NOC operations and SLA management at customer sites
- **Gartner MQ inclusion** (high-confidence tell — Hughes is 3-time Leader in Gartner MQ MNS, XTIUM 2026 Leader)

### Disqualifiers

- Primary revenue from commission resell → Telecom Aggregator
- Primary revenue from cloud reselling (>30%) → Cloud + Telecom Hybrid MSP
- Has agent/sub-agent network of 50+ active agents → TSD or Master Agent
- IT helpdesk / break-fix as primary motion → not network MNS; out of MaiaEdge ICP
- Cybersecurity-only (MDR / SOC) without network angle → out of MaiaEdge ICP

### Anchor companies (10-15, verified 2026)

1. **Hughes Network Systems** — subsidiary of EchoStar Corporation. ~$1.5B managed network book. **Gartner MQ Managed Network Services Leader 2026 (3rd consecutive year).** Pending EchoStar-DISH merger creates parent uncertainty.
2. **Logicalis** — owned by Datatec Limited (JSE-listed, $4.6B parent revenue). **Logicalis annualized revenues $1.7B globally.** Cisco Managed Services Partner of the Year for the Americas 2025.
3. **Presidio** — owned by BC Partners (since 2019, $2.1B take-private; BC Partners announced sale of Presidio April 2024 — verify current ownership). ~$5B+ revenue.
4. **Open Systems** — independent (Swiss SASE/MDR specialist).
5. **XTIUM** — **Gartner MQ MNS Leader 2026.**
6. **GTT Communications** — post-2021 infrastructure divestiture; today primarily managed services / SD-WAN. Boundary case (the brand is reduced; some legacy carrier-resell associations remain).
7. **CDW** — CRN SP500. Massive managed network practice. **Boundary case with Cloud + Telecom Hybrid MSP** post-Mission Cloud acquisition Dec 2024.
8. **Insight Enterprises** — ~$11B revenue. **Boundary case with Cloud + Telecom Hybrid MSP** post-SADA acquisition Dec 2023.
9. **WWT (World Wide Technology)** — ~$20B revenue, $500M AI lab investment. **Boundary case with Cloud + Telecom Hybrid MSP.**
10. **ePlus** — ~$2.2B revenue. CRN SP500 14th consecutive year.
11. **Optiv** — security-led MNS with network practice.
12. **Trustwave** — security-led MNS.
13. **NTT Data Services** — managed network services arm of NTT.
14. **Ensono** — top-5 Channel Futures MSP 501 2025. Hybrid IT + managed services.
15. **Expedient** — top-5 Channel Futures MSP 501 2025.

### Confusable-with comparison

| Compared sub-segment | Boundary test |
|---|---|
| `Cloud + Telecom Hybrid MSP - MSP` | If company has explicit AWS Premier OR Azure Expert OR Google Cloud Premier status AND >30% cloud reselling revenue → Cloud+Telecom Hybrid. Sub-30% cloud → Managed Network Services. CDW, Insight, WWT are the canonical boundary cases. |
| `Telecom Aggregator - MSP` | Revenue mix test. ≥70% managed services contracts → MNS. ≥70% carrier connectivity resell → Telecom Aggregator. |
| `TSD Technology Services Distributor - MSP` | Sub-agent count test. 50+ active sub-agents → TSD. Direct delivery model → MNS. |

### Selling angle

MNS providers run their customers' networks day-to-day. They monetize on managed service contracts (MSL fees, NOC tier subscriptions, change management billings). They live the SLA and have the operational pain that Telecom Aggregators have, plus they're accountable to a more sophisticated customer base.

**Lead angle:** Position MaiaEdge as fabric they can operate on top of multi-carrier underlay. "Give your customers a NaaS-like experience without building a NaaS — we're the fabric you manage for them." This frames MaiaEdge as a product they monetize, not infrastructure they buy.

**Secondary angle:** Cisco-heavy MNS partners are increasingly squeezed by Cisco-direct managed offerings (Cisco+ Hybrid Cloud, ThousandEyes). MaiaEdge gives them differentiated multi-vendor fabric they can sell.

**Boundary case (CDW/Insight/WWT):** Lead with their cloud+network bundle. "Your customers buy AWS AND network from you. Give them the private cross-cloud path that goes with both."

### HubSpot fields R1/R2 must populate

Same as Telecom Aggregator above. `account_tier` typically Tier 1-2 for >$1B revenue companies (Logicalis, Presidio, Hughes, CDW, Insight, WWT, ePlus); Tier 3 for sub-$200M MNS specialists (Open Systems, XTIUM).

### Signal source coverage

Per `context/signals/msp-aggregator-signals.md`:
- **Tier A:** M-A4 (AI Practice launch — high relevance for MNS; 58/13 AI readiness gap), M-A5 (VP Solutions Engineering / VP Product hire)
- **Tier B:** M-B2 (NaaS / SASE / SD-WAN platform launch), M-B4 (public company earnings — Hughes / EchoStar earnings, CDW earnings)
- **Tier C:** M-C2 (FedRAMP / CMMC / StateRAMP push — high relevance for MNS), M-C4 (vertical expansion)

Gartner MQ MNS publication (annual) is a high-conviction signal.

### Contact personas (multi-threaded outreach)

| Tier | Title patterns | Pain frame |
|---|---|---|
| **Primary (Economic Buyer)** | CTO, CIO, VP Network Services, VP Managed Services | Service catalog modernization, AI readiness, cloud-network convergence |
| **Technical Champion** | VP Network Operations, Director Service Delivery, Chief Network Architect | NOC efficiency, automation, cross-vendor visibility |
| **Business Sponsor** | CRO, CMO (for new service-line GTM) | New revenue streams, differentiation vs Cisco-direct |
| **Procurement** | VP Procurement, CFO (for large integrators) | Margin economics on the managed service layer |

### Confidence scoring rules

- **`high_90`:** Hughes / Logicalis / Presidio / XTIUM archetype match (clear MNS positioning, Gartner MQ inclusion, ≥70% managed services revenue, vendor certifications visible) AND ≥2 quantitative markers
- **`medium_7089`:** 2 of 3 above, OR boundary case with Cloud + Telecom Hybrid MSP where cloud mix is unclear
- **`low_5069`:** 1 of 3, OR IT integrator (CDW/Insight/WWT/ePlus) where the network practice is not explicitly disclosed in primary marketing
- **`manual_review_required`:** Scale ambiguity at >$10B revenue with broad IT distribution (CDW, Insight, ePlus, WWT) AND unclear cloud-vs-network revenue split → flag for human review against Cloud + Telecom Hybrid MSP boundary

### Industry sources

- **Gartner Magic Quadrant for Managed Network Services** (annual, paywalled but headlines via search)
- **Network Infrastructure Magazine Top 10 MNS Companies**
- **CRN Solution Provider 500** (annual)
- **Channel Futures MSP 501**
- **Cisco Partner Summit awards** (Managed Services Partner of the Year is a strong tell)
- Public 10-K filings (Insight INSI, CDW CDW, ePlus PLUS, EchoStar SATS)

---

## 3. `TSD Technology Services Distributor - MSP`

### Definition

Distribution-tier organizations with **sub-agent / 1099 channel models**. They aggregate carrier contracts and resell through a large network of sub-agents ("Technology Advisors" or "TAs" in industry parlance, formerly "agents"). The TSD owns the master supplier agreement with carriers; sub-agents own the customer relationship and earn residual commissions. Quote desks, support functions, partner enablement, AI/security/cloud practice arms, and back-office operations are centralized at the TSD. Sub-agents sell.

**Industry rebranding completed 2020-2023:** "Master agents" → "TSDs"; "agents" → "Technology Advisors." Using "agent" instead of "Technology Advisor" signals an outsider behind the curve.

### Quantitative markers

- **Gross billings ≥$1B** (TSDs measured by gross billings — total carrier revenue flowing through their contracts; net commission revenue typically 3-5% of GB). Lower bound calibrated to Bridgepointe ($755M GB in CY2024 — at the floor; promoted to TSD-tier post-2026 recapitalization).
- **Active sub-agents:** 200-15,000 (AppDirect 10K advisors with 1,000+ providers; Bridgepointe 400+ IT Strategists; Telarus thousands)
- **Vendor portfolio:** 100-1,000+ carriers/providers across data, voice/UCaaS, cloud, security, CX, IoT
- **US national footprint** with some Canada / EU expansion (AppDirect / ScanSource have meaningful international)
- **Practice arms:** AI Practice / Cybersecurity Practice / Cloud Practice / CX Practice
- **Platform layer:** quoting platform (Telarus GeoQuote, AVANT Pathfinder, Bridgepointe "The Signal," AppDirect platform), partner portal, deal registration
- **Employee headcount:** 200-2,000

### Required signals

- **Sub-agent network publicly named** — TSD websites have public "find a partner" or "become a partner" pages
- **Master supplier agreement language** in carrier press releases when TSD adds a new supplier
- **Quote-desk and pre-sales engineering** functions prominently staffed
- **Practice-arm launches** (AI Practice, Cybersecurity Practice — high-conviction Tier A signal M-A4)
- **Partner Summit / annual conference** (Telarus Partner Summit, AVANT Special Forces, Bridgepointe Tech Summit, Sandler Partners National Summit)
- **PE ownership common** (Telarus = Court Square Capital; AVANT = Pamlico/Court Square; AppDirect = CDPQ-backed; Upstack = Berkshire Partners; Bridgepointe = Charlesbank + Carlyle AlpInvest April 2026; ScanSource Intelisys = public NASDAQ:SCSC; Sandler = independent; TD SYNNEX = public NYSE:SNX)

### Disqualifiers

- Gross billings <$500M AND <50 sub-agents → likely `Master Agent - MSP`
- Direct enterprise sales without sub-agent layer → `Telecom Aggregator - MSP`
- Vendor-specific (single OEM, e.g., Cisco-only) → `Managed Network Services - MSP`
- IoT / cellular MVNO platform business → EXCLUDE per ICP exclusion list
- IT distribution primary (Ingram Micro, Synnex hardware) without telecom-specific agent business → out of scope (TD SYNNEX is in scope only because of the Intelisys-adjacent telecom agency motion)

### Anchor companies (verified 2026 via Omdia + public filings + 2026 M&A activity)

1. **Telarus** — independent, PE-backed (Court Square Capital). **CY2024 gross billings $2.9B (+11% YoY).** GeoQuote + Telarus Hub platform. Acquisitions through 2024: TCG (2022), Chorus (2021), CarrierSales (2021), TBI (2021), Americomm (2023).
2. **ScanSource Intelisys** — subsidiary of ScanSource (NASDAQ:SCSC). **CY2024 gross billings $2.7B (+4.5% YoY).** ScanSource FY25 $3.04B total; recurring revenue mix shifted 29.3% → 36.0% Q3 FY25 (publicly disclosed).
3. **AVANT Communications** — independent, Pamlico Capital-backed (Dec 2025 Court Square recapitalization). **CY2024 gross billings $2.1B (+19.5% YoY).** Pathfinder decision platform. Acquired PlanetOne May 2022, CX Effect 2024.
4. **AppDirect** — CDPQ-backed. **CY2024 gross billings $2.0B (+12.0% YoY).** 10K advisors, 1,000+ providers. M&A: WTG (2018), MicroCorp (Dec 2020), Telegration (earlier), CNSG (earlier), NXTSYS (2025-26), vCom Solutions (2025-26), Tackle.io, PartnerStack. AppSmart brand retired 2022.
5. **Bridgepointe** — Charlesbank + Carlyle AlpInvest April 2026 ($1B+ valuation). **CY2024 gross billings $755M (+32% YoY).** 400+ IT Strategists. "The Signal" portal. Scott Kinka positioning.
6. **Sandler Partners** — independent (deliberately so per Channel Dive profile). **2024 net commission revenue ~$209M (+24% YoY).** Top 6 TSD per Omdia.
7. **Upstack** — Berkshire Partners-backed. 36 acquisitions through 2025. Acquired Intelisys / RingCentral leading partners.
8. **TD SYNNEX** (NYSE:SNX) — connectivity is secondary to IT hardware motion. Boundary case.

**Anchor count: 8 confirmed top-tier TSDs in 2026 (Omdia's "top 6" + Upstack + TD SYNNEX).**

### Confusable-with comparison

| Compared sub-segment | Boundary test |
|---|---|
| `Master Agent - MSP` | Gross billings $1B threshold + 100+ active sub-agents = TSD. Below both = Master Agent. Bridgepointe at $755M / 400+ sub-agents passes the sub-agent threshold and was elevated to TSD-tier with the April 2026 recap. |
| `Telecom Aggregator - MSP` | Sub-agent network presence. Yes = TSD/Master Agent. No = Telecom Aggregator (Granite, Nitel). |
| `Managed Network Services - MSP` | Revenue model. Commission resell through sub-agents = TSD. Managed services contracts = MNS. |

### Selling angle

TSDs earn on volume across hundreds of sub-agents and differentiate on portfolio breadth, platform speed, AI/security/cloud practice depth, and quote-desk responsiveness. They're under structural pressure from carrier direct sales and hyperscaler interconnect bypass (Azure ExpressRoute 400G in 2026, AWS Direct Connect, Google Cloud Interconnect).

**Lead angle (line-card add):** "Add private cloud connectivity to your line card without operating it. Your sub-agents earn on the sale; you earn on the spread. Audio Codes Live Platform pattern: provisioning weeks → hours, OpEx down 30%."

**Secondary angle (AI Practice gap):** 58% of buyers want AI, 13% of TAs feel prepared. Your AI Practice needs a network layer story. MaiaEdge is the multi-operator fabric your AI Practice can white-label.

**Tertiary angle (replatforming window):** When a TSD is hiring for supplier strategy, platform engineering, developer experience, or VP Platform roles (signal M-A6), the connector-building window is open. "Replatforming windows are connector-building windows. MaiaEdge slots in as an OpEx platform you white-label during the rebuild rather than bolt on post-launch."

### HubSpot fields R1/R2 must populate

Same as Telecom Aggregator. `account_tier` typically Tier 1 for top-8 TSDs (Telarus, Intelisys, AVANT, AppDirect, Bridgepointe, Sandler, Upstack, TD SYNNEX).

### Signal source coverage

Per `context/signals/msp-aggregator-signals.md` — TSDs are THE highest-signal-density sub-segment in MSP/Aggregator:
- **Tier A:** M-A1 (PE acquisition / roll-up — Telarus, AppDirect, Bridgepointe, Upstack all actively rolling up), M-A2 (carrier dropped from line card), M-A3 (new carrier added), M-A4 (AI Practice launch), M-A5 (CRO / VP SE / VP Product / VP AI Practice hire), M-A6 (platform replatforming job-post signal), M-A7 (ScanSource / TD SYNNEX earnings recurring-revenue disclosure)
- **Tier B:** M-B1 (layoffs), M-B2 (NaaS / SASE platform launch by TSD), M-B3 (new marketplace / quote-engine launch), M-B4 (public earnings disclosures)
- **Tier C:** M-C1 (Channel Partners Expo speaking slots — Scott Kinka, Drew Lydecker, Adam Edwards, Patrick Oborn)

Primary scrape sources: Omdia TSD Market Report (annual), Channel Futures TSD coverage, ChannelE2E, individual TSD press pages (Telarus, AppDirect, AVANT, Bridgepointe, Sandler, ScanSource investor pages, Upstack), StockTitan for SCSC + SNX 8-Ks.

### Contact personas (multi-threaded outreach — TSDs are line-card entry plays)

| Tier | Title patterns | Pain frame |
|---|---|---|
| **Primary (Line-Card Gatekeeper)** | VP Carrier Services, VP Supplier Strategy, VP Platform, Head of AI Practice, VP Solutions Engineering | Vendor portfolio breadth, differentiation, AI Practice gap |
| **Economic Buyer** | CRO, Chief Strategy Officer | Margin compression, hyperscaler bypass, growth narrative |
| **Technical Champion** | Director Sub-Agent Enablement, Director Channel Operations, Head of Pre-Sales Engineering | Quote-desk speed, partner enablement, technical sell-through |
| **Founder/CEO** | Founder/CEO (for owner-led TSDs) | Strategic positioning, exit narrative, board-level competitive |

**Entry motion:** TSD master supplier agreement is the path. Line-card onboarding, not direct-to-TA bypass. TAs work off TSD-gated approved-vendor lists. **Target VP Supplier Strategy / VP Platform first; CRO second.**

### Confidence scoring rules

- **`high_90`:** Omdia top-6 named anchor OR clear archetype match (sub-agent network 200+, gross billings $1B+, master supplier agreement language, quoting platform, practice arms)
- **`medium_7089`:** Boundary case (Bridgepointe-style emerging TSD; ~$500M-$1B GB; 100-300 sub-agents)
- **`low_5069`:** Sub-agent count unclear OR boundary with Master Agent (50-99 sub-agents)
- **`manual_review_required`:** Recent acquisition activity (post-deal integration uncertainty); brand-name overlap with acquired companies (e.g., AppDirect contains former AppSmart contains former WTG/MicroCorp/Telegration brands)

### Industry sources

- **Omdia TSD Market Report (annual)** — authoritative source for ranking + gross billings
- **Channel Futures TSD coverage**
- **ChannelE2E**
- **Channel Playbook** (Scott Kinka editorial)
- **Channel Dive**
- **SEC EDGAR + StockTitan** for ScanSource (SCSC), TD SYNNEX (SNX) 10-Q transcripts
- Telarus / AVANT / AppDirect / Bridgepointe / Sandler / Upstack press pages
- **Channel Partners Conference & Expo** speaker agenda (annual)

---

## 4. `Master Agent - MSP`

### Definition

Smaller, often regional or vertically-focused master agencies with sub-agent networks. The "boutique cousin" of TSDs — same business model (aggregate carrier contracts, resell through sub-agents) but at a fraction of the scale. Often regional (3-20 states) or vertically-focused (healthcare-only, hospitality-only, multifamily-only, government-only).

**Critical caveat — post-consolidation reality (2018-2024):** Almost the entire 2018-2024 master agent landscape has been rolled up. Independent surviving master agents are structurally thin.

### The consolidation map (verified 2026)

| Master Agent | Acquired by | Year |
|---|---|---|
| World Telecom Group (WTG) | AppDirect (became AppSmart) | 2018 |
| CNSG | AppDirect / AppSmart | earlier |
| Telegration | AppDirect / AppSmart | earlier |
| MicroCorp | AppDirect / AppSmart | Dec 2020 |
| PlanetOne | AVANT Communications | May 2022 |
| TBI | Telarus | 2021 |
| CarrierSales | Telarus | 2021 |
| Chorus Communications | Telarus | 2021 |
| Telecom Consulting Group (TCG) | Telarus | 2022 |
| TelAdvocate Communications | Telarus | 2022 |
| Americomm | Telarus | 2023 |
| Global Systems Telecom | TCG (now Telarus) | earlier |
| Clover Communications | Bridgepointe | earlier |
| Hypercore Networks | Nitel | June 2022 |
| CX Effect (specialty TSD) | AVANT | 2024 |

### Quantitative markers (revised post-consolidation)

- **Net commission revenue:** $5M-$100M (lowered from file 05's prior $20M-$200M per validation)
- **Active sub-agents:** 10-50
- **Vendor portfolio:** 20-80 carriers (smaller than TSD's 100-300)
- **Footprint:** Regional 3-20 states OR vertical specialty (healthcare, hospitality, multifamily, government)
- **Ownership:** Often privately held, founder-led, PE-rollup target
- **Headcount:** 20-150 employees

### Required signals

- Sub-agent network publicly named on website (smaller "find an agent" page or partner list)
- Vertical or regional specialty in marketing copy
- Founder/CEO often features prominently in industry press
- Annual partner summit (smaller scale than TSD summits)
- PE-rollup target signaling (founder approaching exit age, capital structure simple)

### Disqualifiers

- Gross billings $1B+ AND 100+ active sub-agents → TSD (Bridgepointe was here, now elevated)
- Sub-agent count >200 → TSD
- No sub-agent network → Telecom Aggregator
- Voice / IoT / SMS-only focus → EXCLUDE per ICP exclusion list

### Anchor companies — surviving independents (2025-26 verification effort)

**This is the hardest sub-segment to populate.** Below is the result of the 2026-05-14 surfacing effort:

| # | Company | Status (verified 2026-05-14) | Confidence |
|---|---|---|---|
| 1 | **X4 Solutions** | Independent (founded 2004; cloud services master agency, 35+ carrier partnerships, supports independent business owners). Confirmed independent per their LinkedIn + own website 2025. | HIGH |
| 2 | **Tech Superpowers** | Status uncertain — not surfaced as a master agent in 2026 search; likely an IT MSP, not telecom master agent. **EXCLUDE pending validation.** | EXCLUDE |
| 3 | **CyberNet Communications** | Independent, smaller regional master agent. Public partner program page references multiple carriers. Verify scale. | MEDIUM |
| 4 | **ACS** (acscp.com — "Master Agent Telecom") | Surfaces as a master agent in search. Verify scale + current independence. | LOW-MEDIUM |
| 5 | **Clarusco / Houston Technology Partners** | Regional Houston-area master agent program; partner-program page suggests sub-agent model. Verify scale. | LOW-MEDIUM |
| 6 | **Verizon Partner Program** (master agent / distributor program) | Not a master agent itself — this is Verizon's vendor program FOR master agents. EXCLUDE as anchor. | EXCLUDE |
| 7 | **CCS Global Tech** (also listed under Telecom Aggregator candidates) | Could fit either sub-segment. Verify sub-agent count. | LOW |
| 8 | **TeleQuality Communications** (healthcare-vertical) | Could fit Telecom Aggregator OR Master Agent depending on whether it has a sub-agent layer. Verify. | LOW |

**Anchor count: 1-2 verified independent master agents (X4 Solutions HIGH; CyberNet Communications MEDIUM). Other 5-6 candidates require primary-source validation before promotion.**

### Policy recommendation — default `manual_review_required`

Given the post-consolidation thin landscape, **`Master Agent - MSP` defaults to `segmentation_confidence = manual_review_required`** in the classifier unless ALL of the following are validated by primary source within the last 12 months:

1. Company is independent (not acquired)
2. Company has 10+ active sub-agents publicly disclosed
3. Net commission revenue in the $5M-$100M band
4. Vendor portfolio of 20+ carriers
5. Regional or vertical specialty explicitly positioned

If any of (1)-(5) fail validation, classifier writes `Master Agent - MSP` with `segmentation_confidence = manual_review_required` and RevOps reviews. This protects against false-positive classifications where the company has been acquired but the brand is still active (e.g., AppSmart is technically still a brand of AppDirect, but classifying any AppSmart sub-brand as Master Agent is wrong — it's part of AppDirect TSD).

### Confusable-with comparison

| Compared sub-segment | Boundary test |
|---|---|
| `TSD Technology Services Distributor - MSP` | Gross billings $1B threshold + 100+ sub-agents = TSD. Below both = Master Agent. |
| `Telecom Aggregator - MSP` | Sub-agent network presence. Yes (even at small scale) = Master Agent. No = Telecom Aggregator. |

### Selling angle

Master Agents differentiate from TSDs on niche or vertical expertise. A private cloud fabric on their line card is a "premium add" their sub-agents can offer to enterprise customers when TSDs are all selling the same carrier products.

**Lead angle:** "Premium product your sub-agents can sell to land bigger deals and stay relevant against the TSD giants. Differentiation when everyone is selling the same Telarus / Intelisys / AVANT line card."

**Secondary angle (vertical specialty):** Healthcare / hospitality / multifamily verticals have specific compliance + SLA requirements (HIPAA, PCI, multi-tenant building wiring). Position MaiaEdge as vertical-fit fabric.

**Tertiary angle (exit value):** Master Agents that are PE-rollup targets benefit from a more sophisticated technology line-card story at exit. MaiaEdge contributes to that.

### HubSpot fields R1/R2 must populate

Same as Telecom Aggregator. `account_tier` typically Tier 3-4 (smaller scale than TSDs). `segmentation_confidence` typically `manual_review_required` per policy above.

### Signal source coverage

Per `context/signals/msp-aggregator-signals.md`:
- **Tier A:** M-A1 (PE acquisition / roll-up — HIGH relevance, these are typically the targets), M-A3 (new carrier added — small-scale Master Agents add carriers more rarely; high-signal when they do), M-A5 (CRO / VP hires — small companies, easier to track via LinkedIn)
- **Tier B:** M-B1 (layoffs — less common at small scale), M-B5 (enterprise customer win — major signal for boutique master agents)
- **Tier C:** M-C4 (vertical announcement — high relevance for vertical-specialty master agents)

Primary scrape sources: Channel Futures Top 100 Agents/Master Agents list (legacy series), ChannelE2E master agent news, LinkedIn for founder/CEO posts.

### Contact personas (multi-threaded outreach — smaller orgs, founder-led)

| Tier | Title patterns | Pain frame |
|---|---|---|
| **Primary (Founder/Decision Maker)** | Founder, CEO, President, Managing Partner | Differentiation, exit value, line-card sophistication |
| **Technical Champion** | Director Sub-Agent Enablement, VP Operations, Head of Carrier Relations | Operational simplification, multi-carrier visibility |
| **Business Sponsor** | CRO / Head of Sales | Sub-agent productivity, deal size increase |

**Outreach reality:** Smaller orgs mean fewer titles to thread. Often single-decision-maker plays. CEO/Founder direct is usually the right entry.

### Confidence scoring rules

- **`high_90`:** Reserved — requires (1) independence verified within last 12 months, (2) 10+ active sub-agents publicly named, (3) revenue band fit, (4) carrier portfolio visible, (5) regional/vertical positioning explicit. X4 Solutions meets the bar in 2026; almost no other candidate does.
- **`medium_7089`:** 3-4 of the 5 validation criteria above
- **`low_5069`:** 2 of 5 validation criteria
- **`manual_review_required`:** DEFAULT for this sub-segment per policy above

### Industry sources

- **Channel Futures Top 100 Agents/Master Agents list** (when published)
- **ChannelE2E master agent news**
- **Channel Playbook editorial** (Scott Kinka — covers boutique master agents)
- **selltelcobiz.com Channel M&A News** (acquisition tracker)
- Direct LinkedIn pull on founder/CEO of suspected master agents
- **Channel Partners Expo speaker agenda** (smaller breakouts often feature boutique master agents)

---

## 5. `Cloud + Telecom Hybrid MSP - MSP`

### Definition

MSPs whose business spans **cloud reselling AND telecom managed services**. Distinct from pure cloud MSPs (which are an EXCLUDED ICP — they don't have the network angle). Hybrid MSPs sell AWS / Azure / GCP licensing or migration services AND network services (SD-WAN, dedicated circuits, managed firewalls, SASE). The defining test is **both** cloud AND network practices visible in primary marketing.

### Quantitative markers

- **Revenue:** $30M – $30B+ (widened from file 05's prior $50M-$1B because IT integrators like AHEAD at $3B+, Insight at $11B+, CDW at $22B, WWT at $20B all fit the archetype post-cloud-acquisition)
- **Revenue mix:** 30-60% cloud (licensing, migration, managed cloud, AWS Marketplace transactions) + 30-60% network services (SD-WAN, managed circuits, security)
- **Cloud partner status:** AWS Premier Tier Services Partner OR Azure Expert MSP OR Google Cloud Premier Partner (high-conviction signal)
- **Customer segments:** mid-market and enterprise; sometimes upper-SMB via cloud channel
- **Employee headcount:** 200-15,000
- **Acquisition activity:** segment is in active consolidation; track 12-month M&A history

### Required signals

- **Explicit cloud + network positioning** on website primary marketing — both visible, not just one
- **AWS / Azure / GCP partner badge** (Premier / Expert / Premier tier)
- **Cloud Marketplace listings** (AWS Marketplace, Azure Marketplace transactions)
- **Network services SKUs** (SD-WAN managed, managed Direct Connect, managed ExpressRoute, SASE)
- **Recent acquisition** — extremely common in this segment (CDW + Mission Cloud Dec 2024; Insight + SADA Dec 2023; AHEAD + Computer Design & Integration Feb 2024)
- **Hybrid case studies** showing cross-product wins (customer bought cloud + network from same MSP)

### Disqualifiers

- Cloud-only with no network services → EXCLUDE (pure cloud MSP, not ICP)
- Network-only without cloud reselling → `Managed Network Services - MSP` or `Telecom Aggregator - MSP`
- Sub-$15M revenue → too small; likely a sub-vertical specialist
- IoT / SaaS-platform-only → EXCLUDE per ICP exclusion list

### Anchor companies (10-15, verified 2026)

1. **AHEAD** — independent (~$3B 2024 revenue per ChannelE2E estimate). Reportedly exploring sale 2024-2025. Acquired Computer Design & Integration Feb 2024. Cloud + network + AI practice.
2. **CDW + Mission Cloud (AWS practice)** — CDW ~$22B revenue. Acquired Mission Cloud Dec 2024 ($107M raised by Mission across three tranches; CDW deal price undisclosed). Mission is now "CDW's dedicated AWS practice" per the deal press. CDW MSP 500 Elite 150. Boundary case with `Managed Network Services - MSP`.
3. **Insight Enterprises + SADA (Google Cloud practice)** — Insight ~$11B revenue. Acquired SADA Dec 2023 ($410M). SADA is 6-time Google Cloud Partner of the Year. Now Insight Google Cloud practice (850 SADA professionals into 14,500-team Insight global ops).
4. **WWT (World Wide Technology)** — ~$20B revenue. $500M AI lab investment. AI + cloud + network. **Boundary case with `Managed Network Services - MSP`.**
5. **ePlus** — ~$2.2B revenue. CRN SP500 14th consecutive year. AI / security / cloud / data center / networking / collaboration. Boundary case.
6. **RapidScale** — subsidiary of Cox Business. Cox acquired RapidScale 2018 and Logicworks 2023. **2025 VMware Cloud Foundation as a Service Partner of the Year.** Pending Charter-Cox merger affects RapidScale's structural future.
7. **Effectual Cloud** — independent. AWS Premier Tier Services Partner. Smaller (<$100M est.).
8. **TEKsystems** — AWS Premier Tier Services Partner. Hybrid cloud + network + apps.
9. **TCS (Tata Consultancy Services)** — AWS Premier Tier + AWS MSP. Global scale; may be too far outside MaiaEdge ICP focus (consulting-led).
10. **SoftServe** — AWS Top Ambassador 2025. Hybrid cloud + apps + network.
11. **Trianz** — multi-cloud (AWS + Azure) + network transformation.
12. **SmartShift** — AWS MSP + Azure Cloud Solution Provider Partner.
13. **Logicworks** (now part of Cox / RapidScale post-2023 acquisition) — was a standalone Cloud + Telecom Hybrid until 2023.

### Critical clarification — listing acquired entities

Per Cooper's M&A policy (file 05, lines 46-50), classification is per CURRENT LEGAL STATE. **Mission Cloud and SADA are NO LONGER standalone — they are practices within CDW and Insight respectively.** Anchor list lists them as "CDW + Mission Cloud (AWS practice)" and "Insight Enterprises + SADA (Google Cloud practice)" to make the relationship clear. The HubSpot record on Mission Cloud should be reassociated to CDW (or flagged for review per pre-deletion-audit), and SADA to Insight.

### Confusable-with comparison

| Compared sub-segment | Boundary test |
|---|---|
| `Managed Network Services - MSP` | Cloud-reselling component test. >30% cloud reselling revenue OR clear AWS Premier / Azure Expert / GCP Premier status → Cloud + Telecom Hybrid. Below 30% cloud → MNS. **CDW, Insight, WWT, ePlus are the canonical boundary cases.** |
| Pure cloud MSP | EXCLUSION boundary. Pure cloud MSPs are not ICP. Qualifying signal: meaningful network managed services book visible in primary marketing. |
| `Telecom Aggregator - MSP` | Cloud reselling component test. >30% cloud → Cloud+Telecom Hybrid. <10% cloud → Telecom Aggregator. |
| `TSD Technology Services Distributor - MSP` | Sub-agent network presence. TSDs sell through sub-agents; Cloud+Telecom Hybrid sells directly to enterprise. |

### Selling angle

Cloud + Telecom Hybrid MSPs already sell cloud + network as a bundle. They're the highest-affinity sub-segment for the cross-cloud fabric narrative because the cross-cloud connectivity problem IS their customer's problem.

**Lead angle:** "Your customers buy AWS + Azure from you. Give them the private cross-cloud path without operating it. MaiaEdge is the fabric you wrap into your cloud + telecom service catalog."

**Secondary angle (acquisition-velocity):** Segment is in active consolidation — CDW + Mission, Insight + SADA, AHEAD + CDI, RapidScale + Logicworks. Post-acquisition integration phase is the prime selling window (120-day post-close).

**Tertiary angle (AI inference):** Hybrid MSPs serving AI workloads need deterministic paths to AI clouds. MaiaEdge is the AI-as-a-service connective fabric.

### HubSpot fields R1/R2 must populate

Same as Telecom Aggregator. `account_tier` typically Tier 1 for >$10B IT integrators (CDW, Insight, WWT, ePlus); Tier 2 for mid-market (AHEAD, RapidScale); Tier 3 for sub-$200M cloud-led specialists (Effectual Cloud). `segmentation_confidence` requires post-acquisition state verification.

### Signal source coverage

Per `context/signals/msp-aggregator-signals.md`:
- **Tier A:** M-A1 (PE acquisition / cloud MSP roll-up — HIGH velocity in this sub-segment), M-A4 (AI Practice launch — strong fit), M-A5 (VP Cloud Practice / VP AI hires)
- **Tier B:** M-B2 (NaaS / SASE launch by Hybrid MSP — boundary case for partnership vs competitor frame), M-B4 (public company earnings — CDW, Insight, ePlus, WWT all public-ish)
- **Tier C:** M-C2 (FedRAMP / CMMC — high relevance for hybrid serving regulated industries)

Primary scrape sources: AWS Marketplace partner directory, Azure Expert MSP directory, Google Cloud Partner directory, CRN MSP 500 (Elite 150 tier specifically), Insight / CDW / ePlus / WWT annual reports, AHEAD investor materials, ChannelE2E acquisition coverage.

### Contact personas (multi-threaded outreach)

| Tier | Title patterns | Pain frame |
|---|---|---|
| **Economic Buyer** | CEO, President, COO | Strategic bundle differentiation, exit value, cross-product attach rate |
| **Cloud Practice Lead** | VP Cloud Practice, VP Cloud Solutions, Head of Cloud Services, Head of AWS/Azure/GCP Practice | Cross-cloud customer pain, hyperscaler bypass risk |
| **Network Practice Lead** | VP Connectivity, VP Network Services, VP Managed Services | SD-WAN attach to cloud deals, multi-carrier visibility |
| **Sales** | CRO, VP Enterprise Sales | Deal size, bundle pricing, competitive vs Lumen PCF / Megaport |
| **Technical Champion** | Chief Cloud Architect, CTO, Director Hybrid Cloud | Architectural fit, automation, API integration |

**Multi-threaded sequence:** Open with VP Cloud Practice (customer-cross-cloud-pain), thread VP Connectivity (network-side), close with CEO/President on bundle differentiation.

### Confidence scoring rules

- **`high_90`:** AHEAD / CDW / Insight / WWT / ePlus archetype match (verified cloud partner status + network services in primary marketing + ≥$500M revenue) AND ≥2 quantitative markers
- **`medium_7089`:** 2 of 3 above, OR boundary case where one of cloud or network is rapidly growing post-acquisition (CDW post-Mission, Insight post-SADA)
- **`low_5069`:** 1 of 3, OR cloud-only with hints of network services not yet primary
- **`manual_review_required`:** Recent acquisition activity within last 12 months (per file 05's universal manual-review trigger #2 + sub-segment-specific trigger); brand may not yet reflect post-acquisition product portfolio

### Industry sources

- **AWS Premier Tier Partner directory** (`aws.amazon.com/partners`)
- **Azure Expert MSP directory** (Microsoft Partner Center)
- **Google Cloud Premier Partner directory**
- **CRN MSP 500 Elite 150 tier**
- **CRN Solution Provider 500** (annual)
- **ChannelE2E acquisition coverage**
- **AWS Marketplace** (partner transactions visible)
- Public 10-K filings: CDW (CDW), Insight (INSI), ePlus (PLUS), TD SYNNEX (SNX), WWT (private but discloses revenue)
- AHEAD investor materials (private, exploring sale)

---

# CRITICAL CLARIFICATIONS — REPORT BACK

## 1. Master Agent post-consolidation — independent anchor surfacing

**Verified independent count: 1 HIGH-confidence + 1 MEDIUM-confidence = 2 confirmed independents.**

| # | Name | Confidence |
|---|---|---|
| 1 | **X4 Solutions** | HIGH (35+ carrier partnerships; independent since 2004; supports independent business owners — confirmed via own website + LinkedIn 2025) |
| 2 | **CyberNet Communications** | MEDIUM (public partner program; smaller regional master agent; scale unverified) |

**Candidates requiring primary-source validation before promotion (3-4 names):** ACS (acscp.com), Clarusco / Houston Technology Partners, CCS Global Tech, TeleQuality Communications.

**Could not surface 5-8 verified independents in 2026.** The consolidation of WTG (2018), CNSG, Telegration, MicroCorp (Dec 2020), PlanetOne (May 2022), TBI / CarrierSales / Chorus (2021), TCG (2022), Americomm (2023), Clover, Hypercore, CX Effect (2024) leaves a structurally thin landscape.

**Policy adopted:** `Master Agent - MSP` defaults to `segmentation_confidence = manual_review_required` unless 5 validation criteria met (independence verified within 12 months, 10+ active sub-agents publicly named, $5M-$100M net commission revenue, 20+ carrier portfolio, regional/vertical specialty explicit). Documented in deep-dive Section 4 above.

## 2. TSD anchor list — Omdia 2024 verification

| TSD | File 05 figure | Verified 2026 (Omdia CY2024) | Status |
|---|---|---|---|
| Telarus | $2.9B GB | $2.9B GB (+11% YoY) | CONFIRMED |
| AVANT | $2.1B GB | $2.1B GB (+19.5% YoY) | CONFIRMED |
| Intelisys / ScanSource | $2.7B GB | $2.7B GB (+4.5% YoY) | CONFIRMED |
| AppDirect | (not numbered in file 05) | $2.0B GB (+12.0% YoY) | CONFIRMED |
| Sandler | net commission ~$25M (file 05) | ~$209M revenue (+24% YoY) per Channel Dive 2025 | **REVISED UPWARD** — Sandler is materially larger than file 05 estimate. Recommend updating file 05 |
| Bridgepointe | "Top 6 TSD per Omdia 2024" (file 05) | $755M GB (+32% YoY); recapped April 2026 at $1B+ valuation with Charlesbank + Carlyle AlpInvest | CONFIRMED + RECAP NOTE |

**Omdia total TSD market CY2024: $16.6B gross billings (+14.5% YoY).** Top 6 control 72.3% share (combined +13.4% growth).

**2025 changes:** Bridgepointe April 2026 recap (Charlesbank-led, Carlyle AlpInvest single-asset continuation vehicle, $1B+ valuation) confirms TSD-tier elevation. ScanSource Intelisys recurring revenue mix shift 29.3% → 36.0% Q3 FY25 is a publicly-disclosed leading indicator of bandwidth-resell-to-platform pivot.

## 3. IT integrators (CDW $22B, Insight $11B, ePlus $2.2B, WWT $20B+) classification

**Policy recommendation:** Default to `Cloud + Telecom Hybrid MSP - MSP` IF:
- Company has clearly disclosed AWS Premier / Azure Expert / Google Cloud Premier status
- AND a network services book (SD-WAN, managed circuits, MNS) is visible in primary marketing
- AND >30% cloud reselling revenue (proxy: AWS Marketplace transactions, Azure ESI sales, GCP Premier deal flow)

Default to `Managed Network Services - MSP` IF:
- Cloud component is absent or de minimis (<20% revenue)
- Network managed services is clearly primary

**Confirmed boundary cases (need `manual_review_required` flag):**
- **CDW** (post-Mission Cloud Dec 2024) — likely Cloud + Telecom Hybrid; manual review confirms cloud share now ≥30%
- **Insight Enterprises** (post-SADA Dec 2023) — likely Cloud + Telecom Hybrid; SADA brought 850 cloud professionals
- **WWT** ($500M AI lab) — Cloud + Telecom Hybrid; AI + cloud + network all in primary positioning
- **ePlus** — Cloud + Telecom Hybrid OR MNS depending on cloud-revenue cut; flag for manual review

**Pressure test result:** The boundary IS material. CDW pre-Mission was MNS; CDW post-Mission is Cloud + Telecom Hybrid. Insight pre-SADA was MNS; Insight post-SADA is Cloud + Telecom Hybrid. **Without a clear cloud-revenue threshold, classifier will oscillate.** Recommend 30% cloud-revenue threshold as the bright line.

## 4. Cloud + Telecom Hybrid post-acquisition examples — listing policy

**Recommendation:** List under the acquirer with the practice name in parentheses. Do NOT list the acquired entity as a separate standalone anchor.

| Was | Now | List as |
|---|---|---|
| Mission Cloud Services (independent) | CDW AWS practice | **CDW + Mission Cloud (AWS practice)** |
| SADA Systems (independent) | Insight Google Cloud practice | **Insight Enterprises + SADA (Google Cloud practice)** |
| Logicworks (independent) | Cox / RapidScale | **RapidScale (Cox Business + Logicworks integration)** |
| Computer Design & Integration (independent) | AHEAD subsidiary | **AHEAD** (CDI listed as historical only) |

**Rationale per Cooper's M&A policy (file 05):** Classify per CURRENT LEGAL STATE. The acquired brand may still be in market-facing use (CDW kept the Mission Cloud name for the AWS practice; Insight kept SADA), but the legal entity and revenue is the parent. HubSpot record consolidation is RevOps's manual post-close step.

**Operational note for R1/R2 enrichment:** When R1 picks up a Mission Cloud or SADA HubSpot record, the classifier should:
1. Detect the acquisition (>12 months old → settled state; <12 months → manual_review)
2. Flag the record as a duplicate of the parent (CDW or Insight)
3. Hand off to R3 (Duplicate Accounts) or R4 (Flagged Consolidation) for reassociation
4. Do NOT classify as standalone `Cloud + Telecom Hybrid MSP`

---

# TAXONOMY GAPS IDENTIFIED

1. **`Managed Network Services - MSP` enum suffix mismatch.** File 05 still references `Managed Network Services - Network Operator` (old suffix). HubSpot verification 2026-05-14 confirms the live value is `Managed Network Services - MSP` (post-Phase-1.7c.1 rename). File 05 needs to be updated to reflect the rename; this deep-dive document treats `- MSP` as canonical.

2. **No IoT Connectivity Platform sub-segment exists.** Aeris, EMnify, Wireless Logic, Kore Wireless, 1NCE, Soracom are repeatedly flagged for exclusion across enrichment. If MaiaEdge wants IoT platforms in scope (future strategic decision), a new sub-segment under MSP/Aggregator or NeoCloud would be needed. Today these are categorically excluded.

3. **Bridgepointe needs file 05 update.** File 05 says "smaller — boundary case with Master Agent Sub-Agent" but verified 2026 data shows $755M gross billings + April 2026 $1B+ recap. Bridgepointe is firmly TSD-tier. File 05 already corrected this in the "Anchor companies" line but the boundary-test framing in older sections is stale.

4. **Sandler Partners revenue band needs widening.** File 05 cites "~$25M reported net commission revenue." Verified 2026: ~$209M revenue (+24%). The 8x mismatch suggests file 05 was reading old data or wrong metric. Recommend recalibrating.

5. **Hughes Network Systems' EchoStar-DISH merger pending state.** Hughes is a 3-time Gartner MQ MNS Leader. The pending EchoStar-DISH merger creates parent-level structural uncertainty. Per Cooper's M&A policy, classify per current state (Hughes remains `Managed Network Services - MSP` with note in `recent_news_or_trigger_event`).

6. **GTT Communications dual classification risk.** GTT post-2021 infrastructure divestiture is today primarily managed services / SD-WAN (boundary case for `Managed Network Services - MSP`). File 05's Network Operator section also flags GTT (legacy Pure Wholesale Carrier reference, now replaced by EXA Infrastructure). Classifier needs to know GTT today = MNS, NOT Pure Wholesale Carrier.

7. **X4 Solutions deserves promotion to anchor list** for `Master Agent - MSP` (HIGH confidence based on 2026-05-14 verification). File 05 currently lists X4 as "status unclear."

8. **NaaS Platform Operators sub-classification within MSP/Aggregator.** The current MSP/Aggregator cheatsheet (`context/segments/msp-aggregator.md` lines 279-311) has a "Subtype 1 / Subtype 2" framing where Subtype 2 = NaaS Platform Operator (CBC Tech, Epsilon, PCCW Console Connect, Arelion, Sparkle Sparkhub). **NONE of the 5 active HubSpot sub-segment values clearly captures NaaS Platform Operator.** Console Connect could fit `International Backbone Specialist - Network Op`. CBC Tech, Epsilon could fit `Telecom Aggregator - MSP` or `Cloud + Telecom Hybrid MSP - MSP` depending on cloud-revenue split. Arelion, Sparkle clearly fit `Pure Wholesale Carrier - Network Op`. **Recommendation:** retire the NaaS Platform Operator subtype framing in `msp-aggregator.md` and reclassify each named NaaS operator to its correct HubSpot sub-segment per the disambiguation flowchart in file 05. Document the partnership-vs-competitor caveat (file 05 line 305-308) as a cross-cutting consideration rather than a sub-segment.

9. **TD SYNNEX boundary.** TD SYNNEX (NYSE:SNX) has both IT distribution (out of MaiaEdge ICP) and Intelisys-adjacent telecom agency (`TSD Technology Services Distributor - MSP` candidate). Recommend `manual_review_required` for TD SYNNEX-as-TSD-anchor pending clarification of which division/practice MaiaEdge engages.

---

**Document end.**
