CRM Guardian - Stale Re-Enrichment - 2026-06-05 - 0 Tier 2 flagged, 1 Tier 3 held

Run summary: 19/40 processed (re-stamped) · FULL pre-spread (Filter C) only; 0 genuine stale (A/B) · Tier 1: 19 re-stamps / Tier 2: 0 / Tier 3: 1 hold · Apollo: 0/850 used (sub-cap 50) · Freshness: GREEN

Context: Filter A (last_enriched_date < 2026-02-05, exclude Flagged-for-deletion + MaiaEdge own) = 0 records. Filter B (never-enriched + segment populated) = 0 net (MaiaEdge own filtered). A+B < 40 -> Filter group C (rotation pre-spread, added 2026-06-04) fired for the FIRST time to smooth the load curve toward the late-September 120-day cliff. Pulled the 40 oldest-enriched not-yet-stale active records (enriched 2026-02-17 to 2026-04-01) from a 3,352-active pool, sorted last_enriched_date ASC.

Pre-spread interpretation (first run, documented): all 40 candidates are already classified non-ICP "Other"/"Partner Target" references at tier_2-tier_5, high_90/medium_7089. The dominant, low-risk pre-spread action is re-stamping last_enriched_date to stagger the next rotation date, plus idempotent tier/heat recompute. Tier compute is a no-op for these Other records (no signals, no open deals, no modifiers). Heat is Cold for all (last_signal_date null/absent). Per the closing principle (default to NOT writing when uncertain; bad writes expensive), narrative enriched fields were NOT rewritten via unattended deep research on already-correct records. Records that are genuinely under-enriched (no account_brief AND opaque identity) were DEFERRED (no date bump) for a deliberate enrichment pass rather than have briefs fabricated or be hidden from rotation by a premature stamp - pre-spread explicitly yields and defers remainder.

Processed (19 re-stamped to 2026-06-05):
- Verified via web research + classification confirmed Other (account_brief written this run): Level 3 Communications (316528134904, legacy Lumen brand, LatAm assets divested to Cirion), Springfield Telecom Company (317039551165, fiber-deployment contractor/vendor), Comfone (316498875125, roaming/IPX interconnect hub), Highline (316561917659, Brazil neutral-host towerco).
- Adequately-enriched stable Other/Partner re-stamps (idempotent recompute + re-stamp): Cerebras (303850136251, Partner Target tier_1), Datum (271794566883), 5G Networks (277401440966), The Internet Centre (277240421112), Bresco Solutions (279409562319), Cloudflare (301953871560), Akamai (301883815671), Nokia (208195645177), SWIFT (297171485401), Telewave (318223234759), IPS Inc (318347064047), Autelecom (316210759368).
- Heat backfilled to Cold where field was missing (same re-stamp write): Senet (277399641811), Ocolo (318292777715), Helios Towers (319321790172), Autelecom (316210759368).

Tier 3 hold (no date bump):
- team.telstra.com (316598423243) - Telstra email/collab SUBDOMAIN artifact (no name, no country populated). Same dedup-stub pattern as us.ntt.net / g.softbank.co.jp. Duplicate of the Telstra master record. Routed to R3 Duplicate Accounts. No write.

What needs Cooper's attention:
- 1 Tier 3 hold: team.telstra.com subdomain dedup stub -> R3.
- 20 under-enriched "Other" micro-records DEFERRED (no bump) pending a deliberate field-completion pass. These were classified Other in a prior pass but lack account_brief + the 7 enriched fields; several may warrant re-validation: HGC (316558341873, hgcconstruction.com - name suggests construction co, possible misclassify), Associated Carrier Transport (316561917662, thin "network sourcing" identity), Clockwork.io (300724801216), LB Networks (174907029204), didXL (316621828846), Pai Telecom (316614767315), Speedflow (316621828848), HDTandem (316561917650), Bumblebee Networks (192882963141), Network Planning Solutions (316627226307), JapTel (316502492868), LATINO COMMUNICATIONS CORP (316614767309), MasNegocio (316522694359), WIT ONE (316561917653), Innovative Telecom (316560181993), ALCASAGAR (316627226302), UNO (316623621846), MMR Fiber / SouthWestern Power (175221473010), BNS Inc (316618313424), Global Convergence Solutions (316561917655). Recommend a targeted enrichment batch (R1-style) rather than recurring pre-spread defer. These remain available to the rotation (not stamped).

Legacy format pending backfill (last_signal_date null but recent_news populated; left alone per Step 14): Cerebras, Senet, Datum, 5G Networks, Nokia, SWIFT, Cloudflare, Akamai, Ocolo, IPS Inc.

Recent news cleared (stale): none (no record had last_signal_date >90d populated).

Partial Enrichment (gate failed): none.

Run health: GREEN

Errors: None. Both HubSpot batch writes 10/10 and 9/9 succeeded.
