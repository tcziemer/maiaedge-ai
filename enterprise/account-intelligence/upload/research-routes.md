# Phase 2: Research Routes

Run ONLY the searches relevant to the company's likely classification from Phase 1. Each route now includes both qualifying signal detection AND disqualifying signal detection. Track proof signals found against the Qualification Gate in `segment-qualification.md`.

**Key change:** Phase 1 routing is a HYPOTHESIS. Phase 2 research validates or invalidates that hypothesis. Actively look for disqualifying signals during every search, not just qualifying ones.

## Route: Colocation Operator (3-6 searches)
1. `[company_name] data center facilities locations MW` — facility count, capacity, locations
2. `[company_name] CoreWeave Lambda Labs Crusoe GPU liquid cooling` — AI infrastructure signals
3. `[company_name] expansion acquisition announcement 2024 2025 2026` — recency/timing
4. `[company_name] customers tenants case study` — named customers (only if not found on website)
5. `[company_name] PeeringDB` — directory verification (only if not already confident)
6. `[company_name] managed hosting cloud hosting dedicated servers` — DISQUALIFICATION CHECK (only if website was ambiguous between colo and hosting)

**Proof signals to track (need 2+ to qualify):**
- PeeringDB "Facility" listing
- Published facility specs (MW, rack count, sqft)
- Multiple carriers or carrier-neutral positioning
- Cross-connect/interconnection services with process/pricing
- Compliance certifications for facility ops (SOC 2, SSAE 18)

**Disqualification signals to watch for:**
- "Managed hosting" or "cloud hosting" as primary service
- No physical facility address or specifications
- Primary revenue from IT services
- No meet-me room or carrier interconnection
- Single-rack/fractional offerings as entire business

## Route: Fiber Operator (3-6 searches)
1. `[company_name] fiber route miles network states` — infrastructure scale
2. `[company_name] Megaport PacketFabric Equinix NaaS partnership` — all NaaS in one query
3. `[company_name] expansion acquisition announcement 2024 2025 2026` — recency/timing
4. `[company_name] enterprise wholesale carrier customers` — customer types (only if not on website)
5. `[company_name] NTCA cooperative member` — only if company name suggests cooperative/rural telco
6. `[company_name] residential broadband ISP internet service` — DISQUALIFICATION CHECK (only if website suggested possible retail-only ISP)

**Proof signals to track (need 2+ to qualify):**
- Route miles published (minimum 100)
- CLEC/ETC certification or FCC filings
- Enterprise/wholesale/carrier customer class served
- Physical infrastructure references (splice points, fiber huts, regen sites, headends)
- Network/service area map published

**Disqualification signals to watch for:**
- Residential broadband as sole service with no enterprise/wholesale page
- No evidence of owned fiber plant (resells carrier circuits only)
- Municipal network with no commercial services arm
- Cable MSO with no wholesale/transport division
- Fiber construction contractor (builds for others, doesn't operate)

## Route: Network Operator (3-6 searches)
1. `[company_name] network infrastructure backbone route miles POPs` — scale metrics
2. `[company_name] customer portal API self-service provisioning` — automation maturity (critical for Track A vs B)
3. `[company_name] expansion acquisition partnership 2024 2025 2026` — recency
4. `[company_name] enterprise wholesale customers` — only if not on website
5. `[company_name] Megaport PacketFabric Equinix NaaS` — only if not found on website
6. `[company_name] VoIP UCaaS SD-WAN IT services` — DISQUALIFICATION CHECK (only if "network operator" claim seemed loose)

**Proof signals to track (need 2+ to qualify):**
- 50+ PoPs or 10+ market presence
- Enterprise/wholesale connectivity services (MPLS, wavelength, transport, DIA)
- Backbone/transport infrastructure (10K+ route miles)
- Published multi-state/multi-country network map
- OSS/BSS, customer portal, or provisioning systems

**Disqualification signals to watch for:**
- Primary business is IT services, VoIP, UCaaS, or contact center
- SD-WAN vendor positioning as "network operator"
- WISP under 100 employees, residential focus
- No owned/operated network infrastructure (reseller/VAR)
- Under 50 PoPs AND under 5K route miles AND under 200 employees (likely Fiber instead)

## Route: MSP/Aggregator (2-4 searches)
1. `[company_name] managed services carrier aggregation multi-carrier` — confirm business model
2. `[company_name] customers case study partners` — named customers
3. `[company_name] announcement expansion 2024 2025` — only if needed for scoring
4. `[company_name] IT support helpdesk cybersecurity endpoint managed IT` — DISQUALIFICATION CHECK (always run for MSP hypothesis)

**The IT MSP Test (MANDATORY for every MSP-routed company):**
Check the company against these signals:
- Telecom MSP signals: named carrier partners (AT&T, Lumen, Comcast), MPLS/WAN/SD-WAN/DIA services, "carrier aggregation" or "multi-source" language
- IT MSP signals: helpdesk, endpoint management, cybersecurity, backup/DR, cloud migration, Microsoft 365 management
- If IT MSP signals > Telecom MSP signals → Exclude as "IT MSP (no telecom aggregation)"

**Proof signals to track (need 2+ to qualify):**
- Named carrier partners on website
- Multi-carrier provisioning/aggregation services
- Enterprise WAN/MPLS/managed network services
- "Carrier aggregation" or "vendor-neutral" positioning

**Disqualification signals to watch for:**
- IT managed services as primary business (helpdesk, endpoint, cybersecurity)
- No telecom carrier relationships evident
- VoIP/UCaaS only provider
- No circuit aggregation or wholesale connectivity evidence
- "Services" page lists IT support, cloud migration, cybersecurity with no connectivity

## Route: Neocloud (3-6 searches)
1. `[company_name] GPU cloud infrastructure facilities locations` — scale, facility count
2. `[company_name] expansion funding partnership 2024 2025 2026` — recency and scale
3. `[company_name] customers partners` — only if not on website
4. `[company_name] sovereign AI GDPR compliance data residency` — only if website mentions regulatory/sovereign (Sovereign AI Cloud sub-segment)
5. `[company_name] cryptocurrency mining bitcoin pivot AI` — only if company has crypto/mining history (Crypto-to-AI sub-segment, check SEC filings for pivot language)
6. `[company_name] pricing GPU compute instances API` — PROOF CHECK (verify they actually sell GPU compute, not just AI software)

**Proof signals to track (need 2+ to qualify):**
- GPU fleet specs published (NVIDIA A100, H100, H200, B200, GB200)
- Pricing page for GPU compute ($/GPU-hour or reserved instances)
- Physical facility presence confirmed (lease announcements, capacity disclosures)
- Funding disclosures mentioning GPU infrastructure buildout
- Named enterprise customers for AI/ML compute workloads

**Disqualification signals to watch for:**
- AI/ML software platform without owned GPU infrastructure
- Cloud GPU reseller (resells hyperscaler instances, no physical infra)
- AI consulting firm or services company
- AI chip/hardware manufacturer (sells chips, not compute capacity)
- "AI cloud" marketing without evidence of physical GPU fleet
- Data labeling, annotation, or AI data services company
- AI model marketplace (hosts models, not infrastructure)

### Neocloud Sub-Segment Classification Signals
After research, classify into sub-segment:
- **Large-Scale GPU NeoClouds**: Multi-facility (5+), 100MW+ capacity, $1B+ valuation, building network teams
- **Tier 1 Inference Providers**: Inference-as-a-service is primary product, real-time API SLAs, 5-30+ facilities
- **AI Infrastructure Providers**: Multi-cloud GPU platform, API-driven, developer-first, marketplace model
- **Sovereign AI Clouds**: Regulatory compliance as driver, national AI initiatives, data sovereignty requirements
- **Crypto-to-AI Pivots**: Former crypto mining, transitioning to AI compute, SEC pivot filings, legacy power infrastructure

## Route: Exclude Verification (2-4 searches)

**This route absorbs the logic previously in the Edge Case Researcher skill.** Before excluding any company, spend 2-4 searches trying to find qualifying signals.

**Step 1: Primary verification search**
`[company_name] wholesale fiber enterprise connectivity services infrastructure`

**Step 2: Check for hidden B2B divisions**
`[company_name] carrier services wholesale division network operator`

**Step 3: Evaluate**
- B2B infrastructure services found → **reclassify** to appropriate segment route and run that route's searches
- Genuinely ambiguous → set `needs_manual_review = TRUE` with specific note. **Do NOT exclude ambiguous companies.**
- Clearly not in any MaiaEdge segment → confirm exclude with specific reason

**Common edge case patterns:**
- Utility companies with telecom/fiber divisions (e.g., electric cooperatives)
- Construction/engineering firms that also operate networks
- IT MSPs that are actually telecom aggregators
- Software vendors that also operate infrastructure
- Holding companies with subsidiary operators
- Companies in transition (acquired, pivoting, merging)

## Route: ISP Verification (2-3 searches)
Retail ISPs are the #1 source of false exclusions. Many are BOTH retail ISP and wholesale fiber operators.
1. `[company_name] wholesale carrier enterprise dark fiber services` — look for B2B/wholesale
2. `[company_name] NTCA cooperative` — cooperatives almost always have wholesale fiber
3. If wholesale/carrier found → reclassify as **Fiber Operator** and run fiber route
4. If purely residential → exclude as Retail ISP

## Route: Broad Search Fallback (4-6 searches)
When Phase 1 was insufficient:
1. `[company_name] [company_domain] company` — find what they do
2. `[company_name] fiber data center network infrastructure` — broad infrastructure search
3. `[company_name] PeeringDB` — directory check
4. `[company_name] [headquarters_state] telecom` — add state for disambiguation
5. Based on results, run 1-2 targeted follow-ups from appropriate route
6. If still ambiguous → `needs_manual_review = TRUE`
7. If truly nothing → exclude as Insufficient Data
