# Phase B + C — Network Operator Sub-Segment Deep Dives

**Scope:** Network Operator ICP only. Builds on `05 - Sub-segment definitions for cheatsheets.md` (the v2.1 validated draft, 2026-05-13) and re-validates anchor companies + revenue bands against the most recent industry sources (Vertical Systems Group 2024 Carrier Ethernet Leaderboard, TeleGeography 2025 Submarine Cable Map, Statista Top Telecom 2024, public 10-K / annual reports through Q1 2026, Wikipedia "Tier 1 network" 2025-2026 list). Re-validation pass: 2026-05-14.

**Output target HubSpot internal values (case-sensitive):**
1. `Tier 1 Carrier - Network Op`
2. `Pure Wholesale Carrier - Network Op`
3. `Cable MSO Enterprise Division - Network Op`
4. `International Backbone Specialist - Network Op`

---

## Part B — Industry Taxonomy Alignment for Network Operator

The four MaiaEdge Network Op sub-segments don't map cleanly to any single external industry taxonomy because each public taxonomy slices the market on a different axis (regulatory filings, BGP behavior, wholesale-vs-retail mix, asset class). For accurate classification, the classifier must consult two-three taxonomies and reconcile.

| Taxonomy | Source URL | Structure | MaiaEdge mapping |
|---|---|---|---|
| **FCC Broadband Data Collection (BDC)** | https://help.bdc.fcc.gov/hc/en-us/articles/7682769466395 | Provider categories are *facilities-based fixed broadband*, *facilities-based mobile broadband*, *facilities-based mobile voice*, *fixed voice (including VoIP)*. Filed semi-annually; only facilities-based ISPs file. | **Ambiguous.** BDC doesn't separate wholesale from retail, doesn't capture cable-vs-telco-legacy, and doesn't recognize "international backbone." Tier 1 Carriers, Cable MSO Enterprise Divisions, and many Pure Wholesale Carriers all file as "facilities-based fixed broadband." BDC is useful only as an existence/footprint check, not for sub-segmentation. |
| **PeeringDB Network Type** | https://www.peeringdb.com / docs.peeringdb.com/glossary/ | Categories: NSP, Cable/DSL/ISP, Content, Enterprise, Educational, Non-Profit, Government, Route Server, Route Collector. PeeringDB itself acknowledges definitions are loose. | **Many-to-one.** Tier 1 Carriers + Pure Wholesale Carriers + International Backbone Specialists all self-identify as NSP. Cable MSO Enterprise Divisions tend to register the parent's ASN as Cable/DSL/ISP. PeeringDB confirms an entity is a network operator but does NOT distinguish among our four sub-segments. Use for ASN count, peering density, exchange presence (quantitative markers) — not for sub-segment label. |
| **Wikipedia / BGP "Tier 1 network" list** | https://en.wikipedia.org/wiki/Tier_1_network | Commonly cited as: AT&T (AS7018), Lumen/CenturyLink (AS3356), Verizon (AS701), Cogent (AS174), NTT (AS2914), Tata (AS6453), Sparkle (AS6762), Deutsche Telekom (AS3320), Telia/Arelion (AS1299), Liberty Global / Telxius (AS12956), PCCW (AS3491), Hurricane Electric (AS6939; debated), Zayo (AS6461). Wikipedia maintains a working list but emphasizes no central authority. | **1-to-many.** A single entry on the BGP Tier 1 list maps to multiple MaiaEdge sub-segments: AT&T → Tier 1 Carrier; Cogent → Pure Wholesale Carrier; PCCW → International Backbone Specialist; Tata → International Backbone Specialist (with Pure Wholesale overlap). The "Tier 1" semantic in industry parlance is **BGP routing behavior**, which is orthogonal to MaiaEdge's commercial-segmentation cut. Document this explicitly in the cheatsheet so reps don't confuse "Tier 1 IP transit" with "Tier 1 Carrier - Network Op." |
| **TeleGeography Global Bandwidth / Submarine Cable Map** | https://www.submarinecablemap.com | 597 active or under-construction cable systems + 1,636 landings as of 2025. Lists owners/consortium members per cable. Companies appear as (a) subsea-cable owners/co-owners, (b) terrestrial backbone operators, (c) IP transit providers. | **Ambiguous in one direction, decisive in the other.** Subsea cable co-ownership is a near-deterministic signal for "International Backbone Specialist OR Tier 1 Carrier." But Tier 1 Carriers (AT&T, Verizon, NTT, BT, Telstra) ALSO own subsea cables, so subsea ownership alone doesn't disambiguate. Use TeleGeography to verify the subsea claim in any International Backbone Specialist candidate and to identify hidden subsea positions on Pure Wholesale Carriers. |
| **Vertical Systems Group U.S. Carrier Ethernet Leaderboard** | https://verticalsystems.com/leaderboards/ | 2024 ranks AT&T, Lumen, Spectrum Enterprise, Verizon, Comcast Business, Cox Business as the six providers with ≥4% U.S. retail Ethernet share. Eight Challenge-Tier providers (1-4% share): Altice USA / Lightpath, Cogent, Frontier, Granite, GTT, Windstream, Zayo. | **Many-to-one with one decisive sub-segment.** Comcast Business + Cox Business + Spectrum Enterprise + Optimum Business / Altice = Cable MSO Enterprise Division. AT&T + Verizon + Lumen = Tier 1 Carrier. Cogent + Zayo = Pure Wholesale Carrier (Cogent) and Tier 2 National Wholesale Fiber (Zayo — note this is Fiber Operator segment, not Network Op). Vertical Systems is the single most authoritative source for U.S. Cable MSO Enterprise Division identification. |
| **Capacity Media / Mplify (formerly MEF) Global Carrier rankings** | https://www.capacitymedia.com/global-carrier-awards (Mplify formerly MEF) | Annual Global Connectivity Awards (renamed from Global Carrier Awards 2025). Recognizes Best Global Wholesale Carrier, Best Subsea Operator, Best NaaS Provider categories. Implicit ranking by category. | **Coverage gap.** Capacity ranks by award category, not by sub-segment. International Backbone Specialists are well-covered (Best Subsea, Best Global Wholesale) but the rankings are sparse — only winners and shortlists, not a full census. Use as confirmatory signal, not as primary classifier. |

### Sub-segments we may be missing or have mis-framed

**1. Subsea Cable Operator (pure-play)** — TeleGeography's owner-list reveals a class of operators whose business is **only** subsea cable systems (no terrestrial backbone, no IP transit on top): the consortium-member entities such as Aqua Comms (acquired by EXA Dec 2025), Seaborn Networks, BW Digital, and increasingly hyperscaler subsea SPVs. Currently MaiaEdge folds these into "International Backbone Specialist," but pure-play subsea operators don't have the federation use case — they sell wet-plant capacity, not orchestration-needing services. Recommend Cooper review whether to (a) keep as edge case under International Backbone Specialist with `manual_review_required` default, (b) explicit Non-ICP exclusion, or (c) new sub-segment. The Aqua Comms / Seaborn pattern is increasingly common and the classifier will hit it.

**2. "Mobile-First MNO with token wholesale" sub-segment** — T-Mobile US, Three UK, Vodafone home markets, Rakuten Mobile are primarily retail mobile carriers with a thin wholesale layer. They show up in the Tier 1 Carrier anchor list (Vodafone, T-Mobile parent) but the buying motion is fundamentally different — wholesale and enterprise are not core. Currently no explicit handling; classifier will mis-anchor against the multinational-incumbent-with-wholesale archetype. Recommend Cooper review whether to add a `manual_review_required` trigger for "mobile-revenue >70%" candidates inside Tier 1 Carrier.

**3. Wholesale-only spin-offs of incumbents** — Sparkle (TIM), Telstra International, Bharti Airtel International, Singtel's wholesale book, Telxius (Telefónica), BT Wholesale, Orange Wholesale, T-Wholesale (Deutsche Telekom). These are *divisions* of Tier 1 Carriers that operate as Pure Wholesale or International Backbone. The framework currently handles via "parent ≠ entity in HubSpot" manual-review trigger but doesn't have explicit divisional handling rules. Sparkle's 2026 sale to the Italian state (separating it from TIM) demonstrates the brittleness — the parent-record-vs-division-record collision will keep happening as more incumbents spin out their wholesale arms. Recommend Cooper consider a `wholesale_division_of_tier1` flag or a documented decision rule for these records.

### Reverse-mapping concerns (industry buckets → 2+ MaiaEdge sub-segments)

- **BGP "Tier 1"** → AT&T, Cogent, PCCW, Tata, Lumen all listed. Maps to *Tier 1 Carrier*, *Pure Wholesale Carrier*, *International Backbone Specialist*. **Flag in cheatsheet: BGP Tier 1 ≠ MaiaEdge "Tier 1 Carrier."**
- **PeeringDB NSP** → All three wholesale-ish sub-segments. Use only as existence check.
- **TeleGeography subsea ownership** → Tier 1 Carriers AND International Backbone Specialists. Use as one input, not decisive on its own.
- **FCC BDC facilities-based fixed broadband** → All four Network Op sub-segments + many Fiber Operator sub-segments. Useless for sub-segmenting; useful only for footprint confirmation.

The classifier should treat industry-taxonomy hits as evidence weights, not as labels. Final sub-segment label comes from the deterministic rules in Part C.

---

## Part C — Per-Sub-Segment Deep Dives

---

## Tier 1 Carrier - Network Op

### Definition

The largest national or multinational incumbent carriers. Vertically integrated across retail consumer, retail enterprise, wholesale, and (typically) international wholesale or roaming. State-protected legacy operators in most non-US markets; in the US, the post-Bell-System national carriers and their cable-MSO competitors do NOT belong here (cable MSOs have their own sub-segment). Distinguished from Pure Wholesale Carrier by multi-segment revenue mix (retail + enterprise + wholesale, not wholesale-only), from International Backbone Specialist by retail consumer/enterprise revenue in a home market (Tier 1 Carriers sell consumer mobile; International Specialists don't), and from Cable MSO Enterprise Division by telephone/wireless legacy rather than cable/HFC legacy.

### Quantitative markers (firmographic)

- **Consolidated parent revenue $20B+** (lowered from $30B in original draft; BT at £20.4B / ~$26B FY2025 and Telstra at AU$23B / ~$15B FY2025 are textbook Tier 1 Carriers and would fail a strict $30B test)
- **Multi-segment revenue mix:** retail consumer + retail enterprise + wholesale + (often) international — no single segment >70% of revenue
- **Geographic footprint:** national in home market + meaningful wholesale/enterprise presence in 50+ countries typical; retail in home market + 1-5 adjacent or acquired markets
- **Subsea cable ownership or co-ownership:** typical but not required (AT&T, NTT, BT, Telstra, Orange, DT, Telefónica, Verizon all on TeleGeography owner lists)
- **ASN count:** 10-100+ aggregate across subsidiaries (NTT/AS2914 alone is at scale; multi-subsidiary groups have many more)
- **Employee count:** 50,000+ (typical 80,000-200,000+)
- **Ownership type:** Publicly traded OR state-controlled (China Telecom, China Mobile, China Unicom; Singtel majority Temasek; KDDI public; etc.)
- **Founded:** Pre-1990 typical (legacy incumbent status); US carriers are post-Bell-breakup 1984+; ex-PTT carriers founded as state entities decades earlier

### Required signals (must-have indicators)

- Self-describes on IR / corporate website as "incumbent," "national carrier," "global telecommunications group," or comparable language
- Files annual report (10-K, 20-F, or local equivalent) that breaks out Consumer Mobile, Consumer Wireline / Broadband, Enterprise / Business, AND Wholesale or International as separate reportable segments
- Listed on Statista / GSMA Intelligence "Top Global Telecom" rankings
- Has at least one of: subsea cable co-ownership (verifiable on TeleGeography), Tier 1 IP transit ASN (verifiable on bgp.he.net or Wikipedia), national retail consumer mobile brand
- Appears in Vertical Systems Group U.S. Carrier Ethernet Leaderboard top tier (AT&T, Lumen, Verizon — for U.S. candidates) or equivalent regional ranking (Omdia, Frost & Sullivan, GlobalData)

### Disqualifiers (must-not indicators)

- **No retail consumer business** AND no national wireless brand → Pure Wholesale Carrier or International Backbone Specialist
- **Single-state or sub-national footprint** with no international wholesale presence → Regional CLEC (Fiber Operator) or Cable MSO Enterprise Division
- **Cable / HFC legacy parent** (originally video-cable, not telephone) → Cable MSO Enterprise Division
- **Consolidated revenue under $15B** → too small; check Pure Wholesale Carrier or Cable MSO Enterprise Division
- **Pure subsea-cable owner with no terrestrial network** → Subsea Cable Operator (edge case; flag for Cooper review)

### Anchor companies (15, geographic spread; all re-verified 2026-05-14)

**North America (4):**
- **AT&T** — independent, FY2024 revenue $122.3B. Tier 1 IP transit AS7018, leads Vertical Systems Group 2024 U.S. Carrier Ethernet Leaderboard for 9th consecutive year. Closed acquisition of Lumen's Mass-Markets fiber business Feb 2, 2026 for $5.75B.
- **Verizon** — independent, FY2024 revenue $134.8B. Tier 1 IP transit AS701. Acquiring Frontier Communications (announced 2024, pending close).
- **Lumen Technologies** — independent, FY2025 revenue ~$12.6B (down from $13.1B FY2024 after EMEA divestiture to Colt and consumer FTTH divestiture to AT&T). Tier 1 IP transit AS3356. Borderline — the post-divestiture profile is converging on Pure Wholesale Carrier / large enterprise. Flag for `manual_review_required` review at next quarterly anchor refresh.
- **T-Mobile US** — independent. FY2024 revenue ~$81B. Predominantly retail mobile; thin wholesale. Borderline — mobile-first profile differs from textbook Tier 1 Carrier. See "missing sub-segment #2" in Part B.

**EMEA (4):**
- **BT Group** — independent (UK). FY2025 (ending March 2025) revenue £20.4B (~$26B). Borderline at the $20B threshold but textbook archetype.
- **Deutsche Telekom** — independent. 2024 revenue €115.8B (~$127B). Operates T-Mobile US (separate listing). T-Wholesale / ICSS division for international wholesale.
- **Orange** — independent. 2024 revenue ~€40B (~$44B). Programmable wholesale leader (Sonata-compliant EVPL Online API; 29 countries).
- **Telefónica** — independent. 2024 revenue ~€41B (~$44B). Operates Telxius (subsea wholesale) and consumer brands across Spain + LatAm.

**LATAM (1):**
- **América Móvil** — independent (Carlos Slim-controlled). 2024 revenue ~$54B. Mexico incumbent + LatAm reach. The dominant Tier 1 Carrier across Latin America.

**APAC (4):**
- **NTT Group** — independent. 5th globally by revenue. Tier 1 IP transit AS2914. Subsea owner. NTT's PCF / Private Connectivity Fabric partnership template is referenced explicitly in network-operator.md.
- **KDDI** — independent. 2024 revenue ~$36B. Japan #2 mobile + enterprise + international.
- **Singtel** — Temasek-majority. FY2025 net profit S$4.02B; 100% of NCS (S$732M Q1 FY26 bookings). Singapore incumbent + ASEAN reach.
- **Telstra** — independent. FY2025 (June 2025) revenue AU$23.13B (~$15B). Borderline by $20B threshold but textbook archetype.

**Additional (2):**
- **China Telecom / China Mobile / China Unicom** — state-controlled. Each >$50B revenue. Collapsed as one anchor here for brevity; treat as three separate companies in HubSpot.
- **Vodafone** — independent. FY2025 ~£37B (~$47B). Multi-market European + India (Vi) + Africa (Vantage).

### 2025-26 M&A notes affecting anchors

- **Lumen** completed AT&T Mass-Markets divestiture Feb 2026; EMEA divestiture to Colt closed 2024. Post-divestiture profile is now enterprise + wholesale + AI; consumer is gone. Sub-segment classification trend: drifting toward Pure Wholesale Carrier. Flag at next quarterly review.
- **Verizon-Frontier** announced 2024; expected close 2025-26. Doesn't change Verizon's sub-segment.
- **AT&T** acquiring Lumen consumer FTTH closed Feb 2026; doesn't change AT&T's sub-segment.

### Confusable-with comparison

- **vs Pure Wholesale Carrier:** Tier 1 Carrier has retail consumer mobile or retail consumer broadband; Pure Wholesale is wholesale-only with no retail consumer. Decisive tell: 10-K segment breakouts.
- **vs International Backbone Specialist:** Tier 1 Carrier has dominant home-market retail; International Backbone Specialist's revenue is >60% international wholesale with no meaningful home-market retail. Decisive tell: is the company the dominant telco in a single country (Tier 1) or is it an international wholesale specialist (International Backbone)?
- **vs Cable MSO Enterprise Division - Network Op:** Tier 1 Carrier's legacy is telephone or wireless; Cable MSO's legacy is cable/HFC video. Decisive tell: company history page or Wikipedia origin description.
- **vs Tier 2 National Wholesale - Fiber operator (cross-segment):** Tier 2 National Wholesale is fiber-only, wholesale-only, no consumer mobile. Decisive tell: presence of consumer mobile brand or retail mobile in 10-K.

### Selling angle (MaiaEdge)

Operational scale to negotiate with hyperscalers as equals. Position MaiaEdge as the fabric layer between their footprint and the hyperscalers their enterprise customers are buying from — NOT as a competitor to their own backbone. Reference NTT's PCF partnership template. For Track A (programmable wholesale live in production — Orange, DT, PCCW, NTT, Tata): "your team extends that automation beyond your borders without rebuilding." For Track B (US Tier 1s — Verizon, AT&T pre-PCF, T-Mobile): "your team gets to where Orange and NTT already are without a 3-year build." Pair speed with ownership ("your team provisions in minutes"), never speed alone.

### HubSpot fields R1/R2 must populate

**Required (diagnostic):**
- `customer_segment` = `Network Operator(Tier 1 / VNO)`
- `company_sub_segment` = `Tier 1 Carrier - Network Op`
- `annualrevenue` (must hit $20B+ band)
- `country` (must be a country with $20B+ telco market for archetype match)
- `network_op_track` (`external_extension` = Track A; `internal_external_unification` = Track B)
- `account_tier` (Tier 1 default for this sub-segment; downshift only if active engagement is dead)

**Recommended:**
- `numberofemployees` (50,000+ band)
- `recent_news_or_trigger_event` (PCF / NaaS / executive transition / earnings keyword)
- `web_technologies` if accessible (Mplify Sonata adopter list, GSMA Open Gateway list)
- `account_brief` (free-text strategy summary)

### Signal source coverage

**Tier A (Robust):**
- Company IR / newsroom direct (Lumen, AT&T, Verizon, BT, DT, Orange, Telefónica, NTT, Tata, Singtel, Telstra, KDDI, América Móvil)
- SEC 8-K / 10-K / 20-F via StockTitan + EDGAR
- Vertical Systems Group U.S. Carrier Ethernet Leaderboard (annual)
- Statista Top Telecom Companies
- GSMA Intelligence operator database
- Fierce Network, Light Reading, TelecomTV, Capacity Media (international primary)
- GitHub commit feeds for CAMARA / Nephio / ONAP authors @<carrier.com>

**Tier B (Medium):**
- TM Forum AN registry
- Mplify (MEF) Sonata-conformance registry
- Capacity Awards / Global Connectivity Awards shortlists

**Coverage gaps:**
- Private + state-controlled carriers (China Telecom/Mobile/Unicom, KDDI partial) — disclose less. Use 20-F if ADR-listed; otherwise relies on industry rankings.
- Mobile-first carriers (T-Mobile US) — wholesale signals are thin and don't reliably trigger.

### Contact personas (specific titles)

**Technical Champion:**
- VP Network Strategy
- VP Network Architecture / SVP Network Architecture
- Principal Network Architect / Distinguished Engineer / Chief Architect
- VP Transport / VP IP & Transport
- VP Wholesale Platforms / VP Programmable Network

**Business Sponsor:**
- VP Wholesale / SVP Wholesale
- VP Enterprise / SVP Business Markets
- VP Product (Wholesale or NaaS product)
- Chief Product Officer / Chief Product & Strategy Officer
- VP Business Development

**Economic Buyer:**
- CTO / Chief Technology Officer
- CNO / Chief Network Officer
- CIO (rare for this segment; more common in mobile-first Tier 1s)
- CTrO / Chief Transformation Officer (when present — 12-18 month charter)
- CDO / Chief Digital Officer (when present)
- COO (in carriers where COO owns network)

**Procurement:**
- VP Strategic Sourcing
- VP Network Procurement / Director of Network Procurement
- Procurement Lead, Transformation Programs
- Vendor Management Lead
- Chief Procurement Officer (for >$100M deals)

### Confidence scoring rules (deterministic)

- **high_90:** Anchor match OR near-twin (revenue ≥$20B, multi-segment 10-K breakouts, founded pre-1990 as national incumbent OR post-1984 Bell descendant) + ≥4 quantitative markers met + ≥2 required signals (10-K segment + at least one of subsea / Tier 1 BGP / national retail mobile) + 0 disqualifiers
- **medium_7089:** ≥3 quantitative markers + ≥1 required signal + 0 disqualifiers
- **low_5069:** ≥2 quantitative markers OR partial signal evidence (e.g., revenue band met but multi-segment evidence weak)
- **manual_review_required:** Lumen (post-divestiture trend toward Pure Wholesale Carrier); T-Mobile US (mobile-first profile); cable parent of a national carrier (Charter-Cox combined entity will need this); Bharti Airtel parent record (India retail vs International Backbone overlap); pending close of large M&A (Charter-Cox combined when closes); revenue >2x or <50% of $20B band; parent ≠ HubSpot record name + brand straddles multiple sub-segments

### Industry sources for ongoing validation

- Statista Top Telecom Companies (annual, January release)
- Vertical Systems Group U.S. Carrier Ethernet Leaderboard (annual, February release)
- GSMA Intelligence operator database (continuous)
- Public 10-K / 20-F / annual report filings (annual)
- Wikipedia "Tier 1 network" article (continuous; reference, not authority)
- TeleGeography Submarine Cable Map (annual May release)
- Capacity Media Global Connectivity Awards (annual)
- Fierce Network + Light Reading + TelecomTV (continuous)

---

## Pure Wholesale Carrier - Network Op

### Definition

Wholesale-only carriers that sell capacity, IP transit, ports, and dedicated connectivity to other carriers, hyperscalers, and large enterprises — and do NOT sell to consumers or small business. Often spun out from larger carriers (Arelion from Telia, EXA from GTT InfraCo, Sparkle from Telecom Italia) or built as wholesale-first plays (Hurricane Electric, Cogent — though Cogent has a corporate DIA book that bends the literal definition). Distinguished from Tier 1 Carrier by absence of consumer retail; from International Backbone Specialist by meaningful domestic / regional wholesale presence (not exclusively international); from Tier 2 National Wholesale - Fiber Operator by IP-transit / Tier 1 routing as primary product (the Fiber Operator analog leads with dark fiber and lit transport).

### Quantitative markers (firmographic)

- **Revenue $100M-$5B** (widened from original $200M-$5B; Hurricane Electric is the canonical sub-$200M anchor and the segment definitionally accommodates it)
- **100% B2B / B2B2x:** no retail consumer, no SMB direct sales except corporate DIA (Cogent's case)
- **BGP Tier 1 OR markets as Tier 1 IP transit** (verifiable on bgp.he.net peering tables; Wikipedia's working list; per FastNetMon and Macronet Services 2025 industry references)
- **Anchor wholesale customers:** other carriers, hyperscalers (Meta, Google, AWS), large enterprises, CDNs, large ISPs
- **Geographic footprint:** national US OR pan-European OR multi-regional (US-EU-APAC)
- **Route miles:** 30,000-300,000 fiber typical (Arelion ~77,000 km / 47,800 mi; Cogent metro+long-haul ~90,000 mi)
- **Employee count:** 200-5,000
- **Ownership:** Often PE-owned (EXA = I Squared; Arelion = Polhem Infra) OR publicly traded (Cogent NASDAQ)

### Required signals (must-have indicators)

- "Wholesale" or "carrier" or "global IP transit" in headline marketing language on the corporate site
- AS-level evidence of Tier 1 routing OR Tier 2 transit with paid customers (verifiable via PeeringDB + bgp.he.net)
- Customer references / case studies are carriers, hyperscalers, CDNs — not consumers or SMB
- 10-K / annual report (if public) breaks out service categories like "IP transit," "wavelength," "Ethernet," "dark fiber" rather than "consumer wireless," "consumer broadband"
- Appears on Capacity Media Global Connectivity Awards shortlists OR Vertical Systems Group Challenge Tier

### Disqualifiers (must-not indicators)

- Has consumer retail or national mobile brand → Tier 1 Carrier
- Revenue under $50M with sub-state-level footprint → too small; check Regional CLEC or Dark Fiber Specialist
- Single-state or sub-national footprint → Regional CLEC - Fiber Operator
- Primary identity is subsea cable owner with no terrestrial backbone → Subsea Cable Operator edge case
- Primarily dark fiber + lit wavelength (no IP transit) → Tier 2 National Wholesale - Fiber Operator (cross-segment to Fiber Operator)

### Anchor companies (12, geographic spread; all re-verified 2026-05-14)

**North America (5):**
- **Cogent Communications** — independent, NASDAQ-listed. FY2025 service revenue $975.8M (down from $1.04B FY2024). Tier 1 BGP AS174. Note: also sells corporate DIA direct to SMB/mid-market — not "pure" by literal reading but industry-classified as Pure Wholesale.
- **Hurricane Electric** — independent, privately held. Revenue undisclosed but estimated $100-200M (one source mentions $750M FY2024 — likely refers to a different company; treat with caution). Tier 1 BGP AS6939, 10,000+ BGP sessions, 280+ IX presence, 336+ exchange points. Canonical Tier 1 IP transit pure-play.
- **Zayo Group** — DigitalBridge-owned. Note: post-Crown Castle Fiber acquisition (closed April 2026), Zayo's profile is shifting toward Fiber Operator (Tier 2 National Wholesale). Vertical Systems 2024 Challenge Tier. In MaiaEdge taxonomy, Zayo classifies as `Tier 2 National Wholesale - Fiber operator` (Fiber Operator segment), NOT Pure Wholesale Carrier. Mentioned here only as confusable.
- **GTT Communications (legacy)** — substantially shrunk post-2021 sale of InfraCo to I Squared (now EXA Infrastructure). Today functions more as Managed Network Services. Borderline; if HubSpot record exists, default to `manual_review_required`.
- **Crosslake Fibre / Aqua Comms / Seaborn Networks** — niche subsea-only operators; flag as Subsea Cable Operator edge case (see Part B missing #1).

**EMEA (3):**
- **Arelion** (formerly Telia Carrier) — Polhem Infra-owned since June 2021. Revenue ~€600M (2024 estimate; not publicly disclosed since privatization). AS1299 (Tier 1 BGP). Network ~77,000 km across Europe, North America, Asia. Acquired by Polhem from Telia for $935M (€935M).
- **EXA Infrastructure** — I Squared Capital-owned (acquired GTT InfraCo for $2.15B Sept 2021). 170,000 km fiber in 37 countries. Acquired Aqua Comms Dec 31, 2025. €1.3B refinancing Oct 2025. Borderline with International Backbone Specialist; classify by primary revenue source (EXA: terrestrial-heavy → Pure Wholesale Carrier).
- **Sparkle (TIM)** — pending sale to Italian state (Retelit consortium) for €700M; EU approval April 13, 2026; close expected H1 2026, long-stop date Oct 15, 2026. Revenue ~€1B. 600,000+ km fiber + subsea. Borderline with International Backbone Specialist; primary classification depends on post-close ownership and operating model.

**LATAM (2):**
- **Liberty Networks** (Cable & Wireless Networks brand for B2B in LatAm/Caribbean) — Liberty Latin America subsidiary. ~50,000 km subsea + 17,000 km terrestrial across 30+ countries; 96 PoPs; owns ARCOS-1, CFX, ECFS, PCCS, MAYA-1.2 cable systems; building MANTA pan-regional system.
- **Cirion Technologies** — Stonepeak-owned (acquired from Lumen 2022 for $2.7B). Pan-LATAM wholesale + enterprise. Borderline Tier 1 Carrier candidate for LATAM markets; flag for `manual_review_required`.

**APAC (2):**
- **Console Connect** — owned 80% Infratil + 20% HKT initially announced 2024 for $160M; deal **cancelled October 31, 2024**. Console Connect remains an HKT subsidiary. Top-10 Tier 1 BGP. Revenue undisclosed; Infratil's pre-cancellation deck projected EBITDA US$40-50M FY2025.
- **NTT Communications** (the wholesale arm specifically) — division of NTT Group; AS2914. Listed here for completeness; in HubSpot the parent NTT record is Tier 1 Carrier and the wholesale subsidiary is a divisional record (handle with `manual_review_required`).

### 2025-26 M&A notes affecting anchors

- **Cogent** revenue declining FY2024→FY2025; sub-segment classification unchanged but watch for further drift.
- **Sparkle** pending sale to Italian state Q3-Q4 2026; post-close, Sparkle's parent shifts from Telecom Italia to Italian state (MEF-Retelit consortium). Sub-segment classification stable but parent-entity changes; flag HubSpot record at close.
- **EXA Infrastructure** acquired Aqua Comms Dec 31, 2025 — strengthens subsea position, may push EXA toward International Backbone Specialist classification.
- **GTT Communications** — substantial restructure post-2021; classification trending toward Managed Network Services rather than Pure Wholesale.
- **Console Connect / Infratil** deal cancelled — Console Connect remains HKT-owned.

### Confusable-with comparison

- **vs Tier 1 Carrier:** Pure Wholesale has no consumer retail; Tier 1 Carrier does. Decisive tell: presence of consumer mobile / consumer broadband brand in 10-K segments.
- **vs International Backbone Specialist:** Pure Wholesale has meaningful domestic / regional wholesale presence; International Backbone is 60%+ international. Decisive tell: revenue geography breakout.
- **vs Tier 2 National Wholesale - Fiber operator (cross-segment):** Pure Wholesale is IP-transit / Tier 1 routing primary; Tier 2 National Wholesale is dark fiber + lit transport primary. Decisive tell: corporate site headline product (does it lead with "IP transit / global IP backbone" or "dark fiber / wavelengths / lit transport"?). Zayo and Cogent sit on opposite sides of this boundary.
- **vs Long Haul / Backbone - Fiber operator:** Long Haul / Backbone is primarily dark-fiber on long routes; Pure Wholesale is lit IP transit primary.

### Selling angle (MaiaEdge)

Their margin is wholesale spread. Position MaiaEdge as inventory that improves their customer-facing fabric without touching their core backbone. "We give your customers a private path on top of your transit, and you keep the relationship — they buy fabric experience from us through you." For carriers selling Tier 1 IP transit, the upsell story is: "your wholesale customers want orchestration on top of routes they already get from you; we deliver that without you having to build it." Pair speed with ownership.

### HubSpot fields R1/R2 must populate

**Required (diagnostic):**
- `customer_segment` = `Network Operator(Tier 1 / VNO)`
- `company_sub_segment` = `Pure Wholesale Carrier - Network Op`
- `annualrevenue` ($100M-$5B band)
- `country` (HQ; expect primarily US, UK, Sweden, Italy, Hong Kong, Singapore, Mexico, Brazil)
- `network_op_track` (most are Track A — already have meaningful internal automation, especially the European ones)
- `account_tier` (Tier 1 or Tier 2 by deal-size potential)

**Recommended:**
- `numberofemployees`
- `recent_news_or_trigger_event`
- ASN list (free-text in account brief if not a property)
- `web_technologies` if accessible

### Signal source coverage

**Tier A (Robust):**
- Company IR / newsroom (Cogent, Arelion, EXA, Sparkle, Liberty Networks, Cirion, Console Connect)
- SEC filings via StockTitan (Cogent only — most are private)
- PeeringDB + bgp.he.net (ASN, peering density)
- TeleGeography (subsea cable ownership)
- Vertical Systems Group Challenge Tier listings (Cogent, Zayo)
- Capacity Media Global Connectivity Awards shortlists (Best Global Wholesale Carrier category)
- Fierce Network, Light Reading, TelecomTV, Capacity Media

**Tier B (Medium):**
- Mplify Sonata-conformance registry
- PE-firm portfolio pages (DigitalBridge, I Squared, Polhem Infra, Stonepeak, Infratil)
- Wikipedia "Tier 1 network" article

**Coverage gaps:**
- Most Pure Wholesale Carriers are privately held → no SEC filings → financial data is estimate-heavy
- Hurricane Electric particularly opaque (no public revenue)
- Smaller regional pure-wholesale players (sub-$50M) tend not to show up in industry rankings

### Contact personas (specific titles)

**Technical Champion:**
- VP Engineering / VP Network Engineering
- VP IP & Transport
- Principal Network Architect
- Director of Peering / Head of Peering
- Director of Network Operations

**Business Sponsor:**
- VP Sales / SVP Sales
- VP Carrier Sales / VP Wholesale
- VP Product / VP Product Management
- Head of Hyperscaler Sales
- Head of CDN Sales

**Economic Buyer:**
- CEO (in $100M-$500M revenue companies, CEO is often the buyer)
- CTO
- COO
- CFO (for >$1M annual deals)

**Procurement:**
- VP Procurement / Director of Procurement
- Director of Vendor Management
- Strategic Sourcing Lead
- Note: smaller wholesale carriers often don't have dedicated procurement; deals run through CTO or CFO

### Confidence scoring rules (deterministic)

- **high_90:** Anchor match OR near-twin (wholesale-only revenue mix verified, BGP Tier 1 or Tier 2 transit role confirmed via PeeringDB, ≥$100M revenue band, no consumer retail) + ≥4 quantitative markers + ≥2 required signals + 0 disqualifiers
- **medium_7089:** ≥3 quantitative markers + ≥1 required signal + 0 disqualifiers
- **low_5069:** ≥2 quantitative markers OR partial evidence (e.g., wholesale-positioning language present but ASN evidence weak)
- **manual_review_required:** Lumen (drifting from Tier 1 Carrier toward this sub-segment); Cogent (corporate DIA bends the wholesale-only definition); Sparkle pending sale; EXA Infrastructure post-Aqua Comms acquisition (drifting toward International Backbone Specialist); GTT Communications (drifting toward MNS); Cirion (borderline Tier 1 Carrier candidate for LATAM)

### Industry sources for ongoing validation

- Wikipedia "Tier 1 network" article (continuous; reference)
- bgp.he.net Hurricane Electric BGP toolkit (continuous)
- PeeringDB (continuous)
- TeleGeography 2025 Submarine Cable Map (annual May)
- Capacity Media Global Connectivity Awards (annual)
- Vertical Systems Group Challenge Tier (annual)
- DigitalBridge, I Squared, Polhem Infra, Stonepeak portfolio pages (continuous)
- FastNetMon and Macronet Services Tier 1 ISP working lists (continuous; reference)

---

## Cable MSO Enterprise Division - Network Op

### Definition

The business / enterprise / commercial fiber arm of a cable parent company. Cable parents built for residential video and broadband; the B2B division grew out of that HFC + fiber infrastructure to serve SMB, mid-market, and increasingly enterprise. The enterprise arm is what MaiaEdge sells to — NOT the residential cable parent. Distinguished from Tier 1 Carrier by cable / HFC legacy (vs telephone or wireless legacy); from Regional Cable Operator - Fiber Operator by SCALE (national or near-national, $1.5B+ B2B revenue, not regional sub-$1B); from Tier 2 National Wholesale - Fiber Operator by retail/direct-enterprise sales model (Cable MSO Enterprise sells direct to enterprise, not wholesale via carriers).

### Quantitative markers (firmographic)

- **B2B revenue $1.5B+ (the division, not the parent)** (lowered from $5B+ in early drafts; Cox Business at ~$3-4B and Optimum Business at ~$1.5B are unambiguous Cable MSO Enterprise Divisions by industry consensus)
- **Parent operates residential cable in 10+ states OR is national in home country** (Comcast 39 states, Charter 41 states post-Cox close, Cox 18 states pre-merger)
- **Network footprint:** 5,000+ route miles of fiber + extensive HFC plant
- **Sells:** dedicated fiber, Ethernet (Carrier Ethernet ports), MPLS, SD-WAN, dedicated internet (DIA), managed firewall, increasingly cloud connect / managed cloud
- **Distinct brand and (usually) distinct sales org from residential parent** ("Comcast Business" / "Spectrum Enterprise" / "Cox Business" / "Optimum Business")
- **Employee count:** B2B division 5,000-15,000; parent total 25,000-90,000+
- **Ownership:** parent is publicly traded (Comcast, Charter pre-merger, Cable ONE) OR privately held by founding family (Cox)

### Required signals (must-have indicators)

- Distinct business-services brand and corporate URL (business.comcast.com, enterprise.spectrum.com, coxbusiness.com, optimum.com/business)
- Appears in Vertical Systems Group U.S. Carrier Ethernet Leaderboard (Comcast Business, Spectrum Enterprise, Cox Business all on 2024 list with ≥4% retail Ethernet share; Optimum/Altice in Challenge Tier with Lightpath bundled)
- 10-K (where parent is public) breaks out "business services" or "commercial" revenue separately
- Self-describes as "business services" / "enterprise" / "commercial fiber" / "Ethernet services"
- Parent has clear residential cable + broadband history (cable / HFC legacy)

### Disqualifiers (must-not indicators)

- Regional / single-state cable parent with B2B <$1B → Regional Cable Operator - Fiber operator (cross-segment to Fiber Operator)
- No residential cable / HFC parent history (originally telephone, wireless, or fiber-only) → Tier 1 Carrier or Tier 2 National Wholesale - Fiber Operator
- Pure business-only / no residential history → Fiber Operator segment
- Cable parent operates only in 1-2 small markets → Regional Cable Operator - Fiber Operator
- Wholesale-only book → not Cable MSO Enterprise Division (cable parents very rarely run pure-wholesale wholesale)

### Anchor companies (5, US-centric by definition; all re-verified 2026-05-14)

**North America (Cable MSO Enterprise Division is overwhelmingly a North American phenomenon — Europe and APAC do not have cable-MSO ecosystems at this scale):**

- **Comcast Business** — division of Comcast Corporation (NASDAQ: CMCSA). 2024 revenue **$9.7B** (per TBR via Lightwave), nearing the $10B long-term target. Ranks #5 on Vertical Systems Group 2024 U.S. Carrier Ethernet Leaderboard (top 4% retail Ethernet). Also ranks #1 on Vertical Systems Group 2024 U.S. SD-WAN Leaderboard. Independent (parent is independent).
- **Spectrum Enterprise** — division of Charter Communications (NASDAQ: CHTR). Estimated 2024 revenue $7-9B (Charter does not break out enterprise separately on 10-K; estimate from industry analysts). Ranks #3 on Vertical Systems Group 2024 U.S. Carrier Ethernet Leaderboard. **Pending Charter-Cox merger** announced May 16, 2025 at $34.5B; FCC approval late Feb 2026; close expected mid-2026. Post-close, the combined Spectrum Enterprise + Cox Business book becomes the largest Cable MSO Enterprise Division in the US.
- **Cox Business** — division of Cox Communications (subsidiary of Cox Enterprises, privately held). Parent 2024 revenue $13.1B (Cox Communications standalone). B2B division estimated ~$3-4B (not broken out separately). Ranks #6 on Vertical Systems Group 2024 U.S. Carrier Ethernet Leaderboard. **Pending Charter merger** (see above).
- **Optimum Business** — Altice USA (NYSE: ATUS). Q1 2024 Business Services revenue $364.9M; Q2 $369.3M; FY2024 estimated ~$1.5B. **Note:** Altice USA includes Lightpath as a separate B2B fiber brand (~$300-400M, sibling brand under Altice). Optimum Business + Lightpath bundled appear in Vertical Systems Challenge Tier (1-4% retail Ethernet).
- **Cable ONE / Sparklight Business** — Cable ONE (NYSE: CABO). 2024 revenue ~$1.7B (parent total). B2B portion sub-$300M. Borderline — at the small end of Cable MSO Enterprise Division; could be classified as Regional Cable Operator - Fiber Operator depending on B2B-revenue cut. Default to `manual_review_required` per revenue-band breach rule.

### 2025-26 M&A notes affecting anchors

- **Charter-Cox merger** announced May 2025; FCC approved Feb 27, 2026; expected close mid-2026. Post-close, Spectrum Enterprise + Cox Business combine. Within a year of close, the merged company renames to Cox Communications but retains "Spectrum" as consumer-facing brand. Sub-segment classification of the merged company unchanged (Cable MSO Enterprise Division - Network Op) but two anchor records collapse to one. Flag for HubSpot record consolidation at close.
- **Comcast Business** — no M&A activity affecting anchor status. Approaching $10B target.
- **Altice USA / Optimum** — no major M&A 2025-26, but balance sheet stress + ongoing divestiture rumors. Watch for spinoff or sale of Optimum Business or Lightpath.

### Confusable-with comparison

- **vs Regional Cable Operator - Fiber operator (cross-segment to Fiber Operator):** SCALE test. National multi-state with $1.5B+ B2B → Cable MSO Enterprise Division. Regional / sub-national / <$1B B2B → Regional Cable Operator. Decisive tell: state count of residential cable footprint AND broken-out B2B revenue.
- **vs Tier 1 Carrier - Network Op:** Parent legacy. Cable / HFC video legacy → Cable MSO. Telephone or wireless legacy → Tier 1 Carrier. Decisive tell: Wikipedia company history paragraph one.
- **vs Tier 2 National Wholesale - Fiber operator:** Sales model. Cable MSO sells direct to enterprise; Tier 2 National Wholesale sells via carriers. Decisive tell: 10-K customer-mix breakout; presence of "wholesale" segment.

### Selling angle (MaiaEdge)

Cable MSO B2B arms compete with Tier 1 incumbents (AT&T Business, Verizon Business, Lumen) for the same mid-market and enterprise customers but with a structural disadvantage on multi-state Tier 1 enterprise routing. They have national presence but the network is HFC + regional fiber, not nationwide long-haul. Position MaiaEdge as the gap-filler: "extend your footprint to anywhere your enterprise customers need without negotiating with your competitors." For SD-WAN-led customers (Comcast Business leads Vertical Systems 2024 SD-WAN ranking): "your SD-WAN customers want private cloud paths under the overlay; we deliver the underlay fabric so you keep the customer relationship and the bill." Pair speed with ownership.

### HubSpot fields R1/R2 must populate

**Required (diagnostic):**
- `customer_segment` = `Network Operator(Tier 1 / VNO)`
- `company_sub_segment` = `Cable MSO Enterprise Division - Network Op`
- `annualrevenue` ($1.5B+ B2B division revenue; if parent total is used, $3B+ floor)
- `country` (overwhelmingly US; Canada has Rogers Business + Bell Canada Business but those are typically classified as Tier 1 Carrier)
- `network_op_track` (Cable MSOs trend Track B — internal automation fragmented across HFC + acquired-fiber + cable-system boundaries)
- `account_tier` (Tier 1 or Tier 2 by enterprise-deal potential)

**Recommended:**
- `numberofemployees`
- `recent_news_or_trigger_event` (Charter-Cox close, AT&T-Comcast / AT&T-Verizon competitive moves, BEAD wins)
- `account_brief`
- Parent company name and HubSpot parent-record association

### Signal source coverage

**Tier A (Robust):**
- Parent company IR / 10-K (Comcast, Charter, Altice USA, Cable ONE)
- Vertical Systems Group U.S. Carrier Ethernet Leaderboard (annual February)
- Vertical Systems Group U.S. SD-WAN Leaderboard (annual April)
- Vertical Systems Group U.S. Fiber Lit Buildings Leaderboard (annual May)
- Fierce Network, Light Reading, Lightwave Online
- dgtlinfra top 125 ISPs list

**Tier B (Medium):**
- NCTA member directory (cable industry trade group)
- Leichtman Research Group cable subscriber reports
- TBR (Technology Business Research) carrier coverage

**Coverage gaps:**
- Cox Business (parent privately held; B2B not broken out)
- Spectrum Enterprise (B2B not separately disclosed in Charter 10-K)
- Pre-IPO or sub-Cable ONE-tier MSOs (Atlantic Broadband / Breezeline, etc.) — these fall to Regional Cable Operator - Fiber Operator anyway

### Contact personas (specific titles)

**Technical Champion:**
- VP Engineering, Business / VP Engineering, Enterprise
- VP Network Architecture (Business)
- Principal Network Architect, Enterprise
- Director of Network Engineering, Commercial
- VP Technology, Business Services

**Business Sponsor:**
- President, Comcast Business / Spectrum Enterprise / Cox Business / Optimum Business
- SVP Sales, Enterprise / SVP Enterprise Sales
- VP Product Management, Business / VP Product, Enterprise
- VP Marketing, Business Services
- VP Strategic Partnerships, Business

**Economic Buyer:**
- President, Business Services (the divisional president is often the economic buyer)
- CFO, Parent (for >$5M annual deals)
- COO, Business Services
- CEO, Parent (rare — only for transformational deals)

**Procurement:**
- VP Strategic Sourcing
- Director of Procurement, Network and IT
- Director of Vendor Management, Business Services
- Chief Procurement Officer (parent-level, for >$10M deals)

### Confidence scoring rules (deterministic)

- **high_90:** Anchor match (Comcast Business, Spectrum Enterprise, Cox Business, Optimum Business) OR near-twin (cable parent national in residential, B2B division $1.5B+, distinct brand, Vertical Systems Leaderboard or Challenge Tier) + ≥4 quantitative markers + ≥2 required signals + 0 disqualifiers
- **medium_7089:** ≥3 quantitative markers + ≥1 required signal + 0 disqualifiers
- **low_5069:** ≥2 quantitative markers OR partial evidence
- **manual_review_required:** Charter-Cox combined entity at close (record consolidation); Cable ONE / Sparklight (revenue-band borderline); cable MSO with wholesale fiber book (Comcast Wholesale, Lightpath as a sibling to Optimum); cable parent with international expansion; Altice USA strategic events

### Industry sources for ongoing validation

- Vertical Systems Group Leaderboards (Carrier Ethernet, SD-WAN, Fiber Lit Buildings — three separate annual releases)
- Public 10-K filings (Comcast, Charter, Altice USA, Cable ONE)
- dgtlinfra top 125 ISPs (continuous, periodic updates)
- NCTA cable industry data (continuous)
- Fierce Network cable + broadband coverage
- Light Reading cable coverage

---

## International Backbone Specialist - Network Op

### Definition

Carriers whose primary business is international long-haul / backbone connectivity. Typically own or co-own subsea cable systems and serve as the anchor between major continents (US-EU, EU-APAC, APAC-Americas, Indian Ocean, Mediterranean). May or may not have meaningful retail in any single country, but commercial language and revenue mix is international-first. Industry sometimes calls these "international wholesale carriers" or "global long-haul operators." Distinguished from Tier 1 Carrier by absence of dominant home-market retail (International Backbone Specialists are wholesale-first and international-first); from Pure Wholesale Carrier by international primacy (Pure Wholesale has meaningful domestic / regional wholesale; International Backbone is 60%+ international); from a pure-play Subsea Cable Operator (edge case) by having terrestrial backbone + IP transit on top of the subsea (not subsea-only).

### Quantitative markers (firmographic)

- **Revenue $100M-$5B** (widened from $500M-$5B; HGC at $258M historic / $750M FY2024 and Epsilon at $50-100M are textbook fits at the low end)
- **HQ outside the US OR markets itself primarily as an international connectivity provider** (HQ in US is rare for this archetype; the major US international carriers like AT&T Global Network Services are part of Tier 1 Carrier records)
- **Subsea cable ownership or major IRU positions on multiple cable systems** (verifiable on TeleGeography 2025 Submarine Cable Map; 597 active or under-construction systems with owner data)
- **Geographic revenue split:** 60-80% from international (cross-border) routes (proxy if 10-K not available: HQ + international-only marketing language + customer references that are other international carriers and global enterprises)
- **Tier 1 IP transit with global routing presence** (verifiable on bgp.he.net peering tables)
- **Route miles / KM:** 50,000-700,000+ fiber (PCCW Global 738,000 km; Tata 500,000+ km subsea; Sparkle 600,000+ km; HGC 1,500+ km in Philippines alone)
- **Employee count:** 500-5,000
- **Ownership:** Often a division of a Tier 1 Carrier (Telstra International, Bharti Airtel International, BT Global, Orange Wholesale International, Deutsche Telekom Global Carrier, NTT Communications international, Sparkle pre-divestiture) OR independent (Epsilon, Console Connect, HGC), OR PE-owned (EXA Infrastructure)

### Required signals (must-have indicators)

- Self-describes as "global wholesale," "international wholesale," "international carrier," or "global connectivity"
- Subsea cable ownership or co-ownership verifiable on TeleGeography Submarine Cable Map
- Customer references / case studies are other international carriers, global enterprises, hyperscalers
- Wholesale-product catalog includes wavelengths, IP transit, international Ethernet, and (often) network-as-a-service or platform-style products (Console Connect's NaaS, Tata's IZO, PCCW Global's CC platform)
- Appears on Capacity Media Global Connectivity Awards shortlists in Best Subsea Cable Operator, Best Global Wholesale Carrier, or Best International Carrier categories

### Disqualifiers (must-not indicators)

- Domestic-first business with >70% home-country revenue → not International Backbone Specialist; check Tier 1 Carrier or Pure Wholesale Carrier
- No subsea cable ownership AND no major IRU positions → unlikely true International Specialist (verify on TeleGeography; if absent, drop)
- Single continent or single region → that's a regional pure-wholesale operator, not International Backbone Specialist
- Pure subsea-cable owner with no terrestrial backbone → Subsea Cable Operator edge case (see Part B missing #1)
- Primarily mobile / consumer retail → Tier 1 Carrier

### Anchor companies (10, geographic spread; all re-verified 2026-05-14)

**International Backbone Specialists are by definition non-US-centric; very few HQ in the US. Geographic split therefore biases EMEA + APAC.**

**EMEA (4):**
- **EXA Infrastructure** — I Squared-owned, HQ London. 170,000 km fiber in 37 countries connecting Europe + North America. Acquired Aqua Comms Dec 31, 2025 (transatlantic subsea). €1.3B refinancing Oct 2025. Borderline with Pure Wholesale Carrier (current draft classifies as Pure Wholesale due to terrestrial-heavy mix); post-Aqua Comms, drift toward International Backbone Specialist. Cooper, please confirm primary classification.
- **Sparkle (TIM)** — pending sale to Italian state (Retelit consortium) for €700M, close expected H1 2026. Revenue ~€1B. 600,000+ km fiber + extensive subsea (AAE-2 partner with PCCW + Telecom Egypt + ZOI; many Mediterranean + transatlantic cables). Strong fit for International Backbone Specialist.
- **Orange Wholesale International (OWI)** — division of Orange Group. Revenue undisclosed at division level (parent Orange 2024 €40B+). MEF Sonata-compliant EVPL Online API; 29 countries; ~80 partner PoPs. Programmable-wholesale leader. Borderline — could classify as a division of Tier 1 Carrier or as International Backbone Specialist; `manual_review_required` recommended at parent-or-division decision.
- **BT Global / BT Wholesale International** — division of BT Group. Parent BT FY2025 revenue £20.4B. International wholesale book historically large; recent strategy is wind-down of non-UK enterprise. Borderline — division of Tier 1 Carrier; flag for `manual_review_required` if HubSpot record is at division level.

**APAC (4):**
- **Tata Communications** — independent (Tata Sons-majority). FY2025 revenue INR 23,109 crore (~$2.7B), data revenue >INR 19,000 crore (~$2.2B), up 13.7% YoY. Owns the world's largest wholly owned subsea fibre backbone (~500,000 km submarine fiber). Tier 1 IP transit AS6453. Strong fit; also has Pure Wholesale Carrier overlap. **Default to `manual_review_required` per original draft.**
- **PCCW Global** — independent (parent PCCW). PCCW Group revenue $5.16B (trailing twelve months Dec 2025). PCCW Global has 738,000 km fiber, 135+ POPs, owns/co-owns 67 cable systems. ADC (Asia Direct Cable) operational Nov 2024 carrying 160+ Tbps. AAE-2 consortium with Sparkle, Telecom Egypt, ZOI announced 2025.
- **HGC Global Communications** — independent, HQ Hong Kong. FY2024 revenue $750M (up from $258.7M earlier estimates). Strong Asia Pacific + Mekong + Philippines focus. DCI clusters connecting Hong Kong, Singapore + emerging hubs (Philippines, Thailand, Malaysia) linking 55+ data centers.
- **Telstra International** — division of Telstra (parent Telstra FY2025 AU$23.13B / ~$15B). International wholesale arm; subsea cable owner / co-owner. **Note: Telstra International is NOT Console Connect's parent** (Console Connect is HKT-owned; the Infratil deal cancelled Oct 31, 2024). Borderline — division of Tier 1 Carrier.

**Bharti Airtel International** — division of Bharti Airtel (parent ~$18B FY2025). FY25 international wholesale business has been *de-emphasized* by Airtel ("scaled down low-margin wholesale services"). Two new subsea cables landed (SEA-ME-WE-6 in Chennai, 2Africa). Borderline — Bharti Airtel parent is Tier 1 Carrier for India and Africa, while the International division is International Backbone Specialist. Default to `manual_review_required` at record level.

**LATAM (1):**
- **Liberty Networks** (Liberty Latin America B2B brand) — see Pure Wholesale Carrier section. 50,000 km subsea + 17,000 km terrestrial; owns ARCOS-1, CFX, ECFS, PCCS, MAYA-1.2; building MANTA. Strong subsea-anchored International Backbone Specialist for LATAM/Caribbean; classification depends on primary revenue source. Could classify either way; default `manual_review_required` for sub-segment.

**APAC additional (1):**
- **Epsilon Telecommunications** — owned by KT Corporation (South Korea; acquired 2021; NOT acquired by Bharti Airtel as one variant in draft 05 suggested — Bharti is an Epsilon CUSTOMER, not owner). HQ Singapore. Revenue estimated $50-100M. Bharti Airtel + other carriers use Epsilon for network. London, Paris, Singapore presence. **CORRECTION TO DRAFT 05:** Epsilon is KT Corp-owned; the "Bharti Airtel customer" relationship cited in draft 05 is correct but ownership was misrepresented.

### 2025-26 M&A notes affecting anchors

- **Sparkle** — pending sale to Italian state (Retelit consortium) for €700M; EU approval April 13, 2026; close H1 2026, long-stop Oct 15, 2026. Post-close, parent shifts from Telecom Italia to Italian state.
- **EXA Infrastructure** acquired Aqua Comms Dec 31, 2025 — strengthens subsea position. May push sub-segment classification from Pure Wholesale toward International Backbone Specialist.
- **Console Connect / Infratil** — deal cancelled Oct 31, 2024; Console Connect remains HKT-owned. **Remove "Infratil + HKT joint" framing from draft 05.**
- **Tata Communications** — no M&A activity affecting parent in 2025-26.
- **PCCW Global** — AAE-2 consortium with Sparkle, Telecom Egypt, ZOI signed 2025 (cable system, not corporate M&A).

### Confusable-with comparison

- **vs Tier 1 Carrier:** Tier 1 Carrier has dominant home-market retail consumer; International Backbone Specialist's revenue is 60%+ international wholesale with no dominant home-country retail. Decisive tell: 10-K or annual report revenue geography breakout.
- **vs Pure Wholesale Carrier:** Pure Wholesale has meaningful domestic / regional book; International Backbone is international-first. Decisive tell: revenue geography. Tata and EXA Infrastructure sit on this boundary and benefit from `manual_review_required`.
- **vs Subsea Cable Operator (edge case, see Part B):** International Backbone Specialist has terrestrial backbone + IP transit on top of subsea; pure-play Subsea Operator only sells wet-plant capacity (Aqua Comms pre-EXA, Seaborn, BW Digital).

### Selling angle (MaiaEdge)

Their customers buy international circuits to extend regional footprints. MaiaEdge sits on top: "your subsea capacity is the long-haul; we put a private fabric on top for the cross-cloud, cross-region paths your enterprise customers need without you having to build the orchestration." For Tata-pattern operators with programmable wholesale (IZO Dynamic Connectivity): "we extend your programmable wholesale across partner operators in regions you don't own." For subsea-anchored operators (Sparkle, Liberty Networks): "your wet-plant capacity is great; MaiaEdge wraps the AI-era enterprise experience around your cable systems."

### HubSpot fields R1/R2 must populate

**Required (diagnostic):**
- `customer_segment` = `Network Operator(Tier 1 / VNO)`
- `company_sub_segment` = `International Backbone Specialist - Network Op`
- `annualrevenue` ($100M-$5B; division-level if available)
- `country` (HQ; expect Italy, UK, India, Hong Kong, Singapore, South Korea, Mexico, Australia)
- `network_op_track` (most are Track A — already have meaningful internal automation; Tata IZO, PCCW Console Connect, Orange Sonata APIs)
- `account_tier` (Tier 1 by deal size; Tata + PCCW + Sparkle especially)

**Recommended:**
- `numberofemployees`
- `recent_news_or_trigger_event` (subsea cable RFS dates, consortium announcements)
- ASN list (free-text in brief)
- Subsea cable ownership list (free-text in brief; or new structured field)
- Parent association if record is a division

### Signal source coverage

**Tier A (Robust):**
- Company IR / newsroom (Tata, PCCW, HGC, Sparkle, EXA, Liberty Networks, Epsilon, Telstra, BT)
- TeleGeography 2025 Submarine Cable Map (cable ownership)
- TeleGeography Global Bandwidth research
- Capacity Media Global Connectivity Awards
- TelecomTV, Capacity Media (international primary)
- Light Reading subsea, Submarine Networks magazine

**Tier B (Medium):**
- Mplify (MEF) Sonata-conformance registry
- TM Forum AN registry
- SubTel Forum coverage
- Submarine Networks World articles

**Coverage gaps:**
- Most International Backbone Specialists are private or divisional → limited public financial data
- LATAM coverage thinner than EMEA / APAC; Liberty Networks is the primary anchor
- MENA coverage gap (e&, Etisalat International, STC, Saudi Telecom, Mobily — not covered in current anchor list; recommend Cooper review for additions)

### Contact personas (specific titles)

**Technical Champion:**
- VP Network Architecture
- VP IP & Transport (International)
- Principal Network Architect, International
- Director of Subsea Cable Operations
- Director of Peering / Head of Global Peering
- VP Engineering, International

**Business Sponsor:**
- VP / SVP International Wholesale
- VP / SVP Carrier Sales
- President / CEO, International Division (when divisional)
- VP Product, International / VP NaaS Platform
- Head of Hyperscaler Partnerships

**Economic Buyer:**
- CEO, International Division (Tata Communications CEO; PCCW Global Managing Director; etc.)
- CTO, International Division
- CFO, International Division (for >$5M deals)
- Parent CEO / CTO (for transformational deals)

**Procurement:**
- VP Strategic Sourcing, International
- Director of Procurement, Network
- Strategic Vendor Manager
- Chief Procurement Officer (parent-level)

### Confidence scoring rules (deterministic)

- **high_90:** Anchor match (Tata, PCCW Global, HGC, Sparkle pre-sale, Telstra International, EXA, Liberty Networks LATAM, Epsilon) OR near-twin (HQ outside US, subsea cable co-ownership verifiable on TeleGeography, $100M-$5B revenue, international-first marketing language) + ≥4 quantitative markers + ≥2 required signals + 0 disqualifiers
- **medium_7089:** ≥3 quantitative markers + ≥1 required signal + 0 disqualifiers
- **low_5069:** ≥2 quantitative markers OR partial evidence
- **manual_review_required:** Tata Communications (Pure Wholesale Carrier overlap); EXA Infrastructure post-Aqua Comms (Pure Wholesale overlap); Sparkle pending Italian state acquisition; Bharti Airtel International division vs Bharti Airtel parent record; Liberty Networks (Pure Wholesale Carrier overlap); BT Global / Orange Wholesale International / Deutsche Telekom Global Carrier (division-of-Tier-1 overlap); pure-subsea operators (Aqua Comms pre-EXA, Seaborn — these should drop out as Non-ICP edge cases per Part B missing #1)

### Industry sources for ongoing validation

- TeleGeography 2025 Submarine Cable Map (annual May; cable ownership data)
- TeleGeography Global Bandwidth research (annual)
- Capacity Media Global Connectivity Awards (annual)
- Mplify (MEF) Connects Wholesale event speaker lists (annual)
- Submarine Networks World (continuous)
- SubTel Forum (continuous)
- TelecomTV (continuous; primary international)
- Capacity Media (continuous; primary international)
- Individual company 10-K / 20-F / annual reports (where public)
- PCCW Group annual report (PCCW Global is the principal segment)
- Tata Communications quarterly results (Tata Sons holding)

---

## Final notes for Cooper

**Industry taxonomy buckets MaiaEdge may be missing or need to reframe (decision points for Cooper):**

1. **Pure-play Subsea Cable Operators** (Aqua Comms pre-EXA, Seaborn Networks, BW Digital, hyperscaler subsea SPVs): currently fold into International Backbone Specialist but don't have the federation use case. Recommend explicit Non-ICP edge-case handling or new sub-segment.

2. **Mobile-first Tier 1 Carriers** (T-Mobile US, Three UK, Rakuten Mobile): currently fold into Tier 1 Carrier but the buying motion is fundamentally different (mobile retail dominates, wholesale is thin). Recommend `manual_review_required` trigger when retail-mobile >70% of revenue.

3. **Wholesale division of Tier 1 Carrier records** (Sparkle, Telstra International, Bharti Airtel International, Orange Wholesale, BT Global, T-Wholesale, Deutsche Telekom Global Carrier, NTT Communications): no explicit handling rule. Sparkle's 2026 sale to Italian state demonstrates how brittle parent-vs-division mapping is. Recommend a documented decision rule or a `wholesale_division_of_tier1` flag.

**Anchor companies removed or flagged as borderline:**

- **Lumen Technologies** — post-divestiture (EMEA to Colt 2024, consumer FTTH to AT&T Feb 2026) is drifting from Tier 1 Carrier toward Pure Wholesale Carrier. Flag at next quarterly anchor refresh.
- **Console Connect** — Infratil + HKT deal cancelled Oct 31, 2024 (draft 05 stated 80% Infratil + 20% HKT — this is now wrong). Console Connect remains HKT-owned.
- **Epsilon Telecommunications** — KT Corporation-owned (acquired 2021), NOT Bharti Airtel-owned. Bharti is a customer.
- **Crown Castle Fiber** — sold to Zayo April 2026 for $4.25B; no longer separate entity; combined into Zayo at $2.5B+ estimated revenue. Already handled in fiber-operator draft 05; flagged here as reminder.
- **Pure-subsea operators** (Aqua Comms acquired by EXA Dec 31, 2025; Seaborn) — recommend edge-case Non-ICP treatment.
