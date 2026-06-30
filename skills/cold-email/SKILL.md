---
name: cold-email
description: Write cold outreach emails for MaiaEdge prospects. Use when asked to write, draft, or create a cold email, outreach email, or prospecting email for MaiaEdge. Requires prospect research and segment classification first. Sender is determined by territory per context/hubspot/territory-model.md.
---

# MaiaEdge Cold Email Writer

## Hard Gate Before Writing

Emit a complete **Research Receipt** (format in the Research Receipt section) for each contact before writing that contact's email body. The Receipt requires literal search query strings that were actually run, paired with results: minimum 3 if claiming a cataloged signal, minimum 5 if claiming NONE. A contact-level finding is required on every Receipt.

No Receipt above the email body = invalid output. Run the searches, then write.

## Goal

Get a reply. Not close a deal. Not deliver a pitch deck. Just start a real conversation between two professionals who should be talking.

## Clarification

Two things help land the angle:
1. Who is the prospect - company, segment (colo / fiber / network op / neocloud / MSP / enterprise), and contact role/title? A HubSpot link or recent news speeds things up.
2. Which email in the sequence - E1 (first touch), E2 (follow-up, different angle), or E3 (final)?

Drop the company name and whatever you have - the skill researches HQ location, territory, and sender from context/hubspot/territory-model.md.

## Reference Files

When deployed in a project with reference files, also read:
- **context/outreach/voice-gold-standard.md**  -  **Hold open WHILE writing.** The exemplar set (the Cooper-flagged LinkedIn bar, reply-validated emails, craft-structure E1s) plus the 8-item write-time hard-ban shortlist. Imitate the register; never reuse exemplar phrasing verbatim. Everything else below runs BEFORE writing (research/gates) or AFTER (QA).
- **context/copy-strategy/segment-language.md**  -  **Read first.** Insider vocabulary, daily reality, conversational patterns per segment. This is how you sound like a 15-year industry peer, not a salesperson who read their website.
- **context/outreach/email-writing-rules.md**  -  Core email philosophy, angle-first principle, structure, segment lock, banned phrases
- **context/copy-strategy/segment-messaging.md**  -  Per-segment value-prop matrices, persona tables, embed-by-contrast templates. **Section 5 (Network Operators) is split into Tier 1 (Global + National) vs Tier 2/3 Regional Wholesale lead motions** - see "Network Operator Tier Selection" below.
- **context/core/messaging-framework.md**  -  Segment messaging rules, cloud on-ramp use cases, language rules
- **context/outreach/fallback-messaging.md**  -  Per-segment fallback E1/E2/E3 templates. Colocation is split into Standard (no AI signals) and AI Infrastructure (Lambda/Crusoe/Nebius tenants, liquid cooling, 30kW+ racks).
- **context/outreach/persona-targeting-blocklist.md**  -  **Pre-write gate.** Titles excluded from standard SDR cadence (Director-Carrier-Wholesale, Director-Field-Operations, Country-Manager-at-HQ-product-org, Account Executive, CSM). See "Persona Pre-Check" below.
- **context/outreach/pre-cadence-hygiene.md**  -  **Pre-write gate.** Three list-hygiene filters (auto-bounce/autoresponder detection, OOO detection, LinkedIn-status check) that run before any contact enters the cadence.
- **context/outreach/sender-profiles.md**  -  Sender identities, voice characteristics, signature protocol
- **context/hubspot/territory-model.md**  -  Authoritative 5-region sender routing map. Read before selecting a sender. See "Active Senders" below.
- **context/core/icp-playbook.md**  -  Worked per-segment examples and persona pain points; use alongside segment cheatsheets for angle selection.
- **context/core/differentiation-naas-aggregator.md**  -  Cold-safe NaaS doctrine for competitive framing and orphaned competitive bullets.
- **context/europe/europe-email-compliance.md**  -  Hard legal gate: cold email to DE/AT/IT contacts is unlawful without opt-in. Read before writing any European contact.
- **Segment cheatsheets** (context/segments/colocation.md, context/segments/fiber-operator.md, context/segments/neocloud.md, context/segments/network-operator.md, context/segments/msp-aggregator.md, **context/segments/enterprise.md**)  -  Deep segment context for pain points and competitive landscape
- **context/signals/signal-framework.md**  -  Universal signal types (U1-U6), Apollo signals (AP-1 to AP-7), free signals (FR-1 to FR-3), scoring model, noise list. Required for the Public Signal Cited rule.
- **context/signals/[segment]-signals.md**  -  Per-segment cataloged signals (e.g., fiber-signals.md has F-A1 through F-A7 Tier A signals, plus F-B and F-C tiers). The Pattern: field for each cataloged signal becomes the actual web search query when grounding emails. Required reading for the segment being targeted.
- **context/sales/email-bot-supplemental.md**  -  AI Signal Strength table + decision matrix for WHEN to use AI messaging, plus market-size proof points. Read when the prospect is a neocloud, AI-signals colo, or carries GPU-tenant / liquid-cooling / AI-buildout signals - it decides whether the AI angle is earned or forced.
- **context/product/ai-market-positioning.md**  -  AI-inference positioning: latency as the bottleneck, deterministic paths, the network layer for distributed AI. Read alongside the above when writing the AI angle for neocloud / AI-colo prospects.
- **context/account-tiering/sub-segment-qualification.md**  -  Authoritative list of the 30 active `company_sub_segment` values. Use the exact case-sensitive HubSpot string for any sub-segment reference in research notes, voice guides, or written copy.
- **context/account-tiering/enrichment-protocols.md**  -  Field-by-field enrichment rules. Read for the canonical definitions of `account_brief`, `recent_news_or_trigger_event`, `fabric_provisioning_approach`, and `geographic_focus` - the four enriched fields that ground the cold-email angle in real prospect substance.
- **context/signals/outreach-signal-pushback.md**  -  Canonical procedure for the Final Step signal push-back to HubSpot after email delivery.

MEDIUM reference (load when relevant):
- **context/core/competitive-positioning.md**  -  Competitive landscape; use for context when the email touches a competitive angle.
- **context/signals/universal-platform-signals.md**  -  AP-series universal signals (AP-1 to AP-7) for prospects with no segment-specific cataloged signal.
- **context/copy-strategy/scoring-rubric.md**  -  Email quality scoring; useful for self-QA after drafting.
- **context/europe/sovereignty-positioning.md**  -  European sovereignty framing for contacts in GDPR / DORA jurisdictions.

## Persona Pre-Check (Pre-Write Gate, Mandatory)

Before writing any email, verify the contact's title is NOT on the persona-targeting blocklist (`context/outreach/persona-targeting-blocklist.md`). It blocks replied-thread-validated wrong-persona titles in four buckets: universal (Account Executive / Account Manager / CSM), aggregator-NaaS-TSD (Director-Carrier-Wholesale / Wholesale Manager / Director-Sales-Wholesale), fiber-ISP (Director-Field-Operations / Regional Ops Manager), and international-carrier (Country Manager at HQ-product orgs / Finance Director). The full list, the rationale, and the title to email instead live in that file.

If the contact title is on the blocklist, do NOT write an email. Surface the contact in the Cooper-review queue per the context/outreach/persona-targeting-blocklist.md guidance.

## Network Operator Tier Selection (Mandatory When Segment = Network Operator)

The Network Operator segment splits into two lead motions per `context/copy-strategy/segment-messaging.md` §5A vs §5B:

- **Tier 1 (Global $10B+ or National $1-10B with own backbone and PCE-class internal automation):** Use the §5A "extending L2 services across mixed transport" lead. E1 opens "The hard part isn't the core" (mandatory Track A acknowledgment in one sentence) and pivots to per-transport boundary pain (tower backhaul, partner last-mile, enterprise drops). Examples: AT&T, Verizon, Lumen, NTT, BT, Deutsche Telekom, Orange, PCCW Global, Tata Communications, plus national-footprint Tier 1 Nationals.
- **Tier 2/3 Regional Wholesale ($500M-$1B and below):** Use the §5B extend-reach lead. The buying question is "how do we reach customers and markets beyond our footprint," not "how do we simplify L2 extension across mixed transport we don't own."
- **Track B fallback (any tier with confirmed fragmented internal automation):** Lead with internal-unification framing first. Use only when research shows no public evidence of portal/API automation product.

## Active Senders

Sender selection is territory-driven. Load `context/hubspot/territory-model.md` to resolve the correct sender for a given prospect's location. The authoritative 5-region map and all sender HubSpot IDs live there.

Current senders (summary - context/hubspot/territory-model.md is canonical):
- Tim Lieto (161889085) - Northeast + West interim
- Ken Cunningham (162339176) - Southeast
- Tory Teague (165480917) - Central
- Markus Hendrich (164949459) - Europe
- Tim Ziemer (159350430) - International + Tier 1 SP
- Cooper Kennedy (160267902) - Unassigned

If the user doesn't specify a sender, resolve from context/hubspot/territory-model.md using the prospect's HQ state/country. All senders sign as themselves. Signatures are auto-appended by the email platform. Never write a signature block.

**European contacts (Markus Hendrich):** Read `context/europe/europe-email-compliance.md` before writing. Cold email to DE/AT/IT contacts is unlawful without opt-in - these contacts require LinkedIn-first approach instead.

## The Tone

The email should read like a smart industry peer sat down, spent 10 minutes learning about the company and the person, and then wrote a short, direct note. Not a marketing email. Not a "just checking in." A note from someone who understands their world and has a genuine reason to reach out.

### The Human Test

Before sending any email, ask: "Would a real person actually write this?" If it sounds like it came from a sequence tool, rewrite it. If every sentence is doing obvious "work" (building rapport, establishing credibility, creating urgency, asking for the meeting), it will feel manufactured. The best emails have a few sentences that just... sound like a person talking.

### Tone Rules

- **Be direct, not polished.** Connect your reasoning with so/since/but/even though; one bare fragment per body, max. The way people actually write emails to people they respect.
- **Show your homework without showing off.** Reference one or two specific things about their business that matter. Don't list every fact you found.
- **Use "I'd guess" and "I'd imagine" honestly.** These phrases work because they're genuinely humble. You're making an educated hypothesis, not a claim.
- **Let the research drive the email, not a template.** The structure exists as a guardrail, not a fill-in-the-blank.
- **One idea per email.** Pick the single most relevant angle for this person at this company and commit to it.
- **Don't over-personalize.** Mentioning their company and a relevant business context is good. Referencing their LinkedIn posts or quoting them back feels like surveillance.
- **Nudge, don't preach.** No absolutes ("the only way," "the single biggest"). No prescriptive musts ("you need to," "what you should do"). No definitive diagnostics about their business you can't actually know. Hypothesis language and relational framing only. See context/outreach/email-writing-rules.md "Diplomatic Claims" for the full guardrail.
- **Reply-worthy test.** After writing, read the email as the recipient. If replying would feel like submitting to a pitch, rewrite. The goal is peer engagement, not urgency manufacturing.
- **No credibility anchors in cold emails.** No "Same team that built Acme Packet" or "128 Technology." The message does the talking, not our history. Credibility anchors are for live conversations only.

### What Human Sounds Like (vs. Salesy)

**Salesy:** "I noticed [Company] has been expanding into new markets and I wanted to reach out because we help operators like you automate provisioning to accelerate service delivery."

**Human:** "As you push into the Southeast, I'd guess the provisioning side hasn't caught up yet, since most operators in your position are still quoting 60-90 days to turn up a cross-carrier circuit."

**Salesy:** "MaiaEdge provides purpose-built infrastructure that enables operators to build their own fabric while maintaining complete sovereignty over customer relationships."

**Human:** "I've been working on infrastructure that lets you own the connectivity layer instead of handing it to someone else, so the customer, the margin, and the control all stay with you."

**Salesy:** "I'd love to schedule a brief call to discuss how MaiaEdge can help [Company] transform their interconnection capabilities."

**Human:** "Happy to set up time if it's worth a look."

## Verify Segment (Mandatory Before Writing)

After researching the company, verify that the segment in HubSpot (or the source spreadsheet, or whatever the user provided) actually matches what research reveals about the company.

**Check:**
- Does the segment match what you found? (e.g., classified as "Data Center Colo Provider" but research shows they're actually a fiber operator, or listed as "Network Operator" but they're really an MSP aggregating circuits)
- For colos: Did you find AI signals? If strong, sub-segment should be "AI Infrastructure" not "Standard"
- For network operators: Did you find portal/API evidence? Track A vs Track B.
- Is this company actually on the exclusion list? (IXP, Tower REIT, IT MSP, software vendor, etc.)

**If mismatch:** Flag: `SEGMENT CORRECTED: [Source] says [X], research says [Y]. Using [Y] for messaging.` Then load the CORRECT segment's vocabulary, word counts, angles, and proof points. Write the email to the corrected segment.

**If confirmed:** Note: `Segment verified: [segment] / [sub-segment]`

Use the CORRECT segment for all email writing, regardless of what the source data says. A wrong segment in the CRM is a data quality issue, not a reason to write the wrong email.

## Research Sequence (Company, then Contact, then Tailor)

Research runs in two stages, not one. Don't collapse them.

1. **Company research** (situation, timing signals, competitive pressure). Produces the candidate angle.
2. **Contact research** (role, tenure, what they own, recent activity). Produces the framing lens, the facet of the company angle this specific person owns.
3. **Tailor.** Fuse the two into ONE problem this person would recognize from their Tuesday-afternoon reality.

If the email could be sent to a different role at the same company without changes, Stage 2 is missing. Go back and research the contact before writing. See context/outreach/email-writing-rules.md "Research Sequence" for the canonical rule.

## Angle-First Principle

Before writing any email, identify the company-specific angle: the ONE thing happening at this company right now that creates an urgent, MaiaEdge-relevant problem. This could be an acquisition, a new build, a market expansion, a competitive threat, or a technology migration. State it in one sentence: "[Company] is [doing X], which means [specific operational problem MaiaEdge solves]." Then add the contact-level tailoring: "For [role], this means [facet of the problem this person owns]."

If the angle could apply to any company in the same segment, it's not specific enough. If it could apply to any role at this company, the contact-level tailoring is missing. Go back and research deeper.

**The angle must match reality, not the source data.** If the segment was corrected during verification, the angle must reflect what the company actually does, not what the original classification assumed.

**Earned-Problem Doctrine (canonical in context/outreach/email-writing-rules.md).** The angle must name a problem
the contact is publicly discussing or will predictably hit on their stated growth path - not a
flaw you've assumed. Name it directly, but frame it forward-state ("as you scale into X…"), never
as a verdict on how their business runs today. Then one easy-solution line. No bold, unverifiable
claims about their current network, provisioning, or operations. Run the offense test before sending.

## Email Structure (Angle-Driven, Problem-First)

Every email roughly follows this arc, but the company-specific angle drives the substance. The 4-part arc is a guideline, not a template - breaking it deliberately for authenticity is encouraged.

0. **First-name opener on its own line.** `Paul,` then a blank line, then the body. Every email in a sequence starts this way.
1. **Problem statement (1-2 sentences):** Lead with the company-specific angle, framed as the problem this person deals with. This IS the hook. Posture (DIRECT vs ASKED) depends on signal strength - see "Direct vs Asked Posture" below. Use hedges (premise hedges or "I'd guess"-style pain hedges) when inferring; skip hedges when you have a HIGH-confidence cataloged signal.
2. **Context bridge (1 sentence):** Connect their specific situation to the problem. Research absorbed into framing OR a specific public-signal observation ("Saw the Q3 release notes mentioned…" - see context/outreach/email-writing-rules.md "Public-Signal Observations").
3. **Value connection (AT MOST 1 sentence):** How MaiaEdge relates to that pain. Two valid placements:
   - **EMBEDDED (preferred):** woven into the problem paragraph as a contrast clause. Example: "Routes go lit on schedule, but the cross-carrier piece is still a 60-day conversation. The fix is infrastructure that lets your team stand up those paths in minutes, under your brand."
   - **STANDALONE (allowed if punchy):** a single sentence after the problem paragraph, in "I" voice or product-as-outcome framing. Example: "I've been working on infrastructure that lets fiber operators stand up those paths in minutes, under your brand."
   BANNED: multi-sentence value bridge paragraphs. BANNED openers: "MaiaEdge is..." / "We help operators…" / "We built infrastructure that…" / "We built carrier infrastructure that…" / "We built MaiaEdge for…" / "We work with…" Max 1 product-specific term per email (choose ONE: "carrier infrastructure" OR "fabric" OR "provisioning in minutes"). Use "I" voice, not "we" voice. **Also BANNED in cold body:** "fabric-in-a-box" and "federate" as a verb. The noun phrase "Federated Private Networking" is allowed only in partner-facing collateral, never in cold body.
4. **Close (1 sentence):** exactly ONE ask from the close classes (give-close / soft call-ask statement / honest-reason / interest question - see CTAs section). Low friction. Optional when a strong illumination question carries the close.
5. **Peak-end observation (optional, 1 sentence MAX, only when meaningful):** A non-business observation tied to something specific about the recipient's company or location, separated from the CTA. Must pass the "forwarded by colleague" test (would the recipient find it odd if a colleague added the same line in a forwarded internal message?). NEVER in E2 or E3.

No credibility line. No sign-off. The message does the talking, not our history. Signatures are auto-appended by the email platform.

This is not a fill-in-the-blank template. The segment messaging framework provides vocabulary and proof points to support your angle, not a structure to fill in with company details.

**Non-functional voice required when there's something to say.** Every E1 should have at least one sentence that doesn't "do work" structurally (an aside, an honest acknowledgment of uncertainty, a peak-end observation). Don't force it. A forced non-functional sentence reads as performance.

**No flattery-as-problem-statement.** Sentences that approve of their strategy before naming a pain read as flattery even when the next clause names a problem. BANNED examples: "Growth through acquisition is the right play," "Building Tier-4 facilities is the hard part," "Your expansion is smart." Lead with the problem itself.

**No third-person case-study opener.** Extends the role-addressing ban. BANNED: "For a [role] at [type of company doing X]..." (e.g., "For a CFO at a fiber operator expanding into the Southeast..."). A peer doesn't frame their opener like a case study.

## CTAs (Soft Call-Ask First - Never a Menu)

| Type | Pattern (paraphrase every time) | When |
|------|----------|------|
| Give-close | "Fifteen minutes and I can show you the whole thing end to end, whenever works on your side." (demo offer + ask FUSED into one sentence - never followed by a second ask) | Technical buyers. Live demo is ready and sanctioned for cold. |
| Soft call-ask statement | "Happy to set up time if it's worth a look." / "Glad to find 20 minutes while [real window]." | General default when no give. |
| Honest-reason close | "Felt close enough to what you're building to be worth a conversation." | Senior business buyers; states the actual selection reason. |
| Interest question | "Wanted to see if it's on your radar, or still early." | When a statement close feels heavy. |

**Exactly ONE close per email - these are alternatives, never combined.** The give IS the close when used (a give plus a call-ask stacked reads as two asks).

**CTA rules:**
- **BANNED: yes/no thought-question closes** ("Is this something you've thought about?", which earns no replies). The close gives the reader something to DO.
- These are PATTERNS, not strings: no closing string on >20% of a batch, never twice within an account, never a pattern example copied verbatim.
- ONE ask. Never stack two.
- No "I'd love to..." or "I'd be happy to..." (vendor language)
- No "Let me know if..." (passive, easy to ignore)
- No calendar links in first email; on any hot reply, propose three specific times.
- No "quick call" (signals desperation)

<!-- Canonical source: context/outreach/email-writing-rules.md -->
## Writing Rules

**Do:**
- Periods for sentence breaks
- Connect your reasoning with so/since/but/even though; one bare fragment per body, max.
- Active voice, second person (talk to them)
- Specific numbers when they matter (60-90 days, 80-90%)
- Reference their actual business, not their industry generically
- Acknowledge what they've built before positioning a gap
- **Use "I" voice instead of "we" voice.** "I've been seeing this with…" / "The pattern I'm watching at…" / "I've been talking to operators in your position who…" The email is from Tim or Ken to Paul, not from MaiaEdge to operators-like-Paul. Let the senders speak as themselves.
- **Cite specific public-signal observations when you have them.** "Saw the Q3 release notes mentioned…" / "Caught your panel at MetroConnect" / "Your last earnings call mentioned…" / "Noticed the announcement said X three times." These prove the writer looked at a specific thing and had a thought about it. Reference the segment signals catalog (`context/signals/[segment]-signals.md`) for what counts as a cataloged signal.

**Never:**
- Em dashes, colons, and dashes-as-punctuation (spaced hyphen, double hyphen, en dash). Never, in subject or body. Hyphenated compounds (cross-connect, on-net) are fine. Replace with periods or commas; restructure so the point arrives as a clause, not a labeled reveal.
- Move-announcing transitions ("another angle on this," "one more thought," "quick thought," "worth a thought"). Don't narrate the move. Just say the thing.
- "Hope this finds you well" or any greeting filler
- "Just wanted to reach out"
- "As a [role title]..." (don't label them)
- "I noticed..." (the PHRASE; specific "Saw…" / "Caught your panel…" observations are allowed and encouraged - see Public-Signal Observations rule)
- "Saw your post..." / "Following your work..." (LinkedIn surveillance)
- "Revolutionary" or "game-changing"
- Customer names in cold emails (anonymize: "one fiber operator" not "Arvig")
- Competitor names in cold emails (NEVER write "Megaport" or "Equinix" or "Lumen" by name. Use "third-party fabric providers" or "someone else's fabric")
- Session-smart routing as a lead
- "Same team that built Acme Packet" / "128 Technology" / any credibility anchors (save for live conversations only)
- **Generic-category we-claims.** BANNED: "We help operators…" / "We work with…" / "We work with companies like yours…" / "We've been doing this with…" / "Many of the operators we talk to…" / "Most operators we talk to…" / "What we keep hearing from operators…" These are us-to-a-category sentences with no specific mechanic. Use "I" voice replacements above.
  - **The sanctioned first-person identity sentence is the CRAFT LINE:** "That [handoff leg / last hop / boundary] is the layer I work on, [ONE concrete mechanic in their vocabulary]." Registers: "the layer I work on," "what I spend my days on." The mechanic must contain a concrete object (portal, NNI, turn-up, SKU, path) - abstract noun-stacks fail QA. See context/outreach/voice-gold-standard.md.
  - **The "We've been helping similar [cohort]…" peer line is DEMOTED, not banned:** ≤1 per ACCOUNT, ≤20% of E1s per batch, mechanic wording different at every appearance (repeated verbatim it becomes a recognizable stamp). Never in LinkedIn. For Enterprise and neocloud the mechanic is data-sovereignty / audit-ready-path framing, never operator resale.
- **Acknowledgment openers.** BANNED: "Cold email, so here's the short version" / "Quick cold note since I doubt this is on your radar yet" / "We haven't met, so I'll get to it." These place the sender below the recipient and break peer-to-peer posture.
- **Multi-sentence value bridge paragraphs.** BANNED: any value bridge longer than 1 sentence. Embed the value bridge in the problem paragraph as a contrast clause, OR write it as a single standalone sentence in "I" voice, OR omit it entirely if a strong illumination question carries the close.

## Research Display Detector

Before finalizing any email, scan every sentence for research display. This is a DISQUALIFYING flaw.

**Scan for:**
- Company facts stated as standalone observations ("[Company] has [number] [things]", "[Company] is expanding into [region]")
- "Your [number] [thing]" patterns ("Your 50 data centers", "Your expansion into the Southeast")
- Opening sentences that DESCRIBE the company rather than NAME a problem
- Dollar amounts, facility counts, route miles, or specific project names stated as facts

**If found:** Take the displayed fact, identify the PROBLEM it creates, rewrite to name the problem without the fact. The fact selected the angle. The email names the problem.

**The test:** Read the sentence aloud. If it sounds like you're telling the recipient something about their own company, it's research display. If it sounds like you're naming a problem they live with, it's research-as-fuel.

**The carve-out:** the one fact that earns a place is a fresh why-now signal (raise, award, M&A, hire, build milestone) that ties to the value prop and creates urgency. Name it once as an observation ("Saw the X"), never as a possessive stat ("your X"). Static stats (route miles, facility counts, geography) don't pass, so absorb them. The bar: would removing the fact remove the urgency? If no, cut it.

See context/outreach/email-writing-rules.md "Research Display Detection" for the full translation table.

### Cited-Signal Cap (HARD CONSTRAINT)

**Maximum ONE cited public signal in the opening two sentences of E1.** This is a hard cap, not a suggestion.

When the account has multiple Tier A signals (e.g., a funding close + a project groundbreaking + a named hyperscaler partnership), pick the SINGLE strongest one for the opener. The rest of the research informs the framing of the problem statement and the value bridge, but does not appear as displayed text.

**Why this rule exists:** A research summary that strings 2-3 facts together ("Saw the $X.XB credit close on top of the [tenant] sale. With [Project Name] [verb-ing] and the [Partnership] anchored by [Tenant1] and [Tenant2]…") reads as a recap you handed to the recipient before pivoting to your point. Even when each fact is a legitimate public signal individually, stacking them produces the exact failure mode the "research invisible" rule is built to prevent. The recipient already knows their company closed a $2.58B credit. They know about the groundbreaking. They know who their anchor tenants are. The stacked recap tells them only one thing: you researched them.

**Markers to count in opening 2 sentences:**
- Dollar amounts ($X B/M, "$Y.Z billion")
- Power figures (X MW, Y GW)
- Named hyperscaler tenants (Microsoft, NVIDIA, AWS, Oracle, OpenAI, AMD, Meta, Google, Stargate, AI Infrastructure Partnership, Blackstone, PGIM, BlackRock, MGX, Fluidstack)
- Named projects/campuses (Caprock, Comanche Circle, TCDC, Project Jupiter, Goodnight, Abilene, Matador, Frontier, Delta Forge, Corsicana, LBB-01, Barber Lake, Stingray, etc.)
- Building/site/facility counts ("6 buildings", "540 MW with 6 facilities", "9 campuses")

If the opening 2 sentences contain ≥2 of these markers, the email fails the cap. Rewrite by keeping the strongest single signal and dropping the others into the framing.

**Bad opener (5 markers stacked):**
> "Saw the $2.58B PGIM credit close on top of the BlackRock and MGX sale. With Project Caprock breaking ground and the AI Infrastructure Partnership anchored by Microsoft and NVIDIA, the strategic question for the next five years is which layer becomes Aligned's structural advantage."

**Good opener (1 marker, same research powering it):**
> "With Caprock breaking ground, the strategic question for Aligned over the next five years isn't whether the platform scales. It's which layer becomes the structural advantage."

The rest of the original research (PGIM credit, AI Infrastructure Partnership, Microsoft + NVIDIA) is what told the writer that "the strategic question over the next five years" is the right framing for a VP Strategy & Development at this exact moment. The research is doing its job - it's just not displayed.

**Bad opener (3 markers):**
> "Saw the Microsoft expansion to 2.1 GW plus the Goodnight permit."

**Good opener (1 marker):**
> "Saw the Microsoft expansion."

**The exception:** None. The cap applies to every email. If multiple signals genuinely belong in the email, put one in the opener and weave the others into the problem framing in later sentences (still without displaying them as facts).

## Research Receipt (Hard Gate Before Each Email)

Every email must be preceded by a **Research Receipt** block above the email body. An email without a Receipt is invalid output.

### Lookup sequence (pre-write)

For every contact, before writing:

1. **Web search grounded against the segment's signals catalog** (`context/signals/[segment]-signals.md`). Use the `Pattern:` field for each Tier A signal as the literal query. Run minimum 3 Tier A pattern searches. If a HIGH-confidence Tier A hit lands, stop. If no Tier A hits, expand to Tier B.
2. **Contact-level search:** `[Contact Name] [Company] LinkedIn` - pull role tenure, recent activity, what they own. Required on every Receipt, even when the company-level search finds a signal.
3. **Cross-check HubSpot `recent_news_or_trigger_event`** for confirmation. Web search wins where they disagree (HubSpot can be stale mid-week).
4. **If web search and HubSpot both find nothing across at least 5 query attempts**, mark Signal code = NONE, posture = ASKED, and document the literal queries in the Receipt.

The web search must be grounded in catalog patterns, not generic "[company] news."

### Receipt format (mandatory)

```
RESEARCH RECEIPT - [Contact First Last] @ [Company]

Segment: [segment / sub-segment]   Status: VERIFIED | CORRECTED from [X]
Catalog: context/signals/[segment]-signals.md

Searches run (literal query strings - not paraphrased):
1. `[exact query you ran]` → [URL + date, OR "no Tier A hit"]
2. `[exact query]` → [URL + date, OR "no Tier A hit"]
3. `[exact query]` → [URL + date, OR "no Tier A hit"]
[minimum 3 if claiming a cataloged signal; minimum 5 if claiming NONE]

Company-level finding: [signal description with source quote + date, OR "NONE - no Tier A or Tier B hits across [N] searches"]
Contact-level finding: [what THIS specific contact owns / recent role activity / why they care about THIS facet of the problem. REQUIRED on every Receipt, including when company finding is NONE.]
Load-bearing assumption: [the ONE thing the angle assumes is true about how their business works today] → [VERIFIED via source | UNVERIFIED → reframe forward-state / hedge / cut before writing]
Anchor in the email: [the ONE company/contact-specific fact from the findings above that the email's problem statement is built on] → Swap test: [why this email would NOT make sense sent to a different company in the same segment]. If you cannot name a non-generic anchor, the email is a template - reframe or mark RESEARCH INCOMPLETE.

Signal code: [F-A1 | NC-A2 | NO-B3 | NON-CATALOG | NONE]
Posture: [DIRECT | ASKED] - [one-line reason tied to the finding above]

---

Subject: [subject line]

[email body]
```

### Refuse-to-write rule

If you cannot honestly fill all required sections (Searches Run with at least 3 literal queries paired with results, Company-level finding, Contact-level finding, Load-bearing assumption, Anchor-in-the-email with its swap test, Posture with reason), output `RESEARCH INCOMPLETE: [specific reason]` in place of the email body and move on. Do NOT fabricate a Receipt. The Anchor field is the output gate: if the email's problem statement is not built on a named company/contact-specific fact (if it would still read as sent-to-them with a different company name swapped in), it is a segment template and is invalid output even when the searches were run - re-research or reframe, do not ship it. If the load-bearing assumption is UNVERIFIED and asserts how their business works today (for example that they have not already solved the problem), the angle is not ready - reframe forward-state or cut before writing.

### Examples

Two complete worked Receipts - a cataloged-signal case (Fatbeam, F-A1, DIRECT posture) and a NONE / 5-search case (ATN International, ASKED posture) - appear with their finished emails and annotations in the FULL EMAIL EXAMPLES section near the end of this file. Study the ATN example for the higher (≥5) search-count requirement when claiming NONE.

The Receipt is auditable. Cooper scans Receipts to spot research-skipping at batch scale. A high NONE rate paired with thin contact-level findings is the pattern that flags a batch as research-skipped.

## Direct vs Asked Posture (Decision Criteria, Not Quota)

Posture is the second-order voice choice after segment lock and angle selection. It is NOT a batch percentage. Match the move to what you actually have on this contact.

**Go DIRECT (declarative problem statement) when:**
- A specific public signal you can point at exists (cataloged Tier A from segment signals catalog, recent earnings call, hire announcement, BEAD award, M&A filing). The signal earned you the right to name the consequence.
- The recipient is a technical buyer (CTO, VP Engineering, VP Network) who values precision.
- The pain is universally acknowledged in the segment (every fiber operator agrees provisioning is slow).
- The writer has earned the right via specificity earlier in the email.

**Go ASKED (illumination question) when:**
- The pain is real but NOT visible from public signals. You're inferring.
- The recipient is a senior business buyer (CEO, CFO) who deserves to be treated as a thinking peer, not a diagnosis target.
- The pain is variable across the segment.
- The writer is genuinely uncertain whether the email is timely.
- You want a substantive reply, not a yes/no.

**The principle in one sentence:**
- DIRECT when the recipient should think *"this person did the work and saw what's happening to us."*
- ASKED when the recipient should think *"this person is genuinely curious about how we're handling this."*

**Anti-rule:** Do NOT randomize across batches to hit a 50/30/20 quota. The right posture for THIS contact is the right posture even if every other contact in the batch wants the same one. Match the move to what you actually have, never to a target percentage.

See context/outreach/email-writing-rules.md "Direct vs Asked Posture" for canonical text.

## Role-Addressing Language (Banned)

These patterns are BANNED. They make the sender sound like a consultant, not a peer:
- "At the [role] level" -- positions sender below recipient
- "From a [function] standpoint/perspective" -- consultant-speak
- "For an operator [doing X]" -- third-person case study voice
- "At your scale" / "At the pace you're..." -- frames their situation from outside

**Instead:** State the problem directly. A peer says "the fiber buildout is moving, the question is how fast it starts paying for itself." Not "at the CEO level, I'd imagine revenue conversion matters."

## Sequence Rules (HARD CAPS)

### Email 1: 85-110 Words, the Craft Structure

- **85-110 words.** Count before finalizing. Applies across every segment; overrides segment soft floors. Shorter wins ties; never pad.
- **The cold-conversion shape** (canonical: email-writing-rules.md § Craft Voice; exemplars: voice-gold-standard.md): (1) structural truth of their world, competence credited, research-sharpened but invisible; (2) craft line ("that handoff leg is the layer I work on" + ONE concrete mechanic); (3) ONE close from three classes - give-close (demo offer fused into a single ask, technical buyers), soft call-ask statement, or honest-reason close. The give IS the close; never stack it with a second ask.
- **1-3 paragraphs** with proper blank-line spacing between them.
- **First name on its own line** before the body.

### Email 2: Under 55 Words, Genuinely Different Angle

- **Under 55 words.** Enforce strictly.
- **First name on its own line**, blank line, body.
- **No re-introduction.** BANNED openers: "Quick follow-up," "Following up on my last email," "Circling back," "Just wanted to bump this."
- **No meta-references to Email 1.** BANNED phrases: "The other angle on this," "Another way to think about this," "To build on my last note." Just lead with the new thought.

Email 2 must come from a DIFFERENT angle category than Email 1:
- **Revenue angle:** How the problem affects top-line revenue
- **Competitive angle:** How peers/competitors are solving it (anonymized)
- **Operational angle:** Day-to-day burden on the team
- **Market timing angle:** Why now matters
- **Cost-of-inaction angle:** What happens if they do nothing
- **Peer social proof angle:** What other operators are saying/doing

**Standalone test:** If you removed Email 1 from the sequence, would Email 2 still make sense on its own? If it depends on Email 1 for context, it's not differentiated enough.

**The ask never grows across a sequence.** If E1 offered fifteen minutes, E2/E3 hold or shrink the ask - never escalate to thirty. A stranger asking for MORE time after silence reads tone-deaf.

Cap "one operator told us..." at 1 per 3-email sequence.

### Email 3: 2-3 Sentences, One Actionable Ask

- **2-3 sentences max.** Not "3-4." Not "a short paragraph." Two or three sentences, full stop.
- **First name on its own line**, blank line, body.
- **Exactly ONE CTA.** Not two asks. Not a CTA plus "hope to cross paths." ONE close.
- **Timing nudge ONLY when a real window exists** (event date, quarter end, buildout milestone). No real window → take-away that still asks ("Worth a conversation, or wrong moment?"). Manufactured urgency reads templated.

**Banned pattern:** "If [X] is worth a conversation... Either way, hope to cross paths." Pick one.

**Every E3 carries exactly one ACTIONABLE ask.** Zero-ask passive closers are BANNED ("Easy to reach me if that becomes a priority." / "You know where to find me." - they give the reader nothing to do).

**E3 three-option rotation.** Rotate across three E3 options based on signal (patterns - paraphrase, never copy):
- **Option 1 - Take-away close (default; works without an event anchor):** "Sounds like timing might be off, or the angle missed the mark. Worth a conversation, or wrong moment?"
- **Option 2 - Illumination question (when there's a real plausible "when"):** "Curious if this is on your radar this year, or wrong moment? Either is useful to know."
- **Option 3 - Peer observation with timing nudge (real event within 2 weeks):** "Most operators who solved this in the last year said the trigger was [specific event]. If you're not there yet, no rush - door's open."
See `context/outreach/email-writing-rules.md` § E3 three-option rotation for the selection rule.

### Hedge Variety (Batch Processing)

"I'd guess" and "I'd imagine" are capped at 30% of Email 1s in any batch of 10+. The rest must use alternative constructions: direct assertions, illumination questions, premise hedges ("Not sure if you're already solving this, but…" / "Probably already on your radar, but…"), peer observations, market observations, role-native voice. See context/outreach/email-writing-rules.md "Hedge Variety Requirement."

<!-- Canonical source: context/outreach/email-writing-rules.md "Sequence Length & Structure (HARD CAPS)" -->
## Word Count Limits (HARD CAPS)

| Email | Limit | Structure |
|-------|-------|-----------|
| Email 1 | 85-110 words | 1-3 paragraphs, proper spacing, first name on its own line |
| Email 2 | Under 55 words | First name on its own line, no re-intro, no meta-references |
| Email 3 | 2-3 sentences max | First name on its own line, exactly one ACTIONABLE ask |

These caps apply across every segment and override segment-specific targets. A tight, relevant email under the cap is always better than padding. NEVER pad with observations, flattery, or restated value props. Count words (Email 1, 2) and sentences (Email 3) before finalizing.

The per-segment targets in context/copy-strategy/segment-messaging.md remain as tone calibration - they inform density and technical depth, NOT length.

## Subject Lines

Short. Specific to them. Not clever.

**Good:** "Fatbeam provisioning" / "[Company] interconnection" / "Cross-carrier paths at [Company]"
**Also good for COLD: a genuine, substantive question** - "how do you handle paths beyond Jamaica?" earned the only pure-cold E2 positive on record. The question must carry substance on its own; "Quick question" stays banned.
**Bad:** "Unlock new revenue streams" / "The future of private connectivity" / "Quick question" / all-lowercase-intrigue styling for C-suite (reads casual-AI)

**Variant guidance:**
- **Event-anchored subjects ("Looking to meet at DCD," "connecting at ITW")** - use for event-driven motions.
- **Problem-anchored subjects ("[Company] cross-connect speed," "[Company] partner activation," "[Company] dark fiber monetization")** - default for off-event lists. 4-word "[Company] X" pattern using insider vocabulary from context/copy-strategy/segment-language.md.
- **A/B variant on under-performing event campaigns:** problem-anchored vs event-anchored when an event-anchored campaign opens at <60%.

See `context/outreach/email-writing-rules.md` § Subject-line variant guidance for the full rule.

## Role-Based Pain Matrix

Generic role lead-with/avoid (CEO / CFO / COO / CTO / VP Product / VP Sales / VP Network / Sr. Network Engineer) is canonical in `context/copy-strategy/segment-messaging.md` § Cross-Segment Role Pain Matrix. Per-segment refinements live in that file's segment sections.

## Proof Points (Anonymized for Cold Outreach)

Never use customer names in cold emails. The anonymized cold-outreach proof table (Speed / Sovereignty / Simplicity / Scale / Industry validation / Reach / Multi-carrier) is canonical in `context/product/proof-points.md` § Anonymized Proof Points (for Cold Outreach).

## Competitive Positioning (For Email Context)

Use sparingly and only when relevant. Don't turn the email into a competitive comparison.

**vs. NaaS (Megaport / Equinix Fabric):** "With Megaport, you turn the customer over to Megaport. With MaiaEdge, you keep the customer." Don't name them in cold emails unless obvious. Say "third-party fabric providers" instead.

**vs. Lumen Private Connectivity Fabric:** "Lumen builds their empire. MaiaEdge empowers you to build yours." AWS + Lumen threat is a real urgency lever.

**vs. Status Quo:** Most deals are lost to inertia. Frame the cost of inaction.

## Quality Checklist

Run before delivering anything:

- [ ] Research completed and documented (company AND contact, as two separate stages)
- [ ] Contact-level tailoring present (could not be sent to a different role at the same company)
- [ ] No overclaims, absolutes, or prescriptive "must" language about their business
- [ ] Would THIS specific person want to reply?
- [ ] Segment verified against research (if mismatch, corrected and flagged)
- [ ] If segment corrected, emails use corrected segment's vocabulary, word counts, and angles
- [ ] AI signals checked for colos
- [ ] Pain points match the contact's role, not generic
- [ ] Claims based on research findings, not assumptions
- [ ] Email 1: 85-110 words, 1-3 paragraphs with proper spacing, first name on its own line
- [ ] Email 2: under 55 words, first name line, no re-intro, no meta-references to Email 1
- [ ] Email 3: 2-3 sentences max, first name line, exactly one ACTIONABLE ask (no zero-ask passive closers)
- [ ] No yes/no thought-question close ("Is this something you've thought about?" class - banned)
- [ ] Closing string not reused from any other email in this batch/account (Batch Fingerprint Gate, context/outreach/email-writing-rules.md)
- [ ] No flattery-as-problem-statement ("X is the right play" / "X is smart" / "X is the hard part")
- [ ] No "For a [role] at [type of company]..." opener
- [ ] Sovereignty/ownership language present (speed paired with ownership) [Canonical source: context/outreach/email-writing-rules.md]
- [ ] Doesn't sound like NaaS (we don't own a fabric or sell bandwidth)
- [ ] No em dashes, colons, or dash-as-punctuation anywhere in subject or body (scan for ":", " - ", "--"; hyphenated compounds fine)
- [ ] No move-announcing transitions ("another angle," "one more thought," "quick thought")
- [ ] No banned phrases (see writing rules)
- [ ] No competitor names (Megaport, Equinix, Lumen  -  use "third-party fabric" instead)
- [ ] NO credibility anchors (no Acme Packet, no 128 Technology)
- [ ] Company-specific angle identified (not a segment template restatement)
- [ ] Email driven by company-specific angle, not segment framework
- [ ] Single CTA, low-friction, matches persona
- [ ] Reads like a person wrote it, not a sequence tool
- [ ] Correct sender per context/hubspot/territory-model.md (resolved from prospect HQ location)
- [ ] No customer names (proof points anonymized)
- [ ] Subject line is short and specific to them
- [ ] No research display (company facts invisible, problems named)
- [ ] No role-addressing language (no "at the [role] level", "from a [function] standpoint", etc.)
- [ ] Email 2 comes from different angle category than Email 1
- [ ] Email 3 has exactly one CTA (no double asks)
- [ ] **Reasoning flows, facts don't stack:** clauses connected with so / since / but / even though, not one-idea-per-sentence declaratives. One bare fragment per body, max.
- [ ] **Active voice, second person:** talking to them ("your team provisions"), not reporting about them ("the team provisions").
- [ ] **Value bridge is 1 sentence max**, embedded by contrast OR standalone-but-punchy. Multi-sentence value bridge paragraph is BANNED.
- [ ] **No generic-category we-claims** ("We help operators…" / "We work with companies like yours…" / "Most operators we talk to…"). Use "I" voice. The specific-mechanic peer line ("We've been helping similar [cohort] [specific mechanic], so [plain outcome]") is the one allowed "we" sentence (email only, not LinkedIn; one per sequence).
- [ ] **Research Receipt present above the email body** with all required sections complete: Searches Run (≥3 literal queries paired with results, ≥5 if claiming NONE), Company-level finding, Contact-level finding, Load-bearing assumption, Posture with reason. "NONE" without literal queries above it is research-skipping and fails this check.
- [ ] **Load-Bearing Assumption Gate:** the one assumption the angle depends on is named on the Receipt and verified against a source, or reframed forward-state. Never assert they have not already solved the problem without a source (assume competence). Canonical: `context/outreach/email-writing-rules.md` § The Load-Bearing Assumption Gate.
- [ ] **Posture matches signal strength.** DIRECT when there's a real public signal you can point at; ASKED when inferring. NOT randomized to a quota.
- [ ] **Posture rotates across the 3-email sequence to the same contact.** E1/E2/E3 should NOT all be the same posture; if E1 was DIRECT, E2 should be ASKED, etc.
- [ ] **Hedge cap: "I'd guess" / "I'd imagine" appear in ≤30% of E1s** in any batch of 10+ contacts.
- [ ] **Non-functional voice present in E1** when there's a meaningful thing to say (an aside, an honest acknowledgment of uncertainty, a peak-end observation). Optional but encouraged.
- [ ] **Peak-end observation (if used)** passes the "forwarded by colleague" test.
- [ ] **No acknowledgment openers** ("Cold email, so here's the short version" - banned).
- [ ] **Catalog-grounded web research actually happened** (visible in the Receipt's Searches Run section as literal queries). If "NONE" cited, the Receipt shows ≥5 literal queries that were tried, not just a NONE declaration.
- [ ] **Earned-Problem check:** problem is publicly-grounded or a forward-state growth challenge,
  not an unverifiable current-state claim. Direct but non-offending. Easy-solution line present.

## Enterprise (Multi-DC ICP) - Voice and Angle Guide

Enterprise is `customer_segment = "Enterprise-CustomerSegment"`. Four sub-segments only: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Anchor: Meijer.

**Critical voice difference from operator segments:** Enterprises ARE the customer. There is no commercial layer to resell to. Drop operator-monetization framing entirely.

### Sovereignty rule for Enterprise

Pair speed with **data sovereignty + audit-trail language**, NOT operator sovereignty. The enterprise is consuming the network for their own operations, regulated workloads, and customer-facing services - they are not selling connectivity to anyone.

- **BANNED for Enterprise:** "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "wholesale activation," "extend reach to new markets," "tenant," "meet-me room," "interconnection revenue," "aggregator," "TSD." Federation framing has no place in Enterprise copy.
- **USE for Enterprise:** "audit-ready paths," "deterministic paths between data centers," "your team owns the SLA," "paths you can prove," "policy-based path control," "compliance can prove the path." HIPAA / PCI-DSS / SOX / GDPR / HITRUST mentions are appropriate when the buyer's persona implies regulatory exposure (CISO, regulated-vertical CIO).

### Lead angles by sub-segment

| Sub-segment | Lead with the problem (in their language) |
|---|---|
| **Retail and Distribution - Enterprise** | "Your dark fiber between corporate DCs is one cut from an outage." → fix dark fiber redundancy that is actually redundant + cloud on-ramp under enterprise control. |
| **Financial Services - Enterprise** | "Your inter-DC paths are best-effort. Compliance is asking you to prove the path. You can't." → deterministic inter-DC paths + audit-ready policy enforcement for SOX / PCI-DSS / GDPR + cloud on-ramps under enterprise control. |
| **Healthcare Systems - Enterprise** | "Your EHR DC redundancy depends on a single fiber pair. PHI rides that path." → diverse dark fiber redundancy between EHR DCs + HIPAA-aligned policy control + cloud on-ramps for radiology / analytics. |
| **Outsourcing Services - Enterprise** | "Your clients' regulators are asking where their data went. You have a BGP routing table." → delivery-center reliability + client data sovereignty (your clients' regulated data on paths you can prove) + dark fiber redundancy between primary delivery hubs. |

### Personas (Enterprise-specific)

| Persona | Title patterns | What they care about |
|---|---|---|
| **VP Network Infrastructure / Director Network Engineering** | VP Network Infrastructure, Director Network Engineering, VP Networks | Engineering effort on path management, redundancy that isn't redundant, visibility gaps. **Primary technical champion.** |
| **CIO** | CIO, Chief Information Officer, CTO (at retail/healthcare) | Unified private connectivity across all sites, AI infrastructure access, cloud on-ramps under their brand. **Economic buyer at most enterprises.** |
| **CSO / CISO** | CSO, CISO, VP Cybersecurity | Audit-ready policy enforcement, hop-by-hop visibility, line-rate encryption, data sovereignty. |
| **Network Architect / Principal Network Engineer** | Principal Network Engineer, Network Architect, Lead Network Architect | "HAsync and HAfabric on the SSRs share a single dark fiber pair. That is not redundancy." "Type 2 is a black hole." **Technical influencer.** |

### Pain points (Enterprise - their language)

- "Our DR strategy assumes the dark fiber is redundant. It is not."
- "Every new DC is a six-month networking project. That is the bottleneck on growth."
- "We do not have the headcount to run BGP across the WAN."
- "Megaport works until it does not. We need our own answer."
- "Compliance asked us to prove where the data went. We could not."
- "HAsync and HAfabric on the SSRs share a single dark fiber pair. That is not redundancy." (Network Architect / Principal Engineer at SSR-deployed retailers)
- "Type 2 is a black hole. We cannot troubleshoot what we cannot see."
- "Cloud on-ramp is owned by Megaport. Our team owns the SLA."

### Don't lead with technical detail

Lead with the problem in their language ("your dark fiber between DCs is one cut from an outage" / "your cloud on-ramp goes through Megaport"). Do NOT lead with technical specifics in cold email - SSR1300, HAsync/HAfabric, 100GigE port counts, AES-256-GCM line rate. Those are for the design call. The cheat sheet stays broad in cold; the design call gets technical.

### Provisioning-simplicity language for Enterprise

In **Enterprise** copy, prefer **"connect anywhere to anywhere with a click"** (or close paraphrase) over "no routing complexity." Enterprise buyers (CIO / CFO / VP Sales-adjacent personas) respond better to positive-outcome framing than negation. Technical-champion Enterprise personas (VP Network, Principal Engineer) can still take "no routing complexity" - writer's judgment. The preferred phrase pairs naturally with an Intelligent Path Computation Engine / PCE reference where one fits.

In operator-segment (Fiber, Colo, AI Colo, Network Op, MSP) and neocloud copy, "no routing complexity" is canonical and acceptable.

### Account Tier ceiling

Enterprise records cap at Tier 2 unless an exceptional trigger emerges. There is no Tier 1 path. Tier 2 requires `high_90` confidence + $1B+ revenue + 3+ DCs + in-house net eng + recent trigger event (M&A, AI workload announcement, leadership change ≤6 months). Most Enterprise records land at Tier 3 (baseline qualification, no trigger).

### Reference

Full Enterprise positioning, sub-segment cheatsheets, persona pain language, objection reframes, and HubSpot mapping live in `context/segments/enterprise.md`. Read that file before writing Enterprise cold email.

---

## Common Failures

| Failure | Fix |
|---------|-----|
| Sounds like NaaS | "Build your own fabric" not "connect to our fabric." We're infrastructure, not a service. |
| Customer name-dropping | Anonymize. "One fiber operator" not "Arvig told us." |
| Speed without ownership | Always pair: "your team provisions in minutes" not just "provision in minutes." |
| Claiming Tier 1s are slow | Research first. Acknowledge what they've built. The gap is cross-carrier. |
| Wrong Network Operator track | Research portal/API status. Track A if automated, Track B if fragmented. |
| Wrong segment messaging | Fiber messaging for a colo. Colo messaging for an MSP. Match the value prop. |
| Pain doesn't match role | Operational efficiency to a CEO. Strategic vision to an engineer. Use the matrix. |
| Missing AI signals | Standard colo messaging when they have Lambda Labs as a tenant. Always check. |
| Generic pain hypothesis | "I'm sure provisioning is a challenge." Be specific or use "I'd guess." |
| Template voice | If every email sounds the same with different company names swapped in, rewrite. |
| Operator sovereignty framing for Enterprise | Drop "keep your customer / your portal / build your own fabric to sell." Enterprises are the customer. Pair speed with data sovereignty + audit-trail language instead. |
| "No routing complexity" in Enterprise copy | De-prioritized for Enterprise CIO / CFO / VP Sales personas. Prefer "connect anywhere to anywhere with a click." Phrase remains canonical in operator and neocloud copy. |

## Warm Contact Handling

This section governs warm TARGETING before the first touch in this motion. The moment a prospect replies (any channel) or accepts a LinkedIn connect, switch to the **warm-follow-up** skill - it owns every message after the prospect responds.

If the contact has HubSpot activity, classify them as WARM and modify the approach.

**WARM classification (any of these):**
- HubSpot activity within 90 days (emails sent, meetings, calls)
- Company notes mention shared events (#MetroConnect26, #PTC26, #FiberConnect)
- Deal or POC history exists

**Warm framing rules:**
- If HubSpot shows real activity: use warm-but-vague framing. "We've connected with a few folks at [Company]" or "I think we were both at [Event] and didn't get a chance to connect." ONLY if activity backs it up.
- If HubSpot shows event-tagged notes: weave shared event into the opener naturally.
- Warm emails should be 10-15% shorter than cold word count targets. More casual tone, fewer proof points, more "continuing a relationship" energy.
- NEVER fabricate warmth. If HubSpot shows nothing, proceed cold. Do NOT fake familiarity.

## Calibration Examples

These show what research-as-fuel looks like when done right, plus common patterns to avoid.

### GOOD (Research-as-Fuel -- Research is Invisible)

**Fiber Operator:**
> "The fiber buildout is moving. The question is how fast new routes start generating revenue once they're lit."
> (Writer knows about expansion. Doesn't say it. Names the problem.)

**Colocation:**
> "Every new facility adds interconnection complexity across the portfolio. When tenants need reach beyond your campus, who controls that experience?"
> (Writer knows facility count. Doesn't say it. Names the operational problem.)

**Neocloud:**
> "When tenants need deterministic paths between GPU clusters, who controls that connectivity?"
> (Writer knows about GPU hosting. Doesn't display the research.)

**Network Operator:**
> "The automation works fine within each market. The problem hits at the boundary."
> (Writer knows about multi-country operations. Doesn't list countries.)

**MSP/Aggregator:**
> "When a customer reports a performance issue, the first hour is spent figuring out which carrier in the chain is the problem."
> (Writer knows about carrier aggregation. Names the operational burden directly.)

### CLOSE BUT IMPROVABLE (Common Patterns to Avoid)

> CLOSE: "DartPoints is expanding into new markets with AI-ready infrastructure. That's a big bet on being more than space and power."
> ISSUE: Research display. "DartPoints is expanding" tells them what they already know.
> BETTER: "Every new facility adds interconnection complexity. The bet isn't space and power anymore, it's the connectivity layer."

> CLOSE: "ATN's carrier and enterprise operations span the Caribbean to Alaska. That's a lot of geography."
> ISSUE: Describing the company back to the company. They know their geography.
> BETTER: "The automation works fine within each market. The problem hits every time a customer needs a path that crosses a boundary."

> CLOSE: "Accelecom's expansion into Eastern Kentucky puts more markets on your map, but I'd guess every new carrier interconnection is still a multi-month project."
> ISSUE: "Expansion into Eastern Kentucky" is displayed research with a generic pain bolted on.
> BETTER: "New markets look great on the investor deck. The gap is usually between 'route lit' and 'first dollar of revenue flowing.'"

### FULL EMAIL EXAMPLES (showing the new rules end-to-end)

**Fiber Operator E1 - DIRECT posture, cataloged signal F-A1, embedded value bridge**

```
RESEARCH RECEIPT - Paul Janes @ Fatbeam

Segment: Fiber Operator   Status: VERIFIED
Catalog: context/signals/fiber-signals.md

Searches run:
1. `"BEAD subgrant awarded" Fatbeam route miles` → texas-comptroller.gov/.../bead-q1-2026, 2026-03-15
2. `Fatbeam ("definitive agreement" OR "to acquire") fiber` → no Tier A hit
3. `Fatbeam ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit

Company-level finding: F-A1 BEAD subgrant award. Texas Comptroller, 2026-03-15: $12M Eastern Texas middle-mile build. 45 days old, within Tier A window.
Contact-level finding: Paul Janes, VP Engineering since 2024-08. Owns network provisioning. Recent LinkedIn posts on automation tooling - likely feels the cross-carrier NNI gap acutely.

Signal code: F-A1
Posture: DIRECT - HIGH-confidence cataloged signal, technical buyer (VP Engineering)

---

Subject: Fatbeam Eastern Texas

Paul,

Saw the BEAD subgrant for the Eastern Texas middle-mile build. The part that usually bites isn't the buildout, since that's funded and on a schedule. It's the gap between fiber lit and your first dollar of revenue, because every cross-carrier hop into the new market is still a 60-day NNI conversation. The fix is infrastructure that lets your team stand up those paths in minutes, under your brand.

Worth a conversation?
```

(71 words. Reasoning flows with since/because; second person ("your first dollar," "your team"). Public-signal opener "Saw…" cites the cataloged F-A1 signal. Value bridge embedded by contrast in the problem paragraph. "I" voice implied by sender. No standalone "we built infrastructure that…" paragraph.)

**Network Operator E1 - ASKED posture, NONE Receipt (5+ searches required), premise hedge, omit standalone value bridge**

```
RESEARCH RECEIPT - Paul Janes @ ATN International

Segment: Network Operator   Status: VERIFIED
Catalog: context/signals/network-operator-signals.md

Searches run:
1. `ATN International ("definitive agreement" OR "to acquire")` → no Tier A hit
2. `ATN International BEAD subgrant route miles` → no Tier A hit
3. `ATN International ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit
4. `ATN International ("AI data center" OR "hyperscaler" OR "GPU") fiber` → no Tier A hit
5. `ATN International earnings call provisioning` → no Tier B hit

Company-level finding: NONE - no Tier A or Tier B hits across 5 searches.
Contact-level finding: Paul Janes, CTO since 2023. Came from Liberty Networks where he ran cross-Caribbean network ops. Background suggests he's lived the multi-jurisdiction provisioning problem firsthand.

Signal code: NONE
Posture: ASKED - no public signal, inferring; technical buyer but inference requires hedge

---

Subject: ATN cross-boundary paths

Paul,

Probably already on your radar, but the multi-country operators I've been watching all hit the same pinch point. The automation runs fine inside each market, but the moment a customer needs a path that crosses a boundary your team is back to LOAs and BGP sessions, so the cross-border leg is where the time goes. Curious how you're sequencing that, or whether it already runs at on-net pace.

Either way, the new São Paulo PoP looks well-placed for the LATAM-North flows.
```

(81 words. Reasoning flows with but/so; second person ("your team"). Premise hedge "Probably already on your radar, but…" softens the entire premise. "Operators I've been watching" is "I" voice. Illumination question carries the close - no standalone CTA. Peak-end observation about São Paulo PoP passes the "forwarded by colleague" test. No value bridge sentence at all - the question carries it.)

---

## Enterprise (Multi-DC ICP) - Calibration Examples

Enterprise outreach has its own failure mode the operator examples don't surface: **info-dumping product detail because the company has a real architecture you know about**. The fix is the same rule the other segments follow - research is fuel, the email names a problem in the buyer's language, the product is implied not pitched. The 4 examples below are the calibration.

**Required reading before writing Enterprise cold email:** `context/segments/enterprise-use-cases.md` (use case fit matrix + sub-segment lead-angle templates) and `context/segments/enterprise.md` (sub-segment language banks).

### Example 1 - Financial Services - Enterprise (M&A integration, Use Case 5)

```
RESEARCH RECEIPT - [Director Name] @ [Top-25 US Bank, mid-integration]

Segment: Enterprise (Multi-DC ICP) / Financial Services - Enterprise   Status: VERIFIED
Catalog: context/segments/enterprise.md + enterprise-use-cases.md + context/signals/enterprise-signals.md

Searches run:
1. `[Bank] acquisition integration data center network` → 2025-Q3 investor day deck mentions integration cost overrun
2. `[Bank] "VP Network" OR "Director Network Engineering" LinkedIn` → 8 senior network roles, 3 hired post-close
3. `[Bank] FFIEC carrier diversity 2025` → no Tier A hit
4. `[Bank] DORA CTPP designation` → no specific hit (general DORA designations Nov 18 2025 apply)
5. `[Bank] AT&T carrier MSA termination` → no Tier A hit

Company-level finding: NON-CATALOG - definitive merger close 2025, integration cost line on Q3 deck blew past prior estimate, 3 senior network hires post-close suggest active integration team build-out.
Contact-level finding: Director Network Engineering, joined post-close, came from the acquired entity. Almost certainly running point on the parallel-WAN bridge.

Signal code: NON-CATALOG
Posture: ASKED - no public-statement signal at the path level; inferring from staffing + integration cost trajectory

---

Subject: [Bank] parallel WAN

[Director first name],

Every major bank integration since 2022 has run a third bridge network for 18 to 24 months because the acquired entity's carrier MSA can't be terminated without a regulator-notified plan. The bridge usually outlives the integration, and the team running it is the one that knows the acquired side cold.

Curious where that's sitting for you right now, or whether you've already collapsed it.

Worth a conversation?
```

**Why it works:**
- 70 words. Single CTA. No em dashes, colons, or dash punctuation. No "no routing complexity" (Enterprise scope).
- Pain in the buyer's language: "third bridge network," "regulator-notified plan," "parallel WAN."
- Research is invisible: the writer knows about the integration, the cost overrun, the hires - none of it appears in the body.
- No pitch. No product description. No "MaiaEdge gives you X." The illumination question carries the close.
- Persona-tailored: "the team running it is the one that knows the acquired side cold" lands at a Director who joined from the acquired entity - research-as-fuel doing its job.
- Data sovereignty / regulator framing implicit ("regulator-notified plan"), not operator sovereignty framing.

### Example 2 - Healthcare Systems - Enterprise (dark fiber redundancy + Hyperdrive cutover, Use Case 1)

```
RESEARCH RECEIPT - [Director Name] @ [Multi-hospital IDN, mid-Hyperdrive cutover]

Segment: Enterprise (Multi-DC ICP) / Healthcare Systems - Enterprise   Status: VERIFIED
Catalog: context/segments/enterprise.md + enterprise-use-cases.md

Searches run:
1. `[IDN] Epic Hyperdrive migration 2025 2026` → public press / Epic UGM mention of phased cutover
2. `[IDN] "Director Network Engineering" OR "VP Network Infrastructure" LinkedIn` → 5 senior network roles confirmed
3. `[IDN] data center disclosure 10-K` → 2 corporate DCs disclosed, primary + DR
4. `[IDN] HIPAA breach OCR portal 2024 2025` → no recent disclosure

Company-level finding: NON-CATALOG - mid-Hyperdrive cutover (~70% of multi-hospital IDNs in this window through 2026). Two-DC active/passive Epic topology disclosed in 10-K. No recent compliance event.
Contact-level finding: Director Network Engineering, 7-year tenure, owns the inter-DC path and the Hyperdrive cutover weekend. Has lived through one DR exercise that didn't fully succeed (LinkedIn post 2024).

Signal code: NON-CATALOG
Posture: DIRECT - technical buyer + universally-acknowledged segment pain (Hyperdrive cutover risk + Epic primary-DR replication jitter)

---

Subject: [IDN] Epic primary-DR replication

[Director first name],

Most Hyperdrive cutover weekends I'm hearing about end the same way: the cutover itself goes fine, and then a week later the team notices the RPO budget for Epic DR is being eaten by jitter the carrier can't account for. The inter-DC path that worked at Hyperspace volumes is the part nobody flagged.

Curious whether you've got a clean read on the jitter envelope, or whether that's a Q1 conversation post-cutover.

Worth a conversation?
```

**Why it works:**
- 80 words. Single CTA. No em dashes, colons, or dash punctuation.
- Uses IDN-specific insider vocabulary: "Hyperdrive cutover," "RPO budget," "jitter envelope," "Hyperspace volumes" - pulled straight from the language bank.
- Frames a forward-looking problem (post-cutover Q1 conversation) - doesn't pitch the product, opens a window.
- Research invisible: writer knows the IDN is mid-cutover and has DR-exercise history; the email just names the pattern.
- No HIPAA / OCR / Ascension reference because no compliance event triggered this. If there were one, Use Case 8 would lead instead with audit-trail framing.

### Example 3 - Retail and Distribution - Enterprise (dark fiber redundancy + freeze window, Use Case 1)

```
RESEARCH RECEIPT - Mark Szymanski @ Meijer

Segment: Enterprise (Multi-DC ICP) / Retail and Distribution - Enterprise   Status: VERIFIED
Catalog: context/segments/enterprise.md + enterprise-use-cases.md (anchor account)

Searches run:
1. `Meijer data center locations` → meijer.com/about/properties, 2026-04-22
2. `Meijer "VP Network" OR "Director Network Engineering" LinkedIn` → 24+ network roles
3. `Meijer M&A 2025 2026` → no recent Tier A signal

Company-level finding: Anchor account. Active April 2026 design (Ken + Woody + Mark Szymanski) on PBC + Port Extender for HAsync/HAfabric dark fiber diversity to SSR1300 nodes. **For the calibration example, treat as if first-touch cold to a Meijer-peer at a different retailer (Kroger, Lowe's, Costco corporate IT) - that's how the writer should think about it.**
Contact-level finding: Network Architect / Principal Network Engineer-equivalent. Owns DC-to-DC paths. Most likely already aware that "diverse" fiber may not be diverse.

Signal code: NON-CATALOG
Posture: ASKED - premise hedge + illumination question; matches the conversational reality (writer is inferring this is the pain, not declaring it)

---

Subject: Meijer DC-to-DC paths

Mark,

The dark fiber between corporate DCs at most multi-DC retailers your size is one pair, one path. The DR plan assumes it's diverse. It's not, until a backhoe finds out for everyone.

Curious how you're sequencing the diverse-path piece, or whether someone already has it on their plate.

Worth a conversation?
```

**Why it works (and what was wrong with the earlier draft):**
- 63 words. Single CTA.
- NO PBC. NO SSR. NO HAsync/HAfabric. NO Port Extender. NO "the fix is X." All of those are design-call vocabulary - the cold email earns the design call.
- Names a problem in language Mark would use in a meeting with his VP - dark fiber that's redundant on paper but not in reality.
- Premise hedge ("most multi-DC retailers your size") instead of declarative. Illumination question carries the close - no standalone value bridge.
- The research powering it is invisible: writer knows Meijer is retail, multi-DC, that DR is on the network team's plate, that the SSR architecture exists. Email never displays the research.
- **The earlier draft (v1 of this validation) violated all of this** - info-dumped HAsync/HAfabric/PBC/SSR1300, listed "the fix is...", treated a real cold email like a design-call recap. The skill rules say "lead with the problem in their language; don't lead with technical detail" and the v1 draft violated them.

### Example 4 - Outsourcing Services - Enterprise (BCP failover + delivery-center reliability, Use Case 8 + Use Case 7 blended)

```
RESEARCH RECEIPT - [VP Network Name] @ [BPO with Philippine delivery centers]

Segment: Enterprise (Multi-DC ICP) / Outsourcing Services - Enterprise   Status: VERIFIED
Catalog: context/segments/enterprise.md + enterprise-use-cases.md

Searches run:
1. `[BPO] delivery centers Philippines Manila Cebu` → company site lists 4+ Philippine sites
2. `[BPO] "VP Network" OR "Director Network Operations" LinkedIn` → 6 senior network roles, regional spread
3. `[BPO] Super Typhoon Uwan November 2025` → no specific public statement (DOLE investigation list general)
4. `[BPO] DPDP DORA compliance 2025` → general regulatory exposure visible in 10-K / 20-F

Company-level finding: NON-CATALOG - typhoon-affected geography (98 Philippine BPO sites under DOLE investigation Nov 2025). DPDP + DORA dual exposure given client mix.
Contact-level finding: VP Network Operations, 5+ year tenure, owns BCP architecture across Philippines + India + nearshore footprint. Public talk at NASSCOM 2024 on multi-site resilience.

Signal code: NON-CATALOG
Posture: ASKED - sensitive topic (recent typhoon), illumination question feels more honest than declarative

---

Subject: [BPO] paired-site failover

[VP first name],

Paired-site failover that reads active-standby in the runbook is rarely active-standby in the routing table when the typhoon hits. Most of the failover patterns I've been watching post-Uwan came down to one client's traffic crossing the wrong jurisdiction during the cutover, and the audit conversation eight weeks later.

How are you thinking about the controller side of that, or is it still a routing-convergence problem?

Worth a conversation?
```

**Why it works:**
- 81 words. Single CTA.
- BPO-specific insider vocabulary: "paired-site failover," "active-standby in the runbook," "routing-convergence," "jurisdiction during the cutover," "audit conversation."
- References Super Typhoon Uwan (Nov 2025) implicitly without making the typhoon the headline - the buyer experienced it, the email doesn't recap it.
- Bridges Use Case 7 (BCP failover / site resilience) with Use Case 8 (audit trails / jurisdictional handling) - natural blend for the BPO architecture reality.
- Sensitive topic handled with ASKED posture, not declarative - matches the conversational reality of a peer asking about something the recipient just lived through.
- No "data residency" / "DPDP" mention even though it's the implicit pressure - those are next-email-in-sequence levers, not the cold E1 opener.

### What ALL four Enterprise calibration examples have in common

1. **Research Receipt is real.** Literal queries, real findings, real persona research. Not back-filled.
2. **Pain in buyer's language.** Each email names a problem the recipient would describe the same way in a meeting with their VP. The vocabulary comes from the sub-segment language bank in `context/segments/enterprise.md`.
3. **Research is invisible.** The writer knows specifics about the company; the email body never displays them as facts. The Receipt holds the research; the email carries the framing.
4. **No pitch.** No "MaiaEdge gives you X" / "the fix is Y" / "PBCs at each end" / product names. The product is implied by the problem framing.
5. **One angle.** Each email leads with ONE use case, ONE problem statement. Not three value props stacked.
6. **Right sovereignty pairing.** Enterprise = data sovereignty + audit trails. No "keep your customer / your portal your invoice / build your own fabric to sell" - those are operator framings and break the peer-recognition test.
7. **Embedded or omitted value bridge.** No standalone "We built infrastructure that..." paragraph. The contrast clause inside the problem paragraph (or the illumination question) carries the close.
8. **Persona-tailored.** Each example could not be sent to a different role at the same company without changes.

### What "bad" looks like - the calibration anti-pattern (do NOT write like this)

The pre-rewrite Meijer draft (preserved here as a calibration anti-pattern):

> "Mark, The HAsync and HAfabric pair sharing a single dark fiber between data centers is the textbook example of redundancy that isn't redundant. The fix is PBCs at each end with diverse fibers and automated failover, no BGP across the WAN, and the SSR1300 nodes keep doing exactly what they're doing today. Saw the design notes from last week. The Port Extender side looks clean. Happy to walk through how the diverse path bring-up sequences if it's useful. Open to a conversation this week?"

**What's wrong:**
- **Info-dump on Mark's own architecture** (HAsync/HAfabric/SSR1300) - research display, not research-as-fuel.
- **Pitches the fix** ("The fix is PBCs at each end with diverse fibers and automated failover") - that's design-call vocabulary, not cold-email vocabulary.
- **Treats a cold email like a follow-up** ("Saw the design notes from last week") - only works in an active conversation.
- **Multi-sentence value bridge paragraph** - banned.
- **Em dash** - banned.
- **Names the product** (PBCs, Port Extender) - Enterprise cold emails don't.

This is the failure mode the Enterprise voice section, the use-case playbook, and these four calibration examples exist to prevent.

---

## Final Step: Signal Push-Back to HubSpot

**Runs AFTER the drafted email(s) are delivered to the rep - never before, never blocking.** Follow the canonical procedure in `context/signals/outreach-signal-pushback.md`: if your Step 2 ("Detect Signal") research surfaced a signal-grade event scoring ≥8 whose event date is newer than HubSpot's `last_signal_date`, write the five signal fields (`recent_news_or_trigger_event`, `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`) plus `account_tier` (only when `hs_is_target_account != true`), recompute heat per `context/account-tiering/tier-compute-spec.md` §11.5, do NOT bump `last_enriched_date`, and log the audit note. Skip silently on any failure - R-Tier-Audit reconciles next run.

---

## Skill Chain

- **Best preceded by:** prospect-research (recommended) or existing HubSpot account brief
- **On any reply or accept:** warm-follow-up (owns every message after the prospect responds - thank-you DMs, answers, objections, scheduling)
- **QA:** copy-strategist (for review of completed emails)
- **For batches:** Use sdr-pipeline instead, which includes cold-email writing + research + pipeline management
