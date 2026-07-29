## R-Tier-Audit 2026-06-05

- Total active accounts reviewed: 2809
- Tier changes written: 45
- Heat changes written: 10
- Manual override skips (tier writes only, hs_is_target_account=true): 69
- Heat writes on target-account records (not skipped): 1
- Unknown (segment, sub-segment) pair warnings: 7
- Circuit breaker triggered: NO (53 of 2809 = 1.89%, threshold 10%)
- last_enriched_date bumped: NO (tier/heat-only writes per Unified Stamping Policy)

### Per-record tier changes

| Company ID | Name | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 194004502229 | Arvig | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 (default), open-deal -1 = T2 |
| 297906089706 | Fibernow | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 (default), open-deal -1 = T2 |
| 316196415207 | Fastlink | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | tier_1 | -2 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 316203554520 | Telesom | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | tier_1 | -2 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 316218856147 | S&T Communications | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4 (default), no modifiers = T4 |
| 316283788007 | Telekom2 | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | tier_3 | tier_1 | -2 | Default Network Operator(Tier 1 / VNO)/Regional CLEC - Fiber operator = T1 (unknown-pair-fallback), no modifiers = T1 |
| 316598423244 | CIMA Telecom | MSP/Aggregator | Telecom Aggregator - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 (default), no modifiers = T2 |
| 316620030686 | Fibernetics | MSP/Aggregator | Telecom Aggregator - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 (default), no modifiers = T2 |
| 318106540783 | SBTS | MSP/Aggregator | Managed Network Services - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Managed Network Services - MSP = T2 (default), no modifiers = T2 |
| 318231692000 | Megatel Netcom Corporation | MSP/Aggregator | Telecom Aggregator - MSP | tier_4 | tier_2 | -2 | Default MSP/Aggregator/Telecom Aggregator - MSP = T2 (default), no modifiers = T2 |
| 318339892957 | Sky UK | Network Operator(Tier 1 / VNO) | Cable MSO Enterprise Division - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Cable MSO Enterprise Division - Network Op = T1 (default), no modifiers = T1 |
| 319125023448 | WX Network Panama | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319126830809 | Island Broadband | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319135982321 | Onemax | Fiber Operator | Regional CLEC - Fiber operator | tier_1 | tier_3 | +2 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 (default), no modifiers = T3 |
| 319173102318 | Fast Link Iraq | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319173106384 | PTI Pacifica | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319176778433 | Movicel Angola | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319176780504 | NetCo Lebanon | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319176782542 | Myanmar Net | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319182206700 | BVI Phones | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319182207726 | Setar | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319182213851 | SWIFT Networks | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319182218965 | Canl+ | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319182219973 | PDS Pacific Data Systems | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319190683379 | bmobile Vodafone | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319190684408 | Massy Stores Telecom | MSP/Aggregator | Managed Network Services - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Managed Network Services - MSP = T2 (default), no modifiers = T2 |
| 319190688481 | Hai Telecommunications | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319190691567 | Hexabyte | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319190692541 | Lightspeed Communications | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319190694588 | Newcom Gibraltar | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319194131176 | Flow USVI | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319194135288 | Cobranet | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319197820613 | Logic | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319197822663 | Standard Telecom DRC | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319197829831 | CSL Samoa | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319204732629 | Fiberail | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | tier_3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3 (default), no modifiers = T3 |
| 319204759254 | Digicel Bermuda | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319204762327 | Golis Telecom | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 319208306408 | Tizeti Networks | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 326163435208 | Win s.a. (NRB) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1 (default), no modifiers = T1 |
| 326167082742 | Modern Networks | MSP/Aggregator | Managed Network Services - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Managed Network Services - MSP = T2 (default), no modifiers = T2 |
| 326183183051 | WiLine Networks | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | tier_3 | tier_1 | -2 | Default Network Operator(Tier 1 / VNO)/Regional CLEC - Fiber operator = T1 (unknown-pair-fallback), no modifiers = T1 |
| 326325665485 | Global Transit Communications | Network Operator(Tier 1 / VNO) | Subsea cable operator | tier_1 | tier_2 | +1 | Default Network Operator(Tier 1 / VNO)/Subsea cable operator = T2 (default), no modifiers = T2 |
| 326325669587 | Comms Group | MSP/Aggregator | Managed Network Services - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Managed Network Services - MSP = T2 (default), no modifiers = T2 |
| 326334620360 | SCB Global | MSP/Aggregator | Managed Network Services - MSP | tier_3 | tier_2 | -1 | Default MSP/Aggregator/Managed Network Services - MSP = T2 (default), no modifiers = T2 |

### Per-record heat changes

| Company ID | Name | Old Heat | New Heat | Target? | Reason |
|---|---|---|---|---|---|
| 193865438935 | 123Net | Cold | Cool | no | last_signal_date (event) 15d ago, score 0 |
| 194004502229 | Arvig | Cold | Hot | no | open deal past appointmentscheduled |
| 266871288513 | GiGstreem | Cold | Cool | no | last_signal_date (event) 24d ago, score 0 |
| 291537915620 | Clearwave Fiber | Cold | Cool | no | last_signal_date (event) 21d ago, score 0 |
| 297888731896 | NetCarrier | Cold | Cool | no | last_signal_date (event) 18d ago, score 0 |
| 297906089706 | Fibernow | Cold | Hot | no | open deal past appointmentscheduled |
| 297934868197 | Smart City Telecom | Cold | Cool | no | last_signal_date (event) 8d ago, score 0 |
| 320875891448 | Pilot | Cold | Cool | no | last_signal_date (event) 51d ago, score 0 |
| 322686735045 | altafiber | Cold | Cool | YES | last_signal_date (event) 110d ago, score 0 |
| 323971392219 | IREN | Cold | Hot | no | signal_count_last_30d=2 (stacked) |

### Warnings (unknown segment/sub-segment pairs -> null fallback; data-quality follow-up)

- 251536944849 (Kordia): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
- 316283788007 (Telekom2): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
- 318106540781 (Trans Pacific Networks (TPN)): Unknown (segment, sub-segment) pair: Fiber Operator, Subsea cable operator. Using Fiber Operator null fallback.
- 319135939295 (Grupo GTD Chile): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
- 326165246700 (Gtd Colombia): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
- 326183183051 (WiLine Networks): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
- 326259427057 (Gtd Peru): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.

### Run summary

