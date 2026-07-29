# Mass Re-Enrichment Sweep — Batch 3

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 3
**Date:** 2026-05-18
**Processed:** 50 / 50
**Apollo this batch:** 0 credits
**Run health:** GREEN

## Path mix

| Path | Count |
|---|---|
| LIGHT | 0 |
| MEDIUM | 22 |
| FULL | 0 |
| Flagged for deletion | 22 |
| Other (Partner Target) | 6 |

## Tier writes

- Promotions (toward T1): 1 (HCL Enterprise tier_2 → tier_1)
- Demotions (toward T5): 4 (Got.Net tier_2→tier_3; Wisconsin CyberLynk tier_2→tier_3; KDS Networks tier_2→tier_3; Layer42 Networks tier_3→tier_4)
- Skipped (hs_is_target_account=true): 0
- Other (segment-driven tier_5): 6

## Sub-segment changes

- Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP: 7 (CCR Technologies, Net2Phone Canada, Quest Technology Systems, Acuutech, Got.Net, Netrix Global, Wisconsin CyberLynk Network)

## Segment changes (cascade fires applicable to associated contacts)

- MSP/Aggregator → Flagged for deletion: 14 (Virtustar, rackonomics, MANGO-OMC, toto networks, V-Tell, GAC, CTel, ATxTel, ngenious, wilson-global, 128 Technology, Touchtone, Techmate, BHC, ISG, Truepacket, Resolve Tech, FlowSec, ECI, Sumauma)
- Fiber Operator → Flagged for deletion: 2 (FPL FiberNet [Crown Castle Fiber / Zayo dup], Pac-West Telecomm [MISDOMAIN to bank, defunct CLEC])
- MSP/Aggregator → Other (Partner Target): 5 (DSR, XKL, Pearce Services, JSA, Fortress Solutions, JSI)

## Domain corrections

- Netrix Global (254549120746): `nplus2.com` → `netrixglobal.com`

## Per-record entries

### vCom Solutions (206938584804)
- Path: MEDIUM
- Domain: vcomsolutions.com
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Cloud + Telecom Hybrid MSP - MSP (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- Apollo used: no
- Reason: Refresh post-AppDirect acquisition Dec 2025; trim brief and provisioning_landscape to 2-4 sentence cap.

### Virtustar (200823981796)
- Path: FLAG
- Segment: MSP/Aggregator → Flagged for deletion
- Reason: Technology consultancy (cloud/AI/cybersecurity/5G IoT integration) — D1 disqualifier.

### rackonomics (208232305368)
- Path: FLAG
- Reason: Small AI startup in BC, no infrastructure evidence — D1 disqualifier.

### MANGO-OMC (208235621063)
- Path: FLAG
- Reason: South African PR/marketing agency — D1 disqualifier.

### toto networks (194239436494)
- Path: FLAG
- Reason: Atlanta-area "cloud service nodes" provider with thin public footprint, no PeeringDB / fiber-operator filings — D1 disqualifier.

### V-Tell (209166806766)
- Path: FLAG
- Reason: Hong Kong consumer VPN app on Google Play — D1 disqualifier.

### DSR (Diversified Systems Resources, 209230110409)
- Path: Other (Partner Target)
- Segment: MSP/Aggregator → Other; Tier → tier_5
- Reason: 40-year BSS/OSS-adjacent vendor providing tech support, provisioning workflow, billing, EDI to ISPs.

### XKL (192899501811)
- Path: Other (Partner Target)
- Segment: MSP/Aggregator → Other; Tier → tier_5
- Reason: Optical/DWDM equipment vendor (Cisco co-founder Len Bosack ownership).

### HCL Enterprise (192899501813)
- Path: MEDIUM
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Cloud + Telecom Hybrid MSP - MSP (unchanged)
- Tier: tier_2 → tier_1
- Apollo used: no
- Reason: ~$11B revenue, 210K employees, 250+ DC sites globally — promote to tier_1. Refresh all 7 enriched fields under Phase 3 framework.

### GAC (192886921924)
- Path: FLAG
- Reason: UAE-headquartered shipping/logistics conglomerate (suspect $19.1B revenue is flagged data quality issue per CLAUDE.md) — D1 disqualifier.

### CTel / Consolidated Telecom (192888735459)
- Path: FLAG
- Reason: Inmate phone systems for correctional facilities — vertical-niche telecom outside ICP.

### CCR Technologies (192916122339)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Reason: Cedar Rapids IA holding co with 3 owned DCs + 3,000+ carrier partners + multi-vertical brands. Refresh brief; trim from 4-paragraph to 2-4 sentence cap.

### ATxTel (193094707950)
- Path: FLAG
- Reason: Test and measurement solutions vendor to telecom industry — D1 disqualifier.

### Net2Phone Canada (133572099795)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Reason: UCaaS provider with redundant DCs; legitimate Cloud + Telecom Hybrid MSP. HIPAA AI Agent launch news.

### ngenious (133509641956)
- Path: FLAG
- Reason: Edge computing / AI-IoT product vendor distributed through Telarus channel — D1 disqualifier.

### wilson-global (159344400092)
- Path: FLAG
- Reason: PR/communications consulting firm (likely Wilson Global Communications) — D1 disqualifier.

### Quest Technology Systems (133570302700)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Confidence: medium_7089 → high_90
- Reason: Real 9-DC managed services + colocation provider since 1982. Refresh brief; correct sub-segment.

### 128 Technology (193168217848)
- Path: FLAG
- Reason: Acquired by Juniper Networks in 2020 and integrated as Juniper SSR product — no longer independent operating company.

### Touchtone Corporation (192879702770)
- Path: FLAG
- Reason: AS/400 / IBM iSeries business software developer — D1 disqualifier (not the unrelated TouchTone Communications telecom firm).

### Techmate (193866877683)
- Path: FLAG
- Reason: On-demand IT smart-hands marketplace, not telecom — D1 disqualifier.

### Wave Call (208819353315)
- Path: MEDIUM
- Reason: Wholesale VoIP and SIP trunking aggregator. Refresh brief.

### BTS / Business Telecommunications Services (208821148373)
- Path: MEDIUM
- Confidence: medium_7089 → high_90
- Reason: Exclusive International Voice Managed Services partner for Liberty Latin America across 26 Caribbean/LatAm markets. Refresh brief.

### BHC (208857135827)
- Path: FLAG
- Reason: Civil engineering / surveying firm (fiber design is one of many service lines) — D1 disqualifier.

### Pearce Services (193866877679)
- Path: Other (Partner Target)
- Segment: MSP/Aggregator → Other; Tier → tier_5
- Reason: Outsourced repair/maintenance/engineering services for telecom + renewables. Acquired by CBRE Nov 2025 for ~$1.2B. Field-services partner motion.

### Resolve Tech Solutions (193863999175)
- Path: FLAG
- Reason: SAP / IT modernization consultancy (501-1,000 employees) — D1 disqualifier.

### FlowSec (193865438923)
- Path: FLAG
- Reason: Tel Aviv DDoS protection vendor — D1 disqualifier.

### ECI Software Solutions (193863998148)
- Path: FLAG
- Reason: Manufacturing/distribution ERP vendor — D1 disqualifier.

### JSA / Jaymie Scotto & Associates (209032373963)
- Path: Other (Partner Target)
- Segment: MSP/Aggregator → Other; Tier → tier_5
- Reason: Digital infrastructure PR/branding/marketing agency since 2005; ecosystem partner.

### Fortress Solutions (252453588714)
- Path: Other (Partner Target)
- Segment: MSP/Aggregator → Other; Tier → tier_5
- Reason: Open RAN / private 5G systems integrator (Airspan NTIA NOFO 2 partner; Plano 5G Innovation Lab).

### Sumauma Telecom (167113651945)
- Path: FLAG
- Reason: Brazilian B2B telecom software/consulting vendor — D1 disqualifier.

### Acuutech (223979096790)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Reason: UK Managed Hybrid Cloud provider. Devoteam partnership July 2025.

### ISG (194005222095)
- Path: FLAG
- Reason: Multi-state architecture / planning / civil engineering firm — D1 disqualifier.

### Truepacket (132996276936)
- Path: FLAG
- Reason: Domain truepacket.io exists but no public product, customer, or operating evidence — D1 disqualifier.

### John Staurulakis / JSI (208880541395)
- Path: Other (Partner Target)
- Segment: MSP/Aggregator → Other; Tier → tier_5
- Reason: Specialty regulatory and compliance consulting firm serving 400+ rural broadband / ILEC clients; ecosystem partner.

### Strata Networks (254951523062)
- Path: MEDIUM
- Confidence: medium_7089 → high_90
- Reason: Real Regional CLEC fiber operator (UT, CO, WY). Open-access overbuild in Lehi UT Oct 2025. Refresh brief, trim.

### Got.Net (254554504943)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Tier: tier_2 → tier_3
- Reason: Small regional Santa Cruz CA ISP/MSP since 1995 (wireless + colo + IP transit + metro Ethernet + VoIP). Demote tier (~25 employees, narrow geo).

### Netrix Global (254549120746)
- Path: MEDIUM
- Domain: nplus2.com → netrixglobal.com (MISDOMAIN correction)
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Confidence: medium_7089 → high_90
- Reason: Real engineering-led MSP (600+ engineers); acquired Ricoh USA Managed IT Services Oct 31, 2025.

### FPL FiberNet (254547320539)
- Path: FLAG
- Reason: Crown Castle Fiber legacy entity (FPL FiberNet 11,500 route miles acquired by Crown Castle 2016). Crown Castle Fiber Solutions now being acquired by Zayo for $4.25B (H1 2026 close). Duplicate of Crown Castle Fiber / Zayo record.

### Wisconsin CyberLynk Network (254547320543)
- Path: MEDIUM
- Sub-segment: Telecom Aggregator - MSP → Cloud + Telecom Hybrid MSP - MSP
- Tier: tier_2 → tier_3
- Reason: Small MSP + DC hosting in WI / IL / AZ (Milwaukee + Phoenix DCs). Demote tier for size.

### KDS Networks (254558124752)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Small rural Montana MSP/aggregator (~30 employees). Demote tier; flag at low_5069 for D7 re-validation.

### Pac-West Telecomm (254626062055)
- Path: FLAG
- Reason: Original Pac-West Telecomm CLEC filed Ch.11 in 2010 / absorbed by Granite Telecom. Domain pacwest.com on this record now belongs to Pacific Western Bank ($1.158B Banking entity, 2,438 employees). MISDOMAIN + defunct CLEC — D1 disqualifier.

### Wintek (254627886802)
- Path: MEDIUM
- Confidence: high_90 (unchanged)
- Reason: Small regional fiber + colo in Lafayette IN. Owned by Tipmont REMC since 2019. Trim brief; refresh news to FTTH expansion.

### China Mobile International (254885110482)
- Path: MEDIUM
- Confidence: medium_7089 → high_90
- Reason: Real Tier 1 international backbone specialist. SEA-H2X submarine cable HK landing Nov 2025. Refresh brief, trim.

### Cloudnium (254885110484)
- Path: MEDIUM
- Reason: Small colo in TX + WI; Dublin expansion planned. December 2025 dedicated server launch in Dallas.

### Indy Telcom (255118549734)
- Path: MEDIUM (DUP flag noted)
- Reason: Netrality Data Centers' Indy facility. 9-acre 205K sq ft carrier hotel campus, 10.5 MW, 40+ on-net providers. July 2025 high-density AI/ML/HPC expansion. Note: may duplicate Netrality Data Centers parent record — flag for R3 audit.

### Tier Net Technologies (255118549736)
- Path: MEDIUM
- Reason: Small web hosting + colo across 8 leased DCs; HQ Binghamton NY.

### US Colo (255207759558)
- Path: MEDIUM
- Reason: Mid-size colo with facilities in LA and Seattle.

### Layer42 Networks (254885110480)
- Path: MEDIUM
- Tier: tier_3 → tier_4
- Reason: Suspect prior "100+ POPs" data on a 5-employee CA Bay Area colo. Downgrade infrastructure_profile to Small/Small. Demote tier. Flag for D7 deep dive.

### DP Facilities, Inc. (255118549733)
- Path: MEDIUM
- Reason: Ashburn VA HQ + 65K sq ft Tier III Mineral Gap (Wise VA) facility, 45 MW. High-security government/healthcare/finance vertical.

### ServerMania (254558124747)
- Path: MEDIUM
- Confidence: low_5069 → high_90
- Reason: Real global small colo + IaaS hosting (LAX, Dallas, Buffalo, Piscataway, Montreal, Vancouver, London, Amsterdam, Auckland). AraCloud IaaS launch April 2025.

## Notable patterns and follow-ups for CLAUDE.md "Known Data Quality Follow-ups"

1. **Pac-West Telecomm MISDOMAIN to Pacific Western Bank** — `pacwest.com` belongs to a bank; the legacy CLEC has been defunct since 2010. Any other records using common domain patterns (`*.com` that match well-known non-telecom businesses) need MISDOMAIN audit.
2. **Layer42 Networks 100+ POPs claim** is inconsistent with company size (5 employees). Suggests prior enrichment over-stated infrastructure based on weak signals. D7 should deep-dive other low-confidence records with mid-size+ infrastructure_profile values.
3. **Indy Telcom duplicate of Netrality** — R3 Duplicate Accounts audit should detect this pair on next fire.
4. **FPL FiberNet duplicate of Crown Castle Fiber / Zayo** — Zayo close pending H1 2026; R3 should detect.
5. **"Enterprise (Standard) - Not a target segment. No enrichment performed."** placeholder brief was found on 19 of the 50 records in this batch — this string is the legacy MSP/Aggregator pre-ICP framing. All cleared in batch 3 writes.

## Drain status

- Total processed in sweep (across batches 1-3): ~110 records (2,715 → 2,605)
- Remaining: 2,605
- ETA: ~52 more batches at BATCH_SIZE=50
