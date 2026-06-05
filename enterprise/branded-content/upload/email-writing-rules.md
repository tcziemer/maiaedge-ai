# Email Writing Rules

## The Core Philosophy

Research is fuel, not decoration. The point of researching the contact, company, and segment is not to show off stats or prove you did homework. It is to show the recipient: I understand your world. I understand your company. I understand your day-to-day. I understand your goals. Then tie strategically the best value prop for that company, contact, and segment.

The email should read as if the writer has spent a decade in this person's industry. Not as a salesperson who researched a company. Not as a sequence tool that merged data into a template. As someone who understands their world, their frustrations, their vocabulary, and their goals.

## The Earned-Problem Doctrine (Name the Problem, Not the Flaw)

This is the operating logic for every message we send, in every channel. Four steps:

1. **Find what they care about.** Before choosing an angle, research the contact's public
   voice (recent posts, talks, quotes, panels, their own headline/positioning) and their
   role priorities. The problem you name must be something they are *already talking about*
   or will *predictably hit on the path they are publicly on* — never a problem you have
   assumed they have.
2. **Name that problem directly, without offending.** Say the problem plainly. Directness is
   good and gets replies. What loses the reply is implying their current operation is broken,
   slow, or amateur. The whole game is the difference between those two (see the current-state
   vs. forward-state rule below).
3. **Show the easy solution.** One concrete line on what MaiaEdge does about it, led as an
   easy hand-off ("that's the easy part to hand off," "drop-in, paths up in minutes," "no
   network team needed"), never as a rip-and-replace or a lecture.
4. **Make no bold, unverifiable claims about their business.** If you cannot point to a public
   signal for it, do not assert it as fact. See the ban below.

### The current-state vs. forward-state rule (the core of not offending)

The fastest way to get ignored by a senior operator — especially an ex-telco, ex-HPC, or
ex-infrastructure person — is to tell them how their business runs today based on something
you obviously cannot see, and imply it is bad.

- **BANNED — asserted current-state flaws you cannot verify:** "your customers reach you over
  best-effort internet," "your provisioning is slow," "every site is a one-off project,"
  "you're leaving $X on the table," "your current approach is failing," "you don't have X."
  These are guesses dressed as facts, and they read as an insult to the person who built the thing.
- **REQUIRED instead — forward-state framing, hedged:** name the problem as the predictable
  challenge of *where they are going* — the enterprise/government ramp, the new sites, the next
  40 customers, the multi-region rollout — using "as you…", "as that grows," "tends to,"
  "I'd guess." This is true to how scaling actually works (e.g. the neocloud scaling-wall logic),
  and it is non-insulting because it is about growth, not failure.

A forward-state, hedged problem the contact recognizes from their own roadmap reads as a peer
who gets it. The easy-solution line then gives them a low-friction reason to reply.

### The offense test (run on every message before it ships)

Read each claim as the recipient — someone who has spent years building this company. Does any
line imply "your current setup is bad" based on something you have not actually verified from a
public signal? If yes: reframe to forward-state + hedge, or cut it. When in doubt, pose it as a
question rather than a diagnosis.

### Before / after (real, from the ResetData neocloud batch)

| Offending (asserted current-state flaw) | Earned (forward-state, hedged, easy solution) |
|---|---|
| "…customers reach those GPUs over best-effort internet, which undercuts your promise." (we can't see how their customers connect; implies their sovereignty pitch is hollow) | "As enterprise customers come on, the path into the factory has to be as deterministic as the compute. That's the easy part to hand off: private paths, live in minutes." |
| "every new site and every enterprise customer becomes its own connectivity project" (asserts their operation is a mess) | "As that footprint grows, connecting each new site and onboarding customers onto private paths tends to become real operational drag. That's where we help: paths up in minutes, no network team needed." |
| "your onshore promise only holds if the path stays private too" (tells the CEO his core promise is at risk) | "The onshore, sustainable story sets you apart. As customers connect in, keeping their data on private paths you control is what keeps that airtight." |

This doctrine governs and is consistent with `## Diplomatic Claims (Nudge, Don't Preach)` below;
that section gives the sentence-level mechanics, this section gives the strategy.

## Research Sequence (Company, then Contact, then Tailor)

Research runs in stages. Don't collapse them. Lazy outreach starts with company research, picks a segment-default angle, and sends the same message to every contact on the list. That produces templates with the company name swapped in. The reply rate reflects it.

**Stage 1, Company research.** What is this company's specific situation right now? Acquisition, expansion, leadership change, funding round, technology migration, competitive pressure. Produces the candidate angle.

**Stage 2, Contact research.** Who is this person? Role, tenure, scope of ownership, recent public activity, career history. Produces the framing lens, the facet of the company angle this person actually owns. The CEO cares about revenue and competitive position. The CTO cares about architecture and reliability. The VP Sales cares about deal velocity. The same company angle produces different emails for different roles.

**Stage 3, Tailor.** Fuse the two. The email names ONE problem that is specific to this company AND relevant to this contact's day-to-day responsibilities. If the message could be sent to a different role at the same company without changes, Stage 2 is missing. If it could be sent to a different company in the same segment, Stage 1 is missing.

## Angle-First Principle

Before writing any email, you must have a company-specific angle: the ONE thing happening at this company right now that creates an urgent, MaiaEdge-relevant problem. This angle, not the segment messaging framework, drives the email. The segment framework provides vocabulary, proof points, and persona pain mapping to support the angle. If your email could be sent to a different company in the same segment with only the name swapped out, the angle isn't specific enough. If it could be sent to a different role at the same company, the contact-level tailoring is missing.

## Research Absorption Standard

Research exists for three purposes:

1. SELECT a company-specific angle -- the ONE urgent, MaiaEdge-relevant problem happening at this company right now
2. CONFIRM the right vocabulary for their world (what terms do they use internally?)
3. CALIBRATE the tone to their sophistication level

Research findings must be invisible in the final email. They exist only in:
- The precision of the problem named (could only come from knowing this company)
- The authenticity of the language (uses their terms, not ours)
- The relevance of the angle (addresses what this person actually cares about)

The test: forward the email to someone who's spent 15 years in this segment. Would they say "this person gets it"? Or would they say "this is a salesperson who read our website"?

### Research Display Detection (Mandatory Check)

Before finalizing any email, scan every sentence for research display. Research display is a DISQUALIFYING flaw, not a minor deduction. If found, rewrite the sentence before proceeding.

**Detection patterns (if ANY of these appear, the email fails):**
- Company facts stated as standalone observations: "[Company] has [number] [things]", "[Company] is expanding into [region]", "[Company] raised $[amount]"
- Sentences where removing the company name leaves a factual description of the company rather than a problem statement
- "Your [number] [thing]" patterns: "Your 50 data centers", "Your expansion into the Southeast"
- Opening sentences that DESCRIBE the company rather than NAME a problem
- Dollar amounts, facility counts, route miles, employee counts, or specific project names
- Geographic descriptions of the company's footprint stated as facts

**Translation table -- how to convert research display into research-as-fuel:**

| Research Finding | WRONG (displayed) | RIGHT (absorbed) |
|---|---|---|
| Company has 50,000 route miles | "With 50,000 route miles across the region..." | "Every multi-state deal that stalls on provisioning is margin walking out the door." |
| Company expanding into 3 new states | "Your expansion into Kentucky, Tennessee, and Virginia..." | "New markets look great on the investor deck. The gap is usually between 'route lit' and 'first dollar of revenue flowing.'" |
| Company raised $100M | "With $100M in new financing..." | "The buildout is funded. The question is how fast it starts paying for itself." |
| Company has 12 data centers | "Across your 12 facilities..." | "Every new facility adds interconnection complexity across the portfolio." |
| Company just acquired X | "After the recent acquisition of X..." | "Unifying two provisioning systems is the kind of thing that takes 18 months unless the architecture does the heavy lifting." |
| Company is a major APAC carrier | "Running operations across 17 countries..." | "The automation works fine within each market. The problem hits at the boundary." |
| Company added GPU hosting | "With your new GPU hosting offering..." | "When tenants need deterministic paths between GPU clusters, who controls that connectivity?" |
| Company has subsea cables | "Your 250 Tbps subsea capacity..." | "The return on subsea investment depends on how fast carriers can provision onto those cables once they're lit." |
| Company operates in Latin America | "Operating across 16 countries in Central and South America..." | "Every new market is a different carrier relationship and a different provisioning timeline." |
| Company signed carrier partnership | "Following your partnership with [carrier]..." | "Every new carrier relationship is another NNI, another provisioning queue, another 60-day wait." |

**The test:** Read the sentence aloud. If it sounds like you're telling the recipient something about their own company, it's research display. If it sounds like you're naming a problem they live with, it's research-as-fuel.

### Public-Signal Observations (Allowed When Specific)

The "I noticed" ban applies to the PHRASE, not the act. Pointing at a specific public signal you actually saw is a credibility move, not a research-display move.

**Allowed (use these openers):**
- "Saw the Q3 release notes mentioned the Tennessee build wraps in February."
- "Caught your panel at MetroConnect."
- "Your last earnings call mentioned the GPU-tenant ramp."
- "Noticed the expansion announcement said 'interconnection-led' three times."
- "Saw the appointment of [name] as VP Network Automation."
- "Saw the BEAD subgrant award post on the Texas Comptroller page."

**Still banned (research display):**
- "I noticed [Company] has 12 facilities across 6 states." (generic facts as standalone observations)
- "I came across your LinkedIn post about resilient networks." (LinkedIn surveillance)
- "I saw your great post about…" (flattery angle)
- "With your $100M Series C…" (dropped stat)

**The distinction:** A public-signal observation points at a specific PUBLIC ACT (a press release, an earnings call, a conference panel, an SEC filing, a hire announcement). The signal proves the writer looked at a specific thing and had a thought about it. Research display recites facts the recipient already knows about their own company.

**Required: ground observations against the segment signals catalog.** Before writing, the writer must search public sources for cataloged signals from `context/signals/[segment]-signals.md` (Tier A patterns first, then Tier B). When a cataloged signal applies, cite it by code (e.g., "F-A1: BEAD Subgrant Award"). When a real signal exists outside the catalog, cite it as "NON-CATALOG." When nothing exists, mark posture as ASKED and use inferred angle. The output mechanism is the **Research Receipt** - see the next section.

## Research Receipt (Hard Gate Before Writing)

Every email and every LinkedIn message must be preceded by a Research Receipt block above the body. An email or DM without a Receipt is invalid output.

**Receipt format (mandatory for every E1, every LinkedIn message):**

```
RESEARCH RECEIPT - [Contact First Last] @ [Company]

Segment: [segment / sub-segment]   Status: VERIFIED | CORRECTED from [X]
Catalog: context/signals/[segment]-signals.md

Searches run (literal query strings - not paraphrased):
1. `[exact query you ran]` → [URL + date, OR "no Tier A hit"]
2. `[exact query]` → [URL + date, OR "no Tier A hit"]
3. `[exact query]` → [URL + date, OR "no Tier A hit"]
[minimum 3 searches if claiming a cataloged signal; minimum 5 if claiming NONE]

Company-level finding: [signal description with source quote + date, OR "NONE - no Tier A or Tier B hits across [N] searches"]
Contact-level finding: [what THIS specific contact owns / their recent role activity / why they care about THIS facet of the problem. REQUIRED on every Receipt, including when company finding is NONE.]

Signal code: [F-A1 | NC-A2 | NO-B3 | NON-CATALOG | NONE]
Posture: [DIRECT | ASKED] - [one-line reason tied to the finding above]
```

**Rules for the Receipt:**
- Minimum 3 literal queries if claiming a cataloged signal; minimum 5 if claiming NONE.
- Each query gets its own result line.
- Contact-level finding is required on every Receipt, including when company finding is NONE.

If you cannot honestly fill all four sections (Searches Run, Company finding, Contact finding, Posture), you are not ready to write the email. Go back and research. Do not write the email body until the Receipt above it is complete and truthful.

**Self-check before every email:** Look at your output above the email body for THIS contact. Is there a Research Receipt with at least 3 literal queries paired with results, plus a contact-level finding? If no, STOP. Run the searches now. Then write.

### Non-Functional Voice (Required, Not Banned)

Every E1 should have at least one sentence that doesn't "do work" in the structural sense. An observation, an aside, an honest acknowledgment of uncertainty. Distinguish: flattery angles for something, observation doesn't. The non-functional sentence is what proves a human wrote this email for this specific person.

**Examples that earn their place:**
- "I might be wrong about your situation."
- "Saw the Q3 release notes mentioned the Tennessee build wraps in Feb."
- "Either way, the new Bend office looks well-placed."
- "Curious if I'm reading this right."
- "Could be the wrong moment to ask."

**The test:** Remove the sentence. Does the email still hit the same point structurally? If yes, the sentence was non-functional (good). If no, the sentence was doing structural work (also fine, but that's not what this rule protects).

The non-functional sentence is OPTIONAL but ENCOURAGED. Email 1 should have one when there's a meaningful thing to say. Don't force it. A forced non-functional sentence reads as performance.

### Peak-End Observation (Allowed in E1, Capped at 1)

E1 may close with a non-business observation tied to something specific about the recipient's company or location, separated from the CTA. This is NOT flattery and NOT angling for anything.

**Test:** Would the recipient find it odd if a colleague added the same line in a forwarded internal message? If yes, it's flattery. If no, it's an observation.

**Examples that pass:**
- "Either way, the new Bend office looks well-placed for the Cascadia ramp."
- "And the new portal screenshots in the press release look clean."
- "Either way, congrats on the Tennessee buildout finishing on schedule."

**Examples that fail (still banned):**
- "Love what you're building." (flattery)
- "Impressive growth this year." (flattery)
- "Your LinkedIn posts are great." (flattery + surveillance)

**Cap:** one per E1. Never in E2 or E3. Use only when there's a meaningful thing to say. Forced peak-end observations read as flattery even when they pass the test on paper.

## Segment Lock (Mandatory Before Writing)

Before writing any email:

1. Identify the segment.
2. Load ONLY that segment's vocabulary and value props.
3. If a term appears in another segment's vocabulary but not this one, it is BANNED from this email.

Each ICP speaks a different language with different value props. They do not mesh across segments. Using colocation terms when targeting a neocloud, or fiber language in an MSP email, breaks credibility instantly.

## Structure (Angle-Driven, Problem-First)

Every email roughly follows this arc. The company-specific angle drives the problem statement. The segment framework provides vocabulary. It is not a fill-in-the-blank template:

0. **First-name opener on its own line.** `Paul,` then a blank line, then the body. Every email in the sequence (1, 2, 3) starts this way.
1. Problem statement (1-2 sentences): Lead with the company-specific angle, framed as the problem relevant to their segment + role. This IS the hook. Use THEIR language, not ours. ("I'd guess" or "I'd imagine" if inferring.)
2. Context bridge (1 sentence): Connect their world to that problem. Research absorbed into the framing, not displayed.
3. MaiaEdge positioning (1-2 sentences): What we're doing about it. Share what you're building, not what you're selling. For operators: pair speed with ownership.
4. CTA (1 sentence): One question. Low friction.

No credibility line. No sign-off. The message does the talking, not our history. Signatures are auto-appended by the email platform.

## The Human Test (Likeable and Reply-Worthy)

Before delivering any email, ask two questions:

1. **Would a real person actually write this?** If it sounds like it came from a sequence tool, rewrite it. If every sentence is doing obvious "work" (building rapport, establishing credibility, creating urgency), it feels manufactured.
2. **Would THIS specific person want to reply?** Read the email as the recipient, in their role, on a Tuesday afternoon. If replying would feel like submitting to a pitch, rewrite. Reply-worthiness comes from peer engagement, from the sense that the sender understands their world and is worth 3 minutes of their time. The best emails have sentences that just sound like a person talking, to another person worth talking to.

## Diplomatic Claims (Nudge, Don't Preach)

The goal is a reply. Overclaims and absolutes push against that. They shift the reader from peer engagement to being pitched. Nudge them toward the conversation, don't tell them what their business needs.

**What overclaiming looks like:**
- Absolutes: "the only way," "the single biggest," "you MUST," "this is THE answer," "the future of [anything]"
- Definitive diagnostics about their business when you can't know: "your team can't do X," "you're leaving $X on the table," "your current approach is failing"
  - **Unverifiable current-state claims specifically:** never assert how their network,
    provisioning, or operations work *today* unless a public signal proves it. Reframe to the
    forward-state challenge of their growth (see The Earned-Problem Doctrine).
- Prescriptive musts: "you need to," "what you should do is," "the right approach is"
- Framing their business as broken without acknowledgment of what they've built

**What nudging looks like:**
- Hypothesis language: "I'd guess," "I'd imagine," "my read is" (used sparingly per hedge variety rule, max 30% of Email 1s in a batch)
- Premise hedges: "Not sure if you're already solving this, but…" / "Probably already on your radar, but…" / "Could be wrong about the timing, but…"
- Relational framing in "I" voice: "the pattern I'm watching with operators in your spot," "one thing I keep hearing from operators in growth mode" (NOT "most operators we talk to are seeing" - that's brand voice, banned per Rule H)
- Acknowledging what they've built before positioning a gap: "the internal automation is real, the gap hits at the boundary"
- Inviting the conversation, not demanding it: "worth a conversation?" "dealing with something similar?"

**Calibration:**
- Strong claims about THEIR business need a hedge or a relational frame
- Strong claims about OUR category (what MaiaEdge does, what the market is moving toward) can be direct, but never grandiose. "I've been working on infrastructure that lets operators own the connectivity layer" is direct (and in "I" voice). "We're revolutionizing how carriers deliver connectivity" is grandiose. Direct works, grandiose reads as hype.

**The diplomacy test:** Read every claim as if it were a peer on their team pushing back. Could they disagree? Could they say "that's not actually our problem"? If yes, soften. A claim that invites disagreement opens a conversation. A claim that shuts it down ends it.

Human voice markers (good):
- Reasoning that flows: clauses connected with so / since / but / even though, arriving at one point. One bare fragment per body, max.
- "I'd guess" or "I'd imagine" used genuinely
- Acknowledging what you don't know: "Not sure if this is on your radar"
- Active voice, second person: talking to them, not reporting about them
- One idea per email. Commit to it.

See the **Plain-Spoken / Human-Typed Voice** section below for the full profile.

Sequence tool markers (bad):
- Every sentence doing obvious "work"
- "That's why I'm reaching out..."
- Stacking three value propositions in one email
- "I'd love to..." / "I'd be happy to..." / "Let me know if..."
- Perfect parallel structure throughout

## Plain-Spoken / Human-Typed Voice

The copy must read like a person typed it, not like a sequence tool assembled it. A sequence-tool voice optimizes each sentence to "do work"; a human voice lets sentences connect and breathe, and trusts one clear point to carry. This is a voice profile, not a structure change: the Earned-Problem angle, the Receipt, the caps, the posture, and the segment lock all stay exactly as they are. Six qualities, in priority order.

### 1. Reasoning flows; facts don't stack (the biggest tell)

Connect clauses with **so / since / but / even though** so the email reads as one train of thought arriving at a point, not one-idea-per-sentence declaratives mashed together.

- ✗ (Network Operator) "The orchestration works inside each market. The boundary between markets is manual. That leaves circuits stuck in provisioning."
- ✓ (Network Operator) "The orchestration works fine inside each market, but the moment a circuit crosses the boundary it turns into a manual project, so the off-net leg is where your provisioning time actually goes."

### 2. Say the thing; don't announce the thing

Kill the structural signposts that telegraph the pitch: colon-prefixes ("What we keep doing for similar teams:"), "Here's the thing,", meta-framing openers ("What caught our eye…", "The angle that interests us most…"). State the point as a clause, not a labeled section.

- ✗ (MSP/Aggregator) "Here's what we keep seeing with aggregators: when a customer reports a slowdown, your team can't tell which carrier owns it."
- ✓ (MSP/Aggregator) "When a customer reports a slowdown, the first hour goes to figuring out which upstream carrier owns it, since once traffic leaves your network you're flying blind on the path."

### 3. Talk to them — active voice, second person

"your team provisions", not "the team provisions". "you hand that experience to someone else", not "the experience ends up owned by another provider". Passive + third person reads like a report written about them; active + direct address reads like someone speaking to them.

- ✗ (Colocation) "When a tenant needs reach beyond the campus, that experience tends to be owned by another provider, and interconnection revenue is left on the table."
- ✓ (Colocation) "When your tenant needs reach beyond the campus, you hand that experience to someone else, and the interconnection that should sit in your meet-me room walks across to a carrier."

### 4. Plain words, kept industry words

Swap consultant words for conversation words. Keep the words they actually say at work.

| Consultant word (swap) | Conversation word |
|---|---|
| productizing | sell / turn up |
| operating model | way of working |
| addressable market / TAM | the markets (or sites / buildings) you can reach |
| monetize / monetization | new revenue / get paid for |
| leverage / utilize | use |
| enablement | help / lets you |
| "solution" | the actual thing (the fabric, the path, the port) |

**Segment-native carve-out:** where `segment-language.md` already sanctions a term as insider vocab, that wins. Concrete operator usage like "monetize the fiber you already own" or "monetize idle plant" stays — the swap targets the abstract consultant usage ("monetization strategy", "monetize your assets"), not the peer phrasing operators actually use. KEEP the real insider terms per segment: DIA, NNI, off-net, hop-by-hop, route miles, lit/dark, meet-me room, cross-connect, attach rate, GPU cluster, deterministic paths, dark fiber pair. Those read peer, not corporate.

- ✗ (Neocloud) "As you scale inference across clusters, you'll need to operationalize deterministic connectivity to monetize your addressable GPU capacity."
- ✓ (Neocloud) "Once inference starts crossing clusters, the slow part is standing up deterministic paths between them, and right now that usually means waiting on a carrier to turn up the circuit." (customer-side framing — neoclouds are the customer; no operator-monetization language)

### 5. Honest, spoken uncertainty

When inferring, sound like a person being straight: "Not sure if this is already in motion," "Hard to tell from outside," "tends to," "usually." This widens the existing "I'd guess / I'd imagine" bank — keep the 30% hedge cap.

- ✗ (Enterprise, Multi-DC) "Your DR architecture relies on redundant inter-DC dark fiber. A single pair represents a single point of failure, and data residency cannot be substantiated."
- ✓ (Enterprise, Multi-DC) "Hard to tell from outside, but if the DR plan leans on a single dark fiber pair between the data centers, one cut takes both paths down, and compliance still can't prove where the data went when it reroutes." (data-sovereignty framing — never operator resale)

### 6. Rhythm: vary sentence length; one bare fragment max

A flowing connected sentence next to a short punchy one. One clipped fragment per body lands; three stacked fragments read as ad copy.

- ✗ (Fiber) "Routes go live on schedule. The Ethernet product lags. That leaves revenue on the table. Activation is the gap."
- ✓ (Fiber) "The buildout moves on schedule, but the part that lags is how fast a new route starts paying once it's lit, since the cross-carrier piece is still a 60-day conversation. Revenue sitting on lit plant."

### The throughline

Don't write to make each sentence efficient. Write so the sentences connect into one thought a peer would actually say out loud, and trust the single clearest point to carry the email. The specific-mechanic peer line (see Banned Phrases → generic-category we-claims) is the one sanctioned "we" sentence; everything else stays "I" voice or second person.

## CTAs (Rotate)

- "Open to a conversation?"
- "Worth a conversation?"
- "Would a conversation make sense?"
- "Dealing with something similar?"
- "On your radar for this year?"

ONE question per email. Never stack asks. No "I'd love to..." No "Let me know if..." No calendar links. No "quick call."

## Banned Phrases and Patterns

- Em dashes (NEVER. Use periods or commas.)
- "Hope this finds you well" / "Just wanted to reach out"
- "I noticed..." (the PHRASE; specific public-signal observations using "Saw…" / "Caught your panel…" are allowed - see "Public-Signal Observations Allowed When Specific")
- "Saw your post..." / "I came across..." (LinkedIn surveillance)
- "As a [role title]..."
- "Revolutionary" / "Game-changing"
- Customer names in cold emails (anonymize everything)
- Competitor names in cold emails ("third-party fabric providers" not Megaport/Equinix/Lumen)
- "Same team that built Acme Packet" / "128 Technology" / Andy Ory / any credibility anchors. Banned in cold email and LinkedIn for every sender. Allowed only in live presentations, demos, proposals, and objection handling.
- **"Fabric-in-a-box"** in cold email and LinkedIn body copy. The phrase is canonical in cheatsheets, the 101, sales-enablement collateral, competitive battlecards, and live conversations as a customer-quote anchor — but does NOT appear in cold-email or LinkedIn body. Use "interconnection layer," "service fabric," "build your own fabric," or the segment-specific embed-by-contrast templates instead.
- Sign-offs (Tim, Best, etc.). Signatures are auto-appended.
- "I'd love to schedule..." / "I'd be happy to..."
- Opening with company facts as standalone observations
- Flattery or congratulations
- **Flattery disguised as a problem statement.** Sentences that approve of their strategy before naming a pain. Banned examples: "Growth through acquisition is the right play," "Building Tier-4 facilities is the hard part," "Your expansion is smart." Lead with the problem itself, no validation clause.
- **Email 2 meta-references to Email 1.** "The other angle on this," "Another way to think about this," "To build on my last note," "Quick follow-up," "Circling back." Email 2 leads with a new thought, not a reference to the prior send.
- **Generic-category we-claims inside person-to-person email.** Still banned in E1, E2, and E3:
  - "We help operators…"
  - "We work with…" / "We work with companies like yours…"
  - "Many of the operators we talk to…"
  - "Most operators we talk to…"
  - "What we keep hearing from operators…"
  These are us-to-a-category sentences with no specific mechanic. The mismatch is small but detectable. Replace with "I" voice or with the peer line below.
  - "I've been seeing this with…"
  - "The pattern I'm watching at…"
  - "I've been talking to operators in your position who…"

  **Allowed exception — the specific-mechanic peer line.** A "we" attribution IS allowed when it names a SPECIFIC mechanic and a plain outcome, because that reads as spoken peer credibility, not a brand slogan:

  > We've been helping similar [cohort] [specific mechanic], so [plain outcome].

  Example (Colo): "We've been helping multi-site colos turn a cross-connect request into reach beyond the campus, so the customer stays yours instead of walking to a carrier." The test: a reader can tell exactly what we DO from the sentence. If the "we" sentence could describe any vendor ("we help operators grow"), it's the banned generic claim. If it names the mechanic + outcome, it's the allowed peer line. One per sequence, max; never in LinkedIn (no room under the char cap). For Enterprise and neocloud the mechanic is data-sovereignty / audit-ready-path framing, never operator resale.
- **Acknowledgment openers.** Banned: "Cold email, so here's the short version." / "Quick cold note since I doubt this is on your radar yet." / "We haven't met, so I'll get to it." These place the sender below the recipient and break the peer-to-peer posture. Premise hedges ("Not sure if you're already solving this, but…") accomplish the epistemic-honesty goal without subordinating the sender.
- **Meta-framing openers.** Banned: "The [Company] angle that interests us most…" / "What caught our eye…" / "Here's what stood out…" / "The thing we keep coming back to…" / "What's interesting about [Company]…" / "One pattern we keep seeing…" / "The piece that's hardest to ignore…" These announce a thought instead of stating it. The frame around the claim eats the budget the claim itself should occupy. Lead with the claim, not the framing of the claim. A peer doesn't preface; a peer asserts. If the observation is worth making, make it directly.
- **"No routing complexity" in Enterprise copy** is de-prioritized. In Enterprise outreach use "connect anywhere to anywhere with a click" instead. The phrase remains canonical and acceptable in operator-segment and neocloud copy.

### Role-Addressing Language (Banned)

These patterns make the sender sound like a consultant describing the recipient, not a peer talking to them. All are BANNED:

- "At the [role] level" -- e.g., "At the CEO level, I'd imagine..." (positions sender below recipient)
- "From a [function] standpoint/perspective" -- e.g., "From a BD standpoint," "From a network ops perspective" (consultant-speak)
- "For an operator [doing X]" -- e.g., "For an operator expanding into new markets..." (third-person case study voice)
- "For a [role] at [type of company doing X]" -- e.g., "For a CFO at a fiber operator expanding into the Southeast..." (describes them back to themselves in a third-person case-study frame)
- "At your scale" / "At the pace you're..." -- frames their situation from outside looking in

**Replacement approach:** Instead of framing the problem THROUGH their role, just state the problem directly. A peer doesn't say "at the CEO level, revenue conversion matters." A peer says "the fiber buildout is moving. The question is how fast it starts paying for itself."

| BAD (role-addressing) | GOOD (peer-to-peer) |
|---|---|
| "At the CEO level, I'd imagine the conversation is about how fast fiber investment converts to revenue." | "The fiber buildout is moving. The question is how fast new routes start generating revenue once they're lit." |
| "From a network ops standpoint, every new carrier adds provisioning complexity." | "Every new carrier interconnect is another set of LOAs, cross-connects, and manual provisioning steps. It adds up fast." |
| "For an operator expanding into new markets, I'd imagine the board conversation is about ROI timelines." | "New markets look great on the investor deck. The gap is usually between 'route lit' and 'first dollar of revenue flowing.'" |
| "At your scale across Latin America, I'd guess coordination is the bottleneck." | "The automation works fine within each market. The problem hits every time a customer needs a path that crosses a boundary." |

### Hedge Variety Requirement

"I'd guess" and "I'd imagine" are good phrases. They signal humility and hypothesis. But in batch processing, they become a template when every Email 1 follows the same pattern: "[opener] + I'd imagine [pain]." The pain hedge softens the diagnosis. Premise hedges soften the entire premise of the email. Both are tools; rotate them.

**Rule:** In any batch of 10+ contacts, "I'd guess" and "I'd imagine" may appear in no more than 30% of Email 1 opening problem statements. The remaining 70%+ must use alternative constructions:

1. **Direct assertion:** "The gap between signed deals and live revenue is where margin sits idle."
2. **Illumination question:** "How fast does a new NNI actually go live once the deal is signed?"
3. **Premise hedges:** Soften the whole premise, not just the pain claim. The writer is admitting they might have the wrong person, wrong moment, or wrong company.
   - "Not sure if you're already solving this, but…"
   - "Probably already on your radar, but…"
   - "Might not be a priority right now, but…"
   - "Could be wrong about the timing, but…"
4. **Peer observation:** "One thing I keep hearing from operators in growth mode..."
5. **Market observation:** "The operators winning right now are the ones where provisioning matches the sales pace."
6. **Role-native voice:** "New markets look great on the investor deck. The gap is usually..."
7. **Cost framing:** "Every day between 'fiber lit' and 'service live' is capital sitting idle."

**Selection rule:** Hedges are not interchangeable. Match to signal strength.
- HIGH-confidence cataloged signal (Tier A from segment signals catalog) → direct assertion. Don't hedge a strong signal.
- Inferred pain (no public signal found) → premise hedge OR pain hedge ("I'd guess").
- Variable pain (some operators have it badly, some don't) → illumination question or premise hedge.

Premise hedges are NOT acknowledgment openers. The acknowledgment opener pattern ("Cold email, so here's the short version" / "Quick cold note since I doubt this is on your radar yet") is BANNED - it places the sender below the recipient and breaks the peer-to-peer posture.

After writing a batch, count the "I'd guess/imagine" instances. If over 30%, rewrite the excess using the constructions above. Reviews should count and reject batches that violate the cap.

### Direct vs Asked Posture (Decision Criteria, Not Quota)

Posture is the second-order voice choice after segment lock and angle selection. It is NOT a batch percentage. Match the move to what you actually have on this contact, based on the signal strength and the recipient's role.

**Go DIRECT (declarative problem statement) when:**
- A specific public signal you can point at exists (cataloged Tier A, recent earnings call, hire announcement, BEAD award, M&A filing). The signal earned you the right to name the consequence.
- The recipient is a technical buyer (CTO, VP Engineering, VP Network) who values precision. Questions to deeply technical buyers can read as "I'm not sure enough about my own claim to commit to it."
- The pain is universally acknowledged in the segment (every fiber operator agrees provisioning is slow). You don't need to ask.
- The writer has earned the right via specificity earlier in the email.

**Go ASKED (illumination question) when:**
- The pain is real but NOT visible from public signals. You're inferring. Asking is more honest than asserting.
- The recipient is a senior business buyer (CEO, CFO) who deserves to be treated as a thinking peer, not a diagnosis target.
- The pain is variable across the segment (some operators have it badly, some don't, some are mid-fix). A question lets the recipient self-select.
- The writer is genuinely uncertain whether the email is timely.
- You want a substantive reply, not a yes/no.

**The principle in one sentence:**
- DIRECT when the recipient should think *"this person did the work and saw what's happening to us."*
- ASKED when the recipient should think *"this person is genuinely curious about how we're handling this."*

**Anti-rule:** Do NOT randomize across batches to hit a 50/30/20 quota. The right posture for THIS contact is the right posture even if every other contact in the batch wants the same one. Match the move to what you actually have, never to a target percentage.

### Value Bridge: 1 Sentence, Embed When Possible

The MaiaEdge value bridge is where most emails shift from peer conversation to product pitch. The standalone "We built infrastructure that…" paragraph is the single biggest structural tell in MaiaEdge cold output. Keep the value bridge, but compress it.

**Rules:**
- Value bridge is at most ONE sentence in E1. The multi-sentence value bridge paragraph is BANNED across every segment, including Network Operator.
- **Preferred placement: EMBEDDED in the problem paragraph as a contrast clause.** The contrast IS the value bridge. Example: "Routes go lit on schedule, but the cross-carrier piece is still a 60-day conversation. The fix is infrastructure that lets your team stand up those paths in minutes, under your brand."
- **Allowed placement: STANDALONE single sentence after the problem paragraph,** in "I" voice or product-as-outcome framing. Example: "I've been working on infrastructure that lets fiber operators stand up cross-carrier paths in minutes, under your brand."
- BANNED opening constructions: "MaiaEdge is..." / "We built infrastructure that..." / "We help operators..." / "We work with..." / "Many of the operators we talk to..." See "Banned Phrases" for the full list.
- Maximum 1 MaiaEdge-specific product term per email (choose ONE: "carrier infrastructure" OR "fabric" OR "provisioning in minutes", not all three).
- The value bridge names the OUTCOME (the result the recipient gets) plus enough specificity that the recipient can tell what category this is. MaiaEdge is a category creator; the outcome alone isn't enough - the category-defining word matters.
- If the value bridge sentence cannot be embedded AND a standalone version reads as marketing, omit it. Let a strong illumination question carry the close.

| BAD (multi-sentence pitch paragraph) | BETTER (1-sentence standalone, "I" voice) | BEST (embedded by contrast) |
|---|---|---|
| "MaiaEdge is carrier infrastructure that lets operators deploy their own fabric. Your meet-me rooms become a self-service exchange. Cross-connects in minutes, not weeks. Your brand, your margin, your control." | "I've been working on infrastructure that lets colo operators stand up that interconnection layer in-house, with tenants provisioning through your portal." | "Every cross-connect is still a project. The version that compounds is the one where tenants book paths from your portal in minutes, under your brand." |
| "MaiaEdge gives your team real-time visibility across every upstream carrier from a single pane. Your team sees every hop, every path, every SLA in one place." | "I've been giving aggregators a single view across every upstream carrier so when a customer calls about quality, your team pinpoints it in seconds." | "Three carriers, three tickets, three different answers. The fix is end-to-end visibility across all your upstream providers from one pane, under your brand." |

### Structural Variety (Batch Processing)

When writing 10+ emails in a batch, structural monotony is a detectable pattern. Recipients at the same event may compare notes.

**Rule:** In any batch of 10+ contacts, use at least 3 different Email 1 structures:

1. **Standard:** [Event/context opener paragraph] -> [Problem paragraph] -> [Value bridge] -> [CTA]
2. **Problem-first:** [Problem statement] -> [Context woven in] -> [Value bridge + CTA]
3. **Merged:** [Context + problem in same paragraph] -> [Value bridge + CTA]
4. **Inverted:** [Problem observation] -> [Value bridge] -> [Context mention + CTA]

The event or context mention does NOT always need its own paragraph. It can be a clause: "ITW is where those deals get signed. The question is whether provisioning can keep pace."

**Self-check:** After writing 5+ emails, re-read them in sequence. If you can predict the next paragraph's purpose from the structure alone, the template is too visible. Restructure at least 2 of the 5.

## Subject Lines

Short. Specific. Not clever.
- Good: "[Company] provisioning" / "[Company] interconnection" / "[Company] paths"
- Bad: "Unlock new revenue" / "Quick question" / "The future of connectivity"

### Subject-line variant guidance

Match the subject pattern to the campaign motion:

- **Event-anchored subjects ("Looking to meet at DCD," "connecting at ITW")** for event-driven motions.
- **Problem-anchored subjects ("[Company] cross-connect speed," "[Company] tenant interconnection," "[Company] partner activation," "[Company] dark fiber monetization")** as default for off-event lists. Pattern: 4 words, company name + problem-vocabulary from segment-language.md insider vocabulary lists.
- **A/B test variant on under-performing event campaigns:** Run problem-anchored vs event-anchored on the same list when an event-anchored campaign opens at <60%. Validate before swapping in production.

## Sovereignty Rule

For operator segments (Fiber Operator, Colocation, AI Colocation, Network Operator, MSP/Aggregator): pair speed with **operator** ownership. "Your team provisions in minutes" not just "provision in minutes." The operator keeps the customer, the margin, the control.

**Exceptions - segments where the prospect IS the customer, not an operator selling to one:**

**Neoclouds** have TWO kinds of sovereignty:
- **OPERATOR sovereignty (BANNED):** "keep your customer," "your portal, your invoice," "build your own fabric." They ARE the customer. This language makes no sense.
- **DATA sovereignty (ALLOWED):** "sovereign by design," "your data stays on paths you control," "provably private paths." This is about their data privacy and path control.

**Enterprise (Multi-DC ICP)** is the same pattern as neoclouds - the enterprise IS the customer, no commercial layer to resell to. Pair speed with **data sovereignty + audit-trail language**, NOT operator sovereignty:
- **OPERATOR sovereignty for Enterprise (BANNED):** "keep your customer," "your portal your invoice," "build your own fabric to sell," "monetize stranded fiber," "wholesale activation," "tenant," "meet-me room," "interconnection revenue," "aggregator," "TSD." Same logic as neoclouds - they're not selling connectivity to anyone.
- **DATA sovereignty + regulatory framing for Enterprise (ALLOWED):** "audit-ready paths," "policy-based path control," "paths you can prove," "your data on paths you control," "deterministic paths between data centers," "compliance can prove the path." HIPAA / PCI-DSS / SOX / GDPR / HITRUST mentions are appropriate when the buyer's persona (CISO, Compliance, regulated-vertical CIO) implies regulatory exposure.

## Language Bans

- **"Federation" as a verb** ("federate with partners," "federation creates network effects," "cross-carrier federation") is BANNED in cold-email body and LinkedIn body. Translate to segment-native terms: "extend your reach," "sell into new markets," "connect to partners instantly," "reach beyond your footprint." Federation-as-verb framing has no place in Enterprise copy either - enterprises are not federating with partners; they are the customer.
- **"Federated Private Networking" as a noun phrase (carve-out):** This is the MaiaEdge-owned category descriptor. ALLOWED in partner-facing materials — the 101, segment cheatsheets, the Golden Pitch deck, datasheets, marketing-site copy, partner-grade PDFs from the `branded-doc` skill. BANNED in cold-email body, LinkedIn body, and SDR-driven follow-ups. Customer-facing collateral can name the category; outbound prospecting copy translates it.
- **"Plant"** (for fiber infrastructure). Use "fiber infrastructure" instead.
- **VLAN / Q-in-Q / BGP / NNI** are BANNED in neocloud copy. Neoclouds are compute people, not networking people. Frame multi-tenancy as "serve multiple customers from the same infrastructure" or "each customer gets isolated, private paths."
- **For Enterprise copy:** specific operator-side terms ("tenant," "meet-me room," "interconnection revenue," "wholesale activation," "stranded fiber") are banned - they signal the wrong business model. The enterprise is consuming the network, not selling it. Network-engineering terms (BGP, MPLS, dark fiber, Type 2, hop-by-hop visibility, deterministic paths) are FINE for the technical-champion / network-architect personas; reserve product-specific names (SSR, HAsync, 100GigE specifics) for design conversations, not cold emails.

## Enterprise Provisioning-Simplicity Language

**Scope: Enterprise (Multi-DC ICP) copy only.** For operator segments (Fiber, Colo, AI Colo, Network Op, MSP) and neoclouds, "no routing complexity" remains canonical.

Enterprise buyers (CIO / CFO / VP Sales-adjacent) respond better to positive-outcome framing than to negation framing.

**In Enterprise copy:**
- **Preferred phrase:** "connect anywhere to anywhere with a click" (paraphrases like "anywhere to anywhere with a click" are also acceptable). Pairs naturally with an Intelligent Path Computation Engine / PCE reference when one fits the email.
- **De-prioritized (rewrite when possible for non-technical personas):** "no routing complexity."
- Technical-champion Enterprise personas (VP Network, Principal Engineer) can still take "no routing complexity" — writer's judgment.

**In operator-segment and neocloud copy:** "no routing complexity" stays canonical. The translation tables and segment fallback hooks in `context/outreach/fallback-messaging.md` and `context/copy-strategy/segment-messaging.md` continue to use it.

## Sequence Length & Structure (HARD CAPS)

These caps apply to every 3-email sequence regardless of segment. Segment-specific targets elsewhere in the codebase are soft references for tone calibration only. If a segment target suggests a higher word count for Email 1, this cap wins.

### Email 1
- **70-85 words.** Count before finalizing.
- **1-3 paragraphs**, with proper blank-line spacing between them.
- **First name on its own line** before the body. Example: `Paul,` then a blank line, then paragraph one.
- Research is INVISIBLE. No company facts, stats, counts, "I noticed," or "I saw" anywhere in the body.
- No flattery-as-problem-statement. Don't open by validating their strategy. BANNED examples: "Growth through acquisition is the right play," "Building Tier-4 facilities is the hard part," "Your expansion is smart." These read as flattery even when the next clause names a pain. Lead with the problem itself, not with approval of what they're doing.
- No describing the company back to itself. Extends role-addressing ban. BANNED opener construction: "For a [role] at [type of company doing X]..." (e.g., "For a CFO at a fiber operator expanding into the Southeast..."). A peer doesn't open with a third-person case study frame.

### Email 2
- **Under 55 words.** Enforce strictly.
- No re-introduction. BANNED openers: "Quick follow-up," "Following up on my last email," "Circling back," "Just wanted to bump this."
- No meta-references to Email 1. BANNED phrases: "The other angle on this," "Another way to think about this," "To build on my last note."
- Lead straight with the new thought from a different angle category than Email 1 (Revenue, Competitive, Operational, Market Timing, Cost-of-Inaction, Peer Social Proof).
- First name on its own line before the body.

### Email 3
- **2-3 sentences max.** Not "3-4." Not "a short paragraph." Two or three sentences, full stop.
- **Exactly ONE CTA.** No second ask, no "hope to cross paths" tail, no "either way" closer.
- **"Show is coming up" energy.** Timing nudge, not graceful exit. A reason the window is closing (event date, quarter end, buildout milestone) beats "no worries if not." This holds outside explicit Event Mode.
- First name on its own line before the body.

#### E3 three-option rotation

Rotate across three E3 categories. Pick the one that matches the contact and prior-sequence signal, not a fixed batch percentage.

**Option 1 - Take-away close (default; works without an event anchor)**
> [First name],
>
> Sounds like timing might be off, or the angle missed the mark. Door's open if this becomes useful.

**Option 2 - Illumination question (works when there's a real plausible "when")**
> [First name],
>
> Curious if this is on your radar this year, or wrong moment? Either is useful to know.

**Option 3 - Peer observation with timing nudge (works when there IS a real event anchor or a real timing reason)**
> [First name],
>
> Most operators who solved this in the last year said the trigger was [event - e.g., DCD-aligned: 'a tenant explicitly asked for cloud on-ramp']. If you're not there yet, no rush - door's open.

**Selection rule:**
- Has a real event happening within 2 weeks → Option 3 (event-anchored).
- No event but the contact's segment has a known annual planning cycle (Q4 budget, calendar-year RFP) → Option 2 (illumination question).
- Generic catch-up batches, off-event lists, and any E3 sent past the event week → Option 1 (take-away).

**Anti-pattern:** Do not use Option 3 generically past the event window. The event reference becomes stale and reads templated. When the event is over, drop the event reference and switch to Option 1 or 2.

### Segment Soft Floors (calibration only, NOT overrides)

The segment-specific word targets in `context/copy-strategy/segment-messaging.md` remain as tone calibration. A Network Operator email at 82 words that reads dense and technical is fine; a Fiber email at 85 that reads rushed needs a rewrite, not more padding. A tight, relevant email under the cap is always better than padding. NEVER pad with observations, flattery, or restated value props to hit any number.

## Quality Checklist

- [ ] Research ran in two stages (company AND contact), not collapsed
- [ ] Company-specific angle identified (not a segment template restatement)
- [ ] Contact-level tailoring present (could not be sent to a different role at the same company)
- [ ] Segment identified and vocabulary locked
- [ ] Research absorbed (invisible in email, visible in precision)
- [ ] Email driven by the company-specific angle, not the segment framework
- [ ] Pain matches role AND segment (not generic)
- [ ] No overclaims, absolutes, or prescriptive "must" language
- [ ] Claims about their business are hedged or relational; claims about our category are direct but not grandiose
- [ ] Would this specific person want to reply? (not just "would a person write this")
- [ ] Uses THEIR vocabulary, not ours
- [ ] No terms from other segments
- [ ] Email 1 is 70-85 words, 1-3 paragraphs with proper spacing
- [ ] Email 2 is under 55 words, no re-intro, no meta-references to Email 1
- [ ] Email 3 is 2-3 sentences max with exactly one CTA and "show is coming up" energy
- [ ] Every email opens with the recipient's first name on its own line
- [ ] No flattery-as-problem-statement (no "X is the right play" / "X is smart" / "X is the hard part")
- [ ] Sovereignty/ownership present (except neocloud)
- [ ] No em dashes
- [ ] No banned phrases or patterns
- [ ] No credibility anchors in cold email or LinkedIn (no Acme Packet, 128 Technology, Andy Ory). Those are reserved for live presentations, demos, proposals, and objection handling.
- [ ] No sign-off (signatures auto-appended)
- [ ] Single CTA, low-friction
- [ ] Subject line specific to them
- [ ] Reads like a person wrote it, not a sequence tool
- [ ] **Reasoning flows, facts don't stack** — clauses connected with so / since / but / even though, not one-idea-per-sentence declaratives. One bare fragment per body, max.
- [ ] **Active voice, second person** — talking to them ("your team provisions"), not reporting about them ("the team provisions")
- [ ] **No consultant words** (productizing, operating model, addressable/TAM, leverage, utilize, enablement, "solution") — swapped for conversation words; segment insider terms kept
- [ ] Each sequence email has a genuinely different angle
- [ ] Correct sender assigned
- [ ] No research display (company facts invisible, problems named)
- [ ] No role-addressing language (no "at the [role] level", "from a [function] standpoint", etc.)
- [ ] **Value bridge is 1 sentence max**, embedded by contrast OR standalone-but-punchy. Multi-sentence value bridge paragraph is BANNED.
- [ ] **No generic-category we-claims** ("We help operators…" / "We work with companies like yours…" / "Most operators we talk to…"). Use "I" voice. The specific-mechanic peer line ("We've been helping similar [cohort] [specific mechanic], so [plain outcome]") is the one allowed "we" sentence (email only, not LinkedIn; one per sequence).
- [ ] **Research Receipt present above the email body** with all four sections complete (literal Searches Run, Company-level finding, Contact-level finding, Posture). Minimum 3 queries if claiming a cataloged signal; minimum 5 if claiming NONE. "NONE" without literal queries above it is research-skipping and fails this check.
- [ ] **Posture matches signal strength.** DIRECT when there's a real public signal you can point at; ASKED when inferring. NOT randomized to a quota.
- [ ] **Posture rotates across the 3-email sequence to the same contact.** E1/E2/E3 should NOT all be the same posture; if E1 was DIRECT, E2 should be ASKED, etc.
- [ ] **Hedge cap: "I'd guess" / "I'd imagine" appear in ≤30% of E1s** in any batch of 10+ contacts.
- [ ] **Non-functional voice present in E1** when there's a meaningful thing to say (an aside, an honest acknowledgment of uncertainty, a peak-end observation). Optional but encouraged.
- [ ] **Peak-end observation (if used)** passes the "forwarded by colleague" test: would the recipient find it odd if a colleague added the same line in a forwarded message? If yes, it's flattery, cut it.
- [ ] **No acknowledgment openers** ("Cold email, so here's the short version" - banned, places sender below recipient).
- [ ] **No meta-framing openers** ("The [Company] angle that interests us most…" / "What caught our eye…" / "Here's what stood out…" / "What's interesting about [Company]…"). The first sentence after the name states the problem or observation directly, not a frame around it. If the line announces a thought instead of stating it, rewrite.
- [ ] **Earned-Problem check:** the named problem is something the contact is publicly
  discussing OR a predictable challenge of their stated growth — never an unverifiable claim
  about how their business runs today. Problem framed forward-state (where they're going), not
  as a failure of their current setup. One easy-solution line present.
