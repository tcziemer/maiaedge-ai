# Mass Re-Enrichment Sweep — Batch 29

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 29
**Date:** 2026-05-18
**Records pulled:** 50 (5 paginated calls, offset 0/10/20/30/40, limit 10)
**Unique processed:** 47 (3 duplicates from page-4 offset wrap: FiberCorp, QTnet, TIME DotCom)
**Path mix:** LIGHT 34 · MEDIUM 6 · FULL 7 · HOLD 0
**Apollo this batch:** 0 credits (Apollo enforcement disabled per sweep params; no Apollo calls made)
**Run health:** ✅ GREEN — all 47 HubSpot writes succeeded (5 batches × 10/10/10/10/7, 0 failures)
**Pool before batch 29:** 1,439
**Done this batch:** 40 effective (47 minus 7 already-stamped-today)
**Pool remaining:** ~1,398
**ETA:** ~28 more nominal batches at BATCH_SIZE=50

---

## Path mix detail

### LIGHT (34 records) — date stamp only, framework-consistent

Framework consistent, tier matches default, no signal drift detected, enriched fields populated.

| ID | Name | Segment | Sub-segment | Tier |
|---|---|---|---|---|
| 277437319928 | NTT | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | T1 |
| 296850118383 | NeevCloud | NeoCloud | AI Infrastructure providers - Neocloud | T1 |
| 297940265692 | GMO Internet Group | NeoCloud | Sovereign AI Clouds - Neocloud | T1 |
| 297986183869 | Seeweb | NeoCloud | AI Infrastructure providers - Neocloud | T1 |
| 297770284747 | Sustainable Metal Cloud | NeoCloud | Crypto to AI - Neoclouds | T1 |
| 296880096959 | fal.ai | NeoCloud | Tier 1 Inference - Neocloud | T2 |
| 297782865626 | Massed Compute | NeoCloud | AI Infrastructure providers - Neocloud | T1 |
| 303910638323 | Vero | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 268455104195 | GTA TeleGuam | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 268453305040 | IT&E | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 297986182903 | NexGen Networks | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 297858169557 | Velocity Internet (Opticomm) | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 314347194071 | Aion | NeoCloud | Large Scale GPU - Neocloud | T1 |
| 311372586682 | Hudson InterXchange | Data Center Colo Provider | Standard - colo | T3 |
| 303917854400 | GCX | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | T1 |
| 268197554885 | China Unicom Operations | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | T1 |
| 303892661979 | gounited.net | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 316237316823 | Waves Communications | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 303896263409 | taylortelecomsolutions.com | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 268012614343 | QTnet | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 268210251513 | GTAnet | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 268210252478 | Dauphin Telecom | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 292817295084 | 360 Broadband | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 296850118374 | Coollink.ng | Fiber Operator | Regional CLEC - Fiber operator | T3 |
| 265721356015 | Colo@55 | Data Center Colo Provider | Standard - colo | T3 |
| 266020597493 | Commonwealth Technical Services | Data Center Colo Provider | Standard - colo | T3 |
| 267140078277 | Blue NAP Americas | Data Center Colo Provider | Standard - colo | T3 |
| 266862670523 | Liberty Center One | Data Center Colo Provider | Standard - colo | T3 |
| 311352786662 | Fleet Data Centers | Data Center Colo Provider | Hyperscale Wholesale - colo | T1 |
| 266139329248 | TECfusions | Data Center Colo Provider | AI Signals - colo | T1 |
| 272582853332 | Duos Edge AI | Data Center Colo Provider | AI Signals - colo | T1 |
| 268008618685 | LightHouse Data Centers | Data Center Colo Provider | AI Signals - colo | T1 |
| 266141123265 | Metro Edge Development Partners | Data Center Colo Provider | AI Signals - colo | T1 |
| 314012854998 | DXN Limited | Data Center Colo Provider | Modular - colo | T3 (FROZEN via hs_is_target_account=true; default T1 would apply but skipped per Step A) |

### MEDIUM (6 records) — sub-segment / confidence / geo / tier patches

#### Keel Infrastructure (311386967793)
- Path: MEDIUM
- Domain: keelinfra.com
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud → **Crypto to AI - Neoclouds**
- Confidence: manual_review_required → **high_90**
- Tier: tier_1 → tier_1 (default Crypto to AI T1, no change)
- Reason: Former Bitfarms, 2.2GW HPC/AI pipeline, BTC mining lineage pivoting to AI infrastructure. Cooper 2026-05-14 Operating Principle #9: Crypto to AI is INCLUSIVE of operator AND landlord models. Resolves manual_review per no-default-manual-review principle.

#### Buckeye Telesystem (266846373619)
- Path: MEDIUM
- Domain: buckeye.com
- Segment: Fiber Operator (unchanged)
- Sub-segment: Tier 2 National Wholesale - Fiber operator (unchanged)
- Tier: tier_2 (unchanged)
- State: **Texas → Ohio** (Apollo geo error patch; HQ is Toledo OH per account_brief)
- Reason: Continuing pattern - Apollo geo errors. State property held "Texas" against country US, but every other field (HQ Toledo OH, parent Block Communications) confirmed Ohio. Annual revenue $4.1B flagged as suspect (brief states $75M / 362 employees, parent Block Communications est. $200-300M private) - data quality follow-up open.

#### Donghwa Telecom (316303584985)
- Path: MEDIUM
- Domain: donghwatele.com
- Segment: Data Center Colo Provider (unchanged)
- Country: null → **South Korea**
- Reason: Country field was empty; brief identifies as South Korean telecom infrastructure. No Apollo call needed (data was inferable from existing brief).

#### UrsaCloud (311405563594)
- Path: MEDIUM
- Domain: ursacloud.com
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud → **Greenfield**
- Tier: tier_1 → **tier_2** (Greenfield default T2)
- Confidence: medium_7089 (unchanged)
- Reason: Operating Principle #8: Greenfield is REAL sub-segment for actively-being-built NeoCloud companies. Brief explicitly states "launching 2027", "$500M capital target", "DGX SuperPOD certification", "100MW+ campuses planned" - textbook Greenfield (Series A-C funded, sites under construction, pre-operational).

#### PANGAEA Business Internet (316204485357)
- Path: MEDIUM
- Domain: e-polk.org
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator → **Municipal / Cooperative - Fiber operator**
- Tier: tier_3 → **tier_4** (Municipal/Cooperative default T4, ceiling 2, floor 5)
- Confidence: medium_7089 → high_90
- Reason: Brief identifies as "501(c)(3) nonprofit ISP" serving public institutions (schools, hospitals, county/municipal govts). Cooperative model with grant-funded expansion. Within-Fiber sub-segment demotion. Continuing pattern: cooperative-ownership records misclassified as Regional CLEC.

#### Custom Communications III (297171485400)
- Path: MEDIUM
- Domain: cc3solutions.com
- Segment: Fiber Operator → **MSP/Aggregator**
- Sub-segment: Regional CLEC - Fiber operator → **Master Agent - MSP**
- Tier: tier_3 → tier_3 (Master Agent default T3, no change)
- Confidence: low_5069 → medium_7089
- Reason: Brief explicitly identifies as "asset-light MSP" and notes "leases network capacity from various carriers" + "significant AT&T Alliance Channel partner". Asset-light reseller pattern = Master Agent. Continuing pattern: asset-light MSPs misclassified as Fiber Operators. Segment Change Cascade required (associated contacts).

### FULL (7 records) — re-classification / brief regeneration / eviction

#### The Compute Index, Inc (311410965191) — EVICTION
- Path: FULL
- Domain: compute-index.com
- Segment: NeoCloud → **Flagged for deletion**
- Sub-segment: AI Infrastructure providers - Neocloud (no longer applicable post-eviction)
- Confidence: high_90 (clear non-fit)
- account_brief: regenerated with eviction note
- Reason: SaaS misclassified as NeoCloud. Brief explicitly states "Not a compute provider" - this is a fintech for GPU pricing futures/derivatives, NOT a compute service provider. Continuing pattern: 4 SaaS-as-NeoCloud evictions last batch (Cerebrium, Inferless, Novita AI, TensorDock); this batch +1 (cumulative ~8 across sweep). Grep pattern still active.

#### TDS Telecommunications LLC (297863568114)
- Path: FULL
- Domain: hellotds.com
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (verified - 31 states, 1.1M connections; despite scale, TDS is retail ILEC/CLEC not wholesale, so Regional CLEC remains correct)
- Tier: tier_3 (unchanged)
- account_brief: **regenerated** (was "TDS Telecommunications LLC - research needed for account brief.")
- provisioning_landscape: **regenerated** (was "Research needed for provisioning landscape.")
- Confidence: high_90 (already high)
- Reason: Template-bleed remediation - both narrative fields had "research needed" placeholders. Web-verified: 1M+ fiber passings (Sep 2025), 1.8M target, 31 states, NYSE: TDS parent (TDS Inc).

#### Hype Telecom (297936668396)
- Path: FULL
- Domain: hypetelecom.com
- Segment: Fiber Operator → **MSP/Aggregator**
- Sub-segment: Regional CLEC - Fiber operator → **Managed Network Services - MSP**
- Tier: tier_3 → **tier_2** (Managed Network Services default T2)
- Confidence: high_90 → medium_7089
- account_brief: **regenerated**; provisioning_landscape: **regenerated**
- Reason: Template-bleed + misclassification combo. Web research confirms "hyperscale infrastructure services" model - "delivers full-cycle projects from fiber and data center deployments to 24/7 global client support" + AI-driven NOC. Asset-light managed services for hyperscalers, not asset-owning fiber operator. Segment Change Cascade required.

#### California Internet / GeoLinks (297934868203)
- Path: FULL
- Domain: cainternet.net
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged - verified)
- Tier: tier_3 (unchanged)
- account_brief: **regenerated** (was "California Internet - research needed for account brief.")
- provisioning_landscape: **regenerated** (was "Research needed for provisioning landscape.")
- Confidence: high_90 (already high)
- Reason: Template-bleed remediation. Web-verified: GeoLinks (formerly California Internet Solutions, founded 2011), Camarillo CA HQ, ClearFiber licensed-spectrum fixed wireless up to 10Gbps, 2026 expansion into Las Vegas/Anaheim/Riverside/Pasadena. Hybrid fixed wireless + fiber CLEC.

#### TIME DotCom Berhad (268204721857)
- Path: MEDIUM (segment change, parent reclass)
- Domain: time.com.my
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC - Fiber operator → **Pure Wholesale Carrier - Network Op**
- Tier: tier_3 → **tier_1** (Pure Wholesale Carrier default T1)
- Confidence: high_90 (unchanged)
- Reason: National operator under-tiering pattern. TIME is Malaysia's #2 telco (after TM/Telekom Malaysia), heavily wholesale-focused with 79,850 km pure fiber + ASEAN regional reach + 8,100 km Intra-Asia Marine Cable partnership. infrastructure_profile (Route Miles: Large 10K-50K + POPs: Enterprise 100+) supports wholesale carrier tier. Segment Change Cascade required.

#### FiberCorp / Telecom Argentina (268073696976)
- Path: MEDIUM (segment change)
- Domain: telecomfibercorp.com.ar
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC - Fiber operator → **Tier 1 Carrier - Network Op**
- Tier: tier_3 → **tier_1** (Tier 1 Carrier default T1)
- Confidence: medium_7089 → high_90
- account_brief: regenerated with R3 dedup flag
- Reason: National operator under-tiering. Brief explicitly identifies as "corporate brand of Telecom Argentina" - the dominant Argentine telecom incumbent (Tier 1 national operator). infrastructure_profile (POPs: Enterprise 100+) supports Tier 1 classification. R3 dedup flag raised: verify against any standalone "Telecom Argentina" company record. Segment Change Cascade required.

#### BCE Global (268252506818)
- Path: MEDIUM (segment change, parent reclass)
- Domain: bceglobal.net
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC - Fiber operator → **Pure Wholesale Carrier - Network Op**
- Tier: tier_3 → **tier_1** (Pure Wholesale Carrier default T1)
- Confidence: high_90 (unchanged)
- account_brief: regenerated (clarifies parent + scope)
- Reason: National operator under-tiering. BCE Global is the wholesale arm of Bell Canada (BCE Inc.), Canada's Tier 1 incumbent. 204K route miles + 166 POPs across Canada/US/Europe; voice, IP, broadband, data center wholesale services. infrastructure_profile (Route Miles Enterprise 50K+ + POPs Enterprise 100+) supports Tier 1 classification. D2 wholesale-arm-vs-parent policy: classify under parent's tier (Tier 1 Canadian incumbent). Segment Change Cascade required.

### HOLD (0 records)

Per operating notes (HOLD policy = NONE in this sweep), all 47 records routed to qualified / Other / Flagged for deletion.

---

## Tier movement summary

**Promotions toward T1 (3):**
- TIME DotCom Berhad: T3 → T1
- FiberCorp / Telecom Argentina: T3 → T1
- BCE Global: T3 → T1

**Demotions toward T5 (2):**
- UrsaCloud: T1 → T2 (Greenfield reclass)
- PANGAEA Business Internet: T3 → T4 (Municipal/Cooperative reclass)

**Skipped tier writes (hs_is_target_account=true): 1**
- DXN Limited (would have promoted T3 → T1 to Modular - colo default, but frozen)

**Hype Telecom**: T3 → T2 (segment change reclass to MSP/Managed Network Services)

---

## Continuing patterns observed this batch

| Pattern | This batch | Cumulative across sweep |
|---|---:|---|
| SaaS misclassified as NeoCloud | 1 (The Compute Index) | ~8 |
| National operator under-tiering | 3 (TIME DotCom, FiberCorp/Telecom Arg, BCE Global) | ~27 |
| Apollo geo errors | 1 (Buckeye TX→OH) | ~4 |
| Template-bleed remediation | 3 (TDS, Hype Telecom, California Internet) | ~6 |
| Asset-light MSP misclassified as Fiber Operator | 2 (Custom Comms III, Hype Telecom) | ~5 |
| Within-Fiber → Municipal/Cooperative | 1 (PANGAEA) | ~3 |
| manual_review_required → resolved | 1 (Keel Infra → Crypto to AI) | ~7 |
| Greenfield reclassification | 1 (UrsaCloud) | ~3 |

---

## R3 dedup flags raised this batch (3)

1. **GTAnet (268210251513, gtanet.ca)** vs **GTA TeleGuam (268455104195, gta.net)** — both describe Guam principal telecommunications company; gtanet.ca domain looks incorrect (Canadian TLD for Guam-based telco). Flag for R3 to investigate.
2. **FiberCorp (268073696976, telecomfibercorp.com.ar)** vs any standalone "Telecom Argentina" record — FiberCorp is corporate/wholesale brand of Telecom Argentina; verify no duplicate.
3. **Bell Canada wholesale arm naming** — verify BCE Global (268252506818) is the only Bell wholesale record (no separate "Bell Wholesale" or "Bell Canada Wholesale" duplicates).

---

## Data quality follow-ups open

1. **Buckeye Telesystem annualrevenue $4.1B is suspect** — brief states $75M with 362 employees; parent Block Communications est. $200-300M private. Likely Apollo/CRM data error.
2. **GTAnet domain `gtanet.ca`** — Canadian TLD on a Guam-based telco; suspect wrong domain. R3 should validate and potentially correct to `gta.net` (or merge with GTA TeleGuam).
3. **Donghwa Telecom state still null** post-batch — country populated South Korea, but specific state/province not in brief. Apollo enrich would resolve but disabled this batch.
4. **UrsaCloud state still null** post-batch — Greenfield reclass writes complete but state field left empty (HQ likely Karnataka or Maharashtra per brief context). Defer to next routine touch.

---

## Carryovers from prior batches (still open)

- farmGPU industry FOOD_PRODUCTION (open from prior batch)
- Domyn domain mismatch domyn.io vs domyn.com (open from batch 28)
- Telkomnet missing domain (open from batch 28)
- NaviSite $211.9B annualrevenue (Spectrum copy/paste, open from earlier batch)

---

## Errors

None. All 47 HubSpot property writes succeeded across 5 batches (10/10/10/10/7, 0 failures).

## Apollo budget

This batch: 0 credits consumed (no Apollo calls made; all geo/headcount data inferable from existing fields).
Sweep cumulative: unchanged from batch 28.
