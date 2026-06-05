# Enterprise (Multi-DC ICP) - Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` (scoring, cadence, delivery format) and `segments/enterprise.md` (ICP, sub-segments, language banks, hard gates) and `segments/enterprise-use-cases.md` (8 priority use cases × signal triggers per use case).

HubSpot `customer_segment`: **Enterprise-CustomerSegment** (display label "Enterprise"). ICP promoted 2026-05-11. Priority 5 (lowest of the ICPs but qualified and sellable).

Sub-segments (only these four):
- **Financial Services - Enterprise**
- **Healthcare Systems - Enterprise**
- **Retail and Distribution - Enterprise**
- **Outsourcing Services - Enterprise**

**Anchor account:** Meijer (`Retail and Distribution - Enterprise`, Ken Cunningham + Woody Acosta + Mark Szymanski). Active April 2026 design on PBC + Port Extender for HAsync/HAfabric dark fiber diversity to SSR1300 nodes between data centers.

**Hard sourcing gate (BOTH must pass before any Enterprise-tagged record is created or scored):**
- **Vertical gate:** one of the four sub-segments above.
- **Scale gate:** $1B+ revenue AND (3+ DCs OR direct Equinix Fabric / Megaport port OR confirmed in-house network engineering team via NOC presence or VP/Director/Principal Network Engineering job postings).

**Out-of-scope (Watch List, do NOT tag as Enterprise):** Manufacturing, Energy/Utilities, Logistics/Supply Chain. Government/Defense (FedRAMP-gated). Sub-$1B mid-market. Single-DC. Network fully outsourced to single MSP. No direct carrier contracts.

---

## Tier A - Meeting-Ready Signals (≤60d window, +60-90d decayed per signal-framework.md)

### E-A1. New DC Build / DC Expansion / Major Capacity Add

**Why it predicts a meeting:** Every new DC = a fresh fabric decision (inter-DC dark fiber pair sizing, on-ramp design, BCP path topology). Existing DC capacity uprate at multi-DC enterprises means the connectivity envelope is being redesigned - incumbent carrier wave contracts may not survive the redesign. Hits **all four sub-segments**, hardest at Retail (DC + DC opening cycles every 2-3 years) and Healthcare Systems (acquired-hospital cutover onto parent Epic instance).

**Source:** Modern Healthcare DC + IT capex coverage, Retail Dive store/DC openings, American Banker tech-spend disclosures, Nelson Hall + Everest Group BPO delivery-center expansion, Bisnow Data Center + DC Frontier (when enterprise IT is the lessee), SEC 10-K (Item 2 Properties + capex disclosures), regional business journals (Lakeland Ledger for Publix; Grand Rapids Business Journal for Meijer; Idaho Statesman for Albertsons; etc.).

**Pattern (regex variants):**
- `("opens"|"announces"|"unveils") + ("data center"|"corporate IT campus"|"distribution center"|"delivery center") + (named enterprise + ICP-vertical signal)`
- 10-K Item 2: new entries to Owned Properties list with "data center" or "computing facility" tag
- Regional press: `(town name) + ("breaks ground"|"under construction"|"new corporate IT") + (enterprise name)`

**Sub-segment-specific patterns:**

| Sub-segment | Trigger language to scrape for |
|---|---|
| Retail and Distribution | "new fulfillment center," "Symbotic deployment," "robotics-enabled DC," "regional flow center," "new home office IT campus" |
| Healthcare Systems | "acquired hospital go-live," "Epic Hyperdrive cutover at [acquired site]," "new IDN data center," "PACS consolidation site" |
| Financial Services | "new corporate IT campus," "trading-floor-adjacent build," "NY4/NY5 colo expansion," "European data center launch" |
| Outsourcing Services | "new delivery center," "[N]-seat ramp announcement," "nearshore expansion," "Manila/Pune/Bangalore capacity add" |

**Anchor proof points (real 2024-2026 examples to validate scrapers against):**
- Publix Lakeland IT campus expansion (2024-2025)
- Home Depot CIO Angie Brown appointment (June 2025) → followed by infrastructure modernization announcements
- Albertsons FY2025 capex $1.7-$1.9B with Azure preferred public cloud
- TaskUs Medellín + Cali simultaneous opening (2025)
- HCA Healthcare expansion announcements (ongoing)

**Freshness:** 60d. **Confidence:** HIGH when the named DC is a corporate IT facility (not a leased colo cabinet); MEDIUM when only press release. Validation pattern: enterprise's own press release [Robust] + 10-K cross-reference [Robust] OR 2 trade press [Robust].

---

### E-A2. Definitive M&A Agreement (Announcement OR Close - two-event firing)

**Why it predicts a meeting:** Every enterprise M&A creates a 18-36 month network integration project - two ADs, two MPLS cores, two SD-WAN orchestrators, two security stacks, two cloud-account hierarchies. The "integration cost" line in M&A press releases is mostly network and identity. **Two distinct windows:**
- **At announcement** (deal signed, not yet closed): pre-close integration planning is active. Engaging during this window = on the shortlist when the ops plan locks.
- **At close** (deal complete): Day 60-120 post-close = the integration sweet spot. Pain is acute, new leadership is authorized to spend.

If both events fire on same enterprise within 12 months → **+6 stacking auto-elevation** per signal-framework.md.

**Sub-segment fit:**
- **Financial Services** - HIGH. Capital One / Discover (closed May 18 2025), BMO / Bank of the West, Truist post-merger trailing integration. Banks acquire whole regional banks every cycle.
- **Healthcare Systems** - HIGH. Hospital M&A is constant. CommonSpirit's South region single-Epic go-live (June 2025), UPMC consolidating from 9 EHRs, UPMC-Trinity-Ohio closing 2026, BJC + St. Luke's.
- **Outsourcing Services** - HIGH. Concentrix + Webhelp (closed Sep 2023), Teleperformance + Majorel (integration complete early 2025), Cognizant + Astreya (April 2026). Every major BPO is mid-integration.
- **Retail and Distribution** - LOW. Kroger-Albertsons merger killed Dec 2024. Fires when retail M&A returns (Tapestry/Capri, others).

**Source:** SEC 8-K Item 1.01 + S-4 (announcement), SEC 8-K Item 2.01 (close). Trade press: American Banker M&A tracker, Modern Healthcare deal coverage, Nelson Hall BPO M&A, Retail Dive merger coverage. Aggregators: Mergermarket, S&P Global Market Intelligence, PitchBook.

**Pattern (announcement):** `("announces"|"to acquire"|"agreement to acquire"|"definitive agreement"|"to merge with"|"signs definitive") AND (named enterprise in one of the four ICP sub-segments)`

**Pattern (close):** `("acquires"|"completes acquisition"|"closes acquisition"|"completes merger"|"closes combination") AND (named enterprise in one of the four ICP sub-segments)`

**Validation pattern:** SEC filing [Robust] + ≥1 trade press [Robust] OR 2 independent trade press [Robust]. Single trade press → MEDIUM with "single-source pending second confirmation" flag.

**Freshness:** ≤60d from whichever event is more recent = full Tier A. 60-90d = decayed. >90d from both = drop. **Confidence:** HIGH (cross-source confirm).

---

### E-A3. AI / GPU Workload Announcement Requiring Enterprise GPU Connectivity

**Why it predicts a meeting:** Enterprises announcing GenAI deployments (especially direct GPU-cluster contracts with CoreWeave / Lambda / Crusoe / Nebius) need a private path from corporate network to neocloud GPU clusters. East-west fabric between corporate DC and GPU site wasn't in the 3-year plan. Public-internet inference latency doesn't survive trading-floor or agent-assist consumers of the output. Hits Financial Services hardest (JPMorgan IndexGPT, Goldman GS AI, Morgan Stanley Knowledge Assistant, Bloomberg LLM); Outsourcing Services on agent-assist (Cognizant Neuro AI + NVIDIA, Genpact AI Gigafactory with GE Vernova, Teleperformance + Azure OpenAI 170 markets).

**Source:** WSJ + American Banker tech beat, Bloomberg AI coverage, Modern Healthcare AI vendor announcements, Retail Dive GenAI coverage (Walmart Sparky / WIBEY, Lowe's Mylow, Albertsons / Kroger), Nelson Hall + Everest Group BPO AI moves, NVIDIA partner press (Cognizant Neuro, Teleperformance), CoreWeave / Lambda / Crusoe / Nebius enterprise customer wins, SEC 8-K (when GPU compute contracts hit material thresholds).

**Pattern:**
- `(enterprise name) + ("announces"|"deploys"|"launches"|"goes live with") + ("GenAI"|"AI agent"|"LLM"|"AI assistant"|"agentic")`
- `(enterprise name) + ("partnership with"|"contract with"|"commits to") + ("CoreWeave"|"Lambda"|"Crusoe"|"Nebius"|"Together AI"|"NVIDIA DGX")`
- New Chief AI Officer / Chief Data + AI Officer hire at named ICP enterprise (cross-fires with E-A4)

**Specific 2024-2026 anchor examples to seed scrapers:**
- JPMorgan Chase IndexGPT (research-grade), Goldman Sachs GS AI, Morgan Stanley Knowledge Assistant + Wealth Advisor Copilot
- Walmart Sparky / WIBEY agents (production 2025)
- Lowe's Mylow at 1,700+ stores
- Cognizant Neuro AI + NVIDIA (March 2025), Genpact AI Gigafactory with GE Vernova (Jan 2025)
- Teleperformance Azure OpenAI across 170 markets (post-Majorel integration, early 2025)

**Freshness:** 60d post-announcement (the integration window opens once the AI workload has a production user base, not on launch day). **Confidence:** HIGH on Tier 1 enterprise + named GPU partner; MEDIUM when "AI strategy" is announced without specific compute provider.

---

### E-A4. Executive Hire - VP Network Infrastructure / Director Network Engineering / Principal Network Engineer

**Why it predicts a meeting:** New leader's 90-day plan always includes auditing the inherited network architecture. Inter-DC determinism, dark fiber redundancy, and cloud on-ramp ownership are the three areas they're most likely to flag for replacement. **Highest-confidence relationship-entry signal at the technical-champion persona** - they own the path, the runbook, and the 2am page. Apply to all four sub-segments.

**Source:** SEC 8-K Item 5.02 (officers of public ICP enterprises), PR Newswire / Business Wire "People on the Move" tag, American Banker leadership column (Financial Services), Modern Healthcare + Becker's Hospital Review IT leadership column (Healthcare Systems), Retail Dive "Movers and Shakers" + RIS News (Retail and Distribution), Nelson Hall + Everest Group BPO leadership briefs (Outsourcing Services), enterprise IR newsroom RSS, LinkedIn "excited to join" public posts at target enterprise list, Apollo job-change feed (cross-references with persona target list).

**Pattern (title contains AND start_date < 90d AND company in Enterprise target list):**
- `(VP|SVP|Director|Head|Principal) + (Network Infrastructure|Network Engineering|Network Architecture|Infrastructure Engineering|Connectivity|WAN|Data Center Networking)`

**Sub-segment-specific patterns:**

| Sub-segment | Title patterns that signal hardest |
|---|---|
| Financial Services | + "Markets Network," "Trading Infrastructure," "Connectivity Engineering" (NY4/NY5 / co-lo adjacency) |
| Healthcare Systems | + "Clinical Network Operations," "EHR Infrastructure," "Imaging Network" |
| Retail and Distribution | + "Store-and-DC Network," "Distribution Network Operations," "Retail Connectivity" |
| Outsourcing Services | + "Delivery Center Network," "Client Connectivity," "Site Operations Network" |

**Validation pattern:** LinkedIn profile change [Robust] + (PR Newswire Appointments [Robust] OR SEC 8-K Item 5.02 [Robust] OR enterprise IR press) → HIGH. Apollo or LinkedIn alone → MEDIUM with "single-source pending second confirmation" flag.

**Freshness:** 30-90d post-hire (not Day 1 - give them time to get the inherited-architecture audit underway). **Confidence:** HIGH on cross-source confirmation.

---

### E-A5. Regulatory Enforcement Event / New Framework Effective Date

**Why it predicts a meeting:** Every regulated enterprise - and at this point, all four ICP sub-segments are regulated - is being asked by auditors and examiners to prove **where data went**, not just that data was encrypted. New regulatory frameworks moving from "addressable" to "required" trigger network-architecture reviews. Hits all four sub-segments hard.

**Sub-segment fit + 2024-2026 anchor regulatory drivers:**

| Sub-segment | Regulatory triggers to scrape |
|---|---|
| Financial Services | DORA enforceable Jan 17, 2025; first CTPP designations Nov 18, 2025 (AWS, Microsoft, Google formally designated); NY DFS Part 500 amendments effective Nov 1, 2025 (MFA mandate, asset inventory); first NY DFS cert due April 15, 2026; ESMA EU T+1 target Oct 11, 2027; FFIEC BCM IV.A.6 physical-path verification. |
| Healthcare Systems | HIPAA Security Rule NPRM (Dec 27, 2024) - proposes removing "addressable" flexibility on encryption-in-transit + segmentation, mandates TLS 1.3+; HSCC Sector Mapping & Risk Toolkit (Oct 2025); HSCC Updated Model Contract Language (Nov 2025); California AB 749 (effective Jan 1, 2025) - zero-trust microsegmentation for connected medical devices at CA hospitals; HHS OCR breach disclosures (the public "wall of shame"); HITRUST r2 expansions. |
| Retail and Distribution | PCI DSS v4.0 fully in effect March 2025 - 64 new requirements, continuous segmentation validation, annual scope re-attestation. |
| Outsourcing Services | DORA flow-down to every EU-financial-services BPO client; India DPDP Rules notified 2025 + cross-border framework (Rule 15) live; RBI 2025 NBFC Outsourcing Directions + IFS Cloud launch - Indian FS BPO arms must process onshore; client InfoSec audits demand path-level proof. |

**Source:** Regulator portals (NY DFS, HHS OCR portal, FFIEC, PCI Council, CFPB), DORA enforcement updates from EBA / ESMA / EIOPA, SEC EDGAR for 8-K Item 8.01 disclosures of regulatory matters, enforcement-action news from American Banker (FS) + Modern Healthcare HIPAA breach coverage + Becker's HIPAA breach roundup + RIS News PCI coverage + Nelson Hall regulatory briefs (BPO).

**Pattern:**
- HIPAA breach: HHS OCR portal entry of named enterprise + breach size + records-affected ≥ 100k
- NY DFS enforcement: announced consent order / settlement against named bank
- PCI Council: assessor-found-issue press releases (rare; usually surfaces via American Banker / RIS News reporting on CISO statements)
- DORA CTPP: ESMA / EBA designation announcements
- General "enforcement action" + named ICP enterprise

**Anchor 2024-2026 incidents to seed scrapers:**
- Change Healthcare BlackCat (Feb 2024, 190M records, $3.09B annual hit) - every IDN board demanded segmentation review
- Ascension Black Basta (May 2024, 5.6M patients) - segmentation lessons learned
- Yale New Haven (March 2025)
- Oracle Cerner deletion incident (April 2025, 39-45 CHS hospitals on paper for 5 days)
- Hot Topic Nov 2024 (57M customers via third-party analytics vendor Robling) - retail-side third-party-risk wake-up
- CDK Global dealer outage 2024 - automotive distribution segmentation reviews
- Shopify Cyber Monday outage Dec 1, 2025 (5-6 hours during a $14.2B day)

**Freshness:** ≤60d post-event for breach / enforcement disclosure. New framework effective date: ≤30d post-effective is hottest; ≤90d still actionable as enterprises stand up compliance plans. **Confidence:** HIGH on regulator-portal source + named enterprise.

---

### E-A6. Equinix Fabric / Megaport / PacketFabric / Console Connect Customer Win Naming a Named Enterprise

**Why it predicts a meeting:** Inverse signal - when an interconnection-fabric vendor publishes a customer-win press release naming a Tier 1 enterprise, it confirms the enterprise has an active multi-cloud / multi-DC connectivity buying motion AND is currently committed to a third-party fabric vendor (the exact incumbent MaiaEdge displaces in the cloud-on-ramp use case). Cross-fires with E-A3 (AI workloads need new on-ramp) and E-A1 (DC expansion forces a new on-ramp).

**Source:** Equinix newsroom + customer-story page, Megaport customer-success page + press releases, PacketFabric customer-logos page, Console Connect (PCCW Global) press, CoreSite customer announcements, Cologix customer wins. Wayback Machine month-over-month diffs of these vendor pages catch silent additions.

**Pattern:**
- `("Equinix Fabric"|"Megaport"|"PacketFabric"|"Console Connect") AND ("customer story"|"case study"|"selects"|"deploys"|"goes live with") AND (named enterprise in one of four ICP sub-segments)`

**Validation pattern:** Vendor press release naming the enterprise + enterprise's own quote / spokesperson [Robust] → HIGH. Vendor case study without enterprise spokesperson → MEDIUM (vendor-only voice; the enterprise hasn't actively endorsed).

**Freshness:** 60d (the contract is live; the renewal timer starts ticking). **Confidence:** HIGH when both vendor + enterprise voices appear; MEDIUM when only the vendor speaks.

---

### E-A7. SOX 10-K / Annual Report Disclosure of Network / IT Modernization Initiative

**Why it predicts a meeting:** 10-K Risk Factors and MD&A sections increasingly disclose IT-modernization programs (including network rearchitecture) when material to operations. Enterprises with multi-DC footprints describing "network modernization," "infrastructure consolidation," or "third-party connectivity dependencies" in their annual report = budget-authorized initiative already in flight. Hits Financial Services hardest (most disclosure-heavy); Healthcare Systems and Retail also fire when initiative is large enough to be MD&A-material.

**Source:** SEC EDGAR full-text 10-K + 10-Q + 20-F (foreign private issuers), Risk Factors + MD&A + Properties sections, proxy statements (DEF 14A) when CIO compensation discussion mentions network/infrastructure programs.

**Pattern:**
- `(10-K|10-Q|20-F) AND ("network modernization"|"infrastructure consolidation"|"data center modernization"|"connectivity transformation"|"WAN modernization"|"SD-WAN deployment"|"cloud connectivity transformation") AND (filer is an ICP enterprise in one of the four sub-segments)`
- Risk Factors mention of "third-party connectivity provider risk" or "concentration risk on cloud interconnect providers" (the DORA ripple)
- MD&A mention of "elevated IT capex" tied to network/connectivity initiative

**Freshness:** 90d post-filing (10-Ks are quarterly-cadence signals; the program described is typically multi-quarter). **Confidence:** HIGH (SEC filing is Robust source).

---

## Tier B - Strong Signals (30-60d window)

### E-B1. Senior Network Role Job-Posting Surge at a Named Enterprise

**Why:** 3+ concurrent reqs for VP/Director/Principal Network roles at a Tier 1+2 enterprise = standing up something new. Indicates budget + roadmap. Less acute than an exec-hire announcement (E-A4) but a strong leading indicator on its own; stacks with E-A4 within the same 30-day window.

**Source:** LinkedIn Jobs + Indeed + Greenhouse + Lever + Ashby (the public, ATS-fronted boards), enterprise careers pages.

**Pattern:** Same enterprise, ≥3 active reqs in 30d matching `(network architect|network engineer (principal|staff|senior)|infrastructure architect|connectivity engineer|WAN engineer|cloud network engineer|SDN|automation engineer|fabric engineer)` AND the requisitions reference DC / WAN / inter-site / multi-cloud responsibilities (filter out branch / SD-WAN / facility-only roles unless paired with multi-DC scope).

**Freshness:** 30d. **Confidence:** HIGH when via Greenhouse / Lever / Ashby (Robust); MEDIUM when LinkedIn-Jobs-only (Aspirational layout drift).

---

### E-B2. Recent Ransomware / Public-Disclosure Incident at a Peer in the Sub-Segment

**Why:** Industry-wide segmentation reviews follow notable incidents. After Change Healthcare (Feb 2024) and Ascension (May 2024), every IDN audit committee added segmentation review to the agenda. This is a "segment-wide buying-motion shift" signal, not an account-specific signal - fire when the incident is at a peer in the sub-segment AND the segment-wide agenda shift is observable.

**Source:** Same as E-A5 (regulator portals, trade press incident coverage). Add: rating agency notes (Moody's / S&P Global cyber-incident impact briefs), enterprise risk-management trade press (Risk & Insurance, ISMG GovInfoSecurity).

**Pattern:** `(named ransomware incident at peer enterprise) AND (peer in same Enterprise sub-segment) AND (≤90 days post-disclosure)` - score against ALL Tier 1+2 enterprises in the same sub-segment, not just the affected one.

**Freshness:** 90d. **Confidence:** MED (signal on the segment, not the account; pair with E-A4 or E-A1 on a specific account to elevate to Tier A scoring).

---

### E-B3. New Cloud / Multi-Cloud Migration Kickoff Announcement

**Why:** Enterprise announcing "migrating workloads to AWS / Azure / GCP" or "adopting multi-cloud strategy" reveals an active connectivity-design window. Cloud on-ramp pain (the use case 2 in `enterprise-use-cases.md`) lands hardest within 6 months of the migration kickoff announcement.

**Source:** Enterprise IR press releases + earnings call mentions, AWS / Azure / GCP customer case studies + customer logo pages, hyperscaler announcement feeds (AWS What's New, Azure announcements, Google Cloud blog).

**Pattern:** `(named ICP enterprise) AND ("migrating to"|"adopting"|"deploying on"|"strategic partnership with") AND (AWS|Azure|GCP|Oracle Cloud|multi-cloud|hybrid cloud)`

**Freshness:** 90d. **Confidence:** MED-HIGH when paired with named cloud + named enterprise spokesperson.

---

## Tier C - Context Signals (60-90d window, paired-only per signal-framework.md)

### E-C1. Industry Conference Speaking Slot - Network / IT Architecture Track

**Why:** Enterprise CTO/CIO/VP Network publicly framing network / connectivity / multi-cloud as a strategic priority will take pre-event meetings. Context-only when alone (per signal-framework.md noise list); fires only when stacked with another Enterprise signal on the same account in the same 30-day window.

**Source:** Sibos (financial services), Money 20/20 (financial services), AFP Annual Conference (corporate finance/treasury), HIMSS + CHIME (healthcare IT), Becker's IT + ViVE (healthcare IT), NRF Big Show + Shoptalk + RILA (retail), CCW + NASSCOM + BPO Connect (BPO), Gartner IT Symposium / Xpo, AWS re:Invent enterprise track, Microsoft Ignite / Build enterprise sessions.

**Pattern:** Agenda scrape, filter speakers by company type = ICP Enterprise sub-segment, panel titles matching `(network|connectivity|fabric|inter-DC|cloud connectivity|multi-cloud|sovereignty|audit|segmentation|zero trust)`.

**Freshness:** 30d pre-event / 14d post-event. **Confidence:** HIGH that the speaker is engaged on the topic; LOW that it's a buying signal alone - fires only when stacked.

---

### E-C2. Earnings Transcript Mention of Network / Infrastructure Pain or Investment

**Why:** CEO/CFO/CIO mentioning inter-DC connectivity, dark fiber, third-party fabric dependencies, or AI infrastructure connectivity gaps on an earnings call = internal heat. Earnings transcripts are quarterly-cadence so freshness is structurally 90d; pair with a more acute signal (E-A1 / E-A3 / E-A4) to elevate.

**Source:** SEC 10-Q earnings transcripts (full-text), Seeking Alpha transcripts, enterprise IR investor-day deck mentions.

**Pattern:** `(transcript|earnings call|investor day) AND ("inter-DC"|"network modernization"|"third-party fabric"|"connectivity provider"|"AI infrastructure"|"GPU connectivity"|"cloud on-ramp") AND (filer is ICP Enterprise)`

**Freshness:** 90d. **Confidence:** MED.

---

### E-C3. Tenant of an Equinix / CoreSite / Cologix Facility - Inferred via Customer-Logo Page

**Why:** Enterprise appearing on Equinix / CoreSite / Cologix customer-logo page = confirmed multi-DC connectivity buyer with cross-connect dependency. Signals that the cloud-on-ramp + dark-fiber-redundancy use cases are LIVE pains. Context-only signal - fires only when stacked.

**Source:** Equinix customer-logo page, CoreSite logo wall, Cologix customer page, Wayback Machine diffs of these pages.

**Pattern:** `(named ICP enterprise) appears on (colo customer-logo page) AND (date of first appearance ≤90d) AND (paired with another Enterprise signal on the same account in same 30d window)`

**Freshness:** 90d. **Confidence:** MED-HIGH on appearance; LOW alone.

---

## Explicitly NOT Tracked (noise - do NOT surface even when patterns match)

These signal patterns intentionally excluded per signal-framework.md noise list + Enterprise-specific filtering:

- **"AI Practice" launches at consulting firms inside Enterprise sub-segments** (Deloitte, McKinsey, BCG, Bain) - those are project firms, NOT Outsourcing Services - Enterprise. Do not score.
- **Generic IT modernization press releases** without specific network/connectivity programs.
- **Branch SD-WAN deployments at retailers** - branch is saturated (per `context/segments/enterprise.md` Industry Landscape); inter-DC + cloud-on-ramp is the live conversation.
- **Manufacturing plant network expansions** - fails the vertical gate (Watch List, not Enterprise ICP).
- **ESG / sustainability data center announcements** without operational connectivity mention.
- **Conference sponsorship logos** (vs. speaking slots) - sponsorship is marketing-team budget, not network-team intent.
- **LinkedIn posts about "AI strategy"** without specific compute provider or production deployment.

---

## Sources for This Segment (scrape weekly - pruned 2026-05-11)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework.

**Search-anchor pattern is the canonical access method** - direct `web_fetch` is gated by URL-provenance on Cowork's runtime. Anchor each source via `web_search "{domain} {topic} {year}"` and read snippets from search results. Article URLs returned in search can then be fetched directly. Do NOT skip a documented source because direct fetch fails - use search anchoring.

### Robust tier (single-source can score at HIGH for non-major signals)

1. **StockTitan** (SEC 8-K mirror with parsed summaries - `stocktitan.net/sec-filings/{ticker}/`) - primary surrogate for SEC EDGAR direct queries on public Enterprise targets; covers 10-K, 10-Q, 8-K (Items 1.01, 2.01, 5.02, 8.01), DEF 14A, 20-F [Robust]
2. **SEC EDGAR full-text via search-anchor** - backup to StockTitan; preferred for foreign-private-issuer 20-F filings and DEF 14A proxy filings [Robust]
3. **PR Newswire + Business Wire + GlobeNewswire** - Data Center / Healthcare / Banking / BPO tags + "People on the Move" + "Appointments" tag [Robust]
4. **American Banker** - IT, leadership, regulatory, M&A coverage of US banks + insurers + payment networks [Robust]
5. **Modern Healthcare** - IT capex disclosures, M&A coverage, leadership moves at multi-hospital IDNs [Robust]
6. **Becker's Hospital Review** - IT leadership column, HIPAA breach roundup, IDN expansion coverage [Robust]
7. **Retail Dive** - store/DC openings, retail IT coverage, M&A [Robust]
8. **Nelson Hall** - BPO leadership briefs, deal coverage, AI moves at outsourcing services providers. **Awareness-tier only** - most content subscription-gated; search-anchor leaks self-promo blurbs about NEAT reports / market studies, not full article bodies. Treat as vendor/market awareness, not specific-account triggering [Robust → awareness-tier]
9. **Everest Group** - BPO + IT services rankings, deal news, leadership moves [Robust]
10. **Greenhouse + Lever + Ashby** public job boards - senior network role job postings at target Enterprise list [Robust]
11. **Apollo MCP** - `apollo_organizations_enrich` for firmographics + Apollo Job Postings filter + Apollo Job Changes filter - enrichment tool used at this cadence [Robust]
12. **Equinix newsroom + customer-story page** - customer wins naming Enterprise sub-segment accounts [Robust]
13. **Megaport customer-success page + press releases** - customer wins [Robust]
14. **PacketFabric + Console Connect customer-success pages** - third-party fabric customer wins [Robust]
15. **HHS OCR breach portal** (canonical source) + **HIPAA Journal monthly recap** (`hipaajournal.com` - operational mirror; portal itself is a JSF dynamic table not amenable to scraping) - Healthcare Systems trigger [Robust]
16. **NY DFS portal** - enforcement actions + Part 500 cert filings (Financial Services trigger) [Robust]
17. **PCI Security Standards Council news** - v4.0 enforcement coverage [Robust]
18. **DORA enforcement updates** - EBA / ESMA / EIOPA CTPP designations and supervisory expectations [Robust]
19. **NVIDIA Newsroom + Partner pages** - Cognizant Neuro, Teleperformance, enterprise GenAI + GPU partnerships [Robust]
20. **Earnings transcripts** - Seeking Alpha (free-tier headlines) + Motley Fool + MarketBeat + SEC 10-Q transcripts via StockTitan; keyword-filter for "network modernization" / "third-party fabric" / "private connectivity" / "GenAI infrastructure" / "DC consolidation" [Robust]

### Medium tier (cross-source confirm preferred for major M&A / regulatory claims)

21. **Bloomberg AI + tech beat** - enterprise GenAI deployments, GPU contract coverage [Medium - paywalled but headlines surface in search snippets]
22. **WSJ tech beat + CIO Journal** - enterprise IT capex, connectivity, AI strategy [Medium - paywalled but headlines surface]
23. **Risk & Insurance + ISMG GovInfoSecurity** - segment-wide segmentation reviews post-incident [Medium]
24. **CIO.com + InformationWeek** - enterprise IT leadership coverage [Medium]
25. **Bisnow Data Center** - enterprise as DC tenant (when leasing colo space) [Medium]
26. **Data Center Frontier + Data Center Dynamics** - enterprise-tenant lease coverage [Medium]
27. **Mergermarket + S&P Global Market Intelligence** - M&A deal coverage [Medium - Mergermarket subscription-gated, search-anchor leaks deal pipeline at headline level only; S&P Market Intelligence search-anchor surfaces quarterly M&A volume + sector deal stories]
28. **PitchBook public pages** - PE / strategic deal coverage [Medium]
30. **Crunchbase News** - enterprise tech leadership moves + acquisitions [Medium]
31. **HIMSS Media + CHIME news** - healthcare IT leadership + IDN coverage [Medium]
32. **RIS News + STORES Magazine** - retail IT coverage including PCI v4.0 reactions [Medium]
33. **Sibos / Money 20/20 / HIMSS / NRF / CCW / NASSCOM agenda pages** - speaker scrapes (context only) [Medium]
34. **Cross-segment exec hire stack** (per `signal-framework.md`): StockTitan 8-K Item 5.02, PR Newswire Appointments, IR newsroom diffs, Crunchbase Exec Moves - also covers E-A4 [Medium]

### Excluded (do NOT scrape - cut 2026-05-11)

- Wayback Machine month-over-month diffs of Equinix / Megaport / PacketFabric / CoreSite customer-logo pages - theoretical, never run. Equinix + Megaport + PacketFabric customer-success pages in Robust tier cover the same surface via search anchor.
- Glassdoor reviews - login-gated.
- Reddit r/networking + r/sysadmin + r/healthIT + r/fednews - low signal density.
- TheOrg.com diffs - Aspirational, never produced a signal.
- State business journals (Lakeland Ledger, Grand Rapids Business Journal, Idaho Statesman, Atlanta Business Chronicle, Phoenix Business Journal, Dallas Morning News, Tampa Bay Business Journal) - paywalled and redundant with trade press coverage of DC announcements at named ICP enterprise.
- YouTube transcripts (Sibos / HIMSS / NRF / CCW recordings) - compute-expensive, redundant with conference agenda scrapes.
- **AWS / Azure / GCP customer-case-study pages** - case studies are evergreen marketing assets without trigger dates; not signal-grade for a weekly scan. Use them as anchor-account-research databases at enrichment time (named customers like BMW, Mercedes, WRITER, Blue Origin surface) but not as fresh-signal feeds. Cut 2026-05-11.

LinkedIn public posts retained for **named-account research only** (specific company pages), not market-wide discovery - moved to `signal-framework.md`.

### 2026-05-11 reachability audit notes

All 27 Enterprise-specific sources tested on Cowork's runtime via search-anchor pattern. None structurally broken. Strongest single producers in audit:
- **Becker's Hospital Review** - strongest Healthcare Systems source (2026 CIO list, CMIO IT risk coverage)
- **GovInfoSecurity (ISMG)** - strongest Financial Services breach feed (ADT, Aflac, Dutch Min of Finance, Lloyds, Coupang all surfaced with dates)
- **Megaport + PacketFabric + Console Connect newsrooms** - highest-value Enterprise-specific feeds for customer-win signals (Latitude.sh, Massed Compute, Lisbon/Miami expansions all returned with dates)
- **PCI Security Standards Council** - Jan 2026 Annual Report, Board of Advisors, regional Engagement Boards all surfaced cleanly
- **EBA / DORA press** - 2026 Work Programme, ESAs Joint Committee, DORA Oversight Guide all reachable

Subscription-gated sources (WSJ, Modern Healthcare, Nelson Hall, Mergermarket) all leak headline-level data through search snippets; usable for awareness, weaker for specific-account triggering.

### Validation patterns per Tier A signal

| Signal | Validation rule for HIGH confidence |
|---|---|
| **E-A1 New DC / Expansion** | Enterprise's own press release [Robust] + 10-K cross-reference [Robust] OR 2 independent trade press [Robust]. Local business journal alone → MEDIUM |
| **E-A2 M&A (announcement OR close)** | SEC 8-K Item 1.01/2.01 [Robust] + ≥1 trade press [Robust] OR 2 independent trade press [Robust]. Single trade press → MEDIUM |
| **E-A3 AI / GPU workload** | Enterprise + named GPU partner co-cited [Robust] + production deployment language. "AI strategy" alone without compute provider → MEDIUM |
| **E-A4 Network exec hire** | LinkedIn profile change [Robust] + (PR Newswire Appointments OR SEC 8-K Item 5.02 OR enterprise IR press) [Robust]. Single source → MEDIUM |
| **E-A5 Regulatory event** | Regulator portal entry [Robust] + named enterprise OR 2 trade press confirming the event [Robust]. Single trade press → MEDIUM |
| **E-A6 Fabric vendor customer-win** | Vendor press + enterprise spokesperson quote [Robust] → HIGH. Vendor case study without enterprise voice → MEDIUM |
| **E-A7 10-K disclosure** | SEC EDGAR filing [Robust] alone is sufficient (filings are authoritative on company's own disclosure) → HIGH |

---

## International Sources (Tim Z's territory)

See `signal-framework.md` "International Source Stack" for the regional stack. Enterprise-specific international priorities:

**EMEA Enterprise:**
- **Financial Services:** Financial News London, Bobsguide, Risk.net (DORA + ECB CTPP coverage), European Banking Authority + ESMA + EIOPA portals.
- **Healthcare Systems:** EU healthcare IT trade press limited; track Big-3 EU integrated healthcare networks (Karolinska, NHS England trusts, Apollo Hospitals India for cross-region fit) via national regulator portals.
- **Retail and Distribution:** Retail Week (UK), Linéaires (France), Lebensmittel Zeitung (Germany).
- **Outsourcing Services:** Nelson Hall EMEA, BPO Connect EMEA. India BPO providers serving EU clients fall here for compliance overlap.
- Regulators: BNetzA Germany, ARCEP France, AGCOM Italy, CNMC Spain, ACM Netherlands, FCA UK (financial services).

**APAC Enterprise:**
- **Financial Services:** Asian Banker, Risk.net APAC, Nikkei Asia financial coverage.
- **Healthcare Systems:** Largely fragmented - surface single-IDN-equivalents (e.g., Apollo Hospitals India, Bumrungrad Thailand) via national press only.
- **Outsourcing Services:** This is the biggest APAC sub-segment (Cognizant + Tata + Wipro + Infosys + Genpact + Concentrix India operations + Manila / Cebu BPOs). Sources: Economic Times India IT, Business Standard India, Inquirer Manila tech beat, Nasscom (India BPO trade body), Contact Center Pipeline Asia.
- **Retail and Distribution:** Aeon Group / Walmart-equivalent Asian retailers - limited free coverage; surface via Nikkei + Reuters Asia tech.

**LATAM + MENA Enterprise:** Limited Enterprise ICP presence outside EMEA + APAC. Defer to opportunistic surfacing via cross-segment international sources documented in `signal-framework.md`.

---

**Cross-segment signal infrastructure:** Apollo-native and other cross-segment platform signals (job changes, headcount, intent, funding M&A) are documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Those signals apply here too and are not duplicated in this file. AP-1 (Apollo job change to target persona <90d) is an especially high-fit Apollo-native pairing for E-A4.

---

*Created: May 2026 (Enterprise ICP promotion + Phase 5 always-on automation rollout). Anchor account: Meijer.*
