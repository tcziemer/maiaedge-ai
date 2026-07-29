## R-Tier-Audit 2026-06-10

- Total active accounts reviewed: 2860
- Tier changes written: 66
- Heat changes written: 0
- Manual override skips (tier writes only): 79
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (66 of 2860 = 2.3%, threshold 10% / 286)

### Engagement-field correction (this run)
`compute_tier` stale/sustained-quiet modifiers require a "last engagement" date. The prompt's nominal field `notes_last_activity_date` does not exist on the HubSpot Company object (0/2862 populated). Engagement was re-pulled from the genuine fields `hs_last_sales_activity_timestamp` ("Last Engagement Date") and `notes_last_contacted` ("Last Contacted"), using the most-recent of the two. `notes_last_updated` ("Last Activity Date") was deliberately EXCLUDED: dozens of records carry identical batch timestamps (e.g. 2026-06-08T20:20:00Z) from automated maintenance-note writes (incl. this routine's own tier notes), so it is not a valid rep-activity signal. Net effect vs the naive pull: Worldpay dropped (engagement 28d ago suppresses stale -> no change) and STTELEMEDIA corrected to T1->T2 (engagement 146d ago is inside the 180d sustained-quiet window).

### Why this is real drift (not a connector dropout)
`last_signal_date` is correctly populated (243 records) and engagement fields read correctly on spot-check. All 66 changes are signal-decay demotions and reflect the 2026-05-28 Signal Engine Unification, which narrowed `last_signal_date` to EVENT date - genuinely-old events (100-876 days) now read as stale/sustained-quiet where a detection-date would have looked fresh. 0 heat changes (heat already reflects the decayed dates).

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 192916122339 | ccr.net | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 193853915841 | evolvingsol.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 206938584804 | vcomsolutions.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 209026970360 | joinkllc.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |
| 209235507900 | aeris.net | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 229012870888 | redapt.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 251270645451 | spencerbuilding.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 251474980562 | 3snetwork.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 251591500491 | nowfiberair.ph | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 251659209448 | dayone.global | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_1 | tier_2 | +1 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1 = T2 |
| 254331348701 | sttelemediagdc.ph | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_1 | tier_2 | +1 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1 = T2 |
| 254549120742 | amplex.net | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 254549120743 | dynascale.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_3 | +1 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1 = T3 |
| 254558124747 | servermania.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 254572221114 | ippathways.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 254574022374 | brescobroadband.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 254626062049 | metrobloks.com | Data Center Colo Provider | AI Signals - colo | tier_1 | tier_3 | +2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 254627886802 | wintek.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 254885110478 | bendtel.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 254885110482 | chinamobileinternational.com | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | tier_1 | tier_2 | +1 | Default Network Operator(Tier 1 / VNO)/International Backbone Specialist - Network Op = T1, stale +1, sustained-quiet +1 = T2 |
| 254885110484 | cloudnium.net | Data Center Colo Provider | Standard - colo | tier_3 | tier_4 | +1 | Default Data Center Colo Provider/Standard - colo = T3, stale +1 = T4 |
| 254951523062 | stratanetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 255118549733 | dpfacilities.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 255118549734 | indytelcom.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 263392463556 | compugen.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 263560994527 | hamiltonmh.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264192113374 | adacen.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264192113384 | trgdatacenters.com | Data Center Colo Provider | AI Signals - colo | tier_1 | tier_3 | +2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 264260027123 | colocationnorthwest.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264355635944 | fibertown.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264413011658 | cleanspark.com | NeoCloud | Crypto to AI - Neoclouds | tier_1 | tier_2 | +1 | Default NeoCloud/Crypto to AI - Neoclouds = T1, stale +1 = T2 |
| 264414880442 | archerdatacenters.com | Data Center Colo Provider | Greenfield | tier_2 | tier_3 | +1 | Default Data Center Colo Provider/Greenfield = T2, stale +1, sustained-quiet +1 = T3 |
| 264588752580 | fnts.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 264590543559 | greenhousedata.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264590543560 | fiberstate.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264590543563 | whitelabelitsolutions.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264592334569 | midconrecovery.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 264594125521 | rack59.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 267091939028 | smartaira.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 267091939030 | ena.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 267927865022 | sunwire.ca | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 267969423051 | spectrumvoip.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 268073696978 | gopioneer.com | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_5 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4, stale +1, sustained-quiet +1 = T5 |
| 268111627984 | uniserve.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_3 | +1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1 = T3 |
| 268197554884 | wirestar.net | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 268197554886 | paulbunyantech.com | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_5 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4, stale +1, sustained-quiet +1 = T5 |
| 268208386759 | truespeed.ca | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 268208386760 | nitelusa.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 268208386761 | velocitymsc.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 268241646267 | skymesh.net.au | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 268241651445 | teliax.com | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 268250706655 | cogeco.ca | Fiber Operator | Regional Cable Operator - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional Cable Operator - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 268250706656 | oshean.org | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_5 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4, stale +1, sustained-quiet +1 = T5 |
| 268252506815 | calltower.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 291518043894 | sifinetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 292796237529 | surfinternet.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |
| 297782865628 | imon.net | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | tier_3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stacked -1, stale +1 = T3 |
| 303379474153 | americanrepartners.com | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 318220841719 | orange.be | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 | tier_2 | +1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1, stale +1, sustained-quiet +1 = T2 |
| 320811765446 | luxconnect.lu | Data Center Colo Provider | Standard - colo | tier_3 | tier_5 | +2 | Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5 |
| 320875891448 | pilotfiber.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |
| 322357185260 | bluesuedenetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1, sustained-quiet +1 = T4 |
| 322677223115 | lilly.com | Enterprise-CustomerSegment | Healthcare Systems - Enterprise | tier_3 | tier_4 | +1 | Default Enterprise-CustomerSegment/Healthcare Systems - Enterprise = T3, stale +1 = T4 |
| 323824642762 | netrixglobal.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 324060146411 | net2phone.ca | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_2 | tier_4 | +2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 326325669589 | celeste.fr | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| (none) | | | | computed_heat == current_heat for all 2860 records |

### Summary

```
R-Tier-Audit - 2026-06-10 (daily M-F)

Total active accounts reviewed: 2860

Tier changes written: 66
  Promotions (toward Tier 1): 0
  Demotions (toward Tier 5): 66

Heat changes written: 0
  Hot/Warm -> cooler: 0
  Cool/Cold -> hotter: 0
  Heat writes on target-account records: 0

Heat distribution after this run (all active ICP):
  :red_circle: Hot: 37
  :large_orange_circle: Warm: 50
  :large_yellow_circle: Cool: 103
  :white_circle: Cold: 2670

Manual override skips (hs_is_target_account=true, tier only): 79
Stale signals decayed (+1 tier): 66
Sustained quiet decayed (+1 tier additional): 54
Open-deal promotions (-1 tier): 0

Top 10 tier changes by delta:
1. CCR Technologies (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4
2. Evolving Solutions (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained-quiet +1 = T4
3. vCom Solutions (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4
4. Aeris Communications (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4
5. Redapt (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Managed Network Services - MSP = T2, stale +1, sustained-quiet +1 = T4
6. Spencer Building Carrier Hotel (Data Center Colo Provider): tier_3 -> tier_5 -- Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5
7. LWS Network Pte Ltd (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1, sustained-quiet +1 = T4
8. ServerMania (Data Center Colo Provider): tier_3 -> tier_5 -- Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained-quiet +1 = T5
9. IP Pathways (MSP/Aggregator): tier_2 -> tier_4 -- Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4
10. Metrobloks (Data Center Colo Provider): tier_1 -> tier_3 -- Default Data Center Colo Provider/AI Signals - colo = T1, stale +1, sustained-quiet +1 = T3

Unknown (segment, sub-segment) pair warnings: 6
  - Kordia (251536944849): Unknown/null pair: 'Network Operator(Tier 1 / VNO)','Regional CLEC - Fiber operator' -> no-op, segment null fallback
  - Trans Pacific Networks (TPN) (318106540781): Unknown/null pair: 'Fiber Operator','Subsea cable operator' -> no-op, segment null fallback
  - Grupo GTD Chile (319135939295): Unknown/null pair: 'Network Operator(Tier 1 / VNO)','Regional CLEC - Fiber operator' -> no-op, segment null fallback
  - Gtd Colombia (326165246700): Unknown/null pair: 'Network Operator(Tier 1 / VNO)','Regional CLEC - Fiber operator' -> no-op, segment null fallback
  - WiLine Networks (326183183051): Unknown/null pair: 'Network Operator(Tier 1 / VNO)','Regional CLEC - Fiber operator' -> no-op, segment null fallback
  - Gtd Peru (326259427057): Unknown/null pair: 'Network Operator(Tier 1 / VNO)','Regional CLEC - Fiber operator' -> no-op, segment null fallback

Next run: 2026-06-11 3pm CT
```

### Manual-override tier skips (drift suppressed, hs_is_target_account=true)

| Company ID | Name | Current | Would-be (not written) | Reason |
|---|---|---|---|---|
| 103770392271 | Ecotel Communication | tier_2 | tier_1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, open-deal -1 = T1 |
| 107187281647 | Lumen Technologies | tier_2 | tier_1 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, hot -1, stacked -1 = T1 |
| 133493528256 | Windstream Wholesale | tier_2 | tier_3 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, stale +1, sustained-quiet +1 = T3 |
| 133506047726 | Cirion Technologies | tier_2 | tier_1 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, hot -1 = T1 |
| 133827394280 | Momentum | tier_2 | tier_1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, open-deal -1 = T1 |
| 175225132733 | Frontier | tier_2 | tier_3 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, stale +1 = T3 |
| 185543487196 | Flo Networks | tier_2 | tier_1 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, open-deal -1 = T1 |
| 192899501813 | HCL Enterprise | tier_1 | tier_4 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 193853195971 | C Spire | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 193856074473 | Great Plains Communications | tier_2 | tier_1 | Default Fiber Operator/Long Haul / Backbone - Fiber operator = T2, hot -1 = T1 |
| 193866158814 | FiberLight | tier_2 | tier_4 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |
| 193906531045 | Cologix | tier_1 | tier_2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1 = T2 |
| 193910127352 | Zayo | tier_2 | tier_1 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, hot -1, stacked -1 = T1 |
| 194004502211 | PhoenixNAP | tier_1 | tier_3 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 208821148373 | BTS | tier_2 | tier_3 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, stale +1 = T3 |
| 223979096790 | Acuutech | tier_2 | tier_1 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, open-deal -1 = T1 |
| 251513968344 | Ting Internet | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 251533417160 | Digital Edge DC - Hong Kong, Hong Kong | tier_2 | tier_3 | Default Data Center Colo Provider/Standard - colo = T3 = T3 |
| 251535204084 | Hawaiian Telcom | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 251535204086 | Light Source Communications | tier_2 | tier_1 | Default Fiber Operator/Dark Fiber Specialist - Fiber Operator = T2, hot -1 = T1 |
| 251574626020 | H5 Data Centers | tier_1 | tier_2 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1 = T2 |
| 251591500494 | Maincubes Secure Datacenters | tier_1 | tier_2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1 = T2 |
| 251593554625 | Bridgepointe Technologies | tier_2 | tier_3 | Default MSP/Aggregator/TSD Technology Services Distributor - MSP = T3 = T3 |
| 251661009604 | EXA Infrastructure | tier_1 | tier_2 | Default Network Operator(Tier 1 / VNO)/Pure Wholesale Carrier - Network Op = T1, stale +1, sustained-quiet +1 = T2 |
| 255207759559 | COPT Data Centers | tier_1 | tier_3 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 255207759560 | Stack Infrastructure | tier_1 | tier_3 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 264034971368 | Technium | tier_2 | tier_1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, open-deal -1 = T1 |
| 264414880445 | CloudHQ | tier_1 | tier_3 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 265926495973 | Novva Data Centers | tier_1 | tier_2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1 = T2 |
| 266871288512 | Point Broadband | tier_2 | tier_3 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, stale +1 = T3 |
| 266984898241 | Liquid Web | tier_2 | tier_1 | Default NeoCloud/AI Infrastructure providers - Neocloud = T1 = T1 |
| 267092339390 | Atnorth | tier_1 | tier_2 | Default Data Center Colo Provider/AI Signals - colo = T1, stale +1 = T2 |
| 300408171229 | TD Synnex | tier_1 | tier_3 | Default MSP/Aggregator/TSD Technology Services Distributor - MSP = T3 = T3 |
| 303312798423 | PowerHouse Data Centers | tier_1 | tier_3 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1, sustained-quiet +1 = T3 |
| 303445718756 | T-Systems | tier_1 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 309393917654 | Nexthop | tier_2 | tier_1 | Default Fiber Operator/Dark Fiber Specialist - Fiber Operator = T2, open-deal -1 = T1 |
| 314142327527 | Flexnode | tier_2 | tier_1 | Default NeoCloud/AI Infrastructure providers - Neocloud = T1 = T1 |
| 314374535919 | Consolidated Communications | tier_2 | tier_1 | Default Fiber Operator/Long Haul / Backbone - Fiber operator = T2, hot -1, stacked -1 = T1 |
| 316149788366 | Brightspeed Business | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 316498875122 | BW Digital | tier_1 | tier_2 | Default Network Operator(Tier 1 / VNO)/Subsea cable operator = T2 = T2 |
| 317273591519 | Inference.net | tier_1 | tier_2 | Default NeoCloud/Tier 1 Inference - Neocloud = T2 = T2 |
| 318219105016 | Telarus | tier_1 | tier_3 | Default MSP/Aggregator/Master Agent - MSP = T3 = T3 |
| 318223364848 | TIM Brasil | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 = T1 |
| 319132391104 | Azteca Comunicaciones Colombia | tier_1 | tier_2 | Default Fiber Operator/Long Haul / Backbone - Fiber operator = T2 = T2 |
| 319135943411 | Alfa Lebanon | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 = T1 |
| 319137756912 | Moratelindo | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 = T1 |
| 319141316329 | Internet Thailand | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 = T1 |
| 319145743057 | Copel Telecom | tier_1 | tier_2 | Default Fiber Operator/Long Haul / Backbone - Fiber operator = T2 = T2 |
| 319154865857 | TelOne Zimbabwe | tier_2 | tier_1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 = T1 |
| 320366166738 | BAM Broadband | tier_2 | tier_4 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4 = T4 |
| 320373812947 | IQ Fiber | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 320378046180 | GoNetspeed (formerly OTELCO) | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 320875891447 | BIG Fiber | tier_2 | tier_1 | Default Fiber Operator/Dark Fiber Specialist - Fiber Operator = T2, hot -1 = T1 |
| 320876610267 | Cudo Compute | tier_2 | tier_1 | Default NeoCloud/AI Infrastructure providers - Neocloud = T1 = T1 |
| 320988084985 | New Era Energy & Digital | tier_2 | tier_1 | Default Data Center Colo Provider/Greenfield = T2, hot -1 = T1 |
| 320997081786 | ambiFOX GmbH | tier_2 | tier_1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2, open-deal -1 = T1 |
| 321842590405 | Logicalis | tier_1 | tier_2 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2 = T2 |
| 322038348534 | WOW! (WideOpenWest) | tier_2 | tier_4 | Default Fiber Operator/Regional Cable Operator - Fiber operator = T3, stale +1 = T4 |
| 322405956291 | Google Fiber | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 322761764548 | Shentel | tier_2 | tier_3 | Default Fiber Operator/Regional Cable Operator - Fiber operator = T3 = T3 |
| 323259815670 | Andromeda | tier_2 | tier_1 | Default NeoCloud/AI Infrastructure providers - Neocloud = T1 = T1 |
| 323821758151 | Bluebird Network | tier_3 | tier_4 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4 |
| 323823198919 | Lightpath | tier_2 | tier_1 | Default Fiber Operator/Dark Fiber Specialist - Fiber Operator = T2, stacked -1 = T1 |
| 323996380884 | CyberNet Communications | tier_2 | tier_3 | Default MSP/Aggregator/Master Agent - MSP = T3 = T3 |
| 324001849047 | Sandler Partners | tier_1 | tier_3 | Default MSP/Aggregator/Master Agent - MSP = T3 = T3 |
| 324007013094 | MetroNet | tier_2 | tier_3 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 = T3 |
| 324037036767 | Intelisys | tier_1 | tier_3 | Default MSP/Aggregator/TSD Technology Services Distributor - MSP = T3 = T3 |
| 324037036787 | AppDirect | tier_1 | tier_2 | Default MSP/Aggregator/TSD Technology Services Distributor - MSP = T3, hot -1 = T2 |
| 324037036788 | X4 Solutions | tier_1 | tier_3 | Default MSP/Aggregator/Master Agent - MSP = T3 = T3 |
| 324038855390 | ScanSource | tier_1 | tier_2 | Default MSP/Aggregator/TSD Technology Services Distributor - MSP = T3, hot -1 = T2 |
| 324060022514 | Astound | tier_2 | tier_3 | Default Fiber Operator/Regional Cable Operator - Fiber operator = T3 = T3 |
| 324170890970 | Avant Communications | tier_1 | tier_2 | Default MSP/Aggregator/Master Agent - MSP = T3, hot -1 = T2 |
| 324190689997 | Paperspace | tier_2 | tier_1 | Default NeoCloud/AI Infrastructure providers - Neocloud = T1 = T1 |
| 326733731547 | Lyceum Technology | tier_2 | tier_1 | Default NeoCloud/Sovereign AI Clouds - Neocloud = T1 = T1 |
| 326733731545 | Fireworks AI | tier_1 | tier_2 | Default NeoCloud/Tier 1 Inference - Neocloud = T2 = T2 |
| 326710096623 | SiliconFlow | tier_1 | tier_2 | Default NeoCloud/Tier 1 Inference - Neocloud = T2 = T2 |
| 326646218484 | AUCloud (AUCyber) | tier_3 | tier_4 | Default MSP/Aggregator/Cloud + Telecom Hybrid MSP - MSP = T2, stale +1, sustained-quiet +1 = T4 |
| 326646218483 | Featherless AI | tier_1 | tier_2 | Default NeoCloud/Tier 1 Inference - Neocloud = T2 = T2 |
| 326585940676 | Southern Cross AI (SCX) | tier_1 | tier_2 | Default NeoCloud/Sovereign AI Clouds - Neocloud = T1, stale +1, sustained-quiet +1 = T2 |

### Quality checks
- All eligible records processed: 2860 active (2862 loaded - 2 type=Customer). OK
- No tier writes on hs_is_target_account=true: 79 skipped, 0 written. OK
- All 66 tier writes have a paired HubSpot company note (66 notes created, 0 failed). OK
- Circuit breaker threshold 10% computed against 2860 active ICP. OK
- last_enriched_date NOT bumped (tier/heat-only writes). OK