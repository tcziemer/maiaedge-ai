# R0 Import Validator - 2026-05-27 Run Report

**Schedule:** Daily 9:00 AM CT M-F (cron `0 14 * * 1-5` UTC)
**Runtime:** 2026-05-27 ~14:05 UTC (~9:05 AM CT)
**Status:** GREEN - all writes succeeded; 2 Tier 3 holds surfaced

---

## Trigger Query

- objectType: companies
- filters: `createdate GTE 1779804299029` (2026-05-26 14:04 UTC) AND `last_enriched_date NOT_HAS_PROPERTY` AND `customer_segment NEQ "Flagged for deletion"`
- sort: `createdate ASCENDING`
- limit: 100

**Total matching:** 109
**Processed this run:** 100 (cap)
**Deferred to next run:** 9 (will be picked up at tomorrow's 9 AM CT fire)

---

## Bucket Summary

| Bucket | Count | Action |
|---|---|---|
| MATCH | 92 | `signal_heat = Cold` default (idempotent on existing) |
| HARD_FLAG (HIGH) | 4 | `customer_segment = "Flagged for deletion"` + `last_enriched_date` + audit brief |
| RENAMABLE (HIGH) | 2 | Rename + audit brief + `signal_heat = Cold` |
| MISDOMAIN | 0 | - |
| DEAD_DOMAIN | 0 | - |
| AMBIGUOUS / Tier 3 | 2 | Surface to Cooper; no write |

**Writes attempted:** 98 - **Writes succeeded:** 98 - **Writes failed:** 0
**Apollo credits:** 0 (R0 is Apollo-free)
**Web searches:** 10 (well under budget)

---

## HARD_FLAG writes (4)

| HubSpot ID | Name | Domain | Reason |
|---|---|---|---|
| 324591653605 | Centerline | centerlinecommunications.com | Audax PE construction contractor; clients are AT&T/Verizon/Comcast/Bell/American Tower; 1,500+ employees |
| 324271404793 | Congruex | congruex.com | Crestview broadband construction and engineering firm; clients are top US broadband providers |
| 324508030669 | Phoenix Communications, Inc. | phoenix-fiber.com | Shrewsbury MA fiber-optic contractor; MassDOT MSA; 135 employees |
| 324566401761 | KNET Co.,LTD. | e-knet.com | Korean microduct manufacturer; part of Hexatronic Group (cable vendor category) |

## RENAMABLE writes (2)

| HubSpot ID | Old Name | New Name | Domain | Reason |
|---|---|---|---|---|
| 324628854464 | (empty) | 3 Rivers Communications | 3rivers.coop | Montana rural fiber cooperative; 16K members; 8K mi FTTH; primary site 3rivers.net |
| 324534167255 | pinelandtelco.com | Pineland Telephone Cooperative | pinelandtelco.com | Literal domain string in name field. Domain serves Pineland Telephone Cooperative (Metter GA rural FTTH telco). Likely duplicate of company 324628807414 - flagged for R3 dedup. |

## Tier 3 Holds Surfaced (2 - NO WRITES)

| HubSpot ID | Name | Domain | Why held |
|---|---|---|---|
| 324524875475 | (empty) | gatco.net | Web search returns no clear public match. Surfaced candidates (GATCO Fine Bathware, GATCO Global UK, GATS Telecom India, GETCO Telecommunications) do not unambiguously identify the entity at gatco.net. Cooper to confirm correct entity. |
| 324597786339 | columbus-networks | finetechnologies.co | HubSpot name (slug-formatted "columbus-networks") matches Columbus Networks (Liberty Latin America subsidiary, Caribbean fiber operator). Domain finetechnologies.co does NOT belong to Columbus Networks - it serves an unrelated entity. Direction of correction is ambiguous (could be MISDOMAIN to correct columbus-networks' real domain, or RENAMABLE if name is wrong). No description data to disambiguate. |

## MATCH bucket (92 records - signal_heat = Cold default written)

Representative records (full list in HubSpot via the trigger query):

- Operators with strong ICP fit: Mediacom, Hughes, AST SpaceMobile, KDDI America, Finetwork, Globalstar, Astound Broadband, Grande Communications, Vyve Broadband, Glo Fiber Business, Twin Lakes, Telrite Holdings, Home Telecom, SRT Communications, Vero Fiber, Wire 3 (Fiber Operator), Pineland Telephone Cooperative, Norvado, Complutel, Astranis, Eutelsat (group + America + OneWeb + Network Solutions), Skylo, Boingo, Anterix, YouFibre, SORACOM, Rivada Space, ORBCOMM, Intelsat, Tillman Infrastructure, Everest Infrastructure, Harmoni Towers, TowerCo, Wireless Infrastructure Group, Skyloom Global, NITCO, Novanet, Aryaka, Commnet Broadband, TelePacific/TPx, Skywire, OXIO, Spectrotel, FG (Fiberutilities Group), Wavenet, TCT, ATOM, S-NET, Infrastructure Networks, Astound/Wave Broadband, Stratus ip, Comtel, Rally Internet, Hispasat, Etex Telephone Cooperative, Lightwire, Fastweb Vodafone, Virgin Media O2, KEVLINX, N+ONE DATACENTERS, WIOCC, VERO Broadband, Hilliary Communications.
- Probable R1 evictions (retail MVNO/authorized retailers - name still matches entity at domain, so MATCH path is correct): BeMobile (Verizon retailer), Gateway Wireless (Cricket retailer), Giant Communications Group (Metro by T-Mobile retailer), AT&T - Communication Solutions (AT&T retailer), MOBILY LLC (AT&T retailer), Ultra Mobile, Patriot Mobile.
- Other MATCH candidates that need R1 ICP review: Banco Santander, JPMorgan Chase (Enterprise-ICP Financial Services candidates per Multi-DC scale gate), Rakuten Group (parent - Mobile arm is a real ICP MNO).
- Carryover Tier 3-flavored briefs from prior research (R0 leaves alone, R1 will re-evaluate): Attobahn, Spartan Data Centers, Synnap.

---

## Sample of suspicious-but-MATCH (for transparency)

- **Glo Fiber Business / horizonconnects.com** - LOOKED like MISDOMAIN; confirmed Horizon Telecom was acquired by Shentel and is now branded as Glo Fiber. MATCH.
- **AT&T - Communication Solutions / comnow.net** - LOOKED like MISDOMAIN; confirmed Communication Solutions is an AT&T authorized retailer (24 OK/TX/KS locations); HubSpot name accurately reflects how the entity brands itself. MATCH.
- **pinelandtelco.com record duplicates 324628807414 (Pineland Telephone Cooperative)** - same entity, two domains. RENAMABLE on the literal-name record + flagged for R3 dedup.

---

## What needs Cooper's attention

1. **2 Tier 3 holds** (gatco.net, columbus-networks/finetechnologies.co) - both have name OR domain that doesn't uniquely identify an entity. R0 surfaces, Cooper decides.
2. **4 HARD_FLAGs auto-written** to `Flagged for deletion` - construction contractors (Centerline, Congruex, Phoenix Communications) and microduct manufacturer (KNET). Will appear in next R4 Flagged Consolidation drain.
3. **1 likely-duplicate** (pinelandtelco.com record renamed; flag in audit brief notes likely duplicate of 324628807414 for R3).
4. **9 records deferred** to tomorrow's R0 run (109 candidates exceeded the 100-cap).

---

## Errors / Failures

None. All HubSpot writes 200 OK.
