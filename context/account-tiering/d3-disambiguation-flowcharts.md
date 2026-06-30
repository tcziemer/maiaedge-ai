# D3 — Sub-segment disambiguation flowcharts (all 6 ICPs)

Each flowchart is a decision tree, ≤7 decisions deep, that runs AFTER global disqualifiers (D1) and AFTER parent-vs-wholesale-arm resolution (D2). All flowcharts encode `manual_review_required` as the explicit fall-through, never an implicit one.

**Pre-condition:** Record has cleared D1 (not a hyperscaler/equipment vendor/OTT/etc.) AND D2 (single-record or wholesale-arm decided).

**Convention:** "YES → X" means follow X; "NO → continue" means proceed to next decision. Decisions are written in falsifiable form so an enrichment bot can run them deterministically.

---

## Flowchart 1 — Network Operator (`customer_segment = "Network Operator(Tier 1 / VNO)"`)

```
Pre-gate: Has revenue ≥ $200M AND operates at least one of {national licensed carrier, IP transit, subsea cable IRU}?
  NO → likely Fiber Operator (Regional CLEC band) — exit to Fiber flowchart
  YES → continue

1. Does the company have meaningful RETAIL (consumer wireless / wireline / TV) AS A PARENT — not just enterprise direct?
   YES → continue to Tier 1 / Cable MSO branch (Decision 2)
   NO → continue to Wholesale / International branch (Decision 5)

2. Is the retail parent a CABLE / HFC LEGACY operator (not telephone-legacy)?
   YES → continue to Decision 3
   NO → continue to Decision 4

3. Does the cable parent operate national or near-national US footprint AND has B2B revenue ≥ $1.5B?
   YES → `Cable MSO Enterprise Division - Network Op`
   NO → exit to Fiber Operator flowchart (route as `Regional Cable Operator - Fiber operator`)

4. Does the operator have multinational reach (wholesale or enterprise in ≥10 countries) AND parent revenue ≥ $15B?
   YES → `Tier 1 Carrier - Network Op`
   NO → flag `manual_review_required` (national incumbent below Tier 1 threshold — e.g., Tier 2/regional incumbent; revisit if revenue confirms Tier 1)

5. Is the wholesale activity primarily INTERNATIONAL (subsea ownership/IRU OR >50% international cross-border revenue OR HQ ≠ US AND markets as international connectivity provider)?
   YES → continue to Decision 6
   NO → continue to Decision 7

6. Does the operator own subsea cable systems OR hold major IRU positions on ≥3 cable systems (verifiable via TeleGeography Submarine Cable Map)?
   YES → `International Backbone Specialist - Network Op`
   NO → flag `manual_review_required` (international wholesale without subsea — fits archetype but disqualifier on infrastructure)

7. Is the operator a PURE-WHOLESALE entity (no retail, no consumer; 100% B2B) with Tier 1 IP transit positioning AND revenue $200M-$5B?
   YES → `Pure Wholesale Carrier - Network Op`
   NO → flag `manual_review_required` (likely Fiber sub-segment; route to Fiber flowchart)
```

**Edge cases:**
- **Mobile-first Tier 1s** (T-Mobile US, Three UK, Rakuten Mobile): pass Decision 4 by revenue and footprint but buying motion differs from wireline Tier 1. Add `manual_review_required` if mobile retail >70% of revenue.
- **Lumen Technologies post-divestitures**: passes Decision 4 today by revenue+enterprise; flag for quarterly re-evaluation as Pure Wholesale boundary case.
- **Subsea cable consortia (pure)**: Already excluded via D1.4. They don't enter this flowchart.

---

## Flowchart 2 — Fiber Operator (`customer_segment = "Fiber Operator"`)

```
Pre-gate: Has fiber infrastructure ownership OR significant lit fiber operation; revenue ≥ $30M?
  NO → likely Regional CLEC threshold breach; if owns small fiber footprint but operates differently, exit to manual_review_required
  YES → continue

1. Does the company have RESIDENTIAL CABLE / HFC LEGACY (former MSO)?
   YES → continue to Decision 2 (cable branch)
   NO → continue to Decision 3 (non-cable branch)

2. Does the cable parent operate national footprint AND parent B2B revenue ≥ $1.5B?
   YES → `Cable MSO Enterprise Division - Network Op` (NOT Fiber — re-route)
   NO → `Regional Cable Operator - Fiber operator`

3. Is the primary product WHOLESALE-ONLY (no retail consumer/SMB, no direct-enterprise dominance)?
   YES → continue to Decision 4 (wholesale branch)
   NO → continue to Decision 6 (retail branch)

4. Is the wholesale primarily INTERNATIONAL (subsea / cross-border)?
   YES → `International Backbone Specialist - Network Op` (re-route to Network Op)
   NO → continue to Decision 5

5. Is the wholesale primarily IP TRANSIT / Tier 1 BGP routing (vs dark fiber + lit transport)?
   YES → `Pure Wholesale Carrier - Network Op` (re-route to Network Op)
   NO → continue to Decision 5a

5a. Revenue $300M-$5B AND national US/EU footprint AND ≥20,000 route miles AND wholesale-only?
    YES → `Tier 2 National Wholesale - Fiber operator`
    NO → continue to Decision 5b

5b. Primary activity is long-haul dark fiber / wavelengths between metros (not last-mile / not metro)?
    YES → `Long Haul / Backbone - Fiber operator`
    NO → continue to Decision 5c

5c. Primary activity is metro / specific-route dark fiber sales (data center campus interconnect, enterprise dark fiber)?
    YES → `Dark Fiber Specialist - Fiber Operator` (note: capital "O" in internal value)
    NO → flag `manual_review_required`

6. Is the operator a MUNICIPAL UTILITY, ELECTRIC CO-OP, or community-owned fiber program?
   YES → `Municipal / Cooperative - Fiber operator`
   NO → continue to Decision 7

7. Is the operator a single-state or multi-state CLEC (competitive local exchange carrier) or fiber-overbuilder serving enterprise + SMB direct, with revenue $30M-$1B?
   YES → `Regional CLEC - Fiber operator` (framework default for ambiguous mid-size fiber)
   NO → flag `manual_review_required`
```

**Edge cases:**
- **Cable-overbuilder doing FTTH overbuild of own footprint** (Comcast's FTTH expansions): retain as Cable MSO Network Op (originating legacy is cable).
- **Middle-mile-only operators** (KentuckyWired, Project THOR pre-commercial): EXCLUDE per file 05 — `customer_segment = "Other"`. Don't enter this flowchart.
- **BEAD-funded operators**: a BEAD grant is a SIGNAL not a sub-segment. Classify per commercial-strand business, not grant funding.

---

## Flowchart 3 — Colocation (`customer_segment = "Data Center Colo Provider"`)

```
Pre-gate: Operates physical data center facilities AND sells space/power/cooling (not pure GPU compute)?
  NO → if sells compute → NeoCloud flowchart; otherwise D1 exclusion
  YES → continue

1. Does the operator have CONFIRMED GPU TENANTS (named neocloud or hyperscale-AI customers) AND deploys liquid cooling AND 30kW+ rack densities?
   YES → continue to Decision 2
   NO → continue to Decision 4

2. Is the company a DISTRIBUTED MODULAR operator (containerized pods at multiple power sites, growth = site count not campus size)?
   YES → `Modular - colo` (note: industry-recognized BUILD typology but MaiaEdge-framed OPERATOR archetype — reasoning string should clarify)
   NO → continue to Decision 3

3. Does the operator sell space PRIMARILY to hyperscaler cloud capacity (Microsoft/AWS/Google/Meta/Oracle) on 10MW+ multi-year wholesale terms (≥60% revenue concentration from hyperscalers)?
   YES → continue to Decision 5 (Hyperscale Wholesale vs AI Signals boundary)
   NO → `AI Signals - colo`

4. Does the operator sell space PRIMARILY on wholesale per-MW basis (10MW+ deployments, 5-15 year terms, anchor tenant model)?
   YES → `Hyperscale Wholesale - colo`
   NO → continue to Decision 6

5. (Decision-3 YES path) Of the GPU tenants and hyperscaler tenants, which book is larger by revenue mix?
   Hyperscaler-anchored cloud capacity > GPU tenants → `Hyperscale Wholesale - colo`
   GPU tenants > hyperscaler cloud capacity → `AI Signals - colo`
   Within 60-40 split → flag `manual_review_required`

6. Is the operator a STANDARD retail / multi-tenant interconnection colo (per-rack / per-cabinet / per-kW sales; high cross-connect volume; meet-me-room model)?
   YES → `Standard - colo` (framework default for traditional colos)
   NO → flag `manual_review_required`
```

**Edge cases:**
- **Operators with BOTH retail standard book AND xScale-style hyperscale wholesale** (Equinix, Vantage, Aligned, NTT, Iron Mountain, QTS): file 05 + Colocation Phase B recommend parent + child records OR single record with majority-revenue classification + `manual_review_required` flag. Recommend Phase 3 to encode: single record → default to larger book; create child records when accounts team specifically targets xScale or Aligned AI campus.
- **Power-rich crypto landlords** (IREN with Microsoft deal, Core Scientific hosting CoreWeave): per NeoCloud Phase B finding — reclassify as `AI Signals - colo` (landlord model) NOT `Crypto to AI - Neoclouds`. The colo flowchart needs a Decision 1a to catch them.
- **Greenfield colos (announced but pre-build)**: classify per planned positioning (AI-ready vs Standard) per file 05 Greenfield Disambiguation; if pre-positioning unclear → `manual_review_required`.

**Insert Decision 1a (before Decision 1):**

```
1a. Is the company a former cryptocurrency miner that has pivoted to AI infrastructure AS A LANDLORD (rents space/power/cooling to GPU tenants; does NOT operate its own GPU compute platform)?
    YES → `AI Signals - colo` (landlord model)
    NO → continue to Decision 1
```

This catches IREN, Core Scientific, Northern Data Group facility-level entities, TeraWulf.

---

## Flowchart 4 — NeoCloud (`customer_segment = "NeoCloud"`)

```
Pre-gate: Operates GPU compute / AI infrastructure AS A SERVICE (sells compute, NOT space)?
  NO → if sells space to GPU tenants → Colocation `AI Signals - colo`
  YES → continue

1. Is the cloud built specifically for DATA SOVEREIGNTY (GDPR / DPDP / national AI program / GAIA-X membership + regulatory positioning + in-country marketing)?
   YES → continue to Decision 2
   NO → continue to Decision 3

2. Triple-signal check: (a) explicit sovereign positioning in marketing, (b) GDPR/DPDP/national-program compliance claims with regulator-named gates, (c) ≥1 sovereign-mandated customer reference?
   ALL THREE → `Sovereign AI Clouds - Neocloud`
   Two of three → still `Sovereign AI Clouds - Neocloud` (lower confidence)
   One or zero → re-route to Decision 3 (likely AI Infrastructure Providers)

3. Is the operator a FORMER CRYPTO MINER that has pivoted to operate its OWN GPU compute (not just landlord)?
   YES → `Crypto to AI - Neoclouds` (note trailing "s" in internal value)
   NO → continue to Decision 4

4. Is the primary product BARE-METAL GPU CLUSTERS for LLM training (multi-facility footprint, 20+ locations OR named hyperscaler+enterprise customer base for training)?
   YES → `Large Scale GPU - Neocloud`
   NO → continue to Decision 5

5. Is the primary product DISTRIBUTED INFERENCE ENDPOINTS (20+ edge city deployments, sub-100ms token latency SLA, per-million-tokens pricing model)?
   YES → `Tier 1 Inference - Neocloud`
   NO → continue to Decision 6

6. Is the operator a MID-MARKET cloud provider that ADDED GPU compute to an existing customer base of developers/SMBs (DigitalOcean/Vultr/Linode archetype) — sells per-GPU-hour to a broad customer mix?
   YES → `AI Infrastructure providers - Neocloud` (note lowercase "p" in internal value)
   NO → flag `manual_review_required`
```

**Edge cases:**
- **Custom-silicon AI inference clouds** (Cerebras Cloud, SambaNova, Groq, Fireworks): fit `Tier 1 Inference - Neocloud` from connectivity-pain standpoint; pricing model is per-token. Default → Tier 1 Inference unless training is primary.
- **Sovereign AI clouds also operating as Tier 1 Inference** (Mistral La Plateforme): primary identity beats secondary product. If sovereign IS the brand, sovereign wins.
- **Hybrid landlord-operator** (IREN with both Microsoft landlord deal + own GPU cloud product): NeoCloud Phase B recommends dominant-revenue-line test. Default to AI Signals colo (landlord) if landlord revenue dominates; Crypto-to-AI Neocloud if operator revenue dominates. Recommend `crypto_pivot_model` new HubSpot field.

---

## Flowchart 5 — MSP/Aggregator (`customer_segment = "MSP/Aggregator"`)

```
Pre-gate: Sells managed network / connectivity services OR aggregates carrier products, with revenue ≥ $20M?
  NO → likely Other
  YES → continue

1. Does the company operate a SUB-AGENT / 1099 channel network of ≥50 active agents?
   YES → continue to Decision 2 (TSD / Master Agent branch)
   NO → continue to Decision 3 (other-MSP branch)

2. Gross billings ≥$1B AND ≥100 active sub-agents AND national US footprint?
   YES → `TSD Technology Services Distributor - MSP`
   NO → `Master Agent - MSP` (default `segmentation_confidence = manual_review_required` per MSP Phase B finding — only 2 verified independents survive 2018-2024 consolidation)

3. Does primary marketing position the company as BOTH cloud (AWS Premier / Azure Expert / Google Cloud Premier partner status) AND network services (SD-WAN, SASE, managed circuits)?
   YES → continue to Decision 4
   NO → continue to Decision 5

4. Of the cloud-vs-network revenue mix, is cloud revenue ≥30%?
   YES → `Cloud + Telecom Hybrid MSP - MSP`
   NO → continue to Decision 5

5. Is primary revenue from MANAGED NETWORK SERVICES contracts (≥70% recurring managed services, NOT commission resell)?
   YES → `Managed Network Services - MSP` (note: HubSpot value uses "- MSP" suffix per Phase 1.7c.1; "- Network Operator" archived)
   NO → continue to Decision 6

6. Is primary revenue from DIRECT SALES of carrier connectivity products to enterprise customers (no sub-agent layer; commission-based on carrier products)?
   YES → `Telecom Aggregator - MSP`
   NO → flag `manual_review_required`
```

**Edge cases:**
- **IoT/eSIM platforms** (Aeris, EMnify, Wireless Logic): EXCLUDE via D1.5. Don't enter this flowchart.
- **Pure cloud MSPs without network services** (post-acquisition Mission Cloud, SADA — now subsumed into CDW/Insight): EXCLUDE via D1.5.
- **IT integrators with massive scale** (CDW $25B, Insight $11B, WWT $20B): MSP Phase B recommends `Cloud + Telecom Hybrid MSP - MSP` if all three of (AWS/Azure/GCP partner status + network services in primary marketing + ≥30% cloud revenue). Default → `manual_review_required` for the boundary case.

---

## Flowchart 6 — Enterprise (`customer_segment = "Enterprise-CustomerSegment"`)

```
Pre-gate: Has the record passed BOTH Enterprise hard gates?
  - Vertical gate: one of the 4 ICP sub-segment verticals (Financial / Healthcare / Retail+Distribution / Outsourcing)
  - Scale gate: $1B+ revenue AND (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house network engineering team)
  NO on either → customer_segment = "Other" or "Unknown" — exit
  YES on both → continue

1. Has the record been hard-disqualified?
   - Network fully outsourced to single MSP with no internal engineering ownership? → "Other"
   - Single DC or single geography? → "Other" (refer to SD-WAN partner)
   - Pure SaaS-only enterprise with no owned DCs? → "Other"
   - No direct carrier contracts (everything through reseller/MSP)? → "Other"
   - YES on any disqualifier → exit to "Other"
   - NO on all → continue

2. Is the entity a MULTI-HOSPITAL IDN or large health system (≥3 hospitals OR ≥$5B revenue) with EHR data centers, imaging archives, regional clinic networks?
   YES → `Healthcare Systems - Enterprise`
   NO → continue

3. Is the entity primary business BANKING / INVESTMENT / INSURANCE / PAYMENT NETWORK / CAPITAL MARKETS INFRASTRUCTURE?
   YES → `Financial Services - Enterprise`
   (Special: defense contractor procuring commercially — Lockheed, RTX, Northrop, BAE, L3Harris — lands here per Enterprise cheatsheet policy)
   NO → continue

4. Is the entity a NATIONAL RETAILER with multi-DC corporate IT (not just multi-warehouse) AND ≥100 stores OR ≥$5B retail revenue?
   YES → `Retail and Distribution - Enterprise`
   NO → continue

5. Is the entity a BPO / OUTSOURCING PROVIDER running multi-site delivery centers on ongoing operational basis (NOT project consulting)?
   YES → continue to Decision 6
   NO → flag `manual_review_required`

6. Is the entity hard-excluded as project-based consulting (Deloitte, McKinsey, BCG, Bain, Accenture Strategy & Consulting only)?
   YES → exit to "Other"
   NO → `Outsourcing Services - Enterprise`
   (Dual-arm firms — Accenture Operations: classify on operational delivery revenue line; IBM Consulting: `manual_review_required`)
```

**Edge cases (per Enterprise Phase B+C):**
- **Diversified industrials** (Honeywell, GE, 3M): default `manual_review_required`. Classify Financial Services only if commercial-procurement IT dominates network spend.
- **CVS Health / UnitedHealth / McKesson**: Retail-pharmacy / insurer-PBM / pharma-distribution hybrids — flag `manual_review_required`.
- **Restaurant chains** (McDonald's, Yum, Chick-fil-A): Watch List, not currently ICP (multi-store ≠ multi-DC corporate IT).
- **Government/defense direct sales**: EXCLUDE via D1.7 until FedRAMP achieved.

---

## Implementation guidance for the flowcharts

### Encoding in segment-classification SKILL

Each flowchart becomes a numbered decision sequence in the skill. Use boolean checks at each decision. The output is `(sub_segment_value, confidence_level, reasoning_string)`.

### Encoding in edge-case-researcher SKILL

The edge-case-researcher consumes records that came out of company-enrichment with `low_5069` or `manual_review_required` confidence. It runs the flowchart with deeper research and writes either a (a) confidence upgrade or (b) confirmation of the original verdict with stronger evidence.

### Re-validation cadence

Per Cooper's quarterly anchor-list refresh policy, re-run the flowcharts against the top 20 records per sub-segment quarterly. Drift detection: if >10% of top records flip sub-segment, root-cause investigation needed before bulk re-application.

### Flowchart depth audit

| Flowchart | Max decisions to leaf | Within ≤7 budget? |
|---|---|---|
| Network Operator | 7 | YES |
| Fiber Operator | 7 (with sub-decisions) | YES (5a/5b/5c counted as one branch level) |
| Colocation | 6 (with Decision 1a) | YES |
| NeoCloud | 6 | YES |
| MSP/Aggregator | 6 | YES |
| Enterprise | 6 | YES |
