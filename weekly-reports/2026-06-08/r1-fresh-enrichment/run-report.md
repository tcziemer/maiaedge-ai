CRM Guardian - Fresh Enrichment - 2026-06-08 - 43/100 processed · 7 Tier 3 held

*Pool:* 62 raw candidates - 19 Tier 3 client-side excludes = 43 processed · cap 100 (steady state) · drain projection: pool fully drained this run (0 deferred)

*Path counts (this run):*
- Path alpha full enrichment: 25 processed -> 25 ICP writes, 0 re-routed to gamma
- Path beta re-research: 1 processed -> 1 reclassified (Lonestar manual_review -> Other), 0 Tier 3 holds
- Path gamma eviction: 17 processed -> 4 Other vendor-keeps, 6 Flagged for deletion, 0 MISDOMAIN re-routes to alpha, 7 Tier 3 dedup/identity holds

*Apollo:* 0 credits this run · 0/850 weekly (W24) · 850 remaining for week
*Week rollover:* W23 -> W24 applied at run start (W23 closed 0/850). R1/R2 own the rollover; the 8:30am Signal Scan Colo entry was logged pre-roll under W23.
*Git:* JSON updated locally (commit best-effort; concurrent Monday Signal Scan + R2 contention expected)

*Path alpha - Full ICP enrichments (named, grouped by segment):*

Fiber Operator (8):
- 1Telecom / Um Telecom (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089) - Brazil, owns ~20,000 km fiber; being acquired by V.tal
- Telecentro (Fiber Operator / Regional Cable Operator - Fiber operator / tier_3 / medium_7089) - Argentina, Buenos Aires HFC+FTTH triple-play
- Sacred Wind Communications (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089) - New Mexico rural/tribal FTTH; owner corrected Tim Z -> Ken, country India -> US
- Zentro (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089) - Chicago, largest independent multifamily ISP, ~20 metros
- LigTel Communications (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089) - Indiana rural ILEC/FTTH
- Frontier Networks (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089) - Canadian managed IP comms, owns backbone+POPs+colo (NOT US Frontier)
- Hal Service / WiC (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / low_5069) - small northern Italy fiber/ICT, ASN 44092
- BlueRim Networks (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / low_5069) - Utah MDU ISP, owner corrected -> Ken; possible Smartaira affiliation to verify

Network Operator (1):
- China Unicom / China United Network Communications Group (Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90) - parent of existing China Unicom Global + China Unicom Operations international arms per D2

MSP/Aggregator (12):
- CBC - China Broadband (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - Beijing NaaS, 40+ PoPs; country corrected Romania -> China
- nicos AG (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - German managed-WAN, 130 countries
- Evolve IP (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - UCaaS + managed IT (now Xtium post-ATSG)
- Thrive (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - ~$400M MSP/MSSP
- NTT Global Networks / Virtela (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - asset-light managed WAN, NTT subsidiary
- Proximus NXT (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - Benelux ICT integrator (ex-Telindus)
- Sewan (MSP/Aggregator / Telecom Aggregator - MSP / tier_2 / medium_7089) - pan-European wholesale telecom/cloud platform, 1,250 partners
- Telvantis (MSP/Aggregator / Telecom Aggregator - MSP / tier_2 / low_5069) - wholesale voice, Mexedia group; core unit being acquired by Spectral Capital
- Verve Cloud (MSP/Aggregator / Cloud + Telecom Hybrid MSP - MSP / tier_2 / low_5069) - SMB UCaaS, Digerati subsidiary (distress flag)
- EQUADEX (MSP/Aggregator / Cloud + Telecom Hybrid MSP - MSP / tier_2 / low_5069) - small French Microsoft cloud integrator
- CBTS (MSP/Aggregator / Cloud + Telecom Hybrid MSP - MSP / tier_2 / medium_7089) - ~$1.3B IT services + colo; name fixed from "Cincinnati Bell,"; now TowerBrook-owned, separate from altafiber
- World Cinema / WorldVue (MSP/Aggregator / Managed Network Services - MSP / tier_2 / medium_7089) - hospitality network integrator, 7,000+ properties

Enterprise (4) - Cooper spot-check recommended (verify scale gate $1B+ rev + 3+ DCs OR Equinix/Megaport port OR in-house net eng):
- HCLTech (Enterprise-CustomerSegment / Outsourcing Services - Enterprise / tier_3 / high_90) - $13.8B IT/BPO outsourcer, E4 anchor
- T-Systems Iberia (Enterprise-CustomerSegment / Outsourcing Services - Enterprise / tier_3 / medium_7089) - owns ~8 DCs Spain; D2 inheritance from T-Systems/Deutsche Telekom parent
- T-Systems Brasil (Enterprise-CustomerSegment / Outsourcing Services - Enterprise / tier_3 / low_5069) - regional delivery arm; thin independent footprint
- Blue Cross NC (Enterprise-CustomerSegment / Financial Services - Enterprise / tier_3 / low_5069) - $10B health insurer; routed Financial Services per E1 insurer tiebreaker

*Path beta - reclassification (1):*
- Lonestar Data Holdings: was Other / Standard - colo / manual_review_required -> Other / high_90 / tier_5 (lunar data storage novelty, non-ICP; resolved to stop daily Filter-D reappearance; stale colo sub-segment left in place, cosmetic)

*Path gamma - Eviction summary:*
- 4 Other vendor-keeps: Lenovo (D1 equipment vendor), HughesNet, UltiSat, Pivotel (satellite operators)
- 6 Flagged for deletion (all "No ICP fit"): Komodor, Commercial Furniture Australia, Maximum RE Solutions, Space Digital, New Horizon Enterprises, onecom.sk

*What needs Cooper's attention:*
- 7 Tier 3 holds - see canvas F0B0AFSB9LN section "R1 Fresh Enrichment 2026-06-08" + per-path tables below. 4 are R3-dedup (one.verizon.com, corp.fibernetics.ca, staff.win.be, C3i); 3 are unidentifiable/MISDOMAIN for R0 (dna-communications.com, Desert Lakes Capital, niusgov.com).
- 6 hard-flagged companies in HubSpot Companies filter customer_segment = "Flagged for deletion" (Cooper manual-delete queue).
- 7 partial-confidence (low_5069) ICP writes NOT date-stamped, intentionally left in the R2/D7 re-validation pool: Hal Service, BlueRim, Telvantis, Verve Cloud, EQUADEX, T-Systems Brasil, Blue Cross NC.
- China Unicom carrier family now has 3 records (parent + Global + Operations) - R3 may consolidate per D2 wholesale-arm policy (companion to the existing China Telecom / Verizon / NTT family flags).
- Genuine classification-ambiguity manual_review = 0% (all 7 holds are dedup/identity, not sub-segment ambiguity) - well under the 5% target.

*Run health:* YELLOW
- Full pool drained (43/43), 0 write errors, all 5 HubSpot batches succeeded (10/10/10/6/7). YELLOW only because 7 Tier 3 holds exist (all routine dedup/identity, not problems). Gate-pass rate on definitive-write records ~81% (29/36 stamped; the 7 low_5069 are intentional no-stamp).

*Errors:* None.

---

Path alpha full ICP write table:

```
Account                          | HubSpot ID    | Segment                          | Sub-segment                          | Tier   | Confidence
1Telecom / Um Telecom            | 326179855082  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | medium_7089
Telecentro                       | 326207775473  | Fiber Operator                   | Regional Cable Operator - Fiber op   | tier_3 | medium_7089
Sacred Wind Communications       | 326160068331  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | medium_7089
Zentro                           | 326311594730  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | medium_7089
LigTel Communications            | 326350101208  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | medium_7089
Frontier Networks                | 326188915444  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | medium_7089
Hal Service                      | 326171165415  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | low_5069
BlueRim Networks                 | 326179855037  | Fiber Operator                   | Regional CLEC - Fiber operator       | tier_3 | low_5069
China Unicom (Group)             | 326207775457  | Network Operator(Tier 1 / VNO)   | Tier 1 Carrier - Network Op          | tier_1 | high_90
CBC - China Broadband            | 326179855035  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
nicos AG                         | 326179855058  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
Evolve IP                        | 326188916432  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
Thrive                           | 326350145248  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
NTT Global Networks / Virtela    | 326171165408  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
Proximus NXT                     | 326188915449  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
Sewan                            | 326350145268  | MSP/Aggregator                   | Telecom Aggregator - MSP             | tier_2 | medium_7089
Telvantis                        | 326350145243  | MSP/Aggregator                   | Telecom Aggregator - MSP             | tier_2 | low_5069
Verve Cloud                      | 326350145260  | MSP/Aggregator                   | Cloud + Telecom Hybrid MSP - MSP     | tier_2 | low_5069
EQUADEX                          | 326188916410  | MSP/Aggregator                   | Cloud + Telecom Hybrid MSP - MSP     | tier_2 | low_5069
CBTS                             | 326207775480  | MSP/Aggregator                   | Cloud + Telecom Hybrid MSP - MSP     | tier_2 | medium_7089
World Cinema / WorldVue          | 326188915436  | MSP/Aggregator                   | Managed Network Services - MSP       | tier_2 | medium_7089
HCLTech                          | 326171164408  | Enterprise-CustomerSegment       | Outsourcing Services - Enterprise    | tier_3 | high_90
T-Systems Iberia                 | 326176546504  | Enterprise-CustomerSegment       | Outsourcing Services - Enterprise    | tier_3 | medium_7089
T-Systems Brasil                 | 326188915439  | Enterprise-CustomerSegment       | Outsourcing Services - Enterprise    | tier_3 | low_5069
Blue Cross NC                    | 326350146243  | Enterprise-CustomerSegment       | Financial Services - Enterprise      | tier_3 | low_5069
```

Path beta reclassification table:

```
Account                  | HubSpot ID    | Was -> Became                                          | Confidence delta
Lonestar Data Holdings   | 311409164986  | Other/manual_review_required -> Other/tier_5           | manual_review_required -> high_90
```

Path gamma eviction table:

```
Account                         | HubSpot ID    | Outcome                | Reason
Lenovo                          | 326188916468  | Other (tier_5)         | D1 equipment vendor; ecosystem reference
HughesNet (Brazil)              | 326188916430  | Other (tier_5)         | Satellite operator; ecosystem reference
UltiSat                         | 326176546520  | Other (tier_5)         | Government SATCOM operator; ecosystem reference
Pivotel America                 | 326179855036  | Other (tier_5)         | Satellite MVNO/reseller; ecosystem reference
Komodor                         | 326259493574  | Flagged for deletion   | No ICP fit (Kubernetes ops SaaS)
Commercial Furniture Australia  | 326188916412  | Flagged for deletion   | No ICP fit (furniture wholesaler)
Maximum RE Solutions            | 326188915434  | Flagged for deletion   | No ICP fit (residential real estate)
Space Digital                   | 326207775475  | Flagged for deletion   | No ICP fit (film/VFX studio)
New Horizon Enterprises         | 326179855042  | Flagged for deletion   | No ICP fit (food distributor)
Onecom (Slovakia)               | 326171165393  | Flagged for deletion   | No ICP fit (geospatial micro-firm)
```

Tier 3 hold table:

```
Account                  | HubSpot ID    | Path  | Ambiguity
one.verizon.com          | 326188916423  | gamma | R3 dedup -> Verizon master 192899501812 (verizon.com)
corp.fibernetics.ca      | 326322401993  | beta  | R3 dedup -> Fibernetics 316620030686 (fibernetics.ca)
staff.win.be             | 326350145256  | beta  | R3 dedup -> Win s.a. (NRB) 326163435208 (win.be)
C3i                      | 326176546529  | gamma | R3 dedup/subsidiary -> HCLTech 326171164408 (acquired 2018)
dna-communications.com   | 326284230390  | beta  | MISDOMAIN/identity conflict (NY PR agency vs IL fiber ISP dnacom.com) -> R0
Desert Lakes Capital     | 326228928201  | gamma | Unidentifiable; parked/dormant domain -> R0/Cooper
niusgov.com              | 326311594719  | gamma | Unidentifiable; no recoverable identity -> R0/Cooper
```

Partial gate failure table (low_5069 ICP, written but NOT date-stamped; flow to R2/D7):

```
Account             | HubSpot ID    | Path  | Reason (not a field gap)
Hal Service         | 326171165415  | alpha | low_5069 confidence (small regional operator); below medium stamp threshold
BlueRim Networks    | 326179855037  | alpha | low_5069 confidence (small MDU ISP; possible Smartaira tie)
Telvantis           | 326350145243  | alpha | low_5069 confidence (micro-cap wholesale voice; being acquired)
Verve Cloud         | 326350145260  | alpha | low_5069 confidence (SMB UCaaS; parent distress)
EQUADEX             | 326188916410  | alpha | low_5069 confidence (tiny IT integrator)
T-Systems Brasil    | 326188915439  | alpha | low_5069 confidence (regional delivery arm; thin independent footprint)
Blue Cross NC       | 326350146243  | alpha | low_5069 confidence (insurer; infra/net-eng gates inferred not confirmed)
```
