---
name: linkedin-outreach
description: Write LinkedIn connection requests for MaiaEdge prospects. Use when asked to write a LinkedIn message, connection request, or LinkedIn outreach. Target 35-50 words, hard cap 280 characters (under LinkedIn's 300 hard limit). NO sender intro in body - recipient sees sender from LinkedIn UI. Must include company-specific detail baked into a problem statement, ideally grounded in a cataloged signal from context/signals/[segment]-signals.md. Requires prospect research and segment classification first. Same core philosophy as cold email (research as fuel, angle-first, peer tone, public-signal observations).
---

# MaiaEdge LinkedIn Connection Requests

## Clarification (Ask Before Writing)

Two questions that change the output:

1. **Sender / territory:** Which sender? See `context/hubspot/territory-model.md` for the 5-region map. If Markus Hendrich (Europe), European compliance + sovereignty framing apply and LinkedIn-first is legally required for DE/AT/IT.
2. **Sequence context:** Standalone LinkedIn touch, or Day -3 before Email 1? If in-sequence, the LinkedIn angle must differ from Email 1's (same problem, different lens).

Coach: share contact name, title, company, and segment if known - rough answers still unlock a sharper message.

---

## Hard Gate Before Writing

Emit a complete **Research Receipt** (format in the Receipt section) for each contact before writing that contact's message body. The Receipt requires literal search query strings actually run, paired with results: minimum 3 if claiming a cataloged signal, minimum 5 if claiming NONE. Contact-level finding required on every Receipt.

The Receipt is metadata above the body. It does not count against the LinkedIn 280-character cap.

## Length Target: 35-50 Words / Max 280 Characters

Target 35-50 words / max 280 chars (under LinkedIn's 300 hard limit). Long DMs are themselves a sequence-tool tell. Real humans send shorter DMs.

The sender intro is removed from the body (recipient sees sender from LinkedIn UI), which frees ~17 chars of budget for substance, not for length.

## Reference Files

- **context/outreach/voice-gold-standard.md**  -  **Hold open WHILE writing.** §A is the LinkedIn bar (the three Cooper-flagged craft-voice messages). Imitate the register; never reuse exemplar phrasing verbatim.
- **context/outreach/email-writing-rules.md**  -  Core outreach philosophy: angle-first, research as fuel, segment lock, public-signal observations, § Craft Voice (the cold-conversion register), banned brand-voice constructions, "fabric-in-a-box" ban in cold body, "Federation" verb ban (noun phrase "Federated Private Networking" allowed only in partner-facing collateral). LinkedIn follows the same philosophy, adapted to the LinkedIn length target.
- **context/copy-strategy/segment-language.md**  -  **Read this before writing.** Insider vocabulary, daily reality, conversational patterns, and insider vs outsider examples per segment. This is how you sound like you've been in their world, not like you researched them.
- **context/copy-strategy/segment-messaging.md**  -  Per-segment value-prop matrices and embed-by-contrast templates. Network Operator §5 is split into Tier 1 (Global + National) vs Tier 2/3 Regional Wholesale lead motions.
- **context/core/messaging-framework.md**  -  Segment-specific messaging rules and positioning
- **context/outreach/persona-targeting-blocklist.md**  -  **Pre-write gate.** Titles excluded from standard LinkedIn batch cadence (Director-Carrier-Wholesale, Director-Field-Operations, Country-Manager-at-HQ-product-org, Account Executive, CSM). See "Persona Pre-Check" below.
- **context/outreach/pre-cadence-hygiene.md**  -  **Pre-write gate.** LinkedIn-status check on lead pull is one of three list-hygiene filters that run before any contact enters the cadence.
- **context/outreach/sender-profiles.md**  -  Sender identities, territories, voice characteristics (sender intro is NOT in the LinkedIn body - recipient sees sender from LinkedIn UI)
- **context/copy-strategy/outbound-playbook.md**  -  Multi-touch sequence cadence (LinkedIn connect defaults to Day -3, before Email 1)
- **Segment cheatsheets** (context/segments/colocation.md, context/segments/fiber-operator.md, context/segments/neocloud.md, context/segments/network-operator.md, context/segments/msp-aggregator.md, **context/segments/enterprise.md**)  -  Deep context for pain points, discovery questions, and competitive landscape per segment
- **context/signals/signal-framework.md**  -  Universal signal types, scoring, noise list. Required for the Public Signal Cited rule.
- **context/signals/[segment]-signals.md**  -  Per-segment cataloged signals. The `Pattern:` field for each cataloged Tier A signal becomes the actual web search query when grounding a LinkedIn message. Required reading for the segment being targeted.
- **context/account-tiering/sub-segment-qualification.md**  -  Authoritative list of the 30 active `company_sub_segment` values. Use the exact case-sensitive HubSpot string when referencing sub-segments.
- **context/account-tiering/enrichment-protocols.md**  -  Canonical definitions of `account_brief`, `recent_news_or_trigger_event`, `fabric_provisioning_approach`, and `geographic_focus` - the four enriched fields that ground LinkedIn angle selection in real prospect substance.
- **context/hubspot/territory-model.md**  -  Authoritative 5-region sender map. Load at runtime for Central/Europe routing; apply `get_owner()` instead of hardcoded state lists. Required for every sender selection decision.
- **context/europe/europe-email-compliance.md**  -  LinkedIn-first is legally required (not just stylistic) for DE/AT/IT; cold LinkedIn without opt-in is unlawful in those countries. Gate every European contact through this file before routing.
- **context/core/icp-playbook.md**  -  Per-role pain language by segment. Use for the swap test and to sharpen the contact-angle choice when the role is ambiguous or the contact-level research is thin.
- **context/europe/sovereignty-positioning.md**  -  DORA/NIS2 sovereignty angle for Markus Hendrich / European prospects. Required when the sender is Markus or the prospect HQ is in Europe.
- **context/signals/universal-platform-signals.md**  -  AP-1/AP-3/AP-7 openers for contacts where no segment-specific cataloged signal exists; use as the NONE-posture angle source before falling back to inferred segment pain.

## Persona Pre-Check (Pre-Write Gate, Mandatory)

Before writing any LinkedIn DM, verify the contact's title is NOT on the persona-targeting blocklist (`context/outreach/persona-targeting-blocklist.md`) - the same persona model gates LinkedIn DMs and cold-email batches. It blocks four buckets: universal (Account Executive / Account Manager / CSM), aggregator-NaaS-TSD (Director-Carrier-Wholesale / Wholesale Manager / Director-Sales-Wholesale), fiber-ISP (Director-Field-Operations / Regional Ops Manager), and international-carrier (Country Manager at HQ-product orgs / Finance Director). Full list + rationale in that file.

If the contact title is on the blocklist, do NOT write a LinkedIn DM. Surface the contact in the Cooper-review queue.

## The Philosophy (Same as Email)

Research is fuel, not content. The short message should read like a peer who understands their world, not a salesperson who found them on LinkedIn. The recipient should think "that's my life" not "this person looked me up." A specific public-signal observation ("saw the BEAD subgrant for Eastern Texas") proves the writer actually looked at something concrete, not just inferred from segment patterns.

The difference from email: you have room for exactly one problem statement and a soft ask. No context bridge, no value connection, no structure. Just the sharpest possible version of "I understand your problem."

**Earned-Problem Doctrine (canonical in email-writing-rules.md).** At 35-50 words there is no room
to recover from an offending claim. Lead with a problem the contact is publicly talking about or will
predictably hit as they grow - framed forward-state, never as a verdict on their current setup - then
the one easy-solution line. Never assert how their business runs today unless a public signal proves it.

## Angle Selection: Company + Contact (Mandatory)

The angle is chosen at the intersection of the company's situation AND the contact's role. Research runs in two stages before writing, never collapsed into one. The same company gets a different LinkedIn message depending on whether you're reaching the CTO or the CEO. This mirrors the canonical rule in email-writing-rules.md "Research Sequence."

**Step 1  -  Research the company:** What is their specific situation? Expanding? Losing tenants? Building AI infrastructure? Acquired someone? The company research tells you what's happening.

**Step 2  -  Research the contact:** What is their role? What do they own? What keeps them up at night? A CTO cares about architecture gaps. A CEO cares about competitive threats. A VP Sales cares about deals lost to provisioning delays. The contact research tells you which facet of the company's situation matters to THIS person.

**Step 3  -  Fuse into one angle:** The message names a problem that is specific to this company AND relevant to this contact's responsibilities. If the message could be sent to a different person at the same company with no changes, the contact angle is missing. If it could be sent to the same role at a different company, the company angle is missing.

**Examples of the intersection:**

| Company situation | Contact: CTO | Contact: CEO |
|-------------------|-------------|-------------|
| Expanding into new states | "Every new market means another 60-day NNI build" (his engineering team's bottleneck) | "Expansion doesn't pay off if provisioning can't keep pace with the sales team" (her revenue timeline) |
| GPU tenants asking for interconnects | "Deterministic paths between GPU clusters shouldn't take weeks to provision" (his architecture gap) | "Tenants shopping for interconnection elsewhere is revenue walking out the door" (her competitive threat) |
| Multi-carrier aggregation | "Blind once traffic enters upstream carriers" (his visibility problem) | "SLA penalties on paths you can't see" (her margin risk) |

**How to fit this in 35-50 words / 280 characters:**
- The company detail and the contact relevance get baked into one problem statement
- You don't say "as a CTO" or label their role. The problem itself signals you understand what they own.
- "I'd guess cross-carrier circuits in your newer markets are still eating weeks"  -  this only works for someone who owns network provisioning at a company that's expanding. It's both company-specific and contact-specific without naming either.

**Priority when hitting the 280-char wall (cut in this order):**
1. Keep the contact-relevant problem  -  this is what makes them read it
2. Keep the company-specific detail  -  this is what makes it credible
3. Cut generic segment pain  -  if it could apply to anyone, it goes first
4. Shorten the CTA  -  "Worth connecting?" is 18 chars. That's your budget.

## Sender Selection

The sender is the person who will appear as the connection-request initiator in LinkedIn's UI. Use the same territory-based sender logic as email. The authoritative 5-region map and owner IDs live in `context/hubspot/territory-model.md` - load that file and apply `get_owner()` at runtime. Do NOT inline or hardcode state lists here.

Current senders: Tim Lieto (Northeast + West interim, 161889085), Ken Cunningham (Southeast, 162339176), Tory Teague (Central, 165480917), Markus Hendrich (Europe, 164949459), Tim Ziemer (International + Tier 1 SP, 159350430), Cooper (Unassigned, 160267902). Region boundaries are in `context/hubspot/territory-model.md`.

See `context/hubspot/territory-model.md` for the full territory definitions and state-to-region mapping. For European prospects, Markus Hendrich applies European compliance + sovereignty framing; LinkedIn-first is legally required (not stylistic) in DE/AT/IT.

Founder senders (Abilash, Timothy Ziemer) can be used for LinkedIn when the email sequence uses a founder sender. Match the sender across channels.

**Sender identification happens via LinkedIn's UI, NOT in the message body.** The recipient sees who sent the connection request automatically. Adding "Tim from MaiaEdge." to the body is redundant and triggers the sales-pitch reflex before they read the actual message.

## Format - Craft Voice Is the Default

The default register is the CRAFT pattern (the Cooper-flagged bar, voice-gold-standard.md §A). Four moves in ≤280 chars:

```
[First name], [structural truth of their world, competence credited]. [Craft line: "the layer I work on" / "what I spend my days on" + one concrete mechanic]. [Honest-reason or micro-ask close].
```

**The three calibration messages (imitate the moves, never the words):**

> Sergio, you know better than most that every operator in an alliance brings its own network, so each integration tends to get engineered from scratch. The layer I work on lets partners plug in once and reuse it, which felt close enough to your patch to be worth connecting.

> Matt, customers mostly reach GPU clouds over whatever path they can arrange, which means the product's last hop is best-effort no matter how good the compute is. Fixing that hop is what I spend my days on, and it felt close enough to your world that connecting made sense.

> Jeffery, Megaport raising close to $600M to move into compute signals the network's becoming part of the AI product. Arc tunes GPUs to the limit, so the path into them is the next place performance leaks. We're working with other neoclouds on owning it. Open to connect?

Market-catalyst openers (the Jeffery pattern) are for COMMERCIAL seats only, one light clause, calibrated to whether THIS reader would assign the signal weight. Deep-technical seats get the lived problem (the Matt pattern); cut the catalyst entirely.

**No sender intro in the body.** Sender identification happens via LinkedIn's UI when the connection request lands. `"[Sender first name] from MaiaEdge."` in the message body is BANNED. Everything sends from reps and co-founders - the message must sound like a practitioner, never an SDR.

**Length target:** 35-50 words. **Hard cap: 280 characters - count and EMIT the count** under every message as `char count: N/280`. (Over-cap messages are truncated or rejected by LinkedIn; a message without an emitted char count fails QA.)

**Public-signal observation opener** stays available when a cataloged signal exists ("saw the [signal type]") - same Public Signal Cited rule as cold email.

**Closes:** honest-reason ("felt close enough to your patch to be worth connecting"), micro-ask ("Open to connect?" / "Worth connecting?"), or no CTA when a strong illumination question carries the close. Never the same close twice within an account; no close on >20% of a batch.

## Research Receipt (Hard Gate Before Each Message)

Every LinkedIn message must be preceded by a **Research Receipt** block above the message body. A message without a Receipt is invalid output.

### Lookup sequence (pre-write)

1. **Web search grounded against the segment's signals catalog** (`context/signals/[segment]-signals.md`). Use the `Pattern:` field for each Tier A signal as the literal query. Run minimum 3 Tier A pattern searches. Stop if a HIGH-confidence Tier A hit lands. If no Tier A hits, expand to Tier B.
2. **Contact-level search:** `[Contact Name] [Company] LinkedIn` - pull role, tenure, recent activity, what they own. Required on every Receipt, even when the company-level search finds a signal. The same company gets a different message for CTO vs CEO; that is impossible without contact-level research.
3. **If web search and HubSpot both find nothing across at least 5 query attempts**, mark Signal code = NONE, posture = ASKED, and document the literal queries in the Receipt.

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
Anchor in the message: [the ONE company/contact-specific fact from the findings above that the message is built on] → Swap test: [why this message would NOT make sense sent to a different company in the same segment]. If you cannot name a non-generic anchor, the message is a template - reframe or mark RESEARCH INCOMPLETE.

Signal code: [F-A1 | NC-A2 | NO-B3 | NON-CATALOG | NONE]
Posture: [DIRECT | ASKED] - [one-line reason tied to the finding above]

---

[recipient first name],

[message body, 35-50 words, under 280 characters]
```

### Refuse-to-write rule

If you cannot honestly fill all required sections (Searches Run with at least 3 literal queries paired with results, Company-level finding, Contact-level finding, Load-bearing assumption, Anchor-in-the-message with its swap test, Posture with reason), output `RESEARCH INCOMPLETE: [specific reason]` in place of the message body and move on. Do NOT fabricate a Receipt. The Anchor field is the output gate: if the message is not built on a named company/contact-specific fact (if it would still read as sent-to-them with a different company name swapped in), it is a segment template and is invalid output even when the searches were run - re-research or reframe, do not ship it. If the load-bearing assumption is UNVERIFIED and asserts how their business works today (for example that they have not already solved the problem), the angle is not ready - reframe forward-state or cut before writing.

## Contact Angle Quick Reference

Use this to decide which facet of the company's situation to lead with based on the contact's role. The company research gives you the situation. This table tells you how to frame it for THIS person.

| Role | What they own | Frame the company situation as... |
|------|--------------|-----------------------------------|
| CEO / President | Revenue, competitive position | A competitive threat or revenue at risk |
| CFO | Margins, cost structure | Cost of the current approach or margin erosion |
| COO | Operations, headcount, scale | An operational bottleneck they can't scale past |
| CTO / VP Engineering | Architecture, reliability | A technical limitation or architecture gap |
| VP Sales / Commercial | Pipeline, win rate | Deals being lost or delayed by provisioning |
| VP Network / Infrastructure | Uptime, visibility, tools | A visibility gap or manual burden on their team |
| CSO / CISO (Enterprise) | Audit-ready policy enforcement, encryption, data sovereignty | A regulatory exposure (HIPAA/PCI-DSS/SOX/GDPR) or audit-trail gap |
| Network Architect / Principal Network Engineer (Enterprise) | Inter-DC redundancy, Type 2 visibility, BGP burden | A specific architecture pain ("HAsync and HAfabric share a single dark fiber pair," "Type 2 is a black hole") |

**The test:** If you swap this contact for someone in a different role at the same company, the message should change. If it doesn't, the contact angle is missing.

## Verify Segment (Mandatory Before Writing)

After researching the company, verify that the segment in HubSpot (or the source spreadsheet, or whatever the user provided) actually matches what research reveals about the company.

**Check:**
- Does the segment match what you found? (e.g., classified as "Data Center Colo Provider" but research shows they're actually a fiber operator, or listed as "Network Operator" but they're really an MSP aggregating circuits)
- For colos: Did you find AI signals? If strong, sub-segment should be "AI Infrastructure" not "Standard"
- Is this company actually on the exclusion list? (IXP, Tower REIT, IT MSP, software vendor, etc.)

**If mismatch:** Flag: `SEGMENT CORRECTED: [Source] says [X], research says [Y]. Using [Y] for messaging.` Then load the CORRECT segment's vocabulary and write the message to the corrected segment.

**If confirmed:** Note: `Segment verified: [segment] / [sub-segment]`

Use the CORRECT segment for all message writing, regardless of what the source data says.

<!-- Canonical source: context/copy-strategy/segment-language.md -->
## Segment Lock (Mandatory Before Writing)

Before writing any LinkedIn message:

1. **Confirm the segment** from the verification step above (use the corrected segment if research revealed a mismatch).
2. **Read segment-language.md** for that segment's vocabulary, daily reality, and conversational patterns.
3. **Use ONLY that segment's vocabulary.** If a term belongs to another segment, it is BANNED from this message. Using colo terms ("meet-me room," "attach rate") when targeting a fiber operator ("route miles," "NNI") breaks credibility instantly.
4. **Use their words, not ours.** Say "dark fiber sitting idle" not "underutilized assets." Say "deal at risk" not "business impact." Say "pointing fingers" not "operational complexity." The segment-language.md file has the translations.

The test from segment-language.md applies: would someone with 15 years in this segment read the message and think "this person gets it"? Or "this is a salesperson"?

At 35-50 words you only have room for the words that earn their place. Make every one of them an insider word.

<!-- Canonical source: context/outreach/email-writing-rules.md -->
## Tone Rules

Write the way a person types a message to a peer they respect. The six human-voice qualities from email-writing-rules.md apply here too, EXCEPT the specific-mechanic peer line (no room for it under the char cap - see the note in the banned-phrase list below). In priority order:

1. **Reasoning flows; facts don't stack.** Connect your reasoning with so / since / but / even though - that connective tissue is the biggest tell that a human wrote it. One bare fragment per body, max. Don't stack three clipped declaratives.
2. **Say the thing; don't announce it.** State the point as a clause, not a labeled section. No "here's the thing," no colon-prefixed setups, no "what caught my eye."
3. **Talk to them.** Active voice, second person. "Your team provisions," not "the team provisions." A DM written about them reads like a report; one written to them reads like a person.
4. **Plain words, kept industry words.** Swap the consultant words (productizing → sell / turn up; operating model → way of working; addressable / TAM → the sites you can reach; monetize → new revenue / get paid for, but keep operator-native "monetize idle fiber"; leverage / utilize / enablement / "solution" → plain words). Keep the insider terms they actually say - DIA, NNI, off-net, route miles, lit / dark, meet-me room, cross-connect, attach rate, GPU cluster, deterministic paths. Those read peer.
5. **Honest, spoken uncertainty.** When you're inferring, sound like a person being straight: "hard to tell from outside," "tends to," "usually." Keep the 30% hedge cap on "I'd guess" / "I'd imagine."
6. **Rhythm.** Vary sentence length. A connected sentence next to a short one lands; three stacked fragments read as ad copy.

Plus the LinkedIn-specific rules:

- **Peer to peer.** This is one professional connecting with another. Not a pitch.
- **Problem-first.** Lead with what's broken in their world, not what MaiaEdge does.
- **No flattery.** No "impressive growth" or "love what you're building." Lead with the problem.
- **Genuine curiosity.** "Worth connecting?" signals you want to learn, not sell.
- **Enterprise provisioning-simplicity language:** In Enterprise DMs, prefer "anywhere to anywhere with a click" over "no routing complexity," especially for CIO / CFO personas. In operator and neocloud DMs, "no routing complexity" is canonical.

## Enterprise (Multi-DC ICP) - Compressed Voice Guide

Enterprise is the customer, not an operator selling to one. Drop operator-monetization framing in Enterprise DMs.

### Public signals to anchor on (Enterprise)

LinkedIn DMs need ONE specific, recent signal as the credibility hook. Order of preference for Enterprise prospects:

1. **DC expansion / new DC announcement** - press release, 10-K disclosure, regional business journal. Strongest signal for the dark fiber redundancy lead.
2. **New VP Network / Director Network Engineering / Principal Network Engineer hire** - LinkedIn UI announcements, press releases. Strong signal for the technical-champion persona - they're inheriting legacy provisioning.
3. **M&A activity** - Mergermarket, S&P Global, company press. The network integration angle lands at any technical persona.
4. **AI workload announcement** - corporate IT press release, AI vendor case study. Pulls traffic in directions the network team didn't design for.
5. **Equinix Fabric / Megaport customer win** - Equinix or Megaport press / customer logo pages. Lets the message reference the third-party fabric dependency directly.

### Lead angles compressed for 35-50 words

| Sub-segment | DM angle template |
|---|---|
| **Retail and Distribution** | "Saw the [DC announcement / expansion]. The dark fiber between corporate DCs is usually one cut from an outage when it's a single pair, automated failover or no. Curious how you're handling that." |
| **Financial Services** | "Saw the [signal]. Inter-DC paths going best-effort across the WAN while compliance is asking to prove the path is the place every regulated peer I talk to has hit a wall. Worth connecting?" |
| **Healthcare Systems** | "Saw the [EHR / clinical-DC signal]. EHR DC redundancy on a single fiber pair is the most common HIPAA-adjacent risk I'm hearing from IDN network teams right now. Curious where you're at." |
| **Outsourcing Services** | "Saw the [delivery center / client win]. Multi-site delivery-center reliability + client data sovereignty is the conversation I keep landing in with BPO heads of network. Worth connecting?" |

### Persona compression for Enterprise (35-50 word target)

- **CIO / CTO**: lead with revenue / competitive / cloud framing. "Multi-cloud feels like one cloud" or "cloud on-ramp Megaport owns the SLA on" both land.
- **VP Network Infrastructure / Director Network Engineering**: lead with operational burden. "No headcount to run BGP across the WAN" / "every new DC is a six-month networking project" both land.
- **CSO / CISO**: lead with audit-trail / data sovereignty. "Compliance can prove the path" / "audit-ready paths" both land. HIPAA/PCI-DSS/SOX/GDPR mention is appropriate.
- **Network Architect / Principal Network Engineer**: lead with technical specificity. "HAsync and HAfabric on the SSRs share a single fiber pair" / "Type 2 is a black hole" both land. Most technical, lowest credibility-anchor risk.

### Enterprise DM banned phrases (extends global ban list)

In addition to the global ban list ("Federation," "I noticed," credibility anchors, etc.), Enterprise DMs cannot use: "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "wholesale activation," "tenant," "meet-me room," "interconnection revenue," "aggregator," "TSD." These signal the wrong business model.

### Reference

Full Enterprise positioning, sub-segment cheatsheets, persona pain language, objection reframes, and HubSpot mapping live in `context/segments/enterprise.md`.
- **Nudge, don't preach.** At 35-50 words you don't have room to overclaim. No absolutes ("the only way"), no prescriptive musts ("you need to"), no definitive diagnostics about their business. Hypothesis language ("I'd guess") or premise hedges ("Probably already on your radar, but…") beat declaring what their problem is. NOTE: brand-voice constructions ("most operators we talk to," "we keep hearing from operators") are BANNED in LinkedIn DMs as well as emails - use "I" voice ("the pattern I'm watching at"). See email-writing-rules.md "Diplomatic Claims" and "Banned Phrases."
- **Reply-worthy.** The goal is connection acceptance and a reply, not a pitch landed. If the message would feel like being told what to do, rewrite.

## Writing Rules

**Do:**
- One company-specific detail, baked into the problem
- Peer tone  -  like messaging someone you met at a conference
- End with "Worth connecting?" or similar low-friction ask
- Use their vocabulary, not ours
- **Sovereignty pairing:** Always pair speed with ownership. "Your team provisions in minutes" not just "provision in minutes." Exception: neoclouds (they ARE the customer, so data sovereignty language only  -  "sovereign by design," "paths you control"). [Canonical source: context/outreach/email-writing-rules.md]

**Never:**
- Em dashes, colons, and dashes-as-punctuation (spaced hyphen, double hyphen, en dash). Replace with commas or periods; hyphenated compounds (cross-connect, on-net) are fine
- Move-announcing transitions ("another angle on this," "one more thought," "quick thought," "worth a thought"). Just say the thing
- "I noticed" / "I saw" / "I came across" / "Following your work"
- "Impressive" or any flattery language
- Credibility anchors (no Acme Packet, no 128 Technology, no "$2.55B exits")
- Competitor names (say "third-party fabric" not "Megaport")
- "I'd love to" / "I'd be happy to" / "Let me know if"
- Pitching MaiaEdge features. The goal is connection acceptance, not a sale.
- Customer names (anonymize any proof points)
- **"Fabric-in-a-box"** in LinkedIn body. Use "interconnection layer," "service fabric," or "build your own fabric" in DM body instead. The phrase stays canonical in cheatsheets, the 101, sales enablement, and live conversations but does NOT appear in DMs.
- **"Federation" as a verb** ("federate with partners," "federation creates network effects") in LinkedIn body. Translate to segment-native vocabulary: "extend your reach," "sell into new markets," "connect to partners instantly," "reach beyond your footprint." The noun phrase "Federated Private Networking" is the MaiaEdge category descriptor and is allowed only in partner-facing collateral (101, cheatsheets, deck) - still banned in DM body.
- "We built carrier infrastructure that…" / "We built MaiaEdge for…" / "We help operators…" - brand-voice constructions BANNED in LinkedIn body. Use "I" voice ("I've been working on infrastructure that…"). **The full "we" ban holds for LinkedIn.** Email gets one carve-out - the specific-mechanic peer line ("We've been helping similar [cohort] [specific mechanic], so [plain outcome]") - but that is an EMAIL-only exception. At 35-50 words / 280 chars there's no room for it, so LinkedIn keeps the complete we-ban. Stay in "I" voice or second person.

## Sequence Integration

When used as part of a multi-touch sequence (see **outbound-playbook.md**), the connection request defaults to **Day −3, BEFORE Email 1** - the connect is the warm-up, the email carries the ask and books the meeting. On accept: thank-you DM + account one-pager within 24-48h per the branded-doc outbound variant, then the next email touch names one claim from the one-pager and carries the meeting ask. The thank-you DM, that post-one-pager email, and any verbal DM reply are written via the **warm-follow-up** skill (voice-gold-standard.md §E is its calibration set).

**Critical rule:** The LinkedIn message should NOT repeat Email 1's angle word-for-word. It should reference the same underlying problem from a different entry point. If Email 1 led with provisioning speed, LinkedIn might lead with the competitive threat that creates. Same problem, different lens.

If the prospect already received Email 1 and sees a LinkedIn request with identical language, it feels automated. The messages should feel like they came from the same person thinking about the same problem, not the same template executed across channels.

## Research as Fuel (Same Standard as Email)

The same principle from email-writing-rules.md applies here: research is fuel, not content. The research is invisible **by default** in the message; the one exception is a why-now signal you cite as an observation (see below). It exists in the message as:
- **The precision of the problem named**  -  could only come from knowing this company
- **The authenticity of the language**  -  uses their terms, not ours
- **The relevance of the angle**  -  addresses what this person actually deals with

**What this means at 35-50 words:** You don't recite their stats back to them ("40K route miles," "12 states," "30kW racks"). Instead, the research tells you WHICH problem to lead with. If you found a cataloged signal (BEAD subgrant, M&A announcement, exec hire), you can cite the signal directly with "saw the [signal]" - that's a public-signal observation, not research display. If you only have inferred patterns, you lead with the problem and skip the source citation. The bar for citing the signal: it ties to the value prop and creates urgency. A static stat (route miles, facility count) never earns the space; a fresh signal often does.

**The test:** Would someone with 15 years in their segment read this and think "this person gets it"? Or would they think "this person Googled me"?

### Research Display Detection (Scan Before Finalizing)

Before finalizing ANY LinkedIn message, scan every sentence for research display. At 35-50 words, even one displayed fact consumes a sizable chunk of your budget with something the recipient already knows.

**Scan for:**
- Company facts stated as standalone observations ("[Company] has [number] [things]")
- "Your [number] [thing]" patterns ("Your 50 data centers," "Your expansion into the Southeast")
- Opening sentences that DESCRIBE the company rather than NAME a problem

**If found:** Take the displayed fact, identify the PROBLEM it creates, and rewrite to name the problem without the fact. The fact selected the angle. The message names the problem.

**The display test:** Read the sentence aloud. If it sounds like you're telling the recipient something about their own company, it's research display. If it sounds like you're naming a problem they live with, it's research-as-fuel.

**Showing research (bad):**
"Your expansion into 3 new Southeast markets is exciting. I'd guess provisioning is a challenge."

**Research absorbed (good):**
"I'd guess cross-carrier circuits in your newer markets are still taking weeks. That's the part expansion doesn't fix on its own."

The first version displays the research ("3 new Southeast markets"). The second version uses the research to name the exact problem only someone who understood their situation would know to ask about.

## Examples

These show how the SAME company situation produces DIFFERENT messages depending on the contact. Research on the company selects the situation. Research on the contact selects the framing. All examples follow the standard format: NO sender intro, target 35-50 words, public-signal observation preferred opener, "I" voice, no brand-voice constructions.

**Note on examples:** The first example below shows the FULL Research Receipt above the message body - that is the required output format. The remaining examples abbreviate the Receipt to a single Signal code line for brevity in this reference doc. In real output, EVERY message must be preceded by a full Receipt (Searches Run, Company-level finding, Contact-level finding, Posture).

**Fiber Operator expanding into new states (cataloged signal F-A1: BEAD subgrant award):**

To the VP Engineering (full Receipt format shown):
> RESEARCH RECEIPT - Paul Janes @ Fatbeam
>
> Segment: Fiber Operator   Status: VERIFIED
> Catalog: context/signals/fiber-signals.md
>
> Searches run:
> 1. `"BEAD subgrant awarded" Fatbeam route miles` → texas-comptroller.gov/.../bead-q1-2026, 2026-03-15
> 2. `Fatbeam ("definitive agreement" OR "to acquire") fiber` → no Tier A hit
> 3. `Fatbeam ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit
>
> Company-level finding: F-A1 BEAD subgrant award. Texas Comptroller, 2026-03-15: $12M Eastern Texas middle-mile build.
> Contact-level finding: Paul Janes, VP Engineering since 2024. Owns provisioning. Recent LinkedIn posts on automation suggest he feels the cross-carrier NNI gap.
>
> Signal code: F-A1
> Posture: ASKED - illumination question fits a connection request even with a HIGH-confidence signal
>
> ---
>
> Paul, saw the Eastern Texas BEAD subgrant. The fiber's the easy part, but the cross-carrier NNI into the new market is usually where the 60-day clock starts and the revenue waits. Curious how you're sequencing that piece.

(37 words, 221 chars. ASKED posture, illumination question carries the close, no CTA.)

To the CEO:
> Public Signal Cited: F-A1 - BEAD Subgrant Award (Texas Comptroller, 2026-03-15)
>
> Paul, saw the Eastern Texas BEAD subgrant. The revenue clock doesn't start when the fiber's lit, it starts when the cross-carrier piece is done, so the win is paths your team turns up at the sales pace instead of waiting on the other carrier.

(44 words, 242 chars. DIRECT posture, embedded value bridge, no CTA.)

**Colocation Operator losing tenants to third-party fabrics (no cataloged signal - inferred):**

To the CTO:
> Public Signal Cited: NONE - using inferred segment angle
>
> Paul, probably already on your radar, but every cross-connect that runs through a third-party fabric is a tenant who's started shopping the reach next door, so the relationship drifts out of your meet-me room. Curious what the in-house alternative looks like for you.

(43 words, 267 chars. ASKED posture, premise hedge "probably already on your radar", illumination question close.)

To the VP Sales:
> Public Signal Cited: NONE - using inferred segment angle
>
> Paul, when a prospect asks for instant connectivity and the answer is "call a third-party fabric," the deal walks with the fabric, since whoever turns up the path owns the relationship. Worth a conversation about keeping that path in-house?

(39 words, 240 chars. DIRECT posture, no brand-voice "we help" construction, light CTA.)

**Neocloud with multi-facility GPU deployment (cataloged signal NC-A2: facility expansion):**

To the VP Infrastructure:
> Public Signal Cited: NC-A2 - New Facility Launch
> Source: Press release, 2026-02-10: Lambda Labs adding 3 facilities in Q2
>
> Paul, saw the three new facilities going live in Q2. Once inference starts crossing them, a slowdown is hard to pin down since it could be the carrier, the colo, or the middle-mile. Curious how your team runs that down.

(40 words, 219 chars. DIRECT opener (cataloged signal), illumination question close, no CTA.)

To the CFO:
> Public Signal Cited: NC-A2 - New Facility Launch
> Source: Press release, 2026-02-10: Lambda Labs adding 3 facilities in Q2
>
> Paul, saw the three new facilities going live in Q2. Public-internet egress between GPU clusters runs about 9c/GB at that scale, but private paths run closer to 2c/GB, so the gap compounds with every customer you add.

(37 words, 217 chars. DIRECT, embedded value bridge by contrast, no CTA.)

**MSP aggregating across multiple carriers (no cataloged signal):**

To the VP Engineering:
> Public Signal Cited: NONE - using inferred segment angle
>
> Paul, when a customer reports a path issue and three upstream carriers each say "not us," the real problem isn't the path, it's that once traffic leaves your network you can't see it. Curious how your team runs that down today.

(41 words, 227 chars. ASKED posture, illumination question, no brand-voice "we give you" construction, no CTA.)

To the CEO:
> Public Signal Cited: NONE - using inferred segment angle
>
> Paul, the Tier 1 carriers going direct to your customers are competing on speed, not relationship, so the asset-light advantage only holds if your visibility and provisioning keep pace with theirs. Worth a conversation?

(34 words, 219 chars. DIRECT posture, embedded value bridge by contrast, light CTA.)

**After these examples, always adapt with actual research.** Research on the company tells you the situation. Research on the contact tells you which facet to lead with. These examples show the principle. Your findings provide the substance.

## Off-Event LinkedIn Pattern

For LinkedIn DMs to contacts who are NOT attending an event (the default for most batches), drop the "coming to [event]?" opener and lead with a problem-anchored observation. The "coming to [event]?" opener is event-mode-only - using it off-event reads templated.

Off-event opener pattern:
```
[Recipient first name], [observation or question grounded in the cataloged signal you found, or in segment-native insider pain]. [Optional: one-sentence context]. [CTA or no CTA].
```

Off-event closing CTA patterns (use ONE per message; paraphrase - never the same close twice within an account):
- Honest-reason close: "felt close enough to your patch to be worth connecting."
- "Worth connecting?"
- "Curious how you're handling that."
- (No CTA - let the illumination question carry the close.)

The signal-grounded opener replaces "coming to [event]?" structurally: it's the credibility move that proves the writer actually looked at something concrete about THIS contact.

## Event-Specific LinkedIn Pattern

For pre-event outreach (conferences, trade shows), all LinkedIn messages follow this exact pattern:

```
coming to [event]? [one lowercase human sentence about why talking makes sense based on their Email 1 angle]
```

**Rules:**
- Opens with `coming to [event]?` -- lowercase, every message, zero variation
- No sender intro. No "Tim from MaiaEdge." Nothing before the opener.
- One sentence after the opener. All lowercase. Target 35-50 words / under 280 characters total.
- The sentence MUST be derived from the contact's Email 1 angle -- distilled, not generic.
- "I" voice, not "we" voice. No "we help operators" / "we fix that" / "that's what we solve" - these are brand-voice constructions banned across all MaiaEdge cold outreach.
- No flattery-as-problem-statement. No "the [thing] is the right play / strategic move / smart move" before the pain.
- Process sequentially. Read each contact's Email 1 before writing. NEVER batch-template.
- Different contacts at same company MUST get different messages (role-adapted angles).

**Quality test:** "If I removed the company name, could this message have been sent to any other company?" If yes, rewrite.

**8 Approved Examples (ITW 2026 -- use as calibration set):**

1. `coming to itw? summit broadband's fiber buildout is moving but the gap between routes lit and revenue flowing is usually where the real bottleneck lives.`
2. `coming to itw? as edgeuno adds sites across latam, the operational question is who controls the tenant connectivity layer at each facility, not just whether it exists.`
3. `coming to itw? firstlight's speed advantage is real but i'd guess it doesn't extend past your own footprint yet. cross-carrier provisioning is a different animal.`
4. `coming to itw? when airespring is competing for managed services deals, your delivery timeline depends on whichever upstream carrier moves slowest. curious how you're handling that.`
5. `coming to itw? 1547 is scaling fast with greenfield builds and acquisitions. the question is how quickly each new facility starts generating connectivity revenue, not just filling cabinets.`
6. `coming to itw? at 60 hudson with 300+ carriers, the differentiator isn't who's in the building. it's how fast tenants can provision cross-connects and get services live.`
7. `coming to itw? saw accelecom's expansion into eastern kentucky. new fiber sits idle until carrier interconnections go live, and that timeline is usually months not weeks.`
8. `coming to itw? the clearwave combined footprint only shows up as competitive advantage when delivery across both sides matches the speed of the sales pitch. curious where that stands.`

## Warm Contact Handling

This section governs warm TARGETING before the connection request goes out. Once the prospect accepts or replies, switch to the **warm-follow-up** skill - it owns every message after the prospect responds.

If the contact has HubSpot activity, classify them as WARM and modify approach.

**WARM classification (any of these):**
- HubSpot activity within 90 days (emails sent, meetings, calls)
- Company notes mention shared events (#MetroConnect26, #PTC26, #FiberConnect)
- Deal or POC history exists

**Warm LinkedIn rules:**
- Drop the sender intro. No "[First name] from MaiaEdge." Start directly with the warm context.
- Lead with shared context: "We've been in touch with a few folks at [Company]" or "I think we were both at [Event]."
- Shorter than cold  -  warm contacts need less convincing, more continuing.
- NEVER fabricate warmth. If HubSpot shows nothing, proceed cold. Do NOT fake familiarity.

## Batch Processing Rules

When writing LinkedIn messages for multiple contacts:
- **Process sequentially.** Read each contact's Email 1 before writing their LinkedIn message. Never batch-template.
- **Quality test per message:** "If I removed the company name, could this message have been sent to any other company?" If yes, rewrite.
- **Same-company contacts** get different messages based on their role and the facet of the problem they care about.

### Batch Quality Gates (5+ Messages)

When writing or reviewing 5+ LinkedIn messages:

1. **Read all messages in sequence first.** Don't finalize individually until you've seen the batch.
2. **Research display sweep:** Scan all messages for company facts stated as observations. At 35-50 words, displayed research is even more damaging than in email - every word is precious.
3. **Opening variety check:** Do all messages start with "[Name] from MaiaEdge"? For event batches, do all start with "coming to [event]?" Vary the sentence after the opener.
4. **CTA variety check:** Are all CTAs "Worth connecting?" Rotate: "Worth a conversation?" / "Make sense to connect?" / similar.
5. **Problem framing variety:** Are all messages leading with the same pain category (speed, visibility, cost)? Vary across the batch.
6. **Same-company check:** If multiple contacts at one company, verify each message addresses a different role-relevant facet.
7. **Length sweep:** Verify ALL messages target 35-50 words and under 280 characters. Flag any over the 280 cap.
8. **Sender intro check:** Verify NO message includes "[Sender] from MaiaEdge." in the body. The sender is identified by LinkedIn's UI; the in-body intro is BANNED.
9. **Research Receipt:** Verify every LinkedIn message has a complete Research Receipt above it (Searches Run with ≥3 literal queries, Company-level finding, Contact-level finding, Posture with reason). NONE without ≥5 queries above it is research-skipping.

### Event Pre-Outreach Batch Rules

For conference/trade show batches:
- Process sequentially. Read each contact's Email 1 before writing their LinkedIn.
- The "coming to [event]?" opener is mandatory and identical. Differentiation comes ONLY from the sentence after it.
- If 10+ messages in a batch, sample 3 random pairs and verify they could not be swapped between contacts.
- Flag any message where removing the company name would still make it sendable to a different company.

## Quality Checklist

- [ ] Target 35-50 words, max 280 characters - **char count EMITTED under the message** (`char count: N/280`); over-cap messages are rewritten, never shipped
- [ ] Craft register present (structural truth + "the layer I work on"-class identity line) OR a deliberate signal-opener variant; no exemplar phrasing reused verbatim
- [ ] Segment verified against research (if mismatch, corrected and flagged)
- [ ] If segment corrected, message uses corrected segment's vocabulary
- [ ] **NO sender intro in body** (no "Tim from MaiaEdge." / "Ken from MaiaEdge." - recipient sees sender from LinkedIn UI)
- [ ] **Opens with recipient's first name** followed by a comma, then directly into the observation/question
- [ ] **Research Receipt present above the message body** with all required sections complete: Searches Run (≥3 literal queries paired with results, ≥5 if claiming NONE), Company-level finding, Contact-level finding, Load-bearing assumption, Posture with reason. "NONE" without literal queries above it is research-skipping and fails this check.
- [ ] **Load-Bearing Assumption Gate:** the assumption the angle depends on is verified against a source or reframed forward-state. Never assert they have not already solved the problem without a source (assume competence). See `context/outreach/email-writing-rules.md` § The Load-Bearing Assumption Gate.
- [ ] **Public-signal observation opener preferred** when a cataloged signal exists ("saw the Tennessee build wraps in Feb")
- [ ] Angle is company-specific (could not be sent to another company in the same segment)
- [ ] Angle is contact-specific (could not be sent to a different role at the same company)
- [ ] Problem-first (not feature-first, not flattery-first)
- [ ] **Earned-Problem check:** names a publicly-grounded or forward-state growth problem (not an
  unverifiable current-state claim), framed without implying their setup is broken, with one
  easy-solution line.
- [ ] Research absorbed, not displayed (no reciting stats or facts back to them)
- [ ] **"I" voice, not "we" voice.** No brand-voice constructions ("We help operators…" / "We work with…" / "We give you…" / "We built carrier infrastructure that…" / "We built MaiaEdge for…" - all BANNED in LinkedIn DMs). The email-only specific-mechanic peer line does NOT apply here - it's a char-cap exception, so LinkedIn keeps the full we-ban.
- [ ] **No "fabric-in-a-box"** in DM body. Phrase is cheatsheet / live-conversation only.
- [ ] **No "Federation" as a verb** in DM body ("federate with partners," etc.) Translate per segment-language.md. "Federated Private Networking" noun phrase is partner-facing-collateral only - not in DMs.
- [ ] **Persona pre-check passed** - contact title is not on `context/outreach/persona-targeting-blocklist.md`.
- [ ] Correct sender for the territory (sender = LinkedIn account that initiates the request)
- [ ] CTA is OPTIONAL when a strong illumination question carries the close. If included, low-friction ("Worth connecting?" or equivalent).
- [ ] **Posture differs from E1** (per the per-sequence rotation rule). If E1 was DIRECT, LinkedIn can be ASKED, and vice versa.
- [ ] No em dashes, colons, or dash-as-punctuation anywhere (scan for ":", " - ", "--"; hyphenated compounds fine)
- [ ] No move-announcing transitions ("another angle," "one more thought," "quick thought")
- [ ] No banned phrases (see writing rules)
- [ ] No competitor names, customer names, or credibility anchors
- [ ] Doesn't repeat Email 1 language if part of a sequence
- [ ] Reads like a peer reaching out, not a sales tool executing
- [ ] Sovereignty language present (except neocloud)

---

## Logging (Mandatory - the channel is invisible without it)

LinkedIn accepts, DM replies, and one-pager deliveries are not queryable anywhere in HubSpot unless they are logged. The motion cannot be measured or improved without this protocol:

1. **On send:** complete the HubSpot LinkedIn task (task body = profile URL, blank line, message - per the standard task format).
2. **On ACCEPT:** write the DM text into the contact's `linked_in_message` property and log a note `LinkedIn accept YYYY-MM-DD`.
3. **On one-pager delivery:** log a note on the contact: `one-pager sent: [file name] via LinkedIn DM YYYY-MM-DD`.
4. **On DM reply:** log the reply text as a note (LinkedIn replies live nowhere else).

These four writes are the entire accept-rate / dual-channel funnel. Reps' 30 seconds per event buys the only measurement the channel has.

---

## Final Step: Signal Push-Back to HubSpot

**Runs AFTER the drafted LinkedIn DM is delivered to the rep - never before, never blocking.** Follow the canonical procedure in `context/signals/outreach-signal-pushback.md`: if your research surfaced a signal-grade event scoring ≥8 whose event date is newer than HubSpot's `last_signal_date`, write the five signal fields plus `account_tier` (only when `hs_is_target_account != true`), recompute heat per `context/account-tiering/tier-compute-spec.md` §11.5, do NOT bump `last_enriched_date`, and log the audit note. Skip silently on any failure - the rep already has their DM and R-Tier-Audit reconciles next run.
