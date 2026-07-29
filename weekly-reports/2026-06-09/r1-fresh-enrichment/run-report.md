CRM Guardian - Fresh Enrichment - 2026-06-09 - 34/100 processed · 0 Tier 3 held

*Pool:* 65 candidates raw -> 34 processable after 31-record Tier 3 client-side exclude · cap 100 (steady state, total <=200) · drain projection: 0 days (full pool drained this run)

*Path counts (this run):*
- Path α full enrichment: 20 processed -> 20 ICP writes, 0 re-routed to γ
- Path β re-research: 0 processed (all 34 processable were blank-segment Filter Group A new imports; no Unknown / low-confidence-Other records in the processable pool)
- Path γ eviction: 14 processed -> 3 Other vendor/partner keeps, 11 Flagged for deletion, 0 MISDOMAIN re-routes

*Apollo:* 0 credits this run · 0/850 weekly (W24) · 850 remaining for week. No apollo_organizations_enrich calls - all firmographics resolved from web research + existing import data (state/country already populated). Sub-cap 30, used 0 of 30.
*Git:* deferred (Cowork scheduled task; JSON updated locally)

*Path α - Full ICP enrichments (named, grouped by segment):*
- Network Operator (Tier 1 / VNO):
  - Telenor Danmark (Tier 1 Carrier - Network Op / tier_2 / medium_7089) - challenger #2 Danish MNO, Telenor Group; tier demoted from default tier_1 per Cooper fix-directly principle (developed-market challenger, not incumbent)
  - Telenor Pakistan (Tier 1 Carrier - Network Op / tier_2 / medium_7089) - now PTCL-owned, consolidating into PTCL; flag PTCL dup for R3
  - Telenor Sweden (Tier 1 Carrier - Network Op / tier_2 / medium_7089) - challenger MNO, Net4Mobility JV
  - T-Mobile Polska (Tier 1 Carrier - Network Op / tier_2 / medium_7089) - Deutsche Telekom subsidiary, big-four PL
  - Vivo / Telefonica Brasil (Tier 1 Carrier - Network Op / tier_1 / high_90) - Brazil's largest integrated carrier, anchor-scale
  - DISH Network (Tier 1 Carrier - Network Op / tier_1 / high_90) - US national 5G Open RAN carrier (EchoStar)
  - Reliance Industries / Jio (Tier 1 Carrier - Network Op / tier_1 / high_90) - parent record; Jio holds the carrier + 2,000 MW NVIDIA AI-DC assets; flag Jio dup for R3
- Fiber Operator:
  - LitFiber (Regional CLEC - Fiber operator / tier_3 / medium_7089) - Oak Hill FTTP overbuilder OH/TX, merging with Omni Fiber
- NeoCloud:
  - LuxProvide (Sovereign AI Clouds - Neocloud / tier_1 / high_90) - Luxembourg national MeluXina supercomputer
  - STACKIT (Sovereign AI Clouds - Neocloud / tier_1 / medium_7089) - Schwarz Group sovereign cloud, 4 DCs + 200 MW build
  - exoscale (Sovereign AI Clouds - Neocloud / tier_1 / medium_7089) - A1/Telekom Austria European sovereign cloud + GPU inference
  - Neysa Networks (Large Scale GPU - Neocloud / tier_1 / high_90) - India sovereign AI cloud, $1.2B Blackstone raise Feb 2026
  - Denvr Dataworks (AI Infrastructure providers - Neocloud / tier_1 / medium_7089) - Canada/US GPU cloud, 1,024-GPU H100 cluster
  - Bit Digital (Crypto to AI - Neoclouds / tier_1 / high_90) - former BTC miner, GPU DCs via WhiteFiber (Op Principle 9)
  - iGenius / Domyn (Sovereign AI Clouds - Neocloud / tier_1 / medium_7089) - Italy sovereign AI, Colosseum GB200 buildout, G42-backed
  - YTL (Large Scale GPU - Neocloud / tier_1 / medium_7089) - Malaysia conglomerate; operational YTL AI Cloud GB200 on 600 MW Kulai campus
  - Assembly / Nebul (Sovereign AI Clouds - Neocloud / tier_1 / medium_7089) - assembly.nl operates as Nebul, Dutch sovereign GPU cloud (HGX B200 supercluster); flag Nebul dup for R3
- Enterprise (Multi-DC ICP):
  - Swiss Re (Financial Services - Enterprise / tier_3 / medium_7089) - global reinsurer; scale gate met on revenue + in-house net eng (inferred; no commercial DC ownership)
  - Swiss Life (Financial Services - Enterprise / tier_3 / medium_7089) - Switzerland's largest life insurer; scale gate met on revenue + in-house net eng
  - FPT Software (Outsourcing Services - Enterprise / tier_3 / medium_7089) - Vietnam IT outsourcer, ~$1.6B / 41K staff, global delivery centers; owned infra sits in sibling FPT entities (flag for R3)
  - Note: Cooper should spot-check the 3 Enterprise classifications - scale gate applied on revenue + in-house net eng; commercial DC/Fabric-port confirmation was inferred from scale, not documented.

*Path β - Top 5 reclassifications:* none (0 Path β records this run)

*Path γ - Eviction summary:*
- Other (vendor / partner / ecosystem keeps, tier_5 high_90): Indus Towers (India towerco - passive infra reference), SambaNova Systems (AI chip vendor - D1 equipment disqualifier, competitive reference; owner corrected to Ken/West, country US/CA), SKTA Innopartners (SK Telecom Americas VC arm - ecosystem reference)
- Flagged for deletion (11): Riversand (No ICP fit - MDM/PIM software vendor), Ace Cloud Hosting (No ICP fit - app-hosting reseller on 3rd-party DCs), MyRealData (No ICP fit - same operator as Ace, likely dup), Intellinet (No ICP fit - IT consultancy, FPT-owned), Recursal AI (No ICP fit - serverless AI inference platform), Replicate (No ICP fit - AI model platform, Cloudflare-acquired), FCR Investments (No ICP fit - real-estate investment), SEOX (No ICP fit - marketing agency), Bits in Flight (Hard junk / non-business - personal advisory brand), OIB (Hard junk / non-business - nonprofit association), Ibghy Architectes (No ICP fit - architecture firm)

*What needs Cooper's attention:*
- 0 Tier 3 holds this run - every processable record got a definitive write (20 ICP / 3 Other / 11 Flagged). No deferrals.
- 11 hard-flagged companies now in HubSpot Companies filter customer_segment = "Flagged for deletion" (with flagged_for_deletion_reason populated) - ready for Cooper's manual bulk-delete review.
- 4 dedup relationships surfaced for R3: (1) Telenor Pakistan -> PTCL parent; (2) Reliance Industries -> Reliance Jio; (3) Assembly/assembly.nl -> Nebul; (4) MyRealData -> Ace Cloud Hosting (both flagged). Plus FPT Software / Intellinet are related FPT entities (not a dup, noted for awareness).
- 3 Enterprise scale-gate classifications (Swiss Re, Swiss Life, FPT Software) used inferred (not documented) in-house net-eng signal - spot-check recommended.

*Run health:* GREEN
- Full processable pool drained (34/34), 0 HubSpot write failures (5 batches, all 10/10-or-fewer OK), gate-pass rate 100%, 0 Apollo pressure, 0 Tier 3 holds, all 4 end-of-pipeline self-checks PASS.

*Errors:* None

---

End-of-pipeline self-checks:
1. Sub-segment nullness check: PASS - all 20 ICP writes carry a populated company_sub_segment.
2. Confidence-evidence alignment check: PASS - all 6 ICP high_90 writes (Vivo, DISH, RIL, LuxProvide, Neysa, Bit Digital) carry named anchor/archetype + structured-marker evidence.
3. Disqualifier audit check: PASS - all 3 Other writes (Indus Towers, SambaNova, SKTA) cite the D1 / category disqualifier in account_brief.
4. Catch-all guard check: PASS - the single Regional CLEC (LitFiber) carries positive F1 evidence (FTTP overbuilder, owns last-mile plant, sells residential + business, multi-state OH/TX).

---

Path α - Full ICP write table

```
Account                       | HubSpot ID    | Segment                         | Sub-segment                          | Tier   | Conf
LitFiber                      | 326710261493  | Fiber Operator                  | Regional CLEC - Fiber operator       | tier_3 | medium_7089
Telenor Danmark               | 326381387478  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_2 | medium_7089
Telenor Pakistan              | 326642119370  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_2 | medium_7089
Telenor Sweden                | 326692100825  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_2 | medium_7089
T-Mobile Polska               | 326390414028  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_2 | medium_7089
Vivo (Telefonica Brasil)      | 326168029929  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_1 | high_90
DISH Network                  | 326722976489  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_1 | high_90
Reliance Industries / Jio     | 326735587023  | Network Operator(Tier 1 / VNO)  | Tier 1 Carrier - Network Op          | tier_1 | high_90
LuxProvide                    | 326585995981  | NeoCloud                        | Sovereign AI Clouds - Neocloud       | tier_1 | high_90
STACKIT                       | 326722976497  | NeoCloud                        | Sovereign AI Clouds - Neocloud       | tier_1 | medium_7089
exoscale                      | 326390414029  | NeoCloud                        | Sovereign AI Clouds - Neocloud       | tier_1 | medium_7089
Neysa Networks                | 326154804931  | NeoCloud                        | Large Scale GPU - Neocloud           | tier_1 | high_90
Denvr Dataworks               | 326585989844  | NeoCloud                        | AI Infrastructure providers - Neocloud| tier_1 | medium_7089
Bit Digital                   | 326712100572  | NeoCloud                        | Crypto to AI - Neoclouds             | tier_1 | high_90
iGenius / Domyn               | 326694120171  | NeoCloud                        | Sovereign AI Clouds - Neocloud       | tier_1 | medium_7089
YTL                           | 326699661004  | NeoCloud                        | Large Scale GPU - Neocloud           | tier_1 | medium_7089
Assembly / Nebul              | 326646278880  | NeoCloud                        | Sovereign AI Clouds - Neocloud       | tier_1 | medium_7089
Swiss Re                      | 326381387481  | Enterprise-CustomerSegment      | Financial Services - Enterprise      | tier_3 | medium_7089
Swiss Life                    | 326644735707  | Enterprise-CustomerSegment      | Financial Services - Enterprise      | tier_3 | medium_7089
FPT Software                  | 326715774698  | Enterprise-CustomerSegment      | Outsourcing Services - Enterprise    | tier_3 | medium_7089
```

Path β - reclassification table: none this run

Path γ - eviction table

```
Account              | HubSpot ID    | Outcome               | Reason
Indus Towers         | 326712109770  | Other / tier_5        | Passive tower infra lessor; ecosystem reference, not connectivity operator
SambaNova Systems    | 326710146783  | Other / tier_5        | D1 equipment-vendor (AI chip co); competitive reference (owner -> Ken, US/CA)
SKTA Innopartners    | 326674183868  | Other / tier_5        | SK Telecom Americas VC arm; ecosystem/investor reference
Riversand            | 326745988819  | Flagged for deletion  | No ICP fit: MDM/PIM software vendor
Ace Cloud Hosting    | 326745948917  | Flagged for deletion  | No ICP fit: app-hosting reseller on 3rd-party DCs
MyRealData           | 326735606513  | Flagged for deletion  | No ICP fit: same operator as Ace (likely dup)
Intellinet           | 326701494983  | Flagged for deletion  | No ICP fit: IT consultancy (FPT-owned)
Recursal AI          | 326717559539  | Flagged for deletion  | No ICP fit: serverless AI inference platform
Replicate            | 326644726503  | Flagged for deletion  | No ICP fit: AI model platform (Cloudflare-acquired)
FCR Investments      | 326819944180  | Flagged for deletion  | No ICP fit: real-estate investment firm
SEOX                 | 326690362102  | Flagged for deletion  | No ICP fit: SEO/marketing agency
Bits in Flight       | 326674182894  | Flagged for deletion  | Hard junk / non-business: personal advisory brand
OIB                  | 326719389425  | Flagged for deletion  | Hard junk / non-business: nonprofit association
Ibghy Architectes    | 326175264490  | Flagged for deletion  | No ICP fit: architecture firm
```

Tier 3 hold table: none this run (0 holds)
Partial gate failure table: none this run (0 partials)

Excluded this run (31 standing Tier 3 / R3-dedup holds, verified against canvas F0B0AFSB9LN): T-HT Croatia, Ooredoo consultants, bb.softbank, wechsler, SoftBank Capital, bertellifamily, terrycorder, Desert Lakes Capital, Poly-AI, PolyAI, C3i, one.verizon, corp.fibernetics, ConvergeOne, niusgov, staff.win.be, dna-communications, Cityside Networks, indatelservices, teampoka, us.ntt.net, Digital Fortress, g.softbank, Verizon, columbus-networks, gatco, Synnap, Spartan Data Centers, Attobahn, Tract Capital, LS Power.
