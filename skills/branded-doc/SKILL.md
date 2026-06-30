---
name: maiaedge-branded-doc
description: "Generate partner-grade PDFs in the MaiaEdge brand system. Tomorrow font (embedded), gold/orange/black palette, doc-style cover, eyebrow-numbered sections, branded tables, component cards. Use for partner cheat sheets, MaiaEdge 101-style briefs, battle cards, playbooks, one-pagers, technical references, AND post-call leave-behinds - any partner-facing PDF that should look like the existing partner doc set. Triggers: 'branded doc about X', 'partner PDF for X', 'cheat sheet / battle card / playbook in our brand system', 'turn this markdown into a branded PDF', 'post-call leave-behind for [account]', 'recap and path forward doc', 'leave-behind to send after the [account] call'."
---

# MaiaEdge Branded Doc Generator

Produces partner-grade PDFs in the MaiaEdge design system - visually consistent with the partner cheat sheets and MaiaEdge 101.

## Reference Files

Read these before building any branded deliverable. The Step 0 router above calls out the document-type-specific sources; these are the always-on knowledge layer.

**Core brand + positioning (always read):**
- `assets/brand-reference.md` - full brand system, colors, components, gotchas
- `context/core/messaging-framework.md` - positioning rules, banned language, Cross-Segment Pillar Framework
- `context/copy-strategy/segment-language.md` - vocabulary lock per segment (USE / AVOID per ICP)
- `context/copy-strategy/segment-messaging.md` - angle-selection logic per segment

**Business case + economics:**
- `context/sales/business-case-framework.md` - canonical 10-section framework for segment and account-specific business cases (§A segment, §B account-specific, §C slide-deck outline, §D rigor rules)
- `context/sales/pricing-reference.md` - SKU pricing, discount math, term lengths, ROI model inputs
- `context/product/cloud-onramp-business-case.md` - cloud on-ramp economics (Fiber / Network Operator / Colo / MSP only)
- `context/product/economic-impact-acg-whitepaper.md` - quantified operator outcomes for proof sections
- `context/product/proof-points.md` - anonymized customer outcomes
- `context/sales/use-case-taxonomy.md` - canonical use case list + segment mapping
- `context/hubspot/poc-schema.md` - POC structure for implementation-path sections (§D rigor)

**Strategy + segment depth (grab the matching one):**
- `context/sales/neocloud-strategy-brief.md` - sub-segment economics for neocloud / AI-colo business cases
- `context/sales/edge-ai-thesis-montauk.md` - DETERMINISTIC flagship proof for neocloud / AI-colo
- `context/sales/golden-pitch-key-slides.md` - slide-by-slide reference for §C deck workflow
- `context/core/icp-playbook.md` - per-segment pain + worked examples for business case buyer's-situation framing
- `context/core/competitive-positioning.md` - objection responses and competitive framing (leave-behind objection blocks)
- `context/europe/sovereignty-positioning.md` - DORA/NIS2 framing for European Enterprise / operator accounts

## Use when

- New segment cheat sheet, battle card, playbook, one-pager, or technical brief
- Any markdown content that should ship as a branded partner-facing PDF

**Don't use for:** legal docs (use `sales-docs`), short copy/emails (use outreach skills).

## Clarification (ask before building)

Two questions that shift the output:

1. Which doc type and funnel stage? One-pager (hook a meeting post-connect), leave-behind (advance a deal post-call), or a segment asset (cheat sheet / battle card / use-case brief / business case)? Name the account and segment if you have them.
2. For leave-behinds and business cases: share the call notes or pain points raised - the doc is built from what they actually said, not generic segment framing.

If you only have a doc type and a company name, that is enough to start - segment and signals will be pulled from HubSpot and the context files.

## Step 0 - Pick the variant, then read its context

This skill has THREE variants. Identify which one the request is BEFORE building, then read that variant's context - the right context is what makes the doc correct, not just the styling. The two post-engagement variants (one-pager, leave-behind) are the seller's highest-volume use; they are NOT the general workflow.

| The seller wants... | Variant (jump to its section) | Build system | Read FIRST for the content |
|---|---|---|---|
| A one-pager to hook a meeting - rides a LinkedIn accept or email reply, NEVER cold | **Outbound One-Pager Variant** | `assets/onepager/` (render.py + qa.py, locked template) | `assets/onepager/content-schema.md` - full context router + persona->angle map |
| A post-call recap / debrief / "doc our champion can forward" to advance a deal | **Post-Call Leave-Behind** | `assets/leavebehind/` (template + guide, then `assets/build.py`) | `assets/leavebehind/leave-behind-guide.md` |
| A segment cheat sheet | General workflow | `assets/build.py` | `context/partner-assets/cheatsheet-<segment>.md` (the source) + `context/segments/<segment>.md` |
| A battle card vs a named competitor | General workflow | `assets/build.py` | `context/core/competitive-positioning.md` + `context/core/differentiation-naas-aggregator.md` |
| A use-case brief (e.g. GPU cluster connectivity) | General workflow | `assets/build.py` | the matching use-case source in `context/partner-assets/` (GPU clusters -> `context/partner-assets/use-case-gpu-cluster-connectivity.md`, **NeoCloud / AI-colo scope ONLY**) + `context/sales/use-case-taxonomy.md` + `context/product/proof-points.md` (+ `context/product/ai-market-positioning.md` if AI) |
| A MaiaEdge 101 / company overview | General workflow | `assets/build.py` | `context/partner-assets/maiaedge-101.md` + `context/core/messaging-framework.md` |
| A product / technical reference | General workflow | `assets/build.py` | `context/partner-assets/product-quick-reference.md` + `context/product/pbc-pce-datasheet.md` + `context/product/integrated-switch-datasheet.md` |
| A playbook or any other branded brief | General workflow | `assets/build.py` | the segment + sales context for that topic (`context/segments/<segment>.md`, `context/sales/use-case-taxonomy.md`, `context/product/proof-points.md`) |

Every variant ALSO reads `assets/brand-reference.md` (the brand system) and obeys `context/core/messaging-framework.md` (positioning). `<segment>` is one of: `colocation`, `fiber-operator`, `neocloud`, `network-operator`, `msp-aggregator`, `enterprise`.

**Segment scope is load-bearing - never cross it.** A doc's economics and use cases are segment-specific. Check the source's top metadata before using it, and match the angle to the account's segment: operator segments (SP / fiber / colo / neocloud) are PROFIT-CENTER (revenue, margin, new services), Enterprise is COST-CENTER (cost, risk, redundancy, audit), and neoclouds drop OPERATOR sovereignty. Specifically: the GPU cluster use-case brief is **NeoCloud / AI-colo only**; the ACG economic white paper (`context/product/economic-impact-acg-whitepaper.md`) and the wholesale / cloud-on-ramp economics (`context/product/cloud-onramp-business-case.md`) are **Fiber / Network Operator / Colocation (+ MSP) only - never Enterprise or NeoCloud**. For an economic or business-case leave-behind, pull the quantified backing from those two files, matched to the account's segment.

## The funnel map - which doc moves the deal, and what shape it takes

branded-doc is a full-funnel toolkit, not a doc generator. Every ask maps to a funnel stage with a job, a defined shape, and a segment-flex rule. The whole maiaedge folder is mounted, so each format below POINTS to the spec, exemplar, and context to grab - open the source, never author the shape from memory.

**Segment-flex is one lever everywhere: the per-segment Pillar Framework.** Lead every doc with the account's segment pillars, in order, and never cross segments (see the segment-scope rule above). Quick reference: Fiber = MONETIZE / AUTOMATE / EXTEND REACH · Colocation = INSTANT / MONETIZE / REACH · AI-Colo = DETERMINISTIC / INSTANT / MONETIZE · Neocloud = DETERMINISTIC / PRIVATE / INSTANT · Network Op (Tier 1) = AUTOMATE / EXTEND REACH / MONETIZE · Network Op (Tier 2/3) = EXTEND REACH / MONETIZE / AUTOMATE · MSP/Aggregator = AUTOMATE / EXTEND REACH / MONETIZE · Enterprise = REDUNDANT / SOVEREIGN / AUTOMATED. Full table + rationale: `context/core/messaging-framework.md` § Cross-Segment Pillar Framework.

| Funnel stage | The ask | Job | Shape / spec to read | Build |
|---|---|---|---|---|
| **1. Get the meeting** (rides a connect/reply, NEVER cold) | Outbound one-pager | Earn the first conversation | `assets/onepager/content-schema.md` (locked + qa.py) | `onepager/` |
| **2. Educate / discovery** | Use-case brief | Hand the champion a sharable artifact on ONE problem they own | exemplar `context/partner-assets/use-case-gpu-cluster-connectivity.md` + shape below | `build.py` |
| **2. Educate / discovery** | Technical reference | Answer the technical buyer's "how does it actually work" | exemplar `context/partner-assets/product-quick-reference.md` + shape below | `build.py` |
| **3. Differentiate** (prospect named a competitor) | Comparison brief | Win "why you vs them" without trashing them | shape below + `context/core/differentiation-naas-aggregator.md` | `build.py` |
| **4. Advance / build consensus** (post-call) | Leave-behind (recap & path forward) | The seller in the room you are not in | `assets/leavebehind/leave-behind-guide.md` (10-section, locked) | `leavebehind/` |
| **5. Justify / decide** (CFO, committee) | Business case (segment or account) | The economic case to sign | `context/sales/business-case-framework.md` §A (segment) / §B (account) - 10-section framework + Business Case Rigor + ROI from `context/product/cloud-onramp-business-case.md` & `context/product/economic-impact-acg-whitepaper.md` | `build.py` |
| **5b. Slide deck** | Deck outline | Slide-by-slide outline + markdown source + design notes when the output is a presentation, not a PDF | `context/sales/business-case-framework.md` §C + `context/sales/golden-pitch-key-slides.md` | outline only (branded-doc renders PDFs, not decks) |
| **6. Expand** (post-PO) | Expansion brief / QBR | Grow the footprint into the next sites + use cases | shape below | `build.py` |
| **Enablement** (pre-funnel; events, warm intro) | MaiaEdge 101 / segment cheat sheet | Category intro (101); the cheat sheet is INTERNAL rep enablement, not a customer funnel asset | `context/partner-assets/maiaedge-101.md` / `context/partner-assets/cheatsheet-<segment>.md` | `build.py` |

Per-stage context to grab is in the Step 0 router above. Below are the shapes for the four formats with no standalone spec file. All obey the segment-scope rule, the Pillar Framework, and earned-problem framing (name the predictable challenge of where they are going, never a verdict on how they run today - canonical `context/outreach/email-writing-rules.md` § The Earned-Problem Doctrine).

### Use-case brief (stage 2) - shape
One problem, one segment, the mechanism, named plays. Order: (1) title + one line "eliminates X so you can Y"; (2) the problem - the compounding, segment-specific pain, stated forward-state; (3) the MaiaEdge approach - the mechanism (PBC/PCE) in plain terms; (4) use cases - 3-5 NAMED plays specific to this segment's workflow (classify against `context/sales/use-case-taxonomy.md`); (5) reference architecture (optional, for technical readers); (6) close - scales with the business. Lead the plays with the segment's Pillar 1.

### Technical reference (stage 2) - shape
For the technical champion. Order: product overview -> architecture (swap in an `assets/diagrams/` SVG) -> what each component does (PBC / PCE / port extender) -> deployment models -> integration (Equinix / Megaport) -> security (AES-256-GCM line-rate, sovereign routing) -> specs table. Model depth + ordering on `context/partner-assets/product-quick-reference.md`. Neutral technical voice; no margin / monetization framing unless the reader is commercial.

### Comparison brief (stage 3) - shape
Customer-facing, ONLY when the prospect named the competitor first. Order: (1) the category framing (where MaiaEdge sits - "carrier infrastructure you deploy and bill on," not a fabric to join); (2) an honest comparison table on the dimensions THIS account raised - concede what the competitor does well, then show where MaiaEdge differs; (3) the objection reframes in the three registers from `context/core/differentiation-naas-aggregator.md`; (4) one segment-matched proof point. Never trash the competitor; honor that file's claims-to-avoid list.

### Expansion brief / QBR (stage 6) - shape
Post-PO, to grow the footprint. Post-engagement voice (named references + credibility anchors ALLOWED, as in the leave-behind). Order: (1) what is live today - sites, paths, outcomes realized, quantified from their own data; (2) what the data shows - utilization, what is working; (3) the next 2-3 plays - new sites, new use cases, new segments to sell into, each tied to a segment pillar; (4) a mutual expansion plan with owners + dates.

## General workflow (cheat sheets, battle cards, MaiaEdge 101, technical and use-case briefs)

1. **Read** `assets/brand-reference.md` (full brand system: colors, components, lessons learned, gotchas) and `context/core/messaging-framework.md` for positioning. THEN read the document-type context from the Step 0 router above - that is what makes the content right, not just the styling.

2. **Stage assets** - copy from this skill's `assets/` into the working directory:
   - `brand.css` (with `@font-face` for Tomorrow)
   - `fonts/Tomorrow-*.ttf` (9 weights)
   - `logos/logo-white.svg`
   - `pattern-twotone.png`
   - `icons/<segment>.svg` (cover icon - see mapping in brand-reference.md)
   - `icons/library/*.svg` (40-icon brand library for diagrams + component cards - inventory in brand-reference.md)
   - `product-images/` (PBC + Port Extender photography, for hardware / datasheet docs)
   - `cover-template.html`
   - `build.py` (the renderer)

3. **Author markdown.** Standard markdown. `## Title` for sections, `### Title` for sub-sections. Tables → branded tables. `> Blockquotes` → pain-quote panels (or callouts if a single quote starts with `**Label:**`).

4. **Build** - run `python3 assets/build.py` (or call the equivalent steps inline). It strips the H1, pre-processes lists, renders HTML, post-processes (auto-numbered eyebrows, pain-quote grouping, Q&A table tagging), wraps in cover, and renders PDF via WeasyPrint.

5. **Cover** - fill `cover-template.html` tokens: `title`, `title_accent`, `segment_tag`, `segment_sub`, `subtitle`, `icon_path`.

6. **Diagram swaps** - for ASCII diagrams in fenced code blocks, replace with one of the production SVGs in `assets/diagrams/` (architecture, activation-flow, cloud-onramp). Build new diagrams from the brand icon library in `assets/icons/library/` (PBC, PCE, Port Extender, Cross-Connect, Cloud Onramp, etc.) so they stay on-system; SVG with brand colors at 1600×1100 viewBox.

7. **Render PDF** - `HTML(filename="doc.html", base_url=".").write_pdf("Doc.pdf")`. The `base_url` must resolve `@font-face` URLs.

8. **QA pass:**
   - `pdffonts Doc.pdf` confirms Tomorrow is embedded
   - Render every page to PNG: `pdftoppm -r 80 -png Doc.pdf qa/p` and visually verify
   - No table row split mid-cell, no page > 30% whitespace at the bottom, no em dashes anywhere

9. **Output** - save to `partner docs/final/`. Filename: `<DocType>-<Topic>.pdf` (e.g., `Cheat-Sheet-Colocation.pdf`, `Battle-Card-Cisco.pdf`).

## Brand system at a glance

- **Colors:** Gold `#FFC200` (primary), Orange `#FF9400` (accent), Heather `#D4D0C9` (warm), Black, Heather Tint `#F4F2EE`
- **Font:** Tomorrow only, embedded via `@font-face`
- **No em dashes** - use `·` for inline caps separators
- **"Carrier infrastructure"** is the only acceptable category descriptor

Full reference: `assets/brand-reference.md`.

## Reference examples

Match anything new to the existing set, in look AND structure:
- **Visual exemplars (PDFs that exist today):** open whatever is in `partner docs/final/` - the live, approved partner-doc set (currently `MaiaEdge-HUB787-Onward-Reach.pdf`, `One-Pager-Sharon-AI.pdf`, `Use-Case-Brief-GPU-Cluster-Connectivity.pdf`). For the one-pager variant, rendered exemplars also live in `assets/onepager/` (Sharon-AI, Genesis-Cloud, Orchest, example-Nscale).
- **Canonical content sources (always current, never stale):** the markdown these docs are built from - `context/partner-assets/maiaedge-101.md`, `context/partner-assets/cheatsheet-<segment>.md` (all 6 segments), and `context/partner-assets/product-quick-reference.md`. Read the matching source for structure, depth, and section order before authoring a new one.

---

## Outbound One-Pager Variant (post-engagement asset)

**Trigger: a LinkedIn connection ACCEPT or an email reply. NEVER cold.** The one-pager is not offered, attached, or promised in any cold E1/E2/E3. It rides the thank-you DM after an accept, or the follow-up after a reply.

This variant is a LOCKED, gated template so account briefs ship at volume without per-doc QA. The skeleton carries the safety; personalization lives only in the content slots. Everything is in `assets/onepager/`:

| File | Role |
|---|---|
| `assets/onepager/render.py` | The renderer. Reads a content JSON, outputs ONE single-page branded PDF (Style A "Solution Brief", compact masthead, no full-bleed cover, Tomorrow embedded). Structure is fixed. |
| `assets/onepager/content-schema.md` | The slot spec: every field, its word cap, the voice rules, and the "headers STATE the point, never ANNOUNCE the move" rule. Read this before filling a brief. |
| `assets/onepager/content.example.json` | Worked example (Nscale). Copy per account. |
| `assets/onepager/facts.md` | Single source of truth for stat-strip numbers + external market claims. Every number in a brief comes from here, verbatim. RevOps-owned. |
| `assets/onepager/qa.py` | Pre-flight gate. BLOCKS brand/voice/format problems (leaks, announcing headers, dashes, segment call-out, missing slots, over-cap). FLAGS unverified numbers + account claims as non-blocking VERIFY-BEFORE-SEND notes. |

**Self-contained:** `assets/onepager/` vendors the Tomorrow fonts + logo, so the whole system runs from that one folder. Only external dependency is WeasyPrint (`assets/onepager/requirements.txt`; needs pango/cairo). Run the commands from inside `assets/onepager/`.

**Locked structure (do not add / remove / reorder):** masthead -> 3-up stat banner -> hook (structural truth, stated) -> why-now (forward-state) -> 3-play table (the CENTERPIECE: bigger + deeper) -> what-MaiaEdge-is + pillars -> one-line CTA.

**Build workflow:**
1. Research the account + contact from the company brain to pick the angle: confirm segment (`context/core/segment-qualification.md`), pull persona pains + value props (`context/core/messaging-framework.md`, `context/copy-strategy/segment-messaging.md`), the why-now trigger (`context/signals/<segment>-signals.md`), candidate plays (`context/sales/use-case-taxonomy.md`), and proof (`context/product/proof-points.md`). Full context router + persona->angle map are in `content-schema.md`.
2. Copy `content.example.json` -> `content.<account>.json`; fill every slot within caps, forward-state voice, headers that STATE not announce, stats pulled from `facts.md`.
3. `python3 assets/onepager/qa.py content.<account>.json` - clear MUST-FIX items (they block); confirm each VERIFY-BEFORE-SEND assumption against research (these do NOT block, you guide).
4. `python3 assets/onepager/render.py content.<account>.json` - produces the single-page PDF.
5. Spot-check the PDF (pdffonts shows Tomorrow; one page; no bottom overflow).

**Hard rules (enforced by qa.py, restated here):**
- Headers STATE the point ("The one layer still rented"), never announce the move ("The structural truth", "Why it matters now", "Where we fit"). Structure is felt, not labeled.
- Forward-state only: name the predictable challenge of where they are going, never an asserted flaw in how they run today.
- No internal / pre-call voice on a customer page: no "pre-meeting brief", "ahead of our conversation", "not a pitch", "working session", "clear view of fit", no MaiaEdge founder names, no staging of our meeting. That lives in the follow-up email.
- No em dashes; one page; the masthead eyebrow is ACCOUNT-ONLY (no segment call-out); the product header is a neutral safe label like "What MaiaEdge is", not a category self-claim.
- The 3-play `pays` column is the heaviest hitter, and its lead angle is RESEARCH-DRIVEN, never defaulted: pick what THIS account + THIS contact care about (commercial / CFO -> margin from the compute+connectivity package; security / regulated -> provable sovereignty; engineering -> determinism + visibility; sales -> speed to revenue; ops -> one operating model). Lead the first play with the fit; competitive differentiation is the weakest lead. Persona->angle map in content-schema.md.
- Verifiability: a brief states only what is verified. Do NOT make a big claim about the customer's business from the outside without verified research. qa.py does not block on this - it FLAGS every unverified number and account claim as a VERIFY-BEFORE-SEND note so the user confirms it. Auto-approved numbers live in the `facts.md` fence.
- Every stat-strip number is grounded in `facts.md`. External market facts get re-verified before each use.

**Delivery:** pressure-off thank-you DM with the PDF attached, no CTA push (Campaign A thank-you-note pattern). After a reply, it may go by email instead.
**Follow-up:** the NEXT email touch names ONE claim from the brief and asks to pressure-test it; that email carries the meeting ask. The brief is the hook only if a human asks for the meeting.
**Logging (mandatory):** note on the contact `one-pager sent: [file] via [channel] YYYY-MM-DD` per linkedin-outreach. Undelivered briefs are invisible briefs.

---

## Post-Call Leave-Behind (Recap & Path Forward) - the deal-advancing variant

**Trigger: AFTER a discovery or demo call, to ADVANCE the deal.** Distinct from the outbound one-pager above
(which rides a connection-accept/reply to GET a meeting). This is the document a champion forwards across their
org to build internal consensus. It is the seller in the room you are not in. Triggers: "leave-behind for the
[account] call," "recap and path forward for [account]," "doc our champion can forward up."

**The governing idea (from the research this mode is built on):** the person who decides was probably not on the
call, so write the document they will read on a forward, not a recap for the person who was there. Three rules
shape everything: (1) build it group-relevant, not over-personalized to one persona; (2) lead with the cost of
THEIR status quo before any MaiaEdge capability; (3) the objection section DE-RISKS, it never re-sells the
upside or re-establishes urgency (re-hyping a hesitant buyer statistically loses the deal).

**Everything for this mode is in `assets/leavebehind/`:**

| File | Role |
|---|---|
| `assets/leavebehind/leave-behind-guide.md` | The build guide: the audience parameter, the data router (call-analysis + MEDDPICC + HubSpot), the section structure, the voice deltas, the objection pattern, ROI discipline, and the VERIFY-BEFORE-SEND checklist. Read this first. |
| `assets/leavebehind/template.md` | The fill-in markdown skeleton. Copy per account, fill from the inputs, render with `assets/build.py`. |
| `assets/leavebehind/example-northgate-colo.md` | A worked illustrative example (fictional account) showing the structure, order, and post-engagement voice. |

**Build workflow:**
1. **Specify the audience first** (the rep names it: the champion / CFO / technical lead / the full committee). It
   shifts what leads and which proof shows up. See guide §0.
2. **Gather inputs by composing on the `call-analysis` skill (Mode 1)** over the account's recent call(s) - it
   already extracts the use cases discussed, the pain, the objections, and reads the MEDDPICC contact fields
   (`meddpicc_pain_contact`, `meddpicc_metrics_contact`, `meddpicc_criteria_contact`, `meddpicc_competition_contact`,
   `meddpicc_use_case`, `Champion`). Then pull the company, deal, and contact records. Guide §1.
3. **Copy `template.md` to `leave-behind-<account>.md`** and fill every section from the inputs, dropping any
   section with no real input. Pull objection answers from `context/core/competitive-positioning.md` +
   `context/core/differentiation-naas-aggregator.md`; use cases from `context/sales/use-case-taxonomy.md`; proof
   from `context/product/proof-points.md`; any external/product number from `assets/onepager/facts.md`.
4. **Run the VERIFY-BEFORE-SEND checklist** (guide §6) - this mode renders flexible markdown via `build.py` with
   no `qa.py`, so the QA is on you.
5. **Render via `assets/build.py`** (add a leave-behind entry to its `DOCS` registry with the cover tokens, or
   call the equivalent inline render steps per the main workflow above). Flexible 1-3 pages; for enterprise/high-ACV,
   extend to the ~5-page business case (guide §3) using the `branded-content` business-case framework.
6. **Deliver + log:** send to the champion (built to forward). Note on the contact
   `leave-behind sent: [file] re [call date] for [audience] YYYY-MM-DD`.

**Voice deltas vs. the cold one-pager (this is post-engagement, mid-cycle):** named customer references, case
studies, and the credibility anchors (Acme Packet / 128 Technology) are now ALLOWED; referencing the call is the
whole point; naming their stated current-state cost is fine (they said it). KEPT: no em dashes, "carrier
infrastructure" only, and a hard no-fabrication rule (every number labeled + ranged + input-grounded). Full rules
in guide §4-§5.
