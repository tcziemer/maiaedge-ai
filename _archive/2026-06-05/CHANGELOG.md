# Changelog

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
