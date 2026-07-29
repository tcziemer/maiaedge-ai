# Mass Re-Enrichment Sweep - Batch 40

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Batch:** 40
- **Date:** 2026-05-19
- **VERIFY_DEPTH:** leverage-and-patch
- **APOLLO_ENFORCEMENT:** disabled
- **SEGMENT_SCOPE:** all_active_icp
- **Processed:** 50/50
- **HOLDs:** 0 (per Cooper directive - resolve in-line)
- **Apollo this batch:** 0 credits
- **Trigger pool at batch start:** 859 records
- **Drain after batch 40:** ~809 remaining

## Path mix
- LIGHT: 26
- MEDIUM: 16
- FULL: 8 (4 evictions, 4 segment-changing reclassifications)
- HOLD: 0

## Notable framework moves
- 8 prior-batch HOLDs resolved without re-holding (OADC, China Telecm Americas typo, Pacific Dataport, PLDTUS LTD, Vodafone Kiribati, AVAIO, NORDUnet, TEECOM)
- 4 evictions (Flagged for deletion): China Telecm Americas typo (dedup), Vodafone Kiribati (irreconcilable identity), TEECOM (non-ICP), NSW/Prysmian (cable manufacturer D1)
- 2 sanctions Other-reclasses: China Telecom Americas canonical (T5), China Telecom parent (T5) - FCC US-services ban + OFAC
- 3 AI Signals - colo promotions: Crane Data Centers, Racks Central, AVAIO (confirmed)
- 1 NeoCloud Crypto to AI reclass: Ionic Digital (former BTC miner pivot per Phase 3 principle 9)
- 1 Hyperscale Wholesale promotion: STT Telemedia GDC
- 3 tier downgrades to T4: Egi Hosting, Binary Net, Dacentec (post-acquisition consolidation small-footprint correction)

## Per-record entries

### OADC (251593480894)
- Path: MEDIUM
- Domain: adc.am (unchanged - confirmed Armenian DC, not African OADC)
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo (unchanged)
- Confidence: high_90 -> low_5069
- Tier: tier_3 -> tier_4
- Apollo: no
- web_searches: 0 (resolved via existing brief contradiction)
- Reason: Identity reconciled to ADC Armenia (matches domain + state/country). Cleared OADC-Africa contamination from news/geographic_focus.

### China Telecm Americas typo (251593594605)
- Path: FULL (eviction)
- Segment: Fiber Operator -> Flagged for deletion
- Reason: Duplicate of canonical China Telecom Americas (253166672620). Typo + wrong domain (sbtelecom.net).

### Pacific Dataport Inc. (251593619130)
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Confidence: medium_7089 (unchanged)
- Tier: tier_3 (unchanged)
- Reason: Hybrid satellite/fiber Alaska operator. Pure-satellite-operator framework gap noted as data-quality follow-up (not blocking).

### PLDTUS LTD (251593619131)
- Path: FULL (segment change)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 -> medium_7089
- Tier: tier_3 -> tier_2
- Reason: PLDT is Philippine national Tier 1 carrier; record represents US ops arm. R3 dedup will catch canonical PLDT collision.

### Vodafone Kiribati (251651478242)
- Path: FULL (eviction)
- Segment: Fiber Operator -> Flagged for deletion
- Reason: Irreconcilable identity (name Kiribati, domain Malta, state Malta).

### AVAIO (251651866345)
- Path: FULL (domain + segment)
- Domain: navarino.co.uk -> avaiodigital.com
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo -> AI Signals - colo
- Confidence: high_90 (unchanged)
- Tier: tier_3 -> tier_1
- Owner: 159350430 -> 162339176 (Ken West, per CA location)
- Reason: AVAIO Digital - Project Perseus 99MW Pittsburg CA. Domain + classification + owner all corrected.

### NORDUnet (251655462617)
- Path: LIGHT
- Confidence: medium_7089 (unchanged)
- Tier: tier_3 (unchanged)
- Reason: R&E network framework gap data-quality follow-up; classification stable at Fiber Op + Regional CLEC.

### TEECOM (251661009608)
- Path: FULL (eviction)
- Segment: Fiber Operator -> Flagged for deletion
- Reason: Name + domain mismatch with no clean ICP-fit identity (US AV consultancy vs AU reseller).

### Crane Data Centers (253067618006)
- Path: MEDIUM
- Sub-segment: Standard - colo -> AI Signals - colo
- Tier: tier_3 -> tier_1
- Confidence: medium_7089 -> high_90
- Reason: 100MW Forest Grove OR campus groundbreaking 2025-07 with Fortis - hyperscale AI build-to-suit.

### Galaxy Data Centers (253110409915)
- Path: LIGHT
- Tier: tier_3 (unchanged)
- Reason: $460M PE 2025-10 noted; tier stays at floor pending validated signal score.

### China Telecom Americas canonical (253166672620)
- Path: MEDIUM (segment change to Other)
- Segment: Fiber Operator -> Other
- Tier: tier_3 -> tier_5
- Reason: FCC US-services ban; functionally non-ICP for US sales.

### Aligned Data Centers (253675771620)
- Path: LIGHT
- Tier: tier_1 (unchanged - hot Project Caprock signal)
- Reason: Refresh; Project Caprock 540MW + $2.58B financing keep T1 ceiling.

### EdgeUno (253693516506)
- Path: LIGHT
- Tier: tier_1 (unchanged)

### Aspire Communications (254307139259)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### China Telecom parent (254331348698)
- Path: MEDIUM (segment change to Other)
- Segment: Network Operator(Tier 1 / VNO) -> Other
- Tier: tier_1 -> tier_5
- Reason: Same sanctions/OFAC rationale as CTA.

### STT Telemedia GDC (254331348701)
- Path: MEDIUM
- Sub-segment: Standard - colo -> Hyperscale Wholesale - colo
- Tier: tier_3 -> tier_2
- Reason: Parent STT GDC hyperscale + KKR/Singtel $1.3B in India unit.

### CSS Communications (254549120748)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Egi Hosting (254549120749)
- Path: MEDIUM
- Tier: tier_3 -> tier_4
- Reason: Apply brief-recommended downgrade (small regional, ~16 emp).

### FairlawnGig (254558124743)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### East Kentucky Network (254565004004)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Nextera Communications (254572220148)
- Path: MEDIUM (brief patched)
- Tier: tier_3 (unchanged)

### BalsamWest FiberNET (254626062052)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Binary Net (254627886800)
- Path: MEDIUM
- Tier: tier_3 -> tier_4
- Reason: Apply brief-recommended downgrade (10 emp, NE-only).

### Dacentec (254951524029)
- Path: MEDIUM
- Tier: tier_3 -> tier_4
- Reason: Acquired by CentriLogic; small footprint warrants T4.

### Technium (264034971368)
- Path: LIGHT
- Tier: tier_2 (unchanged)

### MCNC (264355635945)
- Path: MEDIUM (brief patched)
- Tier: tier_3 (unchanged)

### Corscale (265895258817)
- Path: MEDIUM (provisioning_landscape filled)
- Tier: tier_1 (unchanged)

### Telstra (265926494953)
- Path: LIGHT
- Tier: tier_1 (unchanged)

### Novva Data Centers (265926495973)
- Path: LIGHT
- Tier: tier_1 (unchanged)

### PenTeleData (265926495977)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### NSW / Prysmian (266871288514)
- Path: FULL (eviction)
- Segment: Fiber Operator -> Flagged for deletion
- Reason: Cable manufacturer (Prysmian Group brand). Phase 3 D1 disqualifier - cable vendors out of scope.

### GreenScale Data Centres (267140078293)
- Path: LIGHT
- Tier: tier_1 (unchanged)

### LevelOneServers (267927865027)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Ellumnet (267927865029)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Silica Broadband (267965349570)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Kentucky Underground Storage (267967366866)
- Path: LIGHT
- Tier: tier_3 -> tier_4 (single underground facility, niche scope)

### Swiftnode (267985661660)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### BGMU Fiber (268010489575)
- Path: MEDIUM (brief patched)
- Tier: tier_3 (unchanged)

### Conext (268012620503)
- Path: LIGHT
- Tier: tier_3 -> tier_4 (Maracaibo-only, small fiber)

### Ionic Digital (268070011606)
- Path: MEDIUM (cross-segment reclass)
- Segment: Data Center Colo Provider -> NeoCloud
- Sub-segment: AI Signals - colo -> Crypto to AI - Neoclouds
- Tier: tier_1 (unchanged)
- Reason: Phase 3 principle 9 - former BTC miner pivoting to AI routes to NeoCloud Crypto-to-AI regardless of operator/landlord model.

### Neptuno Networks (268070128358)
- Path: LIGHT
- Tier: tier_3 (unchanged - large regional, could promote later with signals)

### 4ip Technology (268073704128)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Interconnecx (268111627987)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Qu Data Centres (268111627988)
- Path: LIGHT
- Tier: tier_3 (unchanged - new launch, fresh data)

### YCO Cloud (268111627989)
- Path: LIGHT
- Tier: tier_3 (unchanged - greenfield)

### Wireless Data Net (268197561042)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Peoples Communication (268208386762)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Connect Mobility (268208452328)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Glenwood Telephone Company (268241646272)
- Path: LIGHT
- Tier: tier_3 (unchanged)

### Racks Central (268250706637)
- Path: MEDIUM
- Sub-segment: Standard - colo -> AI Signals - colo
- Tier: tier_3 -> tier_1
- Reason: 3-country AI corridor expansion announced 2026-01.

## Outstanding sweep status
- Trigger pool size at batch 40 start: 859
- Records processed: 50
- Drain after batch 40: ~809 remaining
- ETA at BATCH_SIZE=50: ~17 more batches
- Total Apollo this batch: 0 credits
- HOLDs created this batch: 0
- HOLDs drained this batch: 8 (prior carryovers)
- Outstanding Mass Re-Enrichment Sweep HOLDs in canvas: 0
