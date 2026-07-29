CRM Guardian - Stale Re-Enrichment - 2026-06-17 - 0 Tier 2 flagged, 1 new Tier 3 held (+6 standing carried)

Run summary: 40 candidates processed (39 written, 1 held) of 100 cap. FULL 0 / LIGHT 1 (Omada keep) / Filter-C pre-spread restamp 38 / DEFER 0. Tier 1: 0 / Tier 2: 0 / Tier 3: 1 new + 6 standing carried. Apollo: 0 used / 848 remaining (W25). Freshness: GREEN.

Today = 2026-06-17 (ET). 120-day cutoff = 2026-02-17. ISO week W25.

Trigger query:
- Filter A (last_enriched_date < 2026-02-17, excl "Flagged for deletion" + MaiaEdge own 124293230301): 0 records.
- Filter B (last_enriched_date NOT_HAS_PROPERTY + customer_segment populated, excl Flagged + MaiaEdge own): 1 record = Omada Technologies (328067841760).
- A+B = 1 < 40 -> Filter group C (rotation pre-spread) fired. Active not-yet-stale pool = 3,384. Pulled 45 oldest-enriched (2026-02-24 to 2026-05-04, sorted last_enriched_date ASC). 6 of the 45 are standing cross-routine Tier 3 holds (carried, no R2 action); 39 processable -> 38 re-stamped + 1 new Tier 3 hold (New Era Helium). Effective candidate count = 1 (B) + 39 (C) = 40, matching the pre-spread target of 40.

Bucket distribution: RE_ENRICH_FULL 0 / RE_ENRICH_LIGHT 1 (Omada) / Filter-C pre-spread 39 (38 restamp + 1 held) / MAYBE_RECLASSIFY 0 / RE_ENRICH_DEFER 0.

What needs Cooper's attention:
- [NEW Tier 3] New Era Helium (321159184060): the existing account_brief is factually wrong - it states "Eviction reason: oil and gas, fully out of MaiaEdge ICP scope" but the company has pivoted. Web-verified (Data Center Frontier, DataCenterDynamics, BusinessWire): New Era Energy & Digital (renamed from New Era Helium) acquired full control of the Texas Critical Data Center JV with Sharon AI - a 250MW (scaling toward a planned 1GW) net-zero AI data center campus in Ector County TX (Permian Basin), Phase 1 targeting ~Dec 2026, Phase 2 engineering initiated, hyperscaler talks ongoing. Recommendation: reclassify to Data Center Colo Provider / Greenfield (owner Ken Cunningham / TX-West - already correct). Held rather than auto-flipped because of (a) the entity rename and (b) the JV structure with Sharon AI (a NeoCloud/GPU operator) - the colo-vs-neocloud boundary and "which entity is the MaiaEdge target" both want a human / D7 call rather than an unattended swing from an eviction-flagged Other to ICP. NO HubSpot write made; record left at last_enriched_date 2026-05-04 so it stays in rotation and resurfaces.
- [LIGHT keep, borderline] Omada Technologies (328067841760): kept as Other (thin partner value). Portsmouth NH value-added IT solutions provider (data center / cloud / networking / security); web-verified as an IT integrator/reseller, not a carrier or telecom aggregator, so non-ICP. Conservative keep on a same-day R0-validated record. If Cooper would rather evict generic regional IT VARs outright, flag it and D7 / manual-review can action.
- 6 standing cross-routine holds carried (no R2 action) - see table below. WATCH: MMR Fiber (175221473010) + team.telstra (316598423243), both enriched 2026-02-24, cross 120d into Filter A ~2026-06-25; still blocked on R3 / Cooper dedup decisions.

Run health: GREEN

Errors: None.

---

Records written (39): 0 Apollo, 0 evictions, 0 segment changes.

LIGHT keep (1):

| ID | Name | Outcome | Writes |
|---|---|---|---|
| 328067841760 | Omada Technologies | PARTNER_KEEP - Other (NH IT-infrastructure VAR; web-verified non-ICP) | account_brief, signal_heat=Cold, last_enriched_date=2026-06-17 |

Filter-C pre-spread re-stamps (38): last_enriched_date=2026-06-17 + signal_heat=Cold backfill; tier no-op (non-ICP Partner Target / Other, compute_tier Step A0 guard). All well-briefed 2026-05-01 / 2026-05-04 ecosystem keepers.

322837059309 Advantech; 193868315350 Blue Planet; 319323798262 Neonetwork; 301878429391 Texas Instruments; 192899159801 Converge Digest (Dell'Oro); 319765072624 Telstar; 102980971224 Connectbase; 193853195980 Palo Alto Networks; 192888367830 Esther Tech; 193866877635 Infosys; 311383369428 SP8CEAI; 311377987271 ICF; 311381570291 Bolt Graphics; 292719764194 NEXSYS-ONE; 320761088757 Minnesota Telecom Alliance; 320761496260 New Mexico Exchange Carriers Group; 320761385696 WISPA; 316436023006 LiquidStack; 320656888527 NTCA; 316489401040 Bloom Energy; 320742094532 North Dakota Telephone Association; 320742046409 NECTA; 320747557591 Nevada Telecommunications Association; 320739388148 WSTA (Wisconsin); 320761496284 Wisconsin Statewide Telephone Cooperative Association; 320742162145 Telecommunications Association of the Southeast; 320747589323 Kentucky Telephone Association; 320745767672 Washington Independent Telecommunications Association (WITA); 320747589319 Illinois Rural Broadband Association; 320761438920 California Cable & Telecommunications Association (CCTA); 320763290317 Alaska Telephone Association; 320742046407 OCTA (Ohio); 320761349832 NRTC; 320733913834 Indiana Broadband and Technology Association; 320733913829 Arizona-New Mexico Telecommunications Association; 193867595503 Light Reading; 292755851984 TELFORCE GROUP LLP; 193867595494 ACG Research.

Held - NEW Tier 3 (1, no write / no bump):

| ID | Name | Reason | Route |
|---|---|---|---|
| 321159184060 | New Era Helium / New Era Energy & Digital | Stale "oil/gas eviction" brief contradicted by web-verified AI-DC Greenfield pivot (Texas Critical Data Center, 250MW AI campus, Ector County TX) | Cooper / D7 - recommend reclassify to Data Center Colo Provider / Greenfield |

Standing cross-routine Tier 3 holds carried (6, no R2 action; none Cooper-resolved since 06-16):

| ID | Name | Reason | Route |
|---|---|---|---|
| 175221473010 | MMR Fiber Solutions / SouthWestern Power | entity-split (fiber arm mmrfiber.com is a real Fiber Operator on the power-parent domain) | R3 / Cooper - WATCH: crosses Filter A ~2026-06-25 |
| 316598423243 | team.telstra.com | subdomain dedup stub | R3 - WATCH: crosses Filter A ~2026-06-25 |
| 311326703342 | Intercontinental Exchange (ICE) | Enterprise/Financial-Services vs Data-Center-Colo (2 sub-segments positive evidence, 0 deals) | Cooper |
| 318223366892 | Boldyn Networks (Mobilitie) | dup of master Boldyn 300402132682 | R3 |
| 192890159856 | Confluence Research | repeated R2 re-verification failures (no clear AU entity) | D7 |
| 300724801211 | FPT (fptsoftware.com) | dup of FPT Software 326715774698 (Enterprise/Outsourcing ICP); FPT AI Factory 303405064912 (fpt.com, NeoCloud) is a separate arm - do not merge | R3 |

Partial Enrichment held for next run: none.
Recent news cleared (stale): none (no FULL passes this run; Filter-C records are non-ICP keepers without signal narratives).
Legacy format pending backfill: none flagged this run.

Data-quality notes:
- LiquidStack (316436023006) and Bloom Energy (316489401040) carry a vestigial company_sub_segment = "AI Signals - colo" on a Partner Target parent (cooling / power tech vendors reclassified DCCP -> Partner Target on 2026-05-04). Harmless (Partner Target is not tier-computed); left as-is (minimal change on a re-stamp pass). Flag for optional hygiene clear.
- New Era Helium brief inconsistency surfaced + routed (see Tier 3 above).

Apollo: 0 credits used this run. Weekly W25: 2/850 consumed, 848 remaining. Sub-cap 50/run, used 0 of 50.
Cross-routine ledger F0B0AFSB9LN: 1 new Tier 3 hold appended + 6 standing re-confirmed; one Run-log row appended (status: success).
Delivery: quiet-on-success (no DM). This disk report + the canvas Run-log row are the record; the CRM Ops Daily Digest (4:45pm CT) surfaces it.
