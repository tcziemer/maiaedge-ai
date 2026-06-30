# Phase B + C — Enterprise (Multi-DC ICP) Industry Taxonomy + Sub-Segment Deep Dives

**Date:** 2026-05-14
**Scope:** `customer_segment = "Enterprise-CustomerSegment"` (display "Enterprise"), 4 active sub-segments. ICP promoted 2026-05-11. Priority 5 (lowest of the ICPs but qualified and sellable).
**Sources read:** `context/segments/enterprise.md`, `context/signals/enterprise-signals.md`, `context/segments/enterprise-use-cases.md`, `working/00-hubspot-enum-verification.md`, `working/A-gap-matrix.md`.

This file refreshes anchors (10-15 per sub-segment with geographic spread), formalizes confidence scoring rules to match the four-bucket `segmentation_confidence` enum (`high_90`, `medium_7089`, `low_5069`, `manual_review_required`), documents Watch List policy clarifications (Manufacturing, Energy/Utilities, Logistics), and extends the existing gold-standard cheatsheet content. The 4 active sub-segment values are encoded EXACTLY as in HubSpot (case-sensitive): `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`.

---

## Top section — Industry taxonomy alignment

### NAICS mapping to the 4 ICP sub-segments

| Sub-segment (HubSpot internal value) | Primary NAICS | Sector codes | Sub-codes that qualify |
|---|---|---|---|
| `Financial Services - Enterprise` | **52** Finance & Insurance | 521 Monetary Authorities-Central Bank; **522** Credit Intermediation (522110 Commercial Banking, 522210 Credit Card Issuing, 522293 International Trade Financing); **523** Securities/Investment (523110 Investment Banking, 523120 Securities Brokerage, 523210 Securities & Commodity Exchanges); **524** Insurance Carriers (524113 Direct Life Insurance, 524126 Direct P&C Insurance); 525110 Pension Funds | 522110, 522210, 523110, 523120, 523210, 524113, 524126 are the core. Commercial-procurement defense contractors (NAICS 336411 Aircraft Mfg, 334511 Search/Detection — Lockheed, RTX, Northrop, BAE, L3Harris) land here too per the existing cheatsheet rule. |
| `Healthcare Systems - Enterprise` | **62** Health Care | **622** Hospitals (622110 General Medical & Surgical Hospitals, 622210 Psychiatric & Substance Abuse, 622310 Specialty Hospitals); 621498 All Other Outpatient Care; 621491 HMO Medical Centers (Kaiser) | 622110 is the gate — multi-hospital IDNs only. Single-hospital regional systems do NOT qualify. Outpatient-only operators (One Medical, Oak Street pre-CVS) do NOT qualify. |
| `Retail and Distribution - Enterprise` | **44-45** Retail Trade | 445110 Supermarkets; 445120 Convenience Stores; 452210 Department Stores; 452311 Warehouse Clubs & Supercenters; 444110 Home Centers; 448140 Family Clothing; 454110 Electronic Shopping & Mail-Order (Amazon retail arm); **42** Wholesale Trade for distribution-heavy operators (424410 General Line Grocery Merchant Wholesalers — Sysco, US Foods, Performance Food) | 452311 + 445110 + 444110 are the heaviest hitters (Walmart, Costco, Kroger, Home Depot). Wholesale-distribution operators with multi-DC corporate IT (Sysco, US Foods) qualify if scale gate passes. |
| `Outsourcing Services - Enterprise` | **56** Admin & Support Services | **5614** Business Support Services (561422 Telemarketing & Call Centers — TaskUs, Concentrix, Teleperformance, Conduent); **5616** Investigation & Security; 541512 Computer Systems Design (Cognizant, Genpact BPS, Wipro BPS, TCS BPS where the BPO arm is a material revenue line); 541611 Admin Mgmt Consulting (FILTER OUT the project-consulting arms — Deloitte / McKinsey / BCG / Bain) | 561422 is the cleanest fit. Cognizant + Genpact + Wipro + TCS sit in 541512 but qualify on operational BPS revenue. Pure consulting firms in 541611 are excluded. |

### Hard qualification gates

**BOTH must pass before any Enterprise-tagged record can score above `manual_review_required`:**

1. **Vertical gate:** account must be one of the four sub-segments above (NAICS aligned).
2. **Scale gate:** $1B+ annual revenue **AND** at least ONE of:
   - **3+ data centers** (corporate IT or operational delivery centers; warehouses alone do NOT count for Retail — must be DC-grade IT facilities); OR
   - **Direct Equinix Fabric / Megaport / PacketFabric / Console Connect port** (confirmed via customer-logo page, case study, vendor press, or Equinix Fabric Customer Directory + Megaport Customer Directory cross-reference); OR
   - **Confirmed in-house network engineering team** — verifiable via NOC presence (24x7 operations center named in 10-K Properties or careers page) OR active LinkedIn/Greenhouse/Lever/Ashby job postings for VP Network / Director Network Engineering / Principal Network Engineer / Network Architect roles.

### Hard disqualifiers (any one disqualifies regardless of other markers)

- **Network fully outsourced to a single MSP** with no internal engineering ownership (e.g., the entire WAN is contracted to Verizon Business Managed Services or AT&T Business with no in-house architect — no technical buyer exists).
- **Single data center / single geography** — no inter-DC determinism story to sell.
- **No direct carrier contracts** — everything procured via reseller or aggregator (no commercial entry point for MaiaEdge).
- **Pure SaaS-only** with no owned data centers (the SaaS provider is the customer of an enterprise; not the enterprise itself).
- **Sub-$1B revenue** regardless of DC count (mid-market $200M-$1B holds as `Other`).

### Watch List clarifications (NOT currently ICP — do NOT tag as Enterprise sub-segment)

| Watch List vertical | Why excluded today | Future-expansion trigger to revisit |
|---|---|---|
| **Manufacturing** (NAICS 31-33 — GE, 3M, Honeywell, Boeing commercial, Caterpillar, John Deere) | Plant networks are OT (operational technology) — IT/OT segmentation work, not multi-DC corporate IT. Most large industrials' corporate IT footprint is dwarfed by their plant footprint. | If the diversified industrial has a stand-alone corporate-IT footprint that matches the multi-DC scale gate AND commercial procurement profile dominates network spend, classify under `Financial Services - Enterprise` (mirrors the defense-contractor rule). Examples flagged for case-by-case review: Honeywell Connected Enterprise, GE HealthCare (post-spinoff), 3M corporate IT. Default action when ambiguous: `manual_review_required`. |
| **Energy / Utilities** (NAICS 22 — Duke Energy, Southern Company, NextEra, Exelon, Dominion) | SCADA fit is technically real, but NERC CIP procurement cycles run 18-36 months with heavy compliance burden. Out of scope for current sales motion. | Revisit when (a) the utility has a dedicated NERC CIP procurement team standing up new vendor relationships AND (b) MaiaEdge has FedRAMP-adjacent compliance maturity (CMMC L2 minimum). Do NOT enrich speculatively. |
| **Logistics / Supply Chain / 3PL** (NAICS 484, 488, 493 — XPO, J.B. Hunt, Expeditors, C.H. Robinson, Ryder, FedEx Freight as separate from FedEx Express, GXO) | Multi-warehouse ≠ multi-DC. Warehouse / freight networks are operational, not IT-DC. Deal sizes smaller; inter-DC determinism story doesn't land. | If a logistics company's CORPORATE IT footprint matches the Retail/Distribution archetype (rare — Sysco-style food distributors come closest), refer to `Retail and Distribution - Enterprise` and qualify on corporate IT, not warehouse count. |

### Government / Defense — FedRAMP gate

There is **no `Government - Enterprise` sub-segment**. State / local agencies, federal civilian, and DoD direct sales are out of scope until MaiaEdge achieves FedRAMP authorization for the PCE.

**Commercial-procurement defense contractors** (Lockheed Martin, RTX/Raytheon, Northrop Grumman, BAE Systems, L3Harris, Leidos, General Dynamics IT, SAIC) land in `Financial Services - Enterprise` per the existing cheatsheet rule — they're classified on their **commercial** procurement profile (FFIEC-style network architecture, Fortune 100 commercial IT footprint), not their government work. Their classified / DoD work is irrelevant to the ICP classification.

The FedRAMP gate is also why we **don't enrich GovCloud-only AWS / Azure customers** under Enterprise. The PCE has to ride the federal-authorized stack before that motion makes sense.

---

# Per Sub-Segment Deep Dives

Each section formalizes definition, quantitative markers, required signals, disqualifiers, anchor companies (10-15 with geographic spread), confusable-with comparison, selling angle, HubSpot fields, signal source coverage, contact personas (incl. procurement), and confidence scoring rules.

---

## `Financial Services - Enterprise`

### Definition (sharpened — what makes this ICP-qualified vs Watch List)

Banks, investment firms, insurers, payment networks, capital-markets infrastructure, and exchanges that operate their own multi-DC network footprint with in-house network engineering. The defining attributes are (a) regulator-driven physical-path verification requirements (FFIEC BCM IV.A.6, DORA CTPP, NY DFS Part 500), (b) low-latency inter-DC replication for mainframe / GDPS / market-data plant, and (c) multi-cloud determinism at sub-millisecond budgets. Commercial-procurement defense contractors (Lockheed, RTX, Northrop, BAE, L3Harris, Leidos, General Dynamics IT, SAIC) land here on their commercial profile — classified work is irrelevant to classification.

**Distinct from Watch List Manufacturing:** Diversified industrials whose corporate IT footprint dominates network spend (Honeywell Connected, GE HealthCare post-spinoff, 3M) are case-by-case `manual_review_required`. If commercial procurement profile + multi-DC IT proven, classify here. If plant-OT spend dominates, hold as `Other`.

### Quantitative markers

| Marker | Band |
|---|---|
| Revenue | $1B-$200B+ (Top 25 US banks: $80B-$162B revenue; G-SIBs $100B-$160B; major insurers $20B-$100B) |
| Data centers | 3-25+ (top banks run 8-15 primary + DR + cloud-on-ramp facilities) |
| In-house network engineering | 25-300+ engineers (JPMorgan ~300, Goldman ~150, mid-size regional ~25-50) |
| Equinix Fabric / Megaport ports | YES (nearly universal — NY4/NY5/LD4/AM5/SG3 are baseline) |
| 24x7 NOC | YES (named in 10-K Properties or trade press) |
| Carrier contracts | Direct (typically AT&T Business, Verizon Business, Lumen, BT GS, NTT Comms, Orange Business) |

### Required signals (the affirmative evidence to confirm fit)

- **NOC presence** — named 24x7 operations center in 10-K Item 2 Properties OR mentioned in trade press / careers page.
- **LinkedIn / Greenhouse / Lever / Ashby job postings** for VP / Director / Principal Network Engineering, Network Architecture, Markets Network Engineering, Trading Infrastructure, Connectivity Engineering, WAN Engineering.
- **Equinix Fabric / Megaport / PacketFabric / Console Connect port** — confirmed via customer-logo page or case study.
- **Direct carrier contracts** — 10-K Risk Factors mentions of third-party telecom dependencies; supplier diversity disclosures.
- **HITRUST / PCI-DSS / SOX scope mentions** in 10-K, proxy DEF 14A, ESG reports.
- **DORA CTPP or NY DFS Part 500 attestation** language in regulatory filings.
- **FFIEC BCM IV.A.6 "physical-path verification" language** in RFPs / vendor selection criteria.

### Disqualifiers

- **Mid-market community bank under $1B assets** — fails scale gate.
- **Pure-play FinTech** with no owned DC (Stripe, Plaid, Affirm, Robinhood when they were small) — pure SaaS, no inter-DC story.
- **Insurance brokerages / agencies** (Marsh & McLennan brokerage arms, Aon-as-broker) — distinct from the carrier operations.
- **Asset managers operating only through 3rd-party prime brokers** — no direct DC ownership.
- **Network fully outsourced to AT&T Business / Verizon Business managed-services-only model** with no in-house architect.
- **Reseller-only carrier procurement** (rare in FS but possible for mid-market).

### Anchor companies (15 — geographic spread)

**North America (10):**
1. **JPMorgan Chase** (NY, NY) — G-SIB, $162B revenue 2024, ~300 net eng, JPM Alves verbatim "control our own destiny" 2025
2. **Bank of America** (Charlotte, NC) — G-SIB, $99B revenue
3. **Citigroup** (NY, NY) — G-SIB, Solomon Sims CTO mandate on infrastructure simplification
4. **Wells Fargo** (San Francisco, CA) — top-4 US bank
5. **Goldman Sachs** (NY, NY) — G-SIB, GS AI deployment 2024-2025
6. **Morgan Stanley** (NY, NY) — G-SIB, Knowledge Assistant + Wealth Advisor Copilot
7. **BNY Mellon** (NY, NY) — top global custodian, Pershing platform infrastructure
8. **State Street** (Boston, MA) — top global custodian, Alpha Platform
9. **Capital One** (McLean, VA) — Discover acquisition closed May 18, 2025 → 18-36 month integration window
10. **Visa** (San Francisco, CA) — payment network, VisaNet ~3 DCs + global

**EMEA (3):**
11. **HSBC** (London, UK) — G-SIB, multi-region DC footprint
12. **Deutsche Bank** (Frankfurt, DE) — G-SIB, multi-DC EU + NY
13. **Lloyds Banking Group** (London, UK) — multi-DC UK + Edinburgh

**APAC (2):**
14. **Mitsubishi UFJ Financial Group / MUFG** (Tokyo, JP) — G-SIB, NY + London + Singapore
15. **DBS Bank** (Singapore) — multi-cloud poster child, named Equinix Fabric customer

**Defense-contractor edge cases (classify here on commercial profile):**
- Lockheed Martin (Bethesda, MD); RTX/Raytheon (Arlington, VA); Northrop Grumman (Falls Church, VA); BAE Systems (Falls Church, VA / Farnborough, UK); L3Harris (Melbourne, FL); Leidos (Reston, VA); General Dynamics IT (Falls Church, VA); SAIC (Reston, VA)

### Confusable-with comparison

- **vs. `Healthcare Systems - Enterprise`** — UnitedHealth Group is a hybrid (Optum Insight tech arm + UnitedHealthcare insurance). Classify UNH parent on its scale (Top 5 Fortune); Optum subsidiaries by sub-segment fit. Insurance carriers (Aetna pre-CVS, Anthem/Elevance, Cigna) sit in FS, not Healthcare. Pharmacy benefit managers (CVS Caremark, Express Scripts) are FS-adjacent due to claims-processing infrastructure; default `manual_review_required`.
- **vs. Watch List Manufacturing** — diversified industrials (Honeywell, 3M, GE HealthCare) where commercial-procurement IT dominates → classify FS. Where plant-OT dominates → `Other`. Default `manual_review_required` when both look significant.
- **vs. `Outsourcing Services - Enterprise`** — Cognizant + Genpact serve FS clients but ARE BPOs, not FS. Don't conflate.
- **vs. `Retail and Distribution - Enterprise`** — Costco's banking arm (Costco Credit Card via Citi) doesn't make Costco an FS company. The parent classification wins.

### Selling angle (M&A network integration as default E1 anchor)

**Lead (M&A anchor — default for FS + OS):** "Capital One / Discover means 22 months of two MPLS cores, two ADs, two SD-WAN orchestrators. The integration cost line in the press release is mostly network." Pivot to: "M&A integration on one fabric instead of two parallel WANs — controller decision, not BGP convergence."

**Secondary angles:** FFIEC physical-path verification ("the 'diverse' path that wasn't"); DORA CTPP concentration risk (Megaport / Equinix Fabric as designated third party); deterministic inter-DC paths (microbursts, brownouts); cloud on-ramps under their control instead of Megaport / Equinix Fabric dependency.

**Current why-nows (2026):**
- **REDUNDANT** - carrier consolidation is invalidating diverse-path attestations. As formerly-independent fiber collapses under fewer owners, a wave that was diverse from the incumbent now shares regional aggregation with the carriers the bank would pick as Path B. Present as a reasoned observation worth re-testing against today's ownership map, not as a single cited fact.
- **SOVEREIGN** - DORA's first oversight cycle (live 2026) extends the CTPP critical-third-party list past the hyperscalers to connectivity and data-center providers (Colt, Deutsche Telekom, Orange, Equinix, InterXion). The concentration question now reaches the fabric the on-ramps ride, and best-effort routing still cannot show the examiner the path.

**Use Case 5 (M&A) is the highest-fit lead per `enterprise-use-cases.md`.** Use Case 1 (dark fiber redundancy) and Use Case 8 (policy-based path control with audit trails) are co-leads when the recipient is a Network Architect or CSO/CISO respectively.

### HubSpot fields R1/R2 must populate

| Field | Target value |
|---|---|
| `customer_segment` | `Enterprise-CustomerSegment` |
| `company_sub_segment` | `Financial Services - Enterprise` |
| `segmentation_confidence` | per Confidence scoring rules below |
| `account_tier` | `tier_2` ceiling; `tier_3` default; `tier_4` aspirational |
| `recent_news_or_trigger_event` | M&A close date / new CIO hire / DORA CTPP designation / NY DFS enforcement |
| `account_brief` | Generated/refreshed every full R2 pass (120-day rotation) |
| `last_enriched_date` | Stamped only on full-pipeline pass + Completeness Gate pass |

### Signal source coverage (from `context/signals/enterprise-signals.md`)

- **E-A1** New DC / corporate IT campus (10-K Item 2, American Banker)
- **E-A2** M&A announcement OR close — 8-K Item 1.01/2.01, American Banker tracker (highest-fit signal for FS)
- **E-A3** AI / GPU workload (IndexGPT, GS AI, MS Knowledge Assistant)
- **E-A4** Network exec hire (PR Newswire Appointments, 8-K Item 5.02, Apollo job-change feed)
- **E-A5** Regulatory event (DORA CTPP Nov 18 2025, NY DFS Part 500 cert April 15 2026, FFIEC BCM IV.A.6)
- **E-A6** Equinix Fabric / Megaport customer-win press
- **E-A7** 10-K disclosure of network modernization
- **E-B1** Senior network role surge (3+ reqs in 30d)
- **E-B2** Peer ransomware incident
- **E-B3** New cloud / multi-cloud migration kickoff
- **E-C2** Earnings transcript "third-party fabric" / "network modernization"

### Contact personas (priority + buying committee + procurement)

**Buying committee:**
- **Technical Champion** — Principal Network Architect, Director Network Engineering, Markets Network Engineer, Trading Infrastructure Lead, Connectivity Engineering Manager
- **Business Sponsor** — VP / SVP Network Infrastructure, Head of Connectivity, Head of WAN, VP Trading Infrastructure
- **Economic Buyer** — CIO, CTO, Head of Markets Technology, CISO (for compliance-driven entry)
- **Security Stakeholder** — CSO / CISO / Head of Cyber Risk / Third-Party Risk
- **Compliance** — Chief Compliance Officer, Head of Op Risk, Head of Vendor Risk Management (DORA CTPP owners)

**Procurement personas (often the gating step at FS):**
- **VP Procurement / Chief Procurement Officer**
- **Director Strategic Sourcing — IT / Telecom**
- **Vendor Management Office (VMO) lead**
- **Director Third-Party Risk Management** — gates DORA CTPP onboarding

Persona priority for cold outreach: **Principal Network Architect → VP Network Infrastructure → CSO/CISO**. CIO is reserved for warm intro or post-discovery.

### Confidence scoring rules

| Confidence bucket | Criteria |
|---|---|
| `high_90` | Anchor list match OR Fortune 500 + 3+ DCs confirmed + in-house net eng team verified (NOC presence OR ≥2 senior network job postings OR LinkedIn engineering-team count ≥25) + Equinix/Megaport port OR direct carrier contract confirmed |
| `medium_7089` | 2 of {anchor list, Fortune 500, 3+ DCs confirmed, in-house team verified}. Scale gate passes but one supporting signal missing. |
| `low_5069` | Scale gate passes ($1B+ rev) but DC count not verified AND in-house team not verified. Single-source claim. |
| `manual_review_required` | (a) Defense contractor edge case where commercial vs classified profile is unclear; (b) Insurance brokerage / asset manager ambiguity; (c) Diversified industrial where Manufacturing vs FS classification depends on hidden corporate IT footprint; (d) PBM (CVS Caremark / Express Scripts) classification; (e) any case where scale gate is met but vertical fit is ambiguous. |

### Industry sources

- **FFIEC member list** (Federal Reserve / FDIC / OCC / NCUA member banks)
- **DORA CTPP designations** (ESMA / EBA / EIOPA portals — AWS, Microsoft, Google formally designated Nov 18, 2025)
- **NY DFS Part 500 amendments** (effective Nov 1, 2025; first cert April 15, 2026)
- **Fortune 500** (Top 25 US banks ranking) + **Forbes Global 2000** (banks subsection)
- **American Banker Top 100 Banks** ranking + M&A tracker + leadership column
- **Federal Reserve large bank holding company list** ($100B+ assets)
- **Equinix Fabric Customer Directory** + **Megaport Customer Directory**
- **SEC EDGAR** (10-K Item 2 Properties, DEF 14A proxy CIO disclosure, 8-K Item 5.02)
- **NAIC** (insurance regulator) + **AM Best** (insurer ratings) for insurer scale gate validation
- **Risk.net** / **Financial News London** / **Bobsguide** (EMEA Financial Services)
- **Sibos / Money 20/20 / AFP** conference agenda scrapes

---

## `Healthcare Systems - Enterprise`

### Definition (sharpened — what makes this ICP-qualified vs Watch List)

Multi-hospital Integrated Delivery Networks (IDNs) and large health systems with EHR data centers, imaging archives, regional clinic networks, and in-house network engineering teams. The defining attributes are (a) HIPAA-aligned redundancy requirements, (b) Epic Hyperdrive cutover programs requiring inter-DC determinism for clinical traffic, (c) PHI sovereignty obligations, and (d) IoMT segmentation projects (Claroty Medigate / Elisity / Asimily) generating fresh network architecture spend. Single-hospital regional systems below the scale gate do NOT qualify regardless of bed count.

**Distinct from Watch List:** Insurance carriers (Aetna, Cigna, Anthem/Elevance) sit in FS, not Healthcare. UnitedHealth Group hybrid case → parent in FS, Optum subsidiaries by sub-segment fit.

### Quantitative markers

| Marker | Band |
|---|---|
| Revenue | $1B-$80B+ (HCA Healthcare $70B; Ascension $28B; CommonSpirit $36B; Kaiser Permanente $115B as integrated payer-provider edge case) |
| Hospitals operated | 8-200+ (HCA ~190; Ascension ~140; CommonSpirit ~140) |
| Data centers (corporate IT, not site closets) | 2-8 (typically primary + DR + cloud-on-ramp + imaging archive) |
| In-house network engineering | 15-80 engineers |
| Epic instance | YES (the dominant EHR for large IDNs; Oracle Cerner / Meditech / Allscripts smaller share) |
| Imaging archive (VNA) | YES (vendor-neutral archive distinct from departmental PACS) |
| Equinix Fabric / Megaport ports | Increasing — radiology cloud workloads + Cogito-on-Azure drive adoption |

### Required signals

- **Named Epic customer** (most large IDNs are; Hyperdrive cutover signals fresh DC project budget)
- **NOC presence** — many IDNs run 24x7 clinical IT operations
- **LinkedIn / Greenhouse / Lever / Ashby postings** for VP / Director Clinical Network Operations, EHR Infrastructure, Imaging Network, Clinical IT Architecture
- **HITRUST r2 scope** + **HIPAA Security Rule NPRM (Dec 27, 2024)** TLS 1.2+ / encryption-in-transit mentions (NPRM not finalized as of mid-2026)
- **OCR ransomware consent orders (April 23, 2026)** - corrective action plans requiring network segmentation, asset inventory, and ePHI data-flow mapping (enforced now, rule-independent)
- **HSCC Sector Mapping toolkit + Updated Model Contract Language** participation (Oct/Nov 2025)
- **TEFCA participation** — federated query traffic to QHINs (real new network flow 2024-2025)
- **Cosmos contribution** (Epic cross-customer research dataset)
- **VNA platform mentioned** (Sectra, Change Healthcare CWS, Fujifilm Synapse VNA, Hyland Acuo, GE Health Imaging)

### Disqualifiers

- **Single-hospital regional systems** under $1B revenue regardless of bed count.
- **Outpatient-only operators** (One Medical, Oak Street pre-CVS, DaVita is dialysis-specialty — borderline; Fresenius the same).
- **Pure managed-services healthcare** (R1 RCM, athenahealth as pure SaaS) — they're vendors TO healthcare, not the IDN itself.
- **Insurance carriers** (Aetna/CVS, Cigna, Anthem/Elevance) — sit in FS.
- **Specialty single-modality chains** (ambulatory surgery centers as standalone — USPI is HCA's, so HCA classifies; SCA as standalone is borderline).
- **Network fully outsourced to managed services** (some IDNs run on Verizon Business managed WAN with thin internal — verify in-house team before classifying).

### Anchor companies (15 — geographic spread, all verified multi-DC + in-house net eng)

**North America (12):**
1. **HCA Healthcare** (Nashville, TN) — ~190 hospitals, 21+ states, $70B revenue, multi-DC IT
2. **Ascension** (St. Louis, MO) — ~140 hospitals, 19 states, post-Black Basta (May 2024) board-level segmentation review still active
3. **CommonSpirit Health** (Chicago, IL) — ~140 hospitals, 21 states, South region single-Epic go-live June 2025
4. **Kaiser Permanente** (Oakland, CA) — integrated payer-provider, 39 hospitals, $115B revenue
5. **Cleveland Clinic** (Cleveland, OH) — academic medical center, multi-state + international (UAE / London)
6. **NewYork-Presbyterian** (NY, NY) — academic, 10 hospitals, Cornell + Columbia affiliates
7. **Mass General Brigham** (Boston, MA) — academic, 14 hospitals, Harvard affiliate
8. **Trinity Health** (Livonia, MI) — 88 hospitals, 26 states, independent IDN and ALSO divesting hospitals to stabilize finances (2026). CORRECTION 2026-06-12: Trinity Health (Livonia) is NOT merging with UPMC — UPMC is acquiring "Trinity Health System" (Steubenville, OH), a CommonSpirit regional system, close expected Fall 2026. Two different entities; do not conflate in outreach.
9. **UPMC** (Pittsburgh, PA) — 40 hospitals, consolidating from 9 EHRs (post-merger network integration window)
10. **Banner Health** (Phoenix, AZ) — 33 hospitals, 6 states
11. **Providence** (Renton, WA) — 51 hospitals, 7 western states
12. **Intermountain Health** (Salt Lake City, UT) — 33 hospitals post-SCL merger

**EMEA (2):**
13. **NHS England** (UK) — federated multi-trust, **classify per individual trust** (Manchester University NHS Foundation Trust, Imperial College Healthcare NHS Trust qualify; primary care trusts do not)
14. **Karolinska University Hospital / Region Stockholm** (SE) — major EU academic IDN with cross-border imaging research

**APAC (1):**
15. **Apollo Hospitals India** (Hyderabad / Chennai, IN) — 73 hospitals, multi-country, in-house net eng (one of the few APAC fits)

**Additional secondary anchors (Tier 3):** BJC HealthCare (St. Louis, MO — merging with St. Luke's), Memorial Hermann (Houston, TX), Sutter Health (Sacramento, CA), Tenet Healthcare (Dallas, TX), AdventHealth (Altamonte Springs, FL), Atrium Health (Charlotte, NC — Advocate Health post-merger), Northwell Health (New Hyde Park, NY), Mayo Clinic (Rochester, MN).

### Confusable-with comparison

- **vs. `Financial Services - Enterprise`** — UnitedHealth Group parent → FS (insurer). Optum subsidiaries → by sub-segment fit (Optum Insight = software vendor, Optum Health = provider network).
- **vs. Watch List Pharma** — pharmaceutical manufacturers (Pfizer, Merck, J&J pharma arm) are NOT Healthcare Systems. They sit in Manufacturing watch list per NAICS 3254. CVS parent is the borderline case — pharmacy + insurance arm + clinic arm. Default `manual_review_required` for CVS; lean Healthcare for the clinic + pharmacy operations side.
- **vs. Watch List Outsourcing** — Healthcare RCM / BPO (R1 RCM, Conduent Healthcare) are Outsourcing, not Healthcare.

### Selling angle (dark fiber redundancy as default E1 anchor)

**Lead (dark fiber redundancy anchor — default for Healthcare + Retail):** "Your two-DC Epic active/passive depends on inter-DC replication. RPO of 90 seconds → 15 seconds is the conversation we keep having with IDNs mid-Hyperdrive." Pivot to: "Diverse dark fiber redundancy between EHR DCs that's actually diverse — PBCs at each end with diverse fibers in, automated failover, no routing protocols."

**Secondary angles:** Cloud on-ramps under enterprise control for radiology / Cogito-on-Azure analytics; policy-based path control for HIPAA flows + HITRUST audit trails; new acquired-hospital site bring-up in days not 9-month carrier-circuit cycle (M&A integration angle).

**Current why-nows (2026):**
- **SOVEREIGN** - OCR ransomware consent-order corrective action plans are enforcing network segmentation, asset inventory, and ePHI data-flow mapping right now, rule or no rule. The IDN has to prove the segmentation, not assert it.
- **REDUNDANT / AUTOMATED** - AI imaging is crushing inter-DC bandwidth. AI-reconstructed studies and 200GB+ tomosynthesis volumes moving between the imaging archive and read sites were never re-provisioned for; the inherited carrier circuit was sized for an older study weight. Each new read site or acquired hospital (UPMC's Epic cutover wave) is a connectivity turn-up before the first image moves.

**Use Case 1 (dark fiber redundancy) + Use Case 8 (audit trails) are co-leads.** Use Case 7 (new site bring-up) fires when an acquired-hospital cutover signal is the trigger.

### HubSpot fields R1/R2 must populate

| Field | Target value |
|---|---|
| `customer_segment` | `Enterprise-CustomerSegment` |
| `company_sub_segment` | `Healthcare Systems - Enterprise` |
| `segmentation_confidence` | per Confidence scoring rules below |
| `account_tier` | `tier_2` ceiling; `tier_3` default |
| `recent_news_or_trigger_event` | HHS OCR breach / Epic Hyperdrive cutover date / IDN M&A close / new CISO hire |
| `account_brief` | Generated/refreshed every full R2 pass |

### Signal source coverage

- **E-A1** New IDN data center / acquired-hospital go-live
- **E-A2** Hospital M&A — constant (CommonSpirit, UPMC, Trinity)
- **E-A4** VP / Director Clinical Network Operations / EHR Infrastructure hire
- **E-A5** HIPAA breach (HHS OCR portal) — Change Healthcare ripple, Ascension Black Basta, Yale New Haven, Oracle Cerner deletion April 2025
- **E-A6** Equinix Fabric customer-win (cloud-radiology workloads drive)
- **E-B2** Peer ransomware (Change Healthcare / Ascension still echoing through 2025-2026)

### Contact personas (priority + procurement)

**Buying committee:**
- **Technical Champion** — Director Clinical Network Operations, Principal Network Engineer (EHR Infrastructure), Network Architect, Director Imaging Network
- **Business Sponsor** — VP Network Infrastructure, VP IT Operations, Chief Health Information Officer (CHIO)
- **Economic Buyer** — CIO, CDIO, CTO
- **Security Stakeholder** — CSO / CISO, Chief Information Security Officer for Healthcare, Director Cyber Risk
- **Compliance** — Chief Compliance Officer, HIPAA Privacy Officer, Director HITRUST

**Procurement personas:**
- **VP Procurement / Chief Supply Chain Officer** (large IDNs have integrated supply chain orgs)
- **Director IT Sourcing / Telecom Sourcing**
- **GPO involvement (Vizient, Premier, HealthTrust)** for some procurement categories — telecom usually direct, but worth noting

Persona priority: **VP Network Infrastructure → CSO/CISO → CIO**.

### Confidence scoring rules

| Confidence bucket | Criteria |
|---|---|
| `high_90` | Anchor list match OR Definitive Healthcare top-50 IDN + 8+ hospitals + 2+ DCs confirmed + Epic customer + in-house team verified |
| `medium_7089` | 2 of {anchor list, Definitive Healthcare top-50, 8+ hospitals, 2+ DCs confirmed, Epic customer, in-house team}. |
| `low_5069` | Scale gate passes but DC count not verified AND Epic status not verified. |
| `manual_review_required` | (a) Hybrid payer-provider (UnitedHealth, Kaiser, CVS) — parent vs subsidiary classification; (b) Specialty single-modality chains (USPI, SCA, Fresenius); (c) NHS England trust-level classification; (d) Outpatient-only operators with $1B+ rev (One Medical pre-Amazon, Oak Street pre-CVS — what's left). |

### Industry sources

- **Definitive Healthcare** top IDN rankings + bed counts
- **AHA (American Hospital Association)** member directory
- **Modern Healthcare** Top 100 Health Systems + M&A tracker
- **Becker's Hospital Review** IT leadership column + HIPAA breach roundup
- **HHS OCR breach portal** (canonical incident source) + **HIPAA Journal** (operational mirror)
- **HSCC (Healthcare Sector Coordinating Council)** Sector Mapping toolkit + Model Contract Language
- **HITRUST Assurance Program** participant directory
- **HIMSS / CHIME** member directories + conference agendas
- **Equinix Fabric Customer Directory** + **Megaport Customer Directory**
- **SEC EDGAR** (for-profit IDNs only — HCA, Tenet, Community Health Systems)
- **EU healthcare IT trade press** (limited — Karolinska, NHS trusts, Apollo Hospitals via national press)

---

## `Retail and Distribution - Enterprise`

### Definition (sharpened — what makes this ICP-qualified vs Watch List)

National retailers and large distribution networks with multi-DC corporate IT AND multi-DC distribution-center networks. **The qualifier is multi-DC corporate IT, not the number of warehouses.** Hundreds to thousands of stores, 100k+ SKUs, 3-10 DCs. Wholesale-distribution operators with multi-DC corporate IT (Sysco, US Foods) qualify if the scale gate passes. Pure-play warehouse / 3PL operators (XPO, GXO, J.B. Hunt) sit in Watch List Logistics.

**Anchor account:** Meijer (Ken Cunningham + Woody Acosta + Mark Szymanski active April 2026 design on PBC + Port Extender HAsync/HAfabric dark fiber diversity to SSR1300 nodes).

### Quantitative markers

| Marker | Band |
|---|---|
| Revenue | $1B-$650B+ (Walmart $648B; Costco $254B; Kroger $150B; Home Depot $152B; Lowe's $86B; Target $107B; Albertsons $79B; Publix $57B; Meijer $20B-$22B est) |
| Stores | 200-10,500+ |
| Distribution centers | 5-150+ (corporate IT DCs distinct from DC count) |
| Corporate IT DCs | 2-6 (the qualifying count, not total warehouses) |
| In-house network engineering | 20-150+ engineers |
| Equinix Fabric / Megaport ports | Growing — Albertsons Azure preferred, Walmart Azure + GCP, Kroger Microsoft partnership |

### Required signals

- **Top 25 US retailer** ranking (NRF / Stores Magazine Top 100 Retailers)
- **NOC presence** — 24x7 operations center for store/DC uptime
- **LinkedIn / Greenhouse / Lever / Ashby postings** for VP / Director Store-and-DC Network, Distribution Network Operations, Retail Connectivity
- **PCI DSS v4.0 scope** mentions (fully in effect March 2025)
- **OMS / WMS platforms** named (Manhattan Active, Oracle Retail, SAP S/4HANA, RELEX, Blue Yonder, Symbotic if robotics-enabled)
- **Direct carrier contracts** + dark fiber leases between corporate DCs
- **Peak readiness / freeze window language** in CIO interviews — confirms multi-DC corporate IT footprint
- **Multi-cloud (Azure / GCP / AWS)** named in 10-K or earnings transcript

### Disqualifiers

- **Single-DC retailers** under $1B revenue.
- **Pure e-commerce** (Wayfair, Etsy, Chewy) — closer to FS/SaaS architecture, no physical DC network.
- **Pure 3PL / warehouse operators** (XPO, GXO, FedEx Freight, Ryder, J.B. Hunt) — sit in Watch List Logistics.
- **Restaurant chains** (McDonald's corporate IT is multi-DC but the network footprint is dominated by franchisee branches; classify as `manual_review_required`; Chick-fil-A is corporate-DC-heavy borderline).
- **Single-store-format specialty retailers** under $1B (Lululemon at scale qualifies; smaller specialty does not).
- **Reseller-only carrier procurement** (some mid-market retailers).

### Anchor companies (15 — geographic spread)

**North America (12):**
1. **Walmart** (Bentonville, AR) — $648B revenue, 10,500 stores, multi-DC IT, Sparky / WIBEY agents production 2025, Azure + GCP
2. **Kroger** (Cincinnati, OH) — $150B, ~2,700 stores, Microsoft partnership, post-Albertsons-killed-merger IT consolidation
3. **Costco** (Issaquah, WA) — $254B, 870 warehouses, multi-DC corporate IT
4. **Home Depot** (Atlanta, GA) — $152B, ~2,300 stores, CIO Angie Brown appointed June 2025
5. **Lowe's** (Mooresville, NC) — $86B, ~1,750 stores, Mylow at 1,700+ stores
6. **Target** (Minneapolis, MN) — $107B, ~1,950 stores
7. **Albertsons** (Boise, ID) — $79B, ~2,270 stores, FY2025 capex $1.7B-$1.9B with Azure preferred
8. **Publix** (Lakeland, FL) — $57B, ~1,400 stores, Lakeland IT campus expansion 2024-2025
9. **Meijer** (Grand Rapids, MI) — ~$22B est, ~500 supercenters, **anchor account — active design**
10. **CVS Health Retail** (Woonsocket, RI) — retail pharmacy arm; classify carefully (parent CVS has insurance arm — `manual_review_required`)
11. **Walgreens Boots Alliance** (Deerfield, IL) — $147B, ~8,500 stores US, multi-DC IT
12. **Best Buy** (Richfield, MN) — $43B, ~1,000 stores

**EMEA (2):**
13. **Tesco** (Welwyn Garden City, UK) — £69B, multi-DC UK + Ireland + CEE
14. **Carrefour** (Massy, FR) — €83B, multi-country EU + Latin America

**APAC (1):**
15. **AEON Group** (Chiba, JP) — multi-country JP + China + ASEAN

**Wholesale-distribution edge cases (Tier 3 — qualify on corporate IT, not warehouses):**
- Sysco (Houston, TX) $77B; US Foods (Rosemont, IL) $36B; Performance Food Group (Richmond, VA) $58B; McKesson pharma distribution (Irving, TX) — borderline Healthcare ↔ Distribution

### Confusable-with comparison

- **vs. Watch List Logistics** — XPO, GXO, J.B. Hunt, FedEx Freight, Ryder are Logistics, NOT Retail/Distribution. Multi-warehouse ≠ multi-DC. Only refer to Retail when corporate IT footprint matches Retail archetype (rare).
- **vs. `Outsourcing Services - Enterprise`** — Conduent Retail BPO arm is Outsourcing, not Retail.
- **vs. Watch List Restaurant** — McDonald's / Yum Brands / Chick-fil-A → `manual_review_required`; corporate-DC-heavy only.
- **vs. `Financial Services - Enterprise`** — Costco's banking partnership (Citi-issued Costco Card) doesn't make Costco FS. Walmart's MoneyCenters likewise.
- **vs. Watch List Pharma** — McKesson is the toughest borderline case (pharma distribution + healthcare hybrid) — default `manual_review_required`.

### Selling angle (dark fiber redundancy as default E1 anchor)

**Lead (dark fiber redundancy — Meijer-archetype):** "DC-to-DC replication lag is the thing nobody escalates until BOPIS times out. Your 'diverse' fiber paths between primary and DR riding the same metro conduit is the 2024-2025 retail story (Hot Topic, Albertsons-style audits)." Pivot to: "Dark fiber pair between primary DCs with PBCs at each end, automated failover, no routing protocols. The freeze window (Aug-Jan) is the only window. Q1/Q2 is the decision."

**Secondary angles:** Cloud on-ramp for SaaS + analytics under retailer control (Albertsons Azure preferred, Walmart Sparky agents); PCI v4.0 segmentation reduction (cut audit scope by two-thirds); peak readiness / Cyber Monday capacity; deterministic paths into highest-traffic DCs (Symbotic robotics, pick-to-light jitter).

**Current why-nows (2026):**
- **SOVEREIGN** - PCI v4.0.1 Req 11.4.7 now requires the segmentation around the cardholder data environment to be **penetration-tested**, not asserted. The retailer has to prove the control held on a schedule; a path-control plane that produces the evidence is the difference between an assertion and an attestation.
- **AUTOMATED** - robotics-DC bring-up is connectivity-led. Symbotic Gen-2 across 42 Walmart DCs (early 2026) and Costco Port St. Lucie (March 2026) each light up as a carrier turn-up before the first bot moves; the carrier install is the long pole, not the racks.
- **AUTOMATED + cost control (GenAI egress)** - production shopping agents (Walmart Sparky, Kroger's Gemini rollout nationwide Jan 2026) ground inference in real-time data in corporate DCs while the inference runs cloud-side, so cross-cloud / cross-region egress (~$0.087/GB) scales with adoption as a new CFO-visible cost line. The inference path is now a cost decision, not just a latency one. Same logic flows to FS and BPO model-grounding.

**Use Case 1 + Use Case 2 are co-leads.** Use Case 8 (PCI v4.0 audit-scope reduction) when recipient is CSO/CISO.

### HubSpot fields R1/R2 must populate

| Field | Target value |
|---|---|
| `customer_segment` | `Enterprise-CustomerSegment` |
| `company_sub_segment` | `Retail and Distribution - Enterprise` |
| `segmentation_confidence` | per Confidence scoring rules below |
| `account_tier` | `tier_2` ceiling (Meijer = tier_2); `tier_3` default |
| `recent_news_or_trigger_event` | DC opening / CIO hire / PCI v4.0 milestone / earnings AI agent mention |

### Signal source coverage

- **E-A1** New DC / fulfillment center (Retail Dive, regional business journals)
- **E-A3** AI agents (Walmart Sparky / WIBEY, Lowe's Mylow, Albertsons / Kroger)
- **E-A4** Network exec hire (Retail Dive Movers and Shakers, RIS News)
- **E-A5** PCI DSS v4.0 enforcement + breach incidents (Hot Topic Nov 2024, CDK Global 2024, Shopify Cyber Monday Dec 2025)
- **E-A6** Equinix Fabric customer-win
- **E-B3** Multi-cloud migration (Albertsons Azure, Kroger Microsoft)

### Contact personas (priority + procurement)

**Buying committee:**
- **Technical Champion** — Network Architect, Director Distribution Network Operations, Principal Network Engineer, Director Store-and-DC Network
- **Business Sponsor** — VP / SVP Network Infrastructure, VP IT Operations, Director Infrastructure
- **Economic Buyer** — CIO, CTO, Chief Digital Officer
- **Security Stakeholder** — CSO / CISO, Director PCI Compliance, VP Information Security
- **Compliance** — PCI QSA owner, Director Loss Prevention IT

**Procurement personas:**
- **VP Procurement / Chief Procurement Officer** (very strong at retailers — Walmart, Target, Costco all have dominant procurement orgs)
- **Director Strategic Sourcing — IT / Telecom**
- **Vendor Management Office (VMO)**

Persona priority: **Network Architect → VP Network Infrastructure → CIO**.

### Confidence scoring rules

| Confidence bucket | Criteria |
|---|---|
| `high_90` | Anchor list match OR NRF Top 100 + 500+ stores + 3+ corporate IT DCs confirmed + in-house team verified |
| `medium_7089` | 2 of {anchor list, NRF Top 100, 500+ stores, 3+ corporate IT DCs, in-house team}. |
| `low_5069` | Scale gate passes but corporate IT DC count not verified (warehouses don't count). |
| `manual_review_required` | (a) Hybrid retail-pharmacy-insurance parents (CVS, Walgreens); (b) Restaurant chains (McDonald's, Yum, Chick-fil-A); (c) Pharma distribution (McKesson, Cardinal Health, AmerisourceBergen); (d) Wholesale-distribution operators where corporate IT vs warehouse footprint is unclear (Sysco, US Foods, Performance Food). |

### Industry sources

- **NRF / Stores Magazine** Top 100 Retailers + Top 50 Global Powers of Retailing
- **Retail Dive** + **RIS News** + **STORES Magazine** + **Chain Store Age**
- **PCI Security Standards Council** (v4.0 enforcement)
- **NACS** (convenience stores) for 7-Eleven / Casey's / Couche-Tard scale
- **Fortune 500** retail subsection
- **Equinix Fabric Customer Directory** + **Megaport Customer Directory**
- **SEC EDGAR** (10-K Item 2 Properties for owned DC list)
- **Retail Week** (UK), **Linéaires** (FR), **Lebensmittel Zeitung** (DE), **Nikkei Asia retail** (JP)
- **NRF Big Show / Shoptalk / RILA** conference agendas

---

## `Outsourcing Services - Enterprise`

### Definition (sharpened — what makes this ICP-qualified vs Watch List)

BPO and outsourced operations providers running multi-site delivery centers on an **ongoing operational basis** for client back-office and customer-facing functions. Multi-country / multi-state delivery footprints; regulated client data (financial, healthcare, telco BPO); latency-sensitive workflows (real-time fraud, claims, patient-data access). The qualifier is **operational delivery centers**, not consulting offices.

**Hard exclusions inside this sub-segment (verified):** Project-based consulting / advisory firms (**Deloitte, McKinsey, BCG, Bain**) are NOT Outsourcing Services - Enterprise. They are project firms, not operations.

**Dual-arm firms** (Accenture, Cognizant, Wipro, TCS, Infosys, Capgemini) are case-by-case based on **operational delivery revenue mix**:
- **Accenture Operations** — qualifies (operational BPS revenue $11B+ FY24)
- **Accenture (consulting + Strategy & Consulting)** — does NOT qualify
- **Cognizant** — qualifies (BPS arm is material revenue line; Cognizant Neuro AI + NVIDIA March 2025)
- **Wipro BPS** — qualifies; Wipro consulting arm does not
- **TCS BPS** — qualifies; TCS Consulting does not
- **Infosys BPM** — qualifies; Infosys Consulting does not
- **Capgemini Business Services** — qualifies; Capgemini Invent (consulting) does not
- **IBM Consulting** — does NOT qualify; IBM hybrid cloud + managed infrastructure could be `MSP/Aggregator` or `Other`; default `manual_review_required`

### Quantitative markers

| Marker | Band |
|---|---|
| Revenue | $1B-$25B+ (Concentrix $9.6B; Teleperformance €10.2B post-Majorel; Cognizant $19.7B with BPS portion; Genpact $4.6B; TaskUs $1B; Conduent $3.4B; Wipro BPS ~$3B of $11B total; TCS BPS ~$3B of $30B total) |
| Delivery centers | 30-300+ |
| Total seats | 50,000-450,000+ (Teleperformance 490k post-Majorel; Concentrix 440k post-Webhelp; Cognizant 350k; TCS 600k+ across all services) |
| In-house network engineering | 50-300+ engineers per major BPO |
| Equinix Fabric / Megaport ports | YES — multi-tenant carrier-grade requirement |
| Direct carrier contracts | YES + client-mandated carrier tails (every Tier-1 client adds an MPLS tail) |

### Required signals

- **Everest Group PEAK Matrix** ranking + **NelsonHall NEAT** reports referencing this BPO
- **Named ISG / Gartner Magic Quadrant** participant for BPS / Customer Experience Outsourcing
- **NOC presence** — 24x7 client-facing operations center
- **LinkedIn / Greenhouse / Lever / Ashby postings** for VP / Director Delivery Center Network, Client Connectivity, Site Operations Network, WAN Engineering
- **Multi-country delivery centers** (US + Philippines + India + LatAm minimum for the Tier 1 anchors)
- **EU DORA flow-down** language (BPO serving EU financial-services clients must comply)
- **India DPDP Rules + RBI 2025 NBFC Outsourcing Directions** language (Indian FS BPO arms)
- **Client InfoSec audit** language ("we have a Citi audit in two weeks")
- **Direct carrier contracts** + per-client MPLS tails

### Disqualifiers

- **Project-based consulting firms** — Deloitte, McKinsey, BCG, Bain, Oliver Wyman, AlixPartners (hard exclude).
- **Pure staffing / staff-aug firms** (Allegis, Kelly Services) without operational delivery centers.
- **Legal-process outsourcing** under $500M — too narrow.
- **Single-country, single-vertical BPOs** under $1B revenue.
- **BPOs whose entire footprint is one client** (captive shops) — no MaiaEdge value beyond what that one client buys.
- **Healthcare RCM single-vertical** under $1B (R1 RCM at $2.5B does qualify; smaller specialty RCM firms do not).

### Anchor companies (15 — geographic spread)

**North America (3):**
1. **Concentrix** (Newark, CA) — $9.6B, post-Webhelp Sep 2023 integration, 440k seats, 90+ countries
2. **TaskUs** (New Braunfels, TX) — $1B, Medellín + Cali + Manila + Tegucigalpa
3. **Conduent** (Florham Park, NJ) — $3.4B, government-services + commercial BPO

**EMEA-headquartered (2):**
4. **Teleperformance** (Paris, FR) — €10.2B post-Majorel, 490k seats, 170 markets, Azure OpenAI integration
5. **Capgemini Business Services** (Paris, FR) — €22B parent, operational delivery footprint

**Indian-headquartered (5):**
6. **Cognizant** (Teaneck, NJ — but Indian-origin) — $19.7B, post-Astreya April 2026 + Neuro AI + NVIDIA March 2025
7. **Genpact** (NY, NY — Indian-origin GE captive spin-off) — $4.6B, AI Gigafactory with GE Vernova Jan 2025
8. **Wipro BPS** (Bangalore, IN) — $11B parent, BPS portion ~$3B
9. **TCS BPS** (Mumbai, IN) — $30B parent, BPS portion ~$3B
10. **Infosys BPM** (Bangalore, IN) — $19B parent

**Philippines-anchored / APAC delivery (2):**
11. **Sutherland Global** (Rochester, NY — global Philippines-heavy) — $1.2B
12. **iQor** (Hollywood, FL — Philippines-heavy)

**LATAM-strong (1):**
13. **Atento** (Madrid, ES) — €1.5B, Latin America + Iberia delivery

**Specialty / regulated-vertical (2):**
14. **R1 RCM** (Murray, UT) — $2.5B, healthcare revenue cycle management
15. **Firstsource Solutions** (Mumbai, IN) — $750M (borderline scale gate — verify)

**Accenture Operations** — qualifies as a standalone classification when the Operations arm is the subject of outreach.

### Confusable-with comparison

- **vs. Consulting firms (HARD EXCLUDE)** — Deloitte, McKinsey, BCG, Bain, Oliver Wyman, AlixPartners are project firms, not operations. NEVER classify as Outsourcing Services - Enterprise. Default classification: `Other`.
- **vs. `MSP/Aggregator`** — IT-managed-services pure plays (Kyndryl, NTT Data Services, DXC Technology) sit closer to MSP/Aggregator depending on procurement profile. Kyndryl specifically is `manual_review_required` — could be `MSP/Aggregator` or `Outsourcing Services - Enterprise` depending on lens.
- **vs. `Financial Services - Enterprise`** — Genpact serves FS clients but IS a BPO, not FS. The BPO classifies on its own operations, not its clients'.
- **vs. Watch List Logistics** — DHL Supply Chain is logistics (Watch List), NOT BPO.
- **vs. Staffing firms** — Allegis, Kelly Services, ManpowerGroup are staffing, not BPO. Hard exclude.
- **vs. Healthcare** — Healthcare RCM firms (R1 RCM, Ensemble Health Partners) are Outsourcing, not Healthcare.

### Selling angle (M&A network integration as default E1 anchor)

**Lead (M&A anchor — default for FS + OS):** "Concentrix-Webhelp / TP-Majorel — two MPLS cores, two AD forests, years of parallel WAN. Every new client adds an MPLS tail and a compliance attestation. The integration cost is mostly network." Pivot to: "M&A integration on one fabric — controller decision, not BGP convergence."

**Secondary angles:** Delivery-center reliability across geographies (Manila → Cebu failover, Super Typhoon Nov 2025 board-level moment); client data sovereignty (their clients' regulated data riding their network — DORA flow-down, India DPDP, RBI 2025); new-client onboarding 14 weeks → 3 weeks (Use Case 7); per-tenant audit trails for client InfoSec audits.

**Rebase off per-seat (the seat-volume premise is eroding):** AI is decoupling BPO revenue from headcount (Genpact's CEO says the business is moving off per-seat; Teleperformance is among Europe's most-shorted names on that fear), so the per-seat ramp story is the wrong lead. Keep "every new client adds a tail," but anchor it to the regulatory/outcome frame:
- **SOVEREIGN (primary)** - per-client jurisdictional path proof. RBI 2025 directions, April 2026 deadline, require proof that an Indian client's data never sits where a foreign regulator can reach it; DPDP and DORA flow-down stack the same obligation. The tail each client adds is a jurisdictional attestation, not a seat count.
- **REDUNDANT** - uptime is margin when the BPO bills per resolution instead of per seat. The path that fails the jurisdictional audit is the one eating margin every minute it wobbles.
- **AUTOMATED** - fast nearshore site activation (CGS Colombia, VXI Egypt class); the carrier install gates the client commit date.

**Use Case 5 (M&A) + Use Case 7 (new site bring-up) are co-leads.** Use Case 8 (audit-ready policy enforcement) when recipient is Chief Compliance or InfoSec lead.

### HubSpot fields R1/R2 must populate

| Field | Target value |
|---|---|
| `customer_segment` | `Enterprise-CustomerSegment` |
| `company_sub_segment` | `Outsourcing Services - Enterprise` |
| `segmentation_confidence` | per Confidence scoring rules below |
| `account_tier` | `tier_2` ceiling; `tier_3` default |
| `recent_news_or_trigger_event` | M&A close / new delivery center / regulatory designation / typhoon-class BCP event |

### Signal source coverage

- **E-A1** New delivery center / N-seat ramp (Nelson Hall, Everest Group, TaskUs Medellín + Cali)
- **E-A2** M&A — constant (Concentrix-Webhelp, TP-Majorel, Cognizant-Astreya)
- **E-A3** AI moves (Cognizant Neuro + NVIDIA, Genpact AI Gigafactory + GE Vernova, Teleperformance + Azure OpenAI 170 markets)
- **E-A4** VP Delivery Center Network / Client Connectivity hire
- **E-A5** DORA flow-down, India DPDP, RBI 2025 NBFC Outsourcing Directions, Genpact BCR-Processor (May 2024)
- **E-A6** Equinix Fabric / Megaport / Console Connect customer-win
- **E-B2** Peer ransomware / Super Typhoon Uwan/Fung-wong Nov 2025 (98 PH BPO sites under DOLE investigation)

### Contact personas (priority + procurement)

**Buying committee:**
- **Technical Champion** — Director Delivery Center Network, Principal Network Engineer (Client Connectivity), Network Architect, Director Site Operations Network
- **Business Sponsor** — VP Network Infrastructure, VP Delivery Operations, Head of Connectivity Engineering
- **Economic Buyer** — CIO, CTO, COO (BPO COOs are often network-aware)
- **Security Stakeholder** — CSO / CISO, Director Client InfoSec, Director Third-Party Risk
- **Compliance** — Chief Compliance Officer, Head of Client Audit Response, Head of Data Privacy (BCR/SCC owner)

**Procurement personas:**
- **Chief Procurement Officer** — direct contracts with major carriers + interconnection fabrics
- **VP Vendor Management — Network/Telecom**
- **Director Strategic Sourcing — IT / Telecom**

Persona priority: **VP Network Infrastructure → CSO/CISO → CIO**.

### Confidence scoring rules

| Confidence bucket | Criteria |
|---|---|
| `high_90` | Anchor list match OR Everest Group PEAK Matrix top-quartile + 30+ delivery centers + multi-country + in-house team verified + BPS revenue $1B+ |
| `medium_7089` | 2 of {anchor list, Everest top-quartile, 30+ delivery centers, multi-country, in-house team, BPS rev $1B+}. |
| `low_5069` | Scale gate passes but delivery-center count not verified OR operational vs consulting revenue mix unclear. |
| `manual_review_required` | (a) Dual-arm firms where operational vs consulting mix is ambiguous (Accenture parent vs Operations, IBM Consulting vs IBM hybrid cloud); (b) Single-vertical BPOs at scale-gate boundary (R1 RCM $2.5B, Firstsource $750M); (c) Captive vs market-facing BPO unclear; (d) IT-managed-services pure plays (Kyndryl, NTT Data Services, DXC) where MSP/Aggregator vs Outsourcing classification is contested. |

### Industry sources

- **Everest Group PEAK Matrix** (BPS, CXM, IT Services)
- **NelsonHall NEAT** reports (BPS, CMS)
- **ISG Provider Lens** (BPS, IT Services)
- **Gartner Magic Quadrant** — Customer Experience BPO, Finance & Accounting BPO
- **NASSCOM** (India BPO trade body) member directory
- **Fortune 500** + **Forbes Global 2000** (BPS subsection)
- **Equinix Fabric Customer Directory** + **Megaport Customer Directory**
- **SEC EDGAR** (public BPOs: Concentrix, TaskUs, Genpact, Cognizant, Conduent, Sutherland) — 10-K Item 2 delivery-center list
- **Indian regulator portals** — RBI NBFC Outsourcing Directions, DPDP cross-border framework
- **EU DORA portals** (EBA / ESMA / EIOPA) for CTPP designations affecting BPO clients
- **Nelson Hall + Everest Group + ISG conference agendas** (CCW, NASSCOM, BPO Connect)
- **Economic Times India IT**, **Business Standard India**, **Inquirer Manila tech beat**

---

## Critical clarifications (consolidated)

### 1. Diversified industrials with multi-DC corporate IT (Honeywell, GE HealthCare, 3M)

**Policy:** When a diversified industrial has a stand-alone corporate IT footprint that matches the multi-DC scale gate AND its commercial procurement profile dominates network spend, classify under `Financial Services - Enterprise` (mirrors the defense-contractor rule). When plant-OT spend dominates, hold as `Other`. **Default: `manual_review_required`.** Examples requiring case-by-case review: Honeywell Connected Enterprise, GE HealthCare (post-spinoff), 3M corporate IT, Caterpillar, Deere & Company, Emerson Electric.

### 2. Outsourcing hard exclusion of consulting firms (verified)

Deloitte, McKinsey, BCG, Bain, Oliver Wyman, AlixPartners are project-based consulting firms, NOT Outsourcing Services - Enterprise. They lack operational delivery centers in the BPO sense. **Hard exclude.**

**Pressure-tested dual-arm firms:**
- **Accenture Operations** (operational BPS) → qualifies as standalone `Outsourcing Services - Enterprise` classification
- **Accenture (Strategy & Consulting)** → does NOT qualify
- **Cognizant, Wipro, TCS, Infosys, Capgemini** → qualify on their operational BPS arms (Cognizant Neuro/BPS, Wipro BPS, TCS BPS, Infosys BPM, Capgemini Business Services)
- **IBM Consulting** → does NOT qualify as Outsourcing; IBM hybrid cloud / managed infrastructure could land elsewhere; default `manual_review_required`

### 3. Healthcare anchor verification (as of 2026-05-14)

All 12 NA Healthcare anchors verified still independent + multi-DC + Epic-instance customers: HCA Healthcare, Ascension, CommonSpirit, Kaiser Permanente, Cleveland Clinic, NewYork-Presbyterian, Mass General Brigham, Trinity Health, UPMC, Banner Health, Providence, Intermountain Health.

**Additional verified anchors surfaced beyond the original 6:** Mass General Brigham, Trinity Health (Livonia - NOT the UPMC target; see anchor #8 correction), UPMC (consolidating from 9 EHRs; acquiring CommonSpirit's Ohio "Trinity Health System," close Fall 2026), Banner Health, Providence, Intermountain Health (post-SCL merger).

**EU/APAC anchors added:** NHS England trust-level (Manchester University, Imperial College), Karolinska/Region Stockholm, Apollo Hospitals India.

**Watch flags:** Tenet Healthcare (USPI segment now larger than hospital segment — `manual_review_required` on whether to classify on hospital arm); BJC + St. Luke's merger close watch.

### 4. Energy/Utilities Watch List confirmation

**Confirmed NOT ICP** as of 2026-05-14. Reasons:
- NERC CIP procurement cycles run 18-36 months
- No FedRAMP for the PCE yet (FedRAMP-adjacent compliance maturity required before utilities engage)
- SCADA fit is technically real but operationally distant from MaiaEdge's current GTM

**Future-expansion trigger to revisit:** When (a) MaiaEdge achieves CMMC L2 / FedRAMP-adjacent compliance, AND (b) the utility has a dedicated NERC CIP procurement team standing up new vendor relationships. Until BOTH hold, do NOT enrich speculatively. Examples to revisit later: Duke Energy, Southern Company, NextEra Energy, Exelon, Dominion Energy, Pacific Gas & Electric, American Electric Power, Xcel Energy.

---

*End of Phase B + C — Enterprise. 4 sub-segments fully scoped. Geographic spread: 47 NA + 7 EMEA + 4 APAC anchors across the four sub-segments (Enterprise lands mostly NA + EMEA as expected; APAC restricted to Outsourcing-heavy + 2 Healthcare/Retail outliers).*
