CRM Guardian - Import Validator - 2026-06-02 - 0 domain-corrected, 2 renamed, 0 flagged, 4 held (2 new, 2 carryover)

Run summary: 9 records scanned, buckets = 5 MATCH / 2 RENAMABLE(HIGH) / 2 Tier 3 (new) / 0 MISDOMAIN / 0 HARD_FLAG / 0 DEAD_DOMAIN, 7 HubSpot writes, 0 errors.

What needs Cooper's attention:
- 4 Tier 3 holds active (2 new this run, 2 carryover) - see Tier 3 table below. None are auto-flag candidates; all are name-vs-domain ambiguity / probable duplicates of existing major-carrier records.
- 0 hard-flagged companies this run.
- 0 medium-confidence corrections to verify (both renames are HIGH confidence).
- FYI (not an R0 action): Mjm Innovations (mjminnovations.com) is a real transit fare-collection software vendor, name matches domain so it passed MATCH, but it has no ICP path - expect R1 to evict it via the LIKELY_NON_ICP (Path gamma) Apollo-free route.

Run health: YELLOW (all writes succeeded; 4 Tier 3 holds present).

Errors: None fatal. Two ledger-canvas caveats (best-effort, non-blocking): (1) the canvas read returned an oversized payload (~696K chars) and was parsed off-disk via grep for R0 items - no abort. (2) The R0 2026-06-02 Run-log + Tier 3 block double-applied: the first `slack_update_canvas` append returned a transient "connector not responding" but had in fact applied server-side, and the retry appended a second identical block. A tombstone note was written over the first copy's header explaining the duplicate and pointing to the canonical block; full removal was abandoned because each section replace regenerates downstream section IDs and the Slack connector went flaky mid-cleanup. The duplicate is benign (same date/routine/HubSpot IDs; the CRM Ops Daily Digest dedupes against HubSpot ground truth). HubSpot writes were unaffected. Not a hard failure - no Slack ping sent.

---

## MATCH (5) - signal_heat=Cold default written, last_enriched_date left blank for R1 (10am CT)

| HubSpot ID | Name | Domain | Owner | Entity at domain (web_search) | Confidence |
|---|---|---|---|---|---|
| 325339396848 | Optage | optage.co.jp | Tim Z (Intl) | OPTAGE Inc - Japanese fiber/telecom operator (Kansai Electric / former K-Opticom). Name matches domain. | HIGH |
| 325326814914 | GetOnward | getonward.com | Ken (West) | Onward (formerly Inyo Networks) - California/Nevada fiber-optic ISP; runs municipal broadband partnerships (Rancho Cucamonga, OntarioNet, Culver Connect). Brand "Get Onward" matches domain. | HIGH |
| 325323215608 | Digital Fortress Data Centers and Colocation | dfcolo.com | Ken (West) | Digital Fortress - Seattle/Washington colocation + data center provider. Name matches domain (dfcolo = Digital Fortress Colo). | HIGH |
| 325339396851 | Mjm Innovations | mjminnovations.com | Tim Lieto (East) | MJM Innovations - Baltimore MD transit fare-collection / transportation management software vendor (11-50 emp). Name matches domain. Non-ICP; deferred to R1 eviction. | HIGH |
| 325333996232 | Telia | teliacompany.com | Tim Z (Intl) | Telia Company - Nordic Tier 1 carrier/telecom (Sweden). Name matches domain. | HIGH |

## RENAMABLE HIGH (2) - renamed + account_brief written, last_enriched_date left blank for R1

| HubSpot ID | Old name | New name | Domain | Owner | Rationale |
|---|---|---|---|---|---|
| 325339396852 | (blank) | Plumas-Sierra Rural Electric Cooperative | psrec.com | Ken (West) | Imported with no name. Domain psrec.com serves the Plumas-Sierra cooperative (member-owned electric utility; subsidiary Plumas-Sierra Telecommunications operates a fiber-optic broadband network, won ~$67M across 11 grants for rural fiber). Likely cooperative Fiber Operator ICP. |
| 325323216629 | (blank) | GSL Networks | gslnetworks.com.au | Tim Z (Intl) | Imported with no name. Domain gslnetworks.com.au serves GSL Networks Pty Ltd (trading as Global Secure Layer) - Australia-HQ IP transit / network infrastructure provider, global fibre backbone AS137409, inline DDoS mitigation + Ethernet + colocation. Likely Network Operator ICP. |

## Tier 3 held - NEW this run (2) - no write, surfaced for Cooper / R3 dedup

| Date first surfaced | HubSpot ID | Name | Domain | Owner | Why held |
|---|---|---|---|---|---|
| 2026-06-02 | 325335795443 | (blank) | g.softbank.co.jp | Cooper | No-name carrier subdomain of the SoftBank group domain. Recurring import-collision pattern. Existing SoftBank entity in CRM (SoftBank AI Cloud 324007728852, softbank.jp, NeoCloud) plus the prior 2026-05-20 "SoftBank Corp" R0 drain make direction ambiguous - likely a duplicate. Held for Cooper / R3 dedup rather than auto-renamed into a duplicate. |
| 2026-06-02 | 325335796410 | (blank) | us.ntt.net | Cooper | No-name subdomain = NTT Global IP Network (GIN) backbone. Near-duplicate of existing NTT record (277437319928, global.ntt, Network Operator Tier 1 Carrier) and related to NTT Global Data Centers (133486361310, ntt.com). Held for R3 dedup rather than auto-renamed into a duplicate. |

## Tier 3 held - CARRYOVER (2) - re-checked, both still unactioned by Cooper, carried forward

| Date first surfaced | HubSpot ID | Name | Domain | Why held | Status this run |
|---|---|---|---|---|---|
| 2026-05-27 | 324524875475 | (blank) | gatco.net | No clear public-entity match; candidates diverge (GATCO Fine Bathware, GATCO Global UK, GATS Telecom, GETCO Telecom). | CARRY - record unchanged (no name, no segment, blank last_enriched_date). |
| 2026-05-27 | 324597786339 | columbus-networks | finetechnologies.co | Directional ambiguity: slug "columbus-networks" matches Columbus Networks (now Liberty Networks) but domain finetechnologies.co serves an unrelated Florida MSP (MISDOMAIN vs RENAMABLE unresolved). | CARRY - record unchanged. |

---

Idempotency: per E, no last_enriched_date stamped on any record this run (no HARD_FLAG/DEAD_DOMAIN eviction occurred). All 9 candidates either MATCH/RENAMABLE (R1 picks up at 10am CT) or Tier 3 hold. The 24h createdate window prevents reprocessing tomorrow.

Apollo: 0 credits (Apollo-free routine).
web_search: 4 searches (GetOnward, MJM Innovations, Plumas-Sierra, GSL Networks). Optage / Telia / Digital Fortress identified from prior knowledge of major operators; no search needed.
