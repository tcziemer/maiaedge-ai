# Mass Re-Enrichment Sweep — Batch 41

**Sweep:** 2026-05-18-post-phase-3-framework
**Date:** 2026-05-19
**Records processed:** 50/50 (all written)
**Pool before:** 809 remaining
**Pool after:** 759 remaining
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled, no Apollo calls needed)
**HOLDs:** 0 (per Cooper directive — resolve all ambiguity in-line)

## Path mix

- LIGHT: 28
- MEDIUM: 15
- FULL: 4
- RECLASSIFY: 3 (2 → Flagged for deletion; 1 → Other; 1 → MSP/Aggregator)

## Batch composition

Heavy fiber-operator skew this batch — 44 of 50 records are Fiber Operator parent, 6 are Data Center Colo Provider, 1 MSP/Aggregator. No NeoCloud, no Network Operator Tier 1, no Enterprise.

## Per-record entries

### Vertical Bridge (292748543700)
- Path: RECLASSIFY (D1 disqualifier — tower company)
- Segment: Fiber Operator -> Other
- Sub-segment: Regional CLEC - Fiber operator -> (cleared)
- Tier: tier_3 -> (cleared, Step A0 — not in 6 ICPs)
- Reason: Largest private US tower owner (17,000+ towers, recent $1.94B tower ABS + KKR $1.5B equity). Towers are useful partner infrastructure but NOT a Fiber Operator ICP. Reclassified Other (Partner Target).

### Globix (296846534373)
- Path: RECLASSIFY (defunct entity)
- Segment: Fiber Operator -> Flagged for deletion
- Reason: Globix renamed NEON Communications Feb 2007, acquired by RCN Nov 2007. Brand defunct ~20 years. Domain globix.com not associated with active fiber operations.

### Troy Cablevision (296846534381)
- Path: RECLASSIFY (acquired and rebranded)
- Segment: Fiber Operator -> Flagged for deletion
- Reason: Acquired by C Spire Dec 2021, fully rebranded as C Spire Jun 2023. Operations consolidated into C Spire parent record.

### Foremost Cloud Services (296846534388)
- Path: RECLASSIFY (segment correction)
- Segment: Fiber Operator -> MSP/Aggregator
- Sub-segment: Regional CLEC - Fiber operator -> Telecom Aggregator - MSP
- Tier: tier_3 -> tier_2
- Reason: TX-based VoIP/Hosted PBX/Internet aggregator with offices in Dallas, Harlingen, San Antonio, Corpus Christi. Aggregates underlying carriers; small in-house colo. Reseller-plus-light-infra pattern fits Telecom Aggregator, not Fiber Operator.

### EarthLink (292520968895)
- Path: FULL (national-scale promotion + field fill)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 2 National Wholesale - Fiber operator
- Tier: tier_3 -> tier_2
- Filled: geographic_focus, infrastructure_profile, fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event
- Reason: 29,000+ route miles, 5M customers across all 50 states, wholesale+retail. National scale fits Tier 2 National Wholesale.

### Hotwire Communications (292648497859)
- Path: FULL (field fill on 6/7 missing)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged; multi-state but FTTH-focused)
- Filled: geographic_focus, infrastructure_profile, fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event
- Reason: Largest privately-held FTTH ISP, 700+ communities in FL/GA/PA, 1500 emp, $369M rev. Multi-state but residential/HOA/MDU focused.

### AOC Connect (292648532688)
- Path: FULL (research-grounded reclassification within Fiber Operator parent)
- Sub-segment: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Filled: all 7 enriched fields rewritten with verified data
- Reason: ~5,000 fiber miles in DC metro reaching 1,000+ government buildings + carrier POPs. JLC Infrastructure acquired Apr 2023. Wholesale carrier + federal interconnect focus fits Long Haul / Backbone.

### Blackfoot (296846534375)
- Path: FULL (placeholder brief replacement)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 (unchanged)
- Filled: account_brief, infrastructure_profile, fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event
- Reason: Western Montana / Idaho regional fiber operator. Surrendered 688/2,687 RDOF locations May 2025 citing FTTP cost overruns. Active but contracting rural-build footprint.

### Sub-segment migrations to Municipal / Cooperative - Fiber operator (6)
- South Central Communications (296846534379) — Regional CLEC -> Municipal / Cooperative — member-owned telephone cooperative
- Glenwood Telephone Membership (296850118369) — Regional CLEC -> Municipal / Cooperative — telecommunications cooperative
- Project Mutual Telephone (296850118370) — Regional CLEC -> Municipal / Cooperative — telecommunications and broadband cooperative
- Sei Communications (296850118373) — Regional CLEC -> Municipal / Cooperative — member-owned cooperative
- CDE Lightband (296851879625) — Regional CLEC -> Municipal / Cooperative — municipally-owned public utility
- PinevilleCS (296851879629) — Regional CLEC -> Municipal / Cooperative — municipally owned telecommunications provider
- All 6: tier_3 -> tier_4 (Municipal / Cooperative default per tier-compute-spec §5)

### MEDIUM (field fills, value-prop bleed cleanup, template-bleed cleanup)
- CyrusOne KEP (277392436946) — filled hyperscaler_proximity (Existing Facility Nearby), fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event
- PointOne (269634685634) — filled hyperscaler_proximity + fabric_provisioning_approach
- Guam Exchange (268456905406) — value-prop bleed cleanup in provisioning_landscape
- Bare Metal Pittsburgh (274077120190) — value-prop bleed cleanup in provisioning_landscape
- Prov.net (274427631338) — corrected infrastructure_profile (Large 20-49 was wrong for SMB-scale), value-prop bleed cleanup
- United Telephone (268250706640) — template bleed cleanup (Network Isolation / polite chaos rhetoric removed from brief)
- TCW (268250706652) — template bleed cleanup
- Clearwave Fiber (291537915620) — filled fabric_provisioning_approach, provisioning_landscape, recent_news_or_trigger_event
- GoNetspeed (296851879623) — filled provisioning_landscape with T-Mobile JV context
- MTCO (296850118367) — added post-acquisition (MCC Network Services Jan 2026) context

### LIGHT (date bump only, framework-consistent, no field changes needed)

InterServer (269700371159), Mosaic Data Services (271844082389), Intrepid Fiber Networks (291687366380), Omni Fiber (292755851981), Surf Internet (292796237529), Orbitel Communications (296846534371), Computers/Electronics/Office Etc. (296846534374), Ketchikan Public Utilities (296846534376), Webster-Calhoun Cooperative (296846534377), Blue Lightning (296846534380), Rico Telephone (296846534382), Baldwin Telecom (296846534383), Blb Communications (296846534384), Mabel Cooperative (296846534385), Reynolds Telephone (296846534386), Clay County Connect (296850118368), LiveOak Fiber (296850118371), Natco (296850118375), Beehive Broadband (296850118376), Monroe Telephone (296850118377), Gridley Telephone (296850118379), Circle Fiber (296850118384), Twin Valley Telephone (296850118388), Noanet (296851879628), Service Electric (296851879632), Reservation Telephone Cooperative (296851879634).

All LIGHT records: confirmed correct customer_segment, sub-segment in 30 active values, 5-7/7 enriched fields, no legacy-string detection match. Tier recompute = current tier (idempotent no-op). Only last_enriched_date stamped.

## Cumulative pattern counters (after batch 41)

| Pattern | Cum prior batch 40 | This batch | New cum |
|---|---:|---:|---:|
| National operator under-tiering | 44 | 1 (EarthLink) | 45 |
| Within-fiber promotions | 26 | 2 (EarthLink, AOC Connect) | 28 |
| Within-fiber demotions | 18 | 6 (muni/coop migrations) | 24 |
| Template-bleed remediation | 26 | 2 (United Telephone, TCW) | 28 |
| Maritime/MSP misclassified as Telecom Aggregator | 6 | 0 | 6 |
| MaiaEdge value-prop bleed | 31 | 3 (Guam Exchange, Bare Metal Pittsburgh, Prov.net) | 34 |
| CPaaS/voice aggregator misclassified as Fiber Op | 7 | 1 (Foremost Cloud Services) | 8 |
| Pure satellite misclassified as Fiber Op | 3 | 0 | 3 |
| Subsea cable operator promotions | 5 | 0 | 5 |
| IX/Internet Exchange policy gap | 3 | 0 | 3 |
| R&E network framework gap | 1 | 0 | 1 |
| AI Signals - colo reclassifications | 5 | 0 | 5 |
| Sanctions-driven ICP->Other reclasses | 2 | 0 | 2 |
| Crypto-to-AI Neocloud reclasses | 1 | 0 | 1 |
| Cable-manufacturer D1 evictions | 1 | 0 | 1 |
| Dedup/identity evictions | 5 | 1 (Troy Cablevision -> C Spire) | 6 |
| Defunct-brand evictions (NEW) | 0 | 1 (Globix) | 1 |
| Tower-co D1 evictions (NEW) | 0 | 1 (Vertical Bridge) | 1 |

## Drain projection

- Done in sweep: ~2050 records (41 batches at ~50 each, minus held)
- Remaining: 759
- ETA: ~15 more batches at BATCH_SIZE=50

## Notes

- One enum validation error caught + corrected mid-batch: `hyperscaler_proximity` allowed values are `["Announced: <50 miles", "Announced: 50-200 miles", "Existing Facility Nearby", "None Known"]`. Retried CyrusOne KEP with "Existing Facility Nearby" successfully. Adding to data quality follow-up: consider deprecating the "On-Net to Hyperscalers (direct or campus)" string that has been used elsewhere if it's NOT a valid HubSpot enum value.
- 6 Municipal/Cooperative migrations in one batch is unusually high — these are likely records that were sourced via a generic broadband-list pull that didn't preserve the cooperative/municipal designation. Account-sourcing skill could be tuned to capture the cooperative-membership signal at intake.
- GoNetspeed stayed Regional CLEC but flagged as a Tier 2 National Wholesale candidate for once the T-Mobile JV closes (1H 2027) and rolls into T-Fiber.
- Hotwire Communications stayed Regional CLEC — multi-state FTTH but residential/HOA/MDU-focused, not wholesale.
