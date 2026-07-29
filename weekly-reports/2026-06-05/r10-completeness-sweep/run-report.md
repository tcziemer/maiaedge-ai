# R10 Field Completeness Sweep — 2026-06-05 (Fri, 1:30 PM CT)

**Status:** ⚠️ PARTIAL (16 records filled, 0 write failures; large ICP enriched-field backlog deliberately held for subsequent daily runs rather than boilerplate-filled).
**Circuit breaker:** not tripped.
**Apollo:** 0 / 25 sub-cap used (all fills knowledge- + web-research-grounded; no firmographic gaps required Apollo). Weekly W23: 0/850.

## Stage 0 — Preflight
- HubSpot / web MCP healthy. Apollo budget read: W23 0/850, effective_apollo = 25.
- Canvas `F0B0AFSB9LN` read; built a 516-ID Tier 3 / standing-hold skip superset (conservative, from the live first-half of the ledger).

## Stage 1 — Candidate pool
Trigger totals (COMPANY, missing-field NOT_HAS_PROPERTY, exclusions applied):
| Trigger | Total | % of ~3,350 active |
|---|---|---|
| `account_tier` missing | 2 | 0.1% |
| `account_brief` missing | 72 | 2% |
| `infrastructure_profile` missing | 397 | 11.8% |
| `company_sub_segment` missing | 484 | 14.4% |
| `signal_heat` missing | 420 | 12.5% |

**Circuit-breaker assessment:** No single field exceeds the 15% (~503) threshold. The large infra/sub_segment/heat counts are dominated by legitimately-blank `Other` / `Partner Target` reference records (competitors, vendors, analysts, distributors) where ICP-structural fields (`infrastructure_profile`, `company_sub_segment`, `fabric_provisioning_approach`) do NOT apply — not a connector dropout. Confirmed by re-querying restricted to the 6 ICP `customer_segment` values.

**Genuine ICP gap pool (the R10 core target):** 133 ICP records missing ≥1 mandatory enriched field (121 non-excluded after skip-set + MaiaEdge + today + 120-day-stale exclusion; 12 excluded as standing Tier 3 / R3-dedup holds). Almost all are a single batch enriched 2026-05-18/19 that received segment + sub_segment + tier but never had the 6 narrative/structured enriched fields populated — exactly the "falls between R1/R2/R-Tier-Audit" gap R10 exists for.

## Stage 2/3 — Fills written (16 records, 2 batches of 8, 0 failures)

**Path A — frozen-tier seed-once (1):**
- ResetData (324591600333), NeoCloud / Sovereign AI Clouds - Neocloud, `hs_is_target_account=true`, `account_tier` blank → seeded `tier_1` (default Sovereign AI = T1, no signal modifiers; heat already Cold). **This resolves the recurring daily R1 "B2 frozen-tier no-op" loop** that the seed-once rule was written to fix. No `last_enriched_date` bump (tier-only write).

**Path B — enriched-field gap fills (15):** filled only missing fields; canonical enums verified against MEMORY (`infrastructure_profile` bands w/ K-abbrev, `hyperscaler_proximity` "None Known", `fabric_provisioning_approach` snake_case). 2-4 sentence cap, hyphens only, "carrier infrastructure" descriptor.

| Record | ID | Segment | Fields filled | LED bump |
|---|---|---|---|---|
| ScanSource | 324038855390 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| Intelisys | 324037036767 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| AppDirect | 324037036787 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| Sandler Partners | 324001849047 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| AVANT Communications | 324170890970 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| Telarus | 318219105016 | MSP/Aggregator | infra only | no (single field) |
| TD SYNNEX | 300408171229 | MSP/Aggregator | geo+infra+hyper+fabric+prov | yes |
| X4 Solutions | 324037036788 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| CyberNet Communications | 323996380884 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| Logicalis | 321842590405 | MSP/Aggregator | infra+hyper+fabric+prov | yes |
| J.P. Morgan & Co. | 240446137023 | Enterprise (Financial) | infra+hyper+prov | yes |
| Google Fiber | 322405956291 | Fiber Operator | geo+infra+hyper+fabric+prov | yes |
| Galaxy Digital | 324071115455 | NeoCloud (Crypto to AI) | infra+hyper+fabric+prov | yes |
| NexGen Cloud | 316466007749 | NeoCloud | geo+infra+hyper+fabric+prov | yes |
| Paperspace | 324190689997 | NeoCloud | infra+hyper+fabric+prov | yes |

- TSD / Master Agent / distributor records (ScanSource, Intelisys, AppDirect, Sandler, AVANT, Telarus, TD SYNNEX, X4, CyberNet) → `infrastructure_profile = None Identified` (canonical MSP pattern: no owned carrier infrastructure), `hyperscaler_proximity = None Known`, `fabric_provisioning_approach = manuallegacy_processes`.
- Galaxy Digital corroborated via web (Helios 1.6 GW+ TX campus, CoreWeave 15-yr anchor lease) → landlord profile.
- NexGen Cloud corroborated via web (Hyperstack GPUaaS, NVIDIA H100/H200, Europe/Nordic) → `homegrownproprietary_platform`.

**Per-field gap counts (ICP pool), before → after this run:** infra-missing 121 → 106; sub_segment-missing (ICP) unchanged (Win s.a. + Hub One held); heat-missing (ICP) unchanged; brief-missing (ICP) unchanged. Tiers seeded on frozen blanks: 1 (ResetData).

## Held for next run (Partial)
- ~105 ICP records (predominantly obscure international Network Operators enriched 2026-05-18/19 — e.g. Telekom Sudan, Kyivstar, Telecom Argentina, Digicel/Flow island carriers, Pacific/African MNOs — plus a few Colos (Vapor IO, Flux Core, Ten Peaks) and regional Fiber Ops). Each needs genuine per-company research to populate `infrastructure_profile` / `provisioning_landscape` accurately; deliberately NOT boilerplate-filled (per framework research-first + R2 2026-06-05 precedent of deferring rather than fabricating).
- Win s.a. (NRB) 326163435208 + Hub One 326325672653 — missing only `company_sub_segment`; Network Operator sub-segment classification needs research to choose correctly among the 5 NetworkOp sub-segments. Held.
- `Other` / `Partner Target` reference records missing infra/sub_segment are correctly NOT R10 gaps (ICP-structural fields N/A); `signal_heat`/`account_brief` backlog on `Other` records left to R-Tier-Audit / R2 backfill.

## Escalations
None requiring a DM. ResetData loop resolved via seed-once (informational; folds into the CRM Ops Daily Digest). No fatal abort, no circuit-breaker trip, no 400 enum errors.

---

# ADDENDUM — Deep-research pass on the held pool (Cooper ad-hoc, same day)

Per Cooper's same-day request, the ~105 held ICP records were NOT deferred — they were researched and filled this session.

**Method:** 106 records (the full held pool incl. Win s.a. + Hub One) split into 8 chunks; 8 parallel general-purpose research subagents ran genuine web research (WebSearch + web_fetch) per company and produced enum-correct field proposals to disk. Centrally validated against canonical enums (0 enum/em-dash errors across 106) and written to HubSpot in batches of 10 (2 by orchestrator + 86 by a mechanical writer subagent). **Result: 106/106 written, 0 failures.** ICP `infrastructure_profile` gap reduced 133 → 11 (the 11 remaining are standing Tier 3 / R3-dedup holds correctly excluded). 0 Apollo (all web-research-grounded). 98 records LED-bumped (full enrichment pass); 8 single/double-field top-ups not bumped.

**Win s.a. (NRB) + Hub One** classified `company_sub_segment = "Tier 1 Carrier - Network Op"` (best available fit among the 5 Network Operator sub-segments for these regional EU operators; noted as approximate).

## Follow-up candidates surfaced by research (flagged for D7 / R4 / R6 / R-Tier-Audit — NOT acted on by R10, which only fills)

**Suspected segment misclassifications (D7):**
- Cast AI (300329366233) — software-only Kubernetes cost-optimization SaaS, no GPU/DC/network; classified NeoCloud. Likely out of ICP.
- Teligent Telecom (318231691993) — telecom software/systems vendor (sells to BT/Telia), not a carrier; classified Tier 1 Carrier.
- IntelePeer (318223398591) — CPaaS software vendor; classified Managed Network Services MSP.
- Massy Stores Telecom (319190684408) — resolves to Massy Technologies InfoCom, an ICT/MSP integrator, not a Tier 1 carrier.
- Megatel Netcom (318231692000) — ~12-emp wholesale voice/SMS reseller, classified Fiber CLEC.
- CIMA Telecom (316598423244) — wholesale voice carrier, classified Fiber CLEC.
- SBTS (318106540783) — CPaaS/messaging JV, classified Tier 1 Carrier.
- Sky UK (318339892957) — national wholesale reseller, classified Regional CLEC.

**Defunct / eviction candidates (R4 / pre-deletion-audit):**
- Centennial (319173096167) — acquired by AT&T (FCC 2009, brand retired 2010); domain not an active independent carrier.
- Symbiote Investments / Caricel (319126831825) — Jamaican licences revoked 2018, never launched at scale.
- Supercable Venezuela (319197827820) — CONATEL licence suspended 2026-03-14, reportedly in liquidation.
- Digital8 PNG (319197829832) — no corroborating evidence of existence (PNG has 3 recognized MNOs); unverifiable.
- MAGECI (319204762328) — no verifiable telecom footprint in Rwanda; unverifiable.

**Over-tiered sub_segment cluster (sub_segment/tier review — R-Tier-Audit/D7):** ~25 small single-territory island/regional MNOs and ISPs carry `Tier 1 Carrier - Network Op` (e.g. BVI Phones, CSL Samoa, Canl+, Logic, Setar, Digicel Bermuda, Flow USVI, bmobile, Golis, Hexabyte, Lightspeed, Cobranet, SWIFT Networks, Myanmar Net, NetCo Lebanon, Newcom Gibraltar, Fast Link Iraq, Standard Telecom DRC, PDS Pacific, PTI Pacifica, Tizeti, VIPNET). Filled conservatively; classification left unchanged.

**Wrong `state` values (R6 — not in this run's miss arrays):** Telecom Vanuatu (NC → Shefa/Port Vila), Telesur (Amazonas → Paramaribo), Tizeti (Prahova → Lagos), Kyivstar (Khmelnytskyi → Kyiv).

**Identity unverified:** Ten Peaks Data Centres (319182692005-area; CRM domain tenpeaks.ca vs documented NZ tenpeaks.co.nz). **Nascent/greenfield:** Flux Core Data Systems (2025-founded, ~2 emp).

11 records flagged low_confidence by the researchers; values are best-supported conservative estimates and will be re-validated by D7.

---

# ADDENDUM 2 — Follow-up corrections ACTIONED (Cooper ad-hoc, same day)

All four follow-up categories were fixed this session (41 records, 0 failures; 0 associated deals on any reclassified/flagged record, deal-safety verified per the inviolable customer-protection rule).

- **8 → Flagged for deletion** (reason code + evidence set; `company_sub_segment` cleared; `account_tier` = tier_5): Cast AI, IntelePeer, Teligent (No ICP fit - software vendors); Centennial (Defunct - AT&T-acquired), Symbiote/Caricel (Defunct - licences revoked 2018), Supercable VE (Defunct - CONATEL-suspended/liquidation); Digital8 PNG, MAGECI (D1 disqualified - unverifiable). These now sit in Cooper's manual-delete queue.
- **5 within-ICP reclassifications:** Sky UK → Network Operator / Cable MSO Enterprise Division (tier_2); Massy Tech + SBTS → MSP/Aggregator / Managed Network Services (tier_3); CIMA + Megatel → MSP/Aggregator / Telecom Aggregator (tier_3 / tier_4) - both were wrongly Fiber Operator / Regional CLEC.
- **25 over-tiered single-territory NetOp MNOs** demoted tier_1 → tier_2 (the computed floor for "Tier 1 Carrier - Network Op" given no active signals; matches what R-Tier-Audit would compute).
- **4 wrong `state` values:** Telecom Vanuatu NC → Shefa; Telesur Amazonas → Paramaribo; Tizeti Prahova → Lagos; Kyivstar Khmelnytskyi → Kyiv.

**Left for downstream routines (noted, not actioned):** the small-MNO cluster has no precise sub_segment in the 30-value taxonomy (used tier demote as the available lever; deeper sub_segment reclassification deferred to D7's per-company D5 pass). Airtel Seychelles (small-MNO mislabeled Fiber Operator) and Lightspeed Communications (possible duplicate / acquired into Kalaam) left for D7 / R3.

