# Changelog

## [1.5.4] - 2026-06-16

### Outreach writing skills: swap-test forcing-field added to the Research Receipt gate

Hardened the write-time anti-templating gate in cold-email, sdr-pipeline, and linkedin-outreach to close the one structural seam behind the "Claude ships a segment template instead of researching this contact" failure. The skills already had both halves of the machinery - a Research Receipt (input gate, with refuse-to-write teeth and "an email without a Receipt is invalid output") AND the swap test (output). But the swap test lived only in SOFT locations (the Angle-First Principle and a post-hoc quality-checklist item) that are easy to rubber-stamp, while the gate that actually has teeth (the Receipt) only verified research was DONE, not that the email USED it. You could fill an honest Receipt and still write a swappable template.

Added a required **"Anchor in the email/message + Swap test"** field to all three Receipt formats and to each refuse-to-write rule: the writer must name the ONE company/contact-specific fact the body is built on and assert why the email would NOT make sense sent to a different company in the segment. If no non-generic anchor can be named, the email is a template and is invalid output even when the searches ran (re-research or reframe, do not ship). This ties the documented research to the output, moves the swap test from a checkbox to a forcing-function inside the gate that already refuses to write, and aligns the writers with the copy-strategist swap-test detector (1.5.3). No new rules - the swap test now sits inside the gate with teeth.

## [1.5.3] - 2026-06-16

### copy-strategist: gate research-SKIPPING (templating), not just research-display

Closed the asymmetry that was actively incentivizing templated, un-researched outreach - the failure where Claude cuts corners and ships a segment-generic template instead of researching the specific contact/company. Dimension 2 ("Research as Fuel") treated research DISPLAY as a disqualifying HARD FAIL but research ABSENCE (a swappable segment template) as merely a low score, so the safe move to avoid the disqualifying sin was to show nothing and go generic. Now both directions are hard fails: an email scores 0 on Research as Fuel if it survives the **swap test** (move the company + contact name to a different company in the same segment and it still reads as fully sent-to-them = the research was skipped).

- `scoring-rubric.md`: added the symmetric HARD FAIL for research absence (Dim 2) + a company-specific-anchor PASS requirement to the batch-distinctiveness gate (Dim 12); corrected the "3-4" band wording (templating is research absence, not display).
- `copy-strategist/SKILL.md`: added a named **Research-Skipped / templating detector** (filter 4b, the inverse of the research-display filter) + a batch templating sweep (check 2a) + the templating line in the "biggest thing wrong" list; added a Core-Philosophy caveat ("absorbed is not generic") that corrects the skill's own swappable example, which was being held up as the model.
- Aligns the scorer with the already-canonical Relevance Principle swap test, and explicitly distinguishes the templating failure from the legitimate research-display carve-out (one fresh why-now signal stated as an observation is the strongest swap-test pass, not a violation).

## [1.5.2] - 2026-06-16

### maiaedge-branded-doc plugin: full context bundle (all 3 modes run standalone)

Expanded the plugin manifest `context` from 1 file to 32 so the one-pager and post-call leave-behind modes run standalone from the plugin, not just the cheatsheet mode. Now bundles everything the branded-doc modes actually read: the positioning spine (messaging-framework, segment-qualification, icp-playbook, competitive-positioning, differentiation-naas-aggregator, sub-segment-qualification), the 6 segment cheatsheets + enterprise-use-cases, the 6 signal catalogs + signal-framework + universal-platform-signals, copy-strategy (segment-messaging, segment-language), sales (use-case-taxonomy, account-brief-template), product (proof-points, ai-market-positioning, cloud-onramp-business-case, pbc-pce-datasheet), and outreach voice (email-writing-rules, voice-gold-standard, persona-targeting-blocklist) - i.e. the one-pager content-schema router + the leave-behind guide's full read set. Bumped manifest + `.claude-plugin/plugin.json` to 1.1.0 in lockstep (no version mismatch). Build verified: zero missing-context warnings, 32 files in `references/`, zip ~2.5MB.

## [1.5.1] - 2026-06-16

### branded-doc is now a Cowork plugin (`maiaedge-branded-doc`)

Registered `branded-doc` as the 11th Cowork plugin. It is the only plugin that ships a skill **asset payload**: `build.sh`'s plugin loop bundles a skill's full `assets/` tree (plus README/QUICKSTART) next to SKILL.md whenever the skill has one, so branded-doc's relative `assets/...` paths (the `build.py` renderer, the 9 Tomorrow fonts, `brand.css`, `cover-template.html`, diagrams, and the `onepager/` + `leavebehind/` systems) resolve inside the plugin. Verified: `bash build.sh` produces `maiaedge-branded-doc.zip` (~2MB) containing SKILL.md + the complete asset tree (including the new Mode B `leavebehind/` files) + `references/messaging-framework.md`. Added the plugin folder (`plugin-manifest.json`, `.claude-plugin/plugin.json`, README) and the CLAUDE.md plugin-registry entry (10 -> 11).

Note: the plugin manifest bundles minimal `context` (just `core/messaging-framework.md`); the cheatsheet/101 generation mode runs on that plus the bundled `brand-reference.md`. The onepager + leave-behind modes route to additional context (use-case-taxonomy, competitive-positioning, proof-points, segment-messaging, etc.) that they read from the surrounding Cowork project. Expand the manifest `context` list if branded-doc needs to run those modes fully standalone.

## [1.5.0] - 2026-06-15

### branded-doc Mode B — the post-call leave-behind ("Recap & Path Forward")

Added a second mode to the `branded-doc` skill: a forwardable, post-call leave-behind a champion sends across their org to advance the deal (distinct from the outbound one-pager, which rides an accept/reply to GET a meeting). Designed from deep, sourced research on champion-enablement / buyer-consensus / objection-handling literature (Gartner buying-group, JOLT indecision, Force Management value framework, MEDDPICC, MAP best practice).

- **Structure** (flexible 1-3 pages, optional ~5-page business case for enterprise/high-ACV): exec summary → what we heard → why moving now beats waiting (cost-of-inaction, before any MaiaEdge capability) → the use-cases-we-mapped table (the centerpiece, with a "who it helps" stakeholder lens) → working through the open questions (objections, de-risked) → proof → per-stakeholder block → mutual action plan.
- **Data router:** composes on the `call-analysis` skill (use cases / pain / objections from `hs_call_summary`) + the contact-level MEDDPICC fields (`meddpicc_pain_contact`, `meddpicc_metrics_contact`, `meddpicc_criteria_contact`, `meddpicc_competition_contact`, `meddpicc_use_case`, `Champion`) + company/deal/contacts, each mapped to a section.
- **Audience-parameterized:** the rep names the audience at request time (champion / CFO / technical / full committee) and the doc tilts what leads + which proof shows up; the per-stakeholder block appears when it's "for the committee / to forward up."
- **Voice deltas (post-engagement, mid-cycle):** named references, case studies, and the credibility anchors are now ALLOWED (the inverse of cold); referencing the call is the point. KEPT: no em dashes, "carrier infrastructure" only, hard no-fabrication (every number labeled + ranged + input-grounded). NEW load-bearing rule from the JOLT research: the objection block DE-RISKS, it never re-sells the upside or re-establishes urgency.
- **Build:** flexible markdown via the main `build.py` (not a gated render), with a VERIFY-BEFORE-SEND checklist since there is no `qa.py`. New files in `skills/branded-doc/assets/leavebehind/`: `leave-behind-guide.md`, `template.md`, `example-northgate-colo.md` (illustrative). Mode B section added to `SKILL.md` + frontmatter triggers.

## [1.4.9] - 2026-06-14

### Repo refresh: segment-messaging sync, skill-reference fixes, branded-doc bundling, manifest hygiene

Final pass to reconcile the repo to the post-Wave-2 spec so every skill, plugin, and enterprise project operates on the current content.

- **segment-messaging.md sync.** The condensed copy-strategy companion lagged the Wave 2 cheatsheet angles. Rather than re-paste prose, extended the file's own **Structural-Truth Banks** mechanism with the genuinely-new June-2026 angles: Fiber capital-discipline + bubble-hedge; Colo inference-geography + margin-compression; NeoCloud time-to-power + provider-survival; Network-op AI-east-west-leads + margin-pincer + Atlantic-2027; MSP AI-whitespace + white-label; Enterprise BPO-jurisdictional. Also added the missing Enterprise row (`REDUNDANT | SOVEREIGN | AUTOMATED`) to the Pillar Framework table. All additions em-dash-free.
- **Skill context-reference fixes (audited all 29).** `company-enrichment/SKILL.md` named five files that were consolidated away (`D3-segment-flowchart.md`, `D5-sub-segment-protocols.md`, `D7-escalation-protocol.md`, `anchor-accounts.md`, `tiebreakers.md`, plus inline `working/tiebreakers.md`); repointed to the real homes (`enrichment-protocols.md` §6/§7, `sub-segment-qualification-full.md` §6, `d3-disambiguation-flowcharts.md`). `copy-strategist/SKILL.md` now references `context/outreach/voice-gold-standard.md` (the craft-voice register it adjudicates against). The other 27 skills were clean — the recent additions (`outreach-signal-pushback.md`, the competitive-positioning refresh, the segment angles) are already correctly wired.
- **branded-doc now actually renders from its projects (the real gap).** Every build path bundled only `SKILL.md`, so the skill's runtime payload (the WeasyPrint renderer `build.py`, `brand.css`, 9 Tomorrow fonts, `cover-template.html`, logos, icons, 3 SVG diagrams, and the whole `onepager/` render+QA system) shipped nowhere — the SKILL.md's `assets/...` relative paths resolved to nothing. `build.sh` now copies the branded-doc `assets/` tree (minus Python cache) into `branded-content/upload/assets/` and `general-assistant/upload/assets/`, so those projects can produce PDFs. Documented in the branded-content manifest.
- **Plugin + enterprise hygiene.** Reconciled `linkedin-network-builder` version (manifest `1.1.0` → `2.0.0` to match its `plugin.json`). Added the live `warm-follow-up` skill to the sales-outreach + founder-outreach manifests (it was missing from the upload instructions). Added a **"source of truth: upload the built `upload/` folder"** note to all 9 enterprise manifests so per-file enumeration drift can never cause an incomplete upload (the build is authoritative — verified zero missing-file warnings, all 29 skills in the instance bundle, all manifest `context`/`static` paths resolve).
- **Hygiene.** `.gitignore` now excludes `__pycache__/` + `*.pyc`; removed a stray tracked `build.cpython-310.pyc`.

## [1.4.8] - 2026-06-14

### Segment positioning audit — Wave 2: additive June-2026 angles (all 6 ICPs)

Second wave of the positioning audit. These are **supporting angles that ladder up to the existing pillars and master pitches** — no pillar, master-pitch, sovereignty, or banned-phrase rule changed. They give the existing positions June-2026 specificity (fresh why-nows, a named competitor, sharper registers). Three are intentional emphasis adjustments (flagged below), approved by Cooper. Every added cold example line was voice-checked (no em dashes, no colons/dashes-as-punctuation in outreach copy, problem-first, speed paired with ownership, anonymized proof in cold); internal-only stats are flagged "do not cite in cold."

- **Cross-cutting — the on-ramp incumbents became compute competitors.** Updated `competitive-positioning.md` from the dated "Megaport/Latitude.sh (2024+)" note to the June-2026 reality and split it precisely: **Megaport BUILDS compute** (A$827M raise, Latitude.sh, bare-metal GPU, AIx) vs **Equinix BROKERS compute** (Distributed AI Hub / Fabric Intelligence / Geo Zones). The "independence vs. tenancy" counter-frame (you're the landlord, not a tenant) was already doctrine — this refreshes its facts and adds the Equinix mechanism. Cold copy stays generic ("third-party fabric providers"); names are live-only.
- **Neocloud:** power-scarcity bridge ("Time to Power" — best-effort paths hand back the capacity you waited out the grid queue for); Megaport flagged as competitor where the repo only cited it as validation; provider-survival-diligence angle (owning + proving the path is how a neocloud answers its enterprise buyer's durability check); anchor refresh (Fireworks ~$15B, Baseten ~$11B, Together $305M, Nscale Rubin/Portugal; Lambda IPO softened to speculated).
- **Colocation:** competitive thesis split (above); inference-geography wedge ("inference lands in your metro, not the cheap-power markets — but only deterministic paths keep the tenant"); rack-density refresh (~130kW+ today, 600kW by 2027); US GRID-Act domestic-regulatory angle; margin-compression CFO/CRO P&L frame.
- **Fiber:** capital-discipline angle (66% of operators slowing builds → monetize the fiber already in the ground); bubble-hedge for long-haul/dark-fiber (capital-light AI interconnect); M&A relevance-bridge refreshed off the stale Aug-2024 "93%" stat; enterprise-pull cloud-on-ramp evidence. Guardrail held: defensive register is segment-specific, tailwind preserved for wholesale/dark-fiber.
- **Network Operator (adjustment):** **AI east-west / federation promoted to the lead; the two-track A/B framing demoted to a tone layer** (it calibrates how you say it, not the reason to meet — the category leader's own $12B-vs-$58B north-south/east-west TAM is the why-now). Plus Pure-Wholesale margin-pincer, Atlantic-2027 subsea crunch hook, DriveNets/hyperscaler-resale bridges, and Mplify "AI federation" as RFP-alignment proof (live, not cold).
- **MSP/Aggregator (adjustment):** **carrier threat reframed from "abandonment" → "out-automation/commoditization"** (carriers are doubling down on the mid-market channel while commoditizing the resale layer — the fear is "your quote looks identical to everyone else's," not "the carrier left you"). Plus the AI-connectivity whitespace wedge, per-seat-economics-breaking, white-label monetization, stale-fact refreshes (ScanSource Q3 FY26, Telarus 58/13 attribution, AppDirect→PartnerStack), and the asset-light copy-rule reconciliation ("a layer you own and bill," never "infrastructure you build"). Flagged: TSD sub-segment has 0 CRM records (RevOps sourcing action), Master Agent is a dead category.
- **Enterprise (adjustment):** **BPO/Outsourcing rebased off "per seat"** onto jurisdictional-path-proof (RBI April 2026) + uptime-as-margin + nearshore activation (the seat premise is eroding under AI). Plus distinct per-vertical why-nows (FS: carrier-consolidation-invalidates-diversity + DORA names connectivity/colo in CTPP scope; Healthcare: AI-imaging inter-DC bandwidth; Retail: PCI v4.0.1 11.4.7 pen-test + robotics-DC bring-up), the GenAI cross-cloud egress angle, and the Cloudian repatriation-stat refresh.

Open follow-ups (not yet done): sync the condensed `copy-strategy/segment-messaging.md` per-segment rows to match the cheatsheet additions (cheatsheets are the canonical home; the condensed file lags); RevOps TSD sourcing pass; neocloud GPU-pricing source reconciliation carried from Wave 1.

## [1.4.7] - 2026-06-14

### Segment positioning audit — Wave 1: verified correctness fixes

First wave of a six-segment positioning audit (deep market research across all 6 ICPs + 30 sub-segments, June 2026). The headline finding is that the segment library is genuinely current and on-thesis; this wave lands only the factual corrections that primary-source verification confirmed, with zero change to voice, caps, or positioning doctrine. Additive angles (competitor framing, per-vertical why-nows, defensive/AI-demand register) are staged for later reviewable waves.

- **Core Scientific (neocloud):** the "rejected a $9B buyout offer to stay independent (March 2026)" framing was wrong. It was *CoreWeave's* ~$9B all-stock offer, voted down by Core Scientific shareholders; merger terminated Oct 30, 2025. Corrected in `B-and-C-neocloud.md` (anchor list + crypto-to-AI pressure-test). Classification (landlord → `AI Signals - colo`) unaffected.
- **California AB 749 (enterprise/healthcare):** removed everywhere it was cited as a live healthcare device-microsegmentation mandate. It is a *dead state-agency* zero-trust bill (held on suspense, never enacted) — a factual liability. Re-anchored on OCR ransomware consent orders (April 23, 2026) whose corrective action plans require network segmentation, asset inventory, and ePHI data-flow mapping. Fixed in `enterprise.md`, `enterprise-use-cases.md`, `enterprise-signals.md`, `B-and-C-enterprise.md`, `use-case-taxonomy.md`.
- **HIPAA Security Rule NPRM (healthcare):** reframed from "rule is coming / mandates TLS 1.3" to "NPRM not finalized as of mid-2026; OCR enforcing segmentation via consent orders now." TLS 1.3 → TLS 1.2+ (matches NPRM text). Same files as above.
- **Carrier consolidation (enterprise FS):** updated to closed-deal language with dates (Verizon/Frontier Jan 20, AT&T/Lumen consumer fiber Feb 2, Zayo/Crown Castle Fiber May 1, 2026).
- **Aqua Comms (network operator subsea):** corrected the acquisition year (was "2024" → EXA completed Dec 31, 2025, ~$46M distressed). Demoted from lead subsea anchor; promoted Seaborn Networks (verified-active independent) as the primary anchor. Fixed in `enrichment-protocols.md` and `network-operator.md`.
- **EU AI Act (neocloud sovereign):** softened "fully enforceable August 2026, fines up to 7%" — the Digital Omnibus (provisional agreement May 2026) deferred the high-risk (Annex III) obligations to December 2027. Sovereign urgency now leads on data-residency demand + sovereign-RFP premiums, not a contested fine deadline.
- **Enterprise pillar canon:** resolved a single-source-of-truth contradiction — `segment-messaging.md` §7 said `REDUNDANT | DETERMINISTIC | VISIBLE` while the master `messaging-framework.md` says `REDUNDANT | SOVEREIGN | AUTOMATED`. Standardized on the master; remapped the value-prop pillar tags (determinism→REDUNDANT, visibility/audit→SOVEREIGN, multi-cloud-unify + M&A-compression→AUTOMATED).

Pulled from this wave pending clean source reconciliation: the neocloud GPU-pricing "plateaued → sold out" refresh (sources conflict; the repo's current hedged framing is defensible).

## [1.4.6] - 2026-06-14

### Research-display doctrine refined — the why-now carve-out (Cooper)

Sharpened the "research is invisible" rule so it cannot read as "never name any fact" (which pushes copy toward generic / blend-in). Research is now **invisible by default, with one explicit carve-out**: a fresh why-now signal (funding round, award, M&A, senior hire, build milestone) may be named ONCE, as an observation ("Saw the X"), when it ties to the value prop and creates urgency. The bar for naming any fact: would removing it remove the urgency or break the tie to what we sell? Static stats (route miles, facility counts, geography) almost never pass and stay absorbed; events/signals often do. Even the fact that earns its place is named as an observation, never a possessive stat ("your $100M").

Updated canonical `email-writing-rules.md` (Research Absorption Standard + Research Display Detection + the $100M translation-table row, which now shows the observation path instead of dropping the fact) and synced the carve-out into cold-email, sdr-pipeline, and linkedin-outreach. This composes with the existing Public-Signal Observations rule and the Cited-Signal Cap (still max one cited signal in E1's opening two sentences). No other voice rule changed.

## [1.4.5] - 2026-06-14

### Phase B completion — role matrix, proof points, persona blocklist deduped

Finished the cross-skill dedup. Three small tables were duplicated across cold-email and sdr-pipeline and carried `<!-- Canonical source: ... -->` comments pointing at files that did not actually hold them. Each now has a real canonical home, and the false-canonical-claim is fixed:
- **Cross-Segment Role Pain Matrix** added to `context/copy-strategy/segment-messaging.md`; cold-email + sdr-pipeline point to it.
- **Anonymized Proof Points (for Cold Outreach)** added to `context/product/proof-points.md` (above the named customer stories, which stay live-conversation-only); cold-email + sdr-pipeline point to it.
- **Persona blocklist** quick-list condensed to a one-line bucket summary + pointer to `persona-targeting-blocklist.md` in all three skills.

**Research Receipt format intentionally NOT relocated.** It is the load-bearing anti-research-skipping gate, reinforced at the point of use by design; relocating it to a referenced file would weaken enforcement at the exact moment it matters. Point-of-use reinforcement is not bloat.

Cumulative skill trim across 1.4.3-1.4.5: cold-email 1048→912, sdr-pipeline 1016→922, linkedin-outreach 632→567 (~295 lines out of the three skills), with zero change to voice, tone, caps, banned phrases, or posture rules.

## [1.4.4] - 2026-06-14

### Email 1 Word Cap → 85-110 + Signal Push-Back Relocation (Phase B)

**E1 word cap raised to 85-110 words (Cooper).** Was 70-100, with a stale 70-85 still lingering in several files. Reconciled fleet-wide so no surface drifts: `email-writing-rules.md` (canonical), the cold-email / sdr-pipeline / copy-strategist skills, `messaging-framework.md`, `segment-messaging.md`, `scoring-rubric.md`, `outbound-playbook.md`, `account-brief-template.md`, the Cold-Outreach / Tradeshow / List-Builder project instructions, and the sales-outreach / founder-outreach / general-assistant enterprise prompts. E2 (under 55 words) and E3 (2-3 sentences) unchanged.

### Phase B — Signal Push-Back deduplicated to one canonical home

The ~65-line Signal Push-Back procedure (with its inlined `compute_signal_heat` block) was pasted near-verbatim into cold-email, sdr-pipeline, and linkedin-outreach. Relocated to a single canonical file **`context/signals/outreach-signal-pushback.md`**; each skill now carries a one-line pointer plus only its own delta (sdr-pipeline keeps its per-company cadence + batch rate-limiting + run-summary reporting). ~190 lines removed across the three skills with zero behavior change. The new file is bundled into `maiaedge-outreach` (1.6.0 → 1.6.1) and `maiaedge-sdr-pipeline` (2.1.0 → 2.1.1); `.claude-plugin/plugin.json` versions synced.

Open follow-ups: refresh the two cold-email worked examples (Fatbeam 71w / ATN 81w, now under the new 85-word floor); remaining Phase B relocations (Research Receipt format, persona blocklist, proof points, role matrix) and the Phase C voice-text consolidations (Enterprise guide, research-display) still pending.

## [1.4.3] - 2026-06-14

### Outreach Skills Cleanup (reliability + de-bloat, Phase A)

Audit-driven cleanup of cold-email, linkedin-outreach, sdr-pipeline. No voice, tone, word/char cap, banned-phrase, or posture rule changed — only correctness fixes, dated-fluff removal, and intra-file dedup.

- **Sender-territory bug fixed.** cold-email and sdr-pipeline had Tim Lieto's and Ken Cunningham's territories inverted (Tim shown as West, Ken as East), which would misroute sends. Corrected to Tim = East, Ken = West per CLAUDE.md. Root cause lived in the SSOT: `sender-profiles.md` listed Ken's title as "Sales, East Region" (territory West) — corrected to "Sales, West Region".
- **Dated changelog fluff stripped** from all three skills per the standing doc-hygiene rule. Rules kept verbatim; only audit-trail stamps ("went 0-for-584," "widened from 70-85 on 2026-06-12," "463 LinkedIn tasks," etc.) removed, with load-bearing reasoning reduced to one neutral clause.
- **cold-email duplicate receipts collapsed** — the Fatbeam + ATN Research Receipts were printed twice; the placeholder copies now point to the single full worked versions in the FULL EMAIL EXAMPLES section.
- **linkedin-outreach** Day-2 vs Day-(-3) reference reconciled to Day -3 (matches the body).
- `.qa-tmp/` scratch dir added to `.gitignore`.

Open follow-ups (not in this release): Phase B cross-skill relocation of the duplicated Signal Push-Back / `compute_signal_heat` / Research Receipt blocks to single canonical homes (~500 lines); reconcile the lingering E1 70-85 word cap in `segment-messaging.md` / `messaging-framework.md` / `outbound-playbook.md` to the canonical 70-100.

## [1.4.2] - 2026-06-12

### Outreach Punctuation + Say-The-Thing Hard Bans (Cooper)

Per Cooper 2026-06-12, outputs were reading as written-by-tool. Three new write-time hard bans for ALL outreach copy (email + LinkedIn, cold and warm), subject and body: **no colons** (a colon labels a reveal, deck-speak), **no dashes-as-punctuation** (spaced hyphen / double hyphen / en dash; hyphenated compounds like cross-connect stay fine; extends the existing em-dash ban), and **no move-announcing transitions** ("another angle on this," "one more thought," "quick thought," "worth a thought"). Just say the thing.

**Canonical:** email-writing-rules.md (Banned Phrases + § "Say the thing" + QA checklist). **Write-time:** voice-gold-standard.md hard bans #1 and #6 extended. **Reminders extended in:** cold-email, linkedin-outreach, sdr-pipeline, warm-follow-up, copy-strategist (scores move-narration as a voice failure), Cold-Outreach + Tradeshow project instructions, CLAUDE.md Key Rules. **Compliance fixes to imitation sources:** 3 voice-gold-standard exemplars minimally rewritten (Konnexx "two things:", Alaska Communications wall colon, OTAVA "The thing I'd ask about:"), FarmGPU exemplar annotated (its "Quick follow-up." opener predates the ban; imitate the body only), 3 fallback-messaging hook strings de-dashed (fiber, colo, neocloud aggregator), 4 in-skill example bodies cleaned (cold-email Meijer-style example, warm-follow-up INTEREST + OBJECTION examples, email-writing-rules E3 example). Writer-facing instruction text (angle-diversity rules, receipt labels, markdown headers) intentionally untouched.

## [1.4.1] - 2026-06-12

### Skill × Context Utilization Sweep (wiring fixes, no new knowledge)

Full both-direction sweep of skill↔context usage (report: `outputs/skill-context-utilization-2026-06-12.md`; companion structural assessment: `outputs/repo-structural-assessment-2026-06-12.md`). Verdict: the knowledge base is well-consumed and nothing is missing — the gaps were wiring. Fixed in this release:

**Latent files wired (had zero skill consumers):** `email-bot-supplemental.md` → cold-email + sdr-pipeline (AI-angle decision matrix); `ai-market-positioning.md` → cold-email + call-prep + account-brief; `edge-ai-thesis-montauk.md` → call-prep + account-brief; `marketplace-seeding-strategy.md` → account-brief + prospect-research (partnership-track); `research-routes.md` + `output-schemas.md` → company-enrichment / account-sourcing / edge-case-researcher; `ab-test-plan.md` → copy-strategist. icp-deep-dives exposed as optional read-on-demand background in account-brief + prospect-research (NOT plugin-bundled — 370KB). `golden-pitch-key-slides.md` deliberately left unwired (draft quality — complete or delete).

**Reference sections made explicit:** pipeline-analytics gains a Reference Files block (deals-schema, poc-schema, territory-model); account-brief gains the objection bank (competitive-positioning + differentiation-naas-aggregator) + territory-model; call-prep + use-case-taxonomy; sales-enablement + icp-playbook; contact-discovery + segment cheatsheets; sales-docs + pricing-reference.md as flagged fallback when `price_list.md` isn't uploaded.

**Plugin bundle holes closed (files skills cite but Cowork bundles lacked):** maiaedge-sales-support 1.1.0 → 1.2.0 (+9 incl. **differentiation-naas-aggregator.md — competitive-intel's declared single source of truth was never shipped**); maiaedge-sdr-pipeline 2.0.0 → 2.1.0 (+email-bot-supplemental, **+voice-gold-standard.md — the skill's "THE write-time page" was never shipped**); maiaedge-outreach 1.5.0 → 1.6.0 (+3 sales/product files); maiaedge-sales-docs 1.1.0 → 1.2.0 (+pricing-reference). `.claude-plugin/plugin.json` versions synced to manifests for all 9 maiaedge plugins (most were stuck at stale values). **Exception: linkedin-network-builder left as-is** — its plugin.json (2.0.0) is AHEAD of its manifest (1.1.0) and the file is write-protected; Cooper to decide which is canonical.

## [1.4.0] - 2026-06-12

### Warm Follow-Up Skill (reply/accept handling)

The cold skills only write into silence; nothing owned the message AFTER a prospect replied or accepted - the exact point where 56% of positive replies were dying before a held meeting (44% positive→held in the retro corpus). Cooper was hand-pasting threads and steering manually.

**New skill: `skills/warm-follow-up/SKILL.md`** - the next message in an active thread, both channels (email + LinkedIn), one shared move map. Input is the thread itself; no Research Receipt (research happened at cold time) - replaced by a REQUIRED Activity Scan (HubSpot contact engagements/notes/owner + company deals/calls/signal fields/brief + Smartlead message history; leverage at most ONE found item, never fabricate, never block on MCP) and a Thread Receipt hard gate (what we sent / what they did / reply class / activity leveraged / contact state / the ONE new thing / must-not-repeat). Nine reply classes → moves: ACCEPT (thank-you DM + one-pager play), INTEREST (three specific times, zero new pitch), QUESTION (answer-then-advance from the doctrine's written register), OBJECTION (concede-what's-true + one mechanical distinction), DEFERRAL (anchor THEIR window + HubSpot task), REDIRECT (warm-intro ask), SOFT NO (door-open + suppress), WENT QUIET (one ≤40-word nudge, then stop), AUTO (not a reply). Non-redundancy gate spans BOTH channels (LinkedIn + email = one conversation). **Cooper locks baked in: NO credibility anchors in writing ever (live spoken calls only) and NO pricing in writing ever** - a pricing question is answered with the meeting, not a number. Federation-mechanics questions route to the do-not-improvise guardrail (verified consent/topology/telemetry facts only) and convert into the escalation give ("20 minutes with the person who designed it"). Logging: reply/one-pager/meeting-proposed notes + deferral tasks via HubSpot MCP; NO signal push-back, NO `last_enriched_date` bump.

**voice-gold-standard.md §E** - placeholder replaced with the warm bar: Cooper's three house-validated post-accept thank-you DMs (E2E Networks, Nscale, new-in-seat exec) with why-it-works annotations. The anatomy they encode: "thanks for connecting" open → one-pager as thinking, not collateral → connect angle restated compressed, never pasted back → close calibrated to contact state (escalation give / no-rush / neutral-soft).

**Pointer edits:** cold-email + linkedin-outreach Warm Contact Handling sections now distinguish warm TARGETING (pre-first-touch, stays in those skills) from reply HANDLING (warm-follow-up); both Skill Chains route "on any reply or accept" to the new skill; Cold-Outreach-Project-Instructions notes replies are processed with warm-follow-up, never by re-running cold copy.

**Wiring:** maiaedge-outreach plugin 1.4.0 → 1.5.0 (adds warm-follow-up + four context files the outreach skills already referenced but the plugin never shipped: voice-gold-standard.md, pre-cadence-hygiene.md, outbound-playbook.md, differentiation-naas-aggregator.md). **sdr-pipeline untouched - cold-only by design.** build.sh upload-name map + instance-skill comments updated.

## [1.3.0] - 2026-06-12

### Segment Knowledge Refresh + NaaS/Aggregator Differentiation Doctrine

Research-and-update run: 7 research agents (one per segment + one differentiation deep-dive, 200+ dated sources), HubSpot call-transcript mining, and a file-by-file audit. Full evidence + per-claim sources + OPEN QUESTIONS: `outputs/segment-refresh/2026-06-12-gap-report.md`. Driver: fiber operators pattern-match the "extending ethernet" pitch to NaaS/aggregators and kill the conversation ("we already have partners for off-net"); secondary, every segment file now reflects June 2026, not its write date.

**New file: `context/core/differentiation-naas-aggregator.md`** — single source of truth for the NaaS/fabric/aggregator/exchange lines. The operator's mental map (the four boxes we get filed in), the mechanical truth table (DIY NNI vs join-a-fabric vs aggregator vs MaiaEdge — every MaiaEdge cell verified against product files), a concede-the-fabric section, the sanctioned June 2026 catalyst (Megaport raised A$827.3M ≈ **US$594M** on June 3 to build a distributed GPU inference cloud — resolves the internal $600M-vs-$800M conflict: $800M was the AUD figure; say "close to $600M (US)" or "an $830M Australian raise"), 8 objections in three registers each (cold-safe / live-call / one-liner), honest win/lose routing, a claims-to-avoid guardrail (12 unverified federation mechanics → OPEN QUESTIONS for Kyle/Abilash), and the vocabulary that keeps us out of the wrong box.

**Fiber rebuilt as the flagship:** fiber-operator.md gains an "Ethernet Extension: How Their Off-Net World Works Today" section (serviceability → rate card/ICB → FOC date → turn-up at the ENNI, in their words; the extension story told with verified objects — a PBC each end over DIA, the consented partner leg, never noun-stacks; the NaaS-confusion trap with trigger-words to avoid), a rebuilt industry landscape (closed-deal consolidation list + FiberCo/anchor-tenant wave, restructured BEAD + $21B non-deployment limbo, NEW copper-retirement wholesale shock, NEW LSO-Sonata/Connectbase asymmetry — "the order automates; the path doesn't"), corrected figures (AI-DC fiber 36x → ~10x, strands 144-432 → 864-1,728, capex $600B → ~$527B), and anchor ownership updates. fiber-signals.md adds F-A10 (operator joins/resells a fabric — two-window firing) + F-C6 (copper-retirement exposure) and purges dead transcript sources.

**Vocabulary research verdicts wired into copy files:** validated — off-net, Type 2, rate card, turn-up, ENNI/E-Access, FOC date, install interval, serviceability, order fallout. KILLED — "peer handoff," "turn-up clock," "quotable reach," literal "on a partner's clock" ("margin stays home" = our coinage, usable but not insider-proof). segment-language.md gains the fiber off-net lexicon, a NEW Enterprise insider-voice section (the file had none), a June-2026 currency block for all six segments (incl. "neocloud is the market label — call prospects what they call themselves" and "master agent is dead"), and the plant-contradiction fix. segment-messaging.md structural-truth banks gain 18 trend-derived truths (Sonata asymmetry, copper deadline, fabric-becomes-competitor, attach-rate-on-earnings-calls, Omdia audit, tokens-per-watt, order-automates-path-doesn't, recap-wave-validates-owned-assets, Geo-Zones rent-vs-own, headcount squeeze, dated audit cycle), plus the doctrine pointer and a verified Rule 9.

**All six cheatsheets refreshed to June 2026** (trend blocks + factual corrections, not company dossiers): colocation (NoVA 0.5%, ~$130B opposition, half-of-2026-builds delayed, named Megaport pivot + "deployment gap," inference-flip proof), neocloud (pricing plateau + consolidation, inference ~60-70% NOW, debt wall re-sourced ~$662B, NEW Omdia-audit section — 50 neoclouds, 1-in-5 single-homed, Lightning AI + Fluidstack anchor fixes, last craft-voice violation fixed), network-operator (Lumen PCF $78M Q1 revenue + Alkira $475M buy — "the market just priced build-your-own-control-plane," US-Sonata claim corrected, subsea scarcity flip, Aduna federation existence-proof), msp-aggregator (Master Agent anchor pool EMPTIED — X4 Sandler-owned since 2016, CyberNet misclassified; Nitel→Comcast; NEW 2026 Market Reality section: recap wave, carriers-buy-aggregators, asset-light over-correction lifted, the supplier-desk trap — "not asking to be supplier #401"), enterprise (EU AI Act partial-postponement correction — transparency Aug 2026, high-risk pushed to Dec 2027/Aug 2028; dated domestic audit cycle; Equinix Geo Zones rent-vs-own counter; selective-rebalancing block). Two B-and-C factual fixes (stale Greenfield-archive recommendation voided; Trinity Health entity mix-up). competitive-intel SKILL now leads its references with the doctrine file and adds an aggregator/TSD section.

**Flags for Cooper:** `maiaedge.ai` is NOT a MaiaEdge property (domain-for-sale listing — brand decision needed); 16 OPEN QUESTIONS in the gap report (12 product-mechanics for Kyle/Abilash incl. inter-operator settlement, far-leg provisioning, federated SLA recourse, pre-partner quotability; 4 commercial/messaging for Cooper). HubSpot untouched (read-only run); scoring models, tier specs, and the 30-value enum untouched per locked architecture.

## [1.2.0] - 2026-06-12

### Craft-Voice Cold Rework (from the 2026-06-11 outbound retrospective)

Full retro at `outputs/outbound-retro/2026-06-11-campaign-retro.md` (4,614 sends analyzed; 18 positives, 16 event-anchored; June anchor-less fleet 0-for-584; sanctioned rule-file strings shipping as batch stamps at up to 100% density). Cooper directive: cold copy must convert WITHOUT events; kill the robotic register.

**New file:** `context/outreach/voice-gold-standard.md` — THE write-time page: gold exemplars (Cooper's three flagged LinkedIn messages, reply-validated emails, craft-structure E1s) + 8-item hard-ban shortlist. Writers imitate exemplars; all other rule files move to pre-write pipeline or post-write QA.

**Craft-Voice register (canonical in email-writing-rules.md § Craft Voice):** structural truth of the reader's world (competence credited, never company diagnosis) → craft line ("that handoff leg is the layer I work on" + one concrete mechanic; replaces "We've been helping similar teams…" as default, now capped ≤1/account) → ONE close from three classes: give-close (demo offer fused into a single ask — "fifteen minutes and I'll show you the whole thing end to end, whenever works on your side"; live demo confirmed ready), soft call-ask statement, or honest-reason close. The give IS the close, never stacked with a second ask (Cooper, 2026-06-12). One-pagers are post-engagement only (after LinkedIn accept or reply), never a cold-E1 give. Yes/no thought-question closes BANNED (0-for-28 in June). Zero-ask E3 closers BANNED. E1 cap 70-85 → 70-100. Question subjects allowed for cold. All string menus converted to paraphrase-mandatory patterns.

**New gate:** Batch Fingerprint Gate (email-writing-rules.md; programmatic Step 9.5 in sdr-pipeline) — no closing string >20% of batch or twice per account; no 8-gram repeats within an account; ≥3 opener patterns per 10; no exemplar/rule-file phrase shipped verbatim. Scoring-rubric Dimension 12 (Batch Distinctiveness, PASS/FAIL).

**Channel orchestration (outbound-playbook):** LinkedIn connect moves to Day −3 (craft voice, from reps/co-founders — no SDR register exists in this motion); accept → thank-you DM + account one-pager (logged: accept → `linked_in_message`, delivery → note); email carries the meeting ask; same-account E1s staggered ≥48h; account-stop on any unsub/reply; propose-3-times on hot replies (validated).

**Files changed:** email-writing-rules, cold-email SKILL, sdr-pipeline SKILL, linkedin-outreach SKILL (craft default + char-count emission + logging), sender-profiles (craft registers per sender; no-typed-sign-off aligned; founder cold-lane pending), fallback-messaging (exemplars-not-strings; Fiber E1 craft conversion; E3 asks), scoring-rubric, outbound-playbook (house baselines: 1.2% human reply / 0.93% positive / 44% reply→meeting; targets 2-3% human on craft cold), Cold-Outreach-Project-Instructions (prescribed CTA strings retired), ab-test-plan (Wave 1: craft vs current, 150/arm), segment-messaging (structural-truth banks + Tier 1 Inference path-to-user correction).

**Campaign A (Neocloud campaign folder):** run prompt updated to craft register + pre-send fix protocol; `Campaign A - PreSend Fix Audit.md` (162 LinkedIn requests over the 280 cap, Omdia opener on 100/152 E1s, 25/28 accounts sharing 8-grams, wave splits for 11- and 25-contact accounts); `REWORKED SAMPLE - Cirrascale.md` is the bar.

## [1.1.0] - 2026-04-17

### Messaging Rework: April 2026 Deck + Neocloud-Colo Shift Brief + Montauk Thesis

New source of truth for messaging across outreach, account briefs, and live sales motion. The April 2026 deck supersedes prior V4.1 framework where conflicts exist.

**Neocloud angle by maturity (NEW):**
- Added "Neocloud Angle by Maturity" framework to context/segments/neocloud.md: pre-revenue / single-site (watch list), early growth 2-5 sites (current angle), mid-growth 5-15 sites (both angles), scale 15+ sites hyperscaler-heavy (scaling-wall angle, new).
- Added scaling-wall persona leads (CEO, CTO, VP Infra, CFO, VP Sales/BD) and opening hooks ("The first 5 hyperscaler contracts didn't need a network team. The next 40 enterprise customers will.").
- Replicated into context/copy-strategy/segment-messaging.md and context/outreach/fallback-messaging.md so cold-email, linkedin-outreach, sdr-pipeline, and account-brief skills consume the same angle tree.
- Updated context/sales/neocloud-strategy-brief.md: demoted observability from universal lead to supporting benefit under DETERMINISTIC; added in-pain-now vs. scaling-wall persona leads; added Large-Scale GPU default angle = scaling-wall.

**Montauk Capital "Last Millisecond" thesis integrated:**
- Added context/sales/edge-ai-thesis-montauk.md: full internal reference on how to use agentic compounding latency (10 hops = tens of seconds of lag), metro-edge deployment model, sovereign edge thesis across neocloud / colo / fiber / network-operator segments.
- Wired into build.sh for sales-outreach, founder-outreach, call-intelligence, crm-guardian enterprise projects. Added to maiaedge-sales-support plugin manifest.
- Layered agentic compounding latency framing into context/product/ai-market-positioning.md Executive Summary (three-trend structure).

**Credibility anchor rule clarified (BANNED cold, ALLOWED live):**
- Previously: "banned in cold emails, allowed in live objection handling only."
- Now: BANNED in cold email and LinkedIn. ALLOWED in live presentations, demos, proposals, and objection handling.
- Rationale: April 2026 deck uses Andy Ory / Acme Packet / 128 Technology credibility on slides 3 and 16 — that is live-presentation context, not cold outreach.
- Updated across: colocation.md, fiber-operator.md, network-operator.md, msp-aggregator.md, neocloud.md, messaging-framework.md, email-writing-rules.md, segment-messaging.md.

**Federation language enforcement (BANNED in customer-facing writing, including partnership collateral):**
- Fixed violations in network-operator.md ("Federation is the asset-light answer" → "Cross-carrier partnerships are the asset-light answer"; "out-federate them" → "out-partner them").
- Fixed msp-aggregator.md ("federated partnerships" → "upstream partnerships"; "federated upstream partners" → "robust upstream partner access").
- Fixed fiber-operator.md ("sovereign, federated alternative" → "sovereign middle-mile alternative with cross-carrier partner reach").
- Clarified marketplace-seeding-strategy.md: document is internal GTM; added translation guidance for operator-facing materials.
- Fixed cloud-onramp-business-case.md segment table ("federate with a partner" → "partner with another operator", "via federation" → "via cross-carrier partnerships").
- Rationale: April 2026 deck uses "Federated" as a live-presentation pillar header (slides 8, 13). Cold outreach and written derivatives still translate to segment-native language.

**Sovereignty must be qualified in writing:**
- Added rule to segment-messaging.md and messaging-framework.md: never use "sovereign" as a bare attribute in writing. Always pair: "sovereign by design," "sovereign routing," "sovereign middle-mile," "provably private."

**Colo additions from deck:**
- Added GPU Tenant Readiness angle (standard colo, when AI corridor / GPU tenant signals present) and AI Colo category positioning (live-only, CEO-level strategic frame — not cold email) to segment-messaging.md and fallback-messaging.md.

**Cloud on-ramp deployment models formalized:**
- Added four deployment models (Private Wavelength, DIA, Partnership, Full Marketplace) from the April 2026 deck to context/product/cloud-onramp-business-case.md. Replaced single-paragraph deployment description with explicit model table and guidance per model.

**Competitive sharpening:**
- Added rule (cross-segment): third-party fabric providers now sell GPU compute directly. Every tenant/enterprise customer sent to their portal discovers a competitor. Cold email still uses "third-party fabric providers" — but now that framing carries competitive weight, not just relationship risk.

**Version stamps:**
- messaging-framework.md bumped to V4.2 (April 2026), with V4.2 changelog section.

**Sovereign AI / neocloud messaging patterns integrated:**
- Extended Sovereign AI Clouds sub-segment in context/segments/neocloud.md with trigger signals (GAIA-X, EU data residency, regulated-industry customer base), a "when NOT to use sovereign angle" callout (US neoclouds swap to deterministic paths + egress; Tier 1 carriers with own backbone, fit is thin), compute-vs-connectivity reusable framing, and new opening conversation lines.
- Added Value Prop Matrix row in context/copy-strategy/segment-messaging.md under the PRIVATE pillar ("Every hop logged, every path controlled") plus a new "Sovereign-Angle Variant" subsection with when-to-use / when-NOT-to-use guidance and reusable lines.
- Added self-framing vocabulary ("compute is multi-tenant but the connectivity isn't"), new Insider vs Outsider pair for European sovereign GPU clouds, and variant vocabulary additions in context/copy-strategy/segment-language.md.
- Added 2 new Board Meeting Language lines to neocloud.md insider bank.

**Outreach behavior tightening (research sequence, diplomacy, reply-worthiness):**
- Added Research Sequence rule to context/outreach/email-writing-rules.md: research runs as three explicit stages (company, then contact, then tailor) and cannot be collapsed. Prevents lazy contact-level angle selection.
- Added Diplomatic Claims section: no absolutes, no prescriptive musts, no definitive diagnostics about their business the sender cannot know. Hypothesis language and relational framing only for claims about their business. Claims about our category direct but not grandiose.
- Reworked the Human Test into a two-question gate: "would a real person write this" AND "would THIS specific person want to reply."
- Added new Dimension 11 to context/copy-strategy/scoring-rubric.md: "Claim Diplomacy & Reply-Worthiness" (5% weight). Rebalanced: Speaks Their Language 18 to 16, Brevity 7 to 5, Credibility Anchor 5 to 4 to make room.
- Propagated the tightening into skills/cold-email/SKILL.md, skills/linkedin-outreach/SKILL.md, skills/sdr-pipeline/SKILL.md (new Step 7b contact-level tailoring with per-role example), and skills/copy-strategist/SKILL.md (new second-pass diplomacy filter and third-pass contact-tailoring filter in the critique workflow).
- Cleaned 3 pre-existing em dashes in scoring-rubric.md while editing.

**Geographic / Transport-Gap angle variant (island-hopping, multi-transport carriers):**
- Added new cross-segment variant to context/copy-strategy/segment-messaging.md: for carriers whose geography forces them past fiber (Caribbean, LATAM, archipelago regions, mobile backhaul at scale, multi-transport mix). Default angle "provisioning is slow" is replaced with "extend deterministic Layer 2 services anywhere, over any available transport, even where fiber isn't."
- Includes trigger signals, when-NOT-to-use (mainland dense-fiber carriers; Tier 1 with own subsea backbone), 5 reusable lines, value bridge, anonymized IENTC-pattern proof reference.
- Cross-references added in the Fiber Operators and Network Operators sections of segment-messaging.md.
- Variant vocabulary added to context/copy-strategy/segment-language.md plus a new Insider vs Outsider pair showing the angle reframe (outsider: "provisioning is slow"; insider: "fiber isn't everywhere you serve, microwave today satellite for the next archipelago, same paths either way").

## [1.0.0] - 2026-03-17

### Initial Repository Creation
- Consolidated all context files into `context/` (single source of truth)
- Consolidated all skills into `skills/` (21 canonical SKILL.md files)
- Created plugin packaging in `plugins/` (7 plugins with manifests)
- Created enterprise project manifests for 5 Claude.ai Projects
- Retired `maiaedge-sales` plugin (unique skills promoted to standalone)
- Fixed stale SDR Pipeline references (messaging-framework.md, email-writing-rules.md)
- Extracted unique V2 bot content into context files:
  - NEW: context/hubspot/deals-schema.md
  - NEW: context/sales/pricing-reference.md
  - NEW: context/sales/marketplace-seeding-strategy.md
  - UPDATED: sender-profiles.md (added founder voices)
  - UPDATED: maiaedge-101.md (added exec team bios)
  - UPDATED: territory-model.md (added Kyle Blackwell, Woody Acosta)
  - UPDATED: proof-points.md (added IENTC reference details)
  - UPDATED: competitive-positioning.md (added Lumen PCF/AWS threat)
- Created build.sh for automated plugin assembly
- Created CLAUDE.md for Claude Code integration
