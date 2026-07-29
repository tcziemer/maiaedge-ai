# Mass Re-Enrichment Sweep — Batch 16

- Sweep: `2026-05-18-post-phase-3-framework`
- Batch: 16
- Date: 2026-05-18
- Processed: 50/50
- Path mix: LIGHT 2 · MEDIUM 26 · FULL 21 · Flagged-for-deletion 1 · HOLD 0
- Apollo this batch: 0 credits (sweep cumulative unchanged)
- Pool remaining at end of batch: ~1,954 records

## Notable patterns this batch

- **2026-04-21 Phase-3-prep target_account=true international carrier wave continued** — 30 of 50 records were target_account=true small/mid international carriers with generic templated briefs (`carrier/MNO with external extension motion to business customers. Regional wholesale partnerships. [Region] Tier N.`). All got narrative refresh; tier writes skipped per inviolable rule.
- **Fiber Op → Network Op T1 flip for national incumbents continues** (5 this batch: Cable & Wireless Communications, 4iG, Orange Belgium, TIM Brasil, Totalplay). All hit Tier 1 Carrier - Network Op sub-segment + Tier 3 → Tier 2 promotion.
- **Fiber Op → MSP/Aggregator (Telecom Aggregator) for SIP/wholesale carrier hybrids continued** (3 this batch: Gamma UK, VIVARO TELECOM, Vívaro). ~13 total in sweep.
- **Network Op → Data Center Colo Provider** (2 this batch — new pattern): Medallion Communications Nigeria (Digital Realty-owned carrier-neutral DC, misclassified as carrier) and Matrix Brazil (SBA Edge subsidiary, was MSP).
- **Network Op → Other (vendor/partner)**: FiberHome Philippines confirmed as equipment vendor (Wuhan FiberHome subsidiary), not a carrier.
- **MSP → Other / Flagged**: Navarino Greece (specialty maritime SATCOM, not core ICP) → Other; Skymeric Technologies India (pivoted out of telecom to AI/RPA) → Flagged for deletion.
- **Apollo parent-revenue bleed prevalent**: Cloud4C ($16M revenue with 1700 emp impossible — subsidiary scope or holdco confusion). Skipped revenue write.
- **Data quality fixes**:
  - RedTrain: country India → Australia (HubSpot had wrong country); industry IMPORT_EXPORT → noted via brief
  - Epic Cyprus: domain epicnet.cy → epic.com.cy (typo)
  - LUS Fiber: provisioning_landscape was 5+ sentences (trimmed to 2); "[Date needed]" placeholder cleared
  - Cybernet PK: recent_news lacked date prefix (added [2026-05-13])

## R3 dedup flags raised

1. Vívaro (vivaro.com) vs VIVARO TELECOM (vivarotelecom.com) — Marcatel rebranded parent + telecom division
2. Matrix Brazil vs SBA Edge — Matrix acquired by SBA Communications; rebranded as SBA Edge
3. Medallion Communications Nigeria vs Digital Realty — acquired 2021, rebranded 2023
4. Forthnet Greece vs Nova / United Group — Forthnet legal entity, Nova operating brand
5. FLOW Jamaica vs Cable & Wireless Communications — same Liberty Caribbean group but distinct operating company (NOT a dedup candidate, just a note)

## D7 escalations

1. **KN Network Services Ltd (Barbados)** — knnetwork.bb. Limited public disclosure; parent KN Network Services group is infrastructure-services contractor (Ireland/UK ops). Classification uncertain — may be a contractor, not a carrier. Set to low_5069 confidence with D7 flag.

## Tier writes summary

- **Tier promotions** (target_account=false, full pipeline pass): 5 (C&W T3→T2, 4iG T3→T2, Orange Belgium T3→T2, TIM Brasil T3→T2, Totalplay T3→T2)
- **Tier demotions**: 1 (Navarino T2→T5 with Other reclassification)
- **Tier skipped (target_account=true)**: 30
- **Tier unchanged**: ~14

## Segment changes this batch (14 total)

| # | Company | Old segment | New segment |
|---|---|---|---|
| 1 | Cable & Wireless Communications | Fiber Operator | Network Operator(Tier 1 / VNO) |
| 2 | Gamma | Fiber Operator | MSP/Aggregator |
| 3 | 4iG | Fiber Operator | Network Operator(Tier 1 / VNO) |
| 4 | Orange Belgium | Fiber Operator | Network Operator(Tier 1 / VNO) |
| 5 | VIVARO TELECOM | Fiber Operator | MSP/Aggregator |
| 6 | TIM Brasil | Fiber Operator | Network Operator(Tier 1 / VNO) |
| 7 | Vívaro | Fiber Operator | MSP/Aggregator |
| 8 | Totalplay | Fiber Operator | Network Operator(Tier 1 / VNO) |
| 9 | Matrix | MSP/Aggregator | Data Center Colo Provider |
| 10 | Navarino | MSP/Aggregator | Other |
| 11 | FiberHome Philippines | Network Operator(Tier 1 / VNO) | Other |
| 12 | Medallion Communications | Network Operator(Tier 1 / VNO) | Data Center Colo Provider |
| 13 | Skymeric Technologies | MSP/Aggregator | Flagged for deletion |
| 14 | RedTrain | Network Operator(Tier 1 / VNO) | Fiber Operator |

## Per-record summary

### Records 1-10 (FULL/LIGHT mix, mostly Fiber Op flips)
- Cable & Wireless Communications (316531667654): FULL · Fiber Op → Network Op T1 · T3→T2
- Gamma (316618313425): FULL · Fiber Op → MSP/Aggregator · T3→T3
- 4iG (316627222264): FULL · Fiber Op → Network Op T1 · T3→T2
- Orange Belgium (318220841719): FULL · Fiber Op → Network Op T1 · T3→T2
- VIVARO TELECOM (318219105990): FULL · Fiber Op → MSP/Aggregator · T3→T3 · R3 flag
- TIM Brasil (318223364848): FULL · Fiber Op → Network Op T1 · T3→T2
- Cybernet (318352538353): LIGHT · MSP unchanged · T2→T2 · added date prefix
- Dobson Fiber (318347064049): LIGHT · Fiber Op unchanged · T3→T3
- Vívaro (318231673566): FULL · Fiber Op → MSP/Aggregator · T3→T3 · R3 dedup w/ VIVARO TELECOM
- Totalplay (318231695096): FULL · Fiber Op → Network Op T1 · T3→T2

### Records 11-20 (target_account=true Phase-3-prep templated briefs)
- MPT (319141268213): MEDIUM · target_account=true · narrative refresh · tier frozen at T1
- Dhiraagu (319137703629): MEDIUM · target_account=true · narrative refresh · tier frozen at T1
- Sabafon (319135988461): MEDIUM · target_account=true · narrative refresh · tier frozen at T3
- Hormuud Telecom (319135976149): MEDIUM · target_account=true · narrative refresh · tier frozen at T2
- FiberHome Philippines (319137756890): FULL · target_account=true · Network Op T1 → Other (vendor disqualifier) · tier frozen
- Epic Malta (319135989484): MEDIUM · target_account=true · narrative refresh · tier frozen at T3
- Digicel Cayman (319135980245): MEDIUM · target_account=true · narrative refresh · tier frozen at T3
- Digicel Haiti (319135980248): MEDIUM · target_account=true · narrative refresh · tier frozen at T3
- Forthnet/Nova (319135968984): MEDIUM · target_account=true · narrative refresh · tier frozen at T2 · R3 dedup w/ Nova
- MyRepublic Indonesia (319135958773): MEDIUM · target_account=true · confidence high_90 → medium_7089 · tier frozen at T2

### Records 21-30 (mixed batch — colo flips, reclassifications)
- Matrix (277218831084): FULL · MSP → Data Center Colo Provider · T2→T2 · sub-segment cleared (R-Tier-Audit to classify) · R3 flag w/ SBA Edge
- Navarino (277405038289): FULL · MSP → Other · T2→T5 · specialty maritime SATCOM
- Cloud4C (277439114945): MEDIUM · MSP/Aggregator unchanged · T2→T2 · Apollo revenue bleed noted
- LUS Fiber (297863568115): MEDIUM · Fiber Op unchanged · T4→T4 · provisioning_landscape trimmed + recent_news fixed
- Dimension Data (277233232582): MEDIUM · MSP/Aggregator unchanged · T2→T2 · filled missing fields
- Telarus (318219105016): FULL · MSP Master Agent unchanged · T3→T3 · filled 7 fields
- TCG-Partners (318106542783): MEDIUM · MSP Master Agent unchanged · T3→T3 · confidence high_90 → low_5069 per Cooper anchor-thin policy
- Skymeric Technologies (300373178085): FULL · MSP → Flagged for deletion · pivoted out of telecom
- Telesystem (193866158811): MEDIUM · MSP unchanged · T2→T2 · filled missing fields
- PalTel Wholesale (319145757370): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T2

### Records 31-40 (target_account=true Phase-3-prep continued + colo flip)
- KN Network (319132457672): MEDIUM · target_account=true · Network Op T1 unchanged · confidence high_90 → low_5069 · D7 escalation
- Corsica Telecom (319132445424): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T2
- Metronet Bangladesh (319124988609): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T2
- Megacable (318315145955): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T2
- Medallion Communications (319125020404): FULL · target_account=true · Network Op T1 → Data Center Colo Provider · tier frozen · R3 flag w/ Digital Realty
- Paratus Mozambique (319125009129): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T2
- Open Telecom (319125018323): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- Hainet (319125017303): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- Mobicom Networks (318290984657): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- TCSL (319125018331): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3

### Records 41-50 (target_account=true continued + reclassifications)
- IBW Nicaragua (319137792698): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- Epic Cyprus (319139527414): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3 · domain corrected epicnet.cy → epic.com.cy
- NetOne Zimbabwe (319141362418): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- Digicel Guadeloupe (319141359309): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- Yemen Net (319139527373): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- RedTrain (319141321440): FULL · target_account=true · Network Op T1 → Fiber Operator + Regional CLEC · tier frozen · country India → Australia · confidence high_90 → medium_7089
- ARSAT Argentina (319141272313): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T1
- Aliv (319141359308): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3
- Internet Thailand (319141316329): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T2
- FLOW Jamaica (319134261951): MEDIUM · target_account=true · Network Op T1 unchanged · tier frozen at T3

## Drain status

- Pool at batch 15 end: ~2,015
- Pool at batch 16 end: ~1,954
- Processed this batch: 50
- Sweep cumulative processed: ~782 records
- Sweep cumulative drain: ~28.6% of starting pool
- ETA: ~39 more batches at BATCH_SIZE=50

## Run health: GREEN

No errors. All writes succeeded.
