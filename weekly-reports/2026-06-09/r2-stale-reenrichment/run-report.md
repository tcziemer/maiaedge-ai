CRM Guardian - Stale Re-Enrichment - 2026-06-09 - 0 Tier 2 flagged, 0 Tier 3 held (new)

Run summary: 16/100 processed (all RE_ENRICH_LIGHT field-completions) · FULL 0 / LIGHT 16 / RECLASSIFY 0 / DEFER 0 · Tier 1: 16 / Tier 2: 0 / Tier 3 new: 0 · Apollo: 0/850 used (sub-cap 50, 0 consumed) · Freshness: GREEN (Filter-C pre-spread)

Trigger query (today 2026-06-09, 120-day cutoff 2026-02-09):
- Filter A (last_enriched_date < 2026-02-09, exclude Flagged-for-deletion + MaiaEdge own): 0 records.
- Filter B (never-enriched + segment populated, exclude Flagged-for-deletion): 2 raw -> MaiaEdge own 124293230301 (hard-stop) + BlueRim Networks 326179855037 (standing R3-dedup Tier 3 hold). Net 1, both non-processable.
- A+B net < 40 -> Filter group C (rotation pre-spread) fired. Active pool 3,422 records. Pulled the oldest-enriched not-yet-stale cluster (last_enriched_date = 2026-02-24, 18 records). 16 processed via LIGHT; 2 were standing R3 Tier 3 holds carried forward (MMR Fiber 175221473010, team.telstra 316598423243).

What needs Cooper's attention:
- 0 Tier 3 new holds. 0 evictions. 0 segment changes. Nothing requires action.
- 3 standing R3-scope Tier 3 holds re-confirmed present in the candidate pool (already on canvas F0B0AFSB9LN): BlueRim Networks (Smartaira dup), MMR Fiber / SouthWestern Power (surprise-ICP wholesale dark-fiber entity-split ambiguity), team.telstra.com (Telstra subdomain dedup stub). All R3 / Cooper scope, not R2.

Run health: GREEN

Errors: None.

---

Field-completion detail (the 16 opaque 2026-02-24 micro-records deferred by 2026-06-08 R2 - all were missing all 7 enriched fields; researched via web_search, real briefs written, keep/delete decided, last_enriched_date stamped 2026-06-09). All confirmed Other / PARTNER_KEEP (non-ICP ecosystem references); none surprise-ICP, none HARD_DELETE junk, none dead-domain. 0 Apollo (LIGHT path; firmographics not needed for keep-vs-delete).

| ID | Name | Domain | Verdict | Category | Conf |
|---|---|---|---|---|---|
| 174907029204 | LB Networks (Local Backhaul Networks) | lbnetworks.co | Other / PARTNER_KEEP | Network-assurance software (OcularIP) for 140+ SPs | high_90 |
| 316614767315 | Pai Telecom | paitelecomm.com | Other / PARTNER_KEEP | Wholesale/retail VoIP + A2P SMS aggregator (HK) | high_90 (was medium) |
| 316561917650 | HDTandem | hdtandem.com | Other / PARTNER_KEEP | Virtual-tandem voice termination (~500M min/mo) | high_90 |
| 192882963141 | Bumblebee Networks | bumblebeenet.com | Other / PARTNER_KEEP | NaaS/VPN-replacement SaaS startup (competitive ref). State corrected Vermont -> California; owner -> Ken (Palo Alto HQ) | high_90 |
| 316627226307 | Network Planning Solutions (NPS) | npsltd.net | Other / PARTNER_KEEP | UK fibre design/build/maintenance contractor (Openreach PIA) | high_90 |
| 316502492868 | JapTel | japtel.net | Other / PARTNER_KEEP | Global VoIP + SMS aggregator (NY) | high_90 (was medium) |
| 316614767309 | Latino Communications (Latcomm) | latcomm.net | Other / PARTNER_KEEP | Wholesale voice carrier, US->LatAm termination (~500M min/mo) | high_90 |
| 316522694359 | MasNegocio | masnegocio.com | Other / PARTNER_KEEP | KIO Networks SaaS/cloud-apps arm (MX) | high_90 |
| 316560181993 | Innovative Telecom | innovativetelecomcorp.com | Other / PARTNER_KEEP | Wholesale voice + SMS aggregator (San Jose) | high_90 (was medium) |
| 316627226302 | ALCASAGAR | alcasagar.com | Other / PARTNER_KEEP | International wholesale voice + SMS (Miami) | high_90 |
| 316623621846 | go2uno (UNO) | go2uno.com | Other / PARTNER_KEEP | Managed SIP/Teams/connectivity services (TX) | high_90 |
| 316561917653 | WIT ONE | witone.one | Other / PARTNER_KEEP | Managed SD-WAN/security MSP, OTT (Miami; competitive ref) | high_90 |
| 316561917662 | Associated Carrier Transport | associatedcarrier.com | Other / PARTNER_KEEP | Telecom network-sourcing broker (thin identity) | medium_7089 |
| 316618313424 | BNS (Bold New Solutions) | boldnew.com | Other / PARTNER_KEEP | Telecom/DC consulting + infra services (FL); BNS Networks div | high_90 |
| 316558341873 | HGC Construction | hgcconstruction.com | Other / PARTNER_KEEP | General contractor w/ data-center + telecom mission-critical practice (Cincinnati) | high_90 |
| 316561917655 | Global Convergence Solutions (GCS) | globalconverge.com | Other / PARTNER_KEEP | Carrier interconnect-voice OSS/BSS software (NJ) | high_90 |

Writes: 2 HubSpot batches (8/8 + 8/8), 0 failed. Each record: customer_segment=Other (confirmed), account_brief + geographic_focus + infrastructure_profile="None Identified" + fabric_provisioning_approach="none_identified" + segmentation_confidence + signal_heat="Cold" + last_enriched_date=2026-06-09. Bumblebee also: state=California, hubspot_owner_id=162339176 (Ken). account_tier left unchanged (LIGHT path does not recompute tier).

Deferred (no bump): ~30 records enriched 2026-04-01 already carry full enriched fields + clean briefs (well below the 120-day line; naturally due ~2026-07-30). Left for future pre-spread runs - no field gap to close, re-stamping them today was lower value than the 02-24 field-completion backlog. They yield to genuine work per the Filter-C "yields + defers remainder" rule.

Owner re-derive note: several 02-24 records carry owners that may not match the HQ-state territory map (e.g. Latcomm TX -> Tim Z; Associated Carrier TN -> Ken). Left untouched - R6 Territory & Hygiene owns territory correction; LIGHT path only re-derives when state itself changes (done for Bumblebee).

Notes for borderline calls: the wholesale voice/SMS termination players (Pai, HDTandem, JapTel, Latcomm, Innovative Telecom, ALCASAGAR) are OTT voice/minute aggregators, not the L1-L3 physical carrier infrastructure MaiaEdge interconnects; consistent with prior R1 treatment of SIPNAV/Speedflow/didXL -> Other. UNO + WIT ONE are small (3-10 employee) managed-services shops, kept as Other partner/competitive references rather than promoted to MSP/Aggregator ICP (no substantial-aggregator evidence).
