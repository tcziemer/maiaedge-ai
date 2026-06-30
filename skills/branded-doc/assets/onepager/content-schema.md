# Outbound One-Pager  -  Content Schema & Voice Rules

How to fill an account brief so it ships at volume without a human eyeballing each one. The renderer
(`render.py`) owns the LOOK; this file owns the WORDS. Fill `content.json` from research, run `qa.py`
(it fails closed), then `render.py`. One account, one brief.

**When this goes out:** only after a LinkedIn-connection accept (rides the thank-you DM) or after a reply.
Never cold. The brief makes the case; the follow-up email carries the meeting ask.

---

## The locked structure (do not add, remove, or reorder)

| Slot (JSON) | Job | Cap |
|---|---|---|
| `account_eyebrow` | Top-right tag, ACCOUNT ONLY, no segment call-out. Use `FOR NSCALE`, never `FOR NSCALE &middot; SOVEREIGN AI CLOUD`. Keeps the top safe across segments and avoids mis-segmenting the account. No "pre-meeting / opportunity brief". | <= 4 words |
| `title_line1` + `title_accent` | Masthead headline. `Owning the` / `Path.` is the campaign title; an account-framed title (`The path between your sites.`) is also fine. Accent renders gold. | <= 4 words total |
| `masthead_sub` | One-line promise in the prospect's frame. Forward-state, no flaw claim. | <= 22 words |
| `hook.headline` + `hook.body` | The structural truth, STATED. A tension that belongs to the physics of their world, not a flaw in their company. | headline <= 8 words; body <= 60 words |
| `whynow.headline` + `whynow.body` | Why this matters now for THIS account, framed as where they're going (the ramp, new sites, the audit, the next region). Research absorbed, never recited. | headline <= 8 words; body <= 65 words |
| `stats[3]` | Three numbers from `facts.md` approved stat tokens. Nothing else. | exactly 3; label <= 12 words |
| `plays_headline` + `plays[3]` | The 3-play table is the CENTERPIECE. Each row ties a capability to THEIR business, specific and concrete (their markets, motions, buyers). The `pays` column is the heaviest hitter - see the rule below. | headline <= 8 words; each cell <= 34 words |
| `product.headline` + `product.body` | Header is a NEUTRAL safe label that works across ALL segments (`What MaiaEdge is`); do NOT lead by self-categorizing ("Carrier infrastructure ..."). Body describes what it does, plainly. | body <= 55 words |
| `pillars[3]` | DETERMINISTIC / PRIVATE / INSTANT (or the segment's pillar set). | each desc <= 16 words |
| `cta.lead` + `cta.body` | One warm, low-friction next step in the prospect's frame. | body <= 32 words |
| `footer_left` | e.g. `MAIAEDGE  ·  PREPARED FOR [ACCOUNT]` | - |

Keep total length within these caps and the brief stays on ONE page. Over the cap is the only reliable way
to spill to a second page, so the caps are the page guarantee. If an account genuinely needs a second page,
that is a deliberate "Works with what you run + diagram" module, not loosened body text.

## The angle is RESEARCH-DRIVEN - pick it from the account AND the contact (do not default)

The `pays` column is the heaviest hitter, so it has to land hard - but WHICH angle leads is chosen from
research, never defaulted. Before writing the plays, decide what THIS account cares about (their stated
motions + public priorities) and what THIS contact cares about (their role), then make the FIRST play's
`pays` carry that angle's strongest payoff. Order the other two rows behind it.

Match the lead angle to the persona (pick the fit, not the habit):

| If the account / contact cares most about... | Lead the `pays` with... |
|---|---|
| CFO / commercial / founder at a revenue-owning prospect | MARGIN: connectivity ships in the same package as compute, so owning the path captures the connectivity margin on compute they already sell. Often strong, NOT automatic. |
| CISO / compliance / a regulated or sovereign account | SOVEREIGNTY proven end to end (audit-ready), a premium tier buyers pay more for |
| VP / Director of Engineering, Platform, or Network | DETERMINISM + visibility: predictable latency, hop-by-hop proof, no routing protocols to run |
| CRO / VP Sales / BD | SPEED TO REVENUE: paths live in minutes, so a new region or customer converts sooner instead of waiting on a carrier |
| COO / operations | OPERATIONAL SIMPLICITY: one operating model across every site; a new region is a config push |

Weakest lead, avoid: "a reason customers pick you over a competitor." Differentiation is a side effect of the
real payoff, not the payoff. Pick the angle from the research and say (to yourself) why it fits this contact.

## Where the angle comes from - read the company brain before you fill a brief

The strongest angle is built from research, and the research lives in `context/` in this repo. Confirm the
segment first, then pull the account angle, the persona's pains, the why-now trigger, and the proof from these:

| To get... | Read (in `context/`) |
|---|---|
| Confirm segment + sub-segment (drives everything) | `core/segment-qualification.md`, `core/icp-playbook.md`, `account-tiering/sub-segment-qualification.md` (+ `account-tiering/icp-deep-dives/`) |
| Persona pains + value props + pillars (the angle menu, by segment AND role) | `core/messaging-framework.md` (pain + value props by persona, discovery, objections), `copy-strategy/segment-messaging.md`, `copy-strategy/segment-language.md` (their words) |
| Deep segment cheat sheet | `segments/<segment>.md` (colocation / fiber-operator / neocloud / network-operator / msp-aggregator / enterprise) |
| The WHY-NOW trigger for THIS account | `signals/<segment>-signals.md` (Tier A meeting-ready triggers), `signals/signal-framework.md`, `signals/universal-platform-signals.md` |
| Candidate plays (capabilities tied to outcomes) | `sales/use-case-taxonomy.md` |
| Proof for the stat strip + any figure | `product/proof-points.md`, `product/ai-market-positioning.md`, `product/cloud-onramp-business-case.md` (margin/egress), `product/pbc-pce-datasheet.md` |
| Competitive angle (only if it fits the persona) | `core/competitive-positioning.md`, `core/differentiation-naas-aggregator.md` |
| Full account research depth (who to address, account-specific value prop) | `sales/account-brief-template.md` |
| Voice + banned phrases + sender | `outreach/email-writing-rules.md`, `outreach/voice-gold-standard.md`, `outreach/persona-targeting-blocklist.md` |

Rule of thumb: the segment file + that segment's signals catalog + the persona row in `messaging-framework.md`
together give you the account angle, the why-now, and the persona-fit payoff. Build the hook, why-now, and the
`pays` column from the value props and triggers there, not from generic claims.

## Headers STATE the point; they never ANNOUNCE the move

This is the rule Cooper called out. The reader should feel the structure, not be told it. The bold headline
carries the meaning on its own; there are no section labels. Do NOT write a headline that narrates what the
section is doing.

| Banned (announces the move) | Required (states the thing) |
|---|---|
| "The structural truth" | "The one layer still rented" |
| "Why it matters now" / "The thesis" | "Three motions converging on one layer" |
| "Where MaiaEdge fits" / "Where we fit" | "What owning the path unlocks" |
| "The opportunity" / "Market context" | (state the actual market shift) |
| "The ask" / "Next step" / "The conversation" | (the CTA is a question/offer, not a labeled section) |

**Two exceptions to the no-label rule:** (1) the product section header may be a neutral, segment-safe label (`What MaiaEdge is`); (2) the masthead eyebrow is account-only (`FOR [ACCOUNT]`), never a segment call-out. The rhetorical sections (hook, why-now, plays) ALWAYS state the point.

## Voice rules (inherited from context/outreach/email-writing-rules.md)

- **Forward-state only.** Frame every problem as the predictable challenge of where they are GOING ("as the
  platform widens", "as you add the second site", "as the audit lands"), never as an asserted flaw in how they
  run today. BANNED: "today that means best-effort internet", "data still rides whatever path each customer
  can arrange", "you cannot see / you cannot prove", "nobody can show the path".
- **Talk to them.** Second person, active voice. "your sites", "as you widen the platform" - not third-person
  description of their company.
- **Relevance, not personalization.** Research shows up as the precision of the named problem and their
  vocabulary, never as recited facts. If the brief would still read fine with another account name swapped in,
  the hook and why-now are not sharp enough.
- **Sovereignty pairing.** Operator segments (Fiber, Colo, AI Colo, Network Op, MSP): pair speed with operator
  ownership ("your team", "under your brand", "you keep the customer"). Neoclouds and Enterprise: the prospect
  IS the customer - use DATA sovereignty ("paths you control", "provably private", "audit-ready"), never
  operator resale.
- **No naming our people, no staging our meeting.** The brief never names MaiaEdge founders, never says "a
  working session", "not a pitch", "clear view of fit", "the right room", "ahead of our conversation". That all
  lives in the follow-up email, not on the customer's PDF.
- **Verifiability (credibility).** A brief states ONLY what is verified. Every number comes from the `facts.md`
  approved fence; every claim about the account or the market is researched THIS run, never asserted from memory.
  If you cannot verify it, leave it out or state it forward-state. `qa.py` blocks ungrounded numbers and any $ / %
  in the body, but it cannot check a qualitative claim - that part is on you.
- **Punctuation.** No em dashes anywhere. Number ranges use hyphens (`60-90 days`). When you name the category at
  all, "carrier infrastructure" is the term (never IaaS / NaaS / platform); the product header itself stays a
  neutral label, not a category claim.

## Workflow

1. Copy `content.example.json` to `content.<account>.json`.
2. Research the account + contact; fill every slot within caps, following the voice rules above.
3. Pull all stat tokens and any external fact from `facts.md` (verbatim).
4. Run `python3 qa.py content.<account>.json` - fix every issue it reports. It fails closed.
5. Run `python3 render.py content.<account>.json` - produces the single-page PDF.
6. Log delivery on the contact per linkedin-outreach (one-pager sent: [file] via [channel] YYYY-MM-DD).
