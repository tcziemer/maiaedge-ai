CRM Guardian - Flagged Consolidation - 2026-06-09 - 5 contacts flagged, 4 reassociated, 85 Tier 3 held

Run summary: 267 flagged companies in queue · 379 contacts evaluated (primary-associated to a flagged company) · Tier 1 flags: 5 new (286 already flagged, no-op) · Tier 1-2 reassociations: 4 contacts -> 3 ICP primaries · Tier 3 holds: 85 (84 preserved contacts with no ICP primary + 1 open-deal company) · 108 flagged companies carry zero contacts (archive-ready, no action)

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete. 291 contacts now carry the flag (286 pre-existing + 5 new this run).
> Then: Filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs the stale associations from the 4 contacts reassociated this run).

- 1 Tier 3 investigation: "Bits in Flight, Ltd" (326674182894) is Flagged-for-deletion but has an OPEN deal "H5 Data Centers - Partner Reg" (created 2026-06-08). Open-deal hard stop + fresh-record (<14d). Recommend: resolve/route the deal or re-evaluate the flag. No contacts on the record.
- 84 Tier 3 preserved-contact holds: preserved contacts (mostly fresh <14-day imports) on flagged companies with no ICP primary to reassociate to. Held, not flagged - they re-evaluate next run as they age or R1/R2 enrich the parent.

Run health: YELLOW
- Writes succeeded (9/9: 5 Mode B flags + 4 Mode A reassociations w/ owner sync). Tier 3 holds present (expected steady-state).

Errors: None. No HubSpot 4xx/5xx. No optouts encountered (0 CAN-SPAM protection cases). Only 1 flagged company carried any deal (handled as hard-stop Tier 3).

Customer-protection / open-deal hard stops: 1 company (Bits in Flight) - open deal, skipped + held. 0 closed-won customer-history mis-flags. C-bis Enterprise defensive check: 0 mis-flags (the 5 Mode B flags are non-Enterprise-vertical; Enterprise-adjacent names e.g. Würth, Allegion, Latham & Watkins, McGough are all in the preserved-hold set, not flagged).

last_enriched_date: NOT bumped (R4 contact-only writes never bump per stamping policy).

====================================================================
MODE B - CONTACTS FLAGGED FOR DELETION (5 new, Tier 1)
====================================================================
| Contact ID | Name/Company | Domain | Reason |
|---|---|---|---|
| 486369299172 | Currency.com | currency.com | No preservation signal (no activity 90d, lead, no deal, created 2025-10-06) |
| 464826875584 | Layer3 | layer3.xyz | No preservation signal (created 2026-04-01) |
| 486616302309 | Melita Ltd | melitaltd.com | No preservation signal (created 2026-05-15) |
| 471678757572 | Open Systems, Inc | opensystems.net | No preservation signal (created 2026-04-15) |
| 486236285666 | Pivotal Mobile eDiscovery | pme-discovery.com | No preservation signal (created 2026-05-14) |

====================================================================
MODE A - REASSOCIATIONS TO ICP PRIMARY (4 contacts, Tier 1-2)
====================================================================
| Contact ID | Flagged source co | Domain | -> ICP primary (id) | Primary segment | Owner synced |
|---|---|---|---|---|---|
| 497855802091 | Primenet Global (326167086796) | primenet.in | Primenet Global (326186737353) | Fiber Operator | 159350430 (Tim Ziemer) |
| 497857257184 | Primenet Global (326167086796) | primenet.in | Primenet Global (326186737353) | Fiber Operator | 159350430 (Tim Ziemer) |
| 492127751896 | ETC Communications - Ellijay Telephone Company (322405956290) | etcnow.com | ETC Communications (322836352712) | Fiber Operator | 161889085 (Tim Lieto) |
| 465763409613 | Vocus Wholesale (319182113497) | vocus.com.au | Vocus (251600877280) | Network Operator(Tier 1 / VNO) | 159350430 (Tim Ziemer) |

HIGH-confidence exact-domain duplicate matches. Added contact->primary association + synced hubspot_owner_id to mirror the ICP primary. Old association to the flagged record persists until Cooper archives the flagged company (clears stale association). customer_segment not written at contact level (company-scoped property; owner is the territory-routing field).

====================================================================
TIER 3 HELD - PRESERVED CONTACTS, NO ICP PRIMARY (84)
====================================================================
| Contact ID | Company | Domain | Preservation signal |
|---|---|---|---|
| 492040575716 | 3 Rivers Communications | 3rivers.coop | fresh<=14d |
| 497530035911 | Alestra | alestra.se | fresh<=14d |
| 486168348355 | Allegion | allegion.com | activity<=90d |
| 484535495355 | (no name) | aristotleweb.com | activity<=90d |
| 492150859494 | BAI Connect | belairinternet.com | fresh<=14d |
| 484521260785 | BitStream | bitstream.org | activity<=90d |
| 492050676464 | Bright House Networks | brighthouse.com | fresh<=14d |
| 494765969108 | CarrierX | carrierx.com | contacted<=90d, activity<=90d, fresh<=14d |
| 484483303160 | Commercial Electronics | commercialelectronics.com | activity<=90d |
| 492052425437 | Congruex | congruex.com | fresh<=14d |
| 314701034216 | Corero | corero.com | activity<=90d |
| 441460370106 | Core Technologies | coretechinc.com | activity<=90d |
| 484486877931 | Dragonfly Internet | dragonfly.net | activity<=90d |
| 484536816318 | Dragonfly Internet | dragonfly.net | contacted<=90d, activity<=90d |
| 492028345051 | KNET Co.,LTD. | e-knet.com | fresh<=14d |
| 440783060708 | EdgeCloudLink | ecldc.com | activity<=90d |
| 485896627901 | EdgeCloudLink | ecldc.com | activity<=90d |
| 451559667429 | Edged Data Centers | edged.ai | activity<=90d |
| 484480023266 | Ellijay | ellijay.com | activity<=90d |
| 489067118326 | Fast Wave | fastwavenetworks.com | contacted<=90d, activity<=90d, lifecycle, has_deal |
| 499362794172 | FCR Investments | fcrinvestments.com | contacted<=90d, activity<=90d, fresh<=14d |
| 297261432562 | FlowSec | flow-sec.com | contacted<=90d, activity<=90d |
| 494763256551 | FreeConferenceCall | freeconferencecall.com | contacted<=90d, activity<=90d, fresh<=14d |
| 492052216551 | Grande Communications Networks LLC | grandecom.com | fresh<=14d |
| 441467629289 | GVTC Communications | gvtc.net | activity<=90d |
| 441504356087 | GVTC Communications | gvtc.net | activity<=90d |
| 486370012871 | Eric Hanselman | hanselman.net | contacted<=90d, activity<=90d |
| 484511204032 | Holston Electric Cooperative | holstonelectric.com | activity<=90d |
| 492003233527 | Home Telecom | homesc.com | fresh<=14d |
| 441572858578 | Hotwire Communications | hotwirecommunication.com | activity<=90d |
| 426027688647 | Hotwire Communications | hotwiremail.com | activity<=90d |
| 441485956825 | Hotwire Communications | hotwiremail.com | activity<=90d |
| 497781152488 | Hotwire Communications | hotwiremail.com | fresh<=14d |
| 497583164115 | IFX Networks | ifxcorp.com | fresh<=14d |
| 497807353536 | IFX Networks | ifxcorp.com | fresh<=14d |
| 497810945766 | IFX Networks | ifxcorp.com | fresh<=14d |
| 497855233776 | IFX Networks | ifxcorp.com | fresh<=14d |
| 497731305209 | Commercial Furniture Australia | innova-group.com.au | fresh<=14d |
| 499014500032 | Intellinet | intellinet.com | fresh<=14d |
| 491978331868 | Internet Subway | internetsubway.com | fresh<=14d |
| 491978331869 | Internet Subway | internetsubway.com | fresh<=14d |
| 492123207362 | Internet Subway | internetsubway.com | fresh<=14d |
| 492127751892 | Internet Subway | internetsubway.com | fresh<=14d |
| 492147415788 | Internet Subway | internetsubway.com | fresh<=14d |
| 465761569489 | IP Transfer | iptransferllc.net | activity<=90d |
| 486369299174 | I & S Group | is-grp.com | contacted<=90d, activity<=90d |
| 497856923378 | Komodor | komodor.com | fresh<=14d |
| 496624074435 | Latham & Watkins | lw.com | contacted<=90d, activity<=90d, fresh<=14d |
| 496624074436 | Latham & Watkins | lw.com | contacted<=90d, activity<=90d, fresh<=14d |
| 465834282718 | Manor | manor.net | activity<=90d |
| 497838126779 | Maximum RE Solutions | maximumresolutions.com | fresh<=14d |
| 496618298094 | McGough | mcgough.com | contacted<=90d, activity<=90d, fresh<=14d |
| 496618298095 | McGough | mcgough.com | contacted<=90d, activity<=90d, fresh<=14d |
| 494730568436 | Mjm Innovations | mjminnovations.com | fresh<=14d |
| 492052425442 | MOBILY LLC | mobilyllc.com | fresh<=14d |
| 497845417680 | Matrix Networks | mtrx.com | fresh<=14d |
| 492137592559 | Maquoketa Valley Electric Cooperative | mvec.com | fresh<=14d |
| 492003233486 | Astound Broadband | mygrande.com | fresh<=14d |
| 474847701712 | MyRepublic Indonesia | myrepublic.net.id | activity<=90d |
| 499032931062 | NexGen Cloud | nexgencloud.co.uk | fresh<=14d |
| 497857181430 | New Horizon Enterprises | nhe-usa.com | fresh<=14d |
| 497838126788 | (no name) | onecom.sk | fresh<=14d |
| 491982424809 | Phoenix Communications, Inc. | phoenix-fiber.com | fresh<=14d |
| 492003240642 | Phoenix Communications, Inc. | phoenix-fiber.com | fresh<=14d |
| 492127413972 | Plumas Sierra Rural Electric Cooperative | psrec.coop | fresh<=14d |
| 499007522534 | Riversand | riversand.com | fresh<=14d |
| 499028004594 | SEOX | seox.ch | fresh<=14d |
| 497530035900 | SIRT | sirt.es | fresh<=14d |
| 497731305167 | (no name) | spacedigital.co.uk | fresh<=14d |
| 476512699073 | Steadfast Networks | steadfast.net | activity<=90d |
| 261906818770 | Sumauma | sumaumatelecom.com.br | contacted<=90d, activity<=90d |
| 261906818771 | Sumauma | sumaumatelecom.com.br | contacted<=90d, activity<=90d |
| 484517998305 | SwyftConnect | swyftconnect.com | activity<=90d |
| 497763205854 | Telecentro | telecentro.net.ar | fresh<=14d |
| 497843516107 | Telecentro | telecentro.net.ar | fresh<=14d |
| 497856275172 | Telecentro | telecentro.net.ar | fresh<=14d |
| 497857181419 | Telecentro | telecentro.net.ar | fresh<=14d |
| 487432186604 | Truepacket | truepacket.io | contacted<=90d, activity<=90d |
| 492150859488 | Vistabeam | vistabeam.net | fresh<=14d |
| 492041284284 | Astound | wavebroadband.com | fresh<=14d |
| 497838128843 | Wavenet | wavenetuk.com | fresh<=14d |
| 497855134455 | Wavenet | wavenetuk.com | fresh<=14d |
| 486162222835 | Würth Industry North America | wurthindustry.com | activity<=90d |
| 499028006618 | (no name) | ytlhotels.co.uk | fresh<=14d |

====================================================================
TIER 3 HELD - OPEN-DEAL / FRESH-RECORD COMPANY (1)
====================================================================
| Company ID | Company | Domain | Reason |
|---|---|---|---|
| 326674182894 | Bits in Flight, Ltd | bitsinflight.com | Open deal "H5 Data Centers - Partner Reg" (open) + createdate 2026-06-08 (<14d). Open-deal hard stop. 0 contacts. |
