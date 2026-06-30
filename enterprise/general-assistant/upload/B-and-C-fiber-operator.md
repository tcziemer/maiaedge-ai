# Phase 3 — Fiber Operator ICP: Industry Taxonomy Alignment + 6 Sub-Segment Deep Dives

**Scope:** Fiber Operator ICP only — 6 active HubSpot `company_sub_segment` values verified live 2026-05-14.

**HubSpot internal values (case-sensitive — DO NOT change):**

1. `Regional CLEC - Fiber operator`
2. `Long Haul / Backbone - Fiber operator`
3. `Dark Fiber Specialist - Fiber Operator` (capital "O" in Operator — the only Fiber sub-segment that breaks lowercase convention)
4. `Tier 2 National Wholesale - Fiber operator`
5. `Regional Cable Operator - Fiber operator`
6. `Municipal / Cooperative - Fiber operator` (renamed from `Co-op/consortium` 2026-05-13)

**Author:** Phase 3 sub-agent
**Date:** 2026-05-14
**Validation:** 14 web searches against FCC BDC, NTCA, NRECA, Vertical Systems Group, dgtlinfra, NCTA, NTIA BEAD, SEC filings, Light Reading / Telecom Ramblings / Fierce Network, operator press

---

## Industry taxonomy alignment

The Fiber Operator segment has no single canonical taxonomy. Five industry taxonomies are used in combination to classify operators; the MaiaEdge HubSpot model approximates the union, but no single industry source maps cleanly to all 6 sub-segments.

| Taxonomy | Source URL | Structure | MaiaEdge mapping |
|---|---|---|---|
| **FCC Broadband Data Collection (BDC) Technology Codes** | https://www.fcc.gov/general/technology-codes-used-fixed-broadband-deployment-data and https://help.bdc.fcc.gov/hc/en-us/articles/5290793888795-Fixed-Technology-Codes | Operators self-report by **transport technology** (Copper / Cable / Fiber / Licensed Fixed Wireless / Unlicensed Fixed Wireless / Satellite) — NOT by business model. CLEC vs ILEC vs Cable is not directly encoded; instead inferred from "Provider type" + service technology code (50 = fiber-to-the-premises, 40 = cable DOCSIS). | BDC tells us Regional Cable Operator (code 40 dominant + commercial fiber subset) vs Regional CLEC (code 50 dominant). Does NOT help distinguish wholesale (Tier 2 National Wholesale / Long Haul / Dark Fiber Specialist) — none of those file BDC because their customers are carriers, not premises. |
| **USAC / FCC legacy carrier classifications** | https://www.fcc.gov/ and USAC reporting categories | RLEC (Rural LEC, Section 251(f) exempt) / ILEC (Incumbent LEC, post-divestiture Bell + GTE legacy) / CLEC (Competitive LEC, post-1996 Act) | Maps RLEC → Municipal/Cooperative anchor + some Regional CLEC. ILEC → catches small Tier 1 Carrier - Network Op cousins (not in Fiber segment). CLEC → Regional CLEC primary. **Gap:** no native bucket for wholesale-only fiber operators (Zayo, Uniti, FiberLight) — these are not LECs at all. |
| **NTCA + NRECA member directories** | https://www.ntca.org/about-us/our-members and https://www.electric.coop/issues-and-policy/broadband | NTCA = ~850 independent community-based RLECs / cooperatives across 46 states. NRECA = ~900 electric co-ops, ~200 of which have broadband programs. | Both feed Municipal / Cooperative - Fiber operator anchor list. NTCA membership is a **near-binary qualifier** for that sub-segment. |
| **dgtlinfra Top 125 ISPs** | https://dgtlinfra.com/top-internet-providers-us/ | Ranks largest 125 US ISPs into Groups 1-4 by households passed, broadband subs, fiber/HFC route miles, revenue. Group 1 = Comcast/Charter/AT&T scale; Group 4 = small/regional providers. | Group 1-2 = Cable MSO Network Op (NOT in Fiber segment). Group 3 = Regional Cable Operator - Fiber operator + Regional CLEC - Fiber operator. Group 4 + below = Regional CLEC + Municipal/Cooperative. Useful anchor source. |
| **Vertical Systems Group U.S. Carrier Ethernet LEADERBOARD** | https://verticalsystems.com/leaderboards/ | Top 6 by retail port share (>4% market share). Challenge Tier = 1-4% share (Mid-2025: Altice, Cogent, Crown Castle (pre-Zayo close), Frontier, Granite, GTT, Windstream, Zayo). Market Players Tier <1%. | Top 6 = Tier 1 Carrier / Cable MSO (Network Op segment, not Fiber). Challenge Tier = Tier 2 National Wholesale - Fiber operator anchor pool. Useful B2B fiber operator ranking. |
| **NCTA member directory** | https://www.ncta.com/ | National + regional cable operators. | Maps to Regional Cable Operator - Fiber operator (sub-MSO) + Cable MSO Network Op (Comcast/Charter/Cox). |
| **NTIA BEAD subgrant award lists** | https://broadbandusa.ntia.gov/ | State-by-state subgrant awards for last-mile and middle-mile fiber. | High-conviction trigger signal for Municipal/Cooperative + Regional CLEC. BEAD awards in 2025-2026 are a primary anchor source for both. |

**Missing sub-segments revealed by taxonomy review:**

1. **Subsea cable consortia / international landing operators** (Aqua Comms, Seaborn, Bulk Fiber Networks). Not in scope — these belong in `International Backbone Specialist - Network Op` per file 05.
2. **Middle-mile-only / grant-funded anchor-institution operators** (KentuckyWired, Project THOR, MassBroadband 123). Per file 05 and the existing `fiber-operator.md` lines 359-363: **exclusion criteria, not a sub-segment.** Revenue base is IRU + anchor contracts, not on-demand wholesale — structurally incompatible with MaiaEdge SaaS consumption model. Confirmed by 2026 research: Mid-Atlantic Broadband (mbc-va.com) and similar middle-mile-only fit this exclusion.
3. **Tribal broadband consortia** — fold into Municipal/Cooperative.
4. **Greenfield FTTH overbuilders** (Ting Internet, Tachus, MetroNet pre-Oak Hill rollups) — these are Regional CLECs by structure even though "CLEC" terminology is awkward for greenfield-only operators with no ILEC heritage. Allow under Regional CLEC with a "fiber overbuilder" annotation in HubSpot reasoning.

**Reverse-mapping concerns:**

- **Regional CLEC vs Tier 2 National Wholesale** is the most ambiguous boundary. Distinguishing test: **direct-enterprise revenue share**. Regional CLECs sell direct to enterprises in their footprint (>40% of revenue from direct-enterprise). Tier 2 National Wholesale sell to carriers/hyperscalers (>80% from wholesale). The pivot is footprint geography (sub-national vs national) + customer mix (direct enterprise vs wholesale).
- **Long Haul / Backbone vs Tier 2 National Wholesale** — Long Haul is **route-defined** (inter-city long-haul corridors with hundreds-of-miles spans + DWDM optical) while Tier 2 National Wholesale is **service-defined** (metro + long-haul, lit Ethernet + waves + dark fiber). Zayo straddles both; classify Zayo as Tier 2 National Wholesale per file 05 (canonical resolution).
- **Regional Cable Operator vs Regional CLEC** — origin test: HFC/coaxial parent legacy → Regional Cable Operator. Telco/CLEC/fiber-overbuilder origin → Regional CLEC. The customer-facing product may look the same (commercial fiber Ethernet), but the OSS/BSS, billing system, and capex model differ enough to materially change the MaiaEdge selling angle.
- **Dark Fiber Specialist vs Long Haul / Backbone** — both can be primarily dark fiber. Dark Fiber Specialist is **metro/regional dark-strand-as-product** (FiberLight, INDATEL members). Long Haul / Backbone is **inter-city corridor dark fiber + waves** (Lumen, Zayo). Smaller route mile counts (~5,000-30,000) + metro density → Dark Fiber Specialist. Larger (~100,000+) + inter-city → Long Haul.

---

## 1. `Regional CLEC - Fiber operator`

### Definition
Multi-state competitive local exchange carriers and PE-backed regional fiber platforms whose primary business is selling fiber connectivity (lit Ethernet, wavelengths, dark fiber, dedicated internet access) directly to enterprises, mid-market, government, and education in their geographic footprint. Built either via CLEC certification (post-1996 Telecom Act) or as fiber-overbuilders without ILEC heritage. The canonical "fiber-island unification" archetype — most have grown by acquiring smaller regional networks and now operate disconnected fiber segments with different OSS/BSS at each site. Footprint scale: 2,000-30,000 route miles, 3-12 states. Catch-all default sub-segment for the Fiber Operator segment (~1,066 HubSpot records post-migration, 2026-05-14).

### Quantitative markers
- **Revenue:** $50M-$700M (canonical band). PE-backed roll-ups can exceed $1B (Segra, FirstLight, Everstream pre-bankruptcy).
- **Route miles:** 2,000-30,000.
- **States:** 3-12 (typical multi-state regional). Single-state operators below $30M are usually Municipal/Cooperative or RLEC.
- **Employees:** 200-2,000.
- **On-net buildings:** 3,500-15,000.
- **Ownership:** PE-backed (Oak Hill, Berkshire Partners, Macquarie, Cox Communications, BC Partners, Stonepeak — common sponsors). Some founder-led independents remain (Arvig MN, Hotwire FL).
- **Founded year:** 1996-2010 (CLEC vintage). Fiber-overbuilder greenfield operators 2008-2020.
- **Direct-enterprise revenue share:** >40% (distinguishing from wholesale-primary operators).

### Required signals (3-5)
1. Multi-state operations with CLEC certifications in 3+ state PUCs (verifiable via state PSC filings).
2. Public marketing of "dedicated internet access," "dark fiber," "wavelengths," "Ethernet" to **enterprise/business customers** (not consumer broadband primary).
3. Route mile disclosure in 2,000-30,000 range on company website or press.
4. PE-sponsor association OR founder-led with multi-state growth pattern.
5. Acquired 1+ smaller regional networks (the "fiber islands" pattern).

### Disqualifiers (3-5 falsifiable)
1. **National (10+ states with wholesale-primary)** → Tier 2 National Wholesale - Fiber operator.
2. **HFC/coaxial cable legacy parent** → Regional Cable Operator - Fiber operator.
3. **Municipal utility, electric co-op, or community-owned** → Municipal / Cooperative - Fiber operator.
4. **Wholesale revenue share >80%, no direct enterprise** → Tier 2 National Wholesale or Long Haul / Backbone.
5. **Subsea cable ownership or international footprint** → International Backbone Specialist (Network Op, not Fiber).

### Anchor companies (target 10-15, NA-weighted)

**North America (US-heavy):**
- **Segra** — PE-backed (Cox Communications acquired 2023). 47,000+ route miles, 17 states (Southeast / Mid-Atlantic). Acquired Everstream's St. Louis metro network 2025.
- **FirstLight Fiber** — PE-backed (Antin Infrastructure Partners). Northeast US, ~25,000 route miles, 9 states.
- **Bluebird Fiber** — PE-backed (Macquarie). **Completed Everstream asset acquisition March 2026** ($384M); now 36,000+ route miles across Kansas to Ohio to the Canadian border, 12 states, 400,000 near-net buildings.
- **Ritter Communications** — independent, Arkansas/Tennessee/Missouri/Texas. ~10,000 route miles.
- **Consolidated Communications** — Searchlight Capital acquired 2024 ($3.1B take-private). ILEC+CLEC hybrid; 23 states, ~58,000 route miles. Borderline — large enough to push into Tier 2 National Wholesale if wholesale book grows; classify as Regional CLEC while enterprise/consumer mix dominates.
- **MetroNet** — Oak Hill / KKR-backed FTTH overbuilder; merged with Vexus and Race Communications 2024. ~12 states, mostly Midwest.
- **Hotwire Communications** — independent, Florida + 11 other states. MDU/multi-unit specialist. ~$500M est.
- **Allo Communications** — Nelnet-owned. Nebraska/Colorado/Arizona.
- **Ziply Fiber** — WaveDivision Capital-backed (now BCE-owned post-2025 close at $5B). Pacific Northwest, 4 states. Borderline scale; classify Regional CLEC while ILEC heritage in WA/OR dominates.
- **Arvig** — independent family-owned, Minnesota. 18,500+ route miles. Quoted MaiaEdge customer.

**EMEA:**
- **euNetworks** — independent (Stonepeak-owned). Pan-European metro fiber, 18 cities. ~$300M est.
- **Eurofiber** — independent (PGGM + Antin Infrastructure). Netherlands/Belgium/France/Germany. ~€400M revenue.
- **Colt Technology Services** — Fidelity-owned. Pan-European + Asia metro. Borderline Tier 2 National Wholesale (Europe equivalent); classify Regional CLEC for Europe-only operators with mostly direct-enterprise revenue mix.

**APAC:**
- **Superloop** — Australia, public (ASX:SLC). National fiber + FTTP, ~A$400M revenue.

### Confusable with
- *Tier 2 National Wholesale - Fiber operator* — pivot is **direct-enterprise revenue share** (Regional CLEC >40%, Tier 2 National Wholesale <20%) and **footprint geography** (sub-national vs national).
- *Regional Cable Operator - Fiber operator* — pivot is **origin / parent legacy** (telco/CLEC vs cable/HFC).
- *Municipal / Cooperative - Fiber operator* — pivot is **ownership structure** (PE/private/public corp vs muni/co-op/community-owned).
- *Long Haul / Backbone - Fiber operator* — pivot is **route mile scale** (regional <30,000 vs national 50,000+) and **inter-city corridor focus** (metro+regional vs primarily long-haul).

### Selling angle (MaiaEdge)
"Your network is acquisitions stitched together. Each fiber island built differently, with different OSS at each site. MaiaEdge turns each of them into one asset class you can sell from — standardized services across every strand mile you own, then extends that automation to partner networks beyond your footprint. Monetize underutilized fiber, unify your network, and win the multi-state deals that go to whoever provisions fastest." Pair speed with ownership: "your team provisions in minutes."

### HubSpot fields R1/R2 must populate
- `customer_segment` = `Fiber Operator`
- `company_sub_segment` = `Regional CLEC - Fiber operator`
- `network_op_track` = (Fiber Operators don't use this field, leave null)
- `segmentation_confidence` = per scoring rules below
- `account_tier` = Tier 1-2 typical (strongest fit per cheatsheet)
- `hs_is_target_account` = `true` for Tier 1-2
- `recent_news_or_trigger_event` = populated from F-A1/F-A2/F-A4/F-A5 signal hits
- Free-text fields: route miles disclosed, states served, parent sponsor (if PE-backed), founded year, on-net building count.

### Signal source coverage (fiber-signals.md cross-reference)
- **F-A1 BEAD Subgrant Award** — Strong fit for Regional CLECs winning state subgrants (often the BEAD beneficiary for sub-state regions).
- **F-A2 Regional Fiber PE Acquisition / Roll-up** — Direct match.
- **F-A5 Executive Hire (VP Network Automation / Chief Network Officer)** — Direct match for the persona stack.
- **F-A7 Broader M&A (announcement OR close)** — Direct match.
- **F-A8 ABS / Refinancing** — Strong fit for PE-backed regional CLECs.
- **F-B2 Route Expansion / New-Market Entry** — Direct match.
- **F-B1 400G/800G Optical Upgrade Press** — Mid-fit (more common for Long Haul / Tier 2 National Wholesale).

### Contact personas (specific titles)

**Sub-$500M revenue:**
- **CTO / Chief Network Officer** (technical champion + veto authority on platform vendors)
- **COO** (operational approver; owns service delivery and NNI process)
- **CRO / VP Wholesale / VP Sales** (monetization sponsor; cares about deal velocity)
- **VP Network Operations / VP Transport / VP Service Delivery** (engineering champion)

**$500M+ or PE-backed:**
- Add **CFO** for >$1M OpEx approvals
- **PE sponsor's infrastructure investment director** (sign-off on software platform spend)
- **Chief Product Officer** or **VP Product** if NaaS/portal program exists

**Engineering tier:**
- **Director of Engineering / Sr. Network Engineer / Transport Engineer / DWDM Engineer / Principal Architect**

Strongest pattern: VP Network + VP Wholesale + CRO as a three-person buying committee.

### Confidence scoring rules

| Confidence | Trigger |
|---|---|
| `high_90` | Anchor pattern match (named anchor OR archetype within 1 SD on revenue/route miles/states) + ≥2 quantitative markers + explicit positioning on website / 10-K / Vertical Systems Group Challenge Tier mention |
| `medium_7089` | 2 of 3 above |
| `low_5069` | 1 of 3 OR ambiguous between Regional CLEC and Tier 2 National Wholesale (boundary case) |
| `manual_review_required` | Footprint straddles >8 states with mixed direct/wholesale revenue; OR record name is a brand of a larger telecom not clearly a Regional CLEC; OR revenue >$1B with growing wholesale book (could push to Tier 2 National Wholesale) |

### Industry sources for ongoing validation
- Vertical Systems Group U.S. Carrier Ethernet LEADERBOARD Challenge Tier annual list
- dgtlinfra Top 125 ISPs Group 3-4
- State PUC dockets (CLEC certifications, tariff filings)
- Light Reading, Fierce Network, Telecompetitor regional operator coverage
- NTIA BEAD subgrant award lists by state
- SEC 10-K filings for public Regional CLECs (Consolidated Communications, Lumen — for benchmarking)
- PitchBook / S&P Global Market Intelligence PE-sponsor portfolio pages

---

## 2. `Long Haul / Backbone - Fiber operator`

### Definition
National or multi-national fiber operators whose primary business is long-haul / inter-city backbone connectivity, typically with 50,000+ route miles of fiber spanning major metros. Sell dark fiber, wavelengths (100G/400G/800G), and IP transit to other carriers, hyperscalers, content providers, and large enterprises. Run sophisticated incumbent automation systems (Zayo DynamicLink, Lumen RapidRoutes) that already provide provisioning at scale within their network. MaiaEdge does NOT replace these; it federates above them, extending automation across operator boundaries. Note Zayo is now classified per file 05 as Tier 2 National Wholesale (post-Crown Castle Fiber close), not Long Haul, despite straddling both archetypes — this is the canonical resolution.

### Quantitative markers
- **Revenue:** $500M-$15B+ (varies widely).
- **Route miles:** 50,000-340,000+. Lumen at 340,000 is the high end.
- **States/countries:** National US (40+ states) OR pan-EU OR pan-APAC.
- **Employees:** 1,500-30,000+.
- **Ownership:** Public (Lumen, Cogent), PE-backed (FiberLight under Morrison & Co; Uniti pre-Windstream merger).
- **Founded year:** Varies; many trace to 1990s long-haul builds (Qwest, MCI, Williams Communications heritage in Lumen).
- **Direct-enterprise revenue share:** Variable; may be primary (Lumen) or near-zero (FiberLight pure wholesale).
- **Customer mix:** Heavy hyperscaler + carrier wholesale; some direct enterprise (Lumen).

### Required signals (3-5)
1. 50,000+ route miles of long-haul fiber explicitly stated on website or 10-K.
2. Inter-city corridor specialization (intercontinental, transcontinental, regional backbone — e.g., Seattle-Minneapolis, Virginia Beach-Northern Virginia).
3. Hyperscaler IRU/dark fiber agreements disclosed in earnings calls or press.
4. 400G/800G coherent optical deployment on backbone (Ciena WaveLogic 5/6, Nokia 1830 PSI-M, Infinera ICE-X).
5. Public mention of own provisioning automation platform (DynamicLink, RapidRoutes, equivalent).

### Disqualifiers (3-5 falsifiable)
1. **<30,000 route miles AND single-region footprint** → Tier 2 National Wholesale or Regional CLEC.
2. **Primary product is direct enterprise managed services without long-haul wholesale book** → Tier 1 Carrier or Cable MSO Enterprise Division (Network Op).
3. **Subsea cable ownership as primary** → International Backbone Specialist (Network Op).
4. **Metro-only or sub-state footprint** → Dark Fiber Specialist or Regional CLEC.
5. **Heavy retail consumer broadband revenue** → Cable MSO or Tier 1 Carrier (Network Op).

### Anchor companies

**North America:**
- **Lumen Technologies** (NYSE: LUMN) — 340,000 route miles, 47 million intercity fiber miles planned by 2028. Consumer FTTH being divested to AT&T (announced 2025). Heritage: Qwest + Level 3 + CenturyLink. **Boundary case:** also has Tier 1 Carrier - Network Op characteristics; classify per current legal state. File 05 keeps Lumen as Tier 1 Carrier for the parent record.
- **Uniti Group** (post-Windstream merger close August 2025) — 240,000 route miles, 300+ metros, 47 states. Combined revenue ~$5B annualized. Public NYSE:UNIT (pending privatization per merger terms).
- **Cogent Communications** (NASDAQ:CCOI) — 20,200 miles of dark fiber gained from Sprint assets + 19,000 inter-city wavelength network. Wavelength revenue $13.6M in Q1 2026 (+90.8% YoY). Note: also classified as Pure Wholesale Carrier (Network Op) for IP transit primary; flag for `manual_review_required` if HubSpot record is the Cogent parent.
- **FiberLight** — Morrison & Co / Australian Retirement Trust / UBS Asset Management consortium-owned. 11,000+ miles in Texas, Atlanta metro presence, acquired Metro Fiber Networks (200-mile Virginia Beach-Richmond) April 2025. Pure wholesale, no retail.
- **GTT Communications** — sold infrastructure to I Squared 2021, restructured Chapter 11 2022; today primarily managed services / SD-WAN. **Removed as Long Haul anchor** — moved to Managed Network Services (MSP).
- **Crown Castle Fiber** — **acquired by Zayo April 2026, no longer exists as standalone entity.** Do NOT use as anchor.

**EMEA:**
- **Arelion** (formerly Telia Carrier) — Polhem Infra-owned. AS1299, pan-European long-haul + transatlantic. ~€600M revenue.
- **EXA Infrastructure** — I Squared Capital-owned (acquired from GTT 2021 for $2.15B). 174,500 km fibre across 37 countries. €1.3B refinancing October 2025. Note: also classified per file 05 as Tier 2 National Wholesale Fiber for EU; the Long Haul classification fits better for EXA's transatlantic + subsea + Paris-Marseille / London-Frankfurt long-haul focus. Flag for `manual_review_required`.

**APAC:**
- **NTT Communications (international backbone) / AS2914** — division of NTT Group. Tier 1 IP transit + 100s of POPs globally. Note: parent is Tier 1 Carrier (Network Op); classify the international wholesale book separately if record is for the wholesale subsidiary.

### Confusable with
- *Tier 2 National Wholesale - Fiber operator* — Tier 2 is metro+long-haul lit services primary; Long Haul / Backbone is primarily long-haul corridor dark fiber + waves with metro as anchor terminations only. Zayo (now Tier 2 National Wholesale per file 05) and Lumen sit on opposite sides of this boundary.
- *Dark Fiber Specialist - Fiber Operator* — Dark Fiber Specialist is metro/regional with smaller route miles (~5,000-30,000); Long Haul is national-scale (50,000+).
- *Pure Wholesale Carrier - Network Op* — Pure Wholesale is IP transit / Tier 1 routing primary; Long Haul is dark fiber + waves primary. Cogent sits on the boundary.
- *International Backbone Specialist - Network Op* — International Specialist is subsea + cross-border primary; Long Haul is intra-continental.

### Selling angle (MaiaEdge)
"Your customers want your NNIs automated. They already are. The next question is whether your customers can reach cities you don't own. MaiaEdge is the cross-operator layer that extends your reach without you laying another strand — federation on top of your existing automation, not a replacement for it. Your customers see one fabric; you keep the customer, the margin, and the control." **Critical framing:** displacement-resistant. Position as layered above the incumbent PCE/OSS (Cisco Crosswork, Juniper Paragon Pathfinder, Ciena Blue Planet, Nokia NSP), not replacing it.

### HubSpot fields R1/R2 must populate
- `customer_segment` = `Fiber Operator`
- `company_sub_segment` = `Long Haul / Backbone - Fiber operator`
- `segmentation_confidence` = per scoring rules below
- `account_tier` = Tier 1-3 (strategic but lower close-rate due to incumbent automation)
- `hs_is_target_account` = `true` for Tier 1-2
- `recent_news_or_trigger_event` = F-A3 / F-A6 / F-A4 hits
- Free-text fields: route mile count (the canonical scale metric), inter-city corridors disclosed, ASN numbers (BGP validation), incumbent automation platform name.

### Signal source coverage
- **F-A3 AI Data Center Lit / Dark Fiber Win or RFP** — Direct match (Lumen-QTS, FiberLight-Virginia Beach corridor).
- **F-A4 NaaS / Automation / Portal Launch** — Direct match (DynamicLink benchmark).
- **F-A6 Dark Fiber IRU / Long-Haul Sold-Out** — Direct match.
- **F-B1 400G/800G Optical Upgrade Press** — Direct match.
- **F-B3 Subsea Cable Landing / Backhaul Partnership** — Partial fit (cross-over with International Specialist).
- **F-B4 Public-Company Earnings Call Keyword Hits** — Direct match for public operators (LUMN, UNIT, CCOI).
- **F-C5 Earnings-Disclosed Fiber-Count Step-Change** — Direct match.

### Contact personas

**Public / $500M+ revenue:**
- **Chief Product & Strategy Officer** (owns automation-platform strategy)
- **VP Network Engineering** + **Principal Architect** (technical buy-in for federation layer)
- **CEO** for strategy-level shifts
- **VP Wholesale / VP Carrier Relations** (monetization sponsor)
- **Chief Network Officer / CTO**

Target company size: ≥1,000 employees.

Engineering tier:
- **Director of Network Architecture / Director of Optical Engineering / DWDM Engineer**

### Confidence scoring rules

| Confidence | Trigger |
|---|---|
| `high_90` | Named anchor OR 50,000+ route miles + long-haul corridor positioning + 400G/800G public deployment + hyperscaler IRU disclosed |
| `medium_7089` | 2 of 3 |
| `low_5069` | Sub-100,000 route miles but national footprint; OR boundary case with Tier 2 National Wholesale |
| `manual_review_required` | Multi-product overlap (e.g., Cogent — Long Haul + Pure Wholesale Carrier); Zayo (now Tier 2 National Wholesale per file 05); operators with significant retail consumer book (Lumen) |

### Industry sources for ongoing validation
- Light Reading optical coverage + M&A Watch
- Telecom Ramblings (long-haul tracker)
- SEC 10-K / 10-Q for LUMN, UNIT, CCOI
- TeleGeography long-haul fiber maps
- Lightwave Online 400G/800G deployment news
- Capacity Magazine wholesale carrier rankings
- Vertical Systems Group LEADERBOARD (Challenge Tier wholesale operators)

---

## 3. `Dark Fiber Specialist - Fiber Operator`

### Definition
Operators whose primary product line is dark fiber sales (Indefeasible Rights of Use, IRUs) and wavelength services rather than lit Ethernet or DIA. Typically metro or regional in geographic scope with strand-rich routes that monetize through 20-year IRU contracts and shorter-term wavelength leases. Smaller in revenue than Long Haul / Backbone operators but with disproportionate strategic value because dark fiber is the lever for AI data center interconnect (36x more fiber per route than CPU racks) and hyperscaler buildouts. The valuation story has shifted: dark fiber strategic value inflated faster than operators can light it in 2025-2026, with M&A multiples reflecting 25-30x EV/EBITDA on AI-adjacent assets. **Note: HubSpot internal value uses capital "O" in "Operator" — the only Fiber sub-segment that breaks lowercase convention.**

### Quantitative markers
- **Revenue:** $20M-$500M (smaller than Long Haul; smaller than Tier 2 National Wholesale).
- **Route miles:** 5,000-30,000 (metro + regional density; not national scale).
- **States/regions:** 1-10 metros OR a single regional corridor (e.g., Virginia Beach-Northern Virginia for FiberLight; Pacific Northwest for various).
- **Employees:** 50-500.
- **Ownership:** PE-backed (FiberLight by Morrison & Co; Crown Castle Fiber pre-Zayo close) or independent founder-led.
- **Revenue mix:** >50% from IRU contracts + wavelength leases; <30% from lit Ethernet / DIA / managed services.
- **Strand-density-per-route:** Higher than long-haul peers (144-432 strand counts on AI-corridor builds; was 8-12 historically).

### Required signals (3-5)
1. Marketing material explicitly leads with "dark fiber" or "IRU" as primary product (not just one of many).
2. Strand counts / strand-mile disclosures (vs route miles only).
3. Metro density in 1-5 markets with strand-rich routes (not pan-national thin coverage).
4. AI data center proximity or hyperscaler cable landing station route ownership.
5. Long-hold-time IRU contract structure (10-25 year terms) disclosed in press or analyst reports.

### Disqualifiers (3-5 falsifiable)
1. **National coverage with 50,000+ route miles** → Long Haul / Backbone.
2. **Primary product is lit Ethernet / DIA to enterprise** → Regional CLEC.
3. **HFC/coaxial cable legacy** → Regional Cable Operator.
4. **Municipal utility, electric co-op, or community-owned** → Municipal / Cooperative.
5. **No discrete dark fiber product offering** (i.e., dark fiber is opportunistic only, not a productized line) → Regional CLEC or Long Haul.

### Anchor companies

**North America:**
- **FiberLight** — Morrison & Co / Australian Retirement Trust / UBS Asset Management. ~11,000+ miles in Texas + Atlanta + Virginia Beach-Richmond 200-mile dark fiber corridor (acquired April 2025, closed June 2025). Subsea cable landing proximity (Virginia Beach handles ~70% of transoceanic internet traffic). Pure wholesale dark fiber + lit services. **Boundary case with Long Haul / Backbone** — classify Dark Fiber Specialist for the metro+regional density; Long Haul if route-mile total grows beyond 30,000 with national footprint.
- **Conterra Networks** — independent, Southeast US dark fiber + wavelengths. Smaller (<$100M est.).
- **Wilcon (Pacific Lightwave)** — independent, California dark fiber.
- **Tilson** — pure wholesale dark fiber + construction (some classification ambiguity with construction services).
- **INDATEL** — 700+ rural ILEC/CLEC consortium providing wholesale dark fiber connectivity between members. Hybrid Dark Fiber Specialist + Municipal/Cooperative; classify primarily Dark Fiber Specialist for the wholesale role.
- **Ocean Networks** — independent (Hawaii/Pacific). Quoted MaiaEdge customer for INDATEL cross-carrier reach.
- **Summit IG (formerly Summit Telecom)** — Dallas metro dark fiber.

**EMEA:**
- **Geo Networks** (UK) — Goldman Sachs Asset Management. UK metro dark fiber + ducts.
- **Fibrelogic / SSE Telecoms** (UK) — utility-affiliate dark fiber.
- **NEOS Networks** (UK, formerly SSE Enterprise Telecoms) — pan-UK dark fiber + wavelengths.

**APAC:**
- **HGC Global Communications** (Hong Kong) — subsea + dark fiber Greater Mekong. Note: also classified as International Backbone Specialist (Network Op); flag boundary.

### Confusable with
- *Long Haul / Backbone - Fiber operator* — pivot is **route mile scale** (Dark Fiber Specialist <30,000; Long Haul 50,000+) and **inter-city corridor vs metro density**.
- *Regional CLEC - Fiber operator* — pivot is **product mix** (Dark Fiber Specialist >50% IRU/dark; Regional CLEC <30%).
- *Tier 2 National Wholesale - Fiber operator* — Tier 2 is metro+long-haul lit services primary with national footprint; Dark Fiber Specialist is dark+wavelength primary with metro/regional density.

### Selling angle (MaiaEdge)
"Dark strands depreciate every day they're unlit. MaiaEdge lights them as sellable, deterministic services on demand — without committing the strand to a single IRU customer. Productize wavelength-on-demand for hyperscaler AI interconnect, monetize unlit capacity in minutes, and turn every dark mile in your inventory into a sellable path." Pair with the AI DC fiber ratio framing: "AI data centers need 36x more fiber per rack — your team's dark strands are the inventory hyperscalers are bidding for. MaiaEdge lets you sell that inventory as a deterministic, productized service before competitors light theirs."

### HubSpot fields R1/R2 must populate
- `customer_segment` = `Fiber Operator`
- `company_sub_segment` = `Dark Fiber Specialist - Fiber Operator` (**capital "O"!**)
- `segmentation_confidence` = per scoring rules below
- `account_tier` = Tier 1-2 (monetization-velocity thesis is the strongest pitch)
- `hs_is_target_account` = `true`
- `recent_news_or_trigger_event` = F-A3 / F-A6 hits priority
- Free-text fields: strand counts disclosed, metros / regional corridors, IRU contract terms cited in press, AI data center proximity.

### Signal source coverage
- **F-A3 AI Data Center Lit / Dark Fiber Win or RFP** — Direct match, highest priority.
- **F-A6 Dark Fiber IRU / Long-Haul Sold-Out** — Direct match.
- **F-C5 Earnings-Disclosed Fiber-Count Step-Change** — Direct match (864-fiber hyperscaler order pattern).
- **F-B3 Subsea Cable Landing / Backhaul Partnership** — Strong fit (cable landing station proximity).
- **F-A8 ABS / Refinancing** — Mid-fit (dark fiber operators issue ABS to monetize plant).

### Contact personas
- **Wholesale / Business Development leadership** (Head of Dark Fiber, VP Capacity, VP Wholesale)
- **CRO / Chief Commercial Officer**
- **CTO / Chief Network Officer**
- **Director of Optical Engineering / DWDM Engineer** (technical due diligence)
- For PE-backed: **CEO** + **PE sponsor's infrastructure investment director**

Strongest pattern: VP Wholesale + Head of Dark Fiber + CTO.

### Confidence scoring rules

| Confidence | Trigger |
|---|---|
| `high_90` | >50% revenue from IRU / dark fiber / wavelengths + metro/regional density (not national) + named anchor pattern + strand-count disclosure |
| `medium_7089` | 2 of 4 above |
| `low_5069` | Dark fiber is one of several products but not lead; boundary case with Long Haul or Tier 2 National Wholesale |
| `manual_review_required` | Dark fiber product exists but unclear share of revenue; INDATEL-style consortium ambiguity (Dark Fiber Specialist vs Municipal/Cooperative); HGC-style international subsea overlap |

### Industry sources for ongoing validation
- dgtlinfra "Top 200 Dark and Lit Fiber Providers in the World" — primary anchor source.
- Lightwave Online dark fiber + IRU coverage.
- Telecom Ramblings dark fiber tracker.
- SEC 8-K / S-1 / 424 ABS prospectuses (Uniti Fiber ABS 2025-1 as benchmark).
- MarketsAndMarkets dark fiber market reports.
- Operator press for hyperscaler IRU announcements.

---

## 4. `Tier 2 National Wholesale - Fiber operator`

### Definition
National or near-national wholesale-primary fiber operators that sell dark fiber, lit transport, wavelengths, and IRUs to other carriers, hyperscalers, large enterprises, and ISPs. Smaller than Tier 1 Carriers (no retail consumer; no large-scale direct enterprise) but bigger and broader than Regional CLECs. The "metro + long-haul wholesale fabric" archetype. National US or pan-EU footprint, 20,000-300,000 route miles, 80%+ revenue from wholesale, often PE-owned or recently consolidated.

### Quantitative markers
- **Revenue:** $300M-$5B+ (post-Zayo+Crown Castle Fiber band widened; Zayo now estimated $2.5B+ combined).
- **Route miles:** 20,000-300,000 (Zayo at 224,000 post-CCF; EXA at 174,500 km / ~108,000 miles).
- **States:** National US (30+) OR pan-EU.
- **POPs:** Most Tier-1 metros.
- **Employees:** 1,000-5,000+.
- **Ownership:** PE / Infrastructure fund-backed (DigitalBridge, EQT, I Squared, Stonepeak — common sponsors).
- **Wholesale revenue share:** 80%+ (distinguishing test from Regional CLEC).
- **Founded year:** Varies (Zayo from 2007; EXA from 2021 GTT InfraCo carve-out).

### Required signals (3-5)
1. Public positioning as wholesale-first / carrier-to-carrier / hyperscaler-anchor on website.
2. National or pan-EU footprint with 20,000+ route miles.
3. Hyperscaler customer disclosures (AWS / Azure / GCP / Meta / Oracle named in press or earnings).
4. PE / infrastructure fund ownership disclosed (DigitalBridge, EQT, I Squared, Stonepeak portfolio company).
5. Dark fiber + lit Ethernet + wavelengths productized as separate offerings.

### Disqualifiers (3-5 falsifiable)
1. **>20% direct-enterprise revenue (not via partner channels)** → Regional CLEC.
2. **<20,000 route miles AND <$200M revenue** → Regional CLEC.
3. **Primary product is dark fiber only (no lit services book)** → Dark Fiber Specialist.
4. **Subsea cable ownership + international primary** → International Backbone Specialist (Network Op).
5. **HFC/coaxial cable legacy with retail residential parent** → Cable MSO Enterprise Division (Network Op).

### Anchor companies

**North America:**
- **Zayo Group** — DigitalBridge-owned. **224,000 route miles post-Crown Castle Fiber acquisition (closed April 29, 2026 — $4.25B + $8.5B combined with EQT's small cells acquisition).** ~70,000 on-net locations including 40,000 new on-net enterprise locations from CCF. Combined revenue >$2.5B est. Canonical anchor.
- **Lightpath** — Altice USA 50.01% + Morgan Stanley Infrastructure Partners 49.99% JV. **Year-end 2025 revenue $468M; AI-related contracts $362M (40% YoY growth); 10,000+ unique fiber route miles serving 15,000+ locations.** 35% Q4 2025 fiber revenue growth driven by hyperscaler demand. Acquiring + building in Phoenix (230 mi), Columbus (150 mi), Eastern PA (130 mi), Greater NY (100 mi). NYSE-listed parent (ATUS).
- **Uniti Fiber / Uniti Wholesale (post-Windstream merger)** — Public, merger closed August 1, 2025. 240,000 route miles, 300+ metros, 47 states. Combined revenue ~$5B annualized. Largest pure-play fiber by route miles in US post-merger.
- **Bluebird Fiber (post-Everstream)** — Macquarie-backed; merger closed March 6, 2026. **36,000+ route miles, 12 states (Kansas to Ohio to Canadian border), 400,000 near-net buildings, ~$384M acquisition price.** Boundary case with Regional CLEC; classify Tier 2 National Wholesale at scale (>12 states with wholesale focus).
- **FiberLight** — listed dual-category here AND Dark Fiber Specialist; classify Dark Fiber Specialist primary unless route mile total exceeds 30,000 and lit services book grows.

**EMEA:**
- **EXA Infrastructure** — I Squared Capital-owned. 174,500 km fibre (37 countries), 65,000 km 400G-enabled, €1.3B refinancing October 2025. Pan-European + transatlantic. **Boundary case with Long Haul / Backbone** — file 05 places EXA in Tier 2 National Wholesale Fiber; the transatlantic + subsea pieces also fit International Backbone Specialist. Default Tier 2 National Wholesale for the pan-EU terrestrial metro + long-haul book.

**APAC:**
- **Superloop Wholesale** — Australian wholesale arm; ~A$400M total revenue with wholesale subset.
- **HGC Global Communications** — Hong Kong, Greater Mekong + subsea. Boundary with International Backbone Specialist.

### Confusable with
- *Regional CLEC - Fiber operator* — pivot is **wholesale revenue share** (Tier 2 >80%; Regional CLEC <60%) and **footprint** (national vs sub-national).
- *Long Haul / Backbone - Fiber operator* — pivot is **product mix** (Tier 2 = metro+long-haul lit; Long Haul = primarily long-haul corridor + dark).
- *Pure Wholesale Carrier - Network Op* — Pure Wholesale Carrier is IP transit primary; Tier 2 National Wholesale Fiber is fiber + lit transport + waves primary.
- *International Backbone Specialist - Network Op* — International Specialist is subsea + cross-border primary.

### Selling angle (MaiaEdge)
"You're squeezed between Tier 1 carriers above and Regional CLECs below. You differentiate on relationships, route choice, and pricing flexibility — but your customers want orchestration, not just transport. MaiaEdge is the orchestration layer they expect from AWS Direct Connect, layered above your existing fabric. Your customers see a private, deterministic cloud on-ramp; you keep the customer, the margin, and the route." Pair with monetization-velocity: "Every dark mile of fiber you own becomes a sellable, deterministic service in minutes — not 60-90 day NNI processes that lose deals."

### HubSpot fields R1/R2 must populate
- `customer_segment` = `Fiber Operator`
- `company_sub_segment` = `Tier 2 National Wholesale - Fiber operator`
- `segmentation_confidence` = per scoring rules below
- `account_tier` = Tier 1 (highest priority — largest deal sizes, federation-anchor accounts)
- `hs_is_target_account` = `true`
- Free-text fields: route miles disclosed, wholesale revenue % (if disclosed), PE sponsor, hyperscaler customer names disclosed in press.

### Signal source coverage
- **F-A2 Regional Fiber PE Acquisition / Roll-up** — Direct match (Zayo-CCF, Bluebird-Everstream, Uniti-Windstream patterns).
- **F-A3 AI Data Center Lit / Dark Fiber Win or RFP** — Direct match.
- **F-A4 NaaS / Automation / Portal Launch** — Direct match (Zayo DynamicLink benchmark; competitor proof-of-struggle).
- **F-A6 Dark Fiber IRU** — Direct match.
- **F-A7 Broader M&A (announcement OR close)** — Direct match.
- **F-A8 ABS / Refinancing** — Direct match.
- **F-B1 400G/800G Optical Upgrade** — Direct match.
- **F-B4 Public-Company Earnings Call Keywords** — Strong fit for public ones (UNIT, parent ATUS).

### Contact personas
- **Chief Product & Strategy Officer / Chief Commercial Officer**
- **VP Wholesale / VP Carrier Relations / VP Network Automation**
- **CTO / Chief Network Officer**
- **VP Network Engineering / Principal Architect**
- **CEO** (for strategy-level decisions on platform partnerships)
- **PE sponsor's infrastructure investment director / operating partner**

Strongest pattern: CPO + VP Wholesale + CTO as buying committee.

### Confidence scoring rules

| Confidence | Trigger |
|---|---|
| `high_90` | Named anchor OR national footprint (30+ states or pan-EU) + 20,000+ route miles + 80%+ wholesale revenue mix + PE/infrastructure-fund sponsor disclosed |
| `medium_7089` | 3 of 4 |
| `low_5069` | National footprint but smaller route miles (<30,000); mixed wholesale/direct enterprise |
| `manual_review_required` | Zayo (boundary with Long Haul), EXA (boundary with International Backbone Specialist + Long Haul), Cogent (boundary with Pure Wholesale Carrier); pending M&A on a record (per file 05 policy: classify per current legal state, RevOps adjusts post-close) |

### Industry sources for ongoing validation
- Light Reading wholesale fiber coverage + M&A Watch
- Telecom Ramblings (the canonical wholesale fiber tracker)
- DCD (Data Center Dynamics) fiber acquisition coverage
- S&P Global Market Intelligence
- Vertical Systems Group Challenge Tier
- dgtlinfra "Top 200 Dark and Lit Fiber Providers"
- SEC 10-K filings for UNIT, public parents (ATUS for Lightpath)
- Stonepeak / DigitalBridge / EQT / I Squared portfolio pages

---

## 5. `Regional Cable Operator - Fiber operator`

### Definition
Regional cable companies (smaller than national MSOs like Comcast, Charter, or Cox) with growing commercial fiber arms. Parent is regional cable; the buying angle MaiaEdge sells to is the commercial / business fiber division. Parent's B2B scale puts them under $1.5B in commercial revenue (above that → Cable MSO Enterprise Division - Network Op). Mostly residential HFC plant with selective FTTH overbuild + commercial fiber expansion to chase enterprise revenue. The commercial fiber book is the growth engine because residential ARPU is plateauing under FWA + fiber overbuilder pressure.

### Quantitative markers
- **Parent B2B revenue:** $30M-$1.5B.
- **Total parent revenue:** $200M-$3B.
- **States:** 3-22 (regional or multi-state but NOT national).
- **Founded year:** 1960s-1990s (cable MSO heritage).
- **Network composition:** Mostly residential HFC + selective FTTH overbuild + commercial fiber routes.
- **Employees:** 500-5,000.
- **Subscribers:** 100K-2M broadband.
- **Ownership:** Public (WOW! NYSE:WOW; Cable ONE NASDAQ:CABO), PE-backed (Astound by Stonepeak), or family/independent (Mediacom, Midco).

### Required signals (3-5)
1. Residential HFC/cable parent — NCTA member or equivalent regional cable trade group.
2. Multi-state footprint (3-22 states) but NOT national (10+ states with national MSO scale).
3. Commercial fiber product line marketed under distinct brand (e.g., "Mediacom Business," "Midco Business," "Breezeline Business").
4. Total parent revenue $200M-$3B.
5. Mixed HFC + fiber network (not 100% fiber).

### Disqualifiers (3-5 falsifiable)
1. **National multi-state cable with $1.5B+ B2B revenue (Comcast Business, Spectrum Enterprise, Cox Business)** → Cable MSO Enterprise Division (Network Op).
2. **No HFC/coaxial cable legacy parent (pure fiber/CLEC heritage)** → Regional CLEC.
3. **Municipal utility or community-owned** → Municipal / Cooperative.
4. **Wholesale-only with no retail residential broadband** → Tier 2 National Wholesale or Dark Fiber Specialist.
5. **Single-state with <$10M B2B** → flag for manual review (likely Municipal/Cooperative or too small).

### Anchor companies

**North America:**
- **Breezeline (Cogeco US)** — 13 US states (CT, DE, FL, ME, MD, MA, NH, NY, OH, PA, SC, VA, WV). Q3 2025 revenue $1.448B; FQ4 2025 $335.8M (down 9% YoY). 622,000+ broadband customers, 1.8M passings, ~28K new FTTP passings/quarter. Acquired WOW! Ohio assets 2024. 8th largest US cable operator by TV customers.
- **WideOpenWest (WOW!)** (NYSE:WOW) — independent, public. 2024 revenue $629M. Sold Chicago/Evansville/Anne Arundel systems to Astound for $661M — footprint shifting. Borderline scale.
- **Mediacom Business** — subsidiary of Mediacom Communications. **22 states, 1.44M broadband subscribers**, smaller cities/rural. Family-owned (Rocco Commisso). Commercial fiber book growing.
- **Midco Business** — subsidiary of Midco. Minnesota, South Dakota, North Dakota, Kansas, Wisconsin (5 Midwest states). ~12.99% of customers fiber-eligible.
- **Service Electric Cable TV** — independent, regional Pennsylvania cable + fiber.
- **GCI** — Alaska, owned by Liberty Broadband. Geographically isolated special case.
- **Cable ONE / Sparklight** (NYSE:CABO) — ~$1.7B revenue. Boundary case — could push into Cable MSO Enterprise Division Network Op. Classify Regional Cable Operator while sub-$1.5B B2B holds.
- **Astound Broadband** — Stonepeak-owned; consolidating Wave/RCN/Grande/Astound brands. **Pending merger with Alphabet's GFiber announced March 11, 2026; close expected Q4 2026 — combined 7.1M passings across 20+ states.** Post-close, will exceed Regional Cable Operator scale and move to Cable MSO Enterprise Division Network Op. **Pre-close: classify Regional Cable Operator with `manual_review_required` flag.**
- **Atlantic Broadband** — historical name for Breezeline pre-2022 rebrand; record may exist under either name.

**EMEA:**
- **Telenet** (Liquid Intelligent Technologies parent, Belgium) — boundary case at $2.5B revenue; could push to Cable MSO Network Op.
- **Vodafone Ziggo** (Netherlands) — JV; likely exceeds Regional Cable scale → Cable MSO Network Op.

**APAC:**
- Limited canonical anchors; APAC cable operators tend to be national (J:COM Japan) or absorbed by national telcos.

### Confusable with
- *Cable MSO Enterprise Division - Network Op* — pivot is **scale** (Cable MSO = national $1.5B+ B2B; Regional Cable Operator = regional sub-$1.5B B2B).
- *Regional CLEC - Fiber operator* — pivot is **origin / parent legacy** (cable/HFC vs CLEC/fiber-overbuilder).
- *Municipal / Cooperative - Fiber operator* — pivot is **ownership** (for-profit cable corp vs muni/co-op).
- *Tier 2 National Wholesale - Fiber operator* — pivot is **customer mix** (Regional Cable = primarily retail residential + SMB direct; Tier 2 Wholesale = primarily wholesale carrier-to-carrier).

### Selling angle (MaiaEdge)
"Residential ARPU is plateauing under FWA and fiber overbuilder pressure. Your commercial fiber book is the growth engine — but you compete with Comcast Business, AT&T Business, and the regional CLECs for the same mid-market customers. MaiaEdge is the SaaS fabric layer that lets your team tell commercial customers 'we connect you to AWS / Azure / GCP / Equinix the same way the big carriers do — no orchestration team required.' Monetize the commercial fiber you've built, win the multi-state SMB deals you're losing to slow provisioning, and productize cloud on-ramp without building a NaaS." Pair speed with ownership: "your team provisions in minutes."

### HubSpot fields R1/R2 must populate
- `customer_segment` = `Fiber Operator`
- `company_sub_segment` = `Regional Cable Operator - Fiber operator`
- `segmentation_confidence` = per scoring rules below
- `account_tier` = Tier 2-3 typical (smaller deal sizes than Regional CLEC; cable parent budget cycles slower)
- `hs_is_target_account` = `true` for Tier 2
- Free-text fields: total parent revenue, B2B revenue (if disclosed), states served, commercial fiber brand name, broadband subscriber count.

### Signal source coverage
- **F-A1 BEAD Subgrant Award** — Mid-fit (cable operators winning BEAD = footprint expansion + commercial fiber growth).
- **F-A4 NaaS / Automation / Portal Launch** — Strong fit (cable operators chasing Tier 1 portal feature parity).
- **F-A5 Executive Hire (VP Business / VP Commercial Sales)** — Strong fit.
- **F-A7 Broader M&A** — Strong fit (Astound-GFiber, WOW!-Astound divestiture pattern).
- **F-B2 Route Expansion / New-Market Entry** — Direct match.
- **F-B4 Public-Company Earnings Call Keywords** — Direct match for public ones (WOW, CABO).

### Contact personas
- **VP Business / VP Commercial Services / President of Business Services** (the commercial fiber arm leadership — distinct from residential)
- **Chief Commercial Officer**
- **VP Network Operations / VP Engineering**
- **CTO** (parent company; sometimes shared between residential + business)
- **Director of Wholesale / VP Carrier Relations** (if commercial fiber wholesale book exists)

Strongest pattern: VP Business + VP Network + CTO.

### Confidence scoring rules

| Confidence | Trigger |
|---|---|
| `high_90` | HFC/cable legacy parent verifiable + 3-22 state footprint + B2B revenue $30M-$1.5B + named anchor pattern + NCTA membership |
| `medium_7089` | 2 of 4 above |
| `low_5069` | Boundary case with Cable MSO Network Op (Astound, Cable ONE); OR cable parent with minimal commercial fiber book |
| `manual_review_required` | Astound (pending GFiber merger), Cable ONE (~$1.7B borderline), record straddling Cable MSO Enterprise Division boundary; record is a brand of a larger telecom not clearly classified |

### Industry sources for ongoing validation
- NCTA member directory
- dgtlinfra Top 125 ISPs Group 2-3
- Leichtman Research Group cable subscriber reports (quarterly)
- Individual company filings (WOW! and Cable ONE are public)
- S&P Global cable M&A coverage
- Light Reading + Fierce Network cable operator coverage
- Vertical Systems Group LEADERBOARD (cable operators in Challenge Tier)

---

## 6. `Municipal / Cooperative - Fiber operator`

### Definition
Municipal utility fiber networks, electric cooperatives running broadband programs, telephone cooperatives (RLEC heritage), tribal broadband authorities, and multi-operator consortia. Community-owned, member-owned, or municipally-owned rather than investor-owned. Operating models include retail FTTH direct-to-subscribers, open-access wholesale platforms (UTOPIA Fiber model), and federation consortia where multiple member operators share infrastructure (Diamond State Networks, INDATEL). The federation thesis MaiaEdge is ahead of carrier messaging on — these operators are already organized around shared infrastructure and need an operating layer for cross-boundary provisioning. **Renamed from `Co-op/consortium` 2026-05-13.** Includes the BEAD subgrant recipient cohort — Q2-Q4 2026 = peak award velocity with binding 4-year build obligations.

**Exclusion clarification:** Middle-mile-only operators that are purely grant-funded anchor-institution models (KentuckyWired, Project THOR, MassBroadband 123, Mid-Atlantic Broadband) are **structurally incompatible with MaiaEdge's SaaS consumption model** — revenue base is IRU + anchor contracts, not on-demand wholesale. Flag for exclusion. **Exception:** If the operator is also a consortium or has a commercial-strand wholesale arm with on-demand pricing, qualify on that basis.

### Quantitative markers
- **Revenue:** Highly variable — $5M-$300M typical; consortia like Diamond State Networks reach $1.66B in fiber infrastructure investment across 13 cooperative members.
- **Route miles:** 500-50,000 (Diamond State's 50,000 miles is the canonical large-consortium scale).
- **States:** Typically single-state for munis/co-ops; consortia may span 1-5 states.
- **Customers passed:** 50K-1.4M (Diamond State Networks at 1.25M rural Arkansans).
- **Ownership:** Municipal utility (EPB Chattanooga), electric co-op (NRECA member), telephone co-op (NTCA member, ~850 RLECs), tribal authority, multi-operator consortium.
- **Funding model:** Mix of municipal bonds, USDA ReConnect, BEAD subgrants, NTIA Middle Mile, state broadband office grants, member capital.
- **Founded year:** Wide range — EPB Chattanooga deployed fiber 2008-2010; UTOPIA founded 2004 by 11 cities; Diamond State Networks founded 2020 by 13 Arkansas electric co-ops.

### Required signals (3-5)
1. NTCA membership (Rural Broadband Association — ~850 member companies, 44 states) OR NRECA broadband program participation (~200+ co-ops).
2. Municipal utility ownership (city-owned electric/water utility) OR member-owned cooperative structure.
3. Open-access wholesale platform (UTOPIA model) OR retail FTTH community broadband (EPB model) OR federation consortium structure (Diamond State / INDATEL model).
4. State broadband office grant recipient OR NTIA BEAD subgrant OR USDA ReConnect grant recipient.
5. Community-governance language on website ("residents own and govern," "city-owned," "member-owned," "consortium of [n] cooperatives").

### Disqualifiers (3-5 falsifiable)
1. **Investor-owned for-profit corporation** → Regional CLEC or Regional Cable Operator.
2. **Middle-mile-only with no retail or commercial wholesale arm** → EXCLUDE (structural misfit per file 05).
3. **National multi-state private cable parent** → Cable MSO Enterprise Division (Network Op) or Regional Cable Operator.
4. **PE-backed roll-up** → Regional CLEC.
5. **Wholesale-only with national or multi-region scale and >$300M revenue** → Tier 2 National Wholesale.

### Anchor companies

**North America — Municipal:**
- **EPB Chattanooga** — City-owned electric utility, Hamilton County TN. 9,000-mile fiber network; first 1 Gig city in Western Hemisphere (2010). $5.3B in net community benefits delivered 2011-2026.
- **UTOPIA Fiber** (Utah Telecommunication Open Infrastructure Agency) — 20 Utah cities + 3 operational partners; open-access wholesale platform. Lowest latency of all 14 municipal broadband providers (6-8ms multi-server).
- **Cleveland Tennessee Utilities** — city-owned utility entering broadband 2025.
- **City of Holly Springs, NC; City of Fort Collins, CO; Sandy Oregon Net; many more** — pattern of city-owned fiber utilities post-2018.

**North America — Co-op:**
- **Diamond State Networks (DSN)** — Consortium of 13 Arkansas electric co-ops + AECC. **50,000 miles of fiber covering 64% of Arkansas, reaching 1.25M rural Arkansans. $1.66B invested in fiber.** Wholesale broadband + middle-mile + commercial fiber. Canonical large-consortium anchor.
- **OzarksGo, Wave Rural Connect, Four States Fiber, Arkansas Fiber Network** — Diamond State member co-ops; also standalone records.
- **GVTC Communications** — Texas telephone cooperative.
- **Conexon-managed projects** — Conexon is a Co-Mo Connect / Bandwidth & Beyond ISP turnkey vendor; specific managed co-op projects are anchors.
- **CO-MO Connect** — Missouri rural electric co-op fiber.
- **NRTC (National Rural Telecommunications Cooperative)** — federation/buying group, not a fiber operator per se; affiliated with co-op landscape.
- **INDATEL** — 700+ rural ILEC/CLEC consortium. Hybrid Municipal/Cooperative + Dark Fiber Specialist. Members include Ocean Networks (Hawaii, quoted MaiaEdge customer).
- **MBC (Mid-Atlantic Broadband Communities Corporation)** — VA-based middle-mile. **Boundary case** — if purely middle-mile-only, EXCLUDE per file 05; if has commercial-strand wholesale arm, qualify.

**North America — Tribal:**
- **Tribal Digital Village (San Diego County); various tribal broadband authorities (Hopi, Navajo, etc.)** — typically grant-funded; classify Municipal/Cooperative.

**EMEA:**
- **Stadtwerke / Stadtnetz** (Germany municipal utility broadband programs — Stadtwerke München, Mainova, etc.)
- **CityFibre** (UK) — independent wholesale fiber to local authorities, public-private partnerships. Boundary case with Tier 2 National Wholesale (UK-only scale).
- **OpenFiber** (Italy) — partial state-owned via CDP; wholesale-only.

**LATAM/APAC:** Limited canonical anchors; municipal fiber model less prevalent outside US/EU.

### Confusable with
- *Regional CLEC - Fiber operator* — pivot is **ownership structure** (muni/co-op/community-owned vs PE/investor-owned).
- *Regional Cable Operator - Fiber operator* — pivot is **technology origin + ownership** (cable HFC for-profit vs muni/co-op fiber).
- *Dark Fiber Specialist - Fiber operator* — INDATEL-style consortia could be either; classify Municipal/Cooperative for the member-ownership structure, with Dark Fiber Specialist annotation.
- *Middle-mile-only excluded operators* — pivot is **on-demand commercial wholesale arm presence** (yes = qualify; no = exclude).

### Selling angle (MaiaEdge)
"You already operate as a federation — multiple member operators sharing infrastructure with manual coordination at every boundary. MaiaEdge is the operating layer for it. Deterministic provisioning across member operators, open-access partner onboarding in minutes (not the 60-90 day NNI process), and cross-boundary service activation that lets your federation sell commercial wholesale on the commercial strands while BEAD-funded strands stay compliant with grant terms." Two revenue models on the same physical plant, run separately — the federation thesis MaiaEdge is ahead of carrier messaging on.

For BEAD/grant-funded subgrant recipients: "BEAD builds the last mile. MaiaEdge monetizes the middle mile you already own — and lets you commercialize the new builds the moment they're lit."

### HubSpot fields R1/R2 must populate
- `customer_segment` = `Fiber Operator`
- `company_sub_segment` = `Municipal / Cooperative - Fiber operator`
- `segmentation_confidence` = per scoring rules below
- `account_tier` = Tier 2-4 (smaller individual deals; large consortia like Diamond State or UTOPIA push to Tier 1-2)
- `hs_is_target_account` = `true` for consortia and large munis
- `recent_news_or_trigger_event` = F-A1 (BEAD) / F-A9 (consortium) primary triggers
- Free-text fields: ownership structure type (municipal utility / electric co-op / telephone co-op / tribal / consortium), NTCA/NRECA membership, BEAD subgrant amounts, member count for consortia, route miles, customers passed.

### Signal source coverage
- **F-A1 BEAD Subgrant Award** — Highest priority match (Q2-Q4 2026 peak award velocity).
- **F-A9 Consortium / Federation / Co-op Announcement** — Direct match (the sub-segment-specific signal).
- **F-A5 Executive Hire** — Mid-fit (Executive Director, COO at munis/co-ops; CEO at consortia).
- **F-B2 Route Expansion / New-Market Entry** — Direct match (BEAD-funded buildouts in 2025-2026).
- **F-C1 FCC Pole-Attachment Complaints** — Direct match (munis and co-ops file pole complaints frequently).
- **F-B5 Fiber Connect / FTTH Conference Speaker Slots** — Strong fit (consortium / open-access panels).

### Contact personas

**Municipal utility fiber:**
- **CEO / President / Executive Director** (utility leadership)
- **VP Telecommunications / VP Broadband / Director of Fiber Operations**
- **CTO**
- **City Manager** (for city-owned utilities, sometimes on technology committee)

**Electric / Telephone Cooperative:**
- **CEO / General Manager** (small co-ops are CEO-led)
- **COO / VP Broadband Services**
- **CTO / Director of Network Operations**
- **Board Chair / Technology Committee Chair** (member governance)
- **CFO** (grant compliance + capital budget)

**Consortium:**
- **CEO / Managing Member / Co-Managing Members** (Diamond State has co-Managing Members)
- **CTO / VP Network Operations**
- **VP Wholesale / Director of Carrier Services**
- **Member co-op CEOs** (the consortium is governed by its members; individual member CEOs are gatekeepers)

Strongest pattern for consortia: Consortium CEO + 2-3 Member CEOs as a governance buying committee.

### Confidence scoring rules

| Confidence | Trigger |
|---|---|
| `high_90` | NTCA OR NRECA membership verifiable + municipal utility / co-op / consortium ownership structure clear + BEAD or state grant recipient OR open-access platform OR named anchor pattern |
| `medium_7089` | 2 of 3 above |
| `low_5069` | Ownership ambiguous (e.g., quasi-municipal, PPP); OR middle-mile-only with possible commercial arm not yet verified |
| `manual_review_required` | Middle-mile-only operator with unclear commercial arm; INDATEL-style consortia (Dark Fiber Specialist overlap); record is for a member operator vs the consortium parent; PPP structures with mixed public/private capital |

### Industry sources for ongoing validation
- **NTCA member directory** (ntca.org/about-us/our-members)
- **NRECA broadband landscape reports** (electric.coop, cooperative.com)
- **NTIA BEAD Progress Dashboard + state broadband office award lists** (broadbandusa.ntia.gov)
- **Community Networks (communitynetworks.org)** — muni broadband tracker
- **Institute for Local Self-Reliance (ilsr.org)** — muni broadband policy + data
- **NTIA Middle Mile Grant award lists**
- **USDA ReConnect program awards**
- **NRTC (National Rural Telecommunications Cooperative)** — co-op landscape coverage
- **Telecompetitor + Broadband Communities (bbcmag.com)** — regional / co-op operator coverage
- **Fierce Network co-op + muni coverage**
- **Conexon project announcements** (turnkey vendor signals)

---

## Cross-cutting notes for Cooper

### Boundary cases requiring `manual_review_required` policy
1. **Zayo** — Tier 2 National Wholesale (per file 05 canonical resolution) but straddles Long Haul / Backbone. Combined route miles + revenue exceed original Tier 2 upper band; band widened in file 05 to accommodate.
2. **Lumen** — Tier 1 Carrier (Network Op) for parent classification per file 05, but Long Haul / Backbone fits the network infrastructure. Use Tier 1 Carrier for the HubSpot parent record.
3. **Cogent** — Long Haul / Backbone (Fiber) + Pure Wholesale Carrier (Network Op) overlap. Wavelength + IP transit primary. Manual review.
4. **EXA Infrastructure** — Tier 2 National Wholesale (file 05) but transatlantic + subsea also fits International Backbone Specialist. Manual review.
5. **Astound Broadband** — Regional Cable Operator pre-close with `manual_review_required`; will become Cable MSO Enterprise Division Network Op post-GFiber merger close Q4 2026.
6. **Cable ONE / Sparklight** — Regional Cable Operator at $1.7B is borderline with Cable MSO Network Op. Manual review with band-breach annotation.
7. **INDATEL** — Municipal/Cooperative + Dark Fiber Specialist overlap (consortium with dark fiber wholesale role). Manual review.
8. **Consolidated Communications** — Regional CLEC at $3.1B / 23 states / 58,000 route miles is upper edge of Regional CLEC band. Could push to Tier 2 National Wholesale if wholesale book grows. Manual review.

### PE-sponsor dual-lens angle (internal - applies to PE-backed Regional CLEC / Tier 2 National Wholesale / Dark Fiber Specialist records)
For PE-backed operators, MaiaEdge speaks to two buyers with two different lenses, and the pitch should carry both:
- **Sponsor's unit-economics lens:** revenue per existing strand goes up, provisioning OpEx goes down. The sponsor cares that monetization velocity on already-owned fiber improves the asset's return without new capital - directly relevant in a 2026 environment where boards have slowed new builds to protect unit economics.
- **Operator's growth lens:** new sellable services (cloud on-ramp, productized wavelength-on-demand, partner interconnects) plus multi-state reach without a build. The operating team cares about saying yes to multi-state RFPs and winning deals currently lost to slow provisioning.
When the PE sponsor's infrastructure investment director is in the buying committee (the persona stack flags this for $500M+ / PE-backed records), lead the sponsor conversation on the unit-economics lens and the operator conversation on the growth lens. The two are not in tension - both are funded by activating fiber already in the ground.

### Consolidation-rumor caution (internal - mid-2026)
Two consolidation moves are REPORTED / RUMORED as of mid-2026, NOT closed: **Zayo -> Uniti/Windstream** and **T-Mobile -> Kinetic**. Do not treat either as fact in conversation, classification reasoning, or anchor-list edits. If a record references one of these, classify per the current legal state and flag for re-validation, exactly as the pending-M&A policy already requires.

### Anchor changes from file 05 + existing cheatsheet
- **Removed:** Crown Castle Fiber as standalone anchor (acquired by Zayo April 29, 2026, closed May 4, 2026). Confirmed via Zayo press + Crown Castle 8-K + Fierce Network coverage.
- **Removed:** Everstream as standalone Regional CLEC anchor (acquired by Bluebird Fiber March 6, 2026, $384M auction). Reclassified Bluebird Fiber as boundary Regional CLEC / Tier 2 National Wholesale.
- **Added:** Bluebird Fiber post-Everstream (36,000+ route miles, 12 states).
- **Added:** Segra (47,000+ route miles, 17 states, Cox-acquired 2023) to Regional CLEC.
- **Added:** Lightpath FY2025 revenue $468M with $362M AI contracts to Tier 2 National Wholesale.
- **Added:** Uniti+Windstream merged 240,000 route miles, 47 states, $5B revenue to Tier 2 National Wholesale.
- **Added:** Diamond State Networks (13 Arkansas co-ops, 50,000 miles, $1.66B fiber investment, 1.25M rural Arkansans) as canonical Municipal/Cooperative consortium anchor.
- **Added:** FiberLight + Metro Fiber Networks 200-mile Virginia Beach-Richmond dark fiber corridor (April 2025) to Dark Fiber Specialist.
- **Added:** Astound Broadband-GFiber merger flag (announced March 11, 2026; close expected Q4 2026; combined 7.1M passings; will exit Regional Cable Operator post-close per file 05 boundary logic).
- **Added:** Lumen 2025 network expansion (340,000 route miles + 16.6M intercity fiber miles by year-end + 34M new fiber miles by 2028) — anchor for Long Haul / Backbone scale benchmarking.

### Taxonomy gaps revealed
1. **FCC BDC technology codes don't help with wholesale-only operators.** Tier 2 National Wholesale, Long Haul / Backbone, Dark Fiber Specialist all sell to carriers/hyperscalers and don't file BDC (their customers do). Anchor list maintenance for these three relies on Vertical Systems Group Challenge Tier + dgtlinfra Top 200 + trade press M&A coverage rather than regulatory filings.
2. **USAC/FCC RLEC/ILEC/CLEC categories pre-date the wholesale fiber operator category.** Industry consensus on "Tier 2 National Wholesale" is implicit (Vertical Systems Group Challenge Tier serves as the de facto list) but no canonical regulatory bucket exists.
3. **Cooperative / municipal / consortium fragmentation across NTCA, NRECA, NTIA Middle Mile, state broadband offices.** No single directory exists for all Municipal / Cooperative - Fiber operator candidates; anchor list maintenance must cross-reference 4-5 directories.
4. **Greenfield FTTH overbuilders (Tachus, Ting Internet, MetroNet)** don't fit cleanly under "CLEC" terminology despite the structural match. Allow under Regional CLEC with a "fiber overbuilder" annotation in HubSpot reasoning.
5. **The "fiber overbuilder vs cable overbuilder" distinction** is increasingly blurry as cable operators FTTH-overbuild their own footprints (Breezeline doing FTTP buildouts in NH, Cogeco-owned). Origin/parent legacy remains the cleanest pivot.

---

**End of document.**

*File: B-and-C-fiber-operator.md*
*Lines: ~830*
*Validated against: FCC BDC, NTCA, NRECA, NCTA, NTIA BEAD, Vertical Systems Group LEADERBOARD, dgtlinfra Top 125 ISPs + Top 200 Fiber Providers, SEC filings (LUMN, UNIT, CCOI, ATUS, WOW, CABO), Light Reading + Fierce Network + Telecom Ramblings, operator press 2025-2026.*
