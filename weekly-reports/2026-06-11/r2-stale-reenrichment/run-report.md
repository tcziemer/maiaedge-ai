# CRM Guardian - Stale Re-Enrichment - 2026-06-11 - 4 Tier 2 flagged, 0 new Tier 3 held (3 carried)

Run summary: 37/100 processed (40-record Filter-C pre-spread batch, 3 standing Tier 3 holds carried unprocessed) · FULL 2 / LIGHT 35 / RECLASSIFY 0 / DEFER 5 · Tier 1: 33, Tier 2: 4, Tier 3 new: 0 · Apollo: 0/50 sub-cap (weekly W24: 0/850) · Freshness: GREEN

## Trigger query

- Filter A (last_enriched_date < 2026-02-11, active): **0 records**
- Filter B (never-enriched + segment populated, active): **0 records**
- Filter C rotation pre-spread (A+B < 40): fired. 45 oldest-enriched active records returned (active pool 3,412; oldest cohort 2026-02-24 to 2026-04-27). Took 40, deferred 5 newest to next run: Telx Computers (318209570545), QKS Group (192930117355), Weka (300374927049), Arqit (192893760222), NASI (320311807732).

## What needs Cooper's attention

- **4 eviction Tier 2** - Filter HubSpot Companies → customer_segment = "Flagged for deletion" (all verified 0 associated deals before flagging):
  1. **PowerBridge** (292440159933, powerbridgesolution.com) - No ICP fit: consumer in-wall power/cable-management hardware for home theater.
  2. **Backbone Digital** (292440159935, backbone.digital) - No ICP fit: Vancouver digital marketing/tech consulting agency.
  3. **EIS Visual** (291620481743, eisvisual.com) - No ICP fit: visual content / proposal-media consultancy.
  4. **Exa** (320876610270, exa.com) - No ICP fit: wrong-entity import artifact. exa.com is legacy Exa Corp (CFD software, Dassault-acquired 2017), NOT EXA Infrastructure. Prior brief already recommended deletion; segment now matches.
- **Tier anomalies on Other records (left untouched, no defaults-table row for Other):** Huawei (302088379095) carries account_tier=tier_1 and Kyndryl (302186294978) tier_2 while classified Other. Recommend manual demotion to tier_4/5 or an R-Tier-Audit rule for Other-segment tier ceilings.
- **Possible future ICP:** Related Companies (277388835573) - parent is real estate, but its Related Digital arm is building large-scale data centers. Left as Other with reference note; worth a dedicated look if Related Digital gets its own record.

## Detail - segment changes / evictions

| Account | ID | Old → New | Reason |
|---|---|---|---|
| PowerBridge | 292440159933 | Other → Flagged for deletion | Consumer AV hardware vendor |
| Backbone Digital | 292440159935 | Other → Flagged for deletion | Digital agency, no infra |
| EIS Visual | 291620481743 | Other → Flagged for deletion | Proposal-media consultancy |
| Exa | 320876610270 | Other → Flagged for deletion | Wrong-entity import artifact (Dassault CFD software) |

## Detail - FULL-path re-enrichments (2)

| Account | ID | Writes |
|---|---|---|
| T-Systems | 303445718756 | recent_news refreshed (T Cloud Public sovereign-hyperscaler expansion targeting US feature parity by end-2026), provisioning_landscape filled, hyperscaler_proximity=Existing Facility Nearby, confidence → high_90, stamped. **Tier write skipped - hs_is_target_account=true** (tier_1 pinned). MSP/Aggregator / Cloud + Telecom Hybrid MSP confirmed. Heat Cold (no dated signal event; last_signal_date left null per truthful-default). |
| Madison Communications | 316197317360 | Web-verified Regional CLEC (Madison/Macoupin counties IL, FTTH, 1 Gbps, family-owned since 1940). Confidence medium_7089 → high_90, stamped. tier_3 / Cold unchanged (idempotent). |

## Detail - LIGHT keepers (31 re-stamped 2026-06-11)

- **12 brief-fills** (account_brief written from web research/verification + infrastructure_profile="None Identified" + fabric="none_identified" + heat=Cold): ServiceNow, Discernity (MDU managed-WiFi, Louisville KY), Related Companies, Enxoo, Cooley, Bank Street Group (**name corrected from "Bank Street Coup"**; digital-infra investment bank - strong deal-flow reference), iconectiv, IDC, Prodapt, AXON Networks (ISP orchestration software + OaaS, 2026 NeoCloud Leadership Award - good ecosystem ref), Sage Management (SIB telecom expense/blockchain SLA software), Huawei Cloud.
- **12 re-stamps, briefs already solid:** SES, Huawei, Kyndryl, Zoom, American Axess, Vinculum, Viasat, Alfacall, Proximus IT Services, Confindustria Assafrica, Global Peering Forum, Aegis Mobile.
- **7 re-stamps + heat backfill (Cold):** CWIT, BGIS (Partner Target - kept), Fiverr, Toptel, Gartner, Tomorrow Networks, UK Cloud.

## Recent news cleared (stale)

- Viasat (320874452703): Navarino-divestiture event dated 2026-01-05 (>90 days), no Signal Scan write in last 7 days → cleared recent_news_or_trigger_event + last_signal_date per Step 17.

## Tier 3 holds

New this run: **0**. Carried forward (standing, unprocessed, no date bump):

| Account | ID | Reason | Owner action |
|---|---|---|---|
| MMR Fiber Solutions / SouthWestern Power | 175221473010 | Entity-split ambiguity (open-access dark fiber op under power-parent domain) | Cooper / R3 |
| team.telstra.com | 316598423243 | Telstra subdomain dedup stub | R3 |
| Intercontinental Exchange | 311326703342 | Enterprise FinServ vs Colo dual-evidence ambiguity (flagged 2026-06-10) | Cooper |

## Run health: GREEN

Errors: None. 4 HubSpot batches (10/10/10/7), 0 failed writes. 0 Apollo credits. ~10 web searches. Date-bump discipline: 37 stamped (gate-passing keepers + definitive evictions), 3 holds not stamped, 5 deferrals not stamped.
