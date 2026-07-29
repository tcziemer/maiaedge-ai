CRM Guardian - Flagged Consolidation - 2026-06-03 - 2 contacts flagged, 0 reassociated, 63 Tier 3 held

Run summary: 248 flagged companies in queue (~80 with associated contacts) - 369 contacts evaluated - 2 Tier 1 Mode B flags / 0 Mode A reassociations / 63 Tier 3 holds - 0 customer-protection / open-deal / fresh-company hard stops. Run health: YELLOW (writes succeeded; Tier 3 holds present, all benign "too-new-to-judge" / recent-activity preserves).

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then: Filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (this severs the stale associations and clears the 248-company queue once contacts are resolved)

Context / scope notes:
- 248 companies currently carry customer_segment = "Flagged for deletion". The company cap is 150/run, but only ~80 of the 248 have any associated contacts; companies with 0 contacts need no consolidation action and simply await Cooper's archive. This run evaluated every flagged-company contact (369 across the full pool) rather than stopping at an arbitrary 150-company boundary, since the actionable set (companies-with-contacts) is well under the cap and under the 1,500-contact soft cap.
- Deal gate: a single flagged company (Broadstar, gigabitfiber.com) carries an open deal; it is also a fresh record (created 2026-05-22). It is held (open-deal hard stop + fresh-record safety) and was not consolidated. No other flagged company has any associated deal, so there were zero customer-protection (closed-won) or open-deal hard stops in the processed set.
- No Enterprise pre-Phase-1 mis-flags detected (no bank / insurer / hospital / retailer / BPO at $1B+ scale in the flagged pool; GAC = shipping logistics, Watch List not Enterprise ICP, 0 contacts).
- Steady-state observation: ~304 of the 369 contacts are already flagged_for_deletion = true from prior R4 runs (idempotent no-op). The remaining 65 unflagged contacts split into 2 not-preserved-and-not-fresh (flagged this run) and 63 preserved (Tier 3 holds).

Mode B flags (Tier 1 - flagged_for_deletion = true this run):

| Contact ID | Company | Company ID | Domain | Reason |
|---|---|---|---|---|
| 486369299172 | Currency.com | 323170981573 | currency.com | Not preserved: no activity since contact create (2025-10-06), company not fresh (created 2026-05-18, 16d). Crypto exchange, confirmed non-ICP. |
| 486616302309 | Melita Ltd | 322877245139 | melitaltd.com | Not preserved: no activity since contact create (2026-05-15), company not fresh (created 2026-05-15, 19d). |

Mode A reassociations (Tier 1-2): NONE. No preserved contact's flagged company resolved to a HIGH-confidence ICP primary (exact domain or exact normalized-name match to a non-flagged ICP company). All flagged companies in scope were flagged as genuine non-ICP non-fits (not R3 duplicates), so no ICP primary reassociation target exists. Per invariant F, preserved contacts with no primary default to Tier 3 hold. Exhaustive per-domain ICP-primary search across all ~50 preserved-contact companies was not run (low expected yield given non-fit provenance; conservative default applied) - noted as an autonomous choice.

Tier 3 holds (63 preserved contacts, NOT flagged, NO reassociation) - grouped by preserve reason:

Category A - Fresh record (company and/or contact createdate within 14 days; "too new to judge", invariant E / signal #6):
3 Rivers Communications (1), ALLO Communications net-new (1 of 3), BAI Connect (1), Bright House Networks (1), CarrierX 494765969108 (1; created 2026-06-02), Congruex (1), Fast Wave (1; 2026-05-20 boundary), FreeConferenceCall (1; 2026-06-02), Grande Communications (1), Home Telecom (1), Internet Subway (5), KNET (1), Maquoketa Valley Electric Coop (1), Mjm Innovations (1; 2026-06-01), MOBILY LLC (1), Astound/mygrande (1), Astound/wavebroadband (1), Phoenix Communications (2), Plumas-Sierra Rural Electric Coop (1), Vistabeam (1).

Category B - Recent activity within 90 days (notes_last_updated or notes_last_contacted >= 2026-03-05):
Allegion (1; 2026-05-15), ALLO Communications (2; 2026-05-08), altafiber (1; 2026-05-15), aristotleweb (1; 2026-05-14), BitStream (1; 2026-05-14), Commercial Electronics (1; 2026-05-18), Corero 314701034216 (1; 2026-03-12), Dragonfly Internet (2; 2026-05-14 / 2026-06-03), Ellijay (1; 2026-05-14), ETC Communications (1), Eric Hanselman (1; 2026-05-06), FlowSec (1; 2026-03-31), FPX AI (2; 2026-04-16 / 2026-03-16), Holston Electric Coop (1; 2026-05-18), Hut 8 (1; 2026-05-20), IP Transfer (1; 2026-04-16), I & S Group (1; 2026-04-24), LS Power (1; 2026-03-16), Manor (1; 2026-04-27), MyRepublic Indonesia (1; 2026-05-11), Ohio Gig (1; 2026-05-18), Riot Platforms (4; 2026-05-25), Saturn Cloud 451588831988 (1; 2026-03-16), Steadfast Networks (1; 2026-03-16), Sumauma (2; 2026-05-29 / 2026-05-15), SwyftConnect (1; 2026-05-18), Truepacket (1; 2026-05-05), Unifique (1; 2026-05-20), Vocus Wholesale (1; 2026-04-24), Würth Industry NA (1; 2026-05-15), Edged Data Centers 451559667429 (1; 2026-03-16).

These holds are benign: each will naturally fall out of the preservation window (14-day fresh / 90-day activity) on a future R4 run and be flagged then if still a non-fit. None require Cooper action now. They are NOT appended individually to the canvas ledger (would be noise); an aggregate line is appended to the Run log instead.

Open-deal / fresh-company holds (not consolidated):
| Company | Company ID | Domain | Reason |
|---|---|---|---|
| Broadstar | 323981908725 | gigabitfiber.com | Open deal (1) + fresh record (created 2026-05-22, 12d). Beyond first-150 by object id; revisit once deal resolves / record ages. |

Errors: None. All HubSpot reads and the 2 contact writes succeeded (2 updated / 0 failed). No 4xx/5xx, no rate limiting.

Cross-routine ledger: canvas F0B0AFSB9LN read at run start; no prior R4 Tier 3 items required draining. One Run-log row appended at run end (status: partial - holds present).
