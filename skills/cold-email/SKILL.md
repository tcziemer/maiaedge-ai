---
name: cold-email
description: Write cold outreach emails for MaiaEdge prospects. Use when asked to write, draft, or create a cold email, outreach email, or prospecting email for MaiaEdge. Requires prospect research and segment classification first. Emails written as Tim Lieto (AVP, North America Sales) or Ken Cunningham (Sales, East Region).
---

# MaiaEdge Cold Email Writer

## STOP — Read Before Each Run (Research Skip Detector)

The single biggest failure mode in this skill is writing the email body before doing the research, then back-filling a "Public Signal Cited: NONE — inferred angle" line to look compliant. That is research-skipping in disguise. Emails written that way are generic, and generic emails do not get replies. Our entire strategy hinges on relevance, and relevance is impossible without paired company + contact research.

**Hard gate:** Emit a complete **Research Receipt** (format in the dedicated section below) for each contact BEFORE writing that contact's email body. The Receipt requires literal search query strings that you actually ran. "NONE" alone is not enough — NONE must be paired with the literal queries that were tried and returned no Tier A or Tier B hits.

**Self-check before writing every email:** Look at your output above the email body for THIS contact. Do you see a Research Receipt with at least 3 literal queries paired with results, plus a contact-level finding line? If no, STOP. Run the searches now. Then come back and write.

If you find yourself drafting an email body without a Receipt sitting above it for that contact, you are skipping research. Stop and fix the order.

## Goal

Get a reply. Not close a deal. Not deliver a pitch deck. Just start a real conversation between two professionals who should be talking.

## Reference Files

When deployed in a project with reference files, also read:
- **segment-language.md**  -  **Read first.** Insider vocabulary, daily reality, conversational patterns per segment. This is how you sound like a 15-year industry peer, not a salesperson who read their website.
- **email-writing-rules.md**  -  Core email philosophy, angle-first principle, structure, segment lock, banned phrases
- **messaging-framework.md**  -  Segment messaging rules, cloud on-ramp use cases, language rules
- **sender-profiles.md**  -  Sender identities, voice characteristics, signature protocol
- **Segment cheatsheets** (colocation.md, fiber-operator.md, neocloud.md, network-operator.md, msp-aggregator.md)  -  Deep segment context for pain points and competitive landscape
- **signal-framework.md**  -  Universal signal types (U1-U6), Apollo signals (AP-1 to AP-7), free signals (FR-1 to FR-3), scoring model, noise list. Required for the Public Signal Cited rule.
- **[segment]-signals.md**  -  Per-segment cataloged signals (e.g., fiber-signals.md has F-A1 through F-A7 Tier A signals, plus F-B and F-C tiers). The Pattern: field for each cataloged signal becomes the actual web search query when grounding emails. Required reading for the segment being targeted.

## Active Senders

| Sender | Title | Territory | Notes |
|--------|-------|-----------|-------|
| Tim Lieto | AVP, North America Sales | West, Central, National accounts | Greater Boston based. Default sender if unspecified. |
| Ken Cunningham | Sales, East Region | Eastern US | Same messaging framework, same peer tone. |

If the user doesn't specify, ask. Both sign as themselves. Signatures are auto-appended by the email platform. Never write a signature block.

## The Tone

The email should read like a smart industry peer sat down, spent 10 minutes learning about the company and the person, and then wrote a short, direct note. Not a marketing email. Not a "just checking in." A note from someone who understands their world and has a genuine reason to reach out.

### The Human Test

Before sending any email, ask: "Would a real person actually write this?" If it sounds like it came from a sequence tool, rewrite it. If every sentence is doing obvious "work" (building rapport, establishing credibility, creating urgency, asking for the meeting), it will feel manufactured. The best emails have a few sentences that just... sound like a person talking.

### Tone Rules

- **Be direct, not polished.** Short sentences are fine. Fragments occasionally. The way people actually write emails to people they respect.
- **Show your homework without showing off.** Reference one or two specific things about their business that matter. Don't list every fact you found.
- **Use "I'd guess" and "I'd imagine" honestly.** These phrases work because they're genuinely humble. You're making an educated hypothesis, not a claim.
- **Let the research drive the email, not a template.** The structure exists as a guardrail, not a fill-in-the-blank.
- **One idea per email.** Pick the single most relevant angle for this person at this company and commit to it.
- **Don't over-personalize.** Mentioning their company and a relevant business context is good. Referencing their LinkedIn posts or quoting them back feels like surveillance.
- **Nudge, don't preach.** No absolutes ("the only way," "the single biggest"). No prescriptive musts ("you need to," "what you should do"). No definitive diagnostics about their business you can't actually know. Hypothesis language and relational framing only. See email-writing-rules.md "Diplomatic Claims" for the full guardrail.
- **Reply-worthy test.** After writing, read the email as the recipient. If replying would feel like submitting to a pitch, rewrite. The goal is peer engagement, not urgency manufacturing.
- **No credibility anchors in cold emails.** No "Same team that built Acme Packet" or "128 Technology." The message does the talking, not our history. Credibility anchors are for live conversations only.

### What Human Sounds Like (vs. Salesy)

**Salesy:** "I noticed [Company] has been expanding into new markets and I wanted to reach out because we help operators like you automate provisioning to accelerate service delivery."

**Human:** "[Company]'s expansion into the Southeast is smart. I'd guess the provisioning side hasn't caught up yet. Most operators in your position are still quoting 60-90 days for cross-carrier circuits."

**Salesy:** "MaiaEdge provides purpose-built infrastructure that enables operators to build their own fabric while maintaining complete sovereignty over customer relationships."

**Human:** "We built infrastructure that lets operators like you own the connectivity layer instead of handing it to Megaport. You keep the customer, the margin, the control."

**Salesy:** "I'd love to schedule a brief call to discuss how MaiaEdge can help [Company] transform their interconnection capabilities."

**Human:** "Open to a conversation?"

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

If the email could be sent to a different role at the same company without changes, Stage 2 is missing. Go back and research the contact before writing. See email-writing-rules.md "Research Sequence" for the canonical rule.

## Angle-First Principle

Before writing any email, identify the company-specific angle: the ONE thing happening at this company right now that creates an urgent, MaiaEdge-relevant problem. This could be an acquisition, a new build, a market expansion, a competitive threat, or a technology migration. State it in one sentence: "[Company] is [doing X], which means [specific operational problem MaiaEdge solves]." Then add the contact-level tailoring: "For [role], this means [facet of the problem this person owns]."

If the angle could apply to any company in the same segment, it's not specific enough. If it could apply to any role at this company, the contact-level tailoring is missing. Go back and research deeper.

**The angle must match reality, not the source data.** If the segment was corrected during verification, the angle must reflect what the company actually does, not what the original classification assumed.

## Email Structure (Angle-Driven, Problem-First)

Every email roughly follows this arc, but the company-specific angle drives the substance. The 4-part arc is a guideline, not a template — breaking it deliberately for authenticity is encouraged.

0. **First-name opener on its own line.** `Paul,` then a blank line, then the body. Every email in a sequence starts this way.
1. **Problem statement (1-2 sentences):** Lead with the company-specific angle, framed as the problem this person deals with. This IS the hook. Posture (DIRECT vs ASKED) depends on signal strength — see "Direct vs Asked Posture" below. Use hedges (premise hedges or "I'd guess"-style pain hedges) when inferring; skip hedges when you have a HIGH-confidence cataloged signal.
2. **Context bridge (1 sentence):** Connect their specific situation to the problem. Research absorbed into framing OR a specific public-signal observation ("Saw the Q3 release notes mentioned…" — see Email-Writing-Rules.md "Public-Signal Observations").
3. **Value connection (AT MOST 1 sentence):** How MaiaEdge relates to that pain. Two valid placements:
   - **EMBEDDED (preferred):** woven into the problem paragraph as a contrast clause. Example: "Routes go lit on schedule, but the cross-carrier piece is still a 60-day conversation. The fix is infrastructure that lets your team stand up those paths in minutes, under your brand."
   - **STANDALONE (allowed if punchy):** a single sentence after the problem paragraph, in "I" voice or product-as-outcome framing. Example: "I've been working on infrastructure that lets fiber operators stand up those paths in minutes, under your brand."
   BANNED: multi-sentence value bridge paragraphs. BANNED openers: "MaiaEdge is..." / "We help operators…" / "We built infrastructure that…" / "We work with…" Max 1 product-specific term per email (choose ONE: "carrier infrastructure" OR "fabric" OR "provisioning in minutes"). Use "I" voice, not "we" voice.
4. **CTA (1 sentence):** One question. Low friction. Optional when a strong illumination question carries the close.
5. **Peak-end observation (optional, 1 sentence MAX, only when meaningful):** A non-business observation tied to something specific about the recipient's company or location, separated from the CTA. Must pass the "forwarded by colleague" test (would the recipient find it odd if a colleague added the same line in a forwarded internal message?). NEVER in E2 or E3.

No credibility line. No sign-off. The message does the talking, not our history. Signatures are auto-appended by the email platform.

This is not a fill-in-the-blank template. The segment messaging framework provides vocabulary and proof points to support your angle, not a structure to fill in with company details.

**Non-functional voice required when there's something to say.** Every E1 should have at least one sentence that doesn't "do work" structurally (an aside, an honest acknowledgment of uncertainty, a peak-end observation). Don't force it. A forced non-functional sentence reads as performance.

**No flattery-as-problem-statement.** Sentences that approve of their strategy before naming a pain read as flattery even when the next clause names a problem. BANNED examples: "Growth through acquisition is the right play," "Building Tier-4 facilities is the hard part," "Your expansion is smart." Lead with the problem itself.

**No third-person case-study opener.** Extends the role-addressing ban. BANNED: "For a [role] at [type of company doing X]..." (e.g., "For a CFO at a fiber operator expanding into the Southeast..."). A peer doesn't frame their opener like a case study.

## CTAs

| Type | Examples | When |
|------|----------|------|
| Peer conversation | "Happy to share what we're seeing with similar [segment] operators. Open to a conversation?" | When you have relevant proof points. |
| Direct + relaxed | "Open to a conversation?" / "Worth a conversation?" / "Would a conversation make sense?" | Default energy. Rotate these. |
| Problem-anchored | "Dealing with something similar?" | Technical buyers who like to problem-solve. |

**CTA rules:**
- ONE question. Never stack two asks.
- No "I'd love to..." or "I'd be happy to..." (vendor language)
- No "Let me know if..." (passive, easy to ignore)
- No calendar links in first email
- No "quick call" (signals desperation)

<!-- Canonical source: context/outreach/email-writing-rules.md -->
## Writing Rules

**Do:**
- Periods for sentence breaks
- Short sentences. Sometimes fragments.
- Active voice
- Specific numbers when they matter (60-90 days, 80-90%)
- Reference their actual business, not their industry generically
- Acknowledge what they've built before positioning a gap
- **Use "I" voice instead of "we" voice.** "I've been seeing this with…" / "The pattern I'm watching at…" / "I've been talking to operators in your position who…" The email is from Tim or Ken to Paul, not from MaiaEdge to operators-like-Paul. Let the senders speak as themselves.
- **Cite specific public-signal observations when you have them.** "Saw the Q3 release notes mentioned…" / "Caught your panel at MetroConnect" / "Your last earnings call mentioned…" / "Noticed the announcement said X three times." These prove the writer looked at a specific thing and had a thought about it. Reference the segment signals catalog (`context/signals/[segment]-signals.md`) for what counts as a cataloged signal.

**Never:**
- Em dashes. Never. Replace with periods or commas.
- "Hope this finds you well" or any greeting filler
- "Just wanted to reach out"
- "As a [role title]..." (don't label them)
- "I noticed..." (the PHRASE; specific "Saw…" / "Caught your panel…" observations are allowed and encouraged — see Public-Signal Observations rule)
- "Saw your post..." / "Following your work..." (LinkedIn surveillance)
- "Revolutionary" or "game-changing"
- Customer names in cold emails (anonymize: "one fiber operator" not "Arvig")
- Competitor names in cold emails (NEVER write "Megaport" or "Equinix" or "Lumen" by name. Use "third-party fabric providers" or "someone else's fabric")
- Session-smart routing as a lead
- "Same team that built Acme Packet" / "128 Technology" / any credibility anchors (save for live conversations only)
- **Brand-voice constructions.** BANNED: "We help operators…" / "We work with…" / "We've been doing this with…" / "Many of the operators we talk to…" / "Most operators we talk to…" / "What we keep hearing from operators…" These are us-to-a-category sentences inside a person-to-person email. Use "I" voice replacements above.
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

See email-writing-rules.md "Research Display Detection" for the full translation table.

## Research Receipt (Hard Gate Before Each Email)

Every email this skill produces must be preceded by a **Research Receipt** block ABOVE the email body. This is a hard gate. An email without a Receipt is invalid output — restart that contact from research.

The Receipt replaces the older "Public Signal Cited" block. The old block let the writer drop in "Public Signal Cited: NONE — inferred angle" without proving any search effort, which is research-skipping in compliant clothing. The Receipt fixes that by requiring the literal search query strings that were run, paired with their results.

### Lookup sequence (mandatory pre-write)

HubSpot's `recent_news_or_trigger_event` field is populated weekly by `weekly-signal-scan` and can be stale mid-week. Web search is the primary source; HubSpot is confirmation only.

For every contact, before writing:

1. **Web search grounded against the segment's signals catalog** (`context/signals/[segment]-signals.md`). Use the `Pattern:` field for each Tier A signal as the literal query. Run a minimum of 3 Tier A pattern searches. If a HIGH-confidence Tier A hit lands, stop — that's the signal. If no Tier A hits, expand to Tier B.
2. **Contact-level search:** `[Contact Name] [Company] LinkedIn` — pull role tenure, recent activity, what they own. This populates the Contact-level finding line. The contact search is NOT optional, even when the company-level search finds a signal.
3. **Cross-check HubSpot `recent_news_or_trigger_event`** for confirmation or additional context. Web search wins where they disagree.
4. **If web search and HubSpot both find nothing across at least 5 query attempts**, mark Signal code = NONE, posture = ASKED, and document the literal queries you ran in the Receipt.

The web search MUST be grounded in catalog patterns, not generic "[company] news." That's what enforces the signal taxonomy and prevents the writer from grabbing whatever press release looks shiny.

### Receipt format (mandatory)

```
RESEARCH RECEIPT — [Contact First Last] @ [Company]

Segment: [segment / sub-segment]   Status: VERIFIED | CORRECTED from [X]
Catalog: context/signals/[segment]-signals.md

Searches run (literal query strings — not paraphrased):
1. `[exact query you ran]` → [URL + date, OR "no Tier A hit"]
2. `[exact query]` → [URL + date, OR "no Tier A hit"]
3. `[exact query]` → [URL + date, OR "no Tier A hit"]
[minimum 3 if claiming a cataloged signal; minimum 5 if claiming NONE]

Company-level finding: [signal description with source quote + date, OR "NONE — no Tier A or Tier B hits across [N] searches"]
Contact-level finding: [what THIS specific contact owns / recent role activity / why they care about THIS facet of the problem. REQUIRED on every Receipt, including when company finding is NONE.]

Signal code: [F-A1 | NC-A2 | NO-B3 | NON-CATALOG | NONE]
Posture: [DIRECT | ASKED] — [one-line reason tied to the finding above]

---

Subject: [subject line]

[email body]
```

### Why each section enforces what it does

- **Literal queries** make faking research more expensive than running it. Writing 3 to 5 specific query strings is roughly the same effort as actually running them — but only running them produces real findings.
- **NONE costs more than success** (5 queries vs 3). This inverts the old incentive where the path of least resistance was to declare NONE and skip the work.
- **Contact-level finding is its own required line.** The old block let writers fold contact research into the company line or skip it entirely. A separate line forces the two-stage Research Sequence (Stage 1 company, Stage 2 contact) to actually happen.
- **Each query gets its own result line.** Listing queries without per-query results fails the format and is detectable on review.

### Refuse-to-write rule

If you cannot honestly fill all four sections (Searches Run with at least 3 literal queries paired with results, Company-level finding, Contact-level finding, Posture with reason), you are not ready to write this email. Output `RESEARCH INCOMPLETE: [specific reason]` in place of the email body and move on. Do NOT fabricate a Receipt to look compliant.

### Examples

**Cataloged signal found:**

```
RESEARCH RECEIPT — Paul Janes @ Fatbeam

Segment: Fiber Operator   Status: VERIFIED
Catalog: context/signals/fiber-signals.md

Searches run:
1. `"BEAD subgrant awarded" Fatbeam route miles` → texas-comptroller.gov/.../bead-q1-2026, 2026-03-15
2. `Fatbeam ("definitive agreement" OR "to acquire") fiber` → no Tier A hit
3. `Fatbeam ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit

Company-level finding: F-A1 BEAD subgrant award. Texas Comptroller, 2026-03-15: Fatbeam awarded $12M for Eastern Texas middle-mile build. 45 days old, within Tier A window.
Contact-level finding: Paul Janes, VP Engineering at Fatbeam since 2024-08. Owns network provisioning. LinkedIn shows recent posts on automation tooling — likely already feels the cross-carrier NNI gap acutely.

Signal code: F-A1
Posture: DIRECT — HIGH-confidence cataloged signal, technical buyer (VP Engineering)

---

Subject: Fatbeam Eastern Texas

Paul,

[email body]
```

**No signal found (NONE — note the higher search count):**

```
RESEARCH RECEIPT — Paul Janes @ ATN International

Segment: Network Operator   Status: VERIFIED
Catalog: context/signals/network-operator-signals.md

Searches run:
1. `ATN International ("definitive agreement" OR "to acquire")` → no Tier A hit
2. `ATN International BEAD subgrant route miles` → no Tier A hit
3. `ATN International ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit
4. `ATN International ("AI data center" OR "hyperscaler" OR "GPU") fiber` → no Tier A hit
5. `ATN International earnings call provisioning` → no Tier B hit

Company-level finding: NONE — no Tier A or Tier B hits across 5 searches. Last cataloged signal in HubSpot is from 2025-09 and now stale.
Contact-level finding: Paul Janes, CTO. Joined ATN 2023, came from Liberty Networks where he ran cross-Caribbean network ops. Background suggests he's lived the multi-jurisdiction provisioning problem firsthand.

Signal code: NONE
Posture: ASKED — no public signal, inferring; technical buyer but inference requires hedge
```

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

See email-writing-rules.md "Direct vs Asked Posture" for canonical text.

## Role-Addressing Language (Banned)

These patterns are BANNED. They make the sender sound like a consultant, not a peer:
- "At the [role] level" -- positions sender below recipient
- "From a [function] standpoint/perspective" -- consultant-speak
- "For an operator [doing X]" -- third-person case study voice
- "At your scale" / "At the pace you're..." -- frames their situation from outside

**Instead:** State the problem directly. A peer says "the fiber buildout is moving, the question is how fast it starts paying for itself." Not "at the CEO level, I'd imagine revenue conversion matters."

## Sequence Rules (HARD CAPS)

### Email 1: 70-85 Words

- **70-85 words.** Count before finalizing. Applies across every segment; overrides segment soft floors.
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

Cap "one operator told us..." at 1 per 3-email sequence.

### Email 3: 2-3 Sentences, Single CTA, "Show Is Coming Up" Energy

- **2-3 sentences max.** Not "3-4." Not "a short paragraph." Two or three sentences, full stop.
- **First name on its own line**, blank line, body.
- **Exactly ONE CTA.** Not two asks. Not a CTA plus "hope to cross paths." ONE close.
- **"Show is coming up" energy.** Timing nudge, not graceful exit, even outside explicit Event Mode. There's a window closing (event date, quarter end, buildout milestone) and that's the reason to engage now. Forward-leaning, not resigned.

**Banned pattern:** "If [X] is worth a conversation... Either way, hope to cross paths." Pick one.

### Hedge Variety (Batch Processing)

"I'd guess" and "I'd imagine" are capped at 30% of Email 1s in any batch of 10+. The rest must use alternative constructions: direct assertions, illumination questions, premise hedges ("Not sure if you're already solving this, but…" / "Probably already on your radar, but…"), peer observations, market observations, role-native voice. See email-writing-rules.md "Hedge Variety Requirement."

<!-- Canonical source: context/outreach/email-writing-rules.md "Sequence Length & Structure (HARD CAPS)" -->
## Word Count Limits (HARD CAPS)

| Email | Limit | Structure |
|-------|-------|-----------|
| Email 1 | 70-85 words | 1-3 paragraphs, proper spacing, first name on its own line |
| Email 2 | Under 55 words | First name on its own line, no re-intro, no meta-references |
| Email 3 | 2-3 sentences max | First name on its own line, exactly one CTA, "show is coming up" energy |

These caps apply across every segment and override segment-specific targets. A tight, relevant email under the cap is always better than padding. NEVER pad with observations, flattery, or restated value props. Count words (Email 1, 2) and sentences (Email 3) before finalizing.

The per-segment targets in segment-messaging.md remain as tone calibration — they inform density and technical depth, NOT length.

## Subject Lines

Short. Specific to them. Not clever.

**Good:** "Fatbeam provisioning" / "[Company] interconnection" / "Cross-carrier paths at [Company]"
**Bad:** "Unlock new revenue streams" / "The future of private connectivity" / "Quick question"

<!-- Canonical source: context/copy-strategy/segment-messaging.md -->
## Role-Based Pain Matrix

| Role | What They Care About | Lead With | Avoid |
|------|---------------------|-----------|-------|
| CEO/President | Revenue, competitive position, market share | Strategic outcomes, competitive moat, market timing | Technical details, operational metrics |
| CFO | Cash flow, CapEx vs OpEx, ROI | 80-90% cost reduction, OpEx model, clear payback | Architecture, technical terms |
| COO | Operational efficiency, headcount, scalability | Scale without headcount, automation | Strategic vision, technical architecture |
| CTO/VP Engineering | Architecture, reliability, integration complexity | Protocol-free, API-driven, no MPLS/BGP | Revenue metrics, strategic positioning |
| VP Product | Roadmap, time-to-market, competitive features | Launch services in weeks not months, fabric-in-a-box | Operational details, cost metrics |
| VP Sales/Commercial | Deal velocity, win rates, differentiation | Close faster, instant provisioning as sales weapon | Technical architecture, OpEx |
| VP Network/Infra | Reliability, visibility, control | End-to-end visibility, hop-by-hop telemetry | Revenue impact, strategy |
| Sr. Network Engineer | Time per task, tooling, troubleshooting burden | Minutes instead of weeks, no protocols | Business strategy, revenue |

<!-- Canonical source: context/product/proof-points.md -->
## Proof Points (Anonymized for Cold Outreach)

Never use customer names in cold emails. Anonymize everything.

| Use Case | How to Reference | When |
|----------|-----------------|------|
| Speed | "One of our fiber operator customers went from 60-90 day provisioning to under 10 minutes." | Speed objections |
| Sovereignty | "A colo operator told us that with Megaport, 'you turn the customer over to Megaport.' With MaiaEdge, they control their destiny." | Colo, NaaS comparison |
| Simplicity | "One operator called it 'fabric in a box. Drop it in, add water, it works.'" | Complexity objections |
| Scale | "Deployed across 800+ cell towers and 20+ data centers for a network operator." | Enterprise-scale proof |
| Industry validation | "Even Equinix called what we're building 'revolutionary and creative.'" | Credibility, skeptics |
| Reach extension | "A fiber operator in the Pacific extends reach to the mainland without new infrastructure." | Geographic expansion |
| Multi-carrier orchestration | "We're working with an aggregator that uses MaiaEdge to unify visibility across all their upstream carrier partners." | MSPs, multi-carrier |

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
- [ ] Email 1: 70-85 words, 1-3 paragraphs with proper spacing, first name on its own line
- [ ] Email 2: under 55 words, first name line, no re-intro, no meta-references to Email 1
- [ ] Email 3: 2-3 sentences max, first name line, exactly one CTA, "show is coming up" energy
- [ ] No flattery-as-problem-statement ("X is the right play" / "X is smart" / "X is the hard part")
- [ ] No "For a [role] at [type of company]..." opener
- [ ] Sovereignty/ownership language present (speed paired with ownership) [Canonical source: context/outreach/email-writing-rules.md]
- [ ] Doesn't sound like NaaS (we don't own a fabric or sell bandwidth)
- [ ] No em dashes anywhere
- [ ] No banned phrases (see writing rules)
- [ ] No competitor names (Megaport, Equinix, Lumen  -  use "third-party fabric" instead)
- [ ] NO credibility anchors (no Acme Packet, no 128 Technology)
- [ ] Company-specific angle identified (not a segment template restatement)
- [ ] Email driven by company-specific angle, not segment framework
- [ ] Single CTA, low-friction, matches persona
- [ ] Reads like a person wrote it, not a sequence tool
- [ ] Correct sender (Tim or Ken)
- [ ] No customer names (proof points anonymized)
- [ ] Subject line is short and specific to them
- [ ] No research display (company facts invisible, problems named)
- [ ] No role-addressing language (no "at the [role] level", "from a [function] standpoint", etc.)
- [ ] Email 2 comes from different angle category than Email 1
- [ ] Email 3 has exactly one CTA (no double asks)
- [ ] **Value bridge is 1 sentence max**, embedded by contrast OR standalone-but-punchy. Multi-sentence value bridge paragraph is BANNED.
- [ ] **No brand-voice constructions** ("We help operators…" / "We work with…" / "Most operators we talk to…"). Use "I" voice instead.
- [ ] **Research Receipt present above the email body** with all four sections complete: Searches Run (≥3 literal queries paired with results, ≥5 if claiming NONE), Company-level finding, Contact-level finding, Posture with reason. "NONE" without literal queries above it is research-skipping and fails this check.
- [ ] **Posture matches signal strength.** DIRECT when there's a real public signal you can point at; ASKED when inferring. NOT randomized to a quota.
- [ ] **Posture rotates across the 3-email sequence to the same contact.** E1/E2/E3 should NOT all be the same posture; if E1 was DIRECT, E2 should be ASKED, etc.
- [ ] **Hedge cap: "I'd guess" / "I'd imagine" appear in ≤30% of E1s** in any batch of 10+ contacts.
- [ ] **Non-functional voice present in E1** when there's a meaningful thing to say (an aside, an honest acknowledgment of uncertainty, a peak-end observation). Optional but encouraged.
- [ ] **Peak-end observation (if used)** passes the "forwarded by colleague" test.
- [ ] **No acknowledgment openers** ("Cold email, so here's the short version" — banned).
- [ ] **Catalog-grounded web research actually happened** (visible in the Receipt's Searches Run section as literal queries). If "NONE" cited, the Receipt shows ≥5 literal queries that were tried, not just a NONE declaration.

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

## Warm Contact Handling

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

**Fiber Operator E1 — DIRECT posture, cataloged signal F-A1, embedded value bridge**

```
RESEARCH RECEIPT — Paul Janes @ Fatbeam

Segment: Fiber Operator   Status: VERIFIED
Catalog: context/signals/fiber-signals.md

Searches run:
1. `"BEAD subgrant awarded" Fatbeam route miles` → texas-comptroller.gov/.../bead-q1-2026, 2026-03-15
2. `Fatbeam ("definitive agreement" OR "to acquire") fiber` → no Tier A hit
3. `Fatbeam ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit

Company-level finding: F-A1 BEAD subgrant award. Texas Comptroller, 2026-03-15: $12M Eastern Texas middle-mile build. 45 days old, within Tier A window.
Contact-level finding: Paul Janes, VP Engineering since 2024-08. Owns network provisioning. Recent LinkedIn posts on automation tooling — likely feels the cross-carrier NNI gap acutely.

Signal code: F-A1
Posture: DIRECT — HIGH-confidence cataloged signal, technical buyer (VP Engineering)

---

Subject: Fatbeam Eastern Texas

Paul,

Saw the BEAD subgrant for the Eastern Texas middle-mile build. The part that usually bites operators in your spot isn't the buildout itself, it's the gap between fiber lit and first dollar of revenue, because every cross-carrier hop into the new market is still a 60-day NNI conversation. The fix is infrastructure that lets your team stand up those paths in minutes, under your brand.

Worth a conversation?
```

(72 words. Public-signal opener "Saw…" cites the cataloged F-A1 signal. Value bridge embedded by contrast in the problem paragraph. "I" voice implied by sender. No standalone "we built infrastructure that…" paragraph.)

**Network Operator E1 — ASKED posture, NONE Receipt (5+ searches required), premise hedge, omit standalone value bridge**

```
RESEARCH RECEIPT — Paul Janes @ ATN International

Segment: Network Operator   Status: VERIFIED
Catalog: context/signals/network-operator-signals.md

Searches run:
1. `ATN International ("definitive agreement" OR "to acquire")` → no Tier A hit
2. `ATN International BEAD subgrant route miles` → no Tier A hit
3. `ATN International ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale)` → no Tier A hit
4. `ATN International ("AI data center" OR "hyperscaler" OR "GPU") fiber` → no Tier A hit
5. `ATN International earnings call provisioning` → no Tier B hit

Company-level finding: NONE — no Tier A or Tier B hits across 5 searches.
Contact-level finding: Paul Janes, CTO since 2023. Came from Liberty Networks where he ran cross-Caribbean network ops. Background suggests he's lived the multi-jurisdiction provisioning problem firsthand.

Signal code: NONE
Posture: ASKED — no public signal, inferring; technical buyer but inference requires hedge

---

Subject: ATN cross-boundary paths

Paul,

Probably already on your radar, but the operators I've been watching with multi-country footprints all hit the same pinch point: the automation works fine within each market, then every time a customer needs a path that crosses a boundary, the team's back to LOAs and BGP sessions. Curious how you're sequencing that, or whether the cross-boundary piece already runs at the same pace as on-net.

Either way, the new São Paulo PoP looks well-placed for the LATAM-North flows.
```

(80 words. Premise hedge "Probably already on your radar, but…" softens the entire premise. "Operators I've been watching" is "I" voice. Illumination question carries the close — no standalone CTA. Peak-end observation about São Paulo PoP passes the "forwarded by colleague" test. No value bridge sentence at all — the question carries it.)

---

## Skill Chain

- **Best preceded by:** prospect-research (recommended) or existing HubSpot account brief
- **QA:** copy-strategist (for review of completed emails)
- **For batches:** Use sdr-pipeline instead, which includes cold-email writing + research + pipeline management
