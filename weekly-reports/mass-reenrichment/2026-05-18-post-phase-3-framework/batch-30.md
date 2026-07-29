# Mass Re-Enrichment Sweep - Batch 30
**Sweep:** 2026-05-18-post-phase-3-framework
**Date:** 2026-05-18
**Operator:** CRM Guardian (Cowork)
**Parameters:** SWEEP_KICKOFF_DATE=2026-05-18, BATCH_SIZE=50, VERIFY_DEPTH=leverage-and-patch, APOLLO_ENFORCEMENT=disabled, SEGMENT_SCOPE=all_active_icp

## Summary

- **Processed:** 50/50 unique (no offset-wrap duplicates this batch)
- **Path mix:** LIGHT 27 / MEDIUM 23 / FULL 0 / HOLD 0
- **Tier writes:** 3 promotions, 6 demotions, 0 hs_is_target_account skips
- **Segment changes (cascade-relevant):** 2 (Sri Lanka Telecom, Lumen Technologies)
- **Sub-segment migrations:** 5 within-Fiber demotions to Municipal/Cooperative + 4 cross-segment reclassifications
- **Apollo this batch:** 0 credits
- **web_searches:** 4 (RTC Communications, Latitude.sh, CVEC Fiber, Schurz Broadband Group)
- **HubSpot write batches:** 5 of 10 (0 failures)
- **Pool remaining:** ~1,272 (1,322 at page 5 - 50 processed; eventual indexing lag expected)
- **ETA:** ~26 more batches at BATCH_SIZE=50

## Per-record audit

### Page 1 (offset 0)

### Brandenburg Telephone (297989642964)
- Path: LIGHT · Segment: unchanged · Sub-segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: all 7 fields present, framework-consistent, recent_news fresh (2026-05-11 Fiber Connect)

### Trace Fiber Networks (296883684038)
- Path: LIGHT · Segment: unchanged · Sub-segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Chickasaw Nation subsidiary; tribal-owned, considered Regional CLEC; recent_news fresh

### Start Campus (268073696972)
- Path: LIGHT · Segment: unchanged · Sub-segment: AI Signals - colo (unchanged) · Tier: tier_1 (unchanged) · Apollo: no · web_searches: 0
- Reason: T1 anchor (Microsoft $10B PE); recent_news Nov 2025 anchor signal preserved

### Armstrong (297888731894)
- Path: LIGHT · Segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: 11th-largest US MSO, 6-state fiber, Fiber Connect attendee fresh

### Luminate Fiber (297742427850)
- Path: MEDIUM · Sub-segment: Regional CLEC -> Municipal / Cooperative - Fiber operator · Tier: tier_3 -> tier_4 · Apollo: no · web_searches: 0
- Reason: Subsidiary of Yampa Valley Electric Association (YVEA), electric cooperative model; account_brief contains "subsidiary of YVEA" confirmation

### Sandhill (316227857140)
- Path: MEDIUM · Sub-segment: Regional CLEC -> Municipal / Cooperative - Fiber operator · Tier: tier_3 -> tier_4 · Apollo: no · web_searches: 0
- Reason: account_brief explicitly states "Sandhill Telephone Cooperative"

### Cellcom (297936668399)
- Path: LIGHT · Segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Regional wireless+fiber operator, fields present, Nsight subsidiary

### Rainbow Communications (297986182905)
- Path: MEDIUM · State: England -> Kansas · Country: United Kingdom -> United States · Owner: 159350430 -> 162339176 (Ken Cunningham West) · Sub-segment: Regional CLEC -> Municipal / Cooperative - Fiber operator · Tier: tier_3 -> tier_4 · Apollo: no · web_searches: 0
- Reason: Apollo geo error (brief explicitly Kansas-based); "telecommunications cooperative founded 1951"

### RTC Communications (297969950435)
- Path: MEDIUM · Sub-segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 1
- Reason: Template-bleed remediation - account_brief + provisioning_landscape regenerated. Confirmed Montgomery, IN private fiber operator, founding Hoosier Net member, $3.1M BEAD grant

### Inland Cellular (320873011959)
- Path: LIGHT · Segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Regional wireless+fiber operator; infrastructure_profile "POPs: Enterprise (100+)" SUSPECT for 30-employee operator but plausible across 2 states

### Page 2 (offset 10)

### Cal-Ore Telephone (268111627991)
- Path: MEDIUM · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Filled missing provisioning_landscape + hyperscaler_proximity = "None Known"; 65+ year ILEC

### Endeavor Communications (297987984059)
- Path: MEDIUM · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Template-bleed remediation - account_brief + provisioning_landscape regenerated from recent_news context (Justin Clark CEO Dec 2025, Endeavor IT merger Jan 2024)

### CVEC Fiber (296851879638)
- Path: MEDIUM · Sub-segment: Regional CLEC -> Municipal / Cooperative - Fiber operator · Tier: tier_3 -> tier_4 · segmentation_confidence: -> high_90 · Apollo: no · web_searches: 1
- Reason: Confirmed wholly-owned subsidiary of Canadian Valley Electric Cooperative (1939 nonprofit electric coop, 10-county Oklahoma footprint). Template-bleed remediation + sub-segment migration

### Ripple Fiber (292719725284)
- Path: MEDIUM · Sub-segment: unchanged · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Sparse account_brief regen + filled provisioning_landscape + hyperscaler_proximity. Southeast FTTH, 83 cities, 6 states, ~255 employees

### Schurz Broadband Group (292748566217)
- Path: MEDIUM · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 1
- Reason: Template-bleed remediation. Confirmed Schurz Communications division (July 2025), 6 regional broadband subs (Antietam MD, Burlington Telecom VT, Hiawatha MN, Long Lines IA/NE/SD, NKTelco OH, Orbitel AZ). Holding-co model

### All West Communications (292752233182)
- Path: MEDIUM · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Template-bleed remediation from recent_news context. Rebranded as All West Fiber Oct 2025, new CEO Justin Nelson + CTO Matt Weller Apr 2025, Bluffdale UT fiber construction Mar 2025

### Latitude.sh (297918677723)
- Path: MEDIUM · Segment: NeoCloud (unchanged, but ICP re-eval flagged) · Tier: tier_1 (unchanged) · Apollo: no · web_searches: 1
- Reason: Updated recent_news_or_trigger_event with confirmed completed Megaport acquisition ($300M, closed 2025-11-27). FLAG: Latitude.sh now Megaport subsidiary; Megaport is direct MaiaEdge NaaS competitor. Cooper to decide re-classification to `Other` (competitive reference)

### Gearheart Communications (266982423277)
- Path: LIGHT · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Regional KY/VA/WV fiber operator, framework-consistent, recent_news 2025-10

### InterBel Telephone Cooperative (297782865623)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already correctly classified Municipal/Cooperative T4

### Beam Cloud (297969950441)
- Path: MEDIUM · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Filled hyperscaler_proximity = "None Known". 5 employees YC company; state-vs-brief geo mismatch flagged (state MA vs brief NY) but no patch

### Page 3 (offset 20)

### OPIQUAD (267969423052)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Italian MSP, M&A activity Aug 2025, framework-consistent

### RF Connect (268012614346)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Michigan wireless+CBRS integrator. Classification "Telecom Aggregator - MSP" arguably suboptimal (specialty wireless integrator); deferred to D7

### Tranquil Hosting (268012614345)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: 5-employee NC hosting/colo MSP, German DC expansion Nov 2025

### The Flat Planet Phone (267985661658)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: 6-employee Hosted PBX provider; FCC robocall enforcement order Dec 2024 = REGULATORY RISK flag for Cooper review

### Sri Lanka Telecom (268012614339)
- Path: MEDIUM · Segment: Fiber Operator -> Network Operator(Tier 1 / VNO) · Sub-segment: Long Haul / Backbone - Fiber operator -> Tier 1 Carrier - Network Op · Tier: tier_2 -> tier_1 · segmentation_confidence: -> high_90 · Apollo: no · web_searches: 0
- Reason: National incumbent telco (Sri Lanka), 8058 employees, 60K+ route miles, 9M customers, retail+wholesale. Continues "national operator under-tiering" pattern. SEGMENT CHANGE - cascade-relevant

### Megawire (268111627990)
- Path: MEDIUM · State: California -> Ontario · Country: United States -> Canada · Owner: 162339176 -> 159350430 (Tim Z International) · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Apollo geo error (brief explicitly Waterloo, Ontario, Canada). Acquired by Uniserve Communications Nov 2025

### Asset Black (268111635142)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Momentum-owned (2023 acquisition); recent_news lacks date prefix but acceptable

### Wholesail Networks (268073696975)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Pacific NW long-haul fiber, framework-consistent; recent_news empty (no current signal known)

### Citizens Telephone Cooperative (was citizensdsl.com) (316197305048)
- Path: MEDIUM · Name: "citizensdsl.com" -> "Citizens Telephone Cooperative" · Sub-segment: Regional CLEC -> Municipal / Cooperative - Fiber operator · Tier: tier_3 -> tier_4 · Apollo: no · web_searches: 0
- Reason: account_brief explicitly states "Citizens Telephone Cooperative, founded 1914 in Floyd, VA". Name patch + sub-segment migration

### Zion Broadband (268208411379)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: West Texas ISP transitioning from fixed wireless to fiber; aggregation model retained

### Page 4 (offset 30)

### softbox.com.do / HDCO Group (272717948637)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Dominican Republic neutral wholesale operator. Name field "softbox.com.do" vs domain "hdcogroup.do" mismatch noted but deferred to D7

### SupraNet Communications (274768041659)
- Path: LIGHT · Tier: tier_3 (unchanged) · Apollo: no · web_searches: 0
- Reason: Madison WI fiber+colo, framework-consistent

### Point5 (268250706644)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Boston Metro MSP, TOWARDEX partnership Aug 2025, framework-consistent

### Spin Servers (268210252474)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: 5-employee wholesale IaaS (Dallas + San Jose), framework-consistent

### Ridge Wireless (268208452325)
- Path: MEDIUM · State: Ohio -> California · Owner: 161889085 -> 162339176 (Ken Cunningham West) · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Apollo geo error (brief explicitly Silicon Valley + California Central Coast)

### Ruralband (268208452331)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already correctly classified Municipal/Cooperative T4 (PGEC subsidiary)

### Neutrona Networks (268226624226)
- Path: MEDIUM · Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator · Tier: tier_3 -> tier_2 · segmentation_confidence: -> high_90 · Apollo: no · web_searches: 0
- Reason: International carrier (LatAm + Caribbean), MPLS + SD-WAN + dedicated internet, acquired by Transtelco 2020. R3 DEDUP FLAG: check vs separate Transtelco record

### Intelligent Computing Solutions (268215653051)
- Path: LIGHT · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Illinois MSP, framework-consistent

### LatWan (268447804090)
- Path: MEDIUM · segmentation_confidence: -> high_90 · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Filled provisioning_landscape (OMNI platform across 32 LatAm countries, 500+ local networks) + hyperscaler_proximity = "None Known"

### Grove Networks (268288174827)
- Path: MEDIUM · Sub-segment: Telecom Aggregator -> Managed Network Services - MSP · segmentation_confidence: -> high_90 · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Hospitality IT MSP misclassified as Telecom Aggregator (no carrier capacity aggregation evidence). Filled provisioning_landscape + hyperscaler_proximity

### Page 5 (offset 40)

### System Crew (268447849149)
- Path: MEDIUM · Sub-segment: Telecom Aggregator -> Managed Network Services - MSP · segmentation_confidence: -> high_90 · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Germany maritime managed services (cruise/yacht/offshore), reclass to Managed Network Services more accurate than Telecom Aggregator

### Nearshore Networks (268447846112)
- Path: MEDIUM · Sub-segment: Telecom Aggregator -> Managed Network Services - MSP · segmentation_confidence: -> high_90 · Tier: tier_2 (unchanged) · Apollo: no · web_searches: 0
- Reason: Texas maritime + offshore managed services (NEO platform, 60+ ports worldwide), same reclass rationale as System Crew

### Lumen Technologies (was CenturyLink) (296880096970)
- Path: MEDIUM · Name: "CenturyLink" -> "Lumen Technologies" · Segment: Fiber Operator -> Network Operator(Tier 1 / VNO) · Sub-segment: Tier 2 National Wholesale -> Tier 1 Carrier - Network Op · Tier: tier_2 -> tier_1 · segmentation_confidence: -> high_90 · Apollo: no · web_searches: 0
- Reason: CenturyLink rebranded to Lumen 2020-09 (5 years stale identity). AT&T closed $5.75B Mass Markets fiber acquisition Feb 2026, leaving Lumen enterprise/wholesale focused. 50K+ route miles = Tier 1 incumbent. Deal-state checked (0 deals on record). FLAG: Lumen Private Connectivity Fabric is direct MaiaEdge NaaS competitor. R3 DEDUP FLAG: check vs separate Lumen record

### Pemiscot Dunklin Electric Cooperative (296850118378)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already Municipal/Cooperative. NO BROADBAND EVIDENCE in brief (template-bleed: "research needed"); recent_news only Youth Programs (electric coop). FLAG for D7: verify fiber service exists or migrate to non-ICP

### Holland Board of Public Works (296851879626)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already Municipal/Cooperative; community-owned MI municipal utility (electric+water+fiber), 455 fiber route miles, framework-consistent

### East Buchanan Telephone Cooperative (296880096955)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already Municipal/Cooperative; member-owned Iowa coop, 100% fiber network expanding under County Line Fiber brand

### Lincoln County Telephone System (296850118372)
- Path: MEDIUM · Sub-segment: Long Haul / Backbone -> Regional CLEC - Fiber operator · Tier: tier_2 -> tier_3 · segmentation_confidence: -> high_90 · Apollo: no · web_searches: 0
- Reason: Rural Nevada ILEC since 1919, primary fixed terrestrial ISP. Previous Long Haul/Backbone classification overstated scale; Regional CLEC fits small-town ILEC pattern

### Grayson-Collin Electric Cooperative (296883684046)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already Municipal/Cooperative. NO BROADBAND EVIDENCE in brief (template-bleed: "research needed"); recent_news only "high bills" member complaint. FLAG for D7: verify fiber service exists or migrate to non-ICP

### Stoneham Cooperative Telephone (296883684045)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already Municipal/Cooperative; CO coop, Colorado Fiber Network member, framework-consistent

### Panhandle Telephone Cooperative (296883684041)
- Path: LIGHT · Tier: tier_4 (unchanged) · Apollo: no · web_searches: 0
- Reason: Already Municipal/Cooperative; Oklahoma Panhandle 1954 coop, 155 employees, fiber+cellular+phone, framework-consistent

## R3 dedup flags raised this batch (5)

1. Lumen Technologies (296880096970) <-> any separate "Lumen" record
2. Megawire <-> Uniserve Communications Corporation (post-2025-11 acquisition)
3. Neutrona Networks <-> Transtelco (post-2020-04 acquisition)
4. Asset Black <-> Momentum (post-2023-08 acquisition)
5. Latitude.sh <-> Megaport (post-2025-11 acquisition)

## Data quality follow-ups (open)

1. Inland Cellular - infrastructure_profile "POPs: Enterprise (100+)" suspect for 30-employee 2-state regional wireless operator
2. Pemiscot Dunklin Electric Cooperative - no broadband evidence; may be misclassified pure-electric coop; flag for D7
3. Grayson-Collin Electric Cooperative - same pattern as Pemiscot Dunklin; flag for D7
4. softbox.com.do - record name vs domain mismatch (real domain is hdcogroup.do); flag for D7
5. The Flat Planet Phone - FCC robocall enforcement order Dec 2024; regulatory risk flag for Cooper review
6. Latitude.sh - now Megaport-owned post-2025-11 acquisition; ICP re-evaluation needed (competitive reference vs prospect)
7. Beam Cloud - state (MA) vs geographic_focus (NY) mismatch; minor

## Continuing patterns (vs batch 29)

- **National operator under-tiering:** +2 (Sri Lanka Telecom, Lumen Technologies). Cumulative ~29.
- **Within-Fiber demotions to Municipal/Cooperative:** +5 (Luminate Fiber, Sandhill, Rainbow Communications, CVEC Fiber, Citizens Telephone Cooperative). Cumulative ~13.
- **Template-bleed remediation:** +7 (RTC, CVEC, Endeavor, Ripple, Schurz, All West, Lumen). Cumulative ~13.
- **Apollo geo errors:** +3 (Rainbow Communications, Megawire, Ridge Wireless). Cumulative ~7.
- **Asset-light MSP misclassified as Fiber Op:** 0 this batch.
- **SaaS misclassified as NeoCloud:** 0 this batch.
- **Greenfield reclass:** 0 this batch.
- **manual_review_required resolution:** 0 this batch.

## NEW patterns this batch (2)

1. **Maritime-vertical MSP misclassified as Telecom Aggregator** - 2 this batch (System Crew DE, Nearshore Networks TX). Reclassified to Managed Network Services - MSP. Cumulative 2.
2. **Acquired-by-competitor records needing ICP re-eval** - 1 this batch (Latitude.sh acquired by Megaport). Flagged for Cooper. Cumulative 1.

## Pool drain status

- Before batch 30: ~1,398 (per batch 29 DM)
- Done this batch: 50 effective (no offset wrap duplicates)
- Pool remaining: ~1,272 (estimate after indexing settles)
- ETA: ~26 more batches at BATCH_SIZE=50

## Run health: :white_check_mark: GREEN

- All 5 HubSpot write batches succeeded (10/10/10/10/10, 0 failures)
- No HubSpot 429s, no Apollo calls, no Slack DM failures (yet)
- No HOLDs, no manual_review escalations
