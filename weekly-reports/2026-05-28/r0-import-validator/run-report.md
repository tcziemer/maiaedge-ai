# R0 Import Validator - 2026-05-28 Run Report

**Cadence:** Daily 9am CT M-F
**Trigger query window:** `createdate >= 2026-05-27T14:00:00Z` (24h rolling, ET-anchored)
**Run health:** GREEN
**Apollo credits:** 0 (Apollo-free routine)

---

## Run summary

- **Candidates returned by trigger query:** 1
- **Processed:** 1
- **Buckets:** 1 MATCH + 0 MISDOMAIN + 0 RENAMABLE + 0 HARD_FLAG + 0 DEAD_DOMAIN + 0 AMBIGUOUS (new)
- **HubSpot writes:** 1 (signal_heat=Cold default)
- **Errors:** 0
- **Tier 3 carryovers re-checked:** 2 (both still pending)

---

## Cross-routine ledger - Carryover drains

Pre-flight read of canvas `F0B0AFSB9LN`. Two R0 Active Tier 3 holds from 2026-05-27 re-evaluated against current HubSpot state.

| HubSpot ID | Name | Domain | hs_lastmodified | Cooper action since hold? | Decision |
|---|---|---|---|---|---|
| 324524875475 | (empty) | gatco.net | 2026-05-26 15:18 UTC | None | **CARRY** - fresh web_search still returns no clear public-entity match (GATCO Fine Bathware, GATCO Global UK, GATS Telecom India, GETCO Telecom Bangladesh - none unambiguously the registrant). Tier 3 hold preserved. |
| 324597786339 | columbus-networks | finetechnologies.co | 2026-05-26 19:10 UTC | None | **CARRY w/ context update** - Columbus Networks rebranded to Liberty Networks under Liberty Latin America (canonical `libertynetworks.com`). finetechnologies.co serves an unrelated Florida MSP (IT services / Brooksville-Spring Hill). Recommended interpretation: MISDOMAIN, redomain to `libertynetworks.com`. Direction still technically ambiguous until Cooper confirms the import intent. |

Both holds remain on the Active Tier 3 queue. No automated rewrites performed - directional ambiguity preserves the rule "AMBIGUOUS / Tier 3 - let Cooper decide" per R0 workflow.

---

## Candidates this run

### 324636275403 - Umniah - umniah.com

| Field | Value |
|---|---|
| HubSpot name | Umniah |
| Domain | umniah.com |
| Website | https://www.umniah.com |
| Industry | TELECOMMUNICATIONS |
| Country | Jordan |
| State | Irbid |
| HubSpot owner | 159350430 (Tim Ziemer, International) |
| createdate | 2026-05-27T17:37 UTC |

**Bucket:** MATCH (HIGH confidence).

**Evidence:**
- web_search "umniah.com" + Wikipedia + jordanict.com + Umniah's own about-us page consistently identify Umniah as a Jordanian mobile network operator.
- Founded 2004, GSM operations launched 2005. Subsidiary of Bahrain-based Batelco (96% ownership acquired 2006 for $415M).
- ~3M subscribers (Jordan's third-largest MNO).
- First operator to commercially launch 5G in Jordan (2023; Irbid, Zarqa, Amman, Aqaba).
- Offers postpaid + prepaid mobile, FTTH internet, 5G, smart home, financial / entertainment services.
- Operates Jordan's first Tier III Uptime-Institute-certified data center (colocation facility).
- 2+ independent sources (Wikipedia + jordanict.com + Umniah's own site) - HIGH confidence.

**Likely ICP path (R1 to confirm at 10am CT):** Network Operator (Tier 2 / VNO) for the mobile side; possible cross-classification with Fiber Operator given the FTTH footprint and Tier III colo. Tim Ziemer ownership is consistent with International territory placement.

**Action taken:**
- `signal_heat = Cold` (new-record default per R0 workflow - no signal history yet; idempotent; TitleCase per HubSpot enum).
- No other writes. `last_enriched_date` left blank for R1 to enrich at 10am CT.

---

## New Tier 3 holds added this run

None.

---

## Carryover Tier 3 holds (still active going into next run)

| date_first_surfaced | HubSpot ID | Name | Domain | Why held |
|---|---|---|---|---|
| 2026-05-27 | 324524875475 | (empty) | gatco.net | No clear public-entity match. Fresh web_search 2026-05-28 returned the same unrelated candidates (GATCO Fine Bathware, GATCO Global UK, GATS Telecom India, GETCO Telecom Bangladesh). Cooper to confirm correct entity or archive. |
| 2026-05-27 | 324597786339 | columbus-networks | finetechnologies.co | HubSpot slug "columbus-networks" identifies Columbus Networks (now rebranded Liberty Networks under Liberty Latin America; canonical libertynetworks.com). Domain finetechnologies.co serves an unrelated Florida MSP. Recommended MISDOMAIN to libertynetworks.com, but direction still ambiguous - Cooper to confirm import intent. |

---

## Apollo budget

- Consumption this run: **0 credits**
- Budget remaining (ISO week 22 / 2026): unchanged
- R0 is intentionally Apollo-free.

---

## Run health

GREEN. 0 errors, all writes succeeded, single MATCH candidate processed cleanly. Tier 3 carryovers re-evaluated; nothing newly added; nothing drained (no Cooper action since prior surfacing).
