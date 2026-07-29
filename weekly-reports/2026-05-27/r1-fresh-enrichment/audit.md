# R1 Fresh Enrichment - Audit Log - 2026-05-27

## Run summary
- Pool: 108 candidates (6 Tier 3 client-side excluded -> 102 actionable)
- Dynamic cap: 100 records/run
- Processed: 100 records (deferred: Twin Lakes 324628839134, ResetData 324591600333)
- Path α full ICP writes: 59
- Path γ Other vendor-keeps: 33
- Path γ HARD_DELETE: 5
- Tier 3 holds: 3
- Apollo credits consumed: 0
- All 4 end-of-pipeline self-checks: PASS
- BACKLOG ELEVATED flag: TRUE (102 active vs ~15-record steady-state)

## Writes (97 total)

- 324633547482 Plumas-Sierra Rural Electric Cooperative: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324525489884 Maquoketa Valley Electric Cooperative: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324650983125 Sequachee Valley Electric Cooperative: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324534174410 Etex Telephone Cooperative: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324534447805 : alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324534167255 Pineland Telephone Cooperative: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324493462230 Norvado: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324628854464 3 Rivers Communications: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324628807415 West Carolina: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324498818750 NITCO: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324617780979 SRT Communications: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324274927326 TCT: alpha Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90
- 324534440655 BAI Connect: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089
- 324542613223 Vistabeam: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / high_90
- 324650983123 Genesis Wireless: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_5 / medium_7089
- 324605237997 Blue Mountain Networks: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / medium_7089
- 324525489876 Hilliary Communications: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90
- 324599849708 VERO Broadband: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089
- 324208873160 Lightwire: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / high_90
- 324566401760 Rally Internet: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / medium_7089
- 324007854794 Comtel: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / high_90
- 324605005505 WIOCC: alpha Network Operator(Tier 1 / VNO) / International Backbone Specialist - Network Op / tier_1 / high_90
- 324628785885 JPMorgan Chase: alpha Enterprise-CustomerSegment / Financial Services - Enterprise / tier_3 / high_90
- 324617947897 Banco Santander: alpha Enterprise-CustomerSegment / Financial Services - Enterprise / tier_3 / high_90
- 324626936514 Virgin Media O2: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90
- 324617980617 Fastweb Vodafone: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90
- 324525213424 Rakuten Group: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90
- 324617805498 KDDI America, Inc.: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90
- 324508030666 Astound: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_2 / medium_7089
- 324591652598 Mediacom Communications: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_2 / high_90
- 324274927322 ATOM: alpha Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_2 / high_90
- 324525241063 N+ONE DATACENTERS: alpha Data Center Colo Provider / Standard - colo / tier_3 / high_90
- 324597812960 KEVLINX: alpha Data Center Colo Provider / Standard - colo / tier_3 / high_90
- 324508030668 S-NET Communications, Inc.: alpha MSP/Aggregator / Managed Network Services - MSP / tier_4 / medium_7089
- 324508030662 Stratus ip: alpha MSP/Aggregator / Managed Network Services - MSP / tier_4 / medium_7089
- 324566401740 Spectrotel: alpha MSP/Aggregator / Telecom Aggregator - MSP / tier_3 / high_90
- 324566401747 FG (Fiberutilities Group): alpha MSP/Aggregator / Managed Network Services - MSP / tier_4 / medium_7089
- 324566401746 Wavenet: alpha MSP/Aggregator / Managed Network Services - MSP / tier_3 / high_90
- 324273199821 TelePacific Communications (TPx Communications): alpha MSP/Aggregator / Managed Network Services - MSP / tier_2 / high_90
- 324498818748 Aryaka: alpha MSP/Aggregator / Managed Network Services - MSP / tier_2 / high_90
- 324208154350 Magna5: alpha MSP/Aggregator / Managed Network Services - MSP / tier_3 / high_90
- 324591653602 OptConnect: alpha MSP/Aggregator / Managed Network Services - MSP / tier_4 / medium_7089
- 324498817734 Lightstream.io - Cloud, Security, & Connectivity Solutions: alpha MSP/Aggregator / Managed Network Services - MSP / tier_4 / medium_7089
- 324628802251 Hughes: alpha MSP/Aggregator / Managed Network Services - MSP / tier_3 / high_90
- 324498817783 Novanet: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / medium_7089
- 324566401744 Skywire Networks: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / medium_7089
- 324271404792 Commnet Broadband: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90
- 324498817738 Wire 3: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90
- 324534164217 Vero Fiber: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_2 / high_90
- 324535467707 TachusFiber: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90
- 324603094737 YouFibre: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90
- 324508029675 Complutel Comunicaciones: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / medium_7089
- 324525206259 Giant Communications Group: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / medium_7089
- 324498817750 Gamma Comunicaciones: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / low_5069
- 324599570160 Home Telecom: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_4 / high_90
- 324542341829 Vyve Broadband: alpha Fiber Operator / Regional Cable Operator - Fiber operator / tier_3 / high_90
- 324542341828 Gateway Wireless LLC: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_5 / medium_7089
- 324628803291 Avatel Technologies: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / medium_7089
- 324617780936 Glo Fiber Business: alpha Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90
- 324534484667 ONUG: gamma Other /  / tier_5 / high_90
- 324007854791 Hispasat: gamma Other /  / tier_5 / high_90
- 324624884456 Rivada Space Networks: gamma Other /  / tier_5 / high_90
- 324603094742 SORACOM: gamma Other /  / tier_5 / high_90
- 324617902793 Eutelsat OneWeb: gamma Other /  / tier_5 / high_90
- 324599578316 Astranis Space Technologies: gamma Other /  / tier_5 / high_90
- 324599578315 Skylo: gamma Other /  / tier_5 / high_90
- 324599578320 Eutelsat: gamma Other /  / tier_5 / high_90
- 324626904811 ORBCOMM: gamma Other /  / tier_5 / high_90
- 324626904813 Intelsat: gamma Other /  / tier_5 / high_90
- 324525207286 Eutelsat America: gamma Other /  / tier_5 / high_90
- 324604972737 Eutelsat Network Solutions: gamma Other /  / tier_5 / high_90
- 324617772772 Globalstar: gamma Other /  / tier_5 / high_90
- 324271404754 AST SpaceMobile: gamma Other /  / tier_5 / high_90
- 324599576298 Harmoni Towers: gamma Other /  / tier_5 / high_90
- 324605639375 Everest Infrastructure Partners: gamma Other /  / tier_5 / high_90
- 324603089647 TowerCo: gamma Other /  / tier_5 / high_90
- 324617780972 Torrecom Partners LP: gamma Other /  / tier_5 / high_90
- 324624875216 Wireless Infrastructure Group: gamma Other /  / tier_5 / high_90
- 324624873165 Tillman Infrastructure, LLC: gamma Other /  / tier_5 / high_90
- 324273199835 Patriot Mobile: gamma Other /  / tier_5 / high_90
- 324566401745 OXIO: gamma Other /  / tier_5 / high_90
- 324617922269 Ultra Mobile: gamma Other /  / tier_5 / high_90
- 324525209276 KORE: gamma Other /  / tier_5 / high_90
- 324617896669 BeMobile, Inc: gamma Other /  / tier_5 / medium_7089
- 324617780965 Finetwork: gamma Other /  / tier_5 / high_90
- 324617792192 Telrite Holdings, Inc: gamma Other /  / tier_5 / medium_7089
- 324525211383 Anterix: gamma Other /  / tier_5 / high_90
- 324617902795 Boingo Wireless: gamma Other /  / tier_5 / high_90
- 324508030663 Infrastructure Networks: gamma Other /  / tier_5 / high_90
- 324525213410 CSL Group: gamma Other /  / tier_5 / high_90
- 324525213412 Skyloom Global: gamma Other /  / tier_5 / high_90
- 324274926305 Gogo: gamma Other /  / tier_5 / high_90
- 324615281396 Bright House Networks: gamma_delete Flagged for deletion /  /  / high_90
- 324617842385 Grande Communications Networks LLC: gamma_delete Flagged for deletion /  /  / high_90
- 324617772770 Astound Broadband: gamma_delete Flagged for deletion /  /  / high_90
- 324617780956 AT&T - Communication Solutions: gamma_delete Flagged for deletion /  /  / high_90
- 324273199819 MOBILY LLC: gamma_delete Flagged for deletion /  /  / high_90

## Tier 3 holds (3)

- 324628807414 Pineland Telephone Cooperative, Inc.: Likely duplicate of 324534167255 Pineland Telephone Cooperative (pinelandtelco.com vs pineland.net). Hold for R3 dedup verification.
- 324498817751 Giant Communications: Likely duplicate of 324525206259 Giant Communications Group (giantcommllc.com vs giantcomm.net). Hold for R3 dedup verification.
- 324597786339 columbus-networks: Name "columbus-networks" but domain finetechnologies.co - apparent MISDOMAIN or stale name. Columbus Networks was rebranded Liberty Networks (LLA subsidiary) and uses libertynetworks.com; finetechnologies.co does not match any obvious operator. Hold for MISDOMAIN investigation by R3 dedup or D7 deep research.

## Slack DM
- Parent: https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1779896123396239
- Thread (tables): https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1779896155771319

## Canvas
- F0B0AFSB9LN: R1 Fresh Enrichment 2026-05-27 Tier 3 holds added section + Run log row appended
