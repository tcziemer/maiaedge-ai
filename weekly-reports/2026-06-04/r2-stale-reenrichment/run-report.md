CRM Guardian - Stale Re-Enrichment - 2026-06-04 - 0 Tier 2 flagged, 0 Tier 3 held

Run summary: 1/100 processed · 1 RE_ENRICH_FULL (0 LIGHT / 0 RECLASSIFY / 0 DEFER) · Tier 1: 1 / Tier 2: 0 / Tier 3: 0 · Apollo: 0 used / 50 remaining (sub-cap), W23 weekly 0/850 · Freshness: GREEN (steady state; 1 never-enriched backlog record)

What needs Cooper's attention:
- Broadstar (323981908725) territory/owner discrepancy: HQ state Florida = East = Tim Lieto per territory model, but record is owned by Ken Cunningham (162339176) who is actively running the open deal "Broadstar - New Logo" ($10k, presentationscheduled) + active POC. Owner PRESERVED to avoid disrupting an active sales motion. Flag for your call on whether to leave with Ken or re-territory to Tim Lieto.
- R3 dedup hold for Broadstar can be CLEARED: prior canvas hold (2026-05-22 R1) flagged Broadstar (323981908725) as a possible duplicate of 193867595510. That sibling record is now cleanly "Gigabit Fiber" (gigabitfiber.com, Dallas TX) and Broadstar (broadstar.com, West Palm Beach FL MDU FTTH) is a DISTINCT, legitimate company. Not a duplicate. R3 can drop the hold.

Run health: GREEN

Errors: None

---

Detail - record processed (RE_ENRICH_FULL):

| Company | ID | Path | Action | Confidence | Tier | Date bumped |
|---|---|---|---|---|---|---|
| Broadstar (broadstar.com) | 323981908725 | RE_ENRICH_FULL | Enrichment completion + confidence upgrade | manual_review_required -> high_90 | tier_2 (unchanged) | YES (2026-06-04) |

Broadstar detail:
- Identity/MISDOMAIN: PASS. broadstar.com = Broadstar (West Palm Beach FL MDU fiber/IPTV/VoIP provider, est. 1994). Matches HubSpot name. Confirmed distinct from Gigabit Fiber (TX, 193867595510).
- Classification: Fiber Operator / Regional CLEC - Fiber operator (UNCHANGED - correct). manual_review_required was a stale artifact of the now-resolved dedup naming confusion, not genuine multi-classification ambiguity (F.3 No-Default-Manual-Review). Upgraded to high_90.
- 7 enriched fields: account_brief refreshed (FL/NJ MDU FTTH, 10G OcNOS upgrade, active POC); geographic_focus, infrastructure_profile (Route Miles: Small (<1K)), hyperscaler_proximity (None Known), fabric_provisioning_approach (manuallegacy_processes), provisioning_landscape written. recent_news_or_trigger_event left empty (no verified dated public signal this run; Signal Scan owns the field - avoided creating a narrative/last_signal_date inconsistency).
- Tier 4 compute: tier_2 retained. Base Regional CLEC + open-deal modifier (open deal "Broadstar - New Logo" at presentationscheduled, past appointmentscheduled) supports elevated tier. hs_is_target_account not set, so tier write permitted; idempotent (no change).
- signal_heat: Hot (unchanged) - correct per compute_signal_heat (associated open deal past appointmentscheduled). Not bumped, no note needed.
- Customer protection: open deal at presentationscheduled (NOT contractsent+, NOT closedwon) - no hard stop. No segment change proposed, so no cascade and no downgrade-protection trigger.
- Owner: PRESERVED (Ken 162339176) - see Cooper-attention note above.
- last_enriched_date: stamped 2026-06-04 (Completeness Gate PASS - all mandatory enriched + classification fields present).

No Tier 3 holds. No evictions. No segment transitions. No partial-enrichment carryovers.

Pool: Filter A (last_enriched_date < 2026-02-04, exclude Flagged-for-deletion + MaiaEdge own) = 0 records. Filter B (never-enriched + segment populated, exclude Flagged-for-deletion + MaiaEdge own) = 1 record (Broadstar). Filter C (rotation pre-spread) NOT triggered for top-up but pool < 40 - note: only 1 genuine A/B candidate existed; pre-spread would top up to 40, however the active population is uniformly enriched < 120 days (May migration + Mass Re-Enrichment Sweep) and the single A/B record was the only outstanding backlog item. Processed it; no pre-spread remainder needed (population already evenly distributed pre-September cliff per prior R2 audits). Apollo not consumed (firmographics current; state/country populated).

Cross-routine ledger: R2 Tier 3 carryover queue confirmed EMPTY at run start (re-verified clean since 2026-05-25 R2 audit). Standing canvas holds (gatco.net, columbus-networks, g.softbank.co.jp, us.ntt.net, Broadstar-as-R3-dedup) are R0/R1/R3 scope; the Broadstar R3 dedup hold is now resolvable (see note). 0 new R2 Tier 3 holds appended.
