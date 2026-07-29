CRM Guardian - Stale Re-Enrichment - 2026-06-10 - 1 Tier 2 flagged, 1 Tier 3 held

Run summary: 40/100 processed (Filter-C pre-spread) · FULL pre-spread re-stamp 38 / EVICTION 1 / Tier 3 hold 1 / deferred 3 · Tier 1: 0 / Tier 2: 1 / Tier 3: 1 · Apollo: 0/850 (sub-cap 50, used 0) · Freshness: GREEN

What needs Cooper's attention:
- 1 Tier 3 hold (no write): Intercontinental Exchange (ice.com, 311326703342). Currently Other / tier_3 / blank sub-segment, brief flags "Borderline ICP fit". Web-confirmed: operates Tier-4 data centers in Mahwah NJ + Basildon UK and runs the SFTI / ICE Global Network as colocation + connectivity for trading firms. Passes the Enterprise / Financial Services gate ($9B+ revenue, 3+ DCs, in-house network engineering, FinServ vertical) but ALSO exhibits Data Center Colo Provider behavior (sells colo + fabric to its trading ecosystem). Two sub-segments carry positive evidence; 0 associated deals (no deal protection). Recommend disambiguation: Enterprise / "Financial Services - Enterprise" vs "Data Center Colo Provider". Held rather than auto-flipped per conservative principle (tier_3 record, genuine ambiguity).
- 1 Tier 2 eviction: Novus (novusint.com, 316285596350) -> Flagged for deletion (No ICP fit). Wrong-entity enrichment caught by the diff check. Filter HubSpot Companies -> customer_segment = "Flagged for deletion".
- 2 standing R3 Tier 3 holds carried forward (not R2 scope): MMR Fiber Solutions (175221473010, surprise-ICP entity-split) + team.telstra.com (316598423243, Telstra subdomain dedup). Awaiting R3 / Cooper.

Run health: GREEN

Errors: None. (Canvas read returned oversized/connector-flaky on first attempt; Run-log row appended best-effort - see Cross-routine ledger note.)

---

Trigger query (today 2026-06-10, 120-day cutoff 2026-02-10):
- Filter A (last_enriched_date < 2026-02-10, active, exclude MaiaEdge own): 0
- Filter B (never-enriched + customer_segment populated, active): 0 net (only MaiaEdge own 124293230301, hard-stopped)
- A+B = 0 < 40 -> Filter group C (rotation pre-spread) fired. Active pool with last_enriched_date >= 2026-02-10 = 3,411. Pulled the 45 oldest-enriched, sorted last_enriched_date ASC. Skipped 2 standing R3 Tier 3 holds, processed 40 (cap), deferred 3 newest (SES / Huawei / Kyndryl, return next run).

Pre-spread rationale: the 2026-04-01 cohort comes due (120 days) ~2026-07-30. Re-stamping today staggers their next due-date to ~2026-10-08, smoothing load away from the late-September migration cliff. Real rotation work, not fabricated.

Bucket distribution: RE_ENRICH_FULL pre-spread 40 (38 re-stamp + 1 eviction + 1 Tier 3 hold). No RE_ENRICH_LIGHT, no MAYBE_RECLASSIFY, no genuine stale (A/B) candidates.

---

EVICTION (Tier 2, date bumped - eviction is a resolution)

| Company | ID | Old segment | Action | Reason |
|---|---|---|---|---|
| Novus -> Novus International | 316285596350 | Other / tier_4 | Flagged for deletion | No ICP fit. novusint.com + state Missouri = Novus International, an animal health/nutrition company (St. Charles MO, owned Mitsui/Nippon Soda). Prior brief mis-described the unrelated Vancouver ISP Novus Entertainment (novusnow.ca). Re-briefed; name corrected to "Novus International". |

TIER 3 HELD (no write, no date bump)

| Company | ID | Current | Recommendation |
|---|---|---|---|
| Intercontinental Exchange | 311326703342 | Other / tier_3 / blank sub-segment | Reclassify after Enterprise-vs-Colo disambiguation. Passes Enterprise/FinServ gate; also colo-like (SFTI). 0 deals. |

PRE-SPREAD RE-STAMPS (38 records, last_enriched_date -> 2026-06-10; tier/heat no-op, all Other/Partner tier_4-5, heat Cold)

316278520567 Vox Communications · 316298284742 9DOT · 316173995710 Breezeline Business · 316179388106 Titan Networks (+infra fill) · 316280383163 Omnispace (+infra fill) · 316205322953 Total Play Telecom · 316298284740 Travelers Telecom · 316296477395 Western Utility · 316179388105 Telespazio (+infra fill) · 316298283759 Linxa (+infra fill) · 316303584987 Associated Carrier · 264270693068 Cloverleaf Infrastructure · 316283788024 Teleports · 316282051273 Hylan (+infra fill) · 316310831803 Maktech Telecom (+infra fill) · 316133717740 Fibracem (+infra fill) · 316224665283 Mawingu Networks · 316296615625 Konnexx Services (+infra fill) · 316305389271 Unity Communications · 316298283757 Novatel (+infra fill) · 316224514753 Orca Wave · 316179388109 Declaration Networks · 316171336387 FAST Global Solutions · 316319849199 poa! internet · 316305389266 Via Communications · 300403571425 Related Digital · 320873011950 Intermedia · 316205325016 Riedel · 320875170516 MP Nexlevel (+infra fill) · 316285596351 Squan · 316303584978 Lightriver · 316205322954 Truconnect · 316210759366 International Data Center Authority · 316196415204 FiberSense · 316224514755 Wireless Logic · 316212615885 Lynk Global · 316171331313 APTelecom · 316278522610 Alibaba Group

Notes:
- 10 records had blank infrastructure_profile -> filled "None Identified" + fabric_provisioning_approach "none_identified" to satisfy the Non-ICP Completeness Gate (Titan, Omnispace, Telespazio, Linxa, Hylan, Maktech, Fibracem, Konnexx, Novatel, MP Nexlevel).
- Legacy-format / pending-backfill (left alone per Step 14): Cloverleaf Infrastructure + Related Digital carry a populated recent_news_or_trigger_event with null last_signal_date (pre-2026-05-28 records). Left unchanged; backfill task will reconcile.
- Deferred to next R2 (cap 40 reached): SES (316179439352), Huawei (302088379095, tier_1/Other), Kyndryl (302186294978, tier_2/Other - worth an MSP-vs-Other look next pass).

HubSpot writes: 4 batches (10 / 10 / 10 / 9), all updated, 0 failed. Apollo: 0 credits.
