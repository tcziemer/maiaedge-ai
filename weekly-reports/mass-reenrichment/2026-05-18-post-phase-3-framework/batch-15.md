# Mass Re-Enrichment Sweep - Batch 15 Audit Log

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 15
**Date:** 2026-05-18
**BATCH_SIZE:** 50
**VERIFY_DEPTH:** leverage-and-patch
**APOLLO_ENFORCEMENT:** disabled (sweep window)
**SEGMENT_SCOPE:** all_active_icp
**Pool remaining at batch start:** 2,055
**Pool remaining at batch end:** ~2,005

## Path mix

| Path | Count |
|---|---:|
| LIGHT | 2 |
| MEDIUM | 39 |
| FULL | 9 |
| HOLD | 0 |

## Tier writes

| Direction | Count |
|---|---:|
| Promotions (toward T1) | 8 |
| Demotions (toward T5) | 4 |
| Skipped (hs_is_target_account=true) | 30 |
| No change | 8 |

## Segment changes / cascades fired

- **EOS IT Solutions** (267141967581): MSP/Aggregator -> Other (hyperscale IT systems integrator, not telecom aggregator); tier_2 -> tier_5
- **Virgin Media Business Wholesale** (318051097275): Fiber Operator -> Network Operator(Tier 1 / VNO); Regional Cable Operator -> Cable MSO Enterprise Division; tier_3 -> tier_1
- **UGI / NOVA** (318205926076): Fiber Operator -> Network Operator(Tier 1 / VNO); Regional CLEC -> Tier 1 Carrier (United Group SEE multi-country MNO+FTTH holding); tier_3 -> tier_1
- **Orange Middle East and Africa** (318211865327): Fiber Operator -> Network Operator(Tier 1 / VNO); Regional CLEC -> Tier 1 Carrier (Orange MEA regional carrier holding 18+ countries); tier_3 -> tier_1
- **MNC Play Media** (319151103725): Network Operator(Tier 1 / VNO) -> Fiber Operator; Tier 1 Carrier -> Regional CLEC (FTTH ISP not national carrier); tier_1 frozen (target_account)
- **Triangelbolaget D4 AB** (318207597267): Fiber Operator -> Other; (Swedish dark fiber consortium TeliaSonera/Telenor/Tele2 JV, 5 employees, not a buyer); tier_2 -> tier_5
- **IDT global** (316598423240): Fiber Operator -> MSP/Aggregator; Regional CLEC -> Telecom Aggregator (international voice/SIP wholesale aggregator pattern); tier_3 -> tier_2
- **Nobel** (316560181997): Fiber Operator -> MSP/Aggregator; Regional CLEC -> Telecom Aggregator (Romania-HQ international voice wholesaler); tier_3 -> tier_2
- **United Cable Company** (316538883829): MSP/Aggregator -> Flagged for deletion (17 emp + None Identified infrastructure pattern); tier_2 -> tier_5
- **Entel Chile** (316558341868): Fiber Operator -> Network Operator(Tier 1 / VNO); Regional CLEC -> Tier 1 Carrier (13K emp, $3.28B, major Chilean MNO+fiber Tier 1 national); tier_3 -> tier_1

## Sub-segment-only flips (within same segment)

- **Globe Business** (319137717960): Tier 1 Carrier -> Pure Wholesale Carrier (B2B wholesale arm of Globe Telecom PH); target_account tier frozen
- **Fasttelco** (319125023419): Tier 1 Carrier -> Pure Wholesale Carrier (stc Kuwait B2B/wholesale arm); target_account tier frozen
- **Inter.link** (318219105017): Regional CLEC -> Long Haul / Backbone (German wholesale interconnect/IXP backbone); tier_3 -> tier_2
- **Trans Pacific Networks** (318106540781): Long Haul / Backbone -> Subsea cable operator (Cayman SPV, transpacific submarine cable); tier_2 stable
- **AXTEL** (316529844940): Regional CLEC -> Tier 2 National Wholesale (4000 emp, $687M, 50K+ route miles, Mexico's #2 carrier); tier_3 -> tier_2
- **Norlys Mobil Wholesale** (318097753798): Regional CLEC -> Municipal / Cooperative (Danish cooperative); tier_3 -> tier_4 (cooperative default T4)

## Greenfield migrations

None this batch.

## Customer-protection HOLDs

None this batch.

## Completeness Gate fails

None this batch.

## Manual-review HOLDs

None this batch.

## Confidence downgrades

- Symbiote Investments (319126831825): high_90 -> low_5069 (thin profile, "Investments" suffix, target_account validation needed via D7)
- WX Network Panama (319125023448): high_90 -> medium_7089 (small Panama carrier, thin public profile)
- Island Broadband (319126830809): high_90 -> medium_7089 (small Turks and Caicos ISP, Tier 1 Carrier stretched)
- Cablenet Cyprus (319145736894): high_90 -> medium_7089 (domestic Cypriot cable+FTTH, "subsea hub" framing overstated)
- UGI / NOVA (318205926076): high_90 -> medium_7089 (record name ambiguous, possible R3 dedup with United Group parent)
- EOS IT Solutions (267141967581): no field returned -> medium_7089 (moved to Other)
- Trans Pacific Networks (318106540781): high_90 -> medium_7089 (operator vs financing-only role needs D7 validation)
- United Cable Company (316538883829): high_90 -> medium_7089 (moved to Flagged for deletion)
- Triangelbolaget D4 AB (318207597267): high_90 -> medium_7089 (moved to Other)

## R3 dedup flags raised

- Vodafone UK (318207598314) vs Vodafone Group Plc - Apollo revenue/employee data is Group-level
- Virgin Media Business Wholesale (318051097275) vs Virgin Media Limited (318223238859) - wholesale arm vs parent cable MSO
- UGI / NOVA (318205926076) vs likely United Group parent record - record name awkward
- Wind Telecom DR carryforward from batch 14 (318327651046 vs 251659209447) - same DR entity

## Per-record summary

### Sub-batch A (10 records, all hs_is_target_account=true, tier frozen)

| Company ID | Name | Country | Path | Notes |
|---|---|---|---|---|
| 319135939295 | Grupo GTD Chile | Chile | MEDIUM | Brief rewrite, geo fill |
| 319137717960 | Globe Business | Philippines | MEDIUM | Tier 1 Carrier -> Pure Wholesale Carrier |
| 319173024494 | Cyta (Cyprus) | Cyprus | MEDIUM | Brief tighten, geo fill |
| 319154800318 | Asiacell Wholesale | Iraq | MEDIUM | Templating clean |
| 319124946663 | CBN (Cyberindo Aditama) | Indonesia | MEDIUM | Templating clean |
| 319151103725 | MNC Play Media | Indonesia | MEDIUM | Network Op -> Fiber Op (FTTH ISP scope), tier frozen |
| 319173025485 | Mytel | Myanmar | MEDIUM | Templating clean |
| 319145758447 | Viva Bahrain Wholesale | Bahrain | MEDIUM | State field 'Minas Gerais' cleared (data quality) |
| 319141268212 | Gibtelecom | Gibraltar | MEDIUM | Templating clean |
| 319145751229 | Belize Telemedia Wholesale | Belize | MEDIUM | Templating clean |

### Sub-batch B (10 records, mixed target_account states)

| Company ID | Name | Country | Path | Notes |
|---|---|---|---|---|
| 318231615183 | TIM SA (TIM Brasil) | Brazil | MEDIUM | Brief fill, geo fill |
| 318223238859 | Virgin Media Limited | UK | MEDIUM | Brief fill |
| 318223391443 | Orange Business Services | UK | MEDIUM | Brief fill |
| 318207598314 | Vodafone UK | UK | MEDIUM | Group-rev dedup flag |
| 267141967581 | EOS IT Solutions | UK | FULL | MSP/Aggregator -> Other, tier_2 -> tier_5 |
| 318051097275 | Virgin Media Business Wholesale | UK | FULL | Fiber Op/Regional Cable -> Network Op/Cable MSO Enterprise, tier_3 -> tier_1 |
| 318097753798 | Norlys Mobil Wholesale | Denmark | MEDIUM | Regional CLEC -> Municipal/Cooperative, tier_3 -> tier_4 |
| 318205926076 | UGI / NOVA | Netherlands | FULL | Fiber Op -> Network Op/Tier 1 Carrier, tier_3 -> tier_1 |
| 318192629457 | New Horizon Communications | US | MEDIUM | Brief fill |
| 318211865327 | Orange Middle East and Africa | (multi) | FULL | Fiber Op -> Network Op/Tier 1 Carrier, tier_3 -> tier_1 |

### Sub-batch C (10 records, heavy classification work)

| Company ID | Name | Country | Path | Notes |
|---|---|---|---|---|
| 318211865329 | Novvacore | Brazil | MEDIUM | Brief fill |
| 318219105017 | Inter.link | Germany | MEDIUM | Regional CLEC -> Long Haul/Backbone, tier_3 -> tier_2 |
| 318207597267 | Triangelbolaget D4 AB | Sweden | FULL | Fiber Op -> Other (dark fiber consortium), tier_2 -> tier_5 |
| 318106540781 | Trans Pacific Networks | Cayman | FULL | Long Haul -> Subsea cable operator |
| 320875891444 | Gazeti Telecomm | Mexico | MEDIUM | Routine note replaced with proper brief |
| 316529844940 | AXTEL / AXTEL NETWORKS | Mexico | MEDIUM | Regional CLEC -> Tier 2 National Wholesale, tier_3 -> tier_2 |
| 316598423240 | IDT global | US | FULL | Fiber Op -> MSP/Aggregator/Telecom Aggregator, tier_3 -> tier_2 |
| 316560181997 | Nobel | Romania | FULL | Fiber Op -> MSP/Aggregator/Telecom Aggregator, tier_3 -> tier_2 |
| 316538883829 | United Cable Company | US | FULL | MSP/Aggregator -> Flagged for deletion, tier_2 -> tier_5 |
| 316558341868 | Entel Chile | Chile | FULL | Fiber Op -> Network Op/Tier 1 Carrier, tier_3 -> tier_1 |

### Sub-batch D (10 records, all hs_is_target_account=true, tier frozen)

| Company ID | Name | Country | Path | Notes |
|---|---|---|---|---|
| 319126831825 | Symbiote Investments | Jamaica | MEDIUM | Confidence -> low_5069, thin profile |
| 319125023448 | WX Network Panama | Panama | MEDIUM | Confidence -> medium_7089 |
| 319126828737 | Telecom Namibia Wholesale | Namibia | MEDIUM | Templating clean |
| 319126792912 | SPT (Saigon Postel) | Vietnam | MEDIUM | Brief refine |
| 319126817492 | CANAL+ Telecom Reunion | Reunion | MEDIUM | Templating clean |
| 319125023419 | Fasttelco | Kuwait | MEDIUM | Tier 1 Carrier -> Pure Wholesale Carrier (stc subsidiary) |
| 319126830809 | Island Broadband | Turks & Caicos | MEDIUM | Confidence -> medium_7089 |
| 319126833854 | Blueline Madagascar | Madagascar | MEDIUM | Templating clean |
| 319134160611 | OPT-NC (New Caledonia) | New Caledonia | LIGHT | Brief already clean, just bump date |
| 319134215877 | NetNam | Vietnam | MEDIUM | Brief refine |

### Sub-batch E (10 records, all hs_is_target_account=true, tier frozen)

| Company ID | Name | Country | Path | Notes |
|---|---|---|---|---|
| 319141291767 | Vodafone Oman Wholesale | Oman | MEDIUM | Templating clean |
| 319173026498 | Omantel Wholesale | Oman | LIGHT | Brief already clean, just bump date |
| 319141273290 | ETB Bogota | Colombia | MEDIUM | Apollo 45-emp count flagged as subsidiary-scope |
| 319145736894 | Cablenet | Cyprus | MEDIUM | Confidence -> medium_7089, subsea framing overstated |
| 319141269238 | True International Gateway | Thailand | MEDIUM | Brief refine |
| 319141290685 | Ogero Wholesale | Lebanon | MEDIUM | Templating clean |
| 319147505395 | Zain Jordan Wholesale | Jordan | MEDIUM | Templating clean |
| 319151122141 | Algerie Telecom Wholesale | Algeria | MEDIUM | Templating clean |
| 319154775756 | Viettel International | Vietnam | MEDIUM | Brief refine |
| 319141272312 | Angola Telecom Wholesale | Angola | MEDIUM | Templating clean |

## Apollo this batch

0 credits (no Apollo calls; leverage-and-patch).

## Sweep cumulative Apollo

0 credits (APOLLO_ENFORCEMENT=disabled, sweep window).

## Run health: GREEN

No errors. All 50 writes succeeded (HTTP 200, summary `updated:10` × 5 sub-batches).

## Patterns this batch

1. **Phase 3 prep target_account templating bleed**: 30/50 records this batch were hs_is_target_account=true international carriers from Phase 3 prep batches (2026-02-24 / 2026-04-21). "[Country] [Company]..." prefix bleed universal; cleaned on every record.
2. **VoIP/SIP wholesale aggregator pattern accelerating**: IDT global + Nobel this batch (Romania). 2 more this batch. Total ~10 in sweep. Continue routing international voice/SIP wholesalers from Fiber Op > Regional CLEC to MSP/Aggregator > Telecom Aggregator.
3. **National incumbent Fiber Op -> Network Op flip pattern continues**: Entel Chile + UGI/NOVA + Orange MEA. 3 this batch. Phase 3 prep batched MNOs as Regional CLEC defaults; integrated multi-country telcos should route to Tier 1 Carrier - Network Op.
4. **Apollo parent/subsidiary revenue bleed**: Vodafone UK ($48B = Group), ETB Bogota (45 emp = subsidiary scope only). Continue noting and skipping when 1000x off subsidiary scale.
5. **Consortium / financing-SPV pattern**: Triangelbolaget D4 AB (Swedish dark fiber JV between Telia/Telenor/Tele2) routed to Other - not a buyer. Trans Pacific Networks (Cayman SPV, 30 emp) routed to Subsea cable operator with D7 follow-up flag (operator vs financing-only role).
6. **Hyperscale IT services firms aren't telecom aggregators**: EOS IT Solutions (hyperscale data center deployment / IT staffing) routed to Other (Partner Target). Pattern: 200-2000 employee IT integrators serving hyperscalers should not be MSP/Aggregator-classified.
7. **"None Identified" infrastructure + thin profile flag pattern continues**: United Cable Company (17 emp, US/NJ) flagged for deletion. Same as batch 14 pattern (Manor, IP Transfer, Telegeeks, Call48).
8. **Subsea cable operator sub-segment second use**: Trans Pacific Networks (after SCCS in batch 13). OPT-NC New Caledonia mentioned Gondwana + Picot2 cables but stays Tier 1 Carrier (primary business is national telco; cable landings byproduct).
9. **Cable MSO Enterprise Division for wholesale arms of cable MSOs**: Virgin Media Business Wholesale routed to Cable MSO Enterprise Division - Network Op, matching the parent Virgin Media Limited classification (parallel to Comcast Business/Cox Business pattern).

## Data quality issues surfaced

- Viva Bahrain Wholesale: `state = "Minas Gerais"` (Brazilian state, wrong country/state pair) - cleared.
- Gazeti Telecomm: `account_brief` was a Routine 0 misdomain auto-correct note from 2026-04-29 instead of a proper brief - replaced.
- ETB Bogota: 45 employees Apollo count is subsidiary-scope; real ETB Colombia is much larger.
- Vodafone UK: $48B revenue / 104K employees is Vodafone Group, not UK alone.
- UGI / NOVA: record name 'UGI / NOVA' awkward (mix of parent + Greek subsidiary).
- Cablenet Cyprus: prior brief overstated "subsea hub status" - Cablenet is primarily a domestic Cypriot cable/FTTH operator.

## D7 escalations from this batch

- **Symbiote Investments** (319126831825): thin profile, "Investments" suffix - need to verify whether this is actually a Jamaican carrier or a holding co.
- **Trans Pacific Networks** (318106540781): need to verify operator vs financing-only role for Subsea cable operator confirmation.
- **WX Network Panama** (319125023448): small operator, thin public profile - sub-segment refinement candidate.
- **Cablenet Cyprus** (319145736894): sub-segment refinement candidate (Regional Cable Operator may fit better than Tier 1 Carrier if target_account is dropped).

## Drain status

- Done in this sweep: ~721/~2,735 (~26%)
- Remaining: ~2,015
- ETA: ~40 more batches at BATCH_SIZE=50
