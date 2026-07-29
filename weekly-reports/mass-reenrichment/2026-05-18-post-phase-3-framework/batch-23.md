# Mass Re-Enrichment Sweep — Batch 23

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch date:** 2026-05-18
**Records processed:** 50/50
**Path mix:** LIGHT 29 · MEDIUM 13 · FULL 8 · HOLD 0
**Apollo used:** 0 (sweep used existing brief evidence + framework rules; APOLLO_ENFORCEMENT=disabled, no draw)
**Web searches:** 0 (operating within existing brief evidence under leverage-and-patch depth)
**Pool remaining:** ~1,622 after batch (started ~1,672)

---

## Path summary

### LIGHT (29) — date stamp only (tier matches default, framework-consistent)

| ID | Name | Segment | Sub-segment | Tier |
|---|---|---|---|---|
| 240390403774 | Groq | NeoCloud | Tier 1 Inference - Neocloud | tier_2 |
| 277242228439 | KIO Networks | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 276993034939 | Serverfarm | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 277406844633 | Iron Mountain EMEA | Data Center Colo Provider | Standard - colo | tier_3 |
| 277224239832 | Iron Mountain (Global) | Data Center Colo Provider | Standard - colo | tier_3 |
| 296846534378 | OneAsia | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 267127377645 | GreenSquareDC | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 267147429614 | IDC Frontier | Data Center Colo Provider | Standard - colo | tier_3 |
| 297936669370 | EdgeNet | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 297984383722 | Hyperstack (NexGen Cloud) | NeoCloud | Large Scale GPU - Neocloud | tier_1 |
| 300361951944 | Fossefall | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 300361951933 | iXAfrica Data Centres | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 302072845030 | DATA4 | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 302088380131 | Pure DC | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 303410169565 | Orange Business | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 |
| 316287384260 | China Telecom Global | Network Operator(Tier 1 / VNO) | International Backbone Specialist - Network Op | tier_1 |
| 316296474361 | MTN | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 |
| 316298284739 | Liberty Global | Network Operator(Tier 1 / VNO) | Cable MSO Enterprise Division - Network Op | tier_1 |
| 316283788017 | TPG Telecom | Fiber Operator | Tier 2 National Wholesale - Fiber operator | tier_2 |
| 316149788367 | Sunrise GMBH | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 316194606816 | DNA | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 316303584990 | Acestar Telecoms Hong Kong | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 |
| 316303584988 | Hub Advanced Networks | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 316305389269 | Acmetel | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 |
| 316303584991 | OLO Global | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 |
| 316310831810 | ipNX Nigeria | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 316305389272 | Dial Tel | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 |
| 316310831806 | Broadband Systems Corp | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 316310831808 | WorldNet Telecommunications | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |

### MEDIUM (13)

| ID | Name | Action | Notes |
|---|---|---|---|
| 277406846694 | Ficolo | Apollo geo fix | country UK → Finland (state England left; HQ inland city unverified) |
| 267097759427 | Hanwha Data Centers | Apollo geo + owner | country US/CA → South Korea/Seoul; owner Ken → Tim Z |
| 297782865631 | Firebird | Apollo geo + owner | country US/CA → Armenia/Yerevan; owner Ken → Tim Z |
| 316173995714 | Altice/Optimum Business | Apollo geo + owner | country Kenya/Nairobi → US/NY; owner Tim Z → Tim Lieto (East) |
| 297892337349 | center3 | Confidence resolution | manual_review_required → high_90 (clear AI Signals - colo evidence: 1GW HUMAIN JV, 20+ DCs, submarine cables) |
| 251593520882 | FSM Telecommunications | Apollo geo + brief regen | country Slovenia/Ljubljana → FSM/Pohnpei; account_brief + provisioning_landscape regenerated (template bleed) |
| 193865437936 | Sonic Telecom | Brief regen | account_brief + provisioning_landscape regenerated (template bleed: "$10B problem", "polite chaos") |
| 193034821367 | visionarybroadband | Brief regen | account_brief + provisioning_landscape regenerated (template bleed) |
| 251593594604 | Noramco Telecom | Brief regen + name flag | account_brief + provisioning_landscape regenerated; HubSpot name "Noramco" vs domain monaco-telecom.mc inconsistent — flagged for canonical brand correction (Monaco Telecom) |
| 254538313405 | BEK Communications | Brief regen | provisioning_landscape regenerated (template bleed) |
| 264590543565 | Gorge Networks | Brief regen + dedup flag | provisioning_landscape regenerated; R3 dedup candidate vs Blue Mountain Networks parent (merged 2020) |
| 251270645449 | IPLink Telecom | Brief regen + brand note | account_brief + provisioning_landscape regenerated; brand IPLink/Giga.Digital ambiguity, domain gigalinks.net.br |
| 268079107799 | Columbus Communications Grenada | Brief regen | provisioning_landscape regenerated (template bleed) |

### FULL (8) — segment/sub-segment reclassifications

| ID | Name | Old → New | Tier change |
|---|---|---|---|
| 253149467339 | CloudBurst | Modular - colo → Greenfield | tier_1 → tier_2 (Greenfield default T2) |
| 297892337355 | Riot Platforms | Data Center Colo Provider/AI Signals - colo → NeoCloud/Crypto to AI - Neoclouds | tier_1 (no change; BTC-mining lineage → NC5 per Cooper 2026-05-14) |
| 267086878426 | DYXnet | Fiber Operator/Regional CLEC → MSP/Aggregator/Managed Network Services - MSP | tier_3 → tier_2 (asset-light overlay, 21Vianet ecosystem) |
| 311359988419 | Structured Communication Systems | Fiber Operator/Regional CLEC → MSP/Aggregator/Managed Network Services - MSP | tier_3 → tier_2 (IT integrator, not fiber) |
| 311374390008 | Netcom Technologies | Fiber Operator/Regional CLEC → MSP/Aggregator/Managed Network Services - MSP | tier_3 → tier_2 (structured cabling integrator) |
| 311358187235 | PowerTransitions | Fiber Operator/Regional CLEC → Flagged for deletion | n/a (non-ICP; power infrastructure operator, no fabric evidence) |
| 316210812646 | Airtel Africa / Nxtra | Fiber Operator/Regional CLEC → Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op | tier_3 → tier_1 (Bharti Airtel subsidiary, 150M+ subscribers, 14 countries) |
| 316303588039 | A1 Wholesale | Fiber Operator/Regional CLEC → Network Operator(Tier 1 / VNO)/Pure Wholesale Carrier - Network Op | tier_3 → tier_1 (A1 Telekom Austria wholesale arm, OAN platform) |

---

## Notable patterns this batch

1. **Template-bleed at scale.** 7 records had marketing-template copy in `account_brief` and/or `provisioning_landscape` containing phrases like "the $10 billion problem", "polite chaos", "60-90 day turn-ups", "automation stops at the network edge". This pattern recurs across Fiber Operator records created 2025-10 / 2026-01 by an earlier enrichment run. Sweep-wide grep candidate: `account_brief CONTAINS "polite chaos" OR "$10 billion problem" OR "stops at the network edge"`. Estimated 50-100 additional records affected.
2. **Apollo geo drift on global-conglomerate records.** Hanwha (Korean conglomerate showing CA), Firebird (Armenian AI DC showing CA), Altice/Optimum (US Northeast cable showing Kenya), Ficolo (Finnish underground colo showing UK). Apollo records the wrong corporate entity HQ when a similarly-named US entity exists or when group/subsidiary parsing fails.
3. **Sub-segment mismatch on Bharti Airtel family.** Airtel Africa / Nxtra was sitting at Fiber Operator/Regional CLEC tier_3 despite being one of Africa's largest mobile operators with major DC arm in India. Two sibling records (Nxtra Data, Nxtra by Airtel) flagged for R3 dedup.
4. **A1 Wholesale misclassification.** Wholesale arm of a European Tier-1 telecom (A1 Telekom Austria) was sitting at Regional CLEC tier_3 despite 95% Austrian municipal fiber coverage + OAN platform serving 50+ providers. Pure Wholesale Carrier - Network Op default T1.
5. **NC5 Crypto-to-AI cascade continues.** Riot Platforms is the next BTC-miner-to-AI-landlord record after Crusoe, Applied Digital, Prometheus Hyperscale (moved 2026-05-14). NVDA/AMD-anchor + GW-scale facility + BTC mining lineage = NC5.
6. **IT integrators tagged as Fiber Operator.** Structured Communication Systems, Netcom Technologies, and PowerTransitions all came in as Fiber Operator/Regional CLEC but are IT integrators (structured cabling, MSP/MSI) or power-only infrastructure. Likely a March 2026 batch import that over-routed CLEC. Three reclassified this batch; suggests a sweep-wide candidate for `account_brief CONTAINS "structured cabling" OR "low-voltage" OR "IT integrator"`.
7. **Greenfield pattern grep candidate (carrying forward from Batch 22).** CloudBurst confirms the pattern: `account_brief CONTAINS "development-stage" OR "developing" + "AI-ready"` + small facility count → Greenfield.
8. **Sort-tie collision.** All 50 records this batch shared `last_enriched_date` clustered around 2026-03-18 (10 records) and 2026-04-01 (39 records). With offset=10/20/30/40 pagination, no dupes this run — full 50/50 throughput.

---

## Apollo budget tracker

- This batch: 0 credits
- Sweep cumulative through batch 23: unchanged (continues at prior batch level)
- APOLLO_ENFORCEMENT=disabled; no draw against 850/wk cap

## Errors / failures

None. All 50 HubSpot writes succeeded across 6 batch calls (3 LIGHT + 2 MEDIUM + 1 FULL).

## Manual review escalations (HOLD)

None this batch. HOLD policy = NONE per sweep parameters; every record qualified, reclassified, or flagged.

## Owner mismatches fixed this batch

3 — Hanwha (Ken → Tim Z), Firebird (Ken → Tim Z), Altice/Optimum (Tim Z → Tim Lieto East).

## R3 dedup flags raised this batch

- Airtel Africa / Nxtra (316210812646) ↔ Nxtra Data (303423288020) ↔ Nxtra by Airtel (302067487460) — 3-way Bharti Airtel family
- Gorge Networks (264590543565) ↔ Blue Mountain Networks (parent record) — merged 2020
- Iron Mountain Global (277224239832) ↔ Iron Mountain EMEA (277406844633) — verify D2 wholesale-arm policy fit

## Carried forward from prior batches

- Switch Datacenters BV entity-mix-up watch (batch 22)
- DataCrunch / Verda Apollo rebrand drift (batch 22)
- Liquid Web / Hetzner managed-hosting borderline (batch 22, recurring)
- 2026-02 records template-bleed cluster (batch 21+22, escalated this batch)
