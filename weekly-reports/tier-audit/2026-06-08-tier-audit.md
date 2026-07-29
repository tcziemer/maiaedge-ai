# R-Tier-Audit - 2026-06-08 (daily M-F)

- Total active accounts reviewed: 2857 (active ICP, type != Customer; 2 Customer-type excluded)
- Tier changes written: 64 (promotions 62, demotions 2)
- Heat changes written: 12
- Manual override skips (tier writes only, hs_is_target_account=true): 355
- Heat writes on target-account records (not skipped): 12
- Circuit breaker triggered: NO (76 of 2857 = 2.66%, threshold 10%)
- Apollo consumed: 0 | last_enriched_date bumped: 0 (per Unified Stamping Policy)

### Per-record tier changes

| Company ID | Name | Segment | Sub-segment | Old | New | Reason |
|---|---|---|---|---|---|---|
| 326325669589 | Celeste | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |
| 297782865628 | ImOn Communications | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stacked -1 = T2 |
| 292796237529 | Surf Internet | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 268111627984 | Uniserve | MSP/Aggregator | Telecom Aggregator - MSP | tier_3 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 264588752580 | FNTS | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_3 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 264413011658 | CleanSpark | NeoCloud | Crypto to AI - Neoclouds | tier_1 | tier_2 | Default NeoCloud/Crypto to AI - Neoclouds = T1, stale +1 = T2 |
| 254885110484 | Cloudnium | Data Center Colo Provider | Standard - colo | tier_4 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 254549120743 | Dynascale | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_3 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 251659209448 | DayOne | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_2 | tier_1 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1 = T1 |
| 209026970360 | joink | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 206938584804 | vCom Solutions | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_3 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 192916122339 | CCR Technologies | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 193853915841 | Evolving Solutions | MSP/Aggregator | Managed Network Services - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Managed Network Services - MSP = T2 = T2 |
| 209235507900 | Aeris Communications | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 229012870888 | Redapt | MSP/Aggregator | Managed Network Services - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Managed Network Services - MSP = T2 = T2 |
| 251270645451 | Spencer Building Carrier Hotel | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 251474980562 | LWS Network Pte Ltd | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 251591500491 | NOW Telecom | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 254331348701 | STTELEMEDIA Global Data Centres | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_3 | tier_1 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1 = T1 |
| 254549120742 | Amplex Internet | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 254558124747 | ServerMania | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 254572221114 | IP Pathways | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 254574022374 | BrescoBroadband | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 254626062049 | Metrobloks | Data Center Colo Provider | AI Signals - colo | tier_3 | tier_1 | Default Data Center Colo Provider/AI Signals - colo = T1 = T1 |
| 254627886802 | Wintek | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 254885110478 | BendTel | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 254885110482 | China Mobile International | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/International Backbone Specialist - Network Op = T1 = T1 |
| 254951523062 | Strata Networks | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 255118549733 | DP Facilities, Inc. | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 255118549734 | Indy Telcom | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 263392463556 | Compugen | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 263560994527 | Hamilton Managed Hosting | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264192113374 | Adacen | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264192113384 | TRG Datacenters | Data Center Colo Provider | AI Signals - colo | tier_3 | tier_1 | Default Data Center Colo Provider/AI Signals - colo = T1 = T1 |
| 264260027123 | Colocation Northwest | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264355635944 | FIBERTOWN | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264414880442 | Archer Datacenters | Data Center Colo Provider | Greenfield | tier_3 | tier_2 | Default Data Center Colo Provider/Greenfield = T2 = T2 |
| 264590543559 | Lunavi (Green House Data) | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264590543560 | FiberState | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264590543563 | Whitelabel ITSolutions | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264592334569 | MIDCON Recovery Solutions | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 264594125521 | RACK59 | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 267091939028 | Smartaira | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 267091939030 | ENA | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 267927865022 | Sunwire | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 267969423051 | SpectrumVoIP | MSP/Aggregator | Managed Network Services - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Managed Network Services - MSP = T2 = T2 |
| 268073696978 | Pioneer Telephone Cooperative | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_5 | tier_4 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4 = T4 |
| 268197554884 | WireStar Networks | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 268197554886 | Paul Bunyan Technologies | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_5 | tier_4 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4 = T4 |
| 268208386759 | Truespeed Internet Services | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 268208386760 | Nitel | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 268208386761 | Velocity | MSP/Aggregator | Managed Network Services - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Managed Network Services - MSP = T2 = T2 |
| 268241646267 | SkyMesh | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 268241651445 | Teliax | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 = T2 |
| 268250706655 | Cogeco Connexion | Fiber Operator | Regional Cable Operator - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional Cable Operator - Fiber operator = T3 = T3 |
| 268250706656 | OSHEAN | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_5 | tier_4 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4 = T4 |
| 268252506815 | CallTower | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 291518043894 | SiFi Networks | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 303379474153 | American Real Estate Partners | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 318220841719 | Orange Belgium | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 = T1 |
| 320811765446 | LuxConnect | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 322357185260 | Blue Suede Networks | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 323824642762 | Netrix | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 324060146411 | Net2Phone Canada | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_4 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |

### Per-record heat changes

| Company ID | Name | Old Heat | New Heat | Reason | Target acct |
|---|---|---|---|---|---|
| 326713801456 | FlexAI | Cool | Cold | event>180d or no signal | yes |
| 326672302824 | Parasail | Warm | Cold | event>180d or no signal | yes |
| 326699605731 | Nava | Warm | Cold | event>180d or no signal | yes |
| 326703205065 | Corvex | Warm | Cold | event>180d or no signal | yes |
| 326715722484 | Prime Intellect | Warm | Cold | event>180d or no signal | yes |
| 326164366053 | STN (GPU One) | Warm | Cold | event>180d or no signal | yes |
| 326166215417 | Hot Aisle | Warm | Cold | event>180d or no signal | yes |
| 326690308818 | Qubrid AI | Warm | Cold | event>180d or no signal | yes |
| 326710096623 | SiliconFlow | Hot | Cold | event>180d or no signal | yes |
| 326646218483 | Featherless AI | Hot | Cold | event>180d or no signal | yes |
| 326733731545 | Fireworks AI | Hot | Cold | event>180d or no signal | yes |
| 326585940676 | Southern Cross AI (SCX) | Warm | Cold | event>180d or no signal | yes |

---

## Run summary

R-Tier-Audit - 2026-06-08 (daily M-F)

Total active accounts reviewed: 2857

Tier changes written: 64
  Promotions (toward Tier 1): 62
  Demotions (toward Tier 5): 2

Heat changes written: 12
  Hot/Warm/Cool -> cooler: 12
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 12

Heat distribution after this run (active ICP, approx):
  Hot: 38
  Warm: 50
  Cool: 103
  Cold: 2668

Manual override skips (hs_is_target_account=true, tier only): 355
Stale signals decayed (+1 tier): 2
Sustained quiet decayed (+1 tier additional): 0
Open-deal promotions (-1 tier): 0
Unknown (segment, sub-segment) pair warnings: 7

HubSpot audit notes written: 76 (one per change, all associated, 0 failures)

Quality checks:
  - All eligible records processed: PASS (Phase 1 count 2857 == processed + 355 target-skips, full pool computed)
  - No tier writes on hs_is_target_account=true: PASS (355 tier-skips; heat still written on 12 target records)
  - All writes have HubSpot notes: PASS (76/76 notes created + associated)
  - Circuit breaker threshold == 10%: PASS (computed 76/2857)
  - Local audit log persisted: PASS (this file)

Notes:
  - The 12 heat -> Cold corrections are all NeoCloud target accounts created earlier today whose creating routine set optimistic Hot/Warm/Cool heat without populating last_signal_date/last_signal_score (11 genuinely null; SCX had a 2025-10-22 event > 180d). Verified field population directly before writing - NOT a connector dropout (records carrying signals returned their dates normally). Heat is not frozen by hs_is_target_account, so these writes proceed per spec.
  - The 62 tier promotions are mostly records whose stored account_tier sat below their sub-segment default with no active modifiers (e.g. Standard-colo at T5 -> T3 default, MSP Cloud+Telecom Hybrid at T4 -> T2 default); R-Tier-Audit normalizes them to the canonical defaults. 2 demotions are stale-signal driven (Celeste, CleanSpark).
  - Open-deal company set (21 unique past appointmentscheduled) already carried Hot heat + open-deal tier; no additional drift from open deals this run.

Next run: 2026-06-09 3:00 PM CT
