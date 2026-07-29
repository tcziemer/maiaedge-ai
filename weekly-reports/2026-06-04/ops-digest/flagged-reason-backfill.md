# Flagged-for-Deletion Reason Backfill - 2026-06-04

Scope: the 214 flagged companies that had no `flagged_for_deletion_reason`. Wrote concrete reasons to **177**; held **37** out of the write because they read as active ICP / competitor / ambiguous and should be reviewed, not deleted.

## Reasons written (by code)

| Reason code | Count |
|---|---|
| D1 disqualified (no reference value) | 72 |
| No ICP fit | 37 |
| Duplicate (merged) | 30 |
| Defunct / out of business | 28 |
| Hard junk / non-business | 10 |
| **Total written** | **177** |

## Held back - NOT written (apparent mis-flags, recommend review)

These 37 carry no deletion reason; each reads as an active ICP, a competitor that belongs in `Other`, or a genuinely ambiguous record. Recommend reinstatement / re-enrichment rather than deletion.

| Company | Domain | ID | Why held |
|---|---|---|---|
| MTA | Alasconnect | mtasolutions.com | 253675894488 | MTA / AlasConnect - Alaska fiber co-op + AlasConnect MNS subsidiary; brief states Tier 3 Fiber Op ICP fit. Not a delete. |
| Spry Servers | spryservers.net | 268208452323 | Spry Servers - brief is contaminated with MaiaEdge outreach copy (data-quality); re-research before any delete. |
| Lumen Technologies | centurylink.com | 296880096970 | Lumen Technologies - Tier 1 incumbent and a direct NaaS competitor (PCF). Belongs in 'Other' as a competitive reference, not deleted. |
| Saturn Cloud | saturncloud.io | 297918677722 | Saturn Cloud - GPU/MLOps platform. NeoCloud-boundary call; confirm before delete. |
| Inferless | inferless.com | 297918677724 | Inferless - serverless GPU inference platform. NeoCloud-boundary call; confirm before delete. |
| Cerebrium | cerebrium.ai | 297918677725 | Cerebrium - serverless AI infra (YC-backed). NeoCloud-boundary call; confirm before delete. |
| TensorDock | tensordock.com | 297987984067 | TensorDock - GPU cloud marketplace (acquired by Voltage Park). NeoCloud-boundary call; confirm before delete. |
| Novita AI | novita.ai | 300372855493 | Novita AI - GPU cloud + inference APIs. NeoCloud-boundary call; confirm before delete. |
| Armstrong Group | armstrongonewire.com | 303892660925 | Armstrong Group - regional PA fiber operator/CLEC serving 400K+ homes; brief states MaiaEdge relevance. Fiber Operator ICP, not a delete. |
| FPX AI | fpx.world | 311392963281 | FPX AI - GPU trading marketplace. NeoCloud-boundary call; confirm before delete. |
| Lonestar Data Holdings | lonestarlunar.com | 311409164986 | Lonestar Data Holdings - off-world/lunar data storage novelty. Out-of-scope but unusual; confirm before delete. |
| LS Power | lspower.com | 311418164947 | LS Power - independent power co with 780+ mi transmission. Known data-quality follow-up; review, not a blind delete. |
| IREN | irisenergy.co | 315977374429 | Active NeoCloud (Crypto-to-AI) - IREN AI/HPC operator. ICP, not a delete (likely dup of iren.com). |
| Bluebird Network | bluebirdnetwork.com | 316163237567 | Active fiber+colo operator (11K-mi MO backbone, underground DC). ICP; verify vs Bluebird Fiber dup, not a blind delete. |
| Yondr | overyondr.com | 316194606814 | Yondr - hyperscale DC developer/operator, 878MW contracted. Colo/Greenfield ICP candidate, not a delete. |
| Fastlink | fast-link.com | 316196415207 | Fastlink - major mobile/broadband operator, Kurdistan Iraq. Network Operator ICP candidate (intl), not a delete. |
| Citizens Telephone Cooperative | citizensdsl.com | 316197305048 | Active fiber co-op (650-mi FTTH + 440-mi open-access wholesale). Fiber Operator ICP, not a delete. |
| United Cooperative Services | united-cs.com | 316197305049 | Electric co-op with 20K+ mi fiber, 34K broadband subs. Fiber Operator (Municipal/Coop) ICP, not a delete. |
| Madison Communications | gomadison.com | 316197317360 | Regional fiber operator (Madison County IL). Fiber Operator ICP, not a delete. |
| Telesom | telesom.com | 316203554520 | Telesom - leading mobile/internet operator, Somaliland. Network Operator ICP candidate (intl), not a delete. |
| S&T Communications | st-tel.net | 316218856147 | S&T fiber telephone co-op (KS). Fiber Operator (Municipal/Coop) ICP, not a delete. |
| Unifi | unifi.com.my | 316282051272 | Unifi - Telekom Malaysia retail broadband brand (3M+ fiber subs). Likely dup of Telekom Malaysia; review, not a blind delete. |
| Telekom2 | telecom2.net | 316283788007 | Telekom2 - UK telco that 'owns some infrastructure' incl. colocation. Possible small ICP; review, not a blind delete. |
| AGIL TELECOM | agiltelecomsp.com.br | 316287384261 | AGIL Telecom - Brazilian operator with regional network infra + carrier customers. Possible ICP; review, not a blind delete. |
| HIVE Digital Technologies | hivedigitaltechnologies.com | 316412310231 | NeoCloud (Crypto-to-AI) - BUZZ HPC, 2,000 GPUs w/ Bell Canada, 320MW AI campus. ICP, not a delete. |
| Airtel Business | africa.airtel.com | 317223880415 | Airtel Business - wholesale arm of Bharti Airtel (14+ African countries). Likely D2 wholesale-arm dup; review, not a blind delete. |
| Summit Broadband | summit-broadband.com | 317745346241 | Regional fiber operator (FL), 2,700 route mi, dark fiber + wholesale. Fiber Operator ICP, not a delete. |
| Onemax | onemax.com.do | 319135982321 | DR enterprise ISP - fiber GPON, AS28053, own microwave net. Network/Fiber ICP candidate (intl), not a clear delete. |
| ALLO Communications | allofiber.com | 320861822686 | Active FTTH fiber operator (Nebraska/CO/AZ). Fiber Operator ICP, not a delete. |
| Unifique | redeunifique.com.br | 321768447684 | Brazil's largest independent fiber operator (816K subs); brief states MaiaEdge fit. ICP, not a delete. |
| Northwest Open Access Network | noanet.net | 322364279513 | WA wholesale open-access fiber co-op (every county). Fiber Operator ICP, not a delete. |
| Schurz Communications | schurz.com | 322405958358 | Schurz Broadband Group - 6 cable/fiber subsidiaries, FLIGHT FIBER. Fiber Operator ICP, not a delete. |
| Riot Platforms, Inc. | riot.inc | 322537130689 | NeoCloud (Crypto-to-AI); brief explicitly states ICP fit, Tier 2. Should not be flagged. |
| altafiber | cinbell.com | 322686735045 | altafiber - regional ILEC-heritage fiber operator, 14K route miles; brief states Tier 2 ICP. Not a delete. |
| Ohio Gig | ohiogig.com | 323821758148 | Ohio Gig - fiber ISP (thin brief); 'titles suggest operator'. Possible Fiber Operator ICP; needs enrichment, not a delete. |
| Hut 8 | hut8.com | 323823198916 | NeoCloud (Crypto-to-AI); brief says this is the CANONICAL record selected over a dup. Should not be flagged. |
| IREN | iren.com | 323971392219 | Active NeoCloud (Crypto-to-AI) - $9.7B Microsoft GPU-cloud contract, 23K GPUs. ICP, not a delete. |

## Full written list

| Company | Domain | Code | Reason |
|---|---|---|---|
| Truepacket | truepacket.io | D1 disqualified (no reference value) | D1 disqualifier: insufficient evidence of operating telecom or carrier-grade infrastructure. |
| ngenious | ngenious.ca | D1 disqualified (no reference value) | They are a product vendor distributing through Telarus, not a network operator or MSP with infrastructure. |
| wilson-global | wilson-global.com | D1 disqualified (no reference value) | wilson-global has limited public footprint; the most prominent Wilson Global Communications match is a strategic public relations and communications consulting firm (DC and South Africa origin) focused on Africa/Europe/China/Brazil PR work. |
| Sumauma | sumaumatelecom.com.br | D1 disqualified (no reference value) | Sumauma Telecom is a Sao Paulo, Brazil B2B telecom software and consulting firm in business since 1998, providing software development, CRM integration, contact-center solutions, and technical support to telecommunications operators. |
| Touchtone | touchtonecorp.com | D1 disqualified (no reference value) | D1 disqualifier: legacy enterprise software vendor, not a telecom operator or aggregator. |
| GCI Liberty | gciliberty.com | Duplicate (merged) | DUPLICATE entity. |
| GAC | gac.com | D1 disqualified (no reference value) | D1 disqualifier: logistics company. |
| CTel | ctel.us | D1 disqualified (no reference value) | D1 disqualifier: niche correctional-vertical telecom, not a Telecom Aggregator or carrier-grade infrastructure provider. |
| PAETEC Holding Corp. | paetec.com | Duplicate (merged) | R3 to dedupe into Windstream Wholesale (HID 133493528256) and primary Uniti record. |
| ATxTel | atxtel.com | D1 disqualified (no reference value) | ATxTel is a San Diego systems integration company providing test and measurement solutions for 5G, mmWave, WiFi, Ethernet, security, and environmental testing of telecom products. |
| 128 Technology | 128technology.com | Defunct / out of business | It is no longer an independent operating company. |
| nFrame (Expedient) | expedient.com | Defunct / out of business | nFrame no longer exists as an operating entity - Expedient is the surviving brand. |
| Lightower Fiber Networks | lightower.com | Duplicate (merged) | R3 to dedupe contacts into Zayo primary. |
| ECI | eci.com | D1 disqualified (no reference value) | ECI Software Solutions is a New York-headquartered manufacturing and distribution ERP vendor with about 900 employees across North America, Europe, and Asia. |
| Resolve Tech Solutions | resolvetech.com | D1 disqualified (no reference value) | D1 disqualifier: SAP and IT modernization consultancy. |
| FlowSec | flow-sec.com | D1 disqualified (no reference value) | FlowSec is a Tel Aviv-based network security company (about 5 employees) focused on DDoS protection and global shield offerings for hosting customers. |
| Techmate | techmate.com | D1 disqualified (no reference value) | Techmate is an on-demand IT support and smart-hands marketplace headquartered in New York City, with a network of 7,000+ vetted technicians across 350+ cities in the US, Canada, UK, and EU. |
| Everstream | everstream.net | Defunct / out of business | Filed Chapter 11 in May 2025; acquired by Bluebird Fiber for $384.6M (closed Aug 2025). |
| ISG | isginc.com | D1 disqualified (no reference value) | D1 disqualifier: architecture and planning firm, not a telecom operator or aggregator. |
| toto networks | totonetworks.com | D1 disqualified (no reference value) | D1 disqualifier: insufficient evidence of operating a Sub-Regional Fiber footprint or a real MSP aggregation business at scale. |
| Virtustar | virtustar.com | D1 disqualified (no reference value) | Virtustar is a minority-owned technology consultancy in Reston, VA delivering cloud, AI/ML, cybersecurity, and 5G/IoT integration services to SMBs and Fortune 100 customers. |
| Ni2 | ni2.com | D1 disqualified (no reference value) | Montreal-based BSS / inventory / quoting software vendor for connectivity service providers. |
| Cloud Age | cloudage.com | Duplicate (merged) | Likely DUPLICATE of an existing Connectbase HubSpot record (if one exists) or a small enough acquired entity that the canonical Connectbase record is the right place to track. |
| rackonomics | rackonomics.ai | D1 disqualified (no reference value) | D1 disqualifier: thin commercial footprint, no infrastructure assets. |
| MANGO-OMC | omc.com | D1 disqualified (no reference value) | MANGO-OMC is a South African public relations and marketing agency founded in 2005, based in Cape Town with regional partners across Africa. |
| BHC | ibhc.com | D1 disqualified (no reference value) | D1 disqualifier: civil engineering services firm. |
| V-Tell | v-tell.com | D1 disqualified (no reference value) | V-Tell is a Hong Kong-based consumer VPN application distributed via Google Play, with about 45 employees and a Kowloon address. |
| CarrierX | carrierx.com | D1 disqualified (no reference value) | Programmable voice + messaging CPaaS platform headquartered Long Beach CA. |
| Corero | corero.com | D1 disqualified (no reference value) | Corero is a network DDoS protection vendor (SmartWall ONE platform with TLS protection, Zero Trust Admission Control, expanded application security). |
| Switch Connect Pty Ltd | wiconnectglobal.com | D1 disqualified (no reference value) | Entity / geography mismatch. |
| Arteria Technologies Private Limited | arteriatech.in | D1 disqualified (no reference value) | Bengaluru India supply-chain SaaS + embedded finance company founded 2007. |
| On Air Telecom | navitelecom.cn | D1 disqualified (no reference value) | Entity / domain mismatch. |
| SB Communications Private Limited | yscommunications.net | D1 disqualified (no reference value) | Insufficient evidence for any ICP sub-segment. |
| Elve, Inc. | evolve.co.uk | D1 disqualified (no reference value) | Entity / domain mismatch and no positive evidence for any ICP sub-segment. |
| TGT Global | csggc.com | D1 disqualified (no reference value) | Insufficient evidence for any ICP sub-segment + entity ambiguity. |
| MaxCell | excellgroup.com | D1 disqualified (no reference value) | Entity / domain mismatch. |
| Edged Data Centers | edged.ai | Duplicate (merged) | Confirmed duplicate of canonical record 251592703686 (Edged Energy, edged.us). |
| Fastrack Technology Pty Ltd | datalec.ph | D1 disqualified (no reference value) | Cannot disambiguate to a single coherent ICP-eligible account. |
| Sipify LLC | sipcity.com.au | D1 disqualified (no reference value) | Entity / domain mismatch. |
| Network Wireless Solutions | network2000.co.uk | D1 disqualified (no reference value) | Insufficient evidence for ICP qualification; flag for deletion per operating principle #7. |
| China Telecm Americas | sbtelecom.net | Duplicate (merged) | Duplicate of canonical China Telecom Americas record (companyId 253166672620). |
| Eastern Communications Ltd. | easterncomm.com | D1 disqualified (no reference value) | 60+ year old mission-critical RF / two-way radio system integrator headquartered Long Island City NY (correct domain easterncommunications.com, not easterncomm.com). |
| TEECOM | gtelecom.com.au | D1 disqualified (no reference value) | TEECOM identity mismatch: name 'TEECOM' suggests teecom.com (US AV/IT integration consultancy, non-ICP). |
| C7 Data Centers | c7datacenters.com | Duplicate (merged) | Likely DUPLICATE of an existing DataBank HubSpot record. |
| FPL FiberNet | fplfibernet.com | Duplicate (merged) | This record duplicates Crown Castle Fiber / Zayo. |
| ColoSpace | colospace.com | Defunct / out of business | Entity is defunct; FirstLight (parent) is the operating record going forward. |
| US Internet | usinternet.com | Duplicate (merged) | Flagged for deletion - dedup vs T-Mobile parent record. |
| ColoHouse | colohouse.com | Duplicate (merged) | Flagged for deletion - duplicate of Hivelocity (id 254575820474, post-merger primary). |
| RagingWire Data Centers | ragingwire.com | Duplicate (merged) | Flagged for deletion - dedup vs NTT Global Data Centers (matches CLAUDE.md follow-up #3 on NTT dedup pairs). |
| Directlink Technologies | directlinktechnology.com | D1 disqualified (no reference value) | Apollo wrong-matched to DirectLTx during prior re-enrichment; the actual entity at the domain has no public footprint to support classification into any of the 30 active sub-segments. |
| Pac-West Telecomm | pacwest.com | Defunct / out of business | Pac-West Telecomm was a California CLEC that filed Chapter 11 in 2010 and was acquired by Granite Telecommunications; the original CLEC entity is defunct. |
| LightSpeed Technologies | lsti.net | D1 disqualified (no reference value) | Fixed-wireless WISP profile at this scale aligns with the retail residential ISP D1 disqualifier rather than the Fiber Operator ICP. |
| Core NAP (Zayo zColo) | corenap.com | Defunct / out of business | Flagged for deletion as a defunct subsidiary; Zayo Group is the active CRM record. |
| Hostrunway | hostrunway.com | D1 disqualified (no reference value) | The site model and lack of verifiable owned infrastructure or independent corporate presence are consistent with a hosting reseller or marketplace rather than an operator. |
| tw telecom | twtelecom.com | Defunct / out of business | Flagged for deletion as defunct. |
| Sparrow Technology Solutions | sparrowtechsolutions.com | D1 disqualified (no reference value) | Sparrow Technology Solutions - Apollo data indicates Pakistan-based management consulting firm (state Punjab, industry MANAGEMENT_CONSULTING). |
| vXchnge | vxchnge.com | Defunct / out of business | vXchnge effectively wound down its colocation operations through portfolio divestments - H5 Data Centers acquired 7 vXchnge facilities (Jan 2022, 250,000+ sqft), Cologix acquired the Santa Clara campus (May 2021) and Minneapolis facility (Sept 2020). |
| Westelcom Networks | westelcomnetworks.com | Duplicate (merged) | Flagged for deletion - dedup vs SLIC Network Solutions parent record. |
| Steadfast Networks | steadfast.net | Duplicate (merged) | Flagged for deletion - dedup vs Hivelocity (id 254575820474). |
| Sungard Availability Services | sungardas.com | Defunct / out of business | Sungard Availability Services in run-off / wind-down post-2022 Chapter 11; DR business sold to 11:11 Systems (formerly iland); remaining colo/managed services divested. |
| TelJet | teljet.com | Duplicate (merged) | Flagged for deletion - dedup vs FirstLight Fiber record. |
| Cavalier Telephone | cavalier.net | Defunct / out of business | Cavalier Telephone is a defunct US CLEC - acquired by Talk America 2007, rolled into PaeTec 2010, then absorbed into Windstream 2011, with the brand effectively retired into Windstream / Kinetic operations. |
| Vault Networks | vaultnetworks.com | Defunct / out of business | Combination of large facility claim, minimal headcount, and decade-old news suggests defunct or substantially diminished operations. |
| ByteGrid | bytegrid.com | Defunct / out of business | Entity is defunct: Lincoln Rackhouse acquired the full portfolio in 2019-03, and DataBank subsequently acquired three former ByteGrid facilities (Aurora IL, Cleveland OH, Silver Spring MD) from Lincoln Rackhouse in 2020-12. |
| Secured Network Services | sns.com | Duplicate (merged) | Flagged for deletion - dedup vs Thrive parent record. |
| IDACORE | idacore.com | D1 disqualified (no reference value) | Flagged for deletion as a misclassified electric utility lacking positive evidence for any ICP sub-segment; D1 disqualifier (energy utility, not network infrastructure operator). |
| NSW | prysmian.com | D1 disqualified (no reference value) | NSW is a brand within Prysmian Group - submarine telecom + power cable MANUFACTURER and installer. |
| Atherton Fiber | athertonfiber.com | Duplicate (merged) | Acquired by Race Communications in August 2025 and flagged for R3 deduplication / consolidation under primary Race Communications record. |
| Shaw | shaw.ca | Duplicate (merged) | Acquired by and integrated into Rogers Communications in April 2023; flagged for R3 deduplication / consolidation under primary Rogers record. |
| Barrett Networks | barrettnetworks.com | D1 disqualified (no reference value) | Barrett Networks (barrettnetworks.com) is a 1-employee web hosting and reseller hosting provider - not a telecom aggregator, not an MSP in the traditional managed-network sense. |
| Netmore Group | netmoregroup.com | No ICP fit | Netmore Group (Stockholm Sweden HQ) is a global LoRaWAN / Low-Power Wide-Area Network (LPWAN) IoT network operator, not a fiber operator. |
| Globix | globix.com | Duplicate (merged) | Recommend deletion - dedup-eviction case. |
| Troy Cablevision | troycable.com | Duplicate (merged) | Recommend deletion - duplicate of C Spire (already in CRM as separate record). |
| Wilcon Holdings | wilconholdings.com | Defunct / out of business | Flagged for deletion as a defunct brand - reassociate any active contacts to the Crown Castle (future Zayo) parent record via R3 consolidation. |
| OctoAI | octoai.cloud | Defunct / out of business | Acquired by NVIDIA in September 2024 for approximately $165-250M; standalone inference platform wound down with engineering folded into NVIDIA AI Enterprise and NIM. |
| Electra Telephone | electratel.net | Defunct / out of business | Apollo shows 1 employee, confirming Electra Telephone is a defunct standalone brand with operations rolled into Hilliary. |
| Southern Light | slfiber.com | Defunct / out of business | Southern Light fiber assets were absorbed into Uniti Group in 2017; Uniti subsequently merged with Windstream in 2025. |
| VISI | visi.com | Defunct / out of business | VISI (founded 1994, Minnesota) was a regional data center and managed hosting provider acquired by TDS in 2010, integrated into OneNeck IT Solutions, then absorbed into US Signal via the September 2024 acquisition. |
| Heritage Networks | heritagenetworks.us | D1 disqualified (no reference value) | D1 disqualifier (IT services / cabling integrator, not a facilities-based fiber operator). |
| 4U Telecom | talk4utelecom.co.uk | D1 disqualified (no reference value) | Small UK telecom services reseller in Lancashire, no owned fiber or POP infrastructure. |
| Florida WiFi | florida-wifi.com | D1 disqualified (no reference value) | D1 disqualifier (IT services / MSP, not facilities-based fiber operator). |
| Imperial Technologies | imperialtechinc.com | D1 disqualified (no reference value) | Small-business technology reseller in Macon GA offering bundled internet, VoIP, mobile, smart security, GPS fleet tracking, and cable TV since 2014. |
| NDemand | ndemand.com | No ICP fit | Primarily fixed wireless, not a fiber-first operator. |
| Trainy | trainy.ai | D1 disqualified (no reference value) | San Francisco multi-cloud GPU orchestration SaaS (5 employees). |
| Cervalis | cervalis.com | Defunct / out of business | Acquired by CyrusOne for ~$400M in July 2015; brand was fully absorbed into CyrusOne's portfolio. |
| Hivenet | hivenet.com | D1 disqualified (no reference value) | Marketplace SaaS model outside MaiaEdge ICP scope. |
| Skymeric Technologies LLC | skymeric.com | D1 disqualified (no reference value) | Indian AI / RPA automation specialist (Pune-based) - PIVOTED out of telecom aggregator/reseller business. |
| Atlantic Metro Communications | atlanticmetro.net | Duplicate (merged) | Likely DUPLICATE of an existing 365 Data Centers record in HubSpot. |
| nFrame | nframe.com | Duplicate (merged) | Flagged for deletion as duplicate; the Expedient parent record is the canonical active ICP entry. |
| Essextel | essextel.com | D1 disqualified (no reference value) | Cloud VoIP reseller with no physical network infrastructure, no fiber, no backbone, no carrier operations. |
| Dorados Cloud |  | D1 disqualified (no reference value) | Provides network automation and SaaS-based CruzNow platform for multi-vendor IT stack monitoring and zero-touch orchestration. |
| The Compute Index, Inc | compute-index.com | D1 disqualified (no reference value) | [2026-05-18] Re-classified: not a compute provider per own description; financial analytics SaaS misclassified as NeoCloud. |
| HyperLink Infrastructure, LLC | hyperlink-networks.com | No ICP fit | In-house design, construction, and maintenance with owned equipment for full schedule control. |
| Qsera Telenet | qsera.com | D1 disqualified (no reference value) | Limited infrastructure ownership; primarily reseller model. |
| United Cable Company | unitedcablecompany.com | D1 disqualified (no reference value) | United Cable Company is a small US telecom reseller with 17 employees and no identified network infrastructure. |
| All Access Telecom | allaccesstelecom.com | D1 disqualified (no reference value) | D1 disqualifier; aggressive flag per operating principle #7. |
| Tollbridge | tollbridge.co | D1 disqualified (no reference value) | tollbridge.co is a digital-publishing paywall / subscription SaaS product built by Square1 (Stripe verified partner) for newspaper, magazine, radio, and digital publishers. |
| Top Networks | top-network.org | No ICP fit | top-network.org is 'ToP Network' - a professional networking ORGANIZATION (Technology of Participation methods training and certification, annual gatherings, 2025 board of directors), NOT a telecom carrier. |
| RW Infra | rwinfra.com | Defunct / out of business | Defunct entity or misdirected import; no positive evidence for any ICP sub-segment. |
| Star Global Solutions PTE LTD | starglobalsolutions.com | Defunct / out of business | Likely defunct or dormant. |
| Call48 | call48.com | D1 disqualified (no reference value) | Small Florida-based VoIP/calling-card services reseller (call48.com). |
| Azos Telecom Brasil | azostelecom.com.br | D1 disqualified (no reference value) | No verifiable Brazilian fiber ISP found at azostelecom.com.br. |
| Smart Telecom Uganda | smarttug.ug | Defunct / out of business | DEFUNCT - ceased operations 2021-08-31. |
| Caribbean Communications | carib.net | D1 disqualified (no reference value) | No verifiable Trinidad and Tobago telecom carrier operates at carib.net under the name 'Caribbean Communications'. |
| Dominica Telecom | dominicatelecom.dm | D1 disqualified (no reference value) | No verifiable Dominica national telecom operates at dominicatelecom.dm. |
| FirstLink | firstlink.net | D1 disqualified (no reference value) | No verifiable Puerto Rico colocation operator found at firstlink.net. |
| Mainstream Technologies Panama | mainstream.pa | D1 disqualified (no reference value) | No verifiable Panamanian carrier or ISP found at mainstream.pa. |
| TVRED El Salvador | tvred.sv | D1 disqualified (no reference value) | No verifiable telecom carrier operates under tvred.sv. |
| Arctel | arctel.com | D1 disqualified (no reference value) | No verifiable Icelandic telecom carrier operates under arctel.com. |
| Ooredoo Qatar Wholesale | ooredoo.qa | Duplicate (merged) | R3 dedup candidate: Ooredoo Group parent. |
| AST Alcance El Salvador | astesal.com.sv | D1 disqualified (no reference value) | No verifiable Salvadoran telecom carrier operates as 'AST Alcance' at astesal.com.sv. |
| ICT PNG | ict.pg | D1 disqualified (no reference value) | PNG regulator domains are nicta.gov.pg (NICTA) and ict.gov.pg (DICT); no verifiable carrier or operator uses ict.pg as its primary domain. |
| revine.io | revine.io | Hard junk / non-business | Domain appears stealth/dormant/placeholder. |
| Frigate Fiber |  | D1 disqualified (no reference value) | Frigate (frigate.ai) is a fiber optic cable manufacturer in India - equipment vendor, not a fiber operator. |
| VNET Fiber | vnetfiber.com | Duplicate (merged) | Sub-brand duplicate. |
| BitStream | bitstream.org | No ICP fit | Not a network operator, ISP, or infrastructure provider. |
| (blank) | aristotleweb.com | Duplicate (merged) | D7 EVICT 2026-05-27: Duplicate of canonical Aristotle Unified Communications Inc record 322837060291 (aristotlebroadband.com, Fiber Operator / Regional CLEC - Fiber operator). |
| Ellijay | ellijay.com | Duplicate (merged) | D7 EVICT 2026-05-27: Duplicate of canonical ETC Communications record 322836352712 (etcnow.com, Fiber Operator / Regional CLEC - Fiber operator). |
| Allegion | allegion.com | D1 disqualified (no reference value) | Allegion is a $3.27B Indianapolis-based security hardware manufacturer (~12,300 employees) - mechanical/industrial engineering industry, not in scope for any MaiaEdge ICP segment. |
| Pivotal Mobile eDiscovery | pme-discovery.com | No ICP fit | Pivotal Mobile eDiscovery (New York) is a legal eDiscovery services firm specializing in mobile device data extraction and review - not a carrier infrastructure entity. |
| Commercial Electronics | commercialelectronics.com | No ICP fit | Commercial Electronics (Virginia, ~150 employees, COMPUTER_HARDWARE industry) is a broadcast/AV/security electronics integrator - not a carrier or fiber operator. |
| Eric Hanselman | hanselman.net | Hard junk / non-business | Eviction rule applied - hanselman.net is the personal blog of Eric Hanselman, Chief Analyst at S&P Global Market Intelligence (formerly 451 Research, acquired by S&P). |
| I & S Group | is-grp.com | D1 disqualified (no reference value) | Category: A/E consultancy and infrastructure contractor - designs civil, utility, and connectivity projects for client operators but does not operate networks. |
| SwyftConnect | swyftconnect.com | Duplicate (merged) | Flagged for deletion as duplicate of the Swyft Fiber canonical record at company_id 322362482422 (domain swyftfiber.com, Fiber Operator, Regional CLEC sub-segment, fully enriched 2026-05-19). |
| Fast Wave | fastwavenetworks.com | D1 disqualified (no reference value) | FastWave Networks (fastwavenetworks.com) is a small property-managed-Wi-Fi ISP serving hotels, RV parks, and extended-stay properties with bundled TV, Internet, and Phone services. |
| Congruex | congruex.com | No ICP fit | Flagged for deletion because domain congruex.com serves Congruex (Crestview-backed broadband construction and engineering firm; clients are carriers AT&T, Charter, Comcast, Cox, Crown Castle, Google, Lumen, TDS, Verizon; 1,000-5,000 employees; category: construction/infrastr... |
| MOBILY LLC | mobilyllc.com | D1 disqualified (no reference value) | MOBILY LLC is an authorized AT&T retailer (Sugar Land TX) with US-wide AT&T storefront network; retail sales channel, no infrastructure. |
| Astound | wavebroadband.com | Duplicate (merged) | Note: wavebroadband.com is a legacy domain (Astound prime domain is astound.com) - flagged for R3 dedup. |
| Phoenix Communications, Inc. | phoenix-fiber.com | No ICP fit | (Shrewsbury MA fiber-optic construction/splicing/testing/restoration contractor; MassDOT Master Service Agreement; 135 employees; category: construction/infrastructure contractor). |
| KNET Co.,LTD. | e-knet.com | D1 disqualified (no reference value) | Flagged for deletion because domain e-knet.com serves KNET (Korean fiber microduct, fiber distribution frame, splicing closure manufacturer; part of Hexatronic Group since 2019; category: cable vendor/manufacturer). |
| Centerline | centerlinecommunications.com | No ICP fit | Flagged for deletion because domain centerlinecommunications.com serves Centerline (Audax PE-backed wireless/wireline/fiber design-build-maintain contractor; clients are carriers AT&T, Verizon, Comcast, Bell, American Tower; 1,500+ employees; category: construction/infrastru... |
| Bright House Networks | brighthouse.com | Defunct / out of business | Bright House Networks brand was fully retired in 2016 following Charter Communications acquisition; assets and customers fully absorbed into Charter Spectrum brand. |
| Astound Broadband | mygrande.com | Duplicate (merged) | mygrande.com is the legacy Grande Communications customer self-service portal subdomain (now Astound). |
| AT&T - Communication Solutions | comnow.net | D1 disqualified (no reference value) | Communication Solutions (comnow.net) is an authorized AT&T retail dealer with 24 storefronts in OK/TX/KS; retail sales channel, no infrastructure. |
| Grande Communications Networks LLC | grandecom.com | Defunct / out of business | Grande Communications brand fully absorbed into Astound Broadband 2021 following TPG/Stonepeak consolidation; legacy brand retired. |
| Fusion Telecom | fusiontelecomm.com | No ICP fit | UK contact-center / payment-compliance technology firm; not a network, colo, or cloud connectivity operator, outside ICP scope. |
| WONLEE Solutions Co., Ltd | neso.co.tz | No ICP fit | 5-employee Tanzania ICT firm with a name/domain mismatch and no infrastructure evidence for any ICP sub-segment. |
| All Access Telecom, Inc. | 1-to-all.com | No ICP fit | International wholesale voice-termination carrier (not fiber) with active FCC/state robocall enforcement risk; outside ICP scope. |
| Wtechlink Inc | wtechlink.com | No ICP fit | 8-employee Eastern Oregon ISP below MaiaEdge ICP scale with no observable infrastructure footprint. |
| Vodafone Kiribati | vodafone.com.mt | Hard junk / non-business | Conflated record: 'Vodafone Kiribati' name sits on the Vodafone Malta domain and geo; two unrelated entities on one record. |
| VariNet | varinet.ca | No ICP fit | Surrey BC pure voice-wholesale IXC; outside MaiaEdge ICP scope. |
| OneSource Cloud Corporation | onesourcecorp.com | No ICP fit | Managed Telecom Expense Management / BPO provider with no positive evidence for any ICP sub-segment. |
| Agile Data Sites | agiledatasites.com | Duplicate (merged) | Single facility integrated into the DataBridge Sites portfolio; DataBridge Sites is the operating parent record. |
| Data-Tech | data-tech.com | No ICP fit | Tampa SMB IT MSP with no telecom-aggregation, network, fiber, or colocation footprint. |
| Yrix | yrix.org | Hard junk / non-business | No substantive business presence found at yrix.org and no positive ICP evidence. |
| NWAX | nwax.net | No ICP fit | Non-profit Internet Exchange Point (peering), not a sellable fiber/MSP/colo ICP. |
| Merkle Standard | merklestandard.com | No ICP fit | Pure bitcoin-mining hosting provider with no AI pivot or carrier-neutral colo offering; outside ICP scope. |
| Empresa de Telecomunicaciones de Cuba | cubacel.cu | No ICP fit | Cuban state telecom (ETECSA); OFAC-prohibited counterparty that cannot be transacted with. |
| Neutrona Networks (Zayo) | crunchbase.com | Defunct / out of business | Neutrona Networks absorbed into Zayo Group; no standalone operating entity (record carried a placeholder crunchbase.com domain). |
| United Fiber & Data | unitedfd.com | Defunct / out of business | United Fiber & Data acquired by Lightpath Feb 2025; assets integrated and the relationship consolidated under Lightpath. |
| Fibertech Networks | fibertech.com | Defunct / out of business | Fibertech merged into Lightower (2015) then Crown Castle; no longer an operating entity. |
| 5c.ai | 5c.ai | Duplicate (merged) | Same entity as 5C Data Centers (canonical record 264355635939); evicted in favor of the canonical record. |
| PowerTransitions | power-transitions.com | No ICP fit | Power-generation asset operator redeveloping brownfield sites; not a network or DC operator and no fabric/carrier services. |
| Casair, | casair.net | Defunct / out of business | Casair broadband/fiber assets acquired by Point Broadband (2020); relationship consolidated under Point Broadband. |
| Dorial Telecom | dorial.com | No ICP fit | Small Miami wholesale VoIP carrier; voice-termination model outside MaiaEdge ICP scope. |
| Lanck Telecom | lancktele.com | No ICP fit | Wholesale voice / A2P-SMS aggregator with no owned network infrastructure; outside ICP scope. |
| Jaintel | jaintel.com | No ICP fit | Small London wholesale VoIP provider with no owned network infrastructure; outside ICP scope. |
| AJ Telekom | ajtelekom.com | No ICP fit | Singapore wholesale VoIP provider with no owned network infrastructure; outside ICP scope. |
| Stella Communications | stellatel.com | No ICP fit | International voice-services aggregator; voice-only model outside MaiaEdge ICP scope. |
| Latinatel | latinatel.net | No ICP fit | LATAM wholesale voice carrier (termination/origination); voice-only, outside ICP scope. |
| Purple Stone Telecom | tollfreechina.com | No ICP fit | China/HK wholesale voice-and-data broker; not a fiber, colo, or cloud infrastructure operator. |
| KS Link Telecommunication | kslinktel.com | No ICP fit | Global wholesale voice/bandwidth broker; not an owned-infrastructure ICP. |
| Blue Dragon Network | bluedragonnetworktelecom.com | No ICP fit | Early-stage wholesale VoIP reseller with no owned infrastructure; outside ICP scope. |
| Manor | manor.net | No ICP fit | Thin record with no infrastructure profile or operational evidence for any ICP sub-segment. |
| IP Transfer | iptransferllc.net | No ICP fit | Small PA VoIP/SIP entity with no infrastructure profile or ICP evidence. |
| Telegeeks | tele-geeks.net | No ICP fit | Small FL IT/telecom services entity with no infrastructure profile or ICP evidence. |
| Anguilla Telecom | angliaphone.ai | Hard junk / non-business | No real Anguilla carrier at this domain; hallucinated record (real operators are Digicel and Flow). |
| Karib Telecom | karibtel.vg | Hard junk / non-business | No real BVI carrier at this domain; hallucinated record (real operators are CCT, Digicel, Flow). |
| Hafa Adai Communications | hafaadai.gu | Hard junk / non-business | Prepaid SIM/eSIM product brand of IT&E, not an independent carrier; hallucinated standalone record. |
| TeleSapiens Argentina | telesapiens.com.ar | Hard junk / non-business | EdTech/education platform misclassified as a carrier; hallucinated templating-bleed record with no ENACOM carrier license. |
| Montserrat Telecom | montserrat-telecom.ms | Hard junk / non-business | No real Montserrat carrier at this domain; hallucinated record (real operators are Flow and Digicel). |
| Paircom | paircom.com.ng | Hard junk / non-business | No real Nigerian operator at this domain; hallucinated record. |
| Japi Internet Costa Rica | japi.cr | Defunct / out of business | Wireless ISP (Japi Internet) service suspended in 2019; domain inactive as a live carrier. |
| Dragonfly Internet | dragonfly.net | No ICP fit | Residential fixed-wireless retail ISP; despite acquiring Myakka the parent has no wholesale or B2B fiber operations qualifying for any MaiaEdge ICP. |
| B&D Communications |  | No ICP fit | Name resolves to a small phone-services firm or a tiny PA fixed-wireless ISP, neither matching any MaiaEdge ICP; ambiguous record evicted. |
| Würth Industry North America | wurthindustry.com | No ICP fit | $22.7B industrial wholesale distributor; not in any of the four Enterprise Multi-DC ICP sub-segments. |
| Currency.com | currency.com | No ICP fit | Gibraltar-licensed crypto-asset trading platform; not a NeoCloud GPU operator or crypto-to-AI infra and fails ICP category. |