# D1 — Global disqualifier rules

**Apply BEFORE sub-segment classification.** If any rule fires, set `customer_segment = "Other"` (or `"Unknown"` if uncertain) and skip sub-segment classification entirely. These rules protect the 6 ICP segments from contamination by lookalikes that fail the underlying ICP thesis (MaiaEdge sells carrier-grade programmable infrastructure to entities that operate or consume real network infrastructure at scale).

This list is the union of Phase 2.2's 13 hyperscaler/equipment-vendor evictions, file 05's exclusion gates, Phase B sub-agent findings, and the segment-classification SKILL's existing exclusion logic.

> **Mandatory companion write on any `Flagged for deletion` route.** Most D1 rules route to `customer_segment = "Other"` (legitimate-but-disqualified entities kept as competitive/partner references — these set NO `flagged_for_deletion_reason`). The subset that routes to `customer_segment = "Flagged for deletion"` (class 9 Defunct/inactive, and any D1 match with NO competitive/partner reference value) MUST set the companion `flagged_for_deletion_reason` in the SAME update, leading with one of the 7 canonical reason codes + a colon + one evidence sentence (no em dashes). For D1 routes use: `D1 disqualified (no reference value)` for a legitimate-but-disqualified entity with no reference value; `Hard junk / non-business` where the disqualifier is junk / non-business / spoofed-brand rather than a real entity; `Defunct / out of business` for defunct/retired-brand cases; `Dead domain` for expired/non-resolving domains. Full spec: `context/hubspot/property-schema.md` §2.1.

## Disqualifier classes (ordered by encounter frequency)

### 1. Hyperscalers and hyperscaler-equivalent platforms

| Disqualifier | Rationale | Action |
|---|---|---|
| Domain in {amazon.com, aws.amazon.com, microsoft.com, azure.microsoft.com, google.com, cloud.google.com, meta.com, oracle.com (cloud), tencent.com, alibaba.com, alibabacloud.com, yandex.cloud, baidu.com, ibm.com (cloud), digitalocean.com (parent — see exception below)} | MaiaEdge does not sell to the hyperscaler. They are the destination, not the buyer. | `customer_segment = "Other"`; null sub-segment; HubSpot note: "Hyperscaler exclusion per D1.1" |
| Self-describes as "hyperscale cloud" with own global region map (≥20 regions) AND own subsea cable ownership | Hyperscaler-equivalent regardless of brand recognition | Same |
| NVIDIA Lepton, NVIDIA-owned cloud properties | Hyperscaler-adjacent; partner list is signal, not target | `customer_segment = "Other"`; flag for partner channel |

**Exception:** DigitalOcean has been carved as `AI Infrastructure providers - Neocloud` per the NeoCloud Phase B+C deep-dive — they're mid-market cloud with GPU compute, not a hyperscaler. Keep DigitalOcean in NeoCloud unless it materially shifts its positioning.

### 2. Equipment vendors and silicon vendors

| Disqualifier | Examples | Action |
|---|---|---|
| Primary business is router/switch/optical equipment OEM | Cisco, Juniper, Nokia, Ericsson, ZTE, Huawei, Arista, Calix, Adtran, Ribbon, Mavenir, Ciena, Infinera | `customer_segment = "Other"` |
| Primary business is silicon | Intel, AMD, NVIDIA (chip side), Broadcom, Marvell, Qualcomm, MediaTek | `customer_segment = "Other"` |
| Primary business is system integration WITH a captive equipment line | Used to be partner candidates; structurally not network operators | `customer_segment = "Other"`; flag for partner channel |

Verification: company website primary navigation is "Products" not "Services"; "buy" or "request a quote" lands on hardware SKUs.

### 3. OTT and pure content platforms

| Disqualifier | Examples | Rationale |
|---|---|---|
| Streaming media OTT | Netflix, Hulu, Roku, Disney+, Paramount+, Max | They consume hyperscaler/CDN bandwidth; they don't operate carrier networks |
| Social media platforms | Meta apps (Facebook, Instagram, WhatsApp), TikTok/ByteDance, Reddit, Discord, Pinterest, Snap, X | Same |
| Gaming networks | Valve/Steam, Epic Games, Sony PSN (the gaming arm), Microsoft Xbox Live | Same |
| Music streaming | Spotify, Apple Music, Tidal | Same |

**Carve-out:** Disney+, Netflix, etc., may operate edge CDN PoPs. If they have a dedicated network-engineering org that procures carrier infrastructure independent of Akamai/Cloudflare/Fastly, classify as Enterprise (Outsourcing Services or Other). Default: `Other`.

### 4. Submarine cable consortia (pure)

| Disqualifier | Examples | Rationale | Action |
|---|---|---|---|
| Multi-operator subsea cable consortium with no operating entity beyond cable maintenance | FLAG, SEA-ME-WE 4/5/6, ACE, EIG, MAREA (the cable, not Meta's role) | Not a sellable entity; consortium members are the buyers | `customer_segment = "Other"` + HubSpot note: "Subsea consortium per D1.4" |
| Pure-play subsea cable operator with NO terrestrial backbone | Aqua Comms (pre-EXA), Seaborn Networks, BW Digital, hyperscaler subsea SPVs (Anjana, Cap-1, etc.) | Different sales motion than International Backbone Specialist | **Cooper decision pending** — recommend `customer_segment = "Other"` with new `subsea_cable_operator` flag, OR carve a new sub-segment under Network Op for these. Default: `manual_review_required` flag until decision. |

### 5. Pure software / SaaS without network ops

| Disqualifier | Examples | Action |
|---|---|---|
| Pure cloud MSP with NO network services (no SD-WAN, no managed circuits, no security service edge) | A "cloud-only" CRN MSP501 entry; AWS migration shops with no carrier line; Mission Cloud (pre-CDW) | `customer_segment = "Other"`; flag |
| IoT/eSIM connectivity platform | Aeris, EMnify, Wireless Logic, KORE, Soracom | `customer_segment = "Other"`; new sub-segment "IoT Connectivity Platform" recommended to Cooper (currently out of scope) |
| Pure-play observability / network monitoring SaaS | Datadog (cloud monitoring side), New Relic, Kentik, ThousandEyes (Cisco-owned) | `customer_segment = "Other"` |
| Pure-play security platform | Palo Alto Networks, Fortinet, CrowdStrike, Zscaler (parent), Cato Networks (SASE-only side) | `customer_segment = "Other"` |

**Carve-outs:**
- ThousandEyes, Kentik = potentially relevant partner/integration targets, not customers.
- Cato Networks: if they sell carrier connectivity via managed service, may qualify as Managed Network Services - MSP. Default: `manual_review_required`.

### 6. Logistics / shipping / transportation tagged as telecom

| Disqualifier | Examples | Action |
|---|---|---|
| Maritime/freight/logistics company misclassified in CRM as telecom | Gulf Agency Co (GAC), Maersk, DHL parent, FedEx parent | `customer_segment = "Other"` + flag revenue for cleanup (file 05's NaviSite/GAC suspect revenue follow-up) |
| 3PL / warehouse operator without multi-DC corporate IT | XPO, GXO, J.B. Hunt, C.H. Robinson | Watch List, not Enterprise ICP (per Enterprise Watch List policy) |

### 7. Government / military / embassy networks

| Disqualifier | Domain pattern / signal | Rationale | Action |
|---|---|---|---|
| US federal civilian agency | `.gov`, `.fed.us` | FedRAMP gate not yet achieved; out of scope | `customer_segment = "Other"` until FedRAMP authorization |
| US military | `.mil`, `army.mil`, `navy.mil`, etc. | Same | Same |
| Embassy / diplomatic mission | embassy.org, foreign-affairs ministry domains | Same | Same |
| State/local government | State government domains (e.g., `state.tx.us`), city/county sites | Long procurement cycles; not current focus | `customer_segment = "Other"`; flag for future-expansion review |
| Foreign government national-cloud entity | Saudi DataX (government-owned), UAE DataVolt (sovereign-affiliated) | Sovereign AI carve-out applies ONLY if they sell to enterprises with sovereign requirements — government-owned operating as commercial entity may qualify under NeoCloud Sovereign AI | Default: `manual_review_required`. Cooper decision. |

### 8. Academic / research / non-profit

| Disqualifier | Examples | Action |
|---|---|---|
| University research and education networks | Internet2, JANET, GÉANT, ESnet, NORDUnet | `customer_segment = "Other"`; out of scope as commercial buyer |
| Pure research consortia | Caltech, MIT, Stanford institutional IT | Same |
| Public broadcasting | PBS, BBC IT side | Same |

### 9. Defunct / inactive entities

> **Companion write:** Any `customer_segment = "Flagged for deletion"` action below MUST set `flagged_for_deletion_reason` in the same HubSpot update — `Defunct / out of business` for bankruptcy / retired-brand cases, `Dead domain` for the expired/non-resolving-domain row. See `context/hubspot/property-schema.md` §2.1 for the 7-code spec.

| Disqualifier | Examples | Action |
|---|---|---|
| Company in active bankruptcy with no operations | GTT pre-emergence (now operational), Velocity Communications | `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason` leading `Defunct / out of business` (cite the bankruptcy/cease-ops event); trigger R4 pre-deletion-audit |
| Brand retired post-acquisition with no successor entity | Wave (absorbed into Astound 2022), original PlanetOne (absorbed into AVANT 2022), MicroCorp (absorbed into AppDirect 2020) | `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason` leading `Defunct / out of business` (cite the acquirer + year); reassociate contacts to acquirer per R4 |
| Domain expired or website non-resolving 90+ days | Any | `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason` leading `Dead domain` (cite NXDOMAIN / parked / persistent 4xx-5xx; a proxy block does NOT count) |

### 10. Misclassified data center adjacencies

| Disqualifier | Examples | Action |
|---|---|---|
| Power infrastructure provider (utility, IPP) with NO colo build-out | NextEra Energy, Duke Energy, Constellation, AEP | `customer_segment = "Other"` |
| Cooling/HVAC vendor | Vertiv (parent), Schneider Electric, Stulz | `customer_segment = "Other"` |
| Real estate parent that LEASES to colos but doesn't operate them | Prologis, Mapletree, GIC real estate arm | `customer_segment = "Other"`; verify (Mapletree currently miscategorized per Phase 2 audit) |
| Crypto exchange / pure mining without GPU pivot | Coinbase (the exchange), Marathon Digital (still pure BTC mining), Riot Platforms (still pure BTC mining) | `customer_segment = "Other"`; revisit if GPU pivot announced |

---

## Implementation guidance

### Pre-classification check order

1. **Domain check** — match against hyperscaler / government / academic domain patterns. If match → disqualify.
2. **NAICS / industry check** — if equipment vendor (NAICS 3342, 3344), shipping/logistics (NAICS 4811-4884), or OTT (NAICS 519130), disqualify.
3. **Website primary navigation check** — if "Products" with hardware SKUs (not "Services" / "Solutions"), disqualify as equipment vendor.
4. **Activity/lifecycle check** — domain non-resolving 90+ days OR active bankruptcy with no operations OR brand retired post-acquisition → `Flagged for deletion`.
5. **Special case lookups** — Pure subsea cable operators, IoT platforms, foreign sovereign-affiliated → `manual_review_required` and pause for human decision.

### When a disqualifier conflicts with an existing customer

**Halt.** If a disqualifier rule would evict a record that is currently `type = "Customer"` or has any associated deal past `closedwon`, halt the disqualifier action and flag for Cooper review. The customer relationship overrides classification cleanup. Document in audit log: "Disqualifier suppressed due to active customer relationship."

### Encoding in skills

- `segment-classification/SKILL.md`: Add a "Step 0: Global disqualifier check" pre-routing block that runs before any segment routing logic.
- `company-enrichment/SKILL.md`: Same — runs at Stage 1.5 before sub-segment assignment.
- `edge-case-researcher/SKILL.md`: Add disqualifier validation as a positive output ("Confirmed disqualifier: hyperscaler") not just a fallback.
- `import-processor/SKILL.md`: Add a pre-import disqualifier filter so HubSpot doesn't ingest known disqualified entities.

### Audit format for any disqualifier eviction

```
Phase 2.X / R1 / R2 / R0 Disqualifier eviction on YYYY-MM-DD by <routine>

Action: customer_segment <old> → "Other" (or "Flagged for deletion")
Field: customer_segment, company_sub_segment (cleared)
   [If → "Flagged for deletion": also set flagged_for_deletion_reason = "<canonical code>: <evidence sentence>" in the same update — see property-schema §2.1]
Disqualifier matched: D1.<class>.<rule>
Evidence: <specific signal that triggered>
Reason: <human-readable summary>
```
