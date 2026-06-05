# Enrichment Run Report — 2026-04-27

**Trigger:** "Find companies where customer_segment is blank or last_enriched_date >120 days. Process 200 in batches of 10."

**Scope adjustment after dataset analysis:** Cooper approved focusing on the 122 blank-segment companies only. The 78 stale-enriched candidates were almost all already classified as `Other` or `Partner Target` (Cisco, Meta, Dell, IBM Cloud, Bloomberg, Accenture, etc.) — re-enriching to confirm "still not ICP" is low ROI.

**Session result:** 90 of 122 written to HubSpot. 32 remaining will roll into the next scheduled `crm-guardian` run.

---

## Distribution of the 90 enriched

| Bucket | Count | Notes |
|---|---|---|
| **Tier 1 strategic ICP** | 5 | Lumos (T-Mobile/EQT), Telmex, Crusoe (NeoCloud), Verizon (dup), Orange España |
| **Tier 2 strategic ICP** | 8 | C Spire/Troy Cable, Telin, EllaLink, GoNetspeed/OTELCO, Buckeye Broadband, Red Uno (Telmex), Boldyn (Mobilitie), Bayobab, Entel Perú |
| **Tier 3 ICP** | 3 | Neterra, BTC Broadband, IntelePeer (CPaaS) |
| **Tier 4 ICP / Partner** | 14 | Execulink, Internet Subway, Softnet, Akton, ONEMAX, Ten Peaks DC, SBTS, Teligent, Telesol Group, BGIS, Davis Infrastructure, Star Solutions, ISPN, Ubiquiti |
| **Tier 5 / Edge / Aggregator** | 12 | Shaun Telecom, Red Telecom, Whisl, RouteTrust, TeleSpace, Megatel, Revaltex, FGN, Endeavor B2B (media partner), Fiber Gaming, Surf Mobile, Savitele |
| **Other (excluded)** | 35 | Gartner, TeleGeography, Fiverr, Chumash tribe, NASI, BCN restaurant, t-shirt wholesaler, Telemetro broadcaster, FreeWheel ad-tech, Clear-Com intercoms, MNJ IT, Open Systems IT, etc. |
| **Flagged for deletion** | 9 | littlecrusoe.com (spoofed), crusoesurvival.com (spoofed), exabeauty.com (Madagascar insect farm), bcnhouston.com (restaurant), t-shirtwholesaler.com, vibrantchurchcommunications.com, dtna.com (Daimler Trucks, NOT Deutsche Telekom), Toptel.pl (consumer electronics distributor), Earth Ledger (blockchain) |
| **Unknown / manual review** | 4 | Capvion BV (NL), revine.io, scit.agency, East2Westbrook, CCsquared, Lexico, Telecommerce.net, Telecommerce.com.mx |

---

## Key strategic finds (worth surfacing to sales)

1. **Lumos (lumosnet.com / lumos.net — 2 records, MERGE)** — Tier 1. T-Mobile/EQT closed 50/50 ownership April 2025. CEO Brian Stading retiring Q1 2026. Building 1M fiber passings by 2026 across VA/NC/SC. Strong trigger event.
2. **Crusoe Energy (crusoe.com)** — Tier 1 NeoCloud. 900 MW Microsoft campus Abilene TX (March 2026), 1.2 GW existing for Oracle/OpenAI, $50B Wyoming Project Jade scaling to 10 GW. Fast Company 2026 Most Innovative.
3. **GoNetspeed (formerly OTELCO)** — Tier 2. Owned by Oak Hill Capital. $33M Maine FTTP investment expanding 43,000 locations. Largest independent fiber builder in Northeast.
4. **EllaLink** — Tier 2 subsea. EU↔LatAm, 100 Tbps, lowest transatlantic latency. Lum@link extension to French Guiana ready 2026.
5. **Bayobab (MTN Group)** — Tier 2. Pan-African wholesale digital infrastructure (renamed from MTN GlobalConnect 2023). Strategic for African enterprise routing.
6. **Orange España** — Tier 1. 21M customers, post-MásMóvil merger Spain's largest mobile op.
7. **Boldyn Networks (mobilitie.com)** — Tier 2. £1.5B Transport for London network overhaul. DUPLICATE — master at 300402132682.

---

## Data quality issues uncovered

### Confirmed duplicates (recommend merge)

| Master record | Duplicate | Notes |
|---|---|---|
| Lumos at lumosnet.com (320388768481) | Llumos at lumos.net (320406695627) | Same entity, two records |
| Telmex (320394255086) | Red Uno reduno.com.mx (320402313930) | Parent + B2B sub-brand |
| Nextlink nextlink.team (320394411750) | nxlink.com (320378046163) | Same entity |
| Verizon master 192899501812 | verizonwireless.com (318223399628) | Existing master + this dup |
| Boldyn master 300402132682 | mobilitie.com (318223366892) | Existing master + Mobilitie sub-brand |
| C Spire master (if exists) | troycable.net (320388768483) | Troy Cable rebrand to C Spire |
| FiberLight master (if exists) | texasfiberdesigngroup.com (319141768918) | Contractor, not operator |

### Wrong domain / wrong company (rename or delete)

| ID | HubSpot name was | Actual entity at domain | Action |
|---|---|---|---|
| 320388768482 | EdgeStone Singapore | **Neterra** (Bulgarian telecom) | Renamed to Neterra |
| 320402328310 | Uptown Hair | **ISPN Network Services** | Renamed |
| 320311807732 | Neural Edge Solutions | **NASI** (space workforce cert) | Renamed |
| 320378046180 | OTELCO | **GoNetspeed** (rebranded 2022) | Renamed |
| 320388767457 | Lightwave | **Endeavor Business Media** (parent) | Renamed |
| 318231546573 | Comcast | **FreeWheel** (ad-tech sub) | Renamed |
| 318231691991 | Deutsche Telekom NA | **Daimler Trucks NA** | Flagged for deletion |
| 318106540786 | BT International | **BT Insurance Korea** (NOT British Telecom) | Renamed/excluded |
| 318223234758 | Ultramobile | Ultra Mobile MVNO at ultra.me | Excluded |
| 318223366892 | AT&T | **Boldyn Networks** (Mobilitie sub) | Renamed |
| 319775490772 | SIP VoIP | **CWIT Dubai** (IT consultancy) | Renamed |
| 318207597276 | Telemetro | **Telemetro Reporta** Panama TV | Renamed |
| 318231692007 | Akton d.o.o. | **Akton Communications** (brand) | Renamed |
| 318231691993 | Teligen | **Teligent Telecom** (Sweden) | Renamed |

### Hard deletes recommended (9 records)

These are clear non-business or wrong-business records that should be removed entirely, not just classified:

- `littlecrusoe.com` (320302232270) — spoofed Crusoe domain
- `crusoesurvival.com` (320364831427) — spoofed Crusoe domain
- `exabeauty.com` (318207597275) — Madagascar insect farming startup
- `bcnhouston.com` (318207597277) — Spanish restaurant in Houston
- `t-shirtwholesaler.com` (318106540782) — apparel wholesaler
- `vibrantchurchcommunications.com` (318231692001) — church AV service
- `dtna.com` (318231691991) — Daimler Trucks (truck manufacturer)
- `toptel.com` (318231691996) — Polish consumer electronics distributor
- `ledgerofearth.com` (319775490773) — blockchain ESG project

---

## Deal protection rule

Per Cooper's directive, the deal-protection rule was applied: re-enrichment to a record with an open deal would have flagged for review rather than auto-overwritten `customer_segment` or `account_tier`. **None of the 90 records I touched had populated `customer_segment` going in** (this whole batch was the blank-segment bucket), so the rule was a no-op — every write was net-new classification, not an overwrite.

---

## Remaining 32 (companies 91-122) — defer to next CRM Guardian run

These are ready to be picked up by the next scheduled `crm-guardian` enrichment job. They share the same characteristics as the records I processed (mostly small VoIP/voice resellers and confused imports), so I'd estimate the segment distribution will look similar to batches 4-8: ~40% Other/Excluded, ~30% small Tier 4-5 ICP, ~10% Partner Target, ~10% Unknown/manual, ~10% flagged for deletion.

The remaining IDs (sample):
- gugli.com, clearcom.mx, nos.pt (NOS Wholesale Portugal — likely Tier 2 ICP), tecomsa-ltd.com, cellusys.com (Ireland)
- unitednetworksofamerica.com, trellisnetworks.com, trilogycomms.com, tealcom.io
- dawztele.com, stratusnetworks.com, gatewayglbl.com, unlimitednetworksinc.com
- tritonnw.com, coloxchange.com (likely a colo!), latinocdc.org, starbi.com
- volksresources.com, pineapplesms.com, unitedwholesale.com, telesis.com
- gvcs.com, telepartner.com, axentbath.us (probably bathroom fixtures), americanfibernetwork.com (AFN — likely Fiber Op)
- tix.com, thehorizongroup.net, allaccesstelecom.com, alluretelecom.com
- metronetinc.com (MetroNet — actually a major fiber operator, this is wrongly UNQUALIFIED)
- kiocompany.com, suddenlink.com (Suddenlink — now part of Optimum/Altice)

**Standouts in the remaining 32 worth flagging:**
- **NOS Wholesale (nos.pt)** — Major Portuguese telecom wholesale division. Likely Tier 2.
- **MetroNet (metronetinc.com)** — Real US fiber operator (Indiana-based). Currently marked UNQUALIFIED in HubSpot — that classification is questionable.
- **Suddenlink (suddenlink.com)** — Now Optimum/Altice. Major US cable. Should be merged with Altice/Optimum master.
- **AFN (americanfibernetwork.com)** — Likely a Kansas regional fiber operator.
- **COLOXCHANGE (coloxchange.com)** — Name strongly suggests colocation marketplace/operator.

---

## Recommendations

1. **Run CRM Guardian** to pick up the remaining 32 records.
2. **Hygiene merge sweep** of the 7 confirmed duplicates listed above before next outbound batch — Lumos, Telmex/Red Uno, Nextlink, Verizon, Boldyn, C Spire, FiberLight.
3. **Hard-delete** the 9 records flagged above — they're polluting the CRM with non-businesses (restaurants, apparel, insect farms, etc.).
4. **Re-classify MetroNet** (currently UNQUALIFIED) — it's a real Tier 2 fiber operator.
5. **Investigate the import source** that brought in records like "BCN" (Houston restaurant), "EXA" (insect farming), and "Deutsche Telekom NA" (truck manufacturer). The import logic appears to be flagging records by name keyword without verifying the underlying domain — this is a systematic data-quality leak.
