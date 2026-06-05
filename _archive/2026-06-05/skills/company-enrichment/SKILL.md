---
name: company-enrichment
description: "MaiaEdge company enrichment and classification bot. Research companies, classify into customer segments (Colocation, Fiber Operator, Network Operator, MSP/Aggregator, Neocloud), score/tier, and write enriched records directly to HubSpot via MCP. Use when asked to enrich companies, research accounts, run enrichment pipeline, classify companies for MaiaEdge, or segment analysis. Uses a website-first adaptive research strategy (6-8 focused calls per company). Input: company names or domains. Primary output: HubSpot company-record writes via MCP (all enrichment fields populated, `last_enriched_date` stamped). Secondary output: excludes log for audit trail. Handles deduplication, domain discovery, deep investigation, edge case flagging, and HubSpot property mapping. Falls back to XLSX only when the user explicitly asks for a file."
---

# MaiaEdge Account Enrichment Bot

## Skill Name: `maiaedge-enrichment-bot`
## Call Action: Use when asked to "enrich companies", "research accounts", "run enrichment", or "classify companies for MaiaEdge"

## Purpose
Research companies, classify into MaiaEdge customer segments, score/tier, and write enriched records directly to HubSpot via the HubSpot MCP. Uses a website-first, adaptive search strategy that averages 6-8 focused calls per company to produce accurate, auditable results.

**Primary delivery: HubSpot MCP (direct property writes).** For each qualified company, write every enrichment field (`customer_segment`, `company_sub_segment`, `account_tier`, `segmentation_confidence`, `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`, `account_brief`, `maiaedge_value_proposition`, `last_enriched_date`) to the company record via MCP. Do not produce an XLSX unless the user explicitly asks for one.

**Secondary outputs:**
- **Excludes Log** — Record-count summary + per-record exclusion reason delivered inline to the user (and optionally as a file). Audit trail.
- **XLSX file** — ONLY when the user asks ("give me a file", "export to spreadsheet", "prepare for manual import"). Not the default path.

**Skill 2 (Import Processor) is NOT needed when this skill runs.** Import-processor is retained for the rare case of transforming a legacy CSV/XLSX enrichment file into HubSpot-compatible shape — current Claude-driven enrichment writes directly to HubSpot via MCP and skips that step entirely.

---

## Input

**Only `company_name` is truly required.** Everything else is discovered through research.

A list of companies with:
- `company_name` (REQUIRED  -  the only mandatory field)
- `company_domain` (optional  -  if not provided, Step 0 discovers it)

The input may be a CSV, XLSX, or just a list of company names. Do not assume any other fields exist. Treat every data point as something to be researched and verified, even if the input includes partial data like state or segment  -  verify it independently.

---

## STEP 0: Domain Discovery & Dedup Check

### 0A: HubSpot Deduplication Check (recommended)

Before enriching, check if the company already exists in HubSpot to avoid wasting research effort and overwriting existing data:

1. If HubSpot MCP tools are available, search by `company_domain` (or `company_name` if no domain) using `search_crm_objects`
2. If a match is found with `customer_segment` already populated:
   - **Skip enrichment** for this company  -  it's already been processed
   - Log it: `"SKIPPED  -  already in HubSpot as [segment], enriched [date]"`
3. If a match is found but `customer_segment` is empty:
   - **Proceed with enrichment**  -  the company exists but hasn't been classified yet
4. If no match → proceed with enrichment as normal

Report dedup results before starting research: "Found X of Y companies already in HubSpot  -  skipping those, enriching Z net-new companies."

If HubSpot tools are unavailable, skip this step and proceed. Note: "HubSpot dedup check unavailable  -  processing all companies."

### 0B: Domain Discovery (only when domain is missing)

**Skip this step entirely if `company_domain` is provided.**

When a company has no domain:

1. `web_search` for `[company_name] official website`
   - Look for the company's actual website in search results
   - Prefer .com, .net, .io domains over social media profiles or directory listings
   - Watch for disambiguation  -  "Summit" could be 50 companies. Use any context clues from the input (state, industry, etc.)

2. If the search returns a clear match → set `company_domain` and proceed to Stage 1
3. If ambiguous (multiple companies with same name) → try `[company_name] [any available context like state or industry] telecom fiber data center`
4. If still no match → flag `needs_manual_review = TRUE` with note "Could not determine company domain" and skip to excludes log

**Cost: 1-2 additional searches per domain-less company.**

### 0C: Re-Enrichment Mode

When triggered by CRM Guardian or manually for re-enrichment of existing accounts:

**Trigger criteria:** Company has `last_enriched_date` that is **120+ days ago**, OR `last_enriched_date` is blank while `customer_segment` is populated (classified but never formally enriched).

**Difference from new enrichment:**
- Skip Step 0A dedup check  -  company already exists in HubSpot
- Skip Step 0B domain discovery  -  domain is already known
- Go directly to Stage 1 with the existing domain

**Full overwrite behavior:** Re-enrichment overwrites ALL enrichment fields with fresh data. Apollo is the authoritative source for the firmographic identity block (state / country / owner / LinkedIn / domain); when Apollo returns a non-empty value that differs from HubSpot, overwrite per the table below:

| Field | Overwrite behavior on re-enrichment |
|-------|-------------------------------------|
| `customer_segment`, `company_sub_segment`, `account_tier`, `segmentation_confidence` | Overwrite from fresh classification (subject to CRM Guardian safety tiers on deal-protected accounts) |
| `state` | **Overwrite** from Apollo `primary_location.state` when present. Apollo wins over stale HubSpot (companies relocate HQs; M&A shifts HQ) |
| `country` | **Overwrite** from Apollo `primary_location.country`. Non-US rewrites trigger owner cascade to Tim Ziemer |
| `hubspot_owner_id` | **Re-derive** from refreshed `state` / `country` per territory-model.md. Cascade to contacts |
| `linkedin_company_page` | **Overwrite** from Apollo `linkedin_url` when Apollo returns non-empty value differing from HubSpot. Companies change handles after rebrands / M&A |
| `domain` | **Conditional overwrite** — if HubSpot `domain` is blank OR Apollo's primary domain differs AND the HubSpot value no longer resolves (dead DNS / redirect to a new domain), write Apollo's domain. If both HubSpot and Apollo have live-but-different domains, flag as Tier 2 (applied + flagged to Cooper) rather than Tier 1 — this is a rebrand signal worth reviewing |
| `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus` | Overwrite from fresh research |
| `hyperscaler_proximity`, `key_tenant_segments__cloned_` | Overwrite from fresh research |
| `account_brief`, `provisioning_landscape`, `maiaedge_value_proposition` | Overwrite from fresh research |
| `recent_news_or_trigger_event` | Overwrite with the highest-scored signal if a fresh signal fired; otherwise leave existing |
| `last_enriched_date` | **Always write** → today's ET date. This is the idempotency key for the 120-day rotation |

**Do NOT overwrite on re-enrichment:** `lifecyclestage`, `hs_lead_status`, `type`, `hs_is_target_account`  -  these may have been updated by sales activity since initial import. Also never overwrite: custom notes, MEDDPICC fields on deals, any field owned by the sales team.

**Research approach:** Same Phase 1/2/3 as new enrichment. Website-first adaptive research, segment-specific deep dive, qualification gates. No shortcuts  -  treat it as a fresh enrichment with the advantage of already knowing the domain.

**What to watch for on re-enrichment:**
- Company may have changed segment (e.g., colo operator that pivoted to neocloud, fiber op acquired by larger carrier). If segment changes, trigger full cascade: re-derive sub-segment, tier, confidence, infrastructure_profile. Sync updated `customer_segment` to all associated contacts.
- AI infrastructure signals may be new since last enrichment (standard colo → AI colo sub-segment upgrade)
- Leadership changes or acquisitions since last enrichment → update `recent_news_or_trigger_event`
- Trigger events that upgrade tier (expansion, funding → Tier 1 if HIGH confidence)
- Company may have been acquired or gone defunct → if so, flag for review rather than overwriting

**When running under CRM Guardian:** The Guardian's safety tier system and deal protection rule apply. See crm-guardian skill for the authoritative tier definitions. In short: if an account has an open deal and re-enrichment would change `customer_segment` or `account_tier`, those fields are flagged for review rather than auto-written. All other field updates proceed normally.

---

## STAGE 1: Adaptive Deep Investigation

### Design Philosophy
Every search must earn its place — read the company's website first, then only search for what the website didn't answer. Three phases:
1. **Phase 1**: Read the company's actual website  -  this alone answers ~50% of research questions
2. **Phase 2**: Run ONLY the searches needed based on what Phase 1 revealed (segment-specific)
3. **Phase 3**: Fill gaps, verify exclusions, and resolve edge cases

If the website already answered a question, don't search for it again.

---

### PHASE 1: Website + Identity + Apollo (3-4 calls)

**Step 1: Apollo Organization Enrichment (MCP)**

Call `apollo_organizations_enrich` with the company's domain. This is the authoritative source for HQ location and firmographic data.

Extract from Apollo response:
- **HQ state** → `state` (2-letter abbreviation). This is the primary source for territory routing.
- **HQ country** → `country`. If non-US, account routes to Tim Ziemer (International).
- **Employee count**  -  useful for qualification gates (under 7 employees = exclude).
- **Industry**  -  secondary signal for segment routing.
- **Revenue**  -  context for tier assignment.
- **Founded year**  -  context for maturity.

> Apollo enrichment consumes credits. One call per company. Do not call Apollo for companies already flagged for exclusion in Step 0A.

**Step 2: `web_fetch` on `https://[company_domain]`**
Extract: description/tagline, nav menu items, infrastructure language (fiber/DC/colo/network), customer types (residential/enterprise/wholesale/carrier), portal/platform mentions, AI/GPU language, geographic clues, customer logos.

**Step 3: `web_fetch` on services/solutions page** (if linked from homepage)
Look for: specific products, wholesale vs. retail divisions, dark fiber/lit/wavelength offerings, colo/interconnection services, self-service portal or API, NaaS badges (Megaport, PacketFabric, Equinix, etc.)

**Step 4: `web_search` for `[company_name] company overview`**  -  ONLY if website was thin/down/uninformative.

**Derive `hubspot_owner_id` from Apollo's HQ state** using the territory map in property-schema.md:
- East states → Tim Lieto (`161889085`)
- West states → Ken Cunningham (`162339176`)
- Non-US → Tim Ziemer (`159350430`)
- State unknown after running the full Field Resolution Ladder below → leave blank for manual routing

### Field Resolution Ladder (state / country / contact email / phone)

When Apollo returns null, an empty string, or "unknown" on any of `state`, `country`, `phone`, or contact email, do NOT immediately flag for manual research. Run this ladder in order and stop at the first step that yields a HIGH or MEDIUM confidence value. This is the canonical fallback used by all CRM Guardian routines.

| Step | Source | Confidence | Cost | When to use |
|------|--------|------------|------|-------------|
| 1 | `apollo_organizations_enrich` (or `apollo_people_match` for contacts) | HIGH | 1 Apollo credit | Always first |
| 2 | `web_fetch` on `https://[domain]` — read footer, About page, Contact page | HIGH | 1-3 web_fetch calls | If Apollo null on the field |
| 3 | `web_fetch` on `https://www.linkedin.com/company/[slug]/about` — Headquarters block | MEDIUM | 1 web_fetch | If website doesn't disclose location/contact |
| 4 | `web_search` `"[domain] WHOIS registrant address"` → registrant city/state | LOW | 1 web_search | Last resort before Tier 3 hold |

**Confidence handling:**
- HIGH from step 1 or 2 → write the field at Tier 1 (or per the calling routine's safety tier rules).
- MEDIUM from step 3 → write at Tier 2 (applied + flagged) so Cooper can sanity-check.
- LOW from step 4 → write at Tier 3 (held). Surface in the routine report with the source so Cooper can confirm.
- All 4 steps null → Tier 3 hold. Now it's truly "manual research needed."

**Implementation notes:**
- The ladder always runs in order; do not skip step 2 to "save fetches" — the website is HIGH confidence and free of Apollo credit cost.
- For contact records (Routine 8 persona fill), step 1 is `apollo_people_match` and step 3 fetches the contact's individual LinkedIn profile (not the company about page).
- WHOIS step (step 4) is intentionally last because GDPR-redacted WHOIS responses are common; it's a low-yield step that's only worth running when the first three all fail.
- Slack DM reports MUST include the source attribution (e.g., "state filled via website footer" or "via LinkedIn About") so Cooper can audit ladder usage and tune the ordering if any step turns out to be unreliable.

**PHASE 1 CHECKPOINT: Route the company.**

| Website signals | Likely classification | → Phase 2 route |
|---|---|---|
| Data center, colocation, cross-connect, rack space, power | **Colocation Operator** | → Colo research |
| Fiber, route miles, network, transport, wavelength, lit buildings | **Fiber Operator** | → Fiber research |
| National backbone, Tier 1/2, global network, massive scale | **Network Operator** | → Network Op research |
| Aggregator, multi-carrier, no owned infrastructure | **MSP/Aggregator** | → MSP research |
| IS a GPU cloud provider (Lambda, Crusoe, Together.ai, RunPod, Modal, Applied Digital, Hut 8, etc.) | **Neocloud** | → Neocloud research |
| Staffing, software, consulting, manufacturing, construction | **Likely exclude** | → Exclude verification |
| Residential broadband, ISP, "sign up for internet" | **Likely Retail ISP** | → ISP verification (check for wholesale) |
| Website down, parked domain, or completely unrelated | **Insufficient data** | → Broad search fallback |
| Can't determine from website alone | **Ambiguous** | → Broad search fallback |

---

## STAGE 2: Segment-Specific Deep Dive

Each segment has its own research pathway based on Phase 1 routing. Run ONLY the searches relevant to the routed segment. Every search must earn its place.

### Colocation Operators

1. **Facility search:** `[Company] data center facilities locations`  -  Extract facility count, geographic spread, and major markets. → `infrastructure_profile` (Facilities bucket)
2. **AI signal check (MANDATORY for all colos):** `[Company] Lambda Labs Crusoe GPU liquid cooling AI-ready`  -  Look for: confirmed GPU cloud tenants, liquid cooling infrastructure, 30kW+ rack density, "AI-ready" marketing. If strong AI signals found → `company_sub_segment` = `AI Infrastructure`. If none → `Standard`.
3. **NaaS presence:** Check the company website for Megaport, PacketFabric, Equinix Fabric, or Console Connect badges/partnerships. → `fabric_provisioning_approach`
4. **Hyperscaler proximity:** `[Company] AWS Azure Google Cloud data center nearby`  -  Check if company facilities are near announced or existing hyperscaler regions. → `hyperscaler_proximity` (`Announced: <50 miles` is a strong Tier 1 trigger)
5. **Tenant types:** From website and search results, identify what types of tenants they serve. → `key_tenant_segments__cloned_` (cloud_providers, enterprises, carriers, content__hyperscale, financial_services, other). Semicolon-separated.
6. **Sub-segment assignment:** Standard (no AI signals) or AI Infrastructure (confirmed GPU tenants or liquid cooling).

### Fiber Operators

1. **Infrastructure search:** `[Company] fiber route miles network states lit buildings`  -  Extract route miles, lit building count, geographic footprint. → `infrastructure_profile` (Route Miles bucket), `geographic_focus`
2. **NaaS competitive signals:** `[Company] Megaport PacketFabric NaaS`  -  Are they already using a third-party fabric? → `fabric_provisioning_approach`
3. **Wholesale vs retail:** Confirm they sell wholesale/enterprise connectivity, not just residential broadband. Residential-only = exclude.
4. **Carrier partners and interconnection:** Look for NNI partners, peering relationships, carrier-neutral facilities.
5. **Sub-segment classification:**
   - Regional CLEC: Licensed carrier, <5 states, metro/regional footprint
   - Long-Haul / Backbone: Multi-state fiber, 10K+ route miles
   - Dark Fiber Specialist: Primarily dark fiber/wavelength sales

### Network Operators

1. **Automation check (determines messaging track):** `[Company] customer portal API self-service provisioning`  -  Look for evidence of branded portals, API access, self-service provisioning tools.
   - **Track A (External Extension):** Has internal automation, portal, API. The gap is cross-carrier, not internal.
   - **Track B (Internal + External Unification):** No evidence of portal/API automation. Fragmented internally.
2. **Scale verification:** Confirm 50+ PoPs, national/global footprint, 2K+ employees. Under these thresholds → may be a fiber operator or MSP instead.
3. **Branded products:** Look for named connectivity products, enterprise services, wholesale offerings.
4. **Sub-segment assignment:** External Extension (Track A) or Internal + External Unification (Track B).

### MSP / Aggregators

1. **Carrier aggregation check:** `[Company] managed services carrier aggregation multi-carrier`  -  Identify upstream carrier partners. Confirm they aggregate circuits from multiple carriers.
2. **IT MSP Test (MANDATORY):** Apply this test to avoid misclassifying IT MSPs:
   - Does the website mention carrier names (AT&T, Lumen, Comcast)? → Telecom signal
   - Does it list MPLS, WAN, SD-WAN, DIA services? → Telecom signal
   - Does it list helpdesk, endpoint management, cybersecurity? → IT MSP signal (EXCLUDE)
   - Does "managed services" mean managing carriers or managing IT endpoints?
3. **Asset-light verification:** Confirm <10% owned infrastructure. If they own significant fiber or facilities → may be a fiber operator or colo instead.
4. **Sub-segment classification:**
   - Telecom Aggregator: Aggregates carrier circuits, wholesale connectivity
   - Managed Network Services: Managed WAN/MPLS, service-oriented

### Neoclouds

1. **GPU infrastructure ownership (MANDATORY):** `[Company] GPU cloud infrastructure facilities data center`  -  Confirm they OWN or have committed funding to build physical GPU hardware in physical facilities. "AI cloud" marketing alone is NOT sufficient. If they're reselling cloud GPU from AWS/Azure/GCP without owning hardware → EXCLUDE (Cloud GPU Reseller).
2. **Expansion and funding:** `[Company] expansion funding 2025 2026`  -  Growth signals, new facility announcements, funding rounds. Strong Tier 1 triggers.
3. **Scale and capacity:** Facility count, total compute capacity (MW, GPU count), geographic distribution.
4. **Datum partnership check:** If the company appears in Datum.net's network or customer base, note for channel routing. Datum is a channel partner (Layer 7: proxy, anycast, DDoS). MaiaEdge solves Layer 2/3. Do not position as competing with Datum.
5. **Sub-segment classification:**
   - Large-Scale GPU NeoClouds: Multi-facility, 100MW+, $1B+ valuations (Crusoe, Voltage Park, Nebius)
   - Tier 1 Inference Providers: Inference-as-a-service, real-time API SLAs (Together.ai, Anyscale, Groq)
   - AI Infrastructure Providers: Multi-cloud GPU platforms, API-driven, developer-first (Vultr, Fluidstack, Modal)
   - Sovereign AI Clouds: Regulatory-driven, national AI initiatives, data residency (Nscale, Firmus, E2E Networks)
   - Crypto-to-AI Pivots: Former crypto miners transitioning to AI compute (Hive Digital, HUTS, Core Scientific)

### Exclude Verification

If Phase 1 routed to "Likely exclude" or "Likely Retail ISP":
1. **Retail ISP check:** `[Company] wholesale enterprise services`  -  Look for a B2B or wholesale division. Some retail ISPs have significant wholesale operations that qualify.
2. **Vendor/contractor check:** Confirm whether the company builds/manufactures infrastructure or operates it. Builders = exclude. Operators = may qualify.
3. If confirmed exclude → log to Excludes file with reason and audit trail.
4. If ambiguous → route to Stage 3 as edge case.

---

## Completeness Gate Before `last_enriched_date` Write — MANDATORY

**Failure mode this prevents (added 2026-04-28 per Cooper):** Routines have historically marked `last_enriched_date = today` while leaving enrichment fields partially or entirely unpopulated. This is the worst kind of bug — it makes the record look fresh in HubSpot, takes it out of the stale-rotation pool for 120 days, and hides the actual gap. A record without `customer_segment`, `account_tier`, `account_brief`, etc. is NOT enriched; it's masquerading as enriched. **The 120-day rotation depends on `last_enriched_date` being honest.**

**Hard rule:** `last_enriched_date` is the LAST field written, and it is ONLY written after the completeness check below passes. If the check fails, the record's `last_enriched_date` stays UNCHANGED and the record gets flagged in the run report as "Partial enrichment — held for next run" or escalated to edge-case-researcher.

### Mandatory fields per classification outcome

The completeness gate's required-field list depends on the outcome of segment-classification (ICP / PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN). Apply the matching column:

| Field | ICP (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator) | PARTNER_KEEP (`Other` Tier 5) | HARD_DELETE (`Flagged for deletion`) | DEAD_DOMAIN (`Flagged for deletion`) |
|---|---|---|---|---|
| `customer_segment` | REQUIRED (one of 5 ICP enum values) | REQUIRED (`Other`) | REQUIRED (`Flagged for deletion`) | REQUIRED (`Flagged for deletion`) |
| `company_sub_segment` | REQUIRED (per import-processor cascade) | not required | not required | not required |
| `account_tier` | REQUIRED (TIER_1 - TIER_5) | REQUIRED (`TIER_5`) | not required | not required |
| `segmentation_confidence` | REQUIRED (HIGH / MEDIUM / LOW / MANUAL_REVIEW) | REQUIRED | REQUIRED | REQUIRED |
| `state` | REQUIRED for US records (Field Resolution Ladder applies) | recommended | not required | not required |
| `country` | REQUIRED | REQUIRED | not required | not required |
| `hubspot_owner_id` | REQUIRED (derived from state via territory-manager) | recommended | not required | not required |
| `account_brief` | REQUIRED (segment-aware narrative, ≤400 chars) | REQUIRED (PARTNER_KEEP reason) | REQUIRED (eviction reason) | REQUIRED (dead-domain reason) |
| `infrastructure_profile` | REQUIRED for Tier 1-3 ICP; recommended for Tier 4-5 | not required | not required | not required |
| `fabric_provisioning_approach` | REQUIRED for Colo + Fiber Tier 1-3; not required for other segments | not required | not required | not required |
| `geographic_focus` | REQUIRED for Tier 1-3 ICP; recommended for Tier 4-5 | not required | not required | not required |
| `maiaedge_value_proposition` | REQUIRED for Tier 1-3 ICP | not required | not required | not required |
| `provisioning_landscape` | REQUIRED for Tier 1-3 ICP | not required | not required | not required |
| `linkedin_company_page` | REQUIRED if Apollo returned a non-empty `linkedin_url`; otherwise not required | recommended | not required | not required |
| `last_enriched_date` | **Written LAST, gated on all above** | **Written LAST, gated on all above** | **Written LAST, gated on all above** | **Written LAST, gated on all above** |

### Completeness check workflow (before any HubSpot write)

After segment-classification produces a verdict, BEFORE issuing the `manage_crm_objects.updateRequest` batch:

1. **Determine the classification column** from segment-classification verdict (ICP / PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN).
2. **Iterate the column's REQUIRED-row fields.** For each, verify the routine has a value to write (either freshly researched or already populated in HubSpot from a prior run that's still valid).
3. **Pass scenarios:**
   - All REQUIRED fields populated → proceed with full batch write including `last_enriched_date = today (ET)`. Standard Tier 1/2/3 safety tier rules apply.
4. **Fail scenarios:**
   - One or more REQUIRED fields missing AND the routine couldn't research them this run (website down, Apollo rate-limited, edge-case ambiguity) → **DO NOT write `last_enriched_date`.** Write whatever fields ARE available (partial write is fine — that's progress) but the date stays at its prior value. Flag in run report under "Partial Enrichment — held for next run" with: company ID, missing fields, why each was missing, suggested next-run resolution.
   - Segment-classification returned LOW or MANUAL_REVIEW after edge-case-researcher second pass → **DO NOT write `last_enriched_date`.** This is a Tier 3 hold per CRM Guardian safety rules. The record stays unenriched until Cooper resolves it manually.

### Why this gate is mandatory

The 120-day stale-rotation depends on `last_enriched_date` reflecting actual enrichment. A bumped-but-unfilled record:
- Drops out of Routine 2's stale-rotation pool for 120 days
- Doesn't surface as a Routine 1 candidate (segment may be blank but date isn't, so it's neither fresh nor stale)
- Appears "complete" in Cooper's CRM health dashboard
- Pollutes downstream routines (signal-scan, persona-fill, call-recap, rep prospecting) that all assume enriched records are actually enriched

The gate trades a small near-term cost (a record stays stale one extra week) for a large long-term win (the 120-day rotation pool stays honest, downstream routines stop hitting under-enriched records).

### Run report requirements

Every enrichment run must include a "Completeness Gate" subsection in Cooper's audit DM:

```
*Completeness Gate — Run [YYYY-MM-DD]*
- Records processed: [N]
- Full enrichment (last_enriched_date stamped): [M]
- Partial enrichment (date held): [K]
  - Field-level breakdown: missing infrastructure_profile [count], missing account_brief [count], missing state [count], etc.
- Tier 3 holds (LOW/MANUAL_REVIEW after edge-case-researcher): [J]
- Reasons for partials (top 3): [website unreachable / Apollo null / segment-classification ambiguous / etc.]
```

This makes the failure mode visible. If "Partial enrichment" is consistently >5% of run volume, the source coverage or segment-classification logic needs investigation — not silent date-bumping.

---

## STAGE 3: Edge Case Identification & HubSpot Readiness

At the end of enrichment, flag any companies that don't fit clear QUALIFIED or EXCLUDED buckets. These edge cases get documented for the edge-case-researcher skill to review later.

### Edge Case Rules

| Rule | Trigger | Recommended Research |
|------|---------|----------------------|
| **Retail ISP with Infrastructure Signals** | Website mentions "fiber," "wavelength," or "dark fiber" but appears consumer-focused | Check for wholesale/B2B division |
| **Low Employee Count with Infrastructure Metrics** | <50 employees but website mentions "data center," "POPs," "network," or company name contains "cooperative" | Employee count data error? Check infrastructure reality |
| **Insufficient Data** | Segmentation confidence = LOW and has partial segment signals, or company name is generic/ambiguous | Try deeper searches with state/domain context |
| **Vendor/Contractor with Infrastructure Overlap** | Classified as vendor/contractor but research notes mention "fiber network," "colo," "owns and operates" | Dual business model? May operate real infrastructure |

### Edge Case Output

For each edge case, include in the output file:
- All original enrichment fields
- `edge_case_rule`  -  which rule triggered the flag
- `edge_case_reason`  -  specific finding that triggered it
- `recommended_research`  -  what to investigate further

These feed into the edge-case-researcher skill for deeper investigation.

---

## OUTPUT

Generate two files:

### File 1: Qualified Accounts (HubSpot Import Ready)
XLSX with columns mapped to HubSpot property names. Ready for drag-and-drop import with no transformation. Includes:
- `domain`, `name`, `customer_segment`, `company_sub_segment`
- `state`, `country`, `hubspot_owner_id`
- `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`
- `hyperscaler_proximity`, `key_tenant_segments__cloned_`
- `account_tier`, `account_brief`, `provisioning_landscape`
- `maiaedge_value_proposition`, `recent_news_or_trigger_event`, `segmentation_confidence`
- `lifecyclestage`, `hs_lead_status`, `type`, `hs_is_target_account`
- `last_enriched_date`

**Fields populated from research:**
- `state`  -  HQ state (2-letter abbreviation). Drives territory routing. Research this during Phase 1.
- `country`  -  HQ country. Set for all accounts; critical for international routing to Tim Ziemer.
- `hubspot_owner_id`  -  Derived from `state` using the territory map in property-schema.md. East states → Tim Lieto (161889085), West states → Ken Cunningham (162339176), International → Tim Ziemer (159350430). If state is unknown, leave blank for manual routing.
- `hyperscaler_proximity`  -  Set during colo/fiber research when checking for nearby AWS/Azure/GCP regions. Values: `Announced: <50 miles`, `Announced: 50-200 miles`, `Existing Facility Nearby`, `None Known`. Strong Tier 1 trigger if <50 miles.
- `key_tenant_segments__cloned_`  -  For colo operators only. Multi-select, semicolon-separated. Values: `cloud_providers`, `enterprises`, `carriers`, `content__hyperscale`, `financial_services`, `other`. Set based on tenant types observed during colo research. Leave blank for non-colo segments.

**Static defaults for all qualified accounts:**
- `lifecyclestage` = `subscriber`
- `hs_lead_status` = `NEW`
- `type` = `PROSPECT`
- `hs_is_target_account` = `true`

### File 2: Excludes Log
Documents all excluded companies with:
- Company name, domain, reason for exclusion
- Exclusion rule (if it's an edge case, flag here for potential reclassification)
- Audit trail for manual review

---

## Account Tier Assignment

Assign `account_tier` based on these criteria (Tier 1 = highest priority):

**TIER_1_STRATEGIC**  -  Timing + fit are both strong:
- NeoCloud (any sub-segment)
- Colocation with sub-segment = AI Infrastructure (confirmed GPU tenants or liquid cooling)
- Any ICP segment with a recent trigger event (expansion, funding, leadership change in past 6 months) AND segmentation_confidence = HIGH

**TIER_2_CORE**  -  Strong fit, no urgency trigger:
- Standard Colo with HIGH confidence and Mid-Size or larger infrastructure
- Fiber Operator with HIGH confidence
- Network Operator (either track) with HIGH confidence

**TIER_3_EMERGING**  -  Qualified but smaller or less certain:
- Any ICP segment with MEDIUM confidence
- Small-scale accounts (infrastructure_profile = Small in all dimensions)
- MSP/Aggregator (any confidence)

**UNRANKED**  -  Not enough signal:
- LOW confidence or MANUAL_REVIEW confidence
- Qualified segment but no observable use case signal

---

## Key Enrichment Rules

1. **Website-first, adaptive approach.** Always start with the company website.
2. **Every search earns its place.** Don't search for what the website already answered.
3. **Segment confidence matters.** Flag edge cases, don't force bad classifications.
4. **Preserve the audit trail.** Document what you found and why you classified (or excluded) each company.
5. **HubSpot ready from the start.** Format output so it needs zero transformation.

---

## Skill Chain

- **Feeds from:** account-sourcing (prospect lists), crm-guardian (re-enrichment of stale accounts)
- **Outputs to:** HubSpot via MCP (direct property writes — primary path); import-processor is only invoked for the legacy case of transforming a CSV/XLSX file into HubSpot shape
- **Edge cases go to:** edge-case-researcher (for deeper investigation of borderline accounts)
