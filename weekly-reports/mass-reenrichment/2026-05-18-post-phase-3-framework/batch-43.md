# Mass Re-Enrichment Sweep — Batch 43

**Sweep:** 2026-05-18-post-phase-3-framework
**Run date:** 2026-05-19
**Records processed:** 50 / 50
**Path mix:** LIGHT 28 · MEDIUM 20 · FULL 2 (both evictions) · HOLD 0
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled)
**Pool drain:** 50 → 659 remaining (was 709 at start)
**Trigger query:** customer_segment IN [6 ICPs], NEQ Flagged for deletion, NEQ Customer, hs_object_id NEQ 124293230301, (last_enriched_date NULL OR LT 2026-05-18); sort hs_object_id ASC; limit 50.
**HubSpot writes:** 50/50 succeeded across 5 batches of 10. Zero 4xx/5xx.

## Headline patterns

- **16 sub-segment promotions Regional CLEC → Municipal/Cooperative** (tier_3 → tier_4): all are explicitly mutual / member-owned / municipal entities the prior framework parked under the generic Regional CLEC bucket. Carries the Phase 3 §6 D5 evidence rule that "mutual" / "co-op" / "CUD" / "municipal open-access" / "member-owned" diagnostic phrases route to the Co-op sub-segment.
- **2 D1 evictions**: Florida WiFi (2-employee IT services in Fort Lauderdale per existing brief, not a fiber operator) + Heritage Networks (heritagenetworks.us is the Michigan IT-outsourcing/cabling shop, NOT the Alaska fiber operator the prior brief described — wrong-entity bleed caught via web verification).
- **1 cross-company template bleed remediation**: Rye Telephone Company (CO) carried Highline (parent) news entries that conflated Rye-specific footprint with Highline's wider operations. Web verification confirmed Highline acquired Rye 2021-08 — Highline is the legitimate parent, but the brief / provisioning_landscape / geographic_focus needed rewriting to be Rye-specific.
- **2 territory / state corrections**: Highland Communication Services (state TN → IL — record is the City-of-Highland-IL municipal gig, not Highland Telephone Cooperative TN); ToledoTel (state OH → WA, owner Tim Lieto → Ken Cunningham — record is Toledo Washington family-owned LEC).
- **2 placeholder-brief fills via news context**: Franklin Telephone (MS BEAM grant) + ImOn Communications (Iowa cable→fiber transition Cedar Rapids / Fort Madison).
- **1 MaiaEdge value-prop bleed scrub**: Open Infra provisioning_landscape carried "creates greenfield opportunity for NaaS integration" — outreach-skill language inappropriately bled into an enrichment field. Rewritten to a neutral description.
- **~32 stale recent_news_or_trigger_event clears** per §7.4 rule (newest date prefix > 90 days old + no Signal Scan in last 7 days). Most rural fiber-co records had 2024-mid → 2025-mid news that has aged past the 90-day window.

## Pattern counters (cumulative through batch 43)

| Pattern | Δ batch 43 | Cum total |
|---|---:|---:|
| National operator under-tiering | 0 | ~45 |
| Within-fiber promotions | 16 (all to Municipal/Cooperative) | ~44 |
| Within-fiber demotions | 0 | ~25 |
| Template-bleed remediation | 4 (Rye Telephone bleed, Heritage Networks wrong-entity, ToledoTel state, Highland Comm state) | ~32 |
| Maritime/MSP misclassified as Telecom Aggregator | 0 | 6 |
| MaiaEdge value-prop bleed | 1 (Open Infra) | ~35 |
| CPaaS/voice aggregator misclassified as Fiber Op | 0 | 8 |
| Pure satellite operator misclassified as Fiber Op | 0 | 3 |
| Subsea cable operator promotions | 0 | 5 |
| IX/Internet Exchange policy gap | 0 | 3 |
| R&E network framework gap | 0 | 1 |
| AI Signals - colo reclassifications | 0 | 5 |
| Sanctions-driven ICP→Other reclasses | 0 | 2 |
| Crypto-to-AI Neocloud reclasses | 0 | 1 |
| Cable-manufacturer D1 evictions | 0 | 1 |
| Dedup/identity evictions | 0 | 6 |
| Defunct-brand evictions | 0 | 4 |
| Tower-co D1 evictions | 0 | 1 |
| Colo→Fiber Op within-class reclassifications | 0 | 2 |
| **NEW: Wrong-entity-at-domain D1 eviction** | 1 (Heritage Networks) | 1 |
| **NEW: IT-services D1 eviction** | 1 (Florida WiFi) | 1 |

## Per-record audit

### Evictions (customer_segment → Flagged for deletion)

#### Florida WiFi (297782865627)
- Path: FULL (eviction)
- Domain: florida-wifi.com
- Segment: Fiber Operator → **Flagged for deletion**
- Confidence: low_5069 → high_90
- Apollo used: no
- web_searches: 0 (existing brief already flagged "needs manual review")
- Reason: 2-employee IT services / Wi-Fi installer in Fort Lauderdale. Apollo industry IT Services. No fiber operator infrastructure. D1 disqualifier.

#### Heritage Networks (297777475270)
- Path: FULL (eviction)
- Domain: heritagenetworks.us
- Segment: Fiber Operator → **Flagged for deletion**
- Confidence: medium_7089 → high_90
- Apollo used: no
- web_searches: 1 (verified entity at domain)
- Reason: Domain belongs to Michigan IT outsourcing / cabling firm (founded 1997, Lapeer MI). Prior brief described the separate Alaska fiber operator — wrong-entity bleed. Domain entity is IT integrator, D1 disqualifier.

### Sub-segment promotions to Municipal / Cooperative - Fiber operator (tier_3 → tier_4)

All carry the same reason citation: file 06 §6.2 D5 cooperative / municipal evidence test.

| ID | Name | State | Note |
|---|---|---|---|
| 297740621553 | Jo-Carroll Energy (JCE Co-op) | IL | Electric cooperative + fiber division; brief rewritten for clarity |
| 297740621554 | Farmers Mutual Telephone | ID | "Mutual" = member co-op |
| 297740621555 | Casey Mutual Telephone | IA | Operating Adair Fiber brand; 5-county mutual co-op; brief filled with web-verified detail |
| 297742427851 | Oregon Farmers Mutual Telephone | MO | Note: Missouri not Oregon state; brief updated for clarity |
| 297770284741 | Maple Broadband | VT | Communications Union District (CUD) model |
| 297770284745 | Utopia Fiber | UT | Municipal open-access (11 member cities) |
| 297770284748 | Amherst Communications | WI | 1903-founded mutual co-op; brief filled |
| 297777475259 | DUO Broadband | KY | Member-owned cooperative (returned $25M capital credits) |
| 297777475260 | The Hamilton Telephone Company | NE | "Local cooperative" per brief |
| 297777475272 | Pineland Communications | GA | "Cooperative FTTH provider" per brief |
| 297777475285 | Rothsay Telephone | MN | Park Region co-op affiliate |
| 297782865625 | Valley Telecommunications | SD | Member-owned cooperative |
| 297858169568 | Highland Communication Services | IL (corrected from TN) | Municipal gig (City of Highland, IL); brief rewritten; state corrected |
| 297858169569 | Wabash Mutual Telephone | OH | Customer-owned cooperative |
| 297858169570 | Park Region Telephone | MN | 1906 cooperative |
| 297858169572 | Phynx | MO | Kingdom Telephone member-owned co-op |

### Territory / state corrections (no sub-segment change)

#### ToledoTel (297777475274)
- Path: MEDIUM
- state: Ohio → Washington (matches brief "Toledo, WA")
- hubspot_owner_id: 161889085 (Tim Lieto East) → 162339176 (Ken Cunningham West)
- Sub-segment unchanged: Regional CLEC (family-owned 1915 LEC, not a co-op)

### Template-bleed remediation (Regional CLEC stays)

#### Rye Telephone Company (297742427854)
- Path: MEDIUM
- account_brief / provisioning_landscape / geographic_focus all rewritten to be Rye-specific (was conflated with Highline parent's wider footprint)
- Highline is the legitimate parent (acquired Rye 2021-08) — not a bleed in the sense of wrong-entity, but the existing copy mis-attributed Highline's 6-state Michigan-centric activity to Rye's CO local footprint

### Placeholder-brief fills (Regional CLEC stays)

| ID | Name | Source for fill |
|---|---|---|
| 297777475269 | Franklin Telephone Company | News context already on record (MS BEAM $70.9M grant 2024-06) |
| 297782865628 | ImOn Communications | News context (2026-02 Fort Madison completion + 2026-01 Cedar Rapids fiber overbuild) |
| 297863568113 | Hamilton County Communications | web_search verified — subsidiary of Hamilton County Telephone Co-op (1953), Dahlgren IL |
| 297858169573 | Belmont Telephone Company | Brief minimally filled (small Lafayette County WI ILEC) |
| 297777475287 | Colton Telephone Company | Brief minimally filled (Dell Rapids SD small telco) |
| 297777475286 | Antietam Broadband | infrastructure_profile filled (Route Miles: Small <1K); undated news cleared |

### MaiaEdge value-prop bleed scrub (Regional CLEC stays)

#### Open Infra (297830612723)
- Path: MEDIUM
- provisioning_landscape: rewrote the trailing "US expansion creates greenfield opportunity for NaaS integration" — that's outreach copy, not enrichment fact

### LIGHT-path records (stale news clear + last_enriched_date bump, no other changes)

297742427852 LISCO · 297742427853 Tenino Telephone · 297742427855 Lakeland Communications · 297770284739 LTD Broadband/GigFire (tier_2 Long Haul) · 297770284740 ACE Fiber · 297770284749 Madison County Telephone · 297770284751 Seamless Fiber Innovations · 297777475258 mStreet Fiber (fresh signal kept) · 297777475261 Alaska Power & Telephone (already Municipal/Cooperative tier_4) · 297777475262 Reasnor Telephone · 297777475263 NKTelco · 297777475265 Smart Fiber Networks · 297777475267 Scranton Telephone · 297777475271 Ironton Telephone · 297777475273 Pine Cellular · 297830612722 Grafton Technologies · 297858169562 RTA Telecommunications of America (tier_2 Long Haul) · 297858169567 Sacred Wind Communications · 297858169571 Venture Communications Cooperative (already Municipal/Cooperative tier_4) · 297858169574 Grand Telephone · 297863568108 BARConnects · 297863568111 Mlgc · 297877949123 Inyo Networks

## Notable observations / data-quality flags for Cooper

1. **Co-op promotion volume is high** — 16 of 50 in this batch alone. Suggests batches 41-42 footprint (and possibly earlier) also under-routed mutual / member-owned telcos to Regional CLEC. May want to audit prior batches' Regional-CLEC writes for the same pattern. Recommend D7 takes a swing at any tier_3 Regional-CLEC records whose brief contains "mutual" or "member-owned" or "cooperative" or "CUD".
2. **Heritage Networks wrong-entity bleed** is concerning — the prior enrichment described the Alaska fiber operator while the actual domain belongs to a Michigan IT shop. Likely a name-collision miss during a prior R1/R2 run. May want to spot-check other "common name" records for the same issue.
3. **Rothsay Telephone (297777475285) and Park Region Telephone (297858169570) are likely a duplicate-or-affiliated pair** — Rothsay brief explicitly mentions "Park Region (parent)". Recommend R3 Duplicate Accounts sweeps these. Both promoted to Municipal/Cooperative in this batch; if R3 finds them dupe-pair, merge.
4. **Reasnor Telephone (297777475262)** — acquired by Integrated Path Communications 2024-08. Same dedup candidate for R3.
5. **MLGC (297863568111)** — domain `mlgc.com` and brief is thin. Worth a D7 deep-dive for Macomb-Lewis-Garner Communications context or similar.
6. **Florida WiFi domain `florida-wifi.com`** — flagged for deletion. Cooper's manual delete step in HubSpot will sever the record.

## Run health

**GREEN.** No HubSpot errors. No 429/5xx. No Apollo calls. No Slack DM failures. No customer-protection HOLDs (zero closed-won deal records in this batch). No `hs_is_target_account = true` tier-freeze records in this batch.

## Continuation

After this batch: 50 written → 659 remaining (~13 batches at BATCH_SIZE=50 to drain).
