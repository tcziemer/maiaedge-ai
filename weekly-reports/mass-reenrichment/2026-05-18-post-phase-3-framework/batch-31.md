# Mass Re-Enrichment Sweep — Batch 31

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 31
**Date:** 2026-05-19
**Records pulled:** 50 (1 dup — Penasco Valley appeared in offsets 0 + 10 due to last_enriched_date tie)
**Records processed:** 49 unique
**Path mix:** LIGHT 34 · MEDIUM 15 · FULL 0 · HOLD 0
**Apollo this batch:** 0 credits
**Pool remaining (post-batch):** 1,294 - 49 = 1,245

---

## Reclassifications (10)

### West Carolina Tel (297906089716)
- Path: MEDIUM
- Domain: wctel.com (unchanged)
- Segment: Fiber Operator -> Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator -> Municipal / Cooperative - Fiber operator
- Confidence: high_90 (unchanged)
- Tier: tier_3 -> tier_4 (default for Municipal/Cooperative)
- Customer protection invoked: no
- Apollo used: no · web_searches: 0
- Completeness Gate: pass (full enriched fields already populated; brief regenerated)
- Reason: Existing brief explicitly states "member-owned telecommunications cooperative established 1952" — Within-Fiber demotion to Municipal/Cooperative per continuing pattern.

### Globe Telecom (267085008575)
- Path: MEDIUM
- Domain: globe.com.ph (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: not previously set -> implicitly high_90 (Tier 1 carrier evidence overwhelming)
- Tier: tier_3 -> tier_1
- Customer protection invoked: no
- Apollo used: no · web_searches: 0
- Completeness Gate: pass
- Reason: Philippine Tier 1 carrier — 92M+ subscribers, $3.15B annual revenue, 8,200 employees, POPs Enterprise (100+). "Regional CLEC" classification was a major under-tier. Continuing National-Operator-Under-Tiering pattern (cumulative ~30).

### Tampnet (268195865330)
- Path: MEDIUM
- Domain: tampnet.com (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Long Haul / Backbone - Fiber operator -> Subsea cable operator
- Confidence: high_90 (implicit)
- Tier: tier_2 -> tier_2 (default for Subsea cable operator)
- Customer protection invoked: no
- Apollo used: no · web_searches: 0
- Completeness Gate: pass
- Reason: Norwegian offshore subsea fiber operator with Route Miles Enterprise (50K+), specialized in oil & gas / wind farm / maritime via subsea fiber + offshore 4G/5G. Pure subsea-cable profile per new 30th sub-segment definition. **NEW pattern this batch** for Subsea cable operator (first sweep instance).

### Network Innovations (266871403216)
- Path: MEDIUM
- Domain: networkinnovations.com (unchanged)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP -> Managed Network Services - MSP
- Confidence: high_90 (implicit)
- Tier: tier_2 -> tier_3 (default for Managed Network Services)
- Apollo used: no · web_searches: 0
- Completeness Gate: pass
- Reason: Maritime/offshore vertical specialist — oil & gas, energy, vessels, FPSOs, offshore rigs, hybrid LEO/satellite. Maritime-MSP misclassification fix (cumulative 3).

### Speedcast (268460499647)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP -> Managed Network Services - MSP
- Tier: tier_2 -> tier_3
- Reason: Maritime + offshore energy + mining + cruise vertical specialist. Maritime-MSP misclassification fix (cumulative 4).

### IP Access International (268447872750)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP -> Managed Network Services - MSP
- Tier: tier_2 -> tier_3
- Reason: Mission-critical connectivity for remote/offshore — oil/gas, maritime, utilities, emergency services. SuperGIG hybrid cellular-satellite product line. Maritime-MSP misclassification fix (cumulative 5).

### Castor Marine (268447862494)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP -> Managed Network Services - MSP
- Tier: tier_2 -> tier_3
- Reason: Pure maritime — shipping, offshore oil & gas, dredging, superyacht. VSAT + Starlink + Iridium + OneWeb portfolio. Maritime-MSP misclassification fix (cumulative 6).

### Beulahland Communications (296846534372)
- Path: MEDIUM
- Sub-segment: Long Haul / Backbone - Fiber operator -> Regional CLEC - Fiber operator
- Tier: tier_2 -> tier_3
- Reason: 800 residential and business customers across Pueblo and Custer Counties, Colorado — clearly local CLEC, not Long Haul/Backbone. Continuing Within-Fiber-demotion pattern (cumulative ~14).

### Wasatch Broadband (297877949126)
- Path: MEDIUM
- Sub-segment: Long Haul / Backbone - Fiber operator -> Regional CLEC - Fiber operator
- Tier: tier_2 -> tier_3
- Reason: Concentrated local service area in Utah (Saratoga Springs HQ), mix of fixed wireless + fiber to residences and SMBs. Not a long-haul/backbone operator. Continuing Within-Fiber-demotion pattern (cumulative ~15).

### Beacon Data Centers (311326703333)
- Path: MEDIUM
- Sub-segment: Standard - colo -> Greenfield
- Tier: tier_3 -> tier_3 (low_5069 confidence retained; awaits operational milestone)
- Reason: Development-stage. 4.5-4.9 GW planned across Alberta, Q4 2028 energization target, no operational facilities. Per `enrichment-protocols.md` §7 Greenfield migration patterns this is a textbook actively-being-built Colo. Will auto-migrate to Standard/Hyperscale Wholesale at first operational milestone.

---

## Stub regeneration (5)

### Bertram Communications (297940265687)
- Path: MEDIUM
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 (unchanged)
- Brief: stub ("research needed for account brief") -> regenerated 2-4 sentence brief grounded in geo_focus + infrastructure_profile + Fiber Connect 2026 signal.
- Provisioning_landscape: stub -> regenerated.
- Reason: Continuing Template-bleed pattern (cumulative ~14).

### Calaveras Telephone Company (296883684058)
- Path: MEDIUM
- Brief: stub -> regenerated (California rural CLEC, CPUC FTTH grant application via CalTel Connections).
- Provisioning_landscape: stub -> regenerated.
- Reason: Template-bleed (cumulative ~15).

### Emily Cooperative Telephone (297888732861)
- Path: MEDIUM
- Brief: stub -> regenerated (Minnesota Tri-Co partnership, now Tremolo Communications brand, 125 fiber route miles added 2023).
- Provisioning_landscape: stub -> regenerated.
- Reason: Template-bleed (cumulative ~16).

### Co-Mo Electric Cooperative (297888732865)
- Path: MEDIUM
- Brief: stub -> regenerated (Missouri member-owned electric coop, Co-Mo Connect 35K fiber subscribers as of 2025-03).
- Provisioning_landscape: stub -> regenerated.
- Reason: Template-bleed (cumulative ~17).

### Voxtelesys (268111635144)
- Path: MEDIUM
- Brief: regenerated (removed "Voxtelesys is an ideal fit for MaiaEdge" value-prop bleed; replaced with neutral peer-competitive framing).
- Reason: NEW pattern — MaiaEdge value-prop bleed inside `account_brief`. Watch for this pattern on records enriched by earlier framework iterations that mixed outreach value-prop into the brief field. Recommend grep `account_brief CONTAINS "ideal fit for MaiaEdge" OR "MaiaEdge angle" OR "MaiaEdge is" OR "ideal customer for MaiaEdge"` on subsequent batches. Provisional cumulative 1.

---

## LIGHT path (34, date bump only)

Records with all 7 enriched fields present, framework-consistent, sub-segments in 30 active, no MaiaEdge value-prop bleed in `account_brief`, no Tier 3 hold escalation. `last_enriched_date` bumped to 2026-05-19. Tier/segment/sub-segment unchanged. No HubSpot company-note write (note bandwidth conserved for path-change records; LIGHT date bump audit is in this batch file).

| ID | Name | Segment | Sub-segment | Tier | Notes |
|---|---|---|---|---|---|
| 297986183866 | Access Montana | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean |
| 297989642956 | Penasco Valley Telephone Cooperative | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (paginated twice; processed once) |
| 314300605139 | Cato Digital | Data Center Colo Provider | AI Signals - colo | tier_1 | clean |
| 314300605138 | Mod42 | Data Center Colo Provider | AI Signals - colo | tier_1 | clean (modular AI factory, BTC mining lineage — possible NC5 reassess later) |
| 314337129201 | Aethir | NeoCloud | Large Scale GPU - Neocloud | tier_1 | hs_is_target_account=true (tier write skipped per policy; date bumped) |
| 297987984062 | JarvisLabs | NeoCloud | AI Infrastructure providers - Neocloud | tier_1 | clean (brief is short but factual; MaiaEdge-angle phrase in provisioning_landscape — flag for next pass) |
| 297877949128 | Scottsboro Electric Power Board | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean |
| 320873732841 | EPB | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (Chattanooga, EPB Quantum Network) |
| 303848694477 | Shadeform | NeoCloud | AI Infrastructure providers - Neocloud | tier_1 | clean (MaiaEdge-angle phrase in provisioning_landscape — flag for next pass) |
| 315098723030 | Digital Energy | Data Center Colo Provider | AI Signals - colo | tier_1 | clean (NL AI Factory, heat reuse) |
| 266889850617 | Bayou Internet | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean |
| 267086916336 | IIJ America Inc. | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | NOTE: classification suspect — US subsidiary of IIJ (major Japanese network operator). Possible Network Operator parent. Held LIGHT this pass; flag for D7 manual review. |
| 267091668715 | Quad State Internet | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean (KY CLEC, 400G DWDM transport) |
| 268204721854 | GridFury | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean |
| 268197561044 | Terra Nova Telecom | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean |
| 268111635143 | Florida High Speed Internet | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | thin brief but framework-consistent |
| 268111749861 | Xalient | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | clean (UK global SD-WAN + identity) |
| 268455112422 | GNX | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | clean (NL global connectivity platform, 3,000+ ISPs) |
| 296883684039 | Winn Telephone | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean (acquired by Peninsula Fiber Network 2023; combined 6K route miles MI/WI/MN) |
| 297940265679 | FiberComm | Data Center Colo Provider | Standard - colo | tier_3 | clean (acquired by ImOn Communications 2023) |
| 297906089711 | TecInfo Communications | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean (MS/AR rural fiber, RDOF funded) |
| 300469447409 | Simple Fiber | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean (MD Eastern Shore) |
| 320875170517 | WTC Communications | Data Center Colo Provider | Standard - colo | tier_3 | hs_is_target_account=true (tier write skipped per policy; date bumped) |
| 296880096956 | Pembroke Telephone | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | low_5069 confidence retained; D7 candidate |
| 298011233981 | Btel | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean (Brazoria TX, 2,200 fiber route miles) |
| 297877949131 | Lost Nation-Elwood Telephone | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | clean (IA, BLB Communications partnership) |
| 314352890581 | Hyperbolic | NeoCloud | Tier 1 Inference - Neocloud | tier_2 | hs_is_target_account=true (tier write skipped per policy; date bumped) |
| 297877949129 | Cooperative Telephone Company | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (Iowa CTC Technology) |
| 297877949124 | GRM Networks | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean ($11.1M USDA ReConnect grant 2025-01) |
| 297888731895 | Paul Bunyan Communications | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (MN GigaZone) |
| 297888732858 | Spencer Municipal Utilities | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (IA municipal) |
| 297888731892 | Gigabit Communications | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | clean (TX/NM regional fiber, Blue Owl majority investment 2025-09; legitimate Long Haul classification here — owns 500+ route miles and connects 50+ DCs) |
| 297888731891 | United Utilities | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (Alaska GCI subsidiary) |
| 297863568110 | Allamakee-Clayton Electric Cooperative | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | clean (IA AC Skyways) |

---

## HOLD path (0)

Per sweep operating notes "HOLD policy = NONE", no records routed to HOLD. All 49 records reached a definitive classification (qualified, partner, deletion, or LIGHT date-bump).

---

## Tier write summary

- Promotions (toward T1): 1 (Globe Telecom tier_3 -> tier_1)
- Demotions (toward T5): 8 (West Carolina Tel, Beulahland, Wasatch Broadband + 4 maritime MSPs + Beacon held flat)
- Unchanged: 40
- Skipped (hs_is_target_account=true): 3 (Aethir, Hyperbolic, WTC Communications)
- Net tier movement: net demotion bias (continuing pattern from prior batches)

---

## Patterns observed this batch

1. **Maritime-MSP misclassification (continuing, +4 cumulative 6):** Network Innovations, Speedcast, IP Access International, Castor Marine all reclassified from Telecom Aggregator - MSP -> Managed Network Services - MSP. The Telecom Aggregator class continues to be a magnet for maritime/offshore specialists during prior framework runs. **Watch:** grep `customer_segment="MSP/Aggregator" AND company_sub_segment="Telecom Aggregator - MSP" AND (account_brief CONTAINS "maritime" OR "offshore" OR "vessel" OR "VSAT" OR "Starlink" OR "FPSO" OR "yacht" OR "cruise")`.
2. **Within-Fiber Long Haul / Backbone -> Regional CLEC (continuing, +2 cumulative ~15):** Beulahland Communications and Wasatch Broadband — both locally-scoped operators previously tagged Long Haul/Backbone. **Watch:** grep `company_sub_segment="Long Haul / Backbone - Fiber operator" AND geographic_focus CONTAINS "Local" OR "1 states" OR numberofemployees < 50`.
3. **Within-Fiber Regional CLEC -> Municipal/Cooperative (continuing, +1 cumulative ~14):** West Carolina Tel ("member-owned telecommunications cooperative"). **Watch:** grep `customer_segment="Fiber Operator" AND company_sub_segment="Regional CLEC - Fiber operator" AND account_brief CONTAINS "cooperative" OR "member-owned" OR "co-op"`.
4. **National-operator under-tiering (continuing, +1 cumulative ~30):** Globe Telecom — Philippine Tier 1 carrier, 92M subscribers, mislabeled "Regional CLEC". **Watch:** grep `customer_segment="Fiber Operator" AND numberofemployees > 5000 AND annualrevenue > 1000000000`.
5. **Template-bleed remediation (continuing, +4 cumulative ~17):** Bertram, Calaveras, Emily Cooperative, Co-Mo. **Watch:** grep `account_brief CONTAINS "research needed for account brief" OR provisioning_landscape CONTAINS "Research needed"`.
6. **NEW PATTERN — Subsea cable operator first-instance:** Tampnet first record reclassified to the new 30th sub-segment. **Watch:** grep `customer_segment="Fiber Operator" AND (account_brief CONTAINS "subsea" OR "submarine cable" OR "offshore fiber" OR "oil platforms" OR "FPSO") AND infrastructure_profile CONTAINS "Route Miles"`. Likely candidates: Aqua Comms, Seaborn Networks, Hawaiki Submarine Cable, Telxius, PLDC.
7. **NEW PATTERN — Greenfield migration first colo instance this sweep:** Beacon Data Centers reclassified Standard -> Greenfield (development-stage, 4.5GW Alberta, no operational facilities). **Watch:** grep `customer_segment="Data Center Colo Provider" AND (account_brief CONTAINS "planned" OR "under construction" OR "energization target" OR "Series A" OR "Series B" OR provisioning_landscape CONTAINS "development-stage" OR "no operational facilities")`.
8. **NEW PATTERN — MaiaEdge value-prop bleed inside account_brief:** Voxtelesys had "Voxtelesys is an ideal fit for MaiaEdge to unify orchestration..." in the brief itself. Brief should describe the company, not the MaiaEdge value prop. Provisional cumulative 1. **Watch:** grep `account_brief CONTAINS "ideal fit for MaiaEdge" OR "MaiaEdge angle" OR "fit for MaiaEdge" OR "MaiaEdge is" OR "MaiaEdge to"`.
9. **Carry forward — JarvisLabs and Shadeform "MaiaEdge angle:" phrase inside provisioning_landscape field.** Not customer-facing per `maiaedge_value_proposition` policy, but the phrase is operational shorthand that probably shouldn't live in an enriched field. Flag for next-batch cleanup if seen again.

---

## Data quality follow-ups opened this batch

- **IIJ America Inc.** (267086916336): US subsidiary of IIJ, a major Japanese network operator. Currently classified "Regional CLEC". Possible Network Operator(Tier 1 / VNO) parent classification — but US arm scope may be limited. Held LIGHT this pass; flag for D7 manual review.
- **Co-Mo / GRM / Paul Bunyan / Cooperative Telephone / United Utilities / Allamakee-Clayton / Spencer Municipal:** all electric or telephone cooperatives correctly classified Municipal/Cooperative. Solid coverage of the rural-coop pool this batch.
- **R3 dedup flags this batch (1):** Penasco Valley Telephone Cooperative appeared in both offset 0 and offset 10 results — same record, not a duplicate company. Confirming HubSpot's offset-with-stable-sort-key behavior is unreliable; sweep continues using straight offset pagination but tracking the dupe rate per batch.

---

## Drain status

- Pool at batch start: 1,294
- Processed this batch: 49
- Pool remaining: 1,245
- ETA at BATCH_SIZE=50: ~25 more batches (about 25 chat sessions)
- Apollo credits consumed this batch: 0 (sweep param APOLLO_ENFORCEMENT="disabled" allowed unlimited, but no Apollo calls were needed — all reclassifications were determinate from existing enriched-field evidence)
- Apollo credits cumulative this sweep: see `weekly-reports/apollo-budget.json` (sweep is exempt from the 850/wk cap; no JSON write per §8 of sweep prompt)

---

## Run health: GREEN
## Errors: None
