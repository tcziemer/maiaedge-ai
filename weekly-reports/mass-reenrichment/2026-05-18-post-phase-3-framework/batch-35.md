# Mass Re-Enrichment Sweep — Batch 35

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Batch:** 35
- **Date:** 2026-05-19
- **Operator:** Cowork CRM Guardian (Cooper Kennedy)
- **Records processed:** 50 / 50
- **Trigger query:** `customer_segment IN [6 ICPs] AND last_enriched_date < 2026-05-18 OR NULL`, exclude MaiaEdge own record (124293230301), sort `hs_object_id ASC`, limit 50
- **Pool:** total = 965; this batch pulled offset 0 of the new sort
- **Path mix:** LIGHT 29 · MEDIUM 11 · FULL 8 · HOLD 2
- **Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT="disabled")
- **Sweep cumulative Apollo:** 0

---

## Per-record audit

### FULL — eviction / reclassification (8 records)

#### PAETEC Holding Corp. (193027625717)
- Path: FULL (eviction)
- Domain: paetec.com (unchanged)
- Segment: Fiber Operator -> Flagged for deletion
- Sub-segment: Tier 2 National Wholesale - Fiber operator -> cleared
- Confidence: high_90 -> high_90
- Tier: tier_2 -> unchanged (non-ICP, skip per Step A0)
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass (definitive eviction)
- Reason: DEFUNCT — acquired by Windstream 2011, Uniti 2025. R3 to merge into Windstream Wholesale (133493528256).

#### Lightower Fiber Networks (193854634742)
- Path: FULL (eviction)
- Domain: lightower.com (unchanged)
- Segment: Fiber Operator -> Flagged for deletion
- Sub-segment: Regional CLEC - Fiber operator -> cleared
- Confidence: medium_7089 -> high_90
- Tier: tier_3 -> unchanged
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass (definitive eviction)
- Reason: DEFUNCT — Crown Castle acquired 2017, divested fiber to Zayo Oct 2025 in pure-play tower pivot. R3 to merge contacts into Zayo primary.

#### Console Connect (193863998193)
- Path: FULL (segment change to Other)
- Domain: consoleconnect.com (unchanged)
- Segment: MSP/Aggregator -> Other
- Sub-segment: Telecom Aggregator - MSP -> cleared
- Confidence: high_90 -> high_90
- Tier: tier_2 -> tier_5
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: DIRECT NaaS COMPETITOR — PCCW Global software-defined interconnect platform, Private Label SaaS at ITW 2025. Per Operating Principle: "Other reserved for D1 disqualifier matches useful as competitive/partner references." Federation/peering target only, no direct sales motion.

#### BCE (192899501767)
- Path: FULL (segment reclassify)
- Domain: bce.ca (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Canadian #1 incumbent (TSX:BCE), Bell Canada parent, $24.3B rev / 40K emp, Aug 2025 Ziply Fiber acquisition. National operator under-tiering correction.

#### teco (Telecom Argentina) (192951753403)
- Path: FULL (segment reclassify)
- Domain: teco.com.ar (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Argentine #1 incumbent (BCBA:TECO2), Movistar/Personal/Fibertel brands, Feb 2025 $1.245B Telefonica Moviles Argentina acquisition. National operator under-tiering correction.

#### PCCW (193100077817)
- Path: FULL (segment reclassify)
- Domain: pccw.com (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Hong Kong #1 incumbent (HKEX:0008), $42B rev, 20.6K emp, Route Miles Enterprise (50K+). National operator under-tiering correction. PCCW owns Console Connect (now flagged Other in this batch).

#### Inteliquent (193100077816)
- Path: FULL (segment reclassify)
- Domain: inteliquent.com (unchanged)
- Segment: Fiber Operator -> MSP/Aggregator
- Sub-segment: Regional CLEC - Fiber operator -> Telecom Aggregator - MSP
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_2
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Largest US wholesale voice/messaging (Sinch-owned 2021), $249M rev, ~300B minutes annually. CPaaS aggregator, not data fiber. Continuing CPaaS misclassification pattern.

#### Bandwidth (193805229766)
- Path: FULL (segment reclassify)
- Domain: bandwidth.com (unchanged)
- Segment: Fiber Operator -> MSP/Aggregator
- Sub-segment: Regional CLEC - Fiber operator -> Telecom Aggregator - MSP
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_2
- Customer protection: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: NASDAQ:BAND, $748M rev CPaaS / SIP trunking / programmable voice. National voice CLEC but core business is voice/messaging APIs. Continuing CPaaS misclassification pattern.

---

### MEDIUM — sub/tier/conf/domain/fill (11 records)

#### Gila River Telecommunications (192886920922)
- Path: MEDIUM (within-fiber demotion)
- Sub-segment: Long Haul / Backbone -> Municipal / Cooperative - Fiber operator
- Confidence: high_90 -> high_90
- Tier: tier_2 -> tier_4
- Reason: Tribal-owned regional telecom, 65 emp, infra_profile says Route Miles Small (<1K) + POPs Small (<10) — not Long Haul scale. Within-fiber demotion pattern.

#### Transtelco (193034821368)
- Path: MEDIUM (within-fiber upgrade)
- Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: US-Mexico cross-border, 28K+ km, 15 Americas countries, Facilities Large + Route Miles Large + POPs Enterprise. National-operator under-tiering.

#### etisalateurope (193058608885)
- Path: MEDIUM (within-fiber upgrade)
- Sub-segment: Regional CLEC -> Tier 2 National Wholesale - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: e& European wholesale arm (Etisalat UAE), POPs Enterprise (100+), 4 European hubs + North/Latin America entry.

#### Alaska Communications Systems Group (193100077770)
- Path: MEDIUM (within-fiber upgrade)
- Sub-segment: Regional CLEC -> Tier 2 National Wholesale - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: Alaska state-anchor with subsea systems (Alaska United, Northstar, AKORN), 600 emp, $286M rev. 2026-05-13 brief flagged the reclassify intent. Stays on Fiber Op parent rather than Network Op (T1/VNO) per pure-play state-incumbent positioning.

#### GlobalConnect (193857515198)
- Path: MEDIUM (within-fiber upgrade)
- Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: Nordic + DACH fiber, EQT-owned, $1.9B rev, 2.5K emp, Route Miles Enterprise (50K+).

#### euNetworks (193863998169)
- Path: MEDIUM (within-fiber upgrade)
- Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: Pan-European fiber (Stonepeak-owned), 17 countries, 18 cities, 50+ DCs, Route Miles Large.

#### Videotron - Fibrenoire (193865438915)
- Path: MEDIUM (tier bump only)
- Sub-segment: Regional Cable Operator - Fiber operator (unchanged)
- Tier: tier_3 -> tier_2
- Reason: Quebecor subsidiary, $3.6B rev, 6.5K emp, Quebec+Ontario footprint with Route Miles Large.

#### Bluebird Fiber (193832997595)
- Path: MEDIUM (domain typo correction)
- Domain: bluebridfiber.com -> bluebirdfiber.com
- Confidence + tier unchanged this pass; domain correction logged.
- Reason: Verified via web search — official site is bluebirdfiber.com. Domain Identity Sanity Check finding.

#### NUWAVE Communications (193865437932)
- Path: MEDIUM (confidence bump)
- Confidence: medium_7089 -> high_90
- Reason: Rich Apollo data + detailed R2 brief (45 US states / 58 countries, Las Vegas HQ, iPILOT SaaS, Microsoft Operator Connect partner) supports high_90.

#### 123Net (193865438935)
- Path: MEDIUM (field fill)
- Field filled: provisioning_landscape ("Research needed." -> proper 2-4 sentence narrative)
- Reason: Template-bleed remediation. Other 6 fields already framework-consistent.

#### DataBank (193865438937)
- Path: MEDIUM (confidence bump)
- Confidence: manual_review_required -> high_90
- Reason: Rich brief (SoftBank/DigitalBridge Dec 2025 acquisition, $2B financing for 8-DC Red Oak TX campus, NVIDIA DGX-Ready, 65+ HPC-ready DCs). Clear AI Signals - colo + T1 fit. No 2+ sub-segment ambiguity remaining.

---

### LIGHT — date bump + stale news clear (29 records)

| ID | Name | Recent_news action |
|---|---|---|
| 192899501809 | Gateway Fiber | keep (2026-05-11 Fiber Connect) |
| 192921136828 | DE-CIX | keep (2026-05-11 Fiber Connect) - see Patterns: IX classification policy needed |
| 192932279006 | Axiom | clear (2025-07-11 stale) |
| 193033023169 | eX2 Technology | keep (2026-04-28 dark fiber IRU) - dupe-pair watch with 175109006031 |
| 193033023199 | Mass IX | clear (2025-09-17 stale) - see IX policy below |
| 193034821365 | Thrive | clear (2025-11-11 stale) |
| 193058608886 | Neutrality | clear (2025-02-10 stale) |
| 193094707951 | DF&I | clear (no date) |
| 193168217847 | Lightspeed Networks | keep (2026-05-11 Fiber Connect) |
| 193853195964 | Network Data Systems | clear (2025-04-22 stale) |
| 193853195965 | iTel Networks | clear (2024-02-06 stale) |
| 193853914869 | SolEx | clear (no date) |
| 193853915852 | NTT Global Networks | clear (2025-12-19 stale) - see NTT consolidation note |
| 193853915853 | Truestream | clear (2025-11-05 stale) |
| 193853915854 | Resolute CS | clear (2025-10-15 stale) |
| 193854634744 | 382com | empty - no action on field |
| 193855354612 | Aureon | clear (2025-09 stale) |
| 193856074469 | Hosted Backbone | clear (2024-11-30 stale) |
| 193856794352 | TouchTone Communications | clear (2025-06 stale) |
| 193856794355 | Alabama Fiber Network | clear (no date) |
| 193856795322 | Digital Realty | keep (2026-05-04 ATM offering 8-K) |
| 193863998190 | NJFX | clear (no date; AI Infrastructure note plain) |
| 193863998192 | Ezee Fiber | clear (no date) |
| 193863998196 | DartPoints | clear (2025-04-30 stale) |
| 193863998197 | CoreSite | clear (2025-04-08 stale) |
| 193863999165 | Lunavi | clear (2025-07-07 stale) |
| 193865438911 | SECOM | keep (2026-05-11 Fiber Connect) |
| 193865438926 | eStruxture Data Centers | clear (2025-07-30 stale) |
| 193865438941 | GDS | clear (2025-03-10 stale) |

All LIGHT records: tier recompute is no-op (signal fields empty, no modifier shifts). Only `last_enriched_date` written (+ recent_news clear where applicable).

---

### HOLD — no writes, no date bump (2 records)

#### General Motors (192916123348)
- Path: HOLD (continued)
- Reason: Manufacturing vertical is on Enterprise Watch List per 2026-05-11 ICP scope, NOT one of the 4 qualifying Enterprise sub-segments (Financial Services, Healthcare Systems, Retail and Distribution, Outsourcing Services). Original R1 2026-05-13 hold preserved. Awaiting Cooper framework decision (promote Mfg to ICP, or demote GM to Other/Flagged).
- Canvas action: was already on canvas pre-batch; carried forward.

#### Phibee Telecom (193062202073)
- Path: HOLD (new this batch)
- Reason: 6/7 enriched fields empty (geographic_focus, infrastructure_profile, hyperscaler_proximity, fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event all blank) + segmentation_confidence blank. Per §7.4 4+ missing fields = FULL path requirement; without web research budget this batch, defer to D7 / next R2 FULL pass for completeness gate. Confidence field also blank — needs reclassification verification.
- Canvas action: NEW Tier 3 hold.

---

## Tier writes summary

- **Promotions (toward T1):** 8
  - BCE (T3 -> T1), teco (T3 -> T1), PCCW (T3 -> T1) — Tier 1 Carrier reclassifications
  - Transtelco (T3 -> T2), etisalateurope (T3 -> T2), Alaska Communications (T3 -> T2), GlobalConnect (T3 -> T2), euNetworks (T3 -> T2), Videotron-Fibrenoire (T3 -> T2) — sub-segment + tier corrections
  - Inteliquent (T3 -> T2), Bandwidth (T3 -> T2) — segment changes to MSP/Aggregator
- **Demotions (toward T5):** 2
  - Gila River (T2 -> T4) - within-fiber demotion to Municipal/Cooperative
  - Console Connect (T2 -> T5) - reclassified Other (NaaS competitor)
- **Skipped (hs_is_target_account = true):** 0
- **Skipped (non-ICP post-classification):** 2 (PAETEC, Lightower — Flagged for deletion)

## Sub-segment changes (cascade fired): 2

- Inteliquent: Fiber Operator -> MSP/Aggregator (contact cascade may apply)
- Bandwidth: Fiber Operator -> MSP/Aggregator (contact cascade may apply)
- BCE / teco / PCCW: Fiber Operator -> Network Operator(Tier 1 / VNO) (contact cascade may apply)
- Console Connect: MSP/Aggregator -> Other (cascade applies)
- PAETEC / Lightower: Fiber Operator -> Flagged for deletion (R4 handles contact reassociation)

## Sub-segment auto-migrations: 0
No legacy values detected (Tier 1 Global Incumbent / AI - Colocation Operator / Managed Network Services - Network Operator).

## Greenfield migrations: 0

## Customer-protection HOLDs: 0
No closed-won customers proposed for ICP -> non-ICP downgrade.

## Completeness Gate fails: 1
- Phibee Telecom — 6/7 narrative fields empty. HELD, NO date bump. Re-appears in pool.

## Manual-review HOLDs: 1
- General Motors — Manufacturing vertical not in active Enterprise sub-segments. Cooper framework decision required.

---

## Patterns observed this batch

### CONTINUING — National operator under-tiering (cumulative ~39, +3 reclassify Tier 1 + 6 Tier 2 corrections this batch)
- BCE (Canadian #1 incumbent, $24B rev) — Regional CLEC T3 -> Tier 1 Carrier T1
- teco / Telecom Argentina (Argentine #1 incumbent) — Regional CLEC T3 -> Tier 1 Carrier T1
- PCCW (Hong Kong #1 incumbent, $42B rev) — Regional CLEC T3 -> Tier 1 Carrier T1
- Transtelco (28K+ km US-Mexico, 15 Americas) — T3 -> Long Haul T2
- etisalateurope (e& European wholesale) — T3 -> Tier 2 Wholesale T2
- Alaska Communications (state-incumbent + subsea trio) — T3 -> Tier 2 Wholesale T2
- GlobalConnect (Nordic + DACH 50K+ km) — T3 -> Long Haul T2
- euNetworks (Pan-European 17 countries) — T3 -> Long Haul T2
- Videotron-Fibrenoire (Quebecor sub $3.6B) — T3 -> T2 (sub unchanged)

### CONTINUING — Within-fiber demotion (cumulative ~22, +1 this batch)
- Gila River Telecommunications — Long Haul/Backbone misclassified, actually tribal regional with infra Small (<1K route miles, <10 POPs). Demoted to Municipal/Cooperative T4.

### CONTINUING — Voice/CPaaS misclassified as Fiber Operator (cumulative ~3-4, +2 this batch)
- Inteliquent (Sinch wholesale voice) — Fiber Op CLEC -> MSP/Aggregator Telecom Aggregator T2
- Bandwidth (CPaaS / SIP / 911) — Fiber Op CLEC -> MSP/Aggregator Telecom Aggregator T2
- Note: NUWAVE Communications stays as MSP/Aggregator Telecom Aggregator (already correctly classed; confidence bumped to high_90 this batch).

### CONTINUING — Defunct entity reclassification (cumulative ~4, +2 this batch)
- PAETEC Holding Corp. — Windstream/Uniti merger lineage, R3 to merge
- Lightower Fiber Networks — Crown Castle/Zayo divestiture Oct 2025, R3 to merge into Zayo

### CONTINUING — NaaS competitor reclassification (cumulative 1-2, +1 this batch)
- Console Connect — PCCW Global software-defined interconnect platform, direct NaaS competitor. Moved to Other tier_5. Federation/peering motion only.

### CONTINUING — Domain typo correction (cumulative 2, +1 this batch)
- Bluebird Fiber: `bluebridfiber.com` -> `bluebirdfiber.com`. Verified via web search.
- Identity Sanity Check value reaffirmed.

### CONTINUING — Manual-review backlog (cumulative ~5)
- General Motors — Mfg vertical Watch List; framework decision pending.

### NEW — Completeness Gate failure (cumulative 1, +1 this batch)
- Phibee Telecom — small (~1 employee) French aggregator; 6/7 narrative fields empty + confidence blank. Likely thin web research data. Defer to D7 / next R2 with full enrichment budget.

### NEW — IX/Internet Exchange classification policy gap (cumulative 2 surfacing, 0 resolved)
- DE-CIX (largest IX globally, 35+ cities, POPs Enterprise 100+) — currently Fiber Op + Regional CLEC + T3. Not a fiber operator nor a CLEC. No canonical IX sub-segment in the 30 active.
- Mass IX (Boston/New England IX) — same misclassification pattern.
- Recommendation: Cooper to decide whether to add a 31st sub-segment "Internet Exchange Operator" under MSP/Aggregator OR Network Operator parent, OR formally map IXs to existing "Telecom Aggregator - MSP" via a Phase 3.1 doctrine update. Both DE-CIX + Mass IX held this batch with LIGHT date bump pending decision.

### CONTINUING — Apollo industry-field data quality (cumulative ~6, +1 this batch)
- BCE Apollo industry field returns "INVESTMENT_MANAGEMENT" — incorrect for the Canadian #1 telco. Apollo data quality flag.

### CONTINUING — Subsea operator watch list (cumulative 0 promoted, watch continued)
- Alaska Communications — owns Alaska United, Northstar, AKORN subsea systems but also has significant terrestrial scope; classed Tier 2 National Wholesale (Fiber Op parent) rather than Subsea cable operator (Network Op parent) since not pure-play subsea. Distinct decision from prior Ocean Networks (batch 34) which also stayed terrestrial.
- NJFX (carrier-neutral cable landing station + 35-tenant ecosystem) — stays Data Center Colo Provider Standard - colo. Carrier-neutral colo housing subsea landings; not itself a subsea operator.

### CONTINUING — NTT entity tree (cumulative 4-5)
- NTT Global Networks (Colorado) — NTT Communications US business arm. Stays MSP/Aggregator Cloud + Telecom Hybrid MSP T2. Per batch 33-34 context: NTT Communications was rebranded to NTT DOCOMO BUSINESS 2025. Possible duplicate record consolidation needed across NTT records. Carry forward for Tim Z review.

### CONTINUING — Greenfield colo: 0 hits this batch.

---

## Data-quality follow-ups added

1. **Apollo industry field "INVESTMENT_MANAGEMENT" on BCE** — clearly wrong. Apollo refresh needed.
2. **NTT Global Networks consolidation** — possible duplicate against NTT Communications + NTT DOCOMO BUSINESS records. R3 candidate; Tim Z review.
3. **IX/Internet Exchange canonical sub-segment** — DE-CIX + Mass IX both currently misclassified as Regional CLEC. Cooper framework decision needed: add 31st sub-segment OR formally map to existing value.
4. **Phibee Telecom field gap** — 6/7 narrative fields empty + confidence blank, defer to next R2 FULL pass with web research budget.
5. **eX2 Technology dupe pattern** — `ex2technology.com` (this batch 193033023169) vs `eX2 Technology, a Vivacity Company` (batch 34 175109006031). R3 candidate.
6. **MaiaEdge property enum spacing rule discovered** — `Network Operator(Tier 1 / VNO)` and `Municipal / Cooperative - Fiber operator` both REQUIRE surrounding spaces around the `/`. Saved to memory as `hubspot_enum_spacing.md`. Three retries this batch before write succeeded; future routines should copy enum values verbatim.

---

## Apollo budget
- This batch: 0 credits
- Sweep cumulative: 0 (APOLLO_ENFORCEMENT="disabled", Apollo-free path dominant)

## Errors
- 4 initial enum-value rejections (3 national operator reclassifications + 1 Gila River sub-segment) — caused by missing spaces around `/` in canonical enum strings. All 4 retried successfully with corrected values.
- Net: 48/48 intended writes succeeded.

## Run health: GREEN

---

## Drain status

- Done in this sweep: ~1,748 / 2,795 expected pool (63%)
- Pool remaining at trigger query: 965 (down from ~1,096 batch 34, ~131 records drained since)
- Remaining after this batch: ~915 (48 written records exit pool; 2 HOLDs remain)
- ETA: ~19 more batches at BATCH_SIZE=50
