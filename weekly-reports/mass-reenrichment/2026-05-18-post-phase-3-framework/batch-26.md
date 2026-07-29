# Mass Re-Enrichment Sweep — Batch 26

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch date:** 2026-05-18
**Records pulled:** 49 unique (page 3 wrap-around at offset 20 produced VariNet duplicate from page 2)
**Pool remaining at batch start:** 1,533
**Pool remaining after batch:** ~1,484

## Path mix
- LIGHT: 21
- MEDIUM: 22 (segment / sub-segment / field regen / geo fix)
- FULL: 6 (5 evictions + 1 new sub-segment via Subsea cable operator)
- HOLD: 0

## Apollo
- This batch: 0 credits
- Sweep cumulative: 0 (per APOLLO_ENFORCEMENT="disabled" policy)

## Tier writes
- Promotions (toward tier_1): 12 (national incumbents Regional CLEC → Tier 1 Carrier and International Backbone moves)
- Demotions (toward tier_5): 6 (5 Flagged for deletion + Alliance Global tier_2→tier_3 + Dataoorts tier_1→tier_2 confidence demotion)
- Skipped (hs_is_target_account=true): 0

## Segment changes (cascade fired): 21
- 9 national incumbents → Network Operator(Tier 1 / VNO) + Tier 1 Carrier - Network Op
- 4 International Backbone moves
- 1 Subsea cable operator (new 30th sub-segment, first sweep use)
- 1 sub-segment within Fiber Operator (Brightspeed Long Haul → Regional CLEC)
- 5 evictions to Flagged for deletion
- 1 Eand Egypt (subsidiary of e& Group Tier 1)

## Sub-segment auto-migrations: 0 (no §7.4a deterministic mappings hit this batch)

## Greenfield migrations: 0 (Inligo classified as Subsea cable operator, not Greenfield - applying segment-specific Greenfield context but not the Greenfield sub-segment)

## Customer-protection HOLDs: 0
## Completeness Gate fails: 0
## Manual-review HOLDs: 0

---

## Per-record summary

### Ethiotelecom (311372585715)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Confidence: (blank) → high_90
- Tier: tier_3 → tier_2
- Reason: National incumbent under-tiering correction. 76M+ subs, gov-owned, national fiber backbone.

### Ponderosa Telecom (303931686586)
- Path: LIGHT
- No segment change. Brief slight regen to remove em-dash potential.
- Tier: tier_3 (unchanged)
- Reason: Small CA rural ILEC. Below scale but valid Regional CLEC ICP.

### GreenNode (314532044490)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence → high_90
- Reason: Singapore Large Scale GPU NeoCloud, NVIDIA-partnered, 20K+ GPUs.

### Nebul (314501196508)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence → high_90
- Reason: EU sovereign AI cloud, DGX SuperPOD certified.

### Hivenet (297986183874)
- Path: FULL → eviction
- Segment: NeoCloud → Flagged for deletion
- Reason: P2P consumer-GPU marketplace; aggregates idle consumer GPUs (RTX 4090/5090). No owned DC/network infrastructure. SaaS marketplace, not NeoCloud.

### Raxio Group (316210759367)
- Path: LIGHT
- Tier: tier_3 (unchanged)
- Reason: Sub-Saharan African colo, 7 facilities, $100M IFC funding. Standard - colo fits.

### Transworld Networks (316205322957)
- Path: MEDIUM
- Country: Pakistan → United States; State: Islamabad → Florida
- Tier: tier_3 (unchanged)
- Reason: Apollo geo data wrong (likely confused with TWA Pakistan). Brief specifically describes Florida-based fiber MSP for North American electric cooperatives. Data quality follow-up flagged.

### Brightspeed Business (316149788366)
- Path: MEDIUM
- Sub-segment: Long Haul / Backbone - Fiber operator → Regional CLEC - Fiber operator
- Tier: tier_2 (unchanged)
- Reason: Brightspeed is the 5th-largest US ILEC with fiber overbuild for residential/SMB - regional ILEC pattern, not long-haul backbone.

### Global Fiber Peru (316296615622)
- Path: LIGHT
- Tier: tier_2 (unchanged)
- Reason: Peru fiber operator with subsea cable to Colombia/Brazil. Long Haul/Backbone fits.

### AJ Telekom (316210759365)
- Path: FULL → eviction
- Segment: MSP/Aggregator → Flagged for deletion
- Reason: Singapore wholesale VoIP, no owned network infrastructure. Voice-wholesale-only, outside ICP.

### Masorange (316212615891)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: 31M+ mobile subs, 7.1M broadband, merger of Orange Spain + MasMovil. Top-3 Spanish telecom.

### CONSTL (316237371070)
- Path: LIGHT
- Tier: tier_2 (unchanged)
- Reason: 12K+ km India fiber backbone, hyperscaler-focused. Long Haul fits.

### BCN.com (320874452704)
- Path: MEDIUM
- Country: Spain → United States
- provisioning_landscape regenerated (template-bleed removed)
- Tier: tier_2 (unchanged)
- Reason: Apollo geo wrong (.com domain confusion). Brief identifies US MSP since 1994 with Cato/Cisco/SD-WAN stack.

### Sparklight Carrier (320875170515)
- Path: MEDIUM
- provisioning_landscape trimmed (was 9 sentences → 3); account_brief expanded
- Tier: tier_3 (unchanged)
- Reason: Conciseness cap violation fix.

### Open Systems, Inc (320873011949)
- Path: LIGHT
- Tier: tier_2 (unchanged)
- Reason: NY managed-connectivity MSP. Telecom Aggregator - MSP fits.

### Telkomtel / Telkomsel (320960333514)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: Indonesia's #1 mobile (170M+ subs, 66% market share), Telkom Indonesia subsidiary. National incumbent.

### Wtechlink Inc (251597249231)
- Path: FULL → eviction
- Segment: Fiber Operator → Flagged for deletion
- Reason: Brief literally said "Below ICP threshold" pre-sweep. 8 employees Eastern Oregon wireless/fiber ISP.

### VariNet (252601580231)
- Path: FULL → eviction
- Segment: MSP/Aggregator → Flagged for deletion
- Reason: Voice termination IXC, 10 employees BC Canada. Voice-wholesale-only pattern. Continuing eviction pattern.

### Trainy (297944750840)
- Path: FULL → eviction
- Segment: NeoCloud → Flagged for deletion
- Reason: Multi-cloud GPU orchestration SaaS, 5 employees, no owned compute. Software layer, not NeoCloud. Same pattern as Dorados Cloud / CruzNow noted in prior-batch operating notes.

### Dataoorts (297975387888)
- Path: MEDIUM
- Confidence: medium_7089 → low_5069
- Tier: tier_1 → tier_2
- Brief regenerated (was "Brazil-based" but country=India - clear contradiction)
- Reason: Data quality issues (Brazil/India contradiction; Facilities Large vs 4 employees contradiction). Demoted to tier_2 with low confidence. Data quality follow-up flagged.

### Threshold Communications (268012620502)
- Path: MEDIUM
- provisioning_landscape regenerated (template-bleed removed)
- Tier: tier_2 (unchanged)

### Alliance Global Networks (316194606813)
- Path: LIGHT (tier demote)
- Tier: tier_2 → tier_3
- Reason: 20-employee wholesale carrier aggregator with no owned infrastructure - floors at tier_3 per defaults for asset-light aggregators.

### Lanck Telecom (316196415210)
- Path: FULL → eviction
- Segment: MSP/Aggregator → Flagged for deletion
- Reason: Latvia-based voice + A2P messaging wholesale aggregator. No owned network. Voice/SMS wholesale model outside ICP.

### AIRX Technologies (316179439353)
- Path: LIGHT
- Tier: tier_2 (unchanged)
- Reason: Global wholesale network integrator with XONE digital platform, 500+ ISP partners. Strong Telecom Aggregator fit.

### Brightwater Networks (316179439350)
- Path: LIGHT
- Tier: tier_2 (unchanged)
- Reason: Caribbean/LatAm aggregator managing 100K+ circuits. Real volume.

### A1 Telekom Austria Group (316194606817)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: Austria national incumbent, €5.8B revenue, 7 CEE countries, América Móvil subsidiary.

### Telemedia (316194606818)
- Path: LIGHT
- Tier: tier_4 (unchanged)
- Reason: Indiana rural cooperative, 120 sq mi. Municipal / Cooperative fits.

### TDC Net (316203554524)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: Denmark's largest digital infrastructure provider, wholesale fiber, national incumbent.

### BICS (316179439349)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → International Backbone Specialist - Network Op
- Tier: tier_3 → tier_2
- Reason: Proximus international carrier subsidiary, 700+ direct connections, 75 submarine cables, ~50% of world data roaming traffic.

### America Movil (316212615888)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence → high_90
- Reason: Already correctly classified. Brief already flags as duplicate/parent of Claro - **R3 dedup flag raised**.

### Comcast (316237371069)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence → high_90

### OPTAGE (316212615893)
- Path: MEDIUM
- Country: (blank) → Japan; State: Minnesota → Osaka
- Tier: tier_3 (unchanged)
- Reason: Apollo geo data wrong (state=Minnesota incorrect for Japanese operator).

### Taiga Cloud (314519695046)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence → high_90

### Cox Business (316149788370)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence medium_7089 → high_90

### Telstra International (316153417444)
- Path: LIGHT
- Tier: tier_1 (unchanged); confidence → high_90

### Universal Network Services (175178260209)
- Path: MEDIUM
- Country: Australia → United States; State: Victoria → New Jersey
- provisioning_landscape regenerated (template-bleed removed)
- Tier: tier_2 (unchanged)
- Reason: Apollo geo / industry wrong (industry=CONSTRUCTION absurd). Brief identifies Hoboken NJ MSP.

### Alaska Communications (175172795114)
- Path: LIGHT
- Tier: tier_3 (unchanged); confidence → high_90
- Reason: Alaska's leading fiber ILEC, statewide infrastructure with undersea fiber to mainland. Regional CLEC fits at state-incumbent scale.

### VDT Communications (316133717746)
- Path: LIGHT
- Tier: tier_3 (unchanged)
- Reason: Nigerian enterprise IP-MPLS operator, 145+ POPs, 36 states. Regional CLEC fits.

### Proximus Luxembourg (316153417443)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 (unchanged - small country incumbent stays tier_3 baseline)
- Reason: Luxembourg national operator (Proximus Group subsidiary). National incumbent for a small country.

### Harbor Link (316149788369)
- Path: LIGHT
- Tier: tier_2 (unchanged); confidence → high_90
- Reason: Mid-Atlantic dark fiber, 300+ route miles Baltimore/DC/Ashburn, $45M investment. Dark Fiber Specialist fits.

### Colt (316153417447)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → International Backbone Specialist - Network Op
- Tier: tier_3 → tier_2
- Reason: Europe's largest B2B fiber, Fidelity-owned, 38K km in 40+ countries, 275+ PoPs, 12 cable landing stations. Global backbone player.

### Inligo Networks (316153417445)
- Path: FULL (new sub-segment)
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Long Haul / Backbone - Fiber operator → **Subsea cable operator** (first use of 30th sub-segment in sweep)
- Tier: tier_2 (unchanged)
- Reason: Pure-play Australian subsea cable operator. ACC-1 (18,000 km, Singapore-Indonesia-Timor Leste-Australia-Guam-Japan) under construction, $200M Darwin-Adelaide terrestrial build, Indosat Ooredoo partnership. Verified HIGH anchor per CLAUDE.md "Subsea cable operator" guidance. Greenfield-like (under construction) but qualifies as Subsea cable operator with active build progress.

### Chunghwa Telecom (316153417440)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: Taiwan's #1 telecom, NYSE-listed, 13.6M mobile + 8.7M fixed-line + 4.4M broadband. Full-stack national incumbent.

### Eand Egypt (316153417448)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Country: (blank) → Egypt
- Tier: tier_3 (unchanged)
- Reason: e& Group subsidiary in Egypt. Group operates in 16 MEA/Asia countries with 148M+ subscribers - regional Tier 1.

### Two Degrees (316179388110)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Country: United States → New Zealand; State: Washington → Auckland
- Tier: tier_3 (unchanged)
- Reason: NZ #3 wireless with 1.6M subs + post-Vocus NZ merger creating integrated nationwide operator. Apollo geo completely wrong.

### 263 Global (316171331312)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → International Backbone Specialist - Network Op
- Tier: tier_3 (unchanged)
- Reason: Hong Kong global data communications provider, NTT JV for China, PEACE Cable partner.

### Telekomet / Türk Telekom (316173995709)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: Turkey's national incumbent, 33K employees, $4.3B revenue. **R3 dedup flag raised** with Türk Telekom International (already noted in operating notes as confirmed dedup candidate).

### Vodacom (316173995713)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_2
- Reason: South Africa's leading mobile (65M+ customers, 5 African countries, $6.7B revenue, Vodafone-owned). MEA Tier 1.

### OTEGlobe (316179388117)
- Path: MEDIUM
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → International Backbone Specialist - Network Op
- Tier: tier_3 → tier_2
- Reason: OTE international wholesale subsidiary, 21K+ km fiber, AAE-1 submarine cable, SE Europe-to-Asia hub.

---

## Data quality follow-ups raised this batch (3)
1. **Transworld Networks** (316205322957) — Apollo country/state wrong (Pakistan/Islamabad). Brief specifically describes Florida-based US electric-coop fiber MSP. Patched country to US/FL.
2. **Dataoorts** (297975387888) — Brief said "Brazil-based" but country=India. Apollo Facilities band (Large 20-49) doesn't match 4-employee operator. Demoted to low_5069.
3. **OPTAGE** (316212615893) — State=Minnesota wildly wrong for Japan operator. Patched to Japan/Osaka.

## R3 dedup flags raised this batch (2)
1. **America Movil** (316212615888) / **Claro** — Brief already self-acknowledges as parent record. Forward to R3 Duplicate Accounts routine.
2. **Türk Telekom (Telekomet)** (316173995709) / **Türk Telekom International** — Confirmed dedup candidate per operating notes; brief acknowledges separate records exist. Forward to R3.

## Owner mismatch fixes this batch: 0

---

## Continuing patterns confirmed this batch (carry forward)

- **National incumbent under-tiering pattern:** 9 more records this batch (Ethiotelecom, Masorange, Telkomtel/Telkomsel, A1 Austria, TDC Net, Chunghwa Telecom, Türk Telekom domestic, Vodacom, Proximus Luxembourg). Cumulative ~21 across sweep. Sweep-wide grep candidate: `customer_segment = "Fiber Operator" AND company_sub_segment = "Regional CLEC - Fiber operator" AND numberofemployees > 5000 AND annualrevenue IS NULL OR annualrevenue > 1000000000`. Pattern is structural and not exhausting; expect more in subsequent batches.

- **International Backbone Specialist move pattern:** 4 records this batch (BICS, Colt, OTEGlobe, 263 Global) - all originally classified as "Regional CLEC - Fiber operator" but operating global wholesale infrastructure with cable landing presence. Sweep-wide grep candidate: `customer_segment = "Fiber Operator" AND company_sub_segment LIKE "Regional CLEC%" AND (account_brief CONTAINS "submarine" OR "cable landing" OR "global wholesale" OR "international carrier")`.

- **Voice / SMS wholesale eviction pattern:** 3 this batch (AJ Telekom, VariNet, Lanck Telecom). Cumulative ~15 across sweep. Continuing strong.

- **SaaS-misclassified-as-NeoCloud pattern:** 2 this batch (Trainy explicit; Hivenet P2P marketplace). Cumulative ~3. Sweep grep candidate: `customer_segment = "NeoCloud" AND segmentation_confidence = "medium_7089" AND numberofemployees < 20 AND account_brief CONTAINS "orchestration" OR "marketplace" OR "aggregates" OR "distributed network"`.

- **Template-bleed remediation:** 3 records this batch (Hivenet evicted before remediation; BCN.com, Threshold Communications, Universal Network Services, plus Sparklight conciseness trim). Continuing.

- **Apollo geo data wrong:** 5 records this batch (BCN.com Spain→US, OPTAGE Minnesota→Osaka/Japan, Universal Australia→US/NJ, Two Degrees US→NZ, Transworld Pakistan→US, Eand Egypt missing→Egypt). Pattern is recurring; Apollo geo enrichment is unreliable for non-US records and gets confused by .com domains.

## New pattern this batch
- **First Subsea cable operator classification in the sweep** — Inligo Networks. CLAUDE.md added this as 30th sub-segment 2026-05-14. Verified HIGH anchor list (Aqua Comms, Seaborn, Hawaiki, Inligo). Sweep grep candidate going forward: `customer_segment = "Fiber Operator" AND company_sub_segment = "Long Haul / Backbone - Fiber operator" AND account_brief CONTAINS "submarine" OR "subsea" OR "cable landing" OR "ACC-" OR "PEACE Cable" OR "SAEx"`.

## Drain status
- Done in sweep (estimated): 1,300+ / 2,800 (cumulative est., ~47%)
- Remaining in pool: ~1,484
- ETA: ~30 more batches at BATCH_SIZE=50

## Run health: GREEN
## Errors: None

