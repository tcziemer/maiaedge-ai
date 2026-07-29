# Mass Re-Enrichment Sweep — Batch 20

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Batch:** 20
- **Run date:** 2026-05-18
- **Records processed:** 50/50
- **VERIFY_DEPTH:** leverage-and-patch
- **APOLLO_ENFORCEMENT:** disabled (0 credits consumed this batch)
- **HOLD policy:** NONE per Cooper operating note — every record qualified, partner-targeted, partner-referenced, or flagged for deletion
- **Pre-batch pool:** 1,804 records remaining
- **Post-batch pool:** ~1,754 remaining (~982 cumulative processed, ~36% drain)

## Summary

| Path  | Count | Notes                                                                 |
|-------|-------|-----------------------------------------------------------------------|
| LIGHT | 35    | Clear stale `recent_news_or_trigger_event` + bump `last_enriched_date` |
| MEDIUM | 13   | Sub-segment reclass, brief trim, geographic fix, owner re-derive       |
| FULL  | 2     | Bitfury reclass to Other; Essextel flagged for deletion                |
| HOLD  | 0     | Per Cooper override, no Tier 3 holds this batch                        |

- **Apollo credits this batch:** 0
- **Tier writes:**
  - Promotions toward T1: 0
  - Demotions toward T5: 2 (Bitfury NeoCloud T1 → Other T5; Essextel MSP T2 → Flagged T5)
  - Skipped (hs_is_target_account=true): unknown — property not queried in chunk fetch
- **Sub-segment auto-migrations (deterministic 1-to-1):** 0 (no legacy strings hit in this chunk)
- **Sub-segment manual reclassifications:** 4 (Anyscale → AI Infrastructure providers - Neocloud; EdgeCloudLink → Greenfield; Champlain Tech Group → Municipal / Cooperative - Fiber operator; Newwave Communications → Regional Cable Operator - Fiber operator)
- **Greenfield migrations:** 1 (EdgeCloudLink — hydrogen-powered modular DC concept, no operating sites yet)
- **Segment changes (cascade due):** 2 (Bitfury NeoCloud → Other; Essextel MSP → Flagged for deletion) — contact cascade deferred to next R6 / D7 fire
- **Owner re-derivations:** 1 (Newwave Communications: Tim Z International → Ken West, state=AZ)
- **Customer-protection HOLDs:** 0
- **Completeness Gate fails (held for next batch):** 0
- **Manual-review HOLDs (true 2+ ambiguity):** 0

## Per-record outcomes

| # | Company (id) | Path | Segment old → new | Sub-segment old → new | Confidence | Tier old → new | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Northflank (297894135492) | LIGHT | NeoCloud | unchanged (Tier 1 Inference - Neocloud) | medium_7089 | tier_2 | clear stale 2025-01 news |
| 2 | KDDI AI Cloud (300467292882) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | R3 flag: kddi.com parent domain |
| 3 | Sakura Internet (298002235113) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | clear stale 2025-08 news |
| 4 | Bitfarms (298005835457) | LIGHT | NeoCloud | unchanged (Crypto to AI - Neoclouds) | high_90 | tier_1 | fresh news kept (2026-05-01 Keel Infra rebrand) |
| 5 | SK Telecom GPUaaS (297989642972) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | R3 flag: sktelecom.com parent domain |
| 6 | Bitfury Group (303396068040) | FULL | NeoCloud → Other | Crypto to AI - Neoclouds → (cleared) | medium_7089 | tier_1 → tier_5 | Reclass: now pure investment fund ($1B ethical tech fund), no operating GPU/DC infra; portfolio refs (LiquidStack, Axelera) |
| 7 | Greenidge Generation (303405064911) | MEDIUM | NeoCloud | unchanged (Crypto to AI - Neoclouds) | medium_7089 | tier_1 | News refresh: Q1 2026 results, 60MW Dresden NYSEG interconnect, 250MW MS pipeline, 100MW non-curtailable power |
| 8 | Indosat Lintasarta GPU Merdeka (303423198924) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | clear stale 2024-10 news |
| 9 | Linode (Akamai) (303397868271) | LIGHT | NeoCloud | unchanged | medium_7089 | tier_1 | clear stale 2024 news |
| 10 | FPT AI Factory (303405064912) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | R3 flag: fpt.com parent domain |
| 11 | HUMAIN (303287302902) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | clear borderline-stale 2026-02 news |
| 12 | Anyscale (297960965846) | MEDIUM | NeoCloud | Tier 1 Inference - Neocloud → AI Infrastructure providers - Neocloud | high_90 | tier_2 | Ray PaaS, not Tier 1 inference operator; clear 2022-08 news |
| 13 | CleanSpark (264413011658) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | clear stale 2025-10 news |
| 14 | Reliance Jio AI (303370363624) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | R3 flag: jio.com parent domain |
| 15 | Marathon Digital (297770284744) | LIGHT | NeoCloud | unchanged (Crypto to AI) | high_90 | tier_1 | fresh news kept (2026-04-30 Long Ridge acq) |
| 16 | Yotta Data Services (303449222870) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | clear stale 2025-02 news |
| 17 | Ooredoo Qatar AI Cloud (303442039544) | LIGHT | NeoCloud | unchanged | high_90 | tier_1 | R3 flag: ooredoo.qa parent domain |
| 18 | Mawson Infrastructure (303423198925) | LIGHT | NeoCloud | unchanged | medium_7089 | tier_1 | clear stale 2025-10 news |
| 19 | SambaNova (303377637098) | MEDIUM | NeoCloud | unchanged (Tier 1 Inference - Neocloud) | high_90 | tier_2 | Trim verbose brief + provisioning_landscape, add date prefix to news |
| 20 | American Real Estate Partners (303379474153) | MEDIUM | Data Center Colo | unchanged (Standard - colo) | medium_7089 | tier_3 | Trim verbose brief + provisioning, add news date prefix |
| 21 | 1025Connect / Long Island Interconnect (303401563880) | MEDIUM | Data Center Colo | unchanged | medium_7089 | tier_3 | Trim brief + provisioning_landscape, clear stale 2024 news |
| 22 | EdgeCloudLink (ECL) (303423288018) | MEDIUM | Data Center Colo | Standard - colo → **Greenfield** | high_90 | tier_3 | Reclass: hydrogen fuel-cell modular DC concept, no operating sites yet (Series A stage) |
| 23 | Telapex (303892661955) | MEDIUM | Fiber Op | unchanged (Long Haul / Backbone) | high_90 | tier_2 | Trim brief + provisioning, clear non-event news |
| 24 | Poka Lambro Telecom (320876610271) | LIGHT | Fiber Op | unchanged | high_90 | tier_2 | clear stale 2024-10 news |
| 25 | Mid-Rivers Communications (296850118381) | MEDIUM | Fiber Op | unchanged | high_90 | tier_3 | **Fix geographic error in provisioning_landscape** (Shiawassee County is Michigan; this co-op serves Eastern Montana) |
| 26 | PRTC McKee KY (297936668397) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_4 | Keep news (2023-2025 range), bump date |
| 27 | Boldyn Networks (300402132682) | MEDIUM | Fiber Op | unchanged (flagged for R3/D7 review) | high_90 | tier_3 | Trim brief; sub-segment "Regional CLEC" doesn't fit a global neutral host (BAI+ZenFi). Numberofemployees=3 is wrong (real ~1000+). Flag for R3/D7 |
| 28 | DataVision (303910639343) | LIGHT | Fiber Op | unchanged | high_90 | tier_4 | clear news (no date prefix) |
| 29 | MPRTC Mid-Plains Rural (303916049122) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_4 | clear news (no date prefix) |
| 30 | StratusIQ (303912470202) | LIGHT | Fiber Op | unchanged | high_90 | tier_3 | clear news (no date prefix) |
| 31 | RCN (303914254027) | LIGHT | MSP/Aggregator | unchanged (Telecom Aggregator - MSP) | high_90 | tier_2 | clear news (no date prefix) |
| 32 | Grant County PUD (303871311575) | LIGHT | Fiber Op | unchanged (Municipal / Cooperative) | high_90 | tier_4 | clear 2024 buildout-complete news |
| 33 | Optimum / Altice USA (303873077982) | MEDIUM | Fiber Op | unchanged (Regional Cable Operator) | high_90 | tier_3 | News refresh: Q4 2025 Lightpath +35% YoY, $362M AI contracts. **Revenue $54.6B flagged for data quality** (Altice USA standalone is ~$9B) |
| 34 | Madison Communications IL (303871311568) | LIGHT | Fiber Op | unchanged (Regional CLEC) | high_90 | tier_3 | clear non-event news |
| 35 | LightStream IN (303883053810) | LIGHT | Fiber Op | unchanged | high_90 | tier_4 | clear news |
| 36 | Winnebago Co-op IA (303881260774) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_4 | clear news (no date prefix) |
| 37 | United Electric Cooperative MO (303879483119) | LIGHT | Fiber Op | unchanged | high_90 | tier_4 | clear news. **Industry tag flagged**: "ELECTRICAL_ELECTRONIC_MANUFACTURING" should be TELECOMMUNICATIONS or UTILITIES |
| 38 | Tularosa Basin Telephone NM (303883054796) | LIGHT | Fiber Op | unchanged | high_90 | tier_3 | clear news |
| 39 | Kalona Cooperative Tech IA (303890867955) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_4 | clear news |
| 40 | Newwave Communications / Sparklight (303883053800) | MEDIUM | Fiber Op | Regional CLEC → **Regional Cable Operator - Fiber operator** | high_90 | tier_3 | **Owner fix**: state=AZ, owner was 159350430 (Tim Z International) → 162339176 (Ken West). Sub-segment more accurate as Cable Operator |
| 41 | Wiggins Telephone Association CO (303889038029) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_3 | clear news. **Industry tag flagged**: "CONSUMER_GOODS" should be TELECOMMUNICATIONS |
| 42 | Peoples Telephone Cooperative TX (303890868951) | LIGHT | Fiber Op | unchanged | high_90 | tier_4 | clear news |
| 43 | Montana Internet Corporation (303896263366) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_3 | clear news. **Industry tag flagged**: "PROFESSIONAL_TRAINING_COACHING" should be TELECOMMUNICATIONS |
| 44 | Champlain Technology Group NY (303894457072) | MEDIUM | Fiber Op | Long Haul / Backbone → **Municipal / Cooperative - Fiber operator** | low_5069 | tier_2 | 5 employees + 3-5K customers — not long-haul; reclass to rural co-op sub-segment |
| 45 | Surry Communications NC (303890869983) | LIGHT | Fiber Op | unchanged | high_90 | tier_3 | clear news |
| 46 | Essextel (303896262390) | FULL | MSP/Aggregator → **Flagged for deletion** | Telecom Aggregator - MSP → (cleared) | manual_review_required → high_90 | tier_2 → tier_5 | Pure software VoIP reseller, brief explicitly says "no MaiaEdge infrastructure alignment". Aggressive flag per Operating Principle #7 |
| 47 | SmartCom TX (303908845287) | LIGHT | Fiber Op | unchanged | medium_7089 | tier_3 | clear non-event news |
| 48 | Bevcomm MN (303896263408) | LIGHT | Fiber Op | unchanged | high_90 | tier_3 | clear 2025 grant news |
| 49 | Haviland Telephone KS (303919649474) | LIGHT | Fiber Op | unchanged | high_90 | tier_3 | clear news |
| 50 | Intermax Networks ID (303919648465) | LIGHT | Fiber Op | unchanged | high_90 | tier_3 | clear news, brief truncation noted |

## Patterns observed this batch

- **NeoCloud arm shares parent telco domain (R3 dedup pattern continues)** — 5 flags this batch: KDDI AI Cloud (kddi.com), SK Telecom GPUaaS (sktelecom.com), Reliance Jio AI (jio.com), Ooredoo Qatar AI Cloud (ooredoo.qa), FPT AI Factory (fpt.com). Cumulative across batches 19+20 = 11. R3 should run a pass over carrier AI cloud arms specifically.
- **Stale-news clearing** dominates LIGHT path — 2026-02-25 enrichment date means all news that wasn't a current event is stale. Bulk-clearing news during sweep is the right move; R2 + Signal Scan will rehydrate ICP records that get real signals.
- **Industry-tag drift (3 fresh this batch)** — Wiggins (CONSUMER_GOODS), Montana Internet (PROFESSIONAL_TRAINING_COACHING), United Electric Cooperative (ELECTRICAL_ELECTRONIC_MANUFACTURING). All three should be TELECOMMUNICATIONS. Add to Apollo-refresh queue for next Apollo-enabled run.
- **Owner mismatch caught** — Newwave Communications was assigned to Tim Z (International) despite state=Arizona. Fixed to Ken. R6 territory hygiene catches this normally; sweep is an opportunistic find.
- **Hydrogen fuel cell DC operators (Greenfield reclass)** — EdgeCloudLink reclassed to Greenfield sub (no operating sites yet). Different from Symbio.one France (batch 19 — hydrogen fuel cell *vendor* reclassed to Other tier_5). The framework distinguishes operators that use hydrogen power from vendors that sell hydrogen fuel cells.
- **Aggressive Flagged for deletion** — Essextel reclassed from MSP-Aggregator with `manual_review_required` to Flagged for deletion. The brief itself stated "no MaiaEdge infrastructure alignment." Per Cooper's HOLD-policy=NONE operating note and Operating Principle #7, manual_review queue should drain via decisive classification.
- **Pure investment fund pivot (Bitfury)** — distinct from Crypto-to-AI operators (Bitfarms, Marathon, Mawson, Greenidge, CleanSpark all kept as NC5 because they operate). Bitfury now owns portfolio not infrastructure — moved to Other tier_5.
- **Geographic data error** — Mid-Rivers Communications provisioning_landscape said "Shiawassee County" (Michigan) when company is in Circle, MT serving Eastern Montana. Fixed inline. Worth a sweep-wide grep on other generic-AI-output records for geographic hallucinations.

## R3 dedup queue raised this batch

1. KDDI AI Cloud → KDDI (kddi.com)
2. SK Telecom GPUaaS → SK Telecom (sktelecom.com)
3. Reliance Jio AI → Jio (jio.com)
4. Ooredoo Qatar AI Cloud → Ooredoo Group (ooredoo.qa)
5. FPT AI Factory → FPT Corporation (fpt.com)

## D7 / edge-case-researcher flags this batch

- **Boldyn Networks** — global neutral host (BAI Communications + ZenFi). Sub-segment "Regional CLEC - Fiber operator" doesn't fit. Better classification: MSP/Aggregator → Managed Network Services - MSP, OR Fiber Op → Long Haul / Backbone via ZenFi NYC fiber. Requires research.

## Data-quality fixes pending Apollo refresh

- Wiggins Telephone Association (303889038029): industry CONSUMER_GOODS → TELECOMMUNICATIONS
- Montana Internet Corporation (303896263366): industry PROFESSIONAL_TRAINING_COACHING → TELECOMMUNICATIONS
- United Electric Cooperative (303879483119): industry ELECTRICAL_ELECTRONIC_MANUFACTURING → TELECOMMUNICATIONS or UTILITIES
- Optimum / Altice USA (303873077982): annualrevenue $54.6B looks like Altice Group total — Altice USA is ~$9B
- Boldyn Networks (300402132682): numberofemployees=3 is wrong (real ~1000+)

## Run health: GREEN

- All 50 HubSpot writes succeeded (50/50 = 100%)
- No 429s, no 4xx errors, no 5xx errors
- 0 Apollo credits consumed (Apollo-disabled mode)
- 2 web_searches performed (Bitfury investor pivot, Greenidge Q1 2026 status) — both consequential reclassification inputs
- No HOLD escalations
- No concurrent-batch detection
- Audit log persisted on disk
