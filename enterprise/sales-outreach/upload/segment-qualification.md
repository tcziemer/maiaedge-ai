# MaiaEdge Segment Qualification Framework

*Canonical reference for account qualification across all enrichment, classification, and outreach skills.*

---

## Why This Document Exists

Keyword matching produces false positives. A company with "colocation" on their website might be an IT hosting reseller. "Fiber network operator" could be a municipal broadband authority with no commercial services. "AI cloud" could be a software platform with zero GPU infrastructure. "MSP" could mean managed IT helpdesk, not telecom aggregation.

This framework replaces keyword-based routing with proof-based qualification. Every segment has required proof signals, quantitative minimums, and explicit disqualification signals. Classification requires evidence, not vocabulary.

---

## How to Use This Framework

1. **During enrichment (company-enrichment skill):** After Phase 1 website analysis routes a company to a likely segment, Phase 2 research must validate against this framework's proof requirements. A company only qualifies when it passes the Qualification Gate for its segment.
2. **During classification (segment-classification skill):** Before assigning a segment, check the company against the Qualification Gate. If proof signals are insufficient, flag for manual review instead of auto-classifying.
3. **During event processing (event-intelligence skill):** When classifying attendee/exhibitor lists, apply the Quick Classification Test for each segment before assigning.
4. **During SDR pipeline (sdr-pipeline skill):** Before writing outreach, verify the company passes the Qualification Gate for its assigned segment. If it doesn't, flag and skip.

---

## Universal Disqualification (All Segments)

Exclude immediately if ANY of the following are true, regardless of other signals:

- Company is defunct, acquired and absorbed, or in bankruptcy
- Primary business is software/SaaS with no owned infrastructure
- Primary business is consulting, advisory, or professional services
- Primary business is equipment manufacturing, construction, or installation contracting
- Company is a trade organization, standards body, or industry association
- Company is a hyperscaler (AWS, Azure, GCP, Oracle Cloud, Meta)
- Company is an Internet Exchange Point (IXP) operator
- Company is a Tower REIT (SBA, American Tower, Uniti Group)
- Verified employee count under 10 from 2+ sources (unless holding company with operator subsidiaries)

---

## Segment 1: Colocation Operator

### The False Positive Problem
Many companies use "colocation," "data center," or "hosting" language without actually owning/operating multi-tenant facilities. Common false positives: managed hosting providers, single-rack resellers, cloud service providers, disaster recovery vendors, IT outsourcing firms.

### Qualification Gate (must pass ALL three)

**Gate 1 — Facility Ownership/Operation:**
Does the company own or operate at least one physical data center facility where external tenants can colocate equipment?
- "Managed hosting" or "cloud hosting" without physical colo = FAIL
- Office space with a server room they call a "data center" = FAIL
- Reselling rack space from another colo provider = FAIL (they're a tenant, not an operator)

**Gate 2 — Multi-Tenant Model:**
Does the company serve multiple external tenants (not just internal IT)?
- Internal-only data center = Enterprise, not Colo
- Single dedicated customer = Hosting, not Colo

**Gate 3 — Interconnection Capability:**
Does the company provide carrier interconnection, meet-me room access, or cross-connect services?
- No interconnection capability = Hosting provider, not Colo operator
- Only internet connectivity (no carrier-neutral interconnection) = Hosting

### Required Proof Signals (need 1+ to qualify; 2+ for High confidence)

| # | Proof Signal | Where to Find |
|---|---|---|
| 1 | PeeringDB listing as "Facility" type | PeeringDB search |
| 2 | Published facility specs (MW capacity, rack count, floor space in sqft) | Company website, press releases |
| 3 | Multiple carriers present OR carrier-neutral positioning | Website, PeeringDB |
| 4 | Cross-connect or interconnection services listed with pricing/process | Website services page |
| 5 | Compliance certifications (SOC 2, SSAE 18, HIPAA, PCI-DSS) for facility operations | Website, compliance page |

### Quantitative Minimums

- At least 1 facility with published power and space specifications
- Evidence of 3+ tenants OR explicit carrier-neutral positioning
- 20+ employees (colo operations require staff; under 20 suggests reseller)

### Disqualification Signals (exclude even if keywords match)

- "Managed hosting," "cloud hosting," or "dedicated servers" as PRIMARY service with no physical colo offering
- Single-rack or fractional-rack offerings as entire business model
- No facility address, no published power/space specs, no tour option
- Primary revenue from IT services (helpdesk, endpoint management, cybersecurity)
- Website is a template/landing page with no infrastructure detail
- "Data center" means their server closet, not a multi-tenant facility

### AI Infrastructure Sub-Segment Upgrade

Standard colo qualifies first, then check for AI signals:
- **STRONG AI** (upgrade to AI Infrastructure sub-segment): Named GPU cloud tenants confirmed (CoreWeave, Lambda Labs, Crusoe, Voltage Park) WITH specific source, OR confirmed liquid cooling deployment, OR 30kW+ per rack density confirmed
- **MEDIUM AI** (note but keep Standard): High-density power marketing without confirmed GPU tenants
- **WEAK/NONE**: Standard sub-segment

### Quick Classification Test
"Does this company own a building where other companies put their servers, with carrier interconnection available?" If no, it's not a colo operator.

---

## Segment 2: Fiber Operator

### The False Positive Problem
"Fiber" appears on thousands of company websites. Municipal broadband networks, cable companies, electric cooperatives, utility companies, and construction firms all use fiber-related language. The distinction: MaiaEdge targets operators who own fiber plant AND sell connectivity services commercially (enterprise, wholesale, or carrier).

### Qualification Gate (must pass ALL three)

**Gate 1 — Fiber Ownership:**
Does the company own or operate physical fiber infrastructure (measured in route miles or strand-miles)?
- Leasing circuits from carriers without owning fiber = FAIL (they're an MSP)
- "Fiber to the home" marketing for residential broadband = check for wholesale division
- Construction firm that installs fiber for others = FAIL (contractor, not operator)

**Gate 2 — Commercial Services:**
Does the company sell connectivity services commercially to enterprise, wholesale, or carrier customers?
- Residential-only ISP with no wholesale arm = FAIL (Retail ISP exclude)
- Municipal network serving only government buildings = FAIL (Enterprise internal)
- Dark fiber leased exclusively to one customer = borderline (check for broader services)

**Gate 3 — Infrastructure Scale:**
Does the company have sufficient scale to be a viable MaiaEdge customer?
- Under 100 route miles with no growth trajectory = too small
- Single-market, single-service with no expansion = low priority

### Required Proof Signals (need 1+ to qualify; 2+ for High confidence)

| # | Proof Signal | Where to Find |
|---|---|---|
| 1 | Route miles published or discoverable (minimum 100) | Website, press releases, FCC filings |
| 2 | CLEC/ETC certification OR FCC 477/BDC filings | FCC database, state PUC records |
| 3 | Enterprise, wholesale, or carrier customer class explicitly served | Website services page |
| 4 | Physical infrastructure referenced (splice points, fiber huts, regeneration sites, headends, conduit) | Website, network maps |
| 5 | Network map or service area map published showing fiber routes | Website |

### Quantitative Minimums

- 100+ route miles of owned fiber (or verifiable long-term fiber lease/IRU agreements)
- At least one commercial customer type beyond residential (enterprise, wholesale, carrier, government)
- 25+ employees (fiber operations require field crews and NOC staff)

### Disqualification Signals (exclude even if keywords match)

- "Internet service provider" as sole description with residential-only pricing page
- No wholesale, enterprise, or carrier services page anywhere on website
- Revenue appears entirely from residential broadband subscriptions
- No evidence of owned or operated fiber plant (reseller only, leases all capacity)
- Cable MSO with no wholesale division, no dark fiber, no transport services
- Municipal/government network with no commercial services arm (flag for manual review if ambiguous)
- Fiber construction/installation contractor (builds for others, doesn't operate)

### Sub-Segment Classification

After qualifying, assign sub-segment:
- **Regional CLEC**: Fewer than 5 states, CLEC-licensed, regional focus
- **Long-Haul / Backbone**: 10,000+ route miles OR multi-state backbone OR long-haul transport focus
- **Dark Fiber Specialist**: Primary revenue from dark fiber sales, IRUs, and wavelength services (not lit enterprise services)

### Quick Classification Test
"Does this company own fiber in the ground and sell connectivity services to businesses or carriers?" If no to either half, it's not a fiber operator for MaiaEdge purposes.

---

## Segment 3: Network Operator

### The False Positive Problem
"Network operator" is one of the loosest terms in telecom. IT VARs, SD-WAN vendors, WISPs, VoIP providers, and managed IT companies all use "network" language. MaiaEdge targets Tier 1/2 carriers with national/global backbone infrastructure and complex multi-domain architectures.

### Qualification Gate (must pass ALL three)

**Gate 1 — Network Scale:**
Does the company operate network infrastructure at national or multi-regional scale?
- Regional WISP with 3 towers = FAIL (too small, wrong type)
- SD-WAN vendor with software overlay = FAIL (software, not infrastructure)
- VoIP provider with SIP trunks = FAIL (application, not transport)

**Gate 2 — Enterprise/Wholesale Connectivity:**
Does the company sell transport, wavelength, MPLS, or enterprise connectivity services?
- Consumer broadband only = Retail ISP
- VoIP/UCaaS only = Exclude (application provider)
- IT managed services = Exclude (wrong MSP type)

**Gate 3 — Multi-Domain Architecture:**
Does the company have evidence of multi-domain, multi-PoP network complexity?
- Single market, single domain = probably Fiber Operator instead
- Cloud-only infrastructure = probably not a network operator

### Required Proof Signals (need 1+ to qualify; 2+ for High confidence)

| # | Proof Signal | Where to Find |
|---|---|---|
| 1 | 50+ PoPs OR presence in 10+ markets/states/countries | Website network map, press releases |
| 2 | Enterprise and/or wholesale connectivity services (MPLS, wavelength, transport, DIA) | Website services page |
| 3 | Backbone or transport infrastructure (owned or operated, 10K+ route miles) | Website, industry reports |
| 4 | Published network map showing multi-state or multi-country coverage | Website |
| 5 | OSS/BSS systems, customer portal, or provisioning automation evidence | Website, job postings, press releases |

### Quantitative Minimums

- 50+ PoPs OR 10,000+ route miles OR presence in 10+ states/countries
- 500+ employees OR $500M+ revenue (carrier-scale operations require headcount)
- Enterprise connectivity as a named service line (not just consumer broadband)

### Disqualification Signals (exclude even if keywords match)

- Primary business is IT services, VoIP, UCaaS, or contact center
- "Network operator" used in IT context (network management/monitoring, not carrier)
- SD-WAN vendor positioning as "network operator"
- WISP under 100 employees focused on residential/rural broadband
- Reseller/VAR without owned or operated network infrastructure
- Cable MSO whose network is primarily residential DOCSIS (check for enterprise division)
- Under 50 PoPs AND under 5,000 route miles AND under 200 employees (likely Fiber Operator instead)

### Track Assignment

After qualifying, determine Track A or Track B:
- **Track A (External Extension)**: Evidence of customer portal, API documentation, self-service provisioning, branded products, "instant provisioning" claims. The gap is cross-carrier, not internal.
- **Track B (Internal + External Unification)**: No portal evidence, manual quoting process, multiple acquisitions with separate systems, job postings for "network automation" roles. Internal automation is still fragmented.
- Default: Track A if unclear (safer assumption for messaging)

### Quick Classification Test
"Is this a national/global carrier with 50+ PoPs that sells enterprise connectivity?" If no, it's probably a fiber operator, MSP, or something else entirely.

---

## Segment 4: Neocloud (GPU Cloud Provider)

### The False Positive Problem
"AI" appears on every tech company's website in 2025-2026. The distinction: neoclouds OWN and OPERATE physical GPU infrastructure and sell compute capacity. AI software companies, MLOps platforms, AI consulting firms, and GPU resellers are NOT neoclouds.

### Qualification Gate (must pass ALL three)

**Gate 1 — GPU Infrastructure Ownership or Committed Buildout:**
Does the company own, operate, or have committed capital to build physical GPU compute infrastructure?
- AI/ML software platform without owned GPUs and no buildout plans = FAIL (Software vendor)
- Cloud GPU reseller (resells AWS/Azure/GCP instances) = FAIL (Reseller)
- AI consulting firm = FAIL (Services)
- Pre-revenue company with confirmed funding for GPU buildout = PASS (early-stage neocloud)

**Gate 2 — External Compute Sales (or Clear Intent):**
Does the company sell (or plan to sell) GPU compute capacity to external customers?
- GPUs used only for internal R&D = FAIL (Enterprise internal)
- Selling AI models/APIs, not compute = FAIL (Software vendor)
- Pricing page live or infrastructure under construction with announced GA date = PASS

**Gate 3 — Physical Facility Presence (or Confirmed Path):**
Does the company have GPU hardware deployed in at least one physical facility, OR confirmed lease/build agreements for deployment?
- Cloud-only API with no infrastructure and no buildout evidence = FAIL (could be reselling hyperscaler GPUs)
- "AI cloud" marketing with no evidence of physical deployment or committed build = FAIL
- Announced facility lease, construction permit, or datacenter partnership for GPU deployment = PASS (early-stage)

### Required Proof Signals (need 1+ to qualify; 2+ for High confidence)

| # | Proof Signal | Where to Find |
|---|---|---|
| 1 | GPU fleet specifications published (NVIDIA A100, H100, H200, B200, GB200, etc.) | Website, press releases, blog posts |
| 2 | Pricing page for GPU compute ($/GPU-hour, reserved instances, cluster pricing) | Website pricing page |
| 3 | Physical facility presence confirmed (lease announcements, capacity disclosures) | Press releases, SEC filings |
| 4 | Funding/investment disclosures explicitly mentioning GPU infrastructure buildout | Crunchbase, press releases, SEC filings |
| 5 | Named enterprise customers or published case studies for AI/ML compute workloads | Website, press releases |

### Quantitative Minimums

- Evidence of physical GPU infrastructure OR committed capital for GPU buildout (not API reselling from hyperscalers)
- At least 1 facility with confirmed or announced GPU deployment
- Revenue from GPU compute sales, OR pre-revenue with confirmed infrastructure investment and announced launch timeline

### Disqualification Signals (exclude even if keywords match)

- AI/ML software platform (model training framework, MLOps, inference optimization, AI tooling)
- Cloud GPU reseller (buys from AWS/Azure/GCP, resells with markup, no physical infra)
- AI consulting firm, AI services company, AI agency
- AI chip/hardware manufacturer (designs or sells chips, not compute capacity)
- "AI cloud" or "GPU cloud" marketing language without evidence of physical GPU fleet
- Hyperscaler or hyperscaler subsidiary
- Data labeling, annotation, or AI data services company
- AI model marketplace or model hosting platform (hosts models, not infrastructure)

### Sub-Segment Classification

After qualifying, assign sub-segment based on primary business model:
- **Large-Scale GPU NeoClouds**: Multi-facility (5+), 100MW+ capacity, $1B+ valuation, building or has network teams. Examples: CoreWeave, Nebius, Lambda Labs, Crusoe.
- **Tier 1 Inference Providers**: Inference-as-a-service is primary product, real-time API SLAs, optimized for latency. Examples: Together AI, Groq, DeepInfra, Anyscale.
- **AI Infrastructure Providers**: Multi-cloud GPU platform, API-driven, developer-first, marketplace model. Examples: Cirrascale, Vultr, Fluidstack, DigitalOcean GPU.
- **Sovereign AI Clouds**: Regulatory compliance as primary driver, national AI initiatives, data sovereignty. Examples: Firmus, E2E Networks, Yotta, Nscale EU.
- **Crypto-to-AI Pivots**: Former cryptocurrency mining operations transitioning to AI compute. Check SEC filings for pivot language. Examples: IREN, Core Scientific, Northern Data Group, TeraWulf.

### Quick Classification Test
"Does this company own (or have committed funding to build) GPU hardware in physical facilities and sell compute capacity to other companies?" If no to both halves, it's not a neocloud. Early-stage companies with confirmed GPU buildout funding and a published pricing/product page qualify even if hardware isn't deployed yet.

---

## Segment 5: MSP / Aggregator

### The False Positive Problem
"MSP" is dangerously overloaded. In IT, MSP means managed IT services (helpdesk, endpoint management, cybersecurity). In telecom, MSP means managed network services with upstream carrier aggregation. MaiaEdge targets TELECOM MSPs/aggregators who aggregate carrier circuits and resell wholesale connectivity, NOT IT MSPs.

### Qualification Gate (must pass ALL three)

**Gate 1 — Telecom Carrier Aggregation:**
Does the company aggregate connectivity from multiple upstream TELECOM carriers?
- IT managed services (helpdesk, endpoint, cybersecurity) = FAIL (IT MSP, wrong type)
- Software/SaaS reseller = FAIL
- Hardware VAR = FAIL

**Gate 2 — Connectivity Services:**
Does the company sell connectivity services (WAN, MPLS, SD-WAN, DIA, wavelength) to enterprise customers?
- VoIP/UCaaS only = FAIL (application provider, not connectivity aggregator)
- IT consulting only = FAIL
- Cloud services reseller only = FAIL

**Gate 3 — Multi-Carrier Model:**
Does the company have relationships with 3+ upstream telecom carriers?
- Single carrier reseller = FAIL (too dependent, no aggregation value)
- Owns extensive infrastructure = probably Fiber Operator or Network Operator instead

### Required Proof Signals (need 1+ to qualify; 2+ for High confidence)

| # | Proof Signal | Where to Find |
|---|---|---|
| 1 | Named carrier partners (Lumen, AT&T, Comcast Business, Zayo, etc.) on website | Website partners/carriers page |
| 2 | Multi-carrier provisioning, circuit aggregation, or multi-source services advertised | Website services page |
| 3 | Enterprise WAN, MPLS, managed network, or SD-WAN services with carrier backing | Website services page |
| 4 | "Carrier aggregation," "multi-source," "vendor-neutral," or "carrier-neutral" positioning | Website, about page |

### Quantitative Minimums

- 3+ upstream carrier relationships (verifiable)
- Enterprise connectivity as core offering (not secondary to IT services)
- 50+ employees OR $20M+ revenue (sub-scale aggregators have no leverage)

### Disqualification Signals (exclude even if keywords match)

- Primary business is IT managed services (helpdesk, endpoint management, cybersecurity, cloud management)
- "MSP" used in IT context (Managed IT Services Provider, not Managed Network Services)
- No telecom carrier relationships evident on website or in research
- Sells hardware, software, or IT consulting as primary revenue
- VoIP-only or UCaaS-only provider (application, not transport)
- No evidence of circuit aggregation, wholesale connectivity, or carrier management
- Website lists "services" as IT support, cloud migration, cybersecurity, backup/DR with no connectivity

### The IT MSP Test

When "MSP" appears, apply this test:
1. Does the website mention specific carrier names (AT&T, Lumen, Comcast, Zayo)? → Telecom MSP signal
2. Does the website list MPLS, WAN, SD-WAN, DIA as services? → Telecom MSP signal
3. Does the website list helpdesk, endpoint management, cybersecurity, backup? → IT MSP signal
4. Does "managed services" mean managing carrier circuits or managing IT endpoints? → The answer determines classification

**Decision logic (accounts for dual-business models):**
- Telecom signals present AND IT signals absent → Qualify as MSP/Aggregator (High confidence)
- Telecom signals present AND IT signals also present → Qualify as MSP/Aggregator (Medium confidence). Many legitimate telecom MSPs also offer IT services as a secondary line. The key question: does their connectivity/carrier aggregation business exist as a real revenue line, or is it a minor add-on to an IT services practice? If carrier aggregation appears on their services page with named carriers, qualify. Note the dual model in enrichment output.
- IT signals present AND telecom signals absent → Exclude as "IT MSP (no telecom aggregation)"
- Neither signal type present → Flag for manual review

### Quick Classification Test
"Does this company buy circuits from multiple telecom carriers and resell bundled connectivity to enterprises?" If no, it's not a telecom MSP/aggregator for MaiaEdge purposes.

---

## Applying the Framework: Enrichment Workflow

### Step 1: Phase 1 Routing (unchanged)
Website analysis routes to a likely segment. This is still keyword-based but now understood as a HYPOTHESIS, not a classification.

### Step 2: Phase 2 Research (enhanced)
Research searches now include BOTH qualifying and disqualifying signal detection. Each route includes a disqualification check.

### Step 3: Qualification Gate (NEW — mandatory before classifying)
After Phase 2 research, run the company through the Qualification Gate for its hypothesized segment:
- **All three gates pass + 2+ proof signals** → Classify with HIGH confidence
- **All three gates pass + 1 proof signal** → Classify with MEDIUM confidence (qualified, but note limited proof in output)
- **All three gates pass + 0 proof signals** → Classify with LOW confidence, flag for review. Gates passing without proof signals means the company likely fits but web research couldn't confirm specifics. Don't exclude, but flag.
- **One or more gates fail** → Do NOT classify. Either reclassify to correct segment and re-run gates, or exclude, or flag `needs_manual_review = TRUE`

### Step 4: Disqualification Check (NEW — mandatory)
Scan for segment-specific disqualification signals. If ANY disqualification signal is present:
- Research whether the signal is the company's PRIMARY business or a secondary mention
- If primary → Exclude or reclassify
- If secondary (e.g., "managed hosting" as a small offering alongside real colo) → Note but do not disqualify

### Step 5: Confidence Assignment
- **High (90%+)**: All gates pass, 2+ proof signals, no disqualification signals
- **Medium (70-89%)**: All gates pass, 1 proof signal, or minor ambiguity (e.g., dual-business MSP with real telecom line)
- **Low (50-69%)**: Gates pass but 0 proof signals from web research, or conflicting signals. Company is likely a fit but couldn't confirm details. Include in qualified output with flag.
- **Manual Review Required**: Gates unclear, disqualification signals present alongside qualifying signals, or early-stage company with committed buildout but no operational proof yet

---

## Applying the Framework: Quick Classification (Events, SDR Pipeline)

When full enrichment research isn't feasible (processing attendee lists, verifying segments before outreach), use the Quick Classification Test for each segment:

1. **Colo**: "Does this company own a building where other companies put their servers, with carrier interconnection available?"
2. **Fiber**: "Does this company own fiber in the ground and sell connectivity services to businesses or carriers?"
3. **Network Op**: "Is this a national/global carrier with 50+ PoPs that sells enterprise connectivity?"
4. **Neocloud**: "Does this company own GPU hardware in physical facilities and sell compute capacity to other companies?"
5. **MSP**: "Does this company buy circuits from multiple telecom carriers and resell bundled connectivity to enterprises?"

If the answer is uncertain, flag for manual review. Do NOT auto-classify based on keywords alone.

---

## Common Cross-Segment Misclassification Patterns

| Company Type | Often Misclassified As | Correct Classification |
|---|---|---|
| IT hosting provider ("colocation services") | Colocation Operator | Exclude (IT hosting, not multi-tenant colo) |
| Residential ISP with fiber | Fiber Operator | Exclude unless wholesale division exists |
| Electric cooperative with fiber | Fiber Operator | Qualify IF sells wholesale/enterprise (many do) |
| Cable MSO (Comcast, Charter local affiliates) | Fiber Operator | Exclude unless has wholesale/carrier division |
| SD-WAN vendor | Network Operator | Exclude (software vendor) |
| WISP (wireless ISP) | Fiber Operator or Network Operator | Exclude if residential-only, under 100 employees |
| VoIP/UCaaS provider | MSP/Aggregator | Exclude (application provider, not connectivity) |
| IT MSP (helpdesk, cybersecurity) | MSP/Aggregator | Exclude (IT MSP, not telecom MSP) |
| AI software platform | Neocloud | Exclude (software vendor, no GPU infrastructure) |
| GPU reseller (no owned hardware) | Neocloud | Exclude (reseller, not operator) |
| Data center REIT (owns buildings, outsources operations) | Colocation Operator | Qualify only if they operate the facilities, not just own |
| Fiber construction contractor | Fiber Operator | Exclude (contractor, not operator) |
| Cloud service provider (no physical DC) | Colocation Operator | Exclude (cloud hosting, not colo) |
| Managed hosting provider | Colocation Operator | Exclude unless offers true multi-tenant colo with interconnection |

---

*Cross-references: ICP Sales Playbook, Company Enrichment Skill, Segment Classification Skill, HubSpot Value Reference*
*Created: March 2026 (Phase 4 qualification tightening)*
