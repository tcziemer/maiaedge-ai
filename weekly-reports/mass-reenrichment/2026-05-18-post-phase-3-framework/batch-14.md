# Batch 14 - Mass Re-Enrichment Sweep 2026-05-18-post-phase-3-framework

**Date:** 2026-05-18
**Records processed:** 50 / 50
**Path mix:** LIGHT 0 · MEDIUM 33 · FULL 17 · HOLD 0
**Apollo this batch:** 0 credits
**Pool remaining after batch:** ~2,064
**Sweep cumulative drain:** ~671 / ~2,735 (~25%)
**ETA:** ~41 more batches at BATCH_SIZE=50

---

## Sub-batch A (records 1-10) - 10 hs_is_target_account international carriers

All 10 records: hs_is_target_account=true (SKIP tier write, other writes proceed). Phase 3 prep records with templated "[Country] [Company]" prefix bleed in briefs. Cleaned.

- Ooredoo Palestine (319134200515) - MEDIUM, brief templating fix
- Cellcard (319154830027) - MEDIUM
- Digitel Venezuela Wholesale (319139526392) - MEDIUM
- Mobilis Algeria (319124968149) - MEDIUM ($1.05B revenue, ARPT regulated)
- Superloop (319126735549) - MEDIUM, ASX-listed Australian wholesale fiber; removed "Clean extend-reach fit for APAC expansion" rep-facing marketing
- Raxio Data Centre Group (319173030622) - MEDIUM, Pan-African colo (6 countries)
- Maroc Telecom Wholesale (319132384982) - MEDIUM, added Etisalat (e&) parent context
- Kolbi Empresarial ICE (319126760122) - MEDIUM, Costa Rican ICE subsidiary
- DTAC Thailand (319134173939) - MEDIUM
- Vodafone Qatar Wholesale (319126772465) - MEDIUM

## Sub-batch B (records 11-20)

### Sky UK (318339892957)
- Path: MEDIUM
- Confidence: medium_7089 -> low_5069
- Reason: Major UK media + broadband (Comcast subsidiary). Primarily B2C/media; Sky Connect B2B motion secondary. Borderline ICP - keeping Regional CLEC at low_5069 pending D7 validation.

### Rakuten Mobile (318363311861)
- Path: FULL
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC -> **Tier 1 Carrier - Network Op**
- Tier: tier_3 -> tier_2
- Reason: Japanese MNO with cloud-native virtualized RAN. Rakuten Symphony OpenRAN business. Not a fiber operator.

### Union Wireless (297858169566)
- Path: MEDIUM
- Reason: Overlong brief (3 paragraphs) tightened to 4 sentences. provisioning_landscape marketing bleed stripped. Stale 2024-07 GOCare news cleared.

### DIDWW (316627226305)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC -> **Telecom Aggregator - MSP**
- Reason: Ireland-based global DID + SIP trunking wholesale aggregator. VoIP wholesaler, not fiber operator.

### Kyivstar JSC (318400654069)
- Path: FULL
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC -> **Tier 1 Carrier - Network Op**
- Tier: tier_3 -> tier_2
- Reason: Ukraine's largest mobile operator (VEON subsidiary), $836M revenue. Multi-service Tier 1 carrier.

### ITC Telecom (297975387884)
- Path: MEDIUM
- Reason: Small NJ telecom with thin profile; provisioning_landscape marketing bleed stripped; geographic_focus reformatted.

### Lynxx Networks (297975387880)
- Path: MEDIUM
- Infrastructure_profile: Route Miles: Enterprise (50K+) -> **Route Miles: Mid-Size (1K-10K)** (downgrade - 50K+ implausible for WI regional ISP)
- Reason: Wisconsin regional fiber/wireless (founded 1907). Overlong brief tightened. provisioning_landscape had explicit "MaiaEdge can bridge this gap..." marketing bleed - stripped. Stale 2022/2024 news cleared.

### TNZI (316519552744)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC -> **Telecom Aggregator - MSP**
- Reason: International voice/SIP wholesale aggregator (originally Telecom New Zealand International). A-Z termination global voice service.

### Manor (316508757740)
- Path: FULL
- Segment: Fiber Operator -> **Flagged for deletion**
- Confidence: medium_7089 -> high_90
- Reason: None Identified infrastructure profile, no brief, manor.net thin domain. No positive evidence for any ICP sub-segment.

### Symbio Networks (316502492875)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC -> **Telecom Aggregator - MSP**
- Reason: Australian VoIP/SIP wholesale carrier (Symbio Holdings group). Voice services pattern.

## Sub-batch C (records 21-30)

### Globe Teleservices Pte (316621828832)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC -> **Telecom Aggregator - MSP**
- Reason: Singapore-headquartered CPaaS / international voice and messaging wholesale aggregator.

### ADG LDI (318220838608)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC -> **Telecom Aggregator - MSP**
- Reason: Pakistan Long Distance International (LDI) licensed voice carrier. International voice termination wholesale.

### CIMA Telecom (316598423244)
- Path: MEDIUM
- Confidence: medium_7089 -> low_5069
- Reason: Florida-based Caribbean/LATAM telecom services provider with thin public profile. Anchor-level validation pending.

### IP Transfer (316538883827)
- Path: FULL
- Segment: Fiber Operator -> **Flagged for deletion**
- Confidence: medium_7089 -> high_90
- Reason: Pennsylvania VoIP/SIP entity with None Identified infrastructure profile. No positive operational evidence.

### Telegeeks (316625421017)
- Path: FULL
- Segment: Fiber Operator -> **Flagged for deletion**
- Confidence: medium_7089 -> high_90
- Reason: Florida small IT/telecom services entity with None Identified infrastructure profile. No positive operational evidence.

### Telekom Sudan (318231615184)
- Path: FULL
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC -> **Tier 1 Carrier - Network Op**
- Tier: tier_3 -> tier_2
- Reason: Sudan's state-owned national incumbent (Sudatel). Tier 2 national carrier.

### Telecom Argentina (318330813142)
- Path: FULL
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC -> **Tier 1 Carrier - Network Op**
- Tier: tier_3 -> tier_2
- Reason: Argentina's largest integrated telco (Personal mobile, Cablevision cable, Fibertel broadband).

### Wind Telecom (318327651046)
- Path: MEDIUM
- Reason: Stub brief added. **Likely duplicate of record 251659209447 (wind.com.do, "Indigo Telecom") processed in batch 13.** Both records refer to same DR Wind Telecom entity. Flagged in brief for R3 dedup review.

### golis.so (319231102702)
- Path: MEDIUM
- Reason: Somalia-based Golis Telecom regional ISP. Stub brief added.

### Call48 (318229351143)
- Path: FULL
- Segment: Fiber Operator -> **Flagged for deletion**
- Confidence: medium_7089 -> high_90
- Reason: Small Florida VoIP/calling-card services reseller. No owned fiber infrastructure.

## Sub-batch D (records 31-40) - 10 hs_is_target_account international carriers

All 10 records: hs_is_target_account=true (SKIP tier write). Templating cleanup.

- CAT Telecom / National Telecom Thailand (319132383992)
- Batelco Wholesale Bahrain (319137743587)
- Zain Kuwait Wholesale (319139476168)
- Telecentro Argentina (319135941318)
- Tigo Business Guatemala Wholesale (319132402385)
- Unitel Laos (319134176980)
- Tunisie Telecom Wholesale (319139476167)
- Orange Tunisia Wholesale (319132411583)
- Orange Morocco Wholesale (319126771393)
- Orange Egypt Wholesale (319134176979) - Tier 1 subsea landing hub (TES + multiple cables)

## Sub-batch E (records 41-50) - 10 more hs_is_target_account international carriers

All 10 records: hs_is_target_account=true (SKIP tier write). Templating cleanup. Apollo parent-revenue bleed observed but skipped (Orange Group $46B, Ooredoo Group $8.8B, Entel parent $18B - none reflect subsidiary scale).

- Orange Jordan Wholesale (319154804470) - Apollo $46.6B revenue is Orange Group bleed (skipped)
- Ooredoo Kuwait Wholesale (319147504320) - Apollo $8.8B = Ooredoo Group bleed
- Entel Bolivia Wholesale (319147494134) - Apollo $18.6B = parent bleed (Entel Bolivia ~$500M)
- Mobily / Etihad Etisalat Saudi (318363334336) - $4.7B Saudi MNO
- Ooredoo Myanmar (319151104734) - Apollo $8.8B Group bleed
- OTE Wholesale Greece (319139445458) - $4.1B legit Greek incumbent
- BTC Bahamas (320876610272) - $1.75B
- CAMTEL Cameroon (318372093636) - $54M state incumbent
- Kalaam Telecom Bahrain (319125023431)
- OPT French Polynesia (319126734579) - Tier 1 subsea hub (Natitua, Honotua, Manatua consortium)

---

## Patterns observed this batch

- **30/50 records were hs_is_target_account=true international carriers** (Phase 3 prep batches from 2026-04-15 / 2026-04-21). All clean classifications already; primary work was brief templating cleanup ("[Country] [Company]" prefix duplicate) and providing stub briefs for empty ones.
- **VoIP/SIP-only -> MSP/Aggregator pattern accelerating.** 5 records this batch flipped from Fiber Operator/Regional CLEC to MSP/Aggregator/Telecom Aggregator - MSP (DIDWW, TNZI, Symbio Networks, Globe Teleservices, ADG LDI). Pattern: any international voice/SIP wholesaler without owned fiber backbone is being reclassified as Telecom Aggregator - MSP.
- **Fiber Operator -> Network Operator promotions for national incumbents.** 4 records this batch (Rakuten Mobile, Kyivstar, Telekom Sudan, Telecom Argentina). Pattern: national MNO/integrated telcos miscategorized as "Regional CLEC - Fiber operator" during Phase 3 prep; correct route is Network Operator(Tier 1 / VNO) + Tier 1 Carrier - Network Op.
- **4 Flags for deletion this batch** (Manor, IP Transfer, Telegeeks, Call48). Pattern: "None Identified" infrastructure_profile + thin/no brief + small/local scope + no positive ICP sub-segment evidence = aggressive Flag per Operating Principle #7.
- **Apollo parent-revenue bleed prevalent on international subsidiaries.** 4 records this batch (Orange Jordan $46B, Ooredoo Kuwait $8.8B, Entel Bolivia $18B, Ooredoo Myanmar $8.8B) all show group-parent revenue rather than subsidiary scale. Skipped revenue writes; flagging as data quality follow-up.
- **Marketing bleed cleanup continues**: Union Wireless and Lynxx Networks both had explicit "MaiaEdge can bridge..." or rep-facing fit-language in provisioning_landscape. Stripped on both.
- **Possible R3 duplicate detected**: Wind Telecom (318327651046, windtelecom.com.do) vs Indigo Telecom (251659209447, wind.com.do, processed batch 13). Same DR entity under two domain variants. R3 should consolidate.
- **Infrastructure_profile overstatement caught**: Lynxx Networks claimed Route Miles: Enterprise (50K+) but is a Wisconsin I-90-corridor regional ISP - downgraded to Mid-Size (1K-10K). Watch for similar overstatement on small regional records.
- **D7 escalation queue: 0 new records flagged** (HOLD policy = NONE; Wind Telecom dedup is R3 territory, not D7).

## Apollo budget tracker

- This batch: 0 credits
- APOLLO_ENFORCEMENT = "disabled" - sweep is outside weekly cap.

## Errors / failures

None. All 50 writes succeeded.
