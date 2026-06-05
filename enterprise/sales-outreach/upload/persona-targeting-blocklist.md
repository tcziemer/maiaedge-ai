# Persona Targeting Blocklist

**Status:** Mandatory pre-cadence gate for every Smartlead / cold-email batch and every batch LinkedIn cadence.
**Source:** Deep Messaging Audit (2026-05-11) §6. Confirmed in Cross-Audit Decisions Sidecar §2 (Decision 11) and §7.
**Owner:** Cooper (RevOps) - gate is enforced at the SDR pipeline stage before list export to Smartlead or LinkedIn cadence.

---

## Why this exists

The 60-day Smartlead replied-thread audit isolated the single biggest non-content driver of the depressed reply rate: **the wrong titles were being emailed for the buyer's decision authority in two segments**. Out of 34 replies in the file, **5 were wrong-persona redirects** ("not my purview" / forward-to-engineer / hostile unsubscribe driven by stale role data). Fixing the title-targeting model should convert those misfires to real conversations and lift reply rate by an estimated 0.5-1.0 points before any copy work compounds.

The blocklist below is the title-filter that should be applied at the SDR pipeline stage. The signals-catalog enrichment already pulls titles. Adding a "valid-buyer-title" check before the campaign drops into Smartlead is a one-time engineering pass.

---

## Universal rules (every segment)

| Title to STOP emailing | Why | Title to email instead |
|---|---|---|
| **Account Executive / Account Manager** | Customer-facing rep. No buying authority. | VP Sales (for sales-velocity angle), VP Engineering (for technical) |
| **Customer Success Manager** | Post-sale, not a buyer. | VP Operations, VP Customer Success (different role: operational lead, not the individual contributor) |

---

## Aggregators / NaaS Platform Operators / TSDs

| Title to STOP emailing | Why | Title to email instead |
|---|---|---|
| **Director - Carrier Wholesale** | Supply-side procurement role. Buys CIRCUITS from carriers, not software to manage carrier-supply. Reads our pitch as "you want to sell me networks." | COO, VP Network Operations, VP Service Delivery, VP Wholesale Platform (if NaaS), CTO |
| **Wholesale Manager / Manager - Wholesale** | Same as above, junior tier. | Same list as above. |
| **Director - Sales (Wholesale)** | Sells wholesale TO their customers. Doesn't buy software for the back-end. | VP Engineering, VP Operations, VP Service Delivery |

**Anchor evidence:** Mark Palma @ iTel replied "not my purview" to a wholesale-blind-spot framing. Anna Gizhlaryan @ Voxbridge read the inbound carrier-pain framing as a customer complaint because supply-side wholesale managers field complaints all day. Confirmed pattern across 3 of 5 wrong-persona redirects in the corpus.

---

## Fiber Operators / ISPs

| Title to STOP emailing | Why | Title to email instead |
|---|---|---|
| **Director - Field Operations** | Construction / line-tech management. Not a software buyer. Reads "acquisition integration" framing as a complaint about their crew. | VP Network Engineering, VP Operations, CTO, COO, CFO (for monetization framing), VP Sales (for win-rate framing) |
| **GM - [Region] / Regional Operations Manager** | Below-the-line ops, not strategic. | Same as above. |

**Anchor evidence:** Mark Thornton @ Truvista (Director Field Operations) hostile-unsubscribed an acquisition-integration E1. The framing is COO/VP-Network-Engineering language and was misrouted to a construction-management title.

---

## International Carriers / Network Operators

| Title to STOP emailing | Why | Title to email instead |
|---|---|---|
| **Country Manager / GM - [Country]** at carriers with HQ product organizations | At carriers like etisalat group, Helios Towers, Tata, PCCW, the country manager doesn't have product-decision authority. They will route to HQ team and the lead goes cold. | HQ product/strategy titles: VP Network Strategy, VP Product, Chief Network Officer, VP Wholesale (at HQ). For carrier holding groups, target the HOLDING company, not the country op. |
| **Finance Director / Treasurer** | Cost-control role, not buying authority for new infrastructure. | CFO (different role: capex-allocation authority), VP Strategy, CRO |

**Anchor evidence:** Tim Z's E1 to Prabhu @ etisalateurope routed up to the HQ product organization and went cold - country-manager titles at multi-country carrier groups consistently lose to HQ-side product owners.

---

## What this blocklist does NOT cover

- **Wholesale-Director partner-cadence (Decision 11, deferred):** If the Konnexx-style "Infrastructure + Automation pilot" pattern proves repeatable, a separate partner-recruitment cadence may target Wholesale Directors with a co-sell / channel-partner motion. That is NOT the standard SDR cadence and is out of scope for this blocklist. Revisit if a real Konnexx-pattern engagement progresses.
- **Founder-direct exceptions:** Abilash, Tim Z, or another founder may reach out to a blocked title personally for strategic or relationship-building reasons. The blocklist is for batch SDR cadences, not 1:1 founder outreach.
- **Live conversations and warm contacts:** Anyone on the blocklist who has already replied, attended a meeting, or has any HubSpot engagement activity is a warm contact and is handled per the warm-contact rules in the cold-email and linkedin-outreach skills.

---

## Implementation - where this gate runs

1. **Apollo / ZoomInfo enrichment** pulls `current_title` for every contact in a list.
2. **SDR pipeline preflight** (skills/sdr-pipeline/SKILL.md) checks each title against the blocklist above.
3. **Blocked contacts** are surfaced in a separate Cooper-review queue, not silently dropped - the LinkedIn-status check in `context/outreach/pre-cadence-hygiene.md` may also catch stale-title cases that look like a blocked title only because of stale data.
4. **Blocked contacts cleared by Cooper** can re-enter the cadence via a manual override flag.
5. **The blocklist is enforced before Smartlead campaign export and before LinkedIn batch DM cadence runs.** Both channels share the same persona model.

---

## Decision history

- **2026-05-11:** Blocklist created from Deep Messaging Audit §6 + Replied-Lead Thread Audit synthesis. Cross-Audit Decisions Sidecar §2 Decision 11 deferred the Wholesale-Director carve-out (no action - default to drop from standard SDR cadence; build a separate partner cadence later if the Konnexx pattern repeats).
