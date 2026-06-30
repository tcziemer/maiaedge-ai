---
name: company-enrichment
description: "MaiaEdge company enrichment and classification bot. Research companies, classify into customer segments (Colocation, Fiber Operator, Network Operator, MSP/Aggregator, Neocloud, Enterprise Multi-DC ICP), score/tier, and write enriched records directly to HubSpot via MCP. Use when asked to enrich companies, research accounts, run enrichment pipeline, classify companies for MaiaEdge, or segment analysis. Research-first 5-stage workflow: identity resolution, deep research populating 7 enriched fields, D1 disqualifier gates, deterministic D3 flowchart + D5 protocol traversal, tier computation, HubSpot write. Input: company names or domains. Primary output: HubSpot company-record writes via MCP (all enrichment fields populated, `last_enriched_date` stamped). Secondary output: excludes log for audit trail. Handles deduplication, domain discovery, deep investigation, edge case flagging, and HubSpot property mapping. Falls back to XLSX only when the user explicitly asks for a file."
---

# MaiaEdge Account Enrichment Bot

## Skill Name: `maiaedge-enrichment-bot`
## Call Action: Use when asked to "enrich companies", "research accounts", "run enrichment", or "classify companies for MaiaEdge"

## Purpose
Research companies, classify into MaiaEdge customer segments, score/tier, and write enriched records directly to HubSpot via the HubSpot MCP. Uses a research-first, 5-stage workflow that deep-researches a company into 7 structured enriched fields BEFORE attempting segment routing, then traverses the D3 flowchart and D5 protocol questions deterministically to produce a best-fit verdict with calibrated confidence.

**Primary delivery: HubSpot MCP (direct property writes).** For each qualified company, write every enrichment field (`customer_segment`, `company_sub_segment`, `account_tier`, `segmentation_confidence`, `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`, `account_brief`, `hyperscaler_proximity`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`) to the company record via MCP. Do not produce an XLSX unless the user explicitly asks for one.

**This skill does NOT write `maiaedge_value_proposition`** (Cooper 2026-05-14). Outreach skills (cold-email, linkedin-outreach, prospect-research, sdr-pipeline) populate that field on-demand at outreach time, when the prospect, sender, and angle are all known. Enrichment leaves it alone.

---

## Reference Files (READ BEFORE EXECUTING)

The enrichment bot is a deterministic protocol executor. These files are the source of truth - read them at the start of every run and treat their rules as authoritative over any inline summary.

| File | Purpose | When to read |
|------|---------|--------------|
| `context/account-tiering/sub-segment-qualification.md` | Pointer to file 06 (the consolidated sub-segment qualification reference, sections §1-§11). Lists the 30 active sub-segments with case-sensitive HubSpot enum values, the 6 retired sub-segments, and the locations of D1 disqualifiers, D3 flowchart, D5 protocols, D7 escalation, anchor accounts, and tiebreakers. | Always, at run start |
| `context/account-tiering/enrichment-protocols.md` | D5 v2 operational layer. Encodes the 5-stage research-first workflow, multi-marker classification via `infrastructure_profile`, per-protocol confidence thresholds, end-of-pipeline verification queries, audit string format, and the 6 silent-failure modes the bot must guard against. | Always, at run start |
| `context/account-tiering/tier-compute-spec.md` | Stage 4 specification for `account_tier`. Inputs (customer_segment + company_sub_segment + signals + hs_is_target_account), canonical defaults table, signal modifiers (recent_news_or_trigger_event freshness + score), `hs_is_target_account = true` override behavior (compute logged, write skipped), audit format. | Always at Stage 4 |
| `context/core/segment-qualification.md` | Top-level segment gates (the 6 customer_segment values). Use to verify segment routing at Stage 2. | Stage 2 routing |
| `context/hubspot/property-schema.md` | HubSpot field internal names, enum values, territory map (state → owner_id). | Field write + owner derivation |
| `context/enrichment/research-routes.md` | Research methodology: source prioritization and route selection for the Stage 1b deep-research pass. | Stage 1b research |
| `context/enrichment/output-schemas.md` | Output field format specs for the enriched fields. Validate field shape against this before the Stage 5 write. | Stage 5 write validation |
| `context/account-tiering/` companion files | `context/account-tiering/d1-global-disqualifiers.md` (D1 global disqualifiers), `context/account-tiering/d2-wholesale-arm-policy.md` (D2 wholesale-arm policy), `context/account-tiering/d3-disambiguation-flowcharts.md` (D3 flowcharts). The D5 per-sub-segment protocols + D7 escalation/Greenfield catalog live in `context/account-tiering/enrichment-protocols.md` (§6/§6a/§7, above); anchor accounts + per-pair tiebreakers live in `context/account-tiering/sub-segment-qualification-full.md` (§6). | When the protocol cites a disqualifier, flowchart, anchor, or tiebreaker |
| `context/hubspot/territory-model.md` | **Authoritative 5-region territory map** - read at Stage 1b Step 1 to derive `hubspot_owner_id` from HQ state/country. Do NOT inline the state-to-owner table; apply from this file at runtime. Live write-bug if stale: Central-region records get the wrong owner. | Stage 1b Step 1 + any owner derivation |
| `context/hubspot/hubspot-values.md` | Canonical enum strings for all HubSpot picklist fields (segment values, status values, confidence strings). Use to validate field values before the Stage 5 write so no write lands a non-existent enum. | Stage 5 write validation |
| `context/account-tiering/icp-deep-dives/B-and-C-colocation.md` | Per-ICP deep-dive: Colocation. Feeds Stage 3 D5 anchor matching and confidence thresholds for colo sub-segments. | Stage 3 colo protocol execution |
| `context/account-tiering/icp-deep-dives/B-and-C-fiber-operator.md` | Per-ICP deep-dive: Fiber Operator. Anchor match patterns for F1-F6 protocols. | Stage 3 fiber protocol execution |
| `context/account-tiering/icp-deep-dives/B-and-C-neocloud.md` | Per-ICP deep-dive: NeoCloud. Anchor match patterns for NC1-NC5 protocols. | Stage 3 neocloud protocol execution |
| `context/account-tiering/icp-deep-dives/B-and-C-network-op.md` | Per-ICP deep-dive: Network Operator. Anchor match patterns for N1-N5 protocols. | Stage 3 network-op protocol execution |
| `context/account-tiering/icp-deep-dives/B-and-C-enterprise.md` | Per-ICP deep-dive: Enterprise. Anchor match patterns for E1-E4 protocols; vertical gate examples. | Stage 3 enterprise protocol execution |
| `context/account-tiering/icp-deep-dives/B-and-C-msp-aggregator.md` | Per-ICP deep-dive: MSP/Aggregator. Anchor match patterns for M1-M5 protocols. | Stage 3 MSP protocol execution |
| `context/signals/signal-framework.md` | Signal scoring, field semantics, and the full 5-field signal engine spec. Extend signal write-block to all 5 fields per `context/account-tiering/tier-compute-spec.md` §11.5 when a trigger event is found at Stage 1b. | Stage 1b signal field population |
| `context/core/icp-playbook.md` | Worked per-segment examples + persona pain points. Aids Stage 2 routing disambiguation when website signals are mixed. | Stage 2 segment routing (ambiguous cases) |
| `context/core/terminology-glossary.md` | Canonical definitions for MaiaEdge-specific terms (NaaS, fabric, PBC, PCE, etc.). Use to normalize language in narrative enriched fields. | Stage 1b narrative field authoring |

If any of these files are missing or unreadable, halt and report - do not freeform a classification.

---

## The 5-Stage Research-First Workflow (CANONICAL)

The bot executes these stages in order for every company. No stage may be skipped. The workflow is research-first: the enriched profile (Stage 1b) is populated BEFORE segment routing (Stage 2-3), so classification is reading a structured profile, not guessing from a website snippet.

| Stage | Name | What happens | Outputs |
|-------|------|--------------|---------|
| **Stage 0** | Identity resolution | Domain discovery (Step 0B), HubSpot dedup (Step 0A), re-enrichment mode detection (Step 0C). | Confirmed `company_domain`; record-action verdict (NEW / DEDUP_SKIP / RE_ENRICH) |
| **Stage 1a** | D1 quick check (cheap pre-check) | Read D1 global disqualifiers (file 06 §3). If domain / name pattern obviously trips a D1 rule (dead domain, parked, obvious vendor/contractor name), exit early to `Flagged for deletion` with D1 rule citation. | Early-exit verdict OR proceed to 1b |
| **Stage 1b** | Deep research - populate 7 enriched fields | Apollo enrichment + website read + targeted searches. Populate these 7 fields with the 2-4 sentence conciseness cap on narrative fields: `account_brief`, `geographic_focus`, **`infrastructure_profile` (PRIMARY structured signal)**, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`. | 7 enriched fields populated in a working profile |
| **Stage 1c** | D1 deep check | Re-read D1 disqualifiers against the populated profile. Catches disqualifiers research surfaced that the name/domain alone did not (e.g., website turns out to be a staffing firm, IT-only MSP, residential ISP with no wholesale arm). | Eviction verdict OR proceed to 2 |
| **Stage 2** | Segment routing | Read the enriched profile (especially `infrastructure_profile`) and apply the D3 flowchart pre-gate (file 06 §5) to pick the top-level `customer_segment` (Network Operator / Fiber Operator / Data Center Colo Provider / NeoCloud / MSP/Aggregator / Enterprise-CustomerSegment / Other / Flagged for deletion). | `customer_segment` candidate |
| **Stage 3** | D3 flowchart traversal + D5 protocol questions | Walk the D3 flowchart to a LEAF sub-segment. Identify the D5 protocol ID (N1-N5, F1-F6, C0-C3, NC1-NC5, M1-M5, E1-E4, G, etc.). Run all 5-8 protocol questions reading from the 7 enriched fields. Apply per-protocol confidence thresholds. If 2+ sub-segments tie, apply the named tiebreaker per file 06 §6. | `(sub_segment_value, segmentation_confidence, reasoning_string)` |
| **Stage 4** | Tier computation | Call the tier function per `context/account-tiering/tier-compute-spec.md` - `(customer_segment, company_sub_segment, signals)` → `account_tier` with clamping rules and signal modifiers. **If `hs_is_target_account = true`, compute and log the tier but DO NOT write it.** Honor the manual override. | `account_tier` + audit reason |
| **Stage 5** | HubSpot write + audit | Run the Completeness Gate. Run the 4 end-of-pipeline verification queries (D5 §9). Write all segment/sub-segment/enriched fields via HubSpot MCP. `last_enriched_date` is written LAST, gated on completeness + verification pass. **Never write `maiaedge_value_proposition`.** | HubSpot record updated + audit DM |

### Key operating principles

- **Best-fit classification, not default-manual-review** (Cooper 2026-05-14). Pick the best-fit sub-segment with calibrated confidence even when evidence is partial. `manual_review_required` is reserved for genuine multi-classification ambiguity (2+ protocols match equally). Records with no positive evidence for any ICP sub-segment land on `Flagged for deletion` with a D1 rule citation, not `manual_review_required`.
- **Multi-marker classification.** `infrastructure_profile` is the PRIMARY structured signal. Revenue is dirty more often than infrastructure (under-reported, stale, denominated in odd ranges). When revenue conflicts with infrastructure_profile, infrastructure wins.
- **Conciseness cap.** Narrative enriched fields (`account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event`) are capped at **2-4 sentences each** (override any prior 3-6 sentence hint). Long-form rambling is a smell that the bot is freeforming instead of executing the protocol.
- **No em dashes** in any narrative field. Use hyphens.
- **30 corrected sub-segment names** (case-sensitive - verified via HubSpot MCP 2026-05-14, see `context/account-tiering/sub-segment-qualification.md`). Notable corrections:
  - `Tier 1 Carrier - Network Op` (NOT "Tier 1 Global Incumbent")
  - `Managed Network Services - MSP` (NOT `- Network Operator`, legacy)
  - `Subsea cable operator` (NEW 2026-05-14)
  - `Crypto to AI - Neoclouds` is INCLUSIVE of both operator AND landlord patterns
  - `Greenfield` is a real sub-segment (auto-migrates per file 06 §10 / `context/account-tiering/enrichment-protocols.md` §7)
  - Case-sensitive quirks: `Dark Fiber Specialist - Fiber Operator` (capital O), `AI Infrastructure providers - Neocloud` (lowercase p), `Crypto to AI - Neoclouds` (trailing s)
- **`account_tier_legacy` is archived** (Phase 1.3, 2026-05-13). Read `account_tier` directly. No legacy fallback.
- **`hs_is_target_account`** (was `target_account`) - manual override. When true, Stage 4 logs the computed tier but skips the tier write. All other segment/sub-segment/enriched fields still write at Stage 5.

**Secondary outputs:**
- **Excludes Log** - Record-count summary + per-record exclusion reason delivered inline to the user (and optionally as a file). Audit trail.
- **XLSX file** - ONLY when the user asks ("give me a file", "export to spreadsheet", "prepare for manual import"). Not the default path.

**Skill 2 (Import Processor) is NOT needed when this skill runs.** Import-processor is retained for the rare case of transforming a legacy CSV/XLSX enrichment file into HubSpot-compatible shape - current Claude-driven enrichment writes directly to HubSpot via MCP and skips that step entirely.

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
| `hubspot_owner_id` | **Re-derive** from refreshed `state` / `country` per `context/hubspot/territory-model.md`. Cascade to contacts |
| `linkedin_company_page` | **Overwrite** from Apollo `linkedin_url` when Apollo returns non-empty value differing from HubSpot. Companies change handles after rebrands / M&A |
| `domain` | **Conditional overwrite** - if HubSpot `domain` is blank OR Apollo's primary domain differs AND the HubSpot value no longer resolves (dead DNS / redirect to a new domain), write Apollo's domain. If both HubSpot and Apollo have live-but-different domains, flag as Tier 2 (applied + flagged to Cooper) rather than Tier 1 - this is a rebrand signal worth reviewing |
| `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus` | Overwrite from fresh research |
| `hyperscaler_proximity`, `key_tenant_segments__cloned_` | Overwrite from fresh research |
| `account_brief`, `provisioning_landscape` | Overwrite from fresh research (2-4 sentence conciseness cap). **`maiaedge_value_proposition` is NEVER written by enrichment** - outreach skills populate it at outreach time |
| `recent_news_or_trigger_event` | Overwrite with the highest-scored signal if a fresh signal fired; otherwise leave existing |
| `last_enriched_date` | **Always write** → today's ET date. This is the idempotency key for the 120-day rotation |

**Do NOT overwrite on re-enrichment:** `lifecyclestage`, `hs_lead_status`, `type`, `hs_is_target_account`, `maiaedge_value_proposition`  -  these may have been updated by sales activity since initial import. The `maiaedge_value_proposition` field is OUT OF SCOPE for enrichment entirely (outreach skills own it). Also never overwrite: custom notes, MEDDPICC fields on deals, any field owned by the sales team.

**`hs_is_target_account = true` handling on re-enrichment:** at Stage 4, compute and log the tier but DO NOT write `account_tier`. All other re-enrichment writes proceed normally (the manual override only freezes the tier write).

**Research approach:** Same Phase 1/2/3 as new enrichment. Website-first adaptive research, segment-specific deep dive, qualification gates. No shortcuts  -  treat it as a fresh enrichment with the advantage of already knowing the domain.

**What to watch for on re-enrichment:**
- Company may have changed segment (e.g., colo operator that pivoted to neocloud, fiber op acquired by larger carrier). If segment changes, trigger full cascade: re-derive sub-segment, tier, confidence, infrastructure_profile. Sync updated `customer_segment` to all associated contacts.
- AI infrastructure signals may be new since last enrichment (standard colo → AI colo sub-segment upgrade)
- Leadership changes or acquisitions since last enrichment → update `recent_news_or_trigger_event`
- Trigger events that upgrade tier (expansion, funding → Tier 1 if HIGH confidence)
- Company may have been acquired or gone defunct → if so, flag for review rather than overwriting

**When running under CRM Guardian:** The Guardian's safety tier system and deal protection rule apply. See crm-guardian skill for the authoritative tier definitions. In short: if an account has an open deal and re-enrichment would change `customer_segment` or `account_tier`, those fields are flagged for review rather than auto-written. All other field updates proceed normally.

---

## STAGE 1: Deep Research - Populate the 7 Enriched Fields

This stage maps to the canonical workflow stages 1a (D1 quick check), 1b (deep research), and 1c (D1 deep check after research).

### Stage 1a: D1 Quick Check (Cheap Pre-Check)

Before spending Apollo credits or fetch calls, read `context/account-tiering/sub-segment-qualification.md` → `context/account-tiering/sub-segment-qualification-full.md` §3 (D1 global disqualifiers) and `context/account-tiering/d1-global-disqualifiers.md`. If the input domain or name pattern obviously trips a D1 rule (parked domain, dead DNS, obvious vendor/contractor/staffing/IT-helpdesk name, recipe blog, etc.), exit early to `Flagged for deletion` with the D1 rule ID cited in the audit reason. Do not continue to Apollo.

If nothing trips at 1a, proceed to 1b.

### Stage 1b: Deep Research - Populate 7 Enriched Fields

This stage populates the 7 structured enriched fields that all downstream stages read. Treat these fields as the bot's working memory - Stages 2 and 3 read from this profile, not from the raw website / search transcripts.

**The 7 enriched fields** (with 2-4 sentence conciseness cap on narrative fields, override any prior 3-6 sentence hint):

1. **`account_brief`** - 2-4 sentences. Factual: what they do, scale, geography, regulatory posture (if relevant). No MaiaEdge pitch.
2. **`geographic_focus`** - region / state / country footprint string.
3. **`infrastructure_profile`** - PRIMARY structured signal. Three-bucket format (Facilities / Route Miles / POPs) per `context/account-tiering/enrichment-protocols.md` §4. This is the field segment routing relies on most.
4. **`hyperscaler_proximity`** - single-select. Values per `context/account-tiering/enrichment-protocols.md` §4.5: `Announced: <50 miles`, `Announced: 50-200 miles`, `Existing Facility Nearby`, `None Known`.
5. **`fabric_provisioning_approach`** - multi-select. For operators: how they provision their fabric (megaport / equinix_ecx_fabric / packetfabric / consoleconnect / homegrownproprietary_platform / manuallegacy_processes / none_identified). For Enterprise: semantically flips to what fabric they CONSUME.
6. **`provisioning_landscape`** - 2-4 sentences. Narrative companion to `fabric_provisioning_approach`. Describes the operator's (or enterprise's) current provisioning posture and pain.
7. **`recent_news_or_trigger_event`** - 2-4 sentences. The highest-scored recent signal (expansion, funding, M&A, leadership change). Leave existing value if no new signal fires; clear it only at R2's 90-day staleness check.

### Design Philosophy for Research Calls
Every search must earn its place - read the company's website first, then only search for what the website didn't answer. Three sub-stages inside 1b:
1. **Phase 1**: Read the company's actual website  -  this alone answers ~50% of research questions
2. **Phase 2**: Run ONLY the searches needed based on what Phase 1 revealed (segment-specific deep dive - see Stage 2 segment-specific sections below)
3. **Phase 3**: Fill gaps, resolve ambiguity in the 7 enriched fields

If the website already answered a question, don't search for it again.

---

### Stage 1c: D1 Deep Check (After Research)

After the 7 enriched fields are populated, re-read D1 disqualifiers (file 06 §3) against the populated profile. This catches cases the name/domain alone did not surface - e.g., a "managed services" company whose website reveals it's IT-helpdesk-only, a "fiber" company that's actually residential-only ISP with no wholesale arm, a "data center" company that's a relocation contractor.

If 1c trips a disqualifier → eviction verdict (`Flagged for deletion` or `Other` depending on the rule), with D1 rule ID cited. Otherwise proceed to Stage 2.

---

### PHASE 1 OF 1b: Website + Identity + Apollo (3-4 calls)

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

**Derive `hubspot_owner_id` from Apollo's HQ state** using the 5-region territory map in `context/hubspot/territory-model.md` (authoritative - do NOT inline the state list here; read and apply it at runtime). Non-US records route to Tim Ziemer (`159350430`). State unknown after running the full Field Resolution Ladder below → leave blank for manual routing.

### Field Resolution Ladder (state / country / contact email / phone)

When Apollo returns null, an empty string, or "unknown" on any of `state`, `country`, `phone`, or contact email, do NOT immediately flag for manual research. Run this ladder in order and stop at the first step that yields a HIGH or MEDIUM confidence value. This is the canonical fallback used by all CRM Guardian routines.

| Step | Source | Confidence | Cost | When to use |
|------|--------|------------|------|-------------|
| 1 | `apollo_organizations_enrich` (or `apollo_people_match` for contacts) | HIGH | 1 Apollo credit | Always first |
| 2 | `web_fetch` on `https://[domain]` - read footer, About page, Contact page | HIGH | 1-3 web_fetch calls | If Apollo null on the field |
| 3 | `web_fetch` on `https://www.linkedin.com/company/[slug]/about` - Headquarters block | MEDIUM | 1 web_fetch | If website doesn't disclose location/contact |
| 4 | `web_search` `"[domain] WHOIS registrant address"` → registrant city/state | LOW | 1 web_search | Last resort before Tier 3 hold |

**Confidence handling:**
- HIGH from step 1 or 2 → write the field at Tier 1 (or per the calling routine's safety tier rules).
- MEDIUM from step 3 → write at Tier 2 (applied + flagged) so Cooper can sanity-check.
- LOW from step 4 → write at Tier 3 (held). Surface in the routine report with the source so Cooper can confirm.
- All 4 steps null → Tier 3 hold. Now it's truly "manual research needed."

**Implementation notes:**
- The ladder always runs in order; do not skip step 2 to "save fetches" - the website is HIGH confidence and free of Apollo credit cost.
- For contact records (Routine 8 persona fill), step 1 is `apollo_people_match` and step 3 fetches the contact's individual LinkedIn profile (not the company about page).
- WHOIS step (step 4) is intentionally last because GDPR-redacted WHOIS responses are common; it's a low-yield step that's only worth running when the first three all fail.
- Slack DM reports MUST include the source attribution (e.g., "state filled via website footer" or "via LinkedIn About") so Cooper can audit ladder usage and tune the ordering if any step turns out to be unreliable.

**STAGE 1b PHASE 1 CHECKPOINT: Tentative segment routing for the deep-dive sub-pathway.**

This is a tentative routing only - the authoritative `customer_segment` decision is made at Stage 2 (D3 flowchart pre-gate). Use this table to pick the segment-specific Phase 2 deep-dive below.

| Website signals | Tentative segment | → Phase 2 route |
|---|---|---|
| Data center, colocation, cross-connect, rack space, power | **Data Center Colo Provider** | → Colo research |
| Fiber, route miles, network, transport, wavelength, lit buildings | **Fiber Operator** | → Fiber research |
| National backbone, Tier 1/2, global network, massive scale | **Network Operator** | → Network Op research |
| Aggregator, multi-carrier, no owned infrastructure | **MSP/Aggregator** | → MSP research |
| IS a GPU cloud provider (Lambda, Crusoe, Together.ai, RunPod, Modal, Applied Digital, Hut 8, etc.) | **NeoCloud** | → Neocloud research |
| Large enterprise (Fortune 1000) in financial services / healthcare systems / national retail with multi-DC corporate IT / BPO with multi-site delivery centers AND no "we sell connectivity" signal AND in-house network engineering signals (NOC mentions, VP/Director Network Engineering roles, Equinix Fabric / Megaport customer logo presence) | **Enterprise-CustomerSegment** | → Enterprise research |
| Staffing, software, consulting, manufacturing, construction | **Likely D1 trip** | → Stage 1c D1 deep check |
| Residential broadband, ISP, "sign up for internet" | **Likely D1 trip** (Retail ISP) | → Stage 1c (check for wholesale before evicting) |
| Website down, parked domain, or completely unrelated | **Likely D1 trip** | → Stage 1c D1 deep check |
| Can't determine from website alone | **Ambiguous** | → broad search fallback then Stage 1c |

---

## STAGE 1b PHASE 2: Segment-Specific Deep Dive (populates the 7 enriched fields)

Each tentative segment has its own deep-dive pathway. Run ONLY the searches relevant to the tentative segment. Every search must earn its place. The output of this Phase is the populated 7-field profile that Stages 2 and 3 read.

### Colocation Operators

1. **Facility search:** `[Company] data center facilities locations`  -  Extract facility count, geographic spread, and major markets. → `infrastructure_profile` (Facilities bucket)
2. **AI signal check (MANDATORY for all colos):** `[Company] Lambda Labs Crusoe GPU liquid cooling AI-ready`  -  Look for: confirmed GPU cloud tenants, liquid cooling infrastructure, 30kW+ rack density, "AI-ready" marketing. If strong AI signals found → `company_sub_segment` = `AI Infrastructure`. If none → `Standard`.
3. **NaaS presence:** Check the company website for Megaport, PacketFabric, Equinix Fabric, or Console Connect badges/partnerships. → `fabric_provisioning_approach`
4. **Hyperscaler proximity:** `[Company] AWS Azure Google Cloud data center nearby`  -  Check if company facilities are near announced or existing hyperscaler regions. → `hyperscaler_proximity` (`Announced: <50 miles` is a strong Tier 1 trigger)
5. **Tenant types:** From website and search results, identify what types of tenants they serve. → `key_tenant_segments__cloned_` (cloud_providers, enterprises, carriers, content__hyperscale, financial_services, other). Semicolon-separated.
6. **Tentative sub-segment routing (final decision happens at Stage 3 via D5 protocols C0-C3):** Standard - colo (no AI signals), AI Signals - colo (confirmed GPU tenants or liquid cooling), Greenfield (announced but not built), Subsea cable operator (rare cross-routed). Final sub-segment string per `context/account-tiering/sub-segment-qualification.md`.

### Fiber Operators

1. **Infrastructure search:** `[Company] fiber route miles network states lit buildings`  -  Extract route miles, lit building count, geographic footprint. → `infrastructure_profile` (Route Miles bucket), `geographic_focus`
2. **NaaS competitive signals:** `[Company] Megaport PacketFabric NaaS`  -  Are they already using a third-party fabric? → `fabric_provisioning_approach`
3. **Wholesale vs retail:** Confirm they sell wholesale/enterprise connectivity, not just residential broadband. Residential-only = exclude.
4. **Carrier partners and interconnection:** Look for NNI partners, peering relationships, carrier-neutral facilities.
5. **Tentative sub-segment routing (final decision happens at Stage 3 via D5 protocols F1-F6):** 6 active Fiber sub-segments per `context/account-tiering/sub-segment-qualification.md` -> `Regional CLEC - Fiber operator` (licensed carrier, 3-12 states, metro/regional - catch-all default), `Long Haul / Backbone - Fiber operator` (national/multi-national, 1000+ route miles cross-metro), `Dark Fiber Specialist - Fiber Operator` (capital O - 80%+ dark fiber IRU revenue), `Tier 2 National Wholesale - Fiber operator` (national US/EU, 20K+ route miles, 80%+ wholesale - Zayo post-CCF / Lightpath / Uniti+Windstream / EXA EU), `Regional Cable Operator - Fiber operator` (regional cable parent with growing fiber arm), `Municipal / Cooperative - Fiber operator` (muni / co-op / consortium). NOT Fiber: `Subsea cable operator` (NEW 2026-05-14, NETWORK OPERATOR sub-segment, not Fiber - pure-play subsea ownership with minimal terrestrial). Cross-segment NOT Fiber: `Greenfield` pairs ONLY with Colo or NeoCloud, NOT Fiber. **Note:** `Regional CLEC - Fiber operator` is a catch-all - at Stage 3 verification it requires positive-evidence questions per the catch-all guard check.

### Network Operators

1. **Automation check (determines messaging track):** `[Company] customer portal API self-service provisioning`  -  Look for evidence of branded portals, API access, self-service provisioning tools.
   - **Track A (External Extension):** Has internal automation, portal, API. The gap is cross-carrier, not internal.
   - **Track B (Internal + External Unification):** No evidence of portal/API automation. Fragmented internally.
2. **Scale verification:** Confirm 50+ PoPs, national/global footprint, 2K+ employees. Under these thresholds → may be a fiber operator or MSP instead.
3. **Branded products:** Look for named connectivity products, enterprise services, wholesale offerings.
4. **Tentative sub-segment routing (final decision happens at Stage 3 via D5 protocols N1-N5):** 5 active Network Operator sub-segments per `context/account-tiering/sub-segment-qualification.md` -> `Tier 1 Carrier - Network Op` (top-of-stack global incumbent - NOT "Tier 1 Global Incumbent", that name is retired), `Pure Wholesale Carrier - Network Op` (100% B2B carrier-to-carrier wholesale - Cogent, Arelion, EXA Infrastructure, Hurricane Electric, Sparkle), `Cable MSO Enterprise Division - Network Op` (B2B arm of national cable parent - Comcast Business, Spectrum Enterprise, Cox Business, Optimum Business), `International Backbone Specialist - Network Op` (international long-haul + significant terrestrial - Tata Communications, PCCW Global, Telstra International, HGC Global), `Subsea cable operator` (NEW 2026-05-14, no `- Network Op` suffix - pure-play subsea with minimal terrestrial - Aqua Comms, Seaborn Networks, BW Digital, Hawaiki, Telxius). The VNO archetype lives within `Tier 1 Carrier - Network Op` (or Pure Wholesale Carrier when the VNO operates wholesale-only) - there is no separate `VNO - Network Op` sub-segment in HubSpot.

### MSP / Aggregators

1. **Carrier aggregation check:** `[Company] managed services carrier aggregation multi-carrier`  -  Identify upstream carrier partners. Confirm they aggregate circuits from multiple carriers.
2. **IT MSP Test (MANDATORY):** Apply this test to avoid misclassifying IT MSPs:
   - Does the website mention carrier names (AT&T, Lumen, Comcast)? → Telecom signal
   - Does it list MPLS, WAN, SD-WAN, DIA services? → Telecom signal
   - Does it list helpdesk, endpoint management, cybersecurity? → IT MSP signal (EXCLUDE)
   - Does "managed services" mean managing carriers or managing IT endpoints?
3. **Asset-light verification:** Confirm <10% owned infrastructure. If they own significant fiber or facilities → may be a fiber operator or colo instead.
4. **Tentative sub-segment routing (final decision happens at Stage 3 via D5 protocols M1-M5):** Telecom Aggregator - MSP (aggregates carrier circuits, wholesale connectivity - catch-all, requires positive evidence at Stage 3), `Managed Network Services - MSP` (NOT `- Network Operator`, that's retired legacy - managed WAN/MPLS, service-oriented), plus other MSP sub-segments per `context/account-tiering/sub-segment-qualification.md`.

### Neoclouds

1. **GPU infrastructure ownership (MANDATORY):** `[Company] GPU cloud infrastructure facilities data center`  -  Confirm they OWN or have committed funding to build physical GPU hardware in physical facilities. "AI cloud" marketing alone is NOT sufficient. If they're reselling cloud GPU from AWS/Azure/GCP without owning hardware → EXCLUDE (Cloud GPU Reseller).
2. **Expansion and funding:** `[Company] expansion funding 2025 2026`  -  Growth signals, new facility announcements, funding rounds. Strong Tier 1 triggers.
3. **Scale and capacity:** Facility count, total compute capacity (MW, GPU count), geographic distribution.
4. **Datum partnership check:** If the company appears in Datum.net's network or customer base, note for channel routing. Datum is a channel partner (Layer 7: proxy, anycast, DDoS). MaiaEdge solves Layer 2/3. Do not position as competing with Datum.
5. **Tentative sub-segment routing (final decision happens at Stage 3 via D5 protocols NC1-NC5).** Use the case-sensitive HubSpot enum values per `context/account-tiering/sub-segment-qualification.md`:
   - `Large Scale GPU - Neocloud`: multi-facility, 100MW+, $1B+ valuations (Crusoe, Voltage Park, Nebius)
   - `Tier 1 Inference - Neocloud`: inference-as-a-service, real-time API SLAs (Together.ai, Anyscale, Groq)
   - `AI Infrastructure providers - Neocloud` (lowercase "p"): multi-cloud GPU platforms, API-driven, developer-first (Vultr, Fluidstack, Modal)
   - `Sovereign AI Clouds - Neocloud`: regulatory-driven, national AI initiatives, data residency (Nscale, Firmus, E2E Networks)
   - `Crypto to AI - Neoclouds` (trailing "s"): INCLUSIVE of BOTH operator pattern (former crypto miners now running GPU compute themselves) AND landlord pattern (former miners leasing/converting facilities for AI tenants). One sub-segment covers both - do NOT split.

### Enterprise (Multi-DC ICP)

Promoted to ICP 2026-05-11. HubSpot `customer_segment = "Enterprise-CustomerSegment"`. Priority 5 (lowest ICP). Tier 2 ceiling. Run this research path when Phase 1 routes to Enterprise OR when Apollo industry data + Phase 1 website read suggest a multi-DC enterprise in one of the four ICP verticals.

1. **Vertical gate verification (MANDATORY first):** Confirm the company sits in ONE of the four ICP sub-segments:
   - **Financial Services - Enterprise** - banks, investment firms, insurers, payment networks, capital-markets infrastructure, exchanges. Defense contractors that procure commercially (Lockheed, RTX, Northrop, BAE, L3Harris) land here based on commercial procurement profile, NOT their gov work.
   - **Healthcare Systems - Enterprise** - multi-hospital IDNs and large health systems. Single-hospital regional systems below scale fail.
   - **Retail and Distribution - Enterprise** - national retailers with multi-DC corporate IT plus distribution-center networks. Multi-warehouse alone does NOT qualify - the qualifier is multi-DC corporate IT.
   - **Outsourcing Services - Enterprise** - BPO / outsourced operations providers running multi-site delivery centers on an ongoing operational basis. Project-based consulting (Deloitte, McKinsey, BCG, Bain) is EXCLUDED. Dual-arm firms (Cognizant) classify on operational delivery revenue mix.
   - If the company is Manufacturing / Energy/Utilities / Logistics/Supply Chain / Government/Defense / SaaS-only → DO NOT classify as Enterprise. Route to `Other` (Watch List) or `Unknown`.

2. **Scale gate verification (MANDATORY second):** Confirm $1B+ revenue AND at least one of:
   - 3+ data centers (search `[Company] data center locations` / `[Company] 10-K data center`; for SOX-regulated financials and large retailers, 10-K filings disclose DC counts)
   - Direct Equinix Fabric or Megaport customer (search Equinix customer logo pages and Megaport press releases / blog)
   - Confirmed in-house network engineering team (LinkedIn search for `[Company]` + `VP Network Infrastructure` / `Director Network Engineering` / `Principal Network Engineer`; check for NOC presence on careers page)
   - **If scale gate fails → reclassify to `Other` (mid-market $200M-$1B hold) or `Unknown`. Do NOT write `customer_segment = "Enterprise-CustomerSegment"` for records that fail scale.**

3. **Hard disqualifier check:** If ANY of these are true, the account is NOT Enterprise ICP regardless of size:
   - Network fully outsourced to a single managed service provider with no internal engineering ownership.
   - Single data center or single geography.
   - No direct carrier contracts (everything through reseller or MSP).
   - If any hard disqualifier triggers → route to `Other`.

4. **DC footprint + infrastructure profile:** Confirm DC count (`infrastructure_profile` → Facilities bucket: Small `<5` / Mid-Size `5-19` / Large `20-49` / Enterprise `50+`). Most ICP enterprises land in Small (with 3-4 DCs) or Mid-Size. Route Miles and POPs typically come back as `None Identified` for Enterprise records (they don't operate route miles or POPs the way fiber operators do).

5. **Fabric consumption check:** Identify what third-party fabric or cloud-on-ramp the enterprise depends on (Megaport, Equinix Fabric, PacketFabric, carrier-managed). Note: for Enterprise, `fabric_provisioning_approach` semantically flips - instead of "how do they provision their fabric to customers," it becomes "what fabric do they depend on as a consumer." Set values per what they consume (`megaport` / `equinix_ecx_fabric` / etc.). Use `homegrownproprietary_platform` if they have a self-built corporate WAN management layer; `manuallegacy_processes` if it's mostly manual; `none_identified` if no signal.

6. **Hyperscaler proximity:** Set `hyperscaler_proximity = "None Known"` for Enterprise (N/A semantically - they're consumers of cloud, not located near hyperscaler regions for monetization).

7. **Recent trigger event signals (Tier 2 gate):** Search for M&A activity, AI workload announcements, leadership changes (VP Network / CIO / CSO in last 6 months), DC expansion / new DC announcement, multi-cloud migration kickoff, regulatory pressure (HIPAA breach disclosures, PCI audit findings, GDPR enforcement actions). A recent trigger event combined with `high_90` confidence + scale gate pass is the Tier 2 ceiling criterion.

8. **Sub-segment assignment:** Map to one of the four ICP sub-segment values:
   - `Financial Services - Enterprise`
   - `Healthcare Systems - Enterprise`
   - `Retail and Distribution - Enterprise`
   - `Outsourcing Services - Enterprise`

9. **account_brief guidance for Enterprise** (this skill writes ONLY account_brief, NOT maiaedge_value_proposition):
   - **account_brief**: 2-4 sentences (conciseness cap). Cover what they do, their multi-DC footprint, their fabric/cloud-on-ramp posture, their vertical-specific regulatory exposure (HIPAA / PCI-DSS / SOX / GDPR / HITRUST as applicable). Stay factual; do NOT pitch MaiaEdge here.
   - **`maiaedge_value_proposition` is NOT written by this skill.** Outreach skills (cold-email, linkedin-outreach, prospect-research, sdr-pipeline) populate it at outreach time when the sender, the buyer persona, and the angle are all known. Enrichment leaves it alone.
   - **Banned language for Enterprise narrative fields** (operator monetization framing does NOT apply to enterprise account_brief copy either): "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "wholesale activation," "extend reach to new markets," "tenant," "meet-me room," "interconnection revenue," "aggregator." Federation is internal language - never customer-facing for Enterprise. Pair speed with data sovereignty + audit trails, NOT "your team provisions in minutes" (that's operator framing).

### Exclude Verification

If Phase 1 routed to "Likely exclude" or "Likely Retail ISP":
1. **Retail ISP check:** `[Company] wholesale enterprise services`  -  Look for a B2B or wholesale division. Some retail ISPs have significant wholesale operations that qualify.
2. **Vendor/contractor check:** Confirm whether the company builds/manufactures infrastructure or operates it. Builders = exclude. Operators = may qualify.
3. If confirmed exclude → log to Excludes file with reason and audit trail.
4. If ambiguous → route to Stage 3 as edge case.

---

## Completeness Gate Before `last_enriched_date` Write - MANDATORY

**Failure mode this prevents (added 2026-04-28 per Cooper):** Routines have historically marked `last_enriched_date = today` while leaving enrichment fields partially or entirely unpopulated. This is the worst kind of bug - it makes the record look fresh in HubSpot, takes it out of the stale-rotation pool for 120 days, and hides the actual gap. A record without `customer_segment`, `account_tier`, `account_brief`, etc. is NOT enriched; it's masquerading as enriched. **The 120-day rotation depends on `last_enriched_date` being honest.**

**Hard rule:** `last_enriched_date` is the LAST field written, and it is ONLY written after the completeness check below passes. If the check fails, the record's `last_enriched_date` stays UNCHANGED and the record gets flagged in the run report as "Partial enrichment - held for next run" or escalated to edge-case-researcher.

### Mandatory fields per classification outcome

The completeness gate's required-field list depends on the outcome of segment-classification (ICP / PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN). Apply the matching column:

| Field | ICP (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise) | PARTNER_KEEP (`Other` Tier 5) | HARD_DELETE (`Flagged for deletion`) | DEAD_DOMAIN (`Flagged for deletion`) |
|---|---|---|---|---|
| `customer_segment` | REQUIRED (one of 6 ICP enum values) | REQUIRED (`Other`) | REQUIRED (`Flagged for deletion`) | REQUIRED (`Flagged for deletion`) |
| `company_sub_segment` | REQUIRED (per import-processor cascade - Enterprise must be one of the four ICP sub-segments) | not required | not required | not required |
| `account_tier` | REQUIRED (TIER_1 - TIER_5; Enterprise capped at TIER_2) | REQUIRED (`TIER_5`) | not required | not required |
| `segmentation_confidence` | REQUIRED (HIGH / MEDIUM / LOW / MANUAL_REVIEW) | REQUIRED | REQUIRED | REQUIRED |
| `state` | REQUIRED for US records (Field Resolution Ladder applies) | recommended | not required | not required |
| `country` | REQUIRED | REQUIRED | not required | not required |
| `hubspot_owner_id` | REQUIRED (derived from state via territory-manager) | recommended | not required | not required |
| `account_brief` | REQUIRED (segment-aware narrative, ≤400 chars) | REQUIRED (PARTNER_KEEP reason) | REQUIRED (eviction reason) | REQUIRED (dead-domain reason) |
| `infrastructure_profile` | REQUIRED for Tier 1-3 ICP; recommended for Tier 4-5. For Enterprise, Facilities bucket is the primary signal; Route Miles and POPs typically `None Identified`. | not required | not required | not required |
| `fabric_provisioning_approach` | REQUIRED for Colo + Fiber Tier 1-3 + Enterprise (semantic flips for Enterprise - values reflect what fabric they CONSUME, not provision); not required for other segments | not required | not required | not required |
| `geographic_focus` | REQUIRED for Tier 1-3 ICP; recommended for Tier 4-5 | not required | not required | not required |
| `maiaedge_value_proposition` | **NOT WRITTEN BY THIS SKILL** - owned by outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) at outreach time | NOT WRITTEN | NOT WRITTEN | NOT WRITTEN |
| `provisioning_landscape` | REQUIRED for Tier 1-3 ICP (2-4 sentence conciseness cap) | not required | not required | not required |
| `recent_news_or_trigger_event` | REQUIRED for Tier 1-3 ICP if a fresh signal fires (2-4 sentence conciseness cap); otherwise preserve existing value | not required | not required | not required |
| `linkedin_company_page` | REQUIRED if Apollo returned a non-empty `linkedin_url`; otherwise not required | recommended | not required | not required |
| `last_enriched_date` | **Written LAST, gated on all above** | **Written LAST, gated on all above** | **Written LAST, gated on all above** | **Written LAST, gated on all above** |

### Completeness check workflow (before any HubSpot write)

After segment-classification produces a verdict, BEFORE issuing the `manage_crm_objects.updateRequest` batch:

1. **Determine the classification column** from segment-classification verdict (ICP / PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN).
2. **Iterate the column's REQUIRED-row fields.** For each, verify the routine has a value to write (either freshly researched or already populated in HubSpot from a prior run that's still valid).
3. **Pass scenarios:**
   - All REQUIRED fields populated → proceed with full batch write including `last_enriched_date = today (ET)`. Standard Tier 1/2/3 safety tier rules apply.
4. **Fail scenarios:**
   - One or more REQUIRED fields missing AND the routine couldn't research them this run (website down, Apollo rate-limited, edge-case ambiguity) → **DO NOT write `last_enriched_date`.** Write whatever fields ARE available (partial write is fine - that's progress) but the date stays at its prior value. Flag in run report under "Partial Enrichment - held for next run" with: company ID, missing fields, why each was missing, suggested next-run resolution.
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
*Completeness Gate - Run [YYYY-MM-DD]*
- Records processed: [N]
- Full enrichment (last_enriched_date stamped): [M]
- Partial enrichment (date held): [K]
  - Field-level breakdown: missing infrastructure_profile [count], missing account_brief [count], missing state [count], etc.
- Tier 3 holds (LOW/MANUAL_REVIEW after edge-case-researcher): [J]
- Reasons for partials (top 3): [website unreachable / Apollo null / segment-classification ambiguous / etc.]
```

This makes the failure mode visible. If "Partial enrichment" is consistently >5% of run volume, the source coverage or segment-classification logic needs investigation - not silent date-bumping.

---

## STAGE 2: Segment Routing (D3 Flowchart Pre-Gate)

After Stage 1 populates the 7 enriched fields and survives 1c, route to a top-level `customer_segment` value by reading the enriched profile (especially `infrastructure_profile`) and walking the D3 segment flowchart pre-gate per `context/account-tiering/sub-segment-qualification-full.md` §5 (and `context/account-tiering/d3-disambiguation-flowcharts.md`).

The output of Stage 2 is ONE of the 8 top-level `customer_segment` values:

| Value (HubSpot internal) | When |
|---|---|
| `Network Operator(Tier 1 / VNO)` | Top-of-stack carriers, VNOs, large network ops |
| `Fiber Operator` | Owned fiber as the primary asset |
| `Data Center Colo Provider` | Owned/operated DC facilities as primary asset |
| `NeoCloud` | GPU compute owned or committed-build provider |
| `MSP/Aggregator` | Asset-light managed or aggregated services |
| `Enterprise-CustomerSegment` | Multi-DC ICP enterprise (4 sub-verticals) - Tier 2 ceiling |
| `Other` | Watch List / partner-keep / mid-market hold |
| `Flagged for deletion` | D1 disqualifier or no positive ICP evidence |

If the profile shows ambiguity between two segments at this stage, do NOT default to `manual_review_required` - pick the best fit based on `infrastructure_profile` (the PRIMARY structured signal, beats revenue when they conflict per `context/account-tiering/enrichment-protocols.md` §4). Manual review only fires if Stage 3 produces a genuine 2-protocol tie at equal confidence.

---

## STAGE 3: Deterministic D3 Flowchart Traversal + D5 Protocol Execution

This stage is a DETERMINISTIC protocol executor. No freeform "best-guess sub-segment" logic. The bot walks the D3 flowchart from the Stage 2 segment to a leaf sub-segment, identifies the D5 protocol ID, runs the protocol's 5-8 questions reading from the 7 enriched fields, and produces `(sub_segment_value, confidence, reasoning_string)`.

### Step 3.1 - Walk the D3 flowchart to a leaf sub-segment

Per `context/account-tiering/sub-segment-qualification-full.md` §5 (and `context/account-tiering/d3-disambiguation-flowcharts.md`):
- Enter the flowchart at the Stage 2 segment node.
- Follow the decision branches using values from the 7 enriched fields (especially `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`).
- Terminate at a LEAF sub-segment node. Each leaf maps to one of the 30 active sub-segment HubSpot enum values.

### Step 3.2 - Identify the D5 protocol ID

Each leaf sub-segment maps to a D5 protocol ID (`context/account-tiering/sub-segment-qualification-full.md` §6 + `context/account-tiering/enrichment-protocols.md` §6):

| Segment | Protocol IDs |
|---|---|
| Network Operator | N1, N2, N3, N4, N5 |
| Fiber Operator | F1, F2, F3, F4, F5, F6 |
| Colocation | C0, C1, C2, C3 |
| NeoCloud | NC1, NC2, NC3, NC4, NC5 |
| MSP/Aggregator | M1, M2, M3, M4, M5 |
| Enterprise | E1, E2, E3, E4 |
| Cross-segment | G (Greenfield) |

### Step 3.3 - Run the protocol's 5-8 questions against the 7 enriched fields

The bot reads the 5-8 protocol questions from D5 and answers each one by referencing the 7 enriched fields populated at Stage 1b. Do NOT issue new web fetches at this stage - the research is already done. If a question cannot be answered from the populated profile, that question is `unknown`, which lowers confidence (not eviction).

### Step 3.4 - Apply per-protocol confidence threshold

Per `context/account-tiering/enrichment-protocols.md` §6 / file 06 §6:

| Confidence | Trigger |
|---|---|
| `high_90` | Named anchor account match (anchor accounts file 06 §7) OR all required protocol questions confirmed AND infrastructure_profile pattern matches the canonical pattern for the sub-segment per `context/account-tiering/enrichment-protocols.md` §4 |
| `medium_70` | Most required questions confirmed, infrastructure_profile partial match, no contradicting D1 disqualifier |
| `low_5069` | Half or fewer required questions confirmed, OR catch-all sub-segment defaulted-to with only negative-exclusion evidence (no positive evidence) |
| `manual_review_required` | 2+ protocols match equally and the tiebreaker (`context/account-tiering/sub-segment-qualification-full.md` §6) cannot resolve |

### Step 3.5 - Tiebreaker (if 2+ sub-segments match)

If two or more sub-segments are tied after Step 3.4, apply the named tiebreaker for that specific pair per `context/account-tiering/sub-segment-qualification-full.md` §6. Each pair has its own deterministic tiebreaker - do NOT freeform.

If the tiebreaker resolves → final sub-segment string + adjusted confidence.

If the tiebreaker cannot resolve → output `manual_review_required` confidence + reasoning string identifying both candidate sub-segments.

### Step 3.6 - Output the Stage 3 verdict

Produce this tuple:
- `sub_segment_value` - one of the 30 case-sensitive HubSpot enum strings per `context/account-tiering/sub-segment-qualification.md`
- `segmentation_confidence` - `high_90` / `medium_70` / `low_5069` / `manual_review_required`
- `reasoning_string` - short audit string citing the D5 protocol ID + the answered questions, per `context/account-tiering/enrichment-protocols.md` §10 audit format. Example: `"C2/AI Signals - colo: liquid cooling confirmed (Q1 ✓), GPU tenant Crusoe Lambda named (Q2 ✓), 30kW+ rack density disclosed (Q3 ✓); anchor match (Cyxtera). high_90."`

### Greenfield auto-migration handling

If Stage 3 lands on `Greenfield` (G protocol) BUT the bot has evidence the facility is now lit / operational, apply the Greenfield auto-migration rule per `context/account-tiering/enrichment-protocols.md` §7 - promote to the matched mature sub-segment (e.g., Standard - colo, Regional CLEC - Fiber operator).

### Catch-all guard

`Regional CLEC - Fiber operator`, `Standard - colo`, and `Telecom Aggregator - MSP` are catch-all defaults. They MUST be backed by positive-evidence protocol questions, not just negative-exclusion. If Stage 3 lands on a catch-all sub-segment with only negative-exclusion evidence (e.g., "not a long-haul because <10K route miles, therefore Regional CLEC"), downgrade confidence to `low_5069` and route to R2 / D7 escalation (`cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md`).

---

## STAGE 4: Tier Computation (`context/account-tiering/tier-compute-spec.md`)

Call the tier compute function with these inputs (per `context/account-tiering/tier-compute-spec.md` §3):
- `customer_segment` (from Stage 2)
- `company_sub_segment` (from Stage 3)
- `recent_news_or_trigger_event` (from Stage 1b - both the score band and the freshness window matter)
- Apollo / website signals captured during Stage 1b
- `hs_is_target_account` (manual override flag from HubSpot record)

Apply the algorithm per `context/account-tiering/tier-compute-spec.md` §4:
- Step A0 - Pre-classification disqualifier guard (re-check D1 disqualifiers didn't slip through)
- Step A - Manual override: **if `hs_is_target_account = true`, compute the tier and log it in the audit reason, but DO NOT write `account_tier`.** Stage 5 still writes all segment/sub-segment/enriched fields normally - the override only freezes the tier write.
- Step B - Defaults lookup (canonical defaults table, §5)
- Step C - Null + unknown-pair fallback (§6)
- Step D - Signal modifiers (signal score × freshness, §7)
- Step E - Clamp to inverted convention (Tier 1 = highest, Tier 5 = lowest; Enterprise capped at Tier 2)
- Step F - Build the reason string per §10
- Step G - Return `(account_tier, audit_reason, write_skipped_flag)`

**No legacy fallback.** `account_tier_legacy` is archived (Phase 1.3, 2026-05-13). Do not read it.

---

## STAGE 5: HubSpot Write + End-of-Pipeline Verification

Stage 5 is the only stage that mutates HubSpot. It runs in this order:

### Step 5.1 - Completeness Gate

Run the Completeness Gate (see the dedicated section below). If any REQUIRED field for the classification outcome is missing, partial-write the available fields but DO NOT write `last_enriched_date`. Flag as "Partial Enrichment - held for next run" and surface in the audit DM.

### Step 5.2 - End-of-Pipeline Verification Queries (D5 §9 / `context/account-tiering/enrichment-protocols.md` §8)

Run all 4 self-validation checks. If any fails, downgrade or escalate before writing.

1. **Sub-segment nullness check** - If `customer_segment` is an ICP value (Network Operator / Fiber Operator / Data Center Colo Provider / NeoCloud / MSP/Aggregator / Enterprise-CustomerSegment) AND `company_sub_segment` is null, confirm `segmentation_confidence = manual_review_required` AND the reasoning string names both candidate sub-segments. If neither is true, halt the write - this is a silent-failure pattern (ICP segment with no sub-segment is not a valid HubSpot state).

2. **Confidence-evidence alignment check** - `high_90` requires EITHER a named anchor account match (`context/account-tiering/sub-segment-qualification-full.md` §6 anchors) OR all required D5 protocol questions confirmed. If neither is true but Stage 3 emitted `high_90`, downgrade to `medium_70` and append to the reasoning string: `"downgraded from high_90: alignment check failed (no anchor, partial protocol)."`

3. **Disqualifier audit check** - If the verdict is `customer_segment = "Other"` (eviction/Watch-List) the reasoning string MUST cite a D1 rule ID (`context/account-tiering/d1-global-disqualifiers.md`). If no D1 rule is cited, the eviction is freeform and must escalate to D7 (`cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md`) rather than write `Other`.

4. **Catch-all guard check** - If the sub-segment is `Regional CLEC - Fiber operator`, `Standard - colo`, or `Telecom Aggregator - MSP` AND the reasoning string is only negative-exclusion (no positive evidence question confirmed), downgrade `segmentation_confidence` to `low_5069` and route to R2 / D7 for a positive-evidence pass. Do not write `high_90` or `medium_70` on a catch-all sub-segment with only negative evidence.

### Step 5.3 - HubSpot MCP write

If all 4 verification queries pass (or partial-write conditions are met), issue the `manage_crm_objects.updateRequest` batch with all enriched fields. **Never write `maiaedge_value_proposition`** (Cooper 2026-05-14 - outreach skills own that field). Write order: all fields first, `last_enriched_date` LAST so the date never lands ahead of an incomplete write.

**`flagged_for_deletion_reason` companion write (REQUIRED on eviction):** Whenever this write sets `customer_segment = "Flagged for deletion"`, the SAME batch MUST also set `flagged_for_deletion_reason` (multi-line text), leading with one of the 7 canonical reason codes + a colon + one evidence sentence (no em dashes). For the enrichment-pipeline eviction path the code is `D1 disqualified (no reference value)` (D1 match) or `No ICP fit` (researched, no positive ICP evidence). **Clear-on-exit:** if any write moves a record OFF `Flagged for deletion` back into an active segment, set `flagged_for_deletion_reason` to empty in the same batch. Full 7-code spec: `context/hubspot/property-schema.md` §2.1.

### Step 5.4 - Audit string

Per `context/account-tiering/enrichment-protocols.md` §10, write an audit string into the run report capturing:
- Company ID, domain, name
- Stage 2 segment + Stage 3 sub-segment + confidence + D5 protocol ID
- Stage 4 tier (or `hs_is_target_account=true / write_skipped` if override active)
- Which of the 7 enriched fields were freshly written vs preserved
- Verification check outcomes (pass / downgrade / hold)

---

## Stage 3 - Edge Cases & Manual-Review Triggers

Edge cases are subordinate to Stage 3 protocol execution. They surface as outputs of Stage 3 + Stage 5 verification, NOT as a separate freeform stage. The "best-fit + calibrated confidence" principle (Cooper 2026-05-14) applies:

- Records with no positive evidence for any ICP sub-segment → `customer_segment = "Flagged for deletion"` with a D1 rule citation. NOT `manual_review_required`. In the SAME HubSpot update, set `flagged_for_deletion_reason` (multi-line text). Lead with the canonical reason code, then a colon and one concrete sentence of evidence (no em dashes - use a colon): if the eviction is driven by a D1 disqualifier match, use `D1 disqualified (no reference value): [cited D1 rule + what the entity is]`; if research found no positive evidence for any ICP sub-segment and no D1 match applies, use `No ICP fit: [what the entity is + why it has no ICP fit]`. The 2-4 sentence prose rationale still goes in `account_brief` (keep that write). Canonical 7-code spec: `context/hubspot/property-schema.md` §2.1.
- Records with genuine multi-protocol tie at equal confidence after tiebreaker → `segmentation_confidence = manual_review_required` with the reasoning naming both candidates.
- Records that downgrade to `low_5069` via the catch-all guard or confidence-evidence alignment check → route to R2 / D7 for a positive-evidence research pass.

Legacy edge-case rules (Retail ISP with Infrastructure Signals, Low Employee Count with Infrastructure Metrics, Vendor/Contractor with Infrastructure Overlap) now collapse into the D1 deep check (Stage 1c) - they are disqualifier patterns, not separate edge-case classifications. The edge-case-researcher skill takes over only for records that exit Stage 5 with `segmentation_confidence = manual_review_required` after both 1c and the 4 verification queries.

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
- `recent_news_or_trigger_event`, `segmentation_confidence`
- `lifecyclestage`, `hs_lead_status`, `type`, `hs_is_target_account`
- `last_enriched_date`

**`maiaedge_value_proposition` is NOT included in this output.** Outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) populate it at outreach time. Enrichment never writes it.

**Fields populated from research:**
- `state`  -  HQ state (2-letter abbreviation). Drives territory routing. Research this during Phase 1.
- `country`  -  HQ country. Set for all accounts; critical for international routing to Tim Ziemer.
- `hubspot_owner_id`  -  Derived from `state` using the 5-region territory map in `context/hubspot/territory-model.md` (authoritative). Apply the map at runtime - do not inline the state list. If state is unknown, leave blank for manual routing.
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

## Account Tier Assignment (delegated to `context/account-tiering/tier-compute-spec.md`)

`account_tier` is computed at Stage 4 by calling the tier compute function defined in `context/account-tiering/tier-compute-spec.md`. The function takes `(customer_segment, company_sub_segment, signals, hs_is_target_account)` and applies the algorithm in §4 of the spec. Do NOT freeform tier assignment from inline rules - the spec is the single source of truth.

Quick reminders (NOT a substitute for reading the spec):

- **Inverted tier convention:** Tier 1 = highest priority, Tier 5 = lowest.
- **Enterprise ceiling:** Tier 2 (the clamp applies in Step E of the algorithm).
- **`hs_is_target_account = true`:** Compute and log the tier; DO NOT write `account_tier`. All other fields still write.
- **Signal modifiers:** `recent_news_or_trigger_event` score band + freshness apply additively per spec §7.
- **No legacy fallback.** `account_tier_legacy` is archived (Phase 1.3, 2026-05-13). The tier compute function reads `account_tier` only.
- **Worked examples** for common (segment, sub-segment, signal) combinations are in spec §9 - including the `hs_is_target_account = true` freeze case (Example 6) and the inclusive `Crypto to AI - Neoclouds` operator-or-landlord case (Example 8).

---

## Key Enrichment Rules

1. **Research-first.** Populate the 7 enriched fields BEFORE segment routing (Stage 2). The structured profile is the bot's working memory; Stages 2 and 3 read from it, not from raw website / search transcripts.
2. **Website-first within Stage 1b.** Inside the deep-research stage, always start with the company website. Every additional search must earn its place.
3. **Deterministic protocol execution at Stage 3.** Walk the D3 flowchart to a leaf sub-segment, identify the D5 protocol ID, run the protocol's 5-8 questions against the 7 enriched fields, apply the per-protocol confidence threshold and named tiebreaker. No freeform "best-guess sub-segment" logic.
4. **Best-fit + calibrated confidence, NOT default-manual-review.** Records with no positive ICP evidence → `Flagged for deletion` with D1 rule citation. `manual_review_required` is reserved for genuine multi-protocol ties.
5. **Multi-marker classification.** `infrastructure_profile` is the PRIMARY structured signal. Revenue is dirty more often than infrastructure - infrastructure wins on conflict.
6. **Conciseness cap.** Narrative enriched fields (`account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event`) are capped at 2-4 sentences each. No em dashes - use hyphens.
7. **Tier comes from `context/account-tiering/tier-compute-spec.md`.** Stage 4 calls the spec function; honor `hs_is_target_account = true` (compute, log, skip write).
8. **Never write `maiaedge_value_proposition`** (Cooper 2026-05-14). Outreach skills own that field - they populate it at outreach time when sender, persona, and angle are all known.
9. **Use the 30 corrected sub-segment names exactly** (case-sensitive). Read `context/account-tiering/sub-segment-qualification.md` for the canonical enum strings (verified via HubSpot MCP 2026-05-14).
10. **End-of-pipeline verification queries run on every record** (Stage 5.2 / D5 §9). Downgrade or escalate before writing - `last_enriched_date` is written LAST, gated on completeness + verification pass.
11. **Preserve the audit trail.** Every record gets a reasoning string citing the D5 protocol ID, the confirmed questions, and any verification downgrades.

---

## Skill Chain

- **Feeds from:** account-sourcing (prospect lists), crm-guardian (re-enrichment of stale accounts)
- **Outputs to:** HubSpot via MCP (direct property writes - primary path); import-processor is only invoked for the legacy case of transforming a CSV/XLSX file into HubSpot shape
- **Manual-review records go to:** edge-case-researcher (only for records that exit Stage 5 with `segmentation_confidence = manual_review_required` after Stage 1c and the 4 verification queries)
- **`maiaedge_value_proposition` is owned by:** cold-email, linkedin-outreach, prospect-research, sdr-pipeline (populated on-demand at outreach time)
- **Reads authoritative rules from:** `context/account-tiering/sub-segment-qualification.md`, `context/account-tiering/enrichment-protocols.md`, `context/account-tiering/tier-compute-spec.md`
