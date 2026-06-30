# Enterprise Segment

**MaiaEdge for Enterprise IT and Network Teams**

The enterprise segment is the direct-to-customer use case. The enterprise IS the operator of their own private network. Unlike the carrier and colo segments, there is no commercial layer to sell back to a downstream customer. The enterprise consumes MaiaEdge to gain control, visibility, and determinism over the network they already operate.

Enterprise is an **ICP segment as of May 2026** (HubSpot `customer_segment = "Enterprise-CustomerSegment"`, priority 5 - lowest of the ICPs but qualified and sellable). Four sub-segments only; everything else is Watch List or out of scope. See HubSpot Mapping below.

> **Classification authority:** Sub-segment classification rules, anchors, and confidence thresholds live in `context/account-tiering/sub-segment-qualification.md` (pointer) and file 06 (`context/account-tiering/sub-segment-qualification-full.md`). Tier computation lives in `context/account-tiering/tier-compute-spec.md`. This cheatsheet covers selling angles, personas, pain points, and discovery.

> **Lead use cases:** Dark fiber redundancy between data centers and cloud on-ramps under the enterprise's own control. Other use cases (multi-cloud bridging, regulated workload paths, M&A network integration, AI/GPU access via direct private path) are downstream of those two.

> **Cold-email anchor:** Dark-fiber-redundancy is the **default E1 anchor** for Healthcare Systems and Retail/Distribution sub-segments. **M&A network integration is the default E1 anchor for Financial Services + Outsourcing Services sub-segments.** Full E1/E2/E3 templates and persona-by-persona pitch guidance live in `context/outreach/fallback-messaging.md` § Enterprise (Multi-DC ICP). Pilot batch: 50-80 contacts in FS + OS using the M&A anchor.

> **Archetype:** Meijer-class. Multi-DC retailer or distributor. Ken Cunningham + Woody Acosta are working an active design with Mark Szymanski (Apr 2026) on PBC + Port Extender deployment for HAsync / HAfabric dark fiber diversity to SSR1300 nodes between data centers.

---

## HubSpot Mapping

| HubSpot Field | Value | Notes |
|---|---|---|
| `customer_segment` | `Enterprise-CustomerSegment` | Display label "Enterprise". ICP promoted 2026-05-11. |
| `company_sub_segment` | One of the four ICP sub-segments below | Assignment rules in §"Vertical Sub-Segments". |
| `account_tier` | See `context/account-tiering/tier-compute-spec.md` | See `context/account-tiering/tier-compute-spec.md` for tier computation. All 4 Enterprise sub-segments default to Tier 3, ceiling Tier 2, floor Tier 4 - no Tier 1 path for Enterprise. |

**The four Enterprise sub-segments (and only these four):**

| Sub-segment internal value | What it captures |
|---|---|
| `Financial Services - Enterprise` | Banks, investment firms, insurers, payment networks, capital-markets infra. Commercial-procurement defense contractors land here too. |
| `Healthcare Systems - Enterprise` | Multi-hospital IDNs and large health systems. |
| `Retail and Distribution - Enterprise` | National retailers with multi-DC corporate IT + distribution-center networks. |
| `Outsourcing Services - Enterprise` | BPO / outsourced operations providers running multi-site delivery centers (operational, not project-based consulting). |

**Hard sourcing qualification gate (BOTH must pass):**
- **Vertical gate:** one of the four sub-segments above.
- **Scale gate:** $1B+ revenue AND (3+ DCs OR direct Equinix Fabric / Megaport port OR confirmed in-house network engineering team via NOC presence or VP Network / Principal Network Engineer / Director Network Engineering job postings).

**Hard disqualifiers (any one disqualifies):**
- Network fully outsourced to a single MSP with no internal engineering ownership.
- Single data center or single geography.
- No direct carrier contracts (everything through reseller or MSP).

Records that fail either gate stay as `customer_segment = "Other"` or `"Unknown"`. Mid-market ($200M-$1B) without strong signals is not Enterprise ICP - hold.

**Confidence thresholds (per file 06 §6.6 + B-and-C-enterprise.md):**

The five gates: vertical / $1B+ revenue / 3+ DCs OR direct Equinix-Megaport port / in-house network engineering / direct carrier contracts.

| `segmentation_confidence` | Rule |
|---|---|
| `high_90` | Anchor account match AND 4 of 5 gates pass |
| `medium_7089` | 4 of 5 gates pass (no anchor match required) |
| `low_5069` | 3 of 5 gates pass |
| Flagged for deletion | Fewer than 3 gates AND no other ICP path |

**Hard exclusions - project consulting (NOT operational delivery):**

Deloitte, McKinsey, BCG, Bain, and Accenture Strategy & Consulting route to `customer_segment = "Other"`. These are project / advisory firms, not multi-site operational delivery. Their network does not match the Enterprise use case.

**Edge cases (flag `manual_review_required`; route to D7 weekly review):**

| Account | Why contested |
|---|---|
| CVS Health | Retail-pharmacy + insurance hybrid - dominant revenue line decides |
| UnitedHealth | Optum split - parent (insurer) = Financial Services; Optum as separate record |
| McKesson, Cardinal Health, AmerisourceBergen | Pharma distribution - classify Healthcare Systems |
| Kyndryl, NTT Data Services, DXC | MSP/Aggregator vs Outsourcing Services contested |
| Firstsource | ~$750M revenue - borderline scale gate |

**Dominant-revenue-line tiebreaker for diversified players:**

- **CVS Health** (retail-pharmacy + insurance hybrid): retail-pharmacy revenue dominant -> Retail and Distribution; insurance / PBM revenue dominant -> Financial Services.
- **UnitedHealth Group**: parent (insurer) -> Financial Services; Optum split as a separate record.
- **McKesson / Cardinal Health / AmerisourceBergen** (pharma distribution): Healthcare Systems.
- **Cognizant-style dual-arm firms** (BPO + consulting under one parent): classify on the operational revenue mix. If the operational delivery arm (BPO) is a real revenue line with multi-site delivery centers, qualify Outsourcing Services. If consulting / project revenue dominates, hold as `Other`.

---

## Know Your Customer

| Attribute | Details |
|---|---|
| **Profile** | $1B+ revenue. Three or more data centers, plus distribution centers, hospitals, branches, or regional hubs. In-house network engineering team of 10-100+ engineers (verifiable via NOC presence or job postings for VP/Director/Principal Network Engineering). |
| **What They Own** | Corporate WAN. Data center routers and switches. Often lease dark fiber between key sites. SD-WAN overlay (Cisco, Juniper SSR / 128T, Versa, Cato, Fortinet, Palo Alto). Cloud connectivity through Megaport, Equinix Fabric, or carrier-managed services. Direct carrier contracts (not via reseller or MSP). |
| **Posture** | Mature on branch SD-WAN. Less mature on inter-DC determinism. Cloud on-ramps usually outsourced to third-party fabric providers. Type 2 fiber is a black hole. |
| **Scale** | $1B-$200B+ revenue. 3-10+ data center or critical sites. Multi-cloud (AWS + Azure + at least one of GCP / OCI / private). |
| **Why They Buy MaiaEdge** | Own the private fabric across all sites. Deterministic dark fiber redundancy without standing up routing protocols. Cloud on-ramps under their brand and their control. Hop-by-hop visibility everywhere. Audit-ready policy enforcement for HIPAA / PCI-DSS / SOX / GDPR. |

---

## Messaging Hierarchy

1. **Dark fiber redundancy that is actually redundant** (lead). Dark fiber between data centers is rarely truly redundant. PBCs at each end with diverse fibers and automated failover make it so without routing protocols.
2. **Cloud on-ramp under your control** (default). AWS, Azure, GCP, OCI direct connect provisioned through the same fabric, same portal, same visibility as everything else on the network. Megaport / Equinix Fabric become transport options the fabric uses by API rather than vendors the enterprise depends on.
3. **Hop-by-hop visibility on every path including Type 2** (operational angle). When the SLA breaks, the enterprise can prove where it broke.
4. **New site bring-up in days not months** (growth angle). New DR site, new DC, new cloud region: PBC ships, attaches to fabric, paths are live the same day.
5. **Policy-based path control with audit trails** (regulated angle). For financial, healthcare, government, and AI sovereignty workloads.

---

## Vertical Sub-Segments (ICP - the only four)

Assigned via HubSpot `company_sub_segment`. The four ICP sub-segment values exist in HubSpot as of May 2026; reference `context/hubspot/property-schema.md` §2.5 for exact internal values.

### Retail and Distribution - Enterprise (Meijer archetype - anchor account)
**Sub-segment value:** `Retail and Distribution - Enterprise`
**Who:** Multi-DC national retailers and large distribution networks with multi-DC corporate IT plus distribution-center networks. Hundreds to thousands of stores, 100k+ SKUs, 3-10 DCs. **Multi-warehouse alone does not qualify** - the qualifier is multi-DC **corporate IT**, not the number of warehouses.
**Anchors (verified per Phase B):** Meijer (anchor), Walmart, Kroger, Target, Costco, Home Depot, Lowe's, Albertsons, Publix; UK: Tesco, Sainsbury's; APAC: Aeon (Japan); Wholesale edge: Sysco, US Foods.
**Lead angle:** Dark fiber redundancy between primary DCs first. Cloud on-ramp for SaaS and analytics second. Then deterministic paths into the highest-traffic distribution centers.
**Current why-nows (2026):**
- **SOVEREIGN** - PCI v4.0.1 Req 11.4.7 now requires the segmentation between the cardholder data environment and everything else to be **penetration-tested**, not just asserted. The retailer has to prove the segmentation holds, on the wire, on a schedule. A path-control plane that produces the evidence is the difference between an assertion and an attestation.
- **AUTOMATED** - the robotics-DC bring-up wave is a connectivity wave first. Symbotic Gen-2 systems rolling across 42 Walmart DCs (early 2026) and Costco's Port St. Lucie automated facility (March 2026) each light up as a carrier turn-up before the first bot moves. The carrier install is the long pole, not the racks.
**GenAI cross-cloud egress angle (AUTOMATED + cost control - Retail-led, applies to FS + BPO too):** Production shopping agents (Walmart Sparky, Kroger's Gemini rollout nationwide Jan 2026) ground every inference in real-time inventory and customer data that lives in corporate DCs while the inference itself runs cloud-side. Cross-cloud and cross-region egress (~$0.087/GB) now scales with adoption the way nobody modeled in the pilot. The path the inference takes is a CFO-visible cost decision, not just a latency one - and a private path the retailer owns end-to-end is the answer to both.
**Persona priority:** Network Architect / Principal Network Engineer → VP Network Infrastructure → CIO.

### Financial Services - Enterprise
**Sub-segment value:** `Financial Services - Enterprise`
**Who:** Banks, investment firms, insurers, payment networks, capital-markets infrastructure, exchanges. Low-latency inter-DC requirements, multi-cloud determinism, regulator-friendly path control.
**Anchors (15+ verified per Phase B):** JPMorgan, Goldman Sachs, BNY Mellon, State Street, Visa, Mastercard, Bank of America, Wells Fargo, Citi, BlackRock, Schwab; UK/EU: HSBC, Barclays, BNP Paribas; APAC: Mizuho, Nomura; Defense (commercial procurement): Lockheed Martin, RTX, Northrop Grumman, BAE Systems, L3Harris.
**Lead angle:** Deterministic inter-DC paths, audit-ready policy enforcement (SOX, PCI-DSS, GDPR), cloud on-ramps under their control instead of through a third-party fabric provider.
**Current why-nows (2026):**
- **REDUNDANT** - the carrier-consolidation wave is quietly invalidating diverse-path attestations written in the 2020-2022 cycle. As formerly-independent fiber collapses under fewer owners, a wave that was diverse from the incumbent can now share regional aggregation with the carriers a bank would pick as Path B. The "diverse carrier" line in last cycle's examiner letter is a reasoned thing to re-test against today's ownership map, not something to assume still holds.
- **SOVEREIGN** - DORA's first oversight cycle put connectivity and data-center providers (Colt, Deutsche Telekom, Orange, Equinix, InterXion) on the critical-third-party (CTPP) list, not just the hyperscalers. The concentration question now reaches the fabric the on-ramps ride on, and best-effort routing still cannot show the examiner the path the data took.
**Persona priority:** Principal Network Architect → VP Network Infrastructure → CSO/CISO.

### Healthcare Systems - Enterprise
**Sub-segment value:** `Healthcare Systems - Enterprise`
**Who:** Multi-hospital IDNs (Integrated Delivery Networks) and large health systems with EHR data centers, imaging archives, and regional clinic networks. Strict uptime SLAs, HIPAA-aligned redundancy, PHI sovereignty obligations. **Single-hospital regional systems below the scale gate do NOT qualify.**
**Anchors:** HCA Healthcare, Ascension, CommonSpirit, Kaiser Permanente, Cleveland Clinic, NewYork-Presbyterian, Trinity Health, Adventist Health, Banner Health, Providence; EMEA: NHS England (government special case), Karolinska Institutet; APAC: Bumrungrad International.
**Lead angle:** Diverse dark fiber redundancy between EHR DCs. Cloud on-ramps for radiology / analytics under enterprise control. Policy-based path control for HIPAA flows + audit trails for HITRUST.
**Current why-nows (2026):**
- **SOVEREIGN** - OCR ransomware consent orders are enforcing network segmentation, asset inventory, and ePHI data-flow mapping through corrective action plans right now, rule or no rule. The IDN is being asked to prove the segmentation, not assert it.
- **REDUNDANT / AUTOMATED** - AI imaging is crushing inter-DC bandwidth. AI-reconstructed studies and 200GB+ tomosynthesis volumes moving between the imaging archive and the read sites are sized for a path nobody re-provisioned. The carrier circuit the IDN inherited was never built for the new study weight, and the bring-up of each new read site or acquired hospital (UPMC's Epic cutover wave, for one) is a connectivity turn-up before the first image moves.
**Persona priority:** VP Network Infrastructure → CSO/CISO → CIO.

### Outsourcing Services - Enterprise (new for May 2026 ICP promotion)
**Sub-segment value:** `Outsourcing Services - Enterprise`
**Who:** BPO and outsourced operations providers running multi-site delivery centers on an **ongoing operational basis** for client back-office and customer-facing functions. Multi-country / multi-state delivery footprints; regulated client data (financial, healthcare, telco BPO); latency-sensitive workflows (real-time fraud, claims, patient-data access).
**Anchors:** Cognizant, Genpact, Concentrix (post-Webhelp), TaskUs, Conduent; EMEA-HQ: Capgemini; India-HQ: Wipro BPS, TCS BPS, Infosys BPM, HCL Tech; PH-anchored: Teleperformance Manila, Cognizant Manila; LATAM: Atento; Specialty: Firstsource (borderline scale gate), Sutherland Global Services.
**Hard exclusions inside this sub-segment:** project-based consulting / advisory (Deloitte, McKinsey, BCG, Bain, Accenture Strategy & Consulting) are NOT Outsourcing Services Enterprise - they're project firms, not operations, and route to `customer_segment = "Other"`. For dual-arm firms (Cognizant has both BPO and consulting), classify on the **operational delivery revenue mix** - if the BPO arm is a real revenue line with multi-site delivery centers, qualify; if consulting dominates, hold as `Other`.
**Lead angle (rebased off per-seat - the seat-volume premise is eroding):** the old "every new client adds a seat ramp" framing is weakening as AI decouples BPO revenue from headcount (Genpact's CEO says the business is moving off the per-seat model; Teleperformance is among Europe's most-shorted names on exactly this fear). Lead instead on the frame that survives that shift:
- **SOVEREIGN (primary)** - per-client jurisdictional path proof. The RBI 2025 directions, with their April 2026 deadline, now require proof that an Indian client's data is never reachable by a foreign regulator; DPDP and DORA flow-down stack the same obligation from other directions. Every new client still adds a tail - but the tail is a regulatory attestation, not a seat count.
- **REDUNDANT** - uptime is margin when you bill per resolution instead of per seat. The path that fails the jurisdictional audit is the same one eating the margin every minute it wobbles.
- **AUTOMATED** - fast nearshore site activation. New delivery centers (CGS Colombia, VXI Egypt class) light up as a connectivity turn-up; the carrier install is the gate on the client commit date.
**Persona priority:** VP Network Infrastructure → CSO/CISO → CIO.

---

## Watch List / Future Expansion (NOT currently ICP)

These verticals have surface-level multi-site characteristics but **do not meet the multi-DC + in-house net eng definition** that makes MaiaEdge sellable today. Keep them in mind for future TAM expansion; do NOT assign Enterprise sub-segments to these accounts. Reclassify to `Other` if encountered.

### Manufacturing - multi-plant != multi-DC
**Why not ICP:** Plant networks are OT (operational technology), not IT data-center networks. The MaiaEdge use case doesn't naturally apply. Some large diversified industrials with separate corporate IT may surface as Financial Services or Retail-style profiles on examination - classify on the **corporate IT** footprint, not the plant footprint.

### Energy and Utilities - NERC CIP procurement is long-tail
**Why not ICP:** SCADA fit is real, but NERC CIP procurement cycles are brutal (18-36 months, heavy compliance burden). Out of scope for the current sales motion. Revisit when the company is large enough to staff a dedicated NERC CIP procurement team and we have FedRAMP-adjacent compliance maturity.

### Logistics and Supply Chain - multi-warehouse != multi-DC
**Why not ICP:** 3PLs, freight, and large warehouse operators (XPO, GXO, J.B. Hunt) don't run multi-DC IT in the way that qualifies. Deal sizes smaller; the inter-DC determinism story doesn't land. If a logistics company's corporate IT footprint looks like a multi-DC retailer (rare), refer to `Retail and Distribution - Enterprise` and qualify on that.

### Restaurant chains - multi-store != multi-DC corporate IT
**Why not ICP:** McDonald's, Yum Brands, Chick-fil-A, and similar national/global restaurant chains have thousands of stores but the corporate-IT footprint that would drive MaiaEdge purchase is single-DC-class. Multi-store presence is not multi-DC. Hold as `Other` unless the corporate IT side independently matches Retail and Distribution - Enterprise criteria.

---

## Government and Defense - Future Expansion Only

Real federal sales is gated by **FedRAMP compliance** for the PCE. There is no `Government - Enterprise` sub-segment. Defense contractors that procure commercially (Lockheed Martin, RTX, Northrop Grumman, BAE Systems, L3Harris) land in `Financial Services - Enterprise` based on their **commercial** procurement profile - their classified / government work is irrelevant for ICP classification. State / local agencies, federal civilian, and DoD direct sales are out of scope until FedRAMP is achieved.

---

## Structural exclusions

- **Under $1B revenue.** Fails scale gate. Mid-market $200M-$1B can be held as `Other` and revisited when revenue / DC count grows.
- **Single-DC or single-geography enterprises.** No inter-DC determinism story. Refer to SD-WAN partners.
- **Pure SaaS-only enterprises with no owned data centers.** No fiber, no on-ramp use case the enterprise team owns.
- **Network fully outsourced to a single MSP with no internal engineering ownership.** No technical buyer.
- **No direct carrier contracts.** Everything through reseller or MSP means MaiaEdge has no commercial entry.

---

## Positioning Against Adjacent Layers (Not Rip-and-Replace)

MaiaEdge does NOT replace the enterprise's existing investments. This framing is critical because the enterprise has already spent on SD-WAN, carrier circuits, cloud connectivity, and possibly fabric subscriptions.

- **SD-WAN (Cisco, Juniper SSR / 128T, Versa, Cato, Fortinet, Palo Alto):** Different layer. SD-WAN handles branch and user. MaiaEdge handles inter-DC and cloud on-ramp. The two run together. Position the SSR / 128T overlay as exactly the kind of session-smart routing that benefits from a deterministic, observable underlay.
- **Carrier circuits (AT&T, Verizon, Lumen, BT, NTT):** Use them. MaiaEdge sits over the existing transport. The carrier keeps providing the circuit; MaiaEdge gives the enterprise determinism, visibility, and control across whatever transport is underneath.
- **Megaport / Equinix Fabric / PacketFabric:** Coexist. They become a transport option the fabric leverages by API where it makes commercial sense. The enterprise no longer depends on the third-party portal. 2026 sharpening: the incumbent on-ramp vendors are being re-missioned - Megaport is pivoting capital toward a distributed GPU inference cloud (June 2026 raise), and Equinix charges a premium tier for sovereignty enforcement (Fabric Geo Zones, May 2026). For an enterprise holding ports, the on-ramp vendor is now distracted, more expensive for compliance features, and a competitor for AI workloads - the strongest displacement window since the ICP launched. Counter on ownership, not features. Full doctrine: `context/core/differentiation-naas-aggregator.md`.
- **Cloud-native networking (AWS Cloud WAN, Azure vWAN, Google NCC):** Each cloud has its own. They do not federate well across clouds, and they do not solve the dark fiber redundancy problem at all. MaiaEdge is the cross-cloud, cross-DC layer that does.

Use this framing explicitly when an enterprise says "we already have SD-WAN" or "Megaport works fine" or "we just signed a long carrier agreement."

---

## Industry Landscape (2025-2026)

### Multi-cloud is now the default
80%+ of enterprises use two or more clouds in production. Each cloud provider's native networking is locked to its own cloud. Cross-cloud determinism, observability, and policy are unsolved at the cloud-vendor layer. Enterprises are increasingly building their own fabric to span clouds.

### AI workloads are pulling traffic to data centers the enterprise does not run
Inference and RAG workloads pull from corporate data lakes, vendor SaaS, and multiple clouds. The enterprise network team is being asked to deliver deterministic latency on paths they did not design for it.

### Sovereignty is a board-level conversation (and now a shipped product)
EU AI Act: transparency obligations land August 2, 2026, but the May 7, 2026 Digital Omnibus provisional agreement postponed high-risk obligations to December 2027 (Annex III) and August 2028 (Annex I) - do NOT say "fully enforceable August 2026." The audit pressure that did NOT slip is domestic and dated: NY DFS Part 500 annual certifications file under penalty of law (first cycle April 15, 2026; 27 consent orders, $144M+ cumulative fines), DORA's first Joint Examination Team examinations of 19 designated critical ICT providers run through 2026, and PCI v4.0 continuous segmentation validation is in force. Sovereignty also became a product: Equinix sells "network-level sovereignty enforcement" as a premium Fabric tier (Geo Zones, launched May 14, 2026, US included). Counter-position on ownership: a Geo Zone is a property of Equinix's network; MaiaEdge makes path control a property of YOUR network - own the enforcement point instead of renting it per circuit at a premium. BGP best-effort routing still cannot prove where data went; policy-based path control with jurisdictional audit trails remains the compliance gate.

### Rebalancing is selective, and it creates paths
86% of CIOs plan to move SOME workloads off public cloud (highest recorded), but only ~8% move whole workloads - the drivers are cost predictability, egress, and inference economics, not ideology. AI workloads specifically are already moving: Cloudian's 2026 data has 79% of enterprises having already pulled AI workloads back from public cloud, and 55% saying public cloud cannot meet inference latency. GPU colocation breaks even against cloud in under 12 months at high utilization. Every rebalanced workload creates new DC-to-colo-to-cloud paths the enterprise team must own. Lead with the path problem and the named workload ("the inference workloads coming back next quarter"), never with an exodus story.

### Dark fiber leasing has surged
Enterprise dark fiber leases between data centers, between DC and DR, and between DC and cloud on-ramp facilities are up significantly post-2023. The fiber is leased, but redundancy and observability are not solved by the lease.

### Network team is shrinking while scope is growing
Most enterprise network teams have 5-50 engineers. They are being asked to support AI, multi-cloud, sovereignty, and a growing site footprint without proportional headcount. Productized fabrics that do not require carrier-grade engineering depth are the only realistic answer.

### Branch SD-WAN saturation
Branch SD-WAN is largely done. The next round of network spend is shifting back toward the data center, the cloud on-ramp, and the inter-DC fabric. SD-WAN vendors are repositioning into SASE (security overlay), leaving the inter-DC and cloud-fabric layer open.

---

## MaiaEdge Relevance Bridges

| Their Trend | Their Pain | MaiaEdge Angle |
|---|---|---|
| Multi-cloud is the default | Each cloud's networking is locked to itself; cross-cloud paths are bespoke | "One fabric across AWS, Azure, GCP. Same provisioning, same visibility, same control." |
| AI workloads stress inter-DC and cloud paths | Network team did not design for deterministic latency at this scale | "Deterministic paths between data centers and into the cloud, without routing-protocol complexity." |
| Sovereignty is a board topic | BGP best-effort cannot prove where data went | "Policy-based path control with jurisdictional audit trails. Compliance can prove the path." |
| Dark fiber leases up, redundancy still manual | One pair, one path, no automated failover | "PBCs at each end, diverse fibers in, automated failover. Redundancy that actually is." |
| Network team scope growing faster than headcount | Cannot hire carrier-grade engineers fast enough | "Productized fabric, no BGP, no MPLS to manage. Operable by the team they already have." |
| Branch SD-WAN saturated, focus shifting back to inter-DC | The SD-WAN overlay does not give them inter-DC determinism | "MaiaEdge is the underlay. SD-WAN keeps doing its job at the edge. Fabric handles inter-DC and cloud on-ramp." |
| Cloud on-ramp through third-party fabric | Enterprise depends on Megaport / Equinix portal and support | "On-ramps under your control. Megaport / Equinix become transport options the fabric uses by API." |

---

## Insider Language Bank - By Sub-Segment

The Enterprise voice is NOT one voice. A VP Network at JPMorgan talks about the network differently than a VP Network at HCA Healthcare or a Director Network Operations at Cognizant BPS. Use the right sub-segment vocabulary in copy aimed at that sub-segment. Mixing sub-segments' vocabulary breaks the peer-recognition test.

### Cross-Enterprise (lands in all four sub-segments)
- "Our DR strategy assumes the dark fiber is redundant. It is not."
- "Megaport works until it does not. We need our own answer."
- "We are multi-cloud and the network team is being asked to make that feel like one cloud."
- "AI is pulling traffic in directions we did not design for."
- "Compliance asked us to prove where the data went. We could not."
- "Every new DC is a six-month networking project. That is the bottleneck on growth."
- "Whose SLA is it when it's three vendors deep?"

### Financial Services - Enterprise (banks, insurers, payment networks, capital markets)

**Architecture vocabulary buyers actually use:**
- "diverse path" / "physically diverse" (FFIEC examiner shorthand - appears in every RFP)
- "protected wave" vs "unprotected wave" (DWDM SKU distinction)
- "dual entrance" / "dual entry" (building-level fiber redundancy)
- "carrier of last resort" (the 30-year incumbent relationship they can't shed)
- "brownout" (the failure mode that doesn't trigger SLA credits but breaks trading)
- "concentration risk" / "critical third-party" / "CTPP" (DORA / NY DFS Part 500 / FFIEC trigger words)
- "microbursts" (the SOR / market-data feed failure mode)
- "deterministic latency" / "jitter envelope" / "latency-equalized" (NY4/NY5 matching engine spec)
- "hairpin" (bad word - traffic leaving the DC and coming back in via cloud)
- "multi-rail" (payments-team term that bled into network architecture)
- "path of least audit resistance" (gallows-humor phrase for the regulator-approved path)
- "physical-path verification" (FFIEC BCM IV.A.6 language)

**Real boardroom / CIO phrases at top-25 US banks 2025:**
- "control our own destiny, for business and regulatory reasons" (JPMorgan's Darrin Alves verbatim, 2025)
- "just-in-time capacity, five to 10 years out" (same source - the planning horizon)
- "right tool for the right job" (the hedge against "why aren't you all-cloud")
- "everything from mainframe to quantum computers and blockchain to public cloud and generative AI" (JPM Alves describing the stack)

**Regulatory drivers to reference in copy (don't overload - one per email max):**
DORA enforceable Jan 17 2025; CTPP designations Nov 18 2025 (AWS, Microsoft, Google formally designated); NY DFS Part 500 amendments Nov 1 2025 + first cert April 15 2026; ESMA EU T+1 target Oct 11 2027; FFIEC BCM IV.A.6 physical-path language; SOX, PCI-DSS, GDPR, GLBA stacked.

### Healthcare Systems - Enterprise (multi-hospital IDNs)

**Architecture vocabulary buyers actually use:**
- "Epic downtime procedure" (paper-charting fallback; invoking this is a board-level event)
- "Tier-1 clinical" (Epic, PACS retrieval, anesthesia monitoring, telemetry; RTO under 2 hours)
- "read-only mode" (Epic's degraded state when prod DB unreachable)
- "Hyperdrive cutover" (the Hyperspace-to-Hyperdrive migration most IDNs are mid-flight on through 2026)
- "Cogito on Azure" (Epic analytics/reporting tier moving to Microsoft Fabric)
- "imaging VLAN" / "PACS VLAN" (the dedicated low-latency segment for DICOM C-STORE)
- "DICOM C-STORE / C-FIND / C-MOVE" (the protocol verbs network teams tune around)
- "VNA" - vendor-neutral archive (the enterprise imaging store, distinct from departmental PACS)
- "HL7 / FHIR feeds" (integration engine traffic - Rhapsody, Mirth, Corepoint)
- "IoMT segmentation" or "medical device segmentation" (the Claroty Medigate / Elisity / Asimily project)
- "biomed inventory" (clinical engineering's device list - source of truth for IoMT segmentation)
- "big bang go-live" vs "phased go-live" (Epic migration patterns)
- "Cosmos contribution" (sending de-identified data to Epic's cross-customer research dataset)
- "TEFCA participation" (federated query traffic to QHINs - real new network flow 2024-2025)
- "OCR portal disclosure" (the public HHS "wall of shame" every CISO is terrified of)
- "HITRUST scope" (the in-scope systems for the org's r2 assessment)
- "BCDR exercise" (annual full DR failover test, which often doesn't fully succeed)
- "downtime tolerance" (what the CMO says is acceptable, which is always shorter than what's affordable)

**Boardroom / CIO phrases that land at IDNs:**
- "Post-Ascension, the segmentation question is on the audit committee agenda."
- "Change Healthcare reshaped how every health-system CISO thinks about lateral movement."
- "Our HIPAA Security Rule NPRM compliance plan is being written now - TLS 1.2+ and encryption-in-transit are moving from addressable to required."

**Regulatory drivers + recent incidents to reference:**
HIPAA Security Rule NPRM (Dec 27, 2024) - proposes removing "addressable" flexibility on encryption-in-transit and segmentation, TLS 1.2+ (NOT finalized as of mid-2026; the proposed-final window passed and a CHIME-led coalition is lobbying to withdraw it); OCR ransomware consent orders (April 23, 2026, four settlements) whose corrective action plans explicitly require network segmentation, asset inventory, and ePHI data-flow mapping - OCR is enforcing the segmentation substance NOW regardless of whether the rule finalizes; Oracle Cerner deletion incident (April 2025, 39-45 CHS hospitals on paper for 5 days); Ascension Black Basta (May 2024, 5.6M patients, network-segmentation lessons learned); Change Healthcare BlackCat (Feb 2024, 190M records, $3.09B annual hit); Yale New Haven (March 2025); HSCC Sector Mapping toolkit (Oct 2025); HSCC Updated Model Contract Language (Nov 2025).

### Retail and Distribution - Enterprise (national retailers + multi-DC corporate IT)

**Architecture vocabulary buyers actually use:**
- "peak readiness" (internal codename for the 6-month freeze starting roughly August; "we have to be peak-ready by week 32")
- "the freeze" / "code yellow / red period" (change-management lockdown for holiday)
- "cyber weekend" (Thanksgiving through Cyber Monday as one event)
- "endless aisle" (store associate ordering from any DC/store inventory)
- "OMS feeding the store" (order management pushing pick-tickets to BOPIS / ship-from-store)
- "in-scope vs out-of-scope" (PCI segmentation language - "is that VLAN in-scope?")
- "CDE" (cardholder data environment)
- "store-up minutes" (how Operations measures store network uptime against revenue)
- "curbside lane" (network path supporting curbside pickup - usually separate SSID + QoS)
- "DC-side fabric" vs "corp-side fabric" (warehouse-floor network vs corporate carpeted-space)
- "pick-to-light / voice-pick" (sensitive to jitter, not just bandwidth)
- "replication lag" (DC-to-DC sync delay for Oracle/SAP/Manhattan - measured in seconds, watched constantly)
- "active-active" vs "active-passive" for DC pairs (usually said with frustration)
- "tabletop" (quarterly DR exercise)
- "carrier diversity" (retail-specific concern because contract carriers often ride the same conduit)
- "last-mile from the wave" (gap between carrier's wavelength handoff and the retailer's MMR)
- "out-of-region DR" (DR site 250+ miles from primary, FFIEC-style standard borrowed into retail)
- "smart store / connected store" (corporate-marketing term for electronic shelf labels, computer-vision LP)
- "Cyber Monday math" (internal joke for capacity planning at 8-10× steady-state traffic)
- "drift" (when SD-WAN policy across 1,500+ stores diverges from intended state)

**Boardroom / CIO phrases that land at retailers:**
- "We can't touch infrastructure during peak readiness - the Q1/Q2 PO is the only window."
- "DC-to-DC replication lag is the thing nobody escalates until BOPIS times out."
- "Our SD-WAN is store-to-DC. What sits underneath it for DC-to-DC and DC-to-cloud is the conversation."

**Recent incidents and regulatory drivers to reference:**
Shopify Cyber Monday outage Dec 1, 2025 (5-6 hours during a $14.2B day); BF/CM weekend 2025 site outages at Walmart, Lowe's, Best Buy, J.Crew, Office Depot; Hot Topic Nov 2024 (57M customers via third-party analytics vendor Robling); CDK Global dealer outage 2024; Kroger-Albertsons merger killed Dec 11, 2024; PCI DSS v4.0 fully in effect March 2025 (64 new requirements, continuous segmentation validation, annual scope re-attestation); Walmart Sparky / WIBEY agents production 2025; Lowe's Mylow at 1,700+ stores; Albertsons FY2025 capex $1.7-$1.9B with Azure preferred public cloud; Home Depot appointed Angie Brown CIO June 2025; Publix Lakeland IT campus expansion.

### Outsourcing Services - Enterprise (BPO / operational delivery)

**Architecture vocabulary buyers actually use:**
- "seat" (the unit of capacity - everything is priced and provisioned per seat)
- "ramp" ("we have a 2,000-seat ramp in Manila in Q2")
- "pod" (physically segregated cluster of agents serving one client)
- "client carve-out" (per-client isolated network/security stack on shared physical infrastructure)
- "lift and shift the client" (replicating client's required network topology inside a delivery center)
- "onshore / nearshore / offshore mix"
- "follow-the-sun" (24x7 coverage via handoffs across continents - drives inter-DC traffic)
- "site failover" / "BCP site" / "paired site" (what happens when Manila goes underwater)
- "client-mandated carrier" (when an FS or HC client dictates AT&T/Verizon/BT as the only acceptable transport)
- "data residency clause" (contractual obligation to keep client data inside a named country/region)
- "in-scope environment" (PCI / HIPAA / SOX-bounded part of BPO's infrastructure for a given client)
- "client InfoSec audit" ("we have a Citi audit in two weeks")
- "path-level proof" (documented evidence that this client's traffic never traversed a non-approved jurisdiction)
- "shared services environment" vs "dedicated environment" (architecture distinction; dedicated commands premium)
- "connectivity SLA" (the uptime number in the MSA - typically 99.9% or 99.95% with credits)
- "BCR" / "SCCs" (Binding Corporate Rules / Standard Contractual Clauses for cross-border flows)
- "right-to-audit" / "audit right" (contractual right the client retains)
- "logical separation" vs "physical separation" (level of isolation being delivered)
- "client tenant" (the client's own AWS/Azure account that the BPO reaches into)
- "in-country processing" (literal requirement to keep storage and compute inside a named geography)

**Boardroom / CIO / Compliance phrases that land at BPOs:**
- "Every new client adds an MPLS tail and a compliance attestation."
- "Concentrix-Webhelp / TP-Majorel - two MPLS cores, two AD forests, years of parallel WAN."
- "Manila failover to Cebu has to be a controller decision, not a BGP convergence event."

**Recent incidents and regulatory drivers to reference:**
Super Typhoon Uwan/Fung-wong Nov 2025 (98 Philippine BPO sites under DOLE investigation for forcing on-site work); EU DORA enforceable Jan 17, 2025 (flowing to every EU financial-services BPO client); India DPDP Rules notified 2025 + cross-border framework (Rule 15) live; RBI 2025 NBFC Outsourcing Directions + IFS Cloud launch (Indian financial services BPO arms must process onshore); Genpact BCR-Processor approved by Romanian DPA May 2024; Cognizant + Astreya April 2026 (AI infra + data center services); Cognizant Neuro AI + NVIDIA March 2025; Genpact AI Gigafactory with GE Vernova Jan 2025; Teleperformance + Majorel integration complete early 2025 (€10.2B combined, 500+ AI projects, Azure OpenAI across 170 markets); Concentrix + Webhelp combination completed Sep 2023, still being network-integrated.

### KPIs they report (cross-Enterprise)
mean time to provision, mean time to identify (MTTI), site bring-up days, network availability, SLA compliance, MPLS-to-DIA migration percentage, cloud direct-connect cost per Gbps, dark fiber utilization, change failure rate, RPO / RTO for tier-1 systems

### Business terms to know (cross-Enterprise)
DC, DR, EHR, OT, SCADA, RTO, RPO, BC/DR, SD-WAN, SASE, Direct Connect, ExpressRoute, Cloud Interconnect, Type 1/Type 2 fiber, dark fiber lease, IRU (when leased from a fiber operator), MPLS sunset, DIA, NetBond, SCI, BGP, OSPF, IS-IS, Q-in-Q, EVPN, segment routing, ZTNA, SASE, SOC 2 Type II, ISO 27001

---

## Anonymized Proof-Point Bank - By Sub-Segment

These are anonymized proof-point patterns grounded in real industry reality. Use one per cold email. Match the sub-segment to the recipient. Pull from `context/segments/enterprise-use-cases.md` for use-case-specific proof points; this section is the consolidated bank.

### Financial Services - Enterprise

- "A top-10 US bank moved its inter-DC replication off a single-carrier protected wave to a dual-underlay design after a 2024 brownout exposed shared-conduit risk - FFIEC found the 'diverse' path actually shared a regional aggregation point and the finding was material."
- "A global custodian consolidated three regional cloud on-ramp fabrics under one carrier-grade overlay because vendor-risk had flagged each fabric as a separate concentration exposure under DORA and a CTPP designation was imminent."
- "A money-center bank's markets technology group rebuilt its trading-floor-to-NY4 path on dedicated lambdas because microbursts in the previous managed service were generating queue drops the algorithm desk could see but the carrier couldn't account for."
- "A regional bank integrating an acquisition ran two parallel WANs for 22 months because the acquired entity's existing carrier MSA couldn't be terminated without a regulator-notified plan."

### Healthcare Systems - Enterprise

- "A 12-hospital IDN we work with shaved Epic DR failover RPO from 90 seconds to under 15 because we cut jitter on the inter-DC path their existing carrier couldn't account for."
- "A regional system mid-Hyperdrive cutover used our fabric to bring three acquired-hospital sites onto the parent Epic instance in weeks instead of the 9-month carrier-circuit add-site cycle their network team had budgeted."
- "A multi-state Catholic health system running PACS retrievals across two metros stopped the radiologist complaints about study-load times once we gave them a deterministic path their VNA team could measure end-to-end."
- "After Ascension, an East Coast academic medical center had a board mandate to prove inter-DC traffic was segmented and encrypted in transit - we became part of that evidence package because their network team could enforce policy on the wire, not just trust the carrier's word."

### Retail and Distribution - Enterprise

- "A national grocer replaced their carrier-managed DC-to-DC wave with their own dark fiber pair between two corporate DCs because their Oracle Retail replication kept lagging during BOPIS pickup spikes - and they couldn't get root-cause out of the carrier inside the freeze window."
- "A home-improvement retailer discovered their 'diverse' fiber paths between primary and DR rode the same metro conduit for 11 miles - they only found out when a backhoe took both down on a Tuesday."
- "A national specialty retailer running Symbotic in three DCs moved bot-control traffic off contended carrier MPLS once a 90-second WCS hiccup stalled 400 bots during a holiday pre-build. Network team now owns the DC-floor uplinks, not the carrier."
- "A regional grocer cut PCI audit scope by two-thirds when they put their own segmented carrier fiber between corporate DC and the payment-gateway DMZ instead of routing through the shared MPLS that touched every store VLAN."

### Outsourcing Services - Enterprise

- "A North American CX outsourcer was running 22 client-mandated MPLS tails into a single 1,800-seat Manila floor - every new client logo required 10-14 weeks of carrier provisioning before agents could go live. We carved that down to a single delivery-center fabric with per-client logical tenancy, and their next ramp went live in under three weeks."
- "A regulated-financial-services BPO had a Tier 1 bank auditor demand path-level evidence that none of their card-payment workflows ever traversed a non-approved jurisdiction. SD-WAN reports couldn't generate it. Per-tenant traffic attestation closed the audit finding without re-architecting client carve-outs."
- "A nearshore BPO opening Medellín and Cali simultaneously lost two client commits because the incumbent carrier quoted 14 weeks to install. We brought both sites up on our fabric in 18 days, with cloud on-ramp to the clients' AWS regions live on day one."
- "An Indian-headquartered BPO had to fail an entire 4,000-seat Manila delivery center to Cebu in under four hours during a 2025 typhoon. Their existing redundant MPLS was active/standby with stale routing on the standby - active/active per-client across paired sites made the cutover a controller change, not a routing convergence event."

---

## Segment Vocabulary Lock

### MUST-Use Terms (Enterprise)
data center, DC, DR site, dark fiber, dark fiber redundancy, diverse paths, fiber pair, hot standby, active-active, cloud on-ramp, direct connect, multi-cloud, hop-by-hop visibility, deterministic paths, your network, your fabric, your team, your control, sovereignty, audit trail, PBC, port extender, fabric, productized, no routing protocols.

### BANNED Terms (From Other Segments)
- "Keep your customer," "your portal, your invoice," "build your own fabric to sell" (operator monetization language)
- "Monetize stranded fiber," "wholesale activation," "win multi-state deals," "extend reach to new markets" (carrier/operator economics)
- "Tenant," "meet-me room," "cross-connect," "interconnection revenue" (colo language)
- "GPU cluster," "inference latency," "training run," "recompute tax" (neocloud language)
- "Aggregator," "TSD," "line-card" (MSP language)

### Cold Outreach Rules
- Credibility anchors (Acme Packet, 128T, Andy Ory) are BANNED in cold emails and LinkedIn. Reserve for live calls and follow-ups.
- NO sign-offs in emails. Signatures are auto-appended.
- Lead with the problem in their language: "your dark fiber between DCs is one cut from an outage" or "your cloud on-ramp goes through Megaport." Then the angle.
- Do NOT lead with technical detail (SSR1300 / HAsync / 100GigE port specifics). The cheat sheet stays broad. Technical detail belongs in the design conversation, not the first email.

---

*Cross-references: **Enterprise Use Cases Outreach Playbook (`context/segments/enterprise-use-cases.md`)** - the 8 priority use cases × sub-segment fit × persona fit × lead-angle templates × proof points × use-case-specific objections. Required reading before drafting Enterprise cold outreach. Companion files: Cheatsheet (`context/partner-assets/cheatsheet-enterprise.md`), Messaging Framework, Cloud On-Ramp business case, Competitive Positioning Guide, Terminology Glossary.*
*Created: May 2026 (initial - Meijer / Ken Cunningham + Woody Acosta dark fiber redundancy design as anchor account)*
