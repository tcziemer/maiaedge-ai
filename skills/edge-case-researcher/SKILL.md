---
name: edge-case-researcher
description: "MaiaEdge edge case research agent. Deep-dive investigator for excluded accounts from enrichment pipeline. Takes edge case file from import processor and performs targeted research to reclassify as qualified OR confirm exclusion with stronger evidence. Use when given edge case files, asked to re-evaluate excludes, deep dive excluded accounts, check if any excludes should be qualified, or perform second-pass research on questionable companies. Uses web_fetch, multi-source verification, wholesale/B2B detection, and adaptive query refinement. Catches false negatives from single-pass enrichment  -  especially retail ISP/wholesale hybrids, low employee count errors, and insufficient data edge cases."
---

# MaiaEdge Edge Case Research Agent

## Skill Name: `maiaedge-edge-case-researcher`
## Call Action: Use when asked to "research edge cases", "deep dive excluded accounts", "re-evaluate excludes", "check if any excludes should be qualified", or when given an edge case file from the import processor skill

## Purpose
Take the edge case file produced by the `maiaedge-enrichment-import-processor` skill (or the weekly batch fed by the D7 `Edge_Case_Resolution_Prompt.md` routine) and perform deep-dive research on each account to determine if they should be:
1. **RECLASSIFIED** as a qualified account → produce a HubSpot-ready import file with all values mapped identically to the import processor skill
2. **CONFIRMED EXCLUDED** with stronger evidence and an audit trail

This skill is the per-record research engine. The weekly batch routine that uses it is `cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md` (D7).

## Reference Files (read before executing)

Operational protocols and authoritative sub-segment taxonomy:
- `context/account-tiering/sub-segment-qualification.md` - the 30 active sub-segment values (case-sensitive - see quirks in §"Sub-Segment Case-Sensitivity Quirks" below), parent/sub-segment pairing rules
- `context/account-tiering/sub-segment-qualification-full.md` - canonical deep reference: §3 D1 disqualifiers, §4 D2 wholesale-arm policy, §5 all six D3 disambiguation flowcharts, §6 per-sub-segment anchors + confidence rules, §8 industry sources
- `context/account-tiering/enrichment-protocols.md` - D5 evidence-verification protocols for second-pass research (self-contained §6 protocols + §6a NC threshold matrix + §7 Greenfield catalog)
- `context/account-tiering/d1-global-disqualifiers.md`, `context/account-tiering/d2-wholesale-arm-policy.md`, `context/account-tiering/d3-disambiguation-flowcharts.md` - working-form companion docs (the six segment disambiguation flowcharts live in D3)
- `context/account-tiering/icp-deep-dives/` - per-ICP deep-dive references (`B-and-C-{network-op,fiber-operator,colocation,neocloud,msp-aggregator,enterprise}.md`)
- `context/enrichment/research-routes.md` - research methodology and source prioritization for the deep-dive research passes (which sources to try, in what order, before declaring evidence insufficient)
- `context/hubspot/property-schema.md` - canonical enriched-field set + `flagged_for_deletion_reason` companion-write rule + signal-engine field inventory (HIGH)
- `context/hubspot/hubspot-values.md` - all HubSpot enum values for `customer_segment`, `company_sub_segment`, `segmentation_confidence`, `signal_heat`, and other structured fields written on reclassification (HIGH)
- `context/account-tiering/tier-compute-spec.md` - tier-compute algorithm + signal-heat (`compute_signal_heat`) + `signal_heat` enum values; required when writing tier or heat on reclassification (HIGH)
- `context/core/segment-qualification.md` - segment-level qualification criteria summary; cross-check before finalizing a reclassification decision (MEDIUM)
- `context/enrichment/sourcing-reference-guide.md` - source priority and reliability tiers for deep-dive research; informs which evidence sources to weight (MEDIUM)

## Sub-Segment Case-Sensitivity Quirks (apply to every reclassification write)

HubSpot enums are case-sensitive. The following sub-segment values look interchangeable but only one form is accepted:
- `Dark Fiber Specialist - Fiber Operator` - capital `O` on Operator (NOT `operator`)
- `AI Infrastructure providers - Neocloud` - lowercase `p` on providers
- `Crypto to AI - Neoclouds` - trailing `s` on Neoclouds (the only `Neocloud` sub-segment that ends in `s`)
- `Network Operator(Tier 1 / VNO)` - no space before the open paren (this is the `customer_segment` value, but second-pass writes must use this exact form)
- `Subsea cable operator` - lowercase, NO `- Network Op` suffix (the 30th active sub-segment as of 2026-05-14)
- `Managed Network Services - MSP` - post-Phase 1.7c.1; the pre-1.7c.1 form `Managed Network Services - Network Operator` is RETIRED, do not write

Three values were retired 2026-05-13 Phase 1.6 - never write any of these, even on reclassification:
- `Co-op/consortium` (retired - use `Municipal / Cooperative - Fiber operator`)
- `External Extension - Network operator` (retired - set `network_op_track = external_extension` instead)
- `Internal + external unification - Network Operator` (retired - set `network_op_track = internal_external_unification` instead)

### How This Skill Catches False Negatives
Single-pass enrichment inevitably produces false exclusions on borderline accounts. This skill is a second pass built specifically to recover them:
1. **Targeted research per exclusion type**: Different edge case rules get different research strategies  -  not one-size-fits-all
2. **Website crawling**: Uses `web_fetch` on company domains to read actual services/about pages
3. **Multi-source employee verification**: Bad employee-count data is a common false-exclusion driver  -  this skill cross-references multiple sources
4. **Adaptive query refinement**: If initial searches fail, tries alternate names, trade names, or domain-based searches
5. **Wholesale/B2B detection**: Specifically designed to catch companies that are BOTH retail ISPs AND wholesale fiber operators  -  one of the most common misclassifications

## Input
An XLSX/CSV file with edge case accounts (typically the `edge_cases_for_research.xlsx` output from the import processor). Must contain at minimum:
- `company_name`
- `company_domain`
- `edge_case_rule` (from import processor)
- `edge_case_reason`
- `recommended_research`
- Original enrichment fields

---

## RESEARCH METHODOLOGY

### General Research Approach (applies to ALL rules)
Before running rule-specific searches:
1. **Always start with `web_fetch` on `company_domain`**  -  read the homepage and services page. This alone often resolves the edge case.
2. **Check for parent/subsidiary relationships**  -  a company with 5 employees might be a subsidiary of a larger operator. Search `[company_name] parent company` or `[company_name] subsidiary of`.
3. **Try alternate names**  -  if searches on `company_name` return nothing, look at what name the website uses and search with that instead.

### Rule 1  -  Retail ISP with Infrastructure Signals
**Primary question**: Does this company sell wholesale/B2B connectivity or just residential broadband?

**Research actions:**
1. `web_fetch` on company domain  -  look for: "wholesale", "carrier", "enterprise", "dark fiber", "lit services", "transport", "wavelength", "B2B" pages/menu items
2. Search: `[company_name] wholesale fiber services`
3. Search: `[company_name] enterprise business services`
4. Search: `[company_name] carrier services dark fiber`
5. If the website shows separate residential vs. business divisions, `web_fetch` the business/wholesale page
6. Search: `[company_name] NTCA member` or `[company_name] cooperative`  -  cooperatives almost always have wholesale fiber

**Decision criteria:**
- **RECLASSIFY as Fiber Operator** if: Company has wholesale/carrier/B2B division selling fiber, transport, wavelengths, dark fiber, or lit services to other carriers or enterprises. Even if they also do residential ISP, the B2B infrastructure side makes them a Fiber Operator.
- **CONFIRM EXCLUDE** if: Purely residential broadband with no wholesale, carrier, or enterprise infrastructure sales. No evidence of selling to other operators.

**Common pattern**: Rural telcos and cooperatives are frequently Retail ISP + Fiber Operator hybrids. If the company is NTCA member or a cooperative with 500+ route miles, almost always reclassify as Fiber Operator.

### Rule 2  -  Low Employee Count with Infrastructure Metrics
**Primary question**: Is the employee count accurate, and does this company operate real infrastructure?

**Research actions:**
1. `web_fetch` on company domain  -  check About/Team pages for actual staff
2. Search: `[company_name] employees team staff size`
3. Search: `[company_name] LinkedIn`  -  look for employee count mentions in search snippets
4. Search: `[company_name] annual report revenue`  -  revenue indicates real business scale
5. Check if cooperative, municipal entity, or holding company  -  these systematically show low/zero employee counts in data providers because they report differently
6. Search: `[company_name] cooperative` or `[company_name] municipal broadband`

**Decision criteria:**
- **RECLASSIFY** if: Company clearly operates infrastructure (fiber, data centers, POPs) and the low employee count is a data error, OR the company is a cooperative/municipal/holding entity where employee count data is unreliable by nature.
- **CONFIRM EXCLUDE** if: Company genuinely is very small with no meaningful infrastructure, is defunct, or is inactive.

**Key insight**: Telecom cooperatives almost NEVER show accurate employee counts in data providers. If company name contains "cooperative", "coop", "mutual", "telephone association", or "rural", the employee count is almost certainly wrong  -  focus on infrastructure evidence instead.

### Rule 3  -  Insufficient Data with Identifiable Business
**Primary question**: Can we find the data the original bot missed?

**Research actions:**
1. `web_fetch` on company domain  -  often the website has everything the bot missed
2. Search: `[company_name] fiber network`
3. Search: `[company_name] data center colocation`
4. Search: `site:[company_domain]` to index the website
5. Search: `[company_name] PeeringDB`
6. Search: `[company_name] NTCA` or `[company_name] telecom`
7. If company name is generic or ambiguous, search: `[company_name] [headquarters_state] telecom`

**Decision criteria:**
- **RECLASSIFY** if: Research reveals the company fits a valid segment (Colo, Fiber, Network Op, MSP, Neocloud) with at least MEDIUM confidence.
- **CONFIRM EXCLUDE** if: Even with deeper research, the company doesn't fit any ICP segment, domain is dead, or company is genuinely unrelated to telecom/infrastructure.

**Key insight**: Generic company names tend to return search results for the wrong company. Adding the state or domain to the search query usually resolves this.

### Rule 4  -  Vendor/Contractor with Infrastructure Overlap
**Primary question**: Does this company operate infrastructure in addition to being a vendor?

**Research actions:**
1. `web_fetch` on company domain  -  look for services beyond construction/equipment
2. Search: `[company_name] network operations managed services`
3. Search: `[company_name] fiber network owns operates`
4. Search: `[company_name] dark fiber lease`
5. Look for dual business models (e.g., fiber construction company that retains ownership of some routes)

**Decision criteria:**
- **RECLASSIFY as MSP/Aggregator or Fiber Operator** if: Company operates infrastructure in addition to being a vendor. Dual business model makes them a legitimate prospect.
- **CONFIRM EXCLUDE** if: Company is ONLY a vendor/contractor with no infrastructure ownership or operations.

### Rule 5  -  Outsourcing Services Dual-Arm Ambiguity (Enterprise sub-segment)
**Primary question**: Is this a real BPO with multi-site operational delivery, or a project-based consulting firm dressed up with BPO language?

**Context:** Outsourcing Services - Enterprise (HubSpot sub-segment value: `Outsourcing Services - Enterprise`) is for BPO / outsourced operations providers running multi-site delivery centers on an **ongoing operational basis**. Cognizant, Genpact, Accenture Operations, Concentrix, TaskUs, Conduent, Wipro BPS, TCS BPS qualify. Pure consulting (Deloitte, McKinsey, BCG, Bain) does NOT - they're project-based, not operational. The hard call is dual-arm firms like Cognizant that have both BPO and consulting revenue lines.

**Research actions:**
1. `web_fetch` on company domain  -  look for service lines page. Distinguish "BPO" / "operations" / "managed services" from "consulting" / "advisory" / "strategy."
2. Search: `[company_name] delivery centers locations`  -  multi-site delivery centers with sustained operational headcount = BPO signal.
3. Search: `[company_name] annual report revenue mix BPO consulting`  -  for dual-arm firms, find revenue split. Look at 10-K segment reporting if public.
4. Search: `[company_name] NOC operations 24/7`  -  ongoing operational delivery (not project work) requires 24/7 operations.
5. Search: `[company_name] LinkedIn`  -  count of "delivery center" / "operations" / "BPO" job postings vs "consultant" / "advisor" / "strategy" job postings.

**Decision criteria:**
- **RECLASSIFY as Enterprise (`Outsourcing Services - Enterprise`)** if: Operational delivery is a real revenue line (multi-site delivery centers + sustained headcount + 24/7 NOC). For dual-arm firms (Cognizant-style), if BPO revenue is significant (more than a footnote - typically a named operating segment in 10-K), qualify.
- **CONFIRM EXCLUDE (route to `Other`)** if: Pure project-based consulting / advisory (Deloitte, McKinsey, BCG, Bain pattern). No multi-site delivery centers. Revenue model is engagement-based, not run-rate operational.
- **CONFIRM EXCLUDE (route to `Other`)** if: Dual-arm firm but consulting revenue dominates and BPO is a minor add-on.

### Rule 6  -  Sub-Scale Healthcare or Retail Enterprise
**Primary question**: Does this healthcare system or retailer pass the $1B+ revenue AND 3+ DC scale gate, or are they below the Enterprise ICP threshold?

**Context:** Enterprise ICP requires $1B+ revenue AND (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house net eng). Single-hospital regional health systems and mid-market retailers ($200M-$1B) frequently surface in enrichment with surface-level multi-site characteristics that LOOK like Enterprise but FAIL the scale gate.

**Research actions:**
1. `web_fetch` on company domain  -  read About / Locations pages for facility count.
2. Search: `[company_name] annual revenue`  -  confirm $1B+ threshold.
3. For healthcare: Search: `[company_name] hospitals facilities` AND `[company_name] data center disclosure`  -  multi-hospital systems usually disclose DC count in IT spend press releases or 10-K (if public).
4. For retail: Search: `[company_name] corporate data center` AND `[company_name] distribution center IT`  -  distinguish multi-warehouse (logistics) from multi-DC corporate IT.
5. LinkedIn search: `[company_name]` + `VP Network` / `Director Network Engineering` / `NOC`  -  in-house net eng signal.

**Decision criteria:**
- **RECLASSIFY as Enterprise (correct sub-segment)** if: $1B+ revenue AND 3+ DCs (or direct Equinix Fabric/Megaport port, or confirmed in-house net eng team).
- **CONFIRM EXCLUDE (route to `Other`, hold for revisit)** if: Mid-market $200M-$1B retailer with single DC, single-hospital regional health system, or any company that fails the scale gate. These records stay in `Other` until revenue / DC count grows. Do NOT assign Enterprise sub-segments to sub-scale records.

### Rule 7  -  Watch List Vertical Misclassified as Enterprise
**Primary question**: Is this company in Manufacturing, Energy/Utilities, Logistics/Supply Chain, Government, or Defense - verticals that look "multi-site enterprise" but are NOT Enterprise ICP per the May 2026 promotion?

**Context:** Manufacturing (multi-plant ≠ multi-DC, OT not IT), Energy/Utilities (NERC CIP long-tail), Logistics/Supply Chain (multi-warehouse ≠ multi-DC), Government/Defense (FedRAMP-gated) are Watch List or out-of-scope verticals. These commonly surface as Enterprise false positives because they have surface-level multi-site characteristics. Defense contractors that procure commercially (Lockheed, RTX, Northrop, BAE, L3Harris) should land in `Financial Services - Enterprise` on commercial profile, NOT a "Government" sub-segment (which doesn't exist).

**Research actions:**
1. `web_fetch` on company domain  -  read About / Products / Services pages to determine primary business.
2. Search: `[company_name] industry sector` / `[company_name] business overview`.
3. For multi-site companies: distinguish between "plants" (Manufacturing OT), "warehouses" (Logistics), and "corporate data centers" (Enterprise IT).
4. For defense / government: check `[company_name] commercial business unit revenue`  -  are they procuring commercially or via federal contracts?

**Decision criteria:**
- **CONFIRM EXCLUDE (route to `Other`)** if: Manufacturing, Energy/Utilities, Logistics/Supply Chain (Watch List - future TAM, not currently ICP). Document as "Watch List vertical - future expansion."
- **CONFIRM EXCLUDE (route to `Other` or `Unknown`)** if: Federal agency, state/local government, DoD direct, federal civilian. Document as "FedRAMP-gated - not pursued."
- **RECLASSIFY as Enterprise (`Financial Services - Enterprise`)** if: Defense contractor that procures commercially (Lockheed, RTX, Northrop, BAE, L3Harris) AND passes both gates. Their classified / gov work is irrelevant for ICP classification; assess on commercial procurement profile.
- **RECLASSIFY as Enterprise (`Retail and Distribution - Enterprise`)** in the rare case that a logistics or supply-chain company's CORPORATE IT footprint looks like a multi-DC retailer (not just multi-warehouse). Verify multi-DC corporate IT, not warehouse count.

---

## Note: Wholesale/Retail Nuance Does NOT Apply to Enterprise

For fiber and telco edge cases (Rule 1), the wholesale vs retail distinction is a critical reclassification path - a residential ISP with a wholesale division becomes a Fiber Operator. **Enterprise has no wholesale/retail nuance.** Enterprises ARE the customer; there is no commercial layer to resell to. Do not apply Rule 1 logic to Enterprise edge cases. Use Rules 5/6/7 instead.

---

## D3 SEGMENT DISAMBIGUATION FLOWCHARTS

When second-pass research yields evidence the account is operating real infrastructure but the parent segment itself is in question, walk the D3 flowchart for the candidate segment. The six flowcharts below mirror file 06 §5 and the working D3 disambiguation file at `context/account-tiering/d3-disambiguation-flowcharts.md`. Always cite the rule number used in the output reasoning string.

### D3.1 Network Operator vs Fiber Operator vs MSP/Aggregator

Hardest disambiguation. Wholesale-arm-of-incumbent (Tata Communications, Lumen Wholesale, Sparkle, BT Wholesale) goes Network Operator NOT Fiber - per D2 wholesale-arm policy in `context/account-tiering/enrichment-protocols.md`.

1. Does the company own/operate a national or international backbone with PoPs in 10+ metros AND sell IP transit / capacity to other carriers? -> `Network Operator(Tier 1 / VNO)`
   - Sub-segment (5 active): pick from `Tier 1 Carrier - Network Op`, `Pure Wholesale Carrier - Network Op`, `Cable MSO Enterprise Division - Network Op`, `International Backbone Specialist - Network Op`, `Subsea cable operator` (NEW 2026-05-14; lowercase, no `- Network Op` suffix) per file 06 §5.1
2. Does the company own/operate a regional fiber footprint (single state, multi-state metro) selling lit / dark / wavelengths primarily on its own plant? -> `Fiber Operator`
   - Sub-segment (6 active): `Regional CLEC - Fiber operator`, `Long Haul / Backbone - Fiber operator`, `Dark Fiber Specialist - Fiber Operator` (capital O), `Tier 2 National Wholesale - Fiber operator`, `Regional Cable Operator - Fiber operator`, `Municipal / Cooperative - Fiber operator` per §5.2
3. Does the company resell connectivity (does NOT own the underlying plant) and bundle managed services? -> `MSP/Aggregator`
   - Sub-segment (5 active): `Telecom Aggregator - MSP`, `Managed Network Services - MSP`, `TSD Technology Services Distributor - MSP`, `Master Agent - MSP`, `Cloud + Telecom Hybrid MSP - MSP` per §5.3
4. None of the above clean - keep `Unknown` and route to Tier 3 hold with D7 next-cycle re-review.

### D3.2 Colocation vs NeoCloud (the AI corridor trap)

Both segments often share AI-corridor language. Distinguish on what the company SELLS, not what it hosts.

1. Does the company sell power/space/cross-connects in their own DCs and let tenants bring their own GPUs? -> `Data Center Colo Provider`
   - Sub-segment (4 active + Greenfield cross-segment): `Standard - colo`, `AI Signals - colo`, `Modular - colo`, `Hyperscale Wholesale - colo`, `Greenfield` (cross-segment; pairs with EITHER Colo OR NeoCloud parent) per §5.4
2. Does the company sell GPU-as-a-service / inference / training capacity (the GPUs belong to them, customers rent compute hours)? -> `NeoCloud`
   - Sub-segment (5 active + Greenfield cross-segment): `Large Scale GPU - Neocloud`, `Tier 1 Inference - Neocloud`, `AI Infrastructure providers - Neocloud` (lowercase p), `Sovereign AI Clouds - Neocloud`, `Crypto to AI - Neoclouds` (trailing s; INCLUSIVE of operator AND landlord), `Greenfield` (cross-segment) per §5.5
3. Hybrid (operates DC AND rents own GPUs from same site) - assign on revenue mix; if >50% GPU-rental revenue → NeoCloud; else Colo with `AI Signals - colo` sub-segment.
4. `Greenfield` is real and pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` parent - never standalone. Use when the company is pre-revenue / announced-only build.
5. `Crypto to AI - Neoclouds` is INCLUSIVE of both operator AND landlord patterns per Cooper 2026-05-14 (a crypto mining real-estate landlord pivoting to AI tenants qualifies, not just operators).

### D3.3 Fiber Operator sub-segment selection

After D3.1 lands you on `Fiber Operator`, pick the sub-segment from the 6 active values:
1. Single state / metro CLEC, retail+wholesale mix -> `Regional CLEC - Fiber operator` *(framework default)*
2. National / multi-national backbone, primarily long-haul dark fiber + wavelengths -> `Long Haul / Backbone - Fiber operator`
3. Sells dark fiber as primary product (80%+ dark fiber IRU revenue) -> `Dark Fiber Specialist - Fiber Operator` (capital O)
4. National US/EU wholesale-only with 20K+ route miles (Zayo post-CCF, Lightpath, Uniti+Windstream, EXA EU) -> `Tier 2 National Wholesale - Fiber operator`
5. Regional cable parent with growing commercial fiber book (Breezeline, Mediacom Business, WOW!) -> `Regional Cable Operator - Fiber operator`
6. NTCA / municipal utility / electric cooperative / consortium (EPB Chattanooga, UTOPIA Fiber, Diamond State Networks) -> `Municipal / Cooperative - Fiber operator`

`Regional CLEC - Fiber operator` is the framework default - if no positive evidence supports CLEC (vs Long Haul / Dark / Tier 2 National Wholesale / Regional Cable / Municipal-Cooperative), DO NOT default to it. Downgrade `segmentation_confidence` to `low_5069` and route to R2 + D7 with a positive-evidence-needed flag.

### D3.4 MSP/Aggregator sub-segment selection

After D3.1 lands you on `MSP/Aggregator`, pick the sub-segment from the 5 active values:
1. Aggregates carrier circuits, sells bundled connectivity, direct sales (no sub-agent layer) -> `Telecom Aggregator - MSP` *(framework default)*
2. 70%+ managed network services contracts (NOC, monitoring, change management), vendor-neutral or vendor-specific partner (Cisco / Fortinet) -> `Managed Network Services - MSP` (post-Phase 1.7c.1; never write the retired `- Network Operator` suffix)
3. Distribution-tier org with 100+ active sub-agents + gross billings >=$1B (Telarus, AVANT, Intelisys/ScanSource, AppDirect, Sandler, Bridgepointe) -> `TSD Technology Services Distributor - MSP`
4. Smaller regional or vertical-focused master agency, 10-50 sub-agents, net commission $5M-$100M (X4 Solutions, CyberNet Communications) -> `Master Agent - MSP`
5. AWS Premier / Azure Expert / GCP Premier partner + cloud revenue >=30% + network services in primary marketing (AHEAD, CDW post-Mission, Insight post-SADA, WWT, ePlus) -> `Cloud + Telecom Hybrid MSP - MSP`

`Telecom Aggregator - MSP` is the framework default - if no positive evidence supports aggregation as primary revenue, downgrade confidence to `low_5069`. NaaS platform operators (Megaport, Equinix Fabric, PacketFabric) classify as `customer_segment = "Other"` (competitive reference), NOT any MSP sub-segment.

### D3.5 NeoCloud sub-segment selection

After D3.2 lands you on `NeoCloud`, pick the sub-segment:
1. Operates 10k+ GPU cluster training capacity → `Large Scale GPU - Neocloud`
2. Inference-as-a-service, low-latency endpoint focus → `Tier 1 Inference - Neocloud`
3. Sells AI infra primitives (storage, networking, schedulers) → `AI Infrastructure providers - Neocloud` (lowercase p)
4. Government / nationally-backed AI cloud → `Sovereign AI Clouds - Neocloud`
5. Former crypto miner OR crypto real-estate landlord with AI pivot → `Crypto to AI - Neoclouds` (trailing s)
6. Pre-revenue / announced-only build with GPU plan → `Greenfield`

### D3.6 Enterprise (Multi-DC ICP) - already covered by Rules 5/6/7

The Enterprise flowchart from file 06 §5.6 maps to:
- Rule 5 (Outsourcing/Consulting dual-arm) - `Outsourcing Services - Enterprise`
- Rule 6 (Sub-scale healthcare or retail) - scale-gate enforcement
- Rule 7 (Watch-list vertical misclassified) - Manufacturing / Energy / Logistics / Gov-Defense reroute

Enterprise has exactly four valid sub-segment values:
- `Financial Services - Enterprise`
- `Healthcare Systems - Enterprise`
- `Retail and Distribution - Enterprise`
- `Outsourcing Services - Enterprise`

If second-pass research lands the company on Enterprise but the vertical doesn't match one of these four exactly, reroute to `Other` (Watch List) or `Unknown` per Rule 7. Do not invent sub-segment values.

---

## D5 Evidence Verification (apply before any RECLASSIFY write)

Per `context/account-tiering/enrichment-protocols.md` D5 protocols, every reclassification must carry positive-evidence reasoning, not negative-exclusion. A reclassify from `Other` to `Fiber Operator / Regional CLEC - Fiber operator` requires explicit evidence the company operates fiber AND falls into the CLEC pattern - not merely "isn't long-haul, isn't dark-fiber-only."

Evidence verification checklist:
1. Source named (website page URL, NTCA member directory, FCC BDC entry, PeeringDB entry, 10-K segment, customer logo page) - not "search result snippet"
2. Recency: source content dated within last 24 months OR the operational fact is structural (e.g., physical fiber footprint)
3. Cross-reference: at least 2 independent sources for `high_90` confidence; 1 strong + 1 corroborating for `medium_7089`; single decent source for `low_5069`
4. D2 wholesale-arm check: if the parent name matches a known incumbent (Tata, Lumen, AT&T, Verizon, BT, Telefonica, Sparkle, Orange, NTT), verify whether the record represents the wholesale arm vs the parent - and apply D2 wholesale-arm policy from `enrichment-protocols.md`

---

## OUTPUT

For each edge case:

1. **Research Summary** - What you found and why
2. **Decision** - RECLASSIFY or CONFIRM EXCLUDE
3. **Rule Citation** - Explicit Phase 3 / file 06 / D5 rule cited. Required format:
   `(original_sub_segment, new_sub_segment, confidence, reasoning)` where `reasoning` names the specific D1/D2/D3.x/D5 rule and the positive evidence used.
   Example: `("Other", "Regional CLEC - Fiber operator", "medium_7089", "D3.3 Rule 1 - NTCA member directory entry confirms regional CLEC pattern; FCC BDC entry shows 12-county footprint in IA; positive evidence per D5 cross-reference rule. Wholesale-arm check N/A - independent rural cooperative, no incumbent parent.")`
4. **If RECLASSIFY** - Produce a properly formatted HubSpot import row using exact same mapping as the import processor skill, respecting the case-sensitivity quirks listed above. Never write a retired enum value. `hs_is_target_account = true` (replaces legacy `target_account`).
5. **If CONFIRM EXCLUDE** - Document reason with stronger evidence than the original exclusion and cite the D1 disqualifier or D3 fall-through that applies.

Deliver:
- **Reclassified Accounts** (XLSX) - HubSpot-ready import file for qualified edge cases. Columns match the import-processor schema. Every row carries the rule-citation reasoning string in `_ref_d5_reasoning`.
- **Confirmed Excludes** (XLSX) - Audit trail for companies that remain excluded, with D1 / D3 fall-through citation in `_ref_d5_reasoning`.
