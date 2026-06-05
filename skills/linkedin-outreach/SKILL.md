---
name: linkedin-outreach
description: Write LinkedIn connection requests for MaiaEdge prospects. Use when asked to write a LinkedIn message, connection request, or LinkedIn outreach. Target 35-50 words, hard cap 280 characters (under LinkedIn's 300 hard limit). NO sender intro in body — recipient sees sender from LinkedIn UI. Must include company-specific detail baked into a problem statement, ideally grounded in a cataloged signal from context/signals/[segment]-signals.md. Requires prospect research and segment classification first. Same core philosophy as cold email (research as fuel, angle-first, peer tone, public-signal observations).
---

# MaiaEdge LinkedIn Connection Requests

## STOP — Read Before Each Run (Research Skip Detector)

The single biggest failure mode in this skill is writing the message body before doing the research, then back-filling a "Public Signal Cited: NONE — inferred angle" line to look compliant. That is research-skipping in disguise. At 35-50 words a generic LinkedIn DM is even more obviously templated than a generic email. Our entire strategy hinges on relevance, and relevance is impossible without paired company + contact research.

**Hard gate:** Emit a complete **Research Receipt** (format in the Receipt section below) for each contact BEFORE writing that contact's message body. The Receipt requires literal search query strings that you actually ran. "NONE" alone is not enough — NONE must be paired with the literal queries that were tried and returned no Tier A or Tier B hits.

**Self-check before writing every message:** Look at your output above the LinkedIn body for THIS contact. Do you see a Research Receipt with at least 3 literal queries paired with results, plus a contact-level finding? If no, STOP. Run the searches now. Then come back and write.

The Receipt is metadata. It does not count against the LinkedIn 280-character cap — it sits above the message body and is consumed by the human reviewing the output, not the LinkedIn UI.

## Length Target: 35-50 Words / Max 280 Characters

Target 35-50 words / max 280 chars (under LinkedIn's 300 hard limit). Long DMs are themselves a sequence-tool tell. Real humans send shorter DMs.

The sender intro is removed from the body (recipient sees sender from LinkedIn UI), which frees ~17 chars of budget for substance, not for length.

## Reference Files

- **email-writing-rules.md**  -  Core outreach philosophy (angle-first, research as fuel, segment lock, public-signal observations, banned brand-voice constructions). LinkedIn follows the same philosophy, adapted to the LinkedIn length target.
- **segment-language.md**  -  **Read this before writing.** Insider vocabulary, daily reality, conversational patterns, and insider vs outsider examples per segment. This is how you sound like you've been in their world, not like you researched them.
- **messaging-framework.md**  -  Segment-specific messaging rules and positioning
- **sender-profiles.md**  -  Sender identities, territories, voice characteristics (sender intro is NOT in the LinkedIn body — recipient sees sender from LinkedIn UI)
- **outbound-playbook.md**  -  Multi-touch sequence cadence (LinkedIn is typically Day 2)
- **Segment cheatsheets** (colocation.md, fiber-operator.md, neocloud.md, network-operator.md, msp-aggregator.md)  -  Deep context for pain points, discovery questions, and competitive landscape per segment
- **signal-framework.md**  -  Universal signal types, scoring, noise list. Required for the Public Signal Cited rule.
- **[segment]-signals.md**  -  Per-segment cataloged signals. The `Pattern:` field for each cataloged Tier A signal becomes the actual web search query when grounding a LinkedIn message. Required reading for the segment being targeted.

## The Philosophy (Same as Email)

Research is fuel, not content. The short message should read like a peer who understands their world, not a salesperson who found them on LinkedIn. The recipient should think "that's my life" not "this person looked me up." A specific public-signal observation ("saw the BEAD subgrant for Eastern Texas") proves the writer actually looked at something concrete, not just inferred from segment patterns.

The difference from email: you have room for exactly one problem statement and a soft ask. No context bridge, no value connection, no structure. Just the sharpest possible version of "I understand your problem."

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

The sender is the person who will appear as the connection-request initiator in LinkedIn's UI. Use the same territory-based sender logic as email. See **sender-profiles.md** for the full mapping.

| Prospect HQ | Sender (LinkedIn account that initiates the request) |
|---|---|
| Tim Lieto's 30 East states | Tim Lieto |
| Ken Cunningham's 20 West states + DC | Ken Cunningham |
| Outside US | Tim Lieto (Timothy Ziemer for strategic) |
| Unknown | Tim Lieto (default) |

Founder senders (Abilash, Timothy Ziemer) can be used for LinkedIn when the email sequence uses a founder sender. Match the sender across channels.

**Sender identification happens via LinkedIn's UI, NOT in the message body.** The recipient sees who sent the connection request automatically. Adding "Tim from MaiaEdge." to the body is redundant and triggers the sales-pitch reflex before they read the actual message.

## Format

```
[Recipient first name], [observation/question with company-specific signal]. [Optional: one sentence of context]. [CTA or no CTA].
```

**No sender intro in the body.** Sender identification happens via LinkedIn's UI when the connection request lands. `"[Sender first name] from MaiaEdge."` in the message body is BANNED.

**Length target:** 35-50 words. Hard cap: 280 characters (under LinkedIn's 300 hard limit).

**Public-signal observation preferred opener:** When you have a cataloged signal from `context/signals/[segment]-signals.md`, lead with "saw the [signal type]" / "caught your panel at…" — same Public Signal Cited rule as cold email applies. The signal observation grounds the message in something specific the writer actually looked at.

**No CTA when a strong illumination question carries the close.** "Worth connecting?" is optional. If the message ends with a real question, the question IS the ask. The recipient can connect and answer or just connect.

## Research Receipt (Hard Gate Before Each Message)

Every LinkedIn message this skill produces must be preceded by a **Research Receipt** block ABOVE the message body. The Receipt is a hard gate. A message without a Receipt is invalid output — restart that contact from research.

The Receipt replaces the older "Public Signal Cited" block. The old block let the writer drop in "Public Signal Cited: NONE — inferred angle" without proving any search effort, which is research-skipping in compliant clothing. The Receipt fixes that by requiring the literal search query strings that were run, paired with their results.

### Lookup sequence (mandatory pre-write)

1. **Web search grounded against the segment's signals catalog** (`context/signals/[segment]-signals.md`). Use the `Pattern:` field for each Tier A signal as the literal query. Run a minimum of 3 Tier A pattern searches. Stop if a HIGH-confidence Tier A hit lands. If no Tier A hits, expand to Tier B.
2. **Contact-level search:** `[Contact Name] [Company] LinkedIn` — pull role, tenure, recent activity, what they own. The contact search is NOT optional, even when the company-level search finds a signal. The whole point of the Company + Contact angle table above is that the same company gets a different message for CTO vs CEO; that is impossible without contact-level research.
3. **If web search and HubSpot both find nothing across at least 5 query attempts**, mark Signal code = NONE, posture = ASKED, and document the literal queries you ran in the Receipt.

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

[recipient first name],

[message body, 35-50 words, under 280 characters]
```

### Why each section enforces what it does

- **Literal queries** make faking research more expensive than running it. Writing 3 to 5 specific query strings is roughly the same effort as actually running them — but only running them produces real findings.
- **NONE costs more than success** (5 queries vs 3). This inverts the old incentive where the path of least resistance was to declare NONE and skip the work.
- **Contact-level finding is its own required line.** At 35-50 words you have room for ONE company+contact-fused angle. Without contact research, every message at the same company is the same message. The separate line forces the contact research to actually happen.
- **Each query gets its own result line.** Listing queries without per-query results fails the format and is detectable on review.

### Refuse-to-write rule

If you cannot honestly fill all four sections (Searches Run with at least 3 literal queries paired with results, Company-level finding, Contact-level finding, Posture with reason), output `RESEARCH INCOMPLETE: [specific reason]` in place of the message body and move on. Do NOT fabricate a Receipt to look compliant.

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

- **Peer to peer.** This is one professional connecting with another. Not a pitch.
- **Direct, not polished.** Short. Clear. The way you'd actually message someone you respect.
- **Problem-first.** Lead with what's broken in their world, not what MaiaEdge does.
- **No flattery.** No "impressive growth" or "love what you're building." Lead with the problem.
- **Genuine curiosity.** "Worth connecting?" signals you want to learn, not sell.
- **Nudge, don't preach.** At 35-50 words you don't have room to overclaim. No absolutes ("the only way"), no prescriptive musts ("you need to"), no definitive diagnostics about their business. Hypothesis language ("I'd guess") or premise hedges ("Probably already on your radar, but…") beat declaring what their problem is. NOTE: brand-voice constructions ("most operators we talk to," "we keep hearing from operators") are BANNED in LinkedIn DMs as well as emails — use "I" voice ("the pattern I'm watching at"). See email-writing-rules.md "Diplomatic Claims" and "Banned Phrases."
- **Reply-worthy.** The goal is connection acceptance and a reply, not a pitch landed. If the message would feel like being told what to do, rewrite.

## Writing Rules

**Do:**
- One company-specific detail, baked into the problem
- Peer tone  -  like messaging someone you met at a conference
- End with "Worth connecting?" or similar low-friction ask
- Use their vocabulary, not ours
- **Sovereignty pairing:** Always pair speed with ownership. "Your team provisions in minutes" not just "provision in minutes." Exception: neoclouds (they ARE the customer, so data sovereignty language only  -  "sovereign by design," "paths you control"). [Canonical source: context/outreach/email-writing-rules.md]

**Never:**
- Em dashes (replace with commas or periods)
- "I noticed" / "I saw" / "I came across" / "Following your work"
- "Impressive" or any flattery language
- Credibility anchors (no Acme Packet, no 128 Technology, no "$2.55B exits")
- Competitor names (say "third-party fabric" not "Megaport")
- "I'd love to" / "I'd be happy to" / "Let me know if"
- Pitching MaiaEdge features. The goal is connection acceptance, not a sale.
- Customer names (anonymize any proof points)

## Sequence Integration

When used as part of a multi-touch sequence (see **outbound-playbook.md**), LinkedIn is typically sent on **Day 2** after Email 1.

**Critical rule:** The LinkedIn message should NOT repeat Email 1's angle word-for-word. It should reference the same underlying problem from a different entry point. If Email 1 led with provisioning speed, LinkedIn might lead with the competitive threat that creates. Same problem, different lens.

If the prospect already received Email 1 and sees a LinkedIn request with identical language, it feels automated. The messages should feel like they came from the same person thinking about the same problem, not the same template executed across channels.

## Research as Fuel (Same Standard as Email)

The same principle from email-writing-rules.md applies here: research is fuel, not content. The research should be invisible in the message. It exists only in:
- **The precision of the problem named**  -  could only come from knowing this company
- **The authenticity of the language**  -  uses their terms, not ours
- **The relevance of the angle**  -  addresses what this person actually deals with

**What this means at 35-50 words:** You don't recite their stats back to them ("40K route miles," "12 states," "30kW racks"). Instead, the research tells you WHICH problem to lead with. If you found a cataloged signal (BEAD subgrant, M&A announcement, exec hire), you can cite the signal directly with "saw the [signal]" — that's a public-signal observation, not research display. If you only have inferred patterns, you lead with the problem and skip the source citation.

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

**Note on examples:** The first example below shows the FULL Research Receipt above the message body — that is the required output format. The remaining examples abbreviate the Receipt to a single Signal code line for brevity in this reference doc. In real output, EVERY message must be preceded by a full Receipt (Searches Run, Company-level finding, Contact-level finding, Posture).

**Fiber Operator expanding into new states (cataloged signal F-A1: BEAD subgrant award):**

To the VP Engineering (full Receipt format shown):
> RESEARCH RECEIPT — Paul Janes @ Fatbeam
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
> Posture: ASKED — illumination question fits a connection request even with a HIGH-confidence signal
>
> ---
>
> Paul, saw the Eastern Texas BEAD subgrant. The cross-carrier piece into the new market is usually where the 60-day NNI clock starts. Curious how you're sequencing it.

(34 words, 207 chars. ASKED posture, illumination question carries the close, no CTA.)

To the CEO:
> Public Signal Cited: F-A1 — BEAD Subgrant Award (Texas Comptroller, 2026-03-15)
>
> Paul, saw the Eastern Texas BEAD subgrant. The revenue clock starts when the cross-carrier piece is done, not when the fiber's lit. The fix is paths that activate at your sales team's pace.

(43 words, 247 chars. DIRECT posture, embedded value bridge, no CTA.)

**Colocation Operator losing tenants to third-party fabrics (no cataloged signal — inferred):**

To the CTO:
> Public Signal Cited: NONE — using inferred segment angle
>
> Paul, probably already on your radar, but every cross-connect routed through a third-party fabric is a tenant relationship that starts moving next door. Curious what your in-house alternative looks like.

(39 words, 240 chars. ASKED posture, premise hedge "probably already on your radar", illumination question close.)

To the VP Sales:
> Public Signal Cited: NONE — using inferred segment angle
>
> Paul, when a prospect asks for instant connectivity and the answer is "call a third-party fabric," the deal moves with the fabric. Worth a conversation about owning that path?

(35 words, 209 chars. DIRECT posture, no brand-voice "we help" construction, light CTA.)

**Neocloud with multi-facility GPU deployment (cataloged signal NC-A2: facility expansion):**

To the VP Infrastructure:
> Public Signal Cited: NC-A2 — New Facility Launch
> Source: Press release, 2026-02-10: Lambda Labs adding 3 facilities in Q2
>
> Paul, saw the three new facilities going live in Q2. When inference slows across them, the diagnosis usually depends on whether it's the carrier, the colo, or the middle-mile. Curious how your team is set up for that.

(51 words, 290 chars. DIRECT opener (cataloged signal), illumination question close, no CTA. Slightly over the 280-char preference but under the 300 hard cap because the public signal observation justified the length.)

To the CFO:
> Public Signal Cited: NC-A2 — New Facility Launch
> Source: Press release, 2026-02-10: Lambda Labs adding 3 facilities in Q2
>
> Paul, saw the three new facilities going live in Q2. Public-internet egress between GPU clusters at that scale runs 9c/GB. Private paths run 2c/GB and the difference compounds with every customer.

(43 words, 254 chars. DIRECT, embedded value bridge by contrast, no CTA.)

**MSP aggregating across multiple carriers (no cataloged signal):**

To the VP Engineering:
> Public Signal Cited: NONE — using inferred segment angle
>
> Paul, when a customer reports a path issue and three upstream carriers each say "not us," the visibility gap is the actual problem. Curious how your team handles that today.

(34 words, 196 chars. ASKED posture, illumination question, no brand-voice "we give you" construction, no CTA.)

To the CEO:
> Public Signal Cited: NONE — using inferred segment angle
>
> Paul, the Tier 1 carriers going direct to MSP customers compete on speed, not relationship. The asset-light advantage holds only if the visibility and provisioning match. Worth a conversation?

(33 words, 218 chars. DIRECT posture, embedded value bridge by contrast, light CTA.)

**After these examples, always adapt with actual research.** Research on the company tells you the situation. Research on the contact tells you which facet to lead with. These examples show the principle. Your findings provide the substance.

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
- "I" voice, not "we" voice. No "we help operators" / "we fix that" / "that's what we solve" — these are brand-voice constructions banned across all MaiaEdge cold outreach.
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
2. **Research display sweep:** Scan all messages for company facts stated as observations. At 35-50 words, displayed research is even more damaging than in email — every word is precious.
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

- [ ] Target 35-50 words, max 280 characters (count before delivering, under LinkedIn's 300 hard limit)
- [ ] Segment verified against research (if mismatch, corrected and flagged)
- [ ] If segment corrected, message uses corrected segment's vocabulary
- [ ] **NO sender intro in body** (no "Tim from MaiaEdge." / "Ken from MaiaEdge." — recipient sees sender from LinkedIn UI)
- [ ] **Opens with recipient's first name** followed by a comma, then directly into the observation/question
- [ ] **Research Receipt present above the message body** with all four sections complete: Searches Run (≥3 literal queries paired with results, ≥5 if claiming NONE), Company-level finding, Contact-level finding, Posture with reason. "NONE" without literal queries above it is research-skipping and fails this check.
- [ ] **Public-signal observation opener preferred** when a cataloged signal exists ("saw the Tennessee build wraps in Feb")
- [ ] Angle is company-specific (could not be sent to another company in the same segment)
- [ ] Angle is contact-specific (could not be sent to a different role at the same company)
- [ ] Problem-first (not feature-first, not flattery-first)
- [ ] Research absorbed, not displayed (no reciting stats or facts back to them)
- [ ] **"I" voice, not "we" voice.** No brand-voice constructions ("We help operators…" / "We work with…" / "We give you…" — all BANNED in LinkedIn DMs).
- [ ] Correct sender for the territory (sender = LinkedIn account that initiates the request)
- [ ] CTA is OPTIONAL when a strong illumination question carries the close. If included, low-friction ("Worth connecting?" or equivalent).
- [ ] **Posture differs from E1** (per the per-sequence rotation rule). If E1 was DIRECT, LinkedIn can be ASKED, and vice versa.
- [ ] No em dashes anywhere
- [ ] No banned phrases (see writing rules)
- [ ] No competitor names, customer names, or credibility anchors
- [ ] Doesn't repeat Email 1 language if part of a sequence
- [ ] Reads like a peer reaching out, not a sales tool executing
- [ ] Sovereignty language present (except neocloud)
