# Mass Re-Enrichment Sweep - Batch 27

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Batch #:** 27
- **Run date:** 2026-05-18
- **Records processed:** 45/50 (offset wrap-around dedup produced 45 unique; 5 duplicates dropped)
- **Pool remaining (pre-batch):** 1,484
- **Pool remaining (post-batch):** ~1,439
- **Apollo this batch:** 0 credits
- **web_search calls:** 4 (DirectLTx, NGN Fiber, Rackdog, Inferra)

## Path mix

| Path | Count |
|---|---|
| LIGHT | 10 |
| MEDIUM | 24 |
| FULL | 11 |
| HOLD | 0 |

## Tier writes

| Direction | Count | Records |
|---|---|---|
| Promotion (T3→T2) | 5 | Bridged Broadband, PFN, Terranet, cvin.com, Montera Infrastructure |
| Demotion (T1→T3) | 1 | Nodes Cluster |
| Skipped (hs_is_target_account=true) | 1 | Neterra |
| Unchanged | 38 | (rest) |

## Segment / sub-segment changes

| Type | Count | Records |
|---|---|---|
| ICP → Flagged for deletion (eviction) | 3 | Dorial Telecom (voice/SMS wholesale), FPX AI (GPU marketplace SaaS), Saturn Cloud (MLOps SaaS) |
| ICP → Other (partner reference) | 1 | OMS Group (subsea cable services vendor; KKR-backed DC build secondary) |
| Cross-segment shift (parent change) | 4 | Nodes Cluster NeoCloud→Colo; Montera MSP→Colo; SCCN Fiber→Network Operator; TAFS Fiber→Network Operator |
| Sub-segment within parent | 7 | Bridged Broadband, PFN, Terranet, cvin.com (Regional CLEC → Long Haul/Backbone); Hypertec (AI Infra → Large Scale GPU); Moonshot (AI Infra → Crypto to AI Neoclouds); Inferra (AI Signals colo → Greenfield) |
| **NEW: Subsea cable operator** | 2 | Southern Cross Cable Network, Trans Americas Fiber System |
| **NEW: Greenfield reclassifications** | 2 | Montera Infrastructure (Stonepeak $1.5B, 100+ MW build), Inferra (Aidin Aghamiri stealth, Camford seed) |
| Confidence upgrades (to high_90) | 8 | FIBRANET, Impossible Cloud, KanOkla, VXFIBER UK, pmt.coop, Hypertec, Moonshot, cvin.com |

## Per-record audit entries

### ALT Telecom (316310831809) — LIGHT
- Path: LIGHT
- Domain: alt.com.br
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 (unchanged)
- Apollo: no
- Reason: All 7 enriched fields populated, sub-segment correct, conf=medium_7089 acceptable. Brazilian altnet recently acquired by TecPar — captured in recent_news already.

### Saturn Cloud (297918677722) — FULL
- Path: FULL (eviction)
- Segment: NeoCloud → Flagged for deletion
- Sub-segment: Tier 1 Inference - Neocloud (frozen in history, not cleared)
- Reason: MLOps SaaS platform sitting ON TOP of other clouds' GPUs (AWS, GCP, Azure, Nebius, Crusoe, Oracle). Not a GPU operator; not in MaiaEdge wholesale buying universe. *Continuing pattern: SaaS misclassified as NeoCloud.*

### Arc Compute (311400162028) — MEDIUM
- Path: MEDIUM
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud (unchanged)
- Confidence: null → medium_7089
- Tier: tier_1 (unchanged)
- Reason: 15-employee Toronto GPU systems integrator/Elite NVIDIA Partner; questionable scale but real activity. Conf bumped from null.

### Bridged Broadband (314310204091) — MEDIUM
- Path: MEDIUM (sub-segment shift)
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator
- Tier: tier_3 → tier_2
- Reason: 11-ISP consortium with 2,500 fiber route miles, 47 PoPs, 800G DWDM backbone, middle-mile + DIA + wholesale = backbone profile beats regional CLEC.

### C3 Pure Fibre (316310830841) — LIGHT
- Path: LIGHT, no field changes

### Columbus FiberNet (314295813858) — LIGHT
- Path: LIGHT, no field changes

### Conexum (314337079014) — MEDIUM
- Confidence: medium_7089 → low_5069
- Reason: 15 employees + LATAM IaaS in 15+ countries reads as a small multi-country hosting reseller. NeoCloud fit is weak; conf demotion captures uncertainty.

### Consolidated Telephone Company (175170996947) — MEDIUM
- Confidence: null → high_90
- Filled: provisioning_landscape
- Reason: Established rural Minnesota ILEC; FTTH + DSL footprint captured.

### DirectLTx (274763246290) — FULL (regen, structural verify)
- Segment: Data Center Colo Provider (unchanged - verified via web)
- Sub-segment: Standard - colo (unchanged)
- Regen: account_brief, provisioning_landscape (prior content described "last-mile fiber construction" — incorrect; actual is 300K sqft / 6 MW carrier-neutral colo in Reading, PA, est. 2006)
- Confidence: null → high_90

### Dorial Telecom (316173995708) — FULL (eviction)
- Segment: MSP/Aggregator → Flagged for deletion
- Reason: Wholesale VoIP carrier specializing in US domestic voice termination + international toll-free ANI traffic. Voice/SMS wholesale pattern — *continuing eviction pattern*, cumulative ~16 across sweep.

### Edge Nebula (102980970224) — MEDIUM
- Regen: account_brief, provisioning_landscape (template-bleed remediation — prior content was generic MaiaEdge sales-pitch copy not company-specific)
- Reason: *Continuing pattern: template-bleed remediation* (4th this batch).

### FIBRANET (311361785567) — MEDIUM
- Confidence: null → high_90

### FPX AI (311392963281) — FULL (eviction)
- Segment: NeoCloud → Flagged for deletion
- Reason: GPU trading marketplace. Provisioning_landscape explicitly states "Not a compute provider." 13 employees, financial broker model. *Continuing pattern: SaaS misclassified as NeoCloud.*

### Gtec Net (303921458893) — MEDIUM
- Confidence: null → medium_7089

### Hypertec (311548817114) — MEDIUM
- Sub-segment: AI Infrastructure providers - Neocloud → Large Scale GPU - Neocloud
- Confidence: null → high_90
- Tier: tier_1 (unchanged, default for both subs)
- Reason: $250M Sovereign AI Hub near Montreal, NVIDIA Canadian Partner of Year, disclosed 100K GPU scale across tier 4 facilities. Clear NC1 anchor per `enrichment-protocols.md` §6a threshold matrix.

### Impossible Cloud (311381571269) — MEDIUM
- Confidence: null → high_90

### Inferra (314343561972) — FULL (Greenfield reclassification + geo fix)
- Sub-segment: AI Signals - colo → Greenfield
- State: null → California
- Country: null → United States
- Confidence: null → low_5069
- Tier: tier_1 → tier_3 (lowered because pre-launch with only seed funding; strict reading of Operating Principle 8 requires Series A-C)
- Filled: provisioning_landscape, recent_news_or_trigger_event
- Reason: Stealth-mode AI inference startup, founded 2025 by Aidin Aghamiri (ex-ITRenew), seed VC from Camford Capital. Pre-launch as of May 2026.

### KanOkla Networks (303912469240) — MEDIUM
- Confidence: null → high_90

### Marcatel Com (316212615890) — MEDIUM
- Filled: provisioning_landscape (was MISSING)
- Reason: Mexican national wholesale carrier (now Vivaro), 5K km Ciena 600G backbone, 150 cities. National-scope but private carrier, not Tier 1 incumbent. Long Haul/Backbone classification holds at tier_2.

### Montera Infrastructure (311370786500) — FULL (segment + sub change)
- Segment: MSP/Aggregator → Data Center Colo Provider
- Sub-segment: Standard - colo → Greenfield
- Tier: tier_3 → tier_2
- Confidence: manual_review_required → high_90
- Reason: Stonepeak-backed ($1.5B), founded 2025, building 100+ MW single-tenant AI inference DCs. Resolves data quality follow-up #1 from CLAUDE.md (one of the 5 misaligned MSP records with colo sub-segment).

### Moonshot Energy (311358187234) — MEDIUM
- Sub-segment: AI Infrastructure providers - Neocloud → Crypto to AI - Neoclouds
- Confidence: null → high_90
- Tier: tier_1 (unchanged)
- Reason: Account_brief explicitly states "Pivoted from Bitcoin mining." NC5 classification per Operating Principle 9 + 2026-05-14 update (Crusoe, Applied Digital, Prometheus precedent).

### NGN Fiber Network (316282051270) — FULL (country + owner correction)
- Country: United States → Germany
- Owner: Tim Lieto (161889085) → Tim Ziemer (159350430)
- Filled: recent_news_or_trigger_event (data quality note about domain collision)
- Reason: Account_brief describes German Eurofiber unit (acquired netcon AG, 19K+ km dark fiber in Germany) but HubSpot domain ngnfiber.com may also serve US Point Broadband consumer ISP. Conservative correction: trust the substantive brief content (German Eurofiber entity), flag the domain collision for manual review. State left as Alabama with audit flag.

### NGN Fiber Network sub-segment unchanged (Dark Fiber Specialist - Fiber Operator).
### Tier unchanged (tier_2).

### Nodes Cluster (311401962232) — FULL (segment change)
- Segment: NeoCloud → Data Center Colo Provider
- Sub-segment: AI Infrastructure providers - Neocloud → Standard - colo
- Tier: tier_1 → tier_3
- Confidence: low_5069 → high_90
- Reason: Slovakia-based Tier III data center; "Physical infrastructure leasing; customer-managed GPU/HPC provisioning" = colo space leasing, not NeoCloud compute operation. 5-300kW per rack supports mixed customer base (HPC, biotech, cloud, defense).

### Neterra (320873732838) — LIGHT (TA=true, tier write skipped)
- Path: LIGHT, date bump only. `hs_is_target_account = true` freeze honored.

### NGN Fiber Network – see above.

### OMS Group (268250706646) — FULL (→ Other)
- Segment: Fiber Operator → Other
- Tier: tier_2 → tier_5 (Other default)
- Reason: Submarine cable services / repair vendor (opticmarine.com brand). Per CLAUDE.md 30th sub-segment policy (2026-05-14), cable vendors/installers are D1-evicted from Subsea cable operator pool; same logic applies here. KKR $400M DC build is secondary/emerging. Kept as Other (partner reference for connectivity supply chain).

### Omniva (301240492757) — MEDIUM
- Date bump only.
- Data quality flag: annualrevenue = $1.92B is likely parent KMGC group's revenue, not Omniva (30 employees). Flag for cleanup. Per *continuing pattern: suspect annual revenue data*.

### Oppidan Connect (316179439348) — LIGHT
- Date bump only (fields already populated, conf already medium_7089).

### Osnet Wireless (316298283764) — LIGHT
### PFN / Peninsula Fiber Network (314315567817) — MEDIUM
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator
- Tier: tier_3 → tier_2
- Infrastructure_profile: Route Miles Small (<1K) → Mid-Size (1K-10K) [6,300+ miles actual]
- Reason: 6,300+ mile fiber backbone in Michigan UP; NG-911, wholesale broadband/transport, $87M NTIA grant. Backbone profile beats CLEC.

### Phase3 Telecom (316133717748) — LIGHT
### Rackdog (314345370349) — MEDIUM
- Confidence: null → low_5069
- Reason: Verified 8,000 bare metal deployments across 12 global locations. Reseller-style ops with 5-employee headcount disclosure suspect. Kept as Standard-colo; conf=low_5069 captures uncertainty. Possible Tier 2 Inference NeoCloud candidate for next pass.

### Relined Fiber Network (316196415208) — MEDIUM
- Filled: provisioning_landscape, recent_news_or_trigger_event
- Reason: 51K+ km TenneT subsidiary across NL/DE/DK; COBRA subsea cable extension. Both fields were MISSING.

### Roke Telkom (316296615619) — LIGHT
### Saturn Cloud — see above (eviction).

### Southern Cross Cable Network (314297604828) — FULL (segment + sub change)
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Long Haul / Backbone → **Subsea cable operator**
- Tier: tier_2 (unchanged, default for new sub-segment)
- Reason: 28,900 km submarine + 1,600 km terrestrial = overwhelmingly subsea. Pure-play transpacific subsea operator owned by Spark NZ, Singtel, Telstra, Verizon (joint venture, not pure consortium). 2nd subsea reclassification in this batch.

### Stealth Communications (314344297186) — MEDIUM
- State: California → New York (NYC-based per account_brief; Manhattan/Brooklyn/Queens)
- Data quality flag: annualrevenue = $211.9B remains (likely Spectrum copy/paste error per CLAUDE.md follow-up #4). Did not write null since R0 may have left this intentionally; flag stands for next data quality pass.

### Streamtech Fiber (316296615624) — LIGHT
### Telered (316179388112) — LIGHT
### Telmex USA (316133585640) — MEDIUM
- Date bump.
- **R3 dedup flag raised:** Telmex USA / Telmex parent / América Móvil family. Per CLAUDE.md follow-up #3 (D2 wholesale-arm policy). Cumulative R3 flags this sweep: continuing pattern.

### Terranet (316296615616) — MEDIUM
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator
- Tier: tier_3 → tier_2
- Reason: Largest IP network in Lebanon (10 PoPs nationwide), ISO 9001:2015. National-scope wholesale + retail operator; backbone classification reflects scope. *Continuing pattern: National operator under-tiering* (Lebanon flavor; not a true Tier 1 incumbent since OGERO is state PTT).

### Trans Americas Fiber System (314347886277) — FULL (segment + sub change)
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Long Haul / Backbone → **Subsea cable operator**
- Tier: tier_2 (unchanged)
- Reason: TAM-1 subsea system, 7,200 km, 650+ Tbps, 24 fiber pairs, 11 landing points across Central America/Caribbean/LATAM/US. Northern route RFS Q4 2025 — operational by now. 6,000 employee headcount stated is suspect (likely inherited from a parent group).

### UPN Fiber (303871311580) — MEDIUM
- Regen: account_brief (was placeholder text)
- Confidence: null → medium_7089
- Reason: Long-haul backbone operator in Missouri; limited public footprint disclosure.

### VXFIBER UK (303919647470) — MEDIUM
- Confidence: null → high_90
- Note: Name "VXFIBER UK" misleading — they're Sweden-based with operations across SA, CR, MY, UK, BE, AT, DE. Did not rename to avoid unilateral name-write churn; flag for follow-up.

### Velocom (316296474348) — LIGHT
### cvin.com / California Internet (303894458102) — MEDIUM
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator
- Tier: tier_3 → tier_2
- Confidence: null → high_90
- Reason: 1,371-mile backbone + 2,500 fiber miles across 23 California counties; wholesale middle-mile since 2011 = backbone profile. Name "cvin.com" should arguably be "California Internet" / "CVIN" but did not rename.

### pmt.coop (303873079004) — MEDIUM
- Confidence: null → high_90

## Data quality follow-ups (this batch)

1. **Stealth Communications annualrevenue = $211.9B** — remains suspect (matches Spectrum/Charter; copy/paste error). Did not null-out; CLAUDE.md follow-up #4 still open.
2. **Omniva annualrevenue = $1.92B** — almost certainly parent KMGC group revenue, not Omniva (30 employees). Add to follow-ups.
3. **NGN Fiber Network ngnfiber.com domain collision** — German Eurofiber unit account_brief vs US Point Broadband consumer ISP domain. Conservative correction applied; manual review flagged in recent_news.
4. **TAFS headcount = 6,000** — suspect (likely parent group, not the subsea operator itself).
5. **VXFIBER UK name** — Swedish company; name should drop "UK" suffix or be renamed to canonical "VX Fiber".
6. **cvin.com name** — likely should be "California Internet" or "CVIN".
7. **"Stealth Communications" address contradiction** — HubSpot state CA fixed to NY; address rest of fields may still need review.

## R3 dedup flags raised

1. **Telmex USA (316133585640) ↔ Telmex / América Móvil parent.** Per CLAUDE.md follow-up #3 and D2 wholesale-arm policy. Cumulative across sweep.

## Continuing patterns (track for sweep summary)

- **SaaS misclassified as NeoCloud**: 2 evictions (FPX AI, Saturn Cloud) + 1 confidence demotion (Conexum). Cumulative across sweep.
- **Voice/SMS wholesale eviction**: 1 (Dorial Telecom). Cumulative ~16 across sweep.
- **National operator under-tiering**: 1 (Terranet upgraded to Long Haul/Backbone in Lebanon).
- **Subsea cable operator (new 30th sub-segment)**: 2 new classifications (SCCN, TAFS). Plus 1 D1-eviction (OMS Group — cable services vendor, not operator).
- **Greenfield reclassifications**: 2 (Montera Infrastructure, Inferra).
- **Template-bleed remediation**: 1 (Edge Nebula).
- **Apollo geo errors / contradiction patches**: 1 (Stealth Communications state CA→NY).
- **Misdomain-style data conflicts**: 1 (NGN Fiber Network — flagged in recent_news).
- **BTC-to-AI lineage**: 1 (Moonshot Energy → Crypto to AI - Neoclouds).
- **NC1 promotion at scale**: 1 (Hypertec → Large Scale GPU - Neocloud).

## Run health: GREEN

All writes succeeded; no HubSpot 429/5xx; no Apollo calls; no Slack DM failures (pending §10 DM).
