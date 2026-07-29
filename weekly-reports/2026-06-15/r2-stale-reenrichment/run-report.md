CRM Guardian - Stale Re-Enrichment - 2026-06-15 - 0 Tier 2 flagged, 0 Tier 3 held (R2 scope); 2 cross-routine handoffs

```
Run summary: 39/100 processed (re-stamped) · Filter-C pre-spread (A+B=0) · Tier 1 39 / Tier 2 0 / Tier 3 0 (R2 scope) · Apollo: 0/50 sub-cap (W25 2/850, 848 remaining) · Freshness: GREEN

What needs Cooper's attention:
- Confluence Research (192890159856, confluenceresearch.com.au) -> routed to D7. 2nd consecutive R2 re-verification failure (06-12 + today); domain resolves to no clear Australian entity. No date bump. D7 web_fetch/deep-research should make the definitive keep-vs-evict call.
- FPT (300724801211, fptsoftware.com, Other tier_5) -> R3 dedup. Confirmed duplicate of FPT Software (326715774698, fpt-software.com, Enterprise-CustomerSegment / Outsourcing Services - Enterprise, tier_3, created by R1 2026-06-09). Recommend merge into the Enterprise ICP record (keep 326715774698 as primary). NOT re-stamped. NOTE: FPT AI Factory (303405064912, fpt.com, NeoCloud / AI Infrastructure providers, tier_1) is a legitimately separate FPT arm - do not merge.
- 4 standing holds re-confirmed in pool, carried unprocessed (already on canvas): MMR Fiber / SouthWestern Power 175221473010 (entity-split surprise-ICP -> R3/Cooper), team.telstra.com 316598423243 (Telstra subdomain dedup stub -> R3), Intercontinental Exchange 311326703342 (Enterprise-vs-Colo disambiguation -> Cooper), Boldyn Networks/Mobilitie 318223366892 (duplicate of master Boldyn 300402132682 -> R3).

Run health: GREEN

Errors: None. 4 HubSpot batch writes (10/10/10/9), 0 failures.
```

Run detail:

Today is Monday 2026-06-15; 120-day cutoff = 2026-02-15. Filter A (stale >=120 days, excl Flagged-for-deletion + MaiaEdge own): 0 records. Filter B (never-enriched + segment populated): 0 records (MaiaEdge own excluded in-query). A+B = 0 < 40, so Filter group C (rotation pre-spread) fired against the active not-yet-stale pool (3,384 records with last_enriched_date >= 2026-02-15). Pulled the 45 oldest-enriched (cohort 2026-02-24 -> 2026-05-01), sorted last_enriched_date ASC.

Of the 45: 4 standing holds carried (no action, no bump), 1 retry routed to D7 (no bump), 1 dedup deferred to R3 (no bump - FPT), and 39 well-briefed Other / Partner Target keepers re-stamped to 2026-06-15. Re-stamping these staggers their next 120-day due date from the late-September bunching window out to mid-October, smoothing the cliff per the Filter-C design.

Pre-score triage: 0 RE_ENRICH_FULL, 41 RE_ENRICH_LIGHT (39 PARTNER_KEEP/Other-keep re-stamps + Confluence retry + FPT defer), 4 standing holds (RE_ENRICH_DEFER-equivalent). No ICP records in the slice, so 0 Apollo (LIGHT path is Apollo-free; all keepers are stable, well-briefed non-ICP vendors / analysts / SIs / media / associations / non-fits with accurate prior briefs - classifications knowledge-confirmed unchanged, no segment flips possible). compute_tier is a no-op for all 39 (non-ICP segments are guarded out per tier-compute-spec Step A0; account_tier preserved). signal_heat = Cold written/backfilled on all 39 (null last_signal_date -> Cold; correct and complete for rep filtering).

39 keepers re-stamped (last_enriched_date 2026-06-15 + signal_heat Cold):

| Company | ID | Segment | Tier | Cohort date |
|---|---|---|---|---|
| NCTC | 319435694779 | Partner Target | tier_3 | 04-27 |
| Trident Communications | 318209570539 | Other | tier_5 | 04-27 |
| Arista Networks | 233124968132 | Other | tier_5 | 04-27 |
| Spirent | 193863998158 | Other | tier_5 | 04-27 |
| Sinch | 193906530034 | Other | tier_5 | 04-27 |
| Ultramobile | 318223234758 | Other | tier_5 | 04-27 |
| Santa Ynez Band of Chumash Indians | 320402313918 | Other | tier_5 | 04-27 |
| Salesforce | 193807389402 | Other | tier_5 | 04-27 |
| Fiber Gaming Network | 320364986071 | Partner Target | tier_5 | 04-27 |
| Gaichu Managed Services | 318231691995 | Other | tier_5 | 04-27 |
| Sterling and Wilson | 277439113953 | Other | tier_5 | 04-27 |
| Endeavor Business Media | 320388767457 | Partner Target | tier_5 | 04-27 |
| Telescope | 318231691994 | Other | tier_5 | 04-27 |
| TechVision Research | 193868315335 | Other | tier_5 | 04-27 |
| Ledger of earth | 319775490773 | Other | tier_5 | 04-27 |
| EPSGlobal | 319494358732 | Partner Target | tier_3 | 04-27 |
| Ciena | 320529755891 | Other | tier_5 | 04-28 |
| GSMA | 193910127306 | Other | tier_5 | 05-01 |
| NVIDIA | 314541086418 | Partner Target | tier_5 | 05-01 |
| Dell | 275154910936 | Partner Target | tier_5 | 05-01 |
| Versa Networks | 193807389412 | Other | tier_5 | 05-01 |
| InsidePacket | 193867595489 | Partner Target | tier_5 | 05-01 |
| Analysys Mason | 193867595498 | Other | tier_5 | 05-01 |
| Fujitsu | 193868315349 | Other | tier_5 | 05-01 |
| Bloomberg | 193906530018 | Partner Target | tier_5 | 05-01 |
| Frost & Sullivan | 193906530028 | Partner Target | tier_5 | 05-01 |
| Wipro | 193906530029 | Partner Target | tier_5 | 05-01 |
| Join Digital | 193910127309 | Partner Target | tier_5 | 05-01 |
| RAD | 193910127307 | Other | tier_5 | 05-01 |
| Omdia | 192886563562 | Other | tier_5 | 05-01 |
| Cognition | 192890159857 | Other | tier_5 | 05-01 |
| AppEx Networks | 192915752645 | Other | tier_5 | 05-01 |
| Cisco | 193856074470 | Other | tier_5 | 05-01 |
| Telecom Review Group | 193060405955 | Other | tier_5 | 05-01 |
| Denso | 193865438948 | Partner Target | tier_5 | 05-01 |
| SDxCentral | 193863998171 | Partner Target | tier_5 | 05-01 |
| Forrester Research | 193863998160 | Partner Target | tier_5 | 05-01 |
| Amphenol | 301878429405 | Partner Target | tier_5 | 05-01 |
| Capgemini | 301885614809 | Partner Target | tier_5 | 05-01 |

Not re-stamped (no date bump):

| Company | ID | Disposition |
|---|---|---|
| Confluence Research | 192890159856 | D7 handoff - 2nd consecutive re-verification failure (confluenceresearch.com.au unresolved). Other tier_5 left untouched. |
| FPT | 300724801211 | R3 dedup - duplicate of FPT Software 326715774698 (Enterprise/Outsourcing ICP). Merge into ICP record. |
| MMR Fiber / SouthWestern Power Group | 175221473010 | Standing hold (since 06-08) - entity-split surprise-ICP (mmrfiber.com wholesale dark fiber) -> R3/Cooper. |
| team.telstra.com | 316598423243 | Standing hold (since 06-05) - Telstra subdomain dedup stub -> R3 (primary 265926494953). |
| Intercontinental Exchange | 311326703342 | Standing hold (since 06-10) - Enterprise (Financial Services) vs Data Center Colo disambiguation -> Cooper. |
| Boldyn Networks (Mobilitie) | 318223366892 | Dedup - duplicate of master Boldyn 300402132682 -> R3. recent_news already flags the merge. |

Stamping policy: bumped last_enriched_date only on the 39 LIGHT PARTNER_KEEP / Other-keep re-stamps (definitive keeper confirmation). No bump on the 6 carried/handoff records. No recent_news staleness clears this run (no keeper had a stale last_signal_date populated).

Cross-routine coordination: ran after R1 (10am, wrote Jefferson Telecom ICP + 1 Flagged-for-deletion + 2 Tier 3 holds; no low_5069 handoff to R2 today). No HARD_DELETE evictions this run, so nothing feeds R4 (12pm) from R2 today.
