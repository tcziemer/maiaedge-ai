# Mass Re-Enrichment Sweep — Batch 33

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Batch date:** 2026-05-19
- **Batch size:** 50 / 50 processed
- **Pool remaining before batch:** 1,195
- **Pool remaining after batch:** ~1,145 (-50)
- **Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled, Apollo-free path)
- **Path mix:** LIGHT 38 · MEDIUM 12 · FULL 0 · HOLD 0
- **HubSpot writes:** 50 succeeded, 0 failed (6 batches: 10+2+10+10+10+8)
- **HOLD policy:** NONE (per Cooper continuation note — every record qualified, reclassified, or evicted)

---

## Path summary

### MEDIUM (patches) — 12 records

| Company | ID | Path reason | Segment change | Sub-segment change | Tier change |
|---|---|---|---|---|---|
| TM Global | 297982584526 | Brief regen (sovereign-GPU bleed); infra_profile = subsea wholesale 50K+ km | none | Regional CLEC → Tier 2 National Wholesale - Fiber operator | tier_3 → tier_2 |
| SK Group | 303374043854 | Chaebol holding parent (chemicals industry); SK Telecom is separate subsidiary | Fiber Operator → Other | cleared | tier_3 → tier_5 |
| NTT DOCOMO | 303421493962 | Japan Tier 1 mobile carrier 91M subs — under-tiered + wrong parent segment | Fiber Operator → Network Operator(Tier 1 / VNO) | Regional CLEC → Tier 1 Carrier - Network Op | tier_3 → tier_1 |
| Crown Castle | 303890867935 | Sold fiber business to Zayo + small cells to EQT-Arium May 1 2026; now pure-play tower co | Fiber Operator → Other | cleared | tier_3 → tier_5 |
| Cassava Technologies | 303370433234 | Holding co of Liquid (operating arm); D2 wholesale-arm policy | Fiber Operator → Other | cleared | tier_3 → tier_5 |
| MTS | 296883684033 | Russia carrier — sanctions block ICP-actionable | Fiber Operator → Other | cleared | tier_3 → tier_5 |
| Deltaland | 297987983097 | Sledge Telephone MS local exchange — not long-haul; within-Fiber demotion | none | Long Haul / Backbone → Municipal / Cooperative | tier_2 → tier_4 |
| Hargray Communications | 297777475264 | Regional fiber/cable SC/GA/FL/AL Cable One subsidiary — not long-haul; within-Fiber demotion | none | Long Haul / Backbone → Regional CLEC | tier_2 → tier_3 |
| Liquid Intelligent Technologies | 303379447543 | 110K+ km fiber across 20+ African countries — under-tiered national wholesale | none | Regional CLEC → Tier 2 National Wholesale - Fiber operator | tier_3 → tier_2 |
| Roggen Telephone Cooperative | 297984383730 | Template bleed ("research needed"); brief + provisioning_landscape regen | none | none | none |
| West Texas Rural Telephone Cooperative | 298002235104 | Template bleed; brief + provisioning_landscape regen | none | none | none |
| SiFi Networks | 291518043894 | Template bleed; brief + provisioning_landscape regen | none | none | none |

### LIGHT — 38 records (date bump only, framework-consistent)

Sandhill Telephone Cooperative (297984383716) · Federated Rural Electric & Broadband (297987983094) · Egyptian Telephone Cooperative Association (297984383718) · Jefferson PUD (298002235098) · Neutrona Networks/Zayo (298002235106) · NRTC Communications (303489018595) · Altitude Infra (303907044057) · Verveba Telecom (315121276661) · Benton PUD (297164273392) · City of Elberton (297293654758) · AeroNet Wireless (268005442284) · Lingo Networks (297858169564) · PSSI Global Services (297940265681) · Global Compute Infrastructure (266981418733) · Clear Rate Communications (266866495175) · Citizens Mutual Telephone / CM Tech (297940265686) · Arkwest Communications (297969950433) · Esvba (297171485398) · Rice Belt Telephone (297934868202) · Fusion Connect (298009434832) · Socket (320811765451) · Palmerton Telephone (297770284743) · Atnorth (267092339390) · Comcell (297777475266) · United Communications (297293654766) · Blanca Networks (297944750830) · PRTC (316154217170) · ATCDC/Ashland Technology Complex (267965469412) · Ada Infrastructure (300467292890) · Bloomer Telephone (297918677705) · Salsgiver (297936668401) · Bloomingdale Communications (297936668400) · Cherokee Communications (296850118387) · Hospers Telephone (297293654761) · Fort Mojave Telecommunications (297782865622) · Edgestone (267140130522) · Bug Tussel (297877949121) · eLink Corp (267924003573)

---

## Pattern observations (cumulative running tallies)

| Pattern | This batch | Cumulative |
|---|---|---|
| National operator under-tiering (Tier 1 carrier misclassified down) | 2 (NTT DOCOMO promote to T1; Liquid promote to T2) | ~33 |
| Within-Fiber demotions (Long Haul → Regional CLEC or Muni/Coop) | 2 (Deltaland LH→Muni; Hargray LH→Regional CLEC) | ~21 |
| Template-bleed remediation (account_brief "research needed") | 3 (Roggen, WTRT, SiFi) | ~25 |
| Maritime-vertical MSP misclassified as Telecom Aggregator | 0 | 6 |
| MaiaEdge value-prop bleed in provisioning_landscape | 0 explicit in batch (no records had "MaiaEdge angle:") | ~31 |
| Segment misclassification (NeoCloud as Fiber) | 0 (TM Global brief mentioned sovereign-GPU but infra_profile confirms Fiber) | 1 (Syntys carry) |
| Segment misclassification (MSP/CPaaS as Fiber) | 0 | 1 (Voyant carry) |
| **NEW: Chaebol/holding-co parents misclassified as carrier** | 2 (SK Group, Cassava) | 2 |
| **NEW: Exited-fiber-market reclassification** | 1 (Crown Castle post-Zayo divestiture May 2026) | 1 |
| **NEW: Sanctioned-country carrier reclassification** | 1 (MTS Russia → Other) | 1 |

---

## Carry-forward watch list (carried into batch 34)

- **Subsea cable operator candidates:** Aqua Comms, Seaborn Networks, Hawaiki, Telxius, PLDC (none in this batch)
- **Greenfield colo candidates:** Beacon Data Centers + Series A-C funded with construction stage (0 hits this batch)
- **National-operator under-tiering grep:** `customer_segment="Fiber Operator" AND numberofemployees > 1000 AND annualrevenue > 500000000`
- **Template-bleed grep:** `account_brief CONTAINS "research needed"`
- **Value-prop bleed grep:** `provisioning_landscape CONTAINS "MaiaEdge angle:"`
- **NeoCloud-mis-Fiber grep:** `customer_segment="Fiber Operator" AND (account_brief CONTAINS "sovereign AI" OR "NeoCloud" OR "NVIDIA Cloud Partner" OR "GPU cloud" OR "Hopper" OR "Blackwell")`
- **MSP-CPaaS-mis-Fiber grep:** `customer_segment="Fiber Operator" AND (account_brief CONTAINS "UCaaS" OR "CPaaS" OR "SIP Trunking" OR "SMS API")`

## Data-quality follow-ups added this batch

- **SK Group / SK Telecom duplicate-pair?** SK Group at sk.com (chaebol parent) reclassified to Other. Confirm no separate SK Telecom ICP record exists at sktelecom.com — if missing, account-sourcing should add it. If present, this batch's reclassification is correct.
- **Cassava / Liquid duplicate-pair confirmed.** Cassava (holding) → Other, Liquid (operating arm) promoted to T2 National Wholesale. Per D2 wholesale-arm policy.
- **NTT DOCOMO numberofemployees=1000 looks understated** for a 91M-subscriber carrier (~8K employees actual). Apollo refresh recommended on next R2 pass.
- **MTS sanctions** — Tim Z owns the record (hubspot_owner_id 159350430). Cooper may want to mass-Flag for deletion any other Russia-domiciled carriers in CRM via separate sweep.

## Sweep drain projection

- Pool before batch 33: 1,195
- Pool after batch 33: ~1,145
- Records processed in this sweep cumulative: 1,650 (32 prior × ~50 + 50 this batch)
- ETA to completion at BATCH_SIZE=50: ~23 more batches
- Apollo cumulative: 0 (sweep is APOLLO_ENFORCEMENT=disabled and using Apollo-free paths throughout)

## Run health: GREEN
- 50/50 writes succeeded
- 0 HubSpot errors
- 0 Tier 3 holds (HOLD policy = NONE per Cooper)
- 0 customer-protection HOLDs fired
- 0 framework-reference file modifications detected mid-run
