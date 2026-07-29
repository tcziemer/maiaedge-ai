# R-Tier-Audit 2026-06-01

- Total active accounts reviewed: 2570
- Tier changes written: 68
- Heat changes written: 4
- Manual override skips (tier writes only): 323
- Heat writes on target-account records (not skipped): 1
- Circuit breaker triggered: NO (72 changes vs 257 threshold = 2.8% < 10%)

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 186793926376 | vyvebb.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stacked -1 = T2. |
| 192916122339 | ccr.net | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 193853915841 | evolvingsol.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 206938584804 | vcomsolutions.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_3 | +1 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1 = T3. |
| 209026970360 | joinkllc.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4. |
| 209235507900 | aeris.net | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 229012870888 | redapt.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 251270645451 | spencerbuilding.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 251474980562 | 3snetwork.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 251574698722 | globalsecurelayer.com.au | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/International Backbone Specialist - Network Op = T1 = T1. |
| 251591500491 | nowfiberair.ph | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 251659209448 | dayone.global | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_1 | tier_2 | +1 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1 = T2. |
| 254331348701 | sttelemediagdc.ph | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_1 | tier_3 | +2 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1, sustained quiet +1 = T3. |
| 254549120742 | amplex.net | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 254549120743 | dynascale.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_3 | +1 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1 = T3. |
| 254558124747 | servermania.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 254572221114 | ippathways.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 254574022374 | brescobroadband.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 254626062049 | metrobloks.com | Data Center Colo Provider | AI Signals - colo | tier_1 | tier_3 | +2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1, sustained quiet +1 = T3. |
| 254627886802 | wintek.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 254885110478 | bendtel.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 254885110482 | chinamobileinternational.com | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | tier_1 | tier_2 | +1 | Default Network Operator(Tier 1 / VNO)/International Backbone Specialist - Network Op = T1, stale +1, sustained quiet +1 = T2. |
| 254885110484 | cloudnium.net | Data Center Colo Provider | Standard - colo | tier_3 | tier_4 | +1 | Default Data Center Colo Provider/Standard - colo = T3, stale +1 = T4. |
| 254951523062 | stratanetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 255118549733 | dpfacilities.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 255118549734 | indytelcom.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 263392463556 | compugen.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 263560994527 | hamiltonmh.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264192113374 | adacen.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264192113384 | trgdatacenters.com | Data Center Colo Provider | AI Signals - colo | tier_1 | tier_3 | +2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1, sustained quiet +1 = T3. |
| 264260027123 | colocationnorthwest.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264355635944 | fibertown.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264414880442 | archerdatacenters.com | Data Center Colo Provider | Greenfield | tier_2 | tier_3 | +1 | Default Data Center Colo Provider/Greenfield = T2, stale +1, sustained quiet +1 = T3. |
| 264588752580 | fnts.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_3 | +1 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1 = T3. |
| 264590543559 | greenhousedata.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264590543560 | fiberstate.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264590543563 | whitelabelitsolutions.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264592334569 | midconrecovery.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 264594125521 | rack59.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 267091939028 | smartaira.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 267091939030 | ena.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 267927865022 | sunwire.ca | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 267969423051 | spectrumvoip.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 268073696978 | gopioneer.com | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_5 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4, stale +1, sustained quiet +1 = T5. |
| 268111627984 | uniserve.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_3 | +1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1 = T3. |
| 268197554884 | wirestar.net | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 268197554886 | paulbunyantech.com | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_5 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4, stale +1, sustained quiet +1 = T5. |
| 268208386759 | truespeed.ca | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 268208386760 | nitelusa.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 268208386761 | velocitymsc.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 268241646267 | skymesh.net.au | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 268241651445 | teliax.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 268250706655 | cogeco.ca | Fiber Operator | Regional Cable Operator - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional Cable Operator - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 268250706656 | oshean.org | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_5 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4, stale +1, sustained quiet +1 = T5. |
| 268252506815 | calltower.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 297934868197 | smartcitytelecom.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, hot -1 = T2. |
| 303379474153 | americanrepartners.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 318220841719 | orange.be | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | tier_2 | +1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1, stale +1, sustained quiet +1 = T2. |
| 320811765446 | luxconnect.lu | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. |
| 322357185260 | bluesuedenetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained quiet +1 = T4. |
| 322843549398 | tec.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, hot -1 = T2. |
| 323824642762 | netrixglobal.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 324060146411 | net2phone.ca | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4. |
| 325183491791 | airbridgebroadband.com | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3. |
| 325187311308 | xplore.ca | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | tier_3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3. |
| 325187311316 | slothnetworks.net | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_4 | tier_1 | -3 | Default Network Operator(Tier 1 / VNO)/Pure Wholesale Carrier - Network Op = T1 = T1. |
| 325222860480 | edgevana.com | NeoCloud | AI Infrastructure providers - Neocloud | tier_2 | tier_1 | -1 | Default NeoCloud/AI Infrastructure providers - Neocloud = T1 = T1. |
| 325277002462 | workonline.africa | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/International Backbone Specialist - Network Op = T1 = T1. |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 155473925856 | revnet.host | Hot | Cold | recompute per compute_signal_heat (last_signal_date/score/count + open-deal state) |
| 186793926376 | vyvebb.com | Warm | Hot | recompute per compute_signal_heat (last_signal_date/score/count + open-deal state) |
| 193865437936 | sonic.com | Warm | Cool | recompute per compute_signal_heat (last_signal_date/score/count + open-deal state) |
| 322386259648 | gsc.tech | Warm | Cool | recompute per compute_signal_heat (last_signal_date/score/count + open-deal state) |

---

```
R-Tier-Audit - 2026-06-01 (daily M-F)

Total active accounts reviewed: 2570

Tier changes written: 68
  Promotions (lower tier number, toward Tier 1): 8
  Demotions (higher tier number, toward Tier 5): 60

Heat changes written: 4
  Hot/Warm -> cooler: 3
  Cool/Cold -> hotter: 1
  Heat writes on target-account records (not skipped): 1

Heat distribution after this run (across all active ICP):
  Hot: 33
  Warm: 26
  Cool: 75
  Cold: 2436

Manual override skips (hs_is_target_account=true, tier only): 323
Stale signals decayed (+1 tier): 62
Sustained quiet decayed (+1 tier additional): 53
Open-deal promotions (-1 tier): 3

Top 10 tier changes by delta:
1. Sloth Networks (Network Operator(Tier 1 / VNO)): tier_4 -> tier_1 -- Default Network Operator(Tier 1 / VNO)/Pure Wholesale Carrier - Network Op = T1 = T1.
2. CCR Technologies (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4.
3. Evolving Solutions (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained quiet +1 = T4.
4. Aeris Communications (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4.
5. Redapt (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained quiet +1 = T4.
6. Spencer Building Carrier Hotel (Data Center Colo Provider): tier_3 -> tier_5 -- Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5.
7. LWS Network Pte Ltd (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained quiet +1 = T4.
8. STTELEMEDIA Global Data Centres (Data Center Colo Provider): tier_1 -> tier_3 -- Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1, sustained quiet +1 = T3.
9. ServerMania (Data Center Colo Provider): tier_3 -> tier_5 -- Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5.
10. IP Pathways (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained quiet +1 = T4.

Top 10 heat changes:
1. RevNet: Hot -> Cold -- recompute per compute_signal_heat
2. vyvebb: Warm -> Hot -- recompute per compute_signal_heat
3. Sonic Telecom: Warm -> Cool -- recompute per compute_signal_heat
4. Granite State Communications: Warm -> Cool -- recompute per compute_signal_heat

Unknown (segment, sub-segment) pair warnings: 1
  - Trans Pacific Networks (TPN) (318106540781): (Fiber Operator, Subsea cable operator) -> segment null fallback applied (no-op this run; tier already matched fallback)

Next run: 2026-06-02 3pm CT
```