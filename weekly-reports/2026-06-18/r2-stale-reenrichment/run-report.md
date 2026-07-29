CRM Guardian - Stale Re-Enrichment - 2026-06-18 - 3 Tier 2 flagged, 0 Tier 3 held (6 standing carryovers)

Run summary: 39/100 processed (LIGHT path only) · FULL 0 / LIGHT 39 / RECLASSIFY 0 / DEFER 0 · Tier 1: 36 (keeper re-stamps) / Tier 2: 3 (evictions) / Tier 3: 0 new · Apollo: 0 used / 848 remaining (W25 2/850) · Freshness: GREEN

Today = 2026-06-18 (ET). 120-day cutoff = 2026-02-18.
- Filter A (last_enriched_date < 2026-02-18, exclude Flagged-for-deletion + MaiaEdge own 124293230301): 0
- Filter B (never-enriched + customer_segment populated, exclude Flagged): 0
- A + B = 0 (< 40) -> Filter group C (rotation pre-spread) fired. Active not-yet-stale pool = 3,393. Pulled 45 oldest-enriched (2026-02-24 to 2026-05-04, sorted last_enriched_date ASC). 6 standing cross-routine holds at the front carried unprocessed; 39 keepers processed.

Bucket distribution: 0 RE_ENRICH_FULL (no ICP / blank-segment records in pool today), 39 RE_ENRICH_LIGHT (all Other / Partner Target at low tiers).

What needs Cooper's attention:
- 3 eviction Tier 2 -> Filter HubSpot Companies -> customer_segment = "Flagged for deletion": Activate (321173470912), United Networks (318097753795), Lantern Lab (321237115592).
- 0 new Tier 3 holds this run.
- 6 standing cross-routine holds carried (R3 / Cooper / D7 scope, no R2 action). WATCH: team.telstra (316598423243) + MMR Fiber / SouthWestern Power (175221473010), both enriched 2026-02-24, cross 120 days into Filter A on 2026-06-24 - still blocked on R3 / Cooper dedup decisions.
- 2 borderline Other records kept + re-stamped (Teal Communications 318097753794 IoT eSIM/MVNO software; Trellis Networks 318097753789 network design/build SI). Both telecom / network-adjacent so kept as Other partner-adjacent references rather than evicted in an unattended run; surfaced for a possible future Principle-7 (Other-vs-Flagged) review.

Run health: GREEN

Errors: None

---

## Detail: Segment changes (3)

```
| Account            | HubSpot ID    | Old segment | New segment           | Reason code  | Evidence (web-reverified, 0 deals)                                                        |
|--------------------|---------------|-------------|-----------------------|--------------|------------------------------------------------------------------------------------------|
| Activate           | 321173470912  | Other       | Flagged for deletion  | No ICP fit   | 501(c)(3) hard-tech science-commercialization fellowship (Cyclotron Road); not carrier infra, no ref value |
| United Networks    | 318097753795  | Other       | Flagged for deletion  | No ICP fit   | Healthcare managed-care network (Rx/dental/vision/hearing, 240k providers); name-confusion, not a network op |
| Lantern Lab        | 321237115592  | Other       | Flagged for deletion  | No ICP fit   | Strategic design / UX consultancy (2-10 emp); not carrier infra, no partner/competitive ref value          |
```

All 3 were parked in `Other` with migration-era "Eviction reason:" briefs but never flagged. Re-verified non-ICP, non-partner via web_search; 0 associated deals (customer-protection check passed). Reclassified to Flagged for deletion per Operating Principle 7 + RE_ENRICH_LIGHT eviction lever. `flagged_for_deletion_reason` set in same write; `last_enriched_date` bumped to 2026-06-18 (eviction = resolution). signal_heat untouched (eviction supersedes).

## Detail: Keeper re-stamps (36)

last_enriched_date -> 2026-06-18, signal_heat = Cold (backfill). Tier no-op (non-ICP Other / Partner Target; compute_tier guards non-ICP). No account_brief churn (existing briefs current and accurate).

34 Partner Target ecosystem references (state/regional broadband + telecom trade associations: PTA, TANE, TAM, CVTMA, NYSTA, ACA Connects, TN Broadband, OH Telecom, BCAP, FBA, WTA, INCOMPAS, UT Rural Telecom, OR Telecom, CalCom, WY Telecom, ID Telecom Alliance, Broadband MT, SCTBA, IN Rural Broadband, NC Broadband Coop, GA Telephone, LA Telecom, AR Telecom, FL Internet & TV; strategic power/chip/modular-DC vendors: X-Energy, TerraPower, Oklo, Intel, Northstar Enterprise + Defense; advisory/software partner refs: razorflow, KARAGREY, CTOS, Solutional).
2 Other partner-adjacent kept (Teal Communications, Trellis Networks - see Cooper note above).

## Detail: Standing cross-routine holds carried unprocessed (6, no bump)

```
| Account                         | HubSpot ID    | last_enriched | Owner-routine | Issue                                                            |
|---------------------------------|---------------|---------------|---------------|-----------------------------------------------------------------|
| team.telstra                    | 316598423243  | 2026-02-24    | R3            | Telstra subdomain dedup stub. WATCH: -> Filter A 2026-06-24      |
| MMR Fiber / SouthWestern Power  | 175221473010  | 2026-02-24    | R3 / Cooper   | Entity-split (open-access dark-fiber arm under power parent). WATCH: -> Filter A 2026-06-24 |
| Intercontinental Exchange (ICE) | 311326703342  | 2026-04-01    | Cooper        | Enterprise/Financial-Services vs Data-Center-Colo disambiguation |
| FPT                             | 300724801211  | 2026-04-27    | R3            | Dup of FPT Software 326715774698 (Enterprise/Outsourcing ICP)    |
| Confluence Research             | 192890159856  | 2026-04-27    | D7            | 2x re-verification failure; .com.au resolves to no clear entity  |
| Boldyn Networks (Mobilitie)     | 318223366892  | 2026-04-27    | R3            | Dup of master Boldyn 300402132682                                |
```

## Detail: Partial Enrichment - held for next run

None. All 39 processable records reached a definitive resolution (re-stamp keeper or eviction).

## Apollo

0 credits used. RE_ENRICH_LIGHT path is Apollo-free; no RE_ENRICH_FULL records today. Sub-cap 50, used 0 of 50. W25 weekly: 2/850, 848 remaining.

## Operational note

bash-mount view of weekly-reports/apollo-budget.json showed the file truncated at line 191 (the known sandbox-mount stale-JSON illusion). Host file verified VALID and complete (207 lines, through the 2026-06-18 R1 entry) via the file Read tool before any write. File was NOT "repaired" - it was already healthy. Budget history entry appended host-side.
