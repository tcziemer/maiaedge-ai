---
name: warm-follow-up
description: Write the next message in an active outreach thread - after a LinkedIn accept, a DM reply, or an email reply. Use when asked to follow up with someone who replied, accepted a connection request, needs a thank-you message, or needs the message that hooks the meeting after initial engagement. Input is the thread itself (paste what was sent and what they said). Works for both email and LinkedIn. Companion to cold-email and linkedin-outreach - those write into silence; this skill takes over the moment the prospect responds.
---

# MaiaEdge Warm Follow-Up Writer

## Purpose

The cold skills (cold-email, linkedin-outreach) write touches into silence. This skill owns every message AFTER the prospect does anything: accepts a connection, replies to a DM, replies to an email, asks a question, raises an objection, defers, or redirects. One shared move map, both channels - only the formatting differs.

The goal is the held meeting. House data: 44% of positive replies convert to held meetings, which means more than half of positives die at exactly this moment. The reply earned the next message; this skill makes sure the next message earns the meeting.

**The standard:** the follow-up must read like the same person kept thinking, not like a sequence advanced a step. Natural, non-redundant, and calibrated to what they actually said.

## What to Share

Paste the thread - what was sent and what they said (or "bare accept" if they connected with no message). Channel is usually obvious from context; flag it if not.

Coach: sender, funnel stage, and contact state are inferred from the thread + HubSpot scan - the more you paste, the tighter the message.

## Reference Files

When deployed in a project with reference files, also read:

### Always open
- **context/outreach/voice-gold-standard.md** - **Hold open WHILE writing.** §E is the warm bar: three Cooper-validated post-accept thank-you DMs. Imitate the moves, never the words.
- **context/core/differentiation-naas-aggregator.md** - The objection bank. QUESTION and OBJECTION replies about fabrics, aggregators, NaaS, or "we already have partners" are answered from its written (cold-safe) register. Its claims-to-avoid list is this skill's do-not-improvise list.
- **context/copy-strategy/segment-language.md** - The prospect replied in their vocabulary; answer in it.
- **context/copy-strategy/segment-messaging.md** - Per-segment angle-selection and vocabulary; governs QUESTION and OBJECTION answer framing.
- **context/outreach/email-writing-rules.md** - The banned-phrase list and craft-voice register hold in warm. What relaxes is listed below, not there.
- **context/copy-strategy/outbound-playbook.md** - Reply benchmarks, the propose-three-times rule, cadence context.
- **context/outreach/sender-profiles.md** - Sender identity and voice. The follow-up comes from whoever sent the cold touch.
- **context/outreach/pre-cadence-hygiene.md** - AUTO class (OOO / autoresponder) delegates here; also governs resume-after-return-date logic.
- **skills/branded-doc/SKILL.md** - § Outbound One-Pager Variant: the asset that rides the thank-you DM. This skill writes the message; branded-doc builds the PDF.

### HIGH - open when the reply touches product, segment, or deal context
- **context/product/proof-points.md** - The only sourced fact-anchor for QUESTION-class answers; use for specific performance or scale claims.
- **context/product/pbc-pce-datasheet.md** - Authoritative product-mechanics source for questions about PBC/PCE provisioning, programmable cross-connects, or federation mechanics.
- **context/hubspot/contact-schema.md** - Exact field names for Logging writes (notes, tasks, linked_in_message, owner assignment).
- **context/core/icp-playbook.md** - Per-segment objection handling and buyer pain maps; the primary source for OBJECTION-class substance.

### MEDIUM - open when specifically relevant
- **context/hubspot/property-schema.md** - signal_heat enum and target-account freeze rule; relevant when Activity Scan surfaces heat/tier context.
- **context/hubspot/call-schema.md** - Call engagement fields; relevant when the Activity Scan surfaces a prior call to reference.
- **context/hubspot/deals-schema.md** - Open deal stage and fields; relevant when the Activity Scan surfaces an open deal.
- **context/core/competitive-positioning.md** - Competitive framing for OBJECTION replies naming a specific competitor.
- **context/product/ai-market-positioning.md** - AI/NeoCloud angle for replies from GPU-cluster or AI-infrastructure buyers.
- **context/product/cloud-onramp-business-case.md** - Cloud on-ramp economics for replies from enterprise or NeoCloud buyers asking about cloud connectivity.
- **context/core/maiaedge-101.md** - Foundational positioning for any reply that asks "what does MaiaEdge actually do."
- **context/core/terminology-glossary.md** - Precise definitions when the prospect uses a term that warrants an exact answer.

## Input: The Thread

The user pastes the thread in any format - Smartlead export, forwarded email, LinkedIn conversation copy-paste, or "I sent X, they said Y." Plus the channel (email or LinkedIn) if not obvious.

**No Research Receipt.** The research happened at cold time. What replaces it is the Activity Scan + Thread Receipt below. If the thread shows the angle that was used, trust the thread over re-deriving it.

## Activity Scan (Required Before Writing)

Before writing, check HubSpot and all available resources for activity on this contact and account that the follow-up can leverage:

1. **HubSpot contact:** engagements (emails, meetings, calls, tasks), notes (including `linked_in_message` and logged accept/reply/one-pager notes), owner.
2. **HubSpot company:** open deals and stage, recent calls with ANYONE at the account, other contacts currently in motion, `recent_news_or_trigger_event` + `last_signal_date` + `signal_heat`, `account_brief`.
3. **Smartlead** (email channel, contact in a campaign): pull the full message history so the thread is complete - replies sometimes quote only part of it.
4. **Web search** - OPTIONAL, only when the reply itself turns on something news-dependent ("saw you raised" / "after our acquisition closes"). Never a mandatory gate; this skill turns replies around fast.

**Rules for using what you find:**
- **Leverage at most ONE found item**, woven naturally: a held call with a colleague ("sounds like you and Priya covered the multi-site piece last week"), an open deal elsewhere at the account, a fresh signal. More than one reads as surveillance.
- **Thin activity → don't force warmth.** If the scan finds nothing usable, the thread alone is enough. Never fabricate familiarity.
- **MCP unavailable → proceed from the thread alone** and note it in the Thread Receipt. Never block a reply on tooling.

## Thread Receipt (Hard Gate Before Each Message)

Emit above every message. A follow-up without a Thread Receipt is invalid output.

```
THREAD RECEIPT - [Contact First Last] @ [Company]

Channel: [email | LinkedIn]   Sender: [Tim Lieto | Ken Cunningham | founder]
What we sent: [angle / vocabulary / close / signal cited - across BOTH channels if both were touched]
What they did: [verbatim reply, OR "BARE ACCEPT - no words"]
Reply class: [ACCEPT | INTEREST | QUESTION | OBJECTION | DEFERRAL | REDIRECT | SOFT NO | WENT QUIET | AUTO]
Activity scan: [what HubSpot/Smartlead showed + the ONE item leveraged, OR "none usable", OR "MCP unavailable - thread only"]
Contact state: [new-in-seat / senior-technical / commercial / timing constraints they named]
This message adds: [the ONE new thing]
Must not repeat: [angle sentence / close / cited signal / distinctive phrases from the thread]

---

[message]
```

## Reply Classification → Move Map

Classify what they did, then run the move. Every class works on both channels.

| Class | What it looks like | The move |
|---|---|---|
| **ACCEPT** | LinkedIn accept, no words | Thank-you DM + one-pager play (next section). Pressure-off; the meeting ask rides the next email. |
| **INTEREST** | "Sounds interesting" / "open to a call" / "tell me more" with buying energy | Zero new pitch. One-line re-anchor, then three specific times. ≤60 words. Speed beats depth here. |
| **QUESTION** | A substantive question ("how is this different from X?" / "does this ride our existing NNIs?") | Answer-then-advance: 2-4 sentences of direct answer from the doctrine/segment files, then the call pivot ("easier to show than describe - I can walk you through it live"). See the two sub-rules below. |
| **OBJECTION** | "We already have partners for off-net" / "we use a fabric for that" | The doctrine's written register: concede what's true, then the one mechanical distinction, then a soft ask. Never defensive, never a feature dump. |
| **DEFERRAL** | "Circle back in Q3" / "after the buildout wraps" | Accept gracefully, anchor THEIR named window ("makes sense - mid-Q3 it is"), ask permission for the specific re-touch, log the HubSpot task. No sneaky extra pitch. |
| **REDIRECT** | "Not my area - talk to our VP Network" | Thank them, ask for the warm intro ("would a two-line intro from you land better than me reaching out cold?"). Never burn the referrer. Log the new contact. |
| **SOFT NO** | "Not for us right now" / polite decline | Door-open close, no rebuttal, one sentence. Suppress in cadence. A graceful exit is the last impression. |
| **WENT QUIET** | They engaged, then silence ≥4-5 business days (e.g. agreed to a call, never picked a time) | ONE short nudge, ≤40 words: simplify the logistics ("if scheduling's the friction, here's the simplest version") or add one micro-fact, never re-pitch. Second silence → close the loop with a door-open line and stop. |
| **AUTO** | OOO, autoresponder, address change | Not a reply. Apply pre-cadence-hygiene rules; resume after the return date. Never respond to a robot warmly. |

### QUESTION sub-rule: pricing

**Pricing never goes in writing. No numbers, no ranges, no "about X per month," no cost comparisons.** A pricing question is a strong buying signal - treat it as INTEREST stacked on QUESTION and convert it into the meeting: the shape of the answer is "it depends on the deployment shape, and it's a 15-minute conversation rather than a number in an email - here are three times." The pricing conversation IS the hook; writing a number kills it.

### QUESTION sub-rule: federation mechanics (do-not-improvise)

These topics have no sanctioned written answer. If the reply asks how partners get paid / settlement, who provisions across a partner's network, contractual SLA recourse on a partner leg, quoting destinations where no partner exists yet, platform fees, PCE multi-tenancy across competing operators, Sonata conformance depth, partner-side telemetry or consent revocation, fabric account ownership, or cross-connect ownership between partner sites - **do not improvise an answer.**

What you MAY say in writing (verified): connections are consent-based (the selling operator approves every one), partner network topology stays hidden from both sides, and the operator sees hop-by-hop telemetry across the full path.

For the rest, the honest answer is the escalation give: "That one I want to get you the exact answer on rather than the rough one. Easiest is 20 minutes with the person who designed it." A precise question earned a precise answer from the source - that is a reason to meet, not a gap to paper over.

## The Thank-You DM (ACCEPT class - house-validated pattern)

Calibration set: **voice-gold-standard.md §E** (three Cooper-validated DMs). The anatomy:

1. **Open: "thanks for connecting."** Sanctioned verbatim - it's what a person says. Name placement flexible ("Matt, thanks for connecting." / "thanks for connecting Dagi.").
2. **One-pager framed as thinking, not collateral.** "Put together a short one-pager on the thing I raised" / "put some thinking together on what that could look like for [Company]" / "dropping a quick one-pager on how we think about [their side] of this." Never "please find attached our overview."
3. **Continuity, compressed.** Restate the connect-request angle in NEW words - one clause, sharper than the original. Never paste the original sentence back.
4. **Close calibrated to contact state** - three registers:
   - **Escalation give** (senior or deep-technical seat, architecture-grade angle): a named next step with a real reason - "if it's relevant I'd like to set a call with my co-founder who designed it to get deeper into the architecture." Sender-aware: founders say "my co-founder"; Tim/Ken say "the founder who designed it."
   - **No-rush** (new-in-seat, mid-crunch, just-acquired): defer explicitly - "understand you'll likely be taking some time to settle in so no rush." Reading their situation IS the message.
   - **Neutral-soft default:** "happy to talk it through whenever the timing works." / "open to walking through where it fits, whenever the timing's right."
5. **Timing:** 24-48h after the accept. **Then the meeting ask rides the next EMAIL** (1-3 days after one-pager delivery): it names ONE claim from the one-pager in new words and carries the ask. Retro-validated: held meetings book over email; LinkedIn supplies the warmth.

Register note: lowercase-casual (the Dagi pattern) is sanctioned when the cold touch ran lowercase or the prospect writes that way. Match the thread.

## Non-Redundancy Gate (Hard)

The follow-up may NOT reuse, from any prior message in the thread (either channel):
- the angle sentence
- the close
- the cited signal
- any distinctive phrase

And it MUST add exactly ONE new thing: an answer, a new facet of the problem, the one-pager, a leveraged activity item, or an honest reason. Not two. Adding nothing is a bump ("just floating this up") and bumps are banned; adding two reads as a pitch restart.

**The test:** read the whole thread top to bottom with the new message at the end. Does it read like a person kept thinking about this prospect, or like a sequence advanced? A deeper explanation is new substance in fewer words - never the same pitch with more words.

## Register: What Relaxes, What Holds

**Relaxes in warm (vs the cold rules):**
- **Hedging drops.** They engaged; "I'd guess" reads weak now. Answer directly.
- **Length flexes for QUESTION class:** up to ~120 words (email) / ~80 words (DM). Everything else stays short - INTEREST ≤60 words, WENT QUIET ≤40.
- **The 280-character cap does NOT apply** - that's the connection-note limit. Post-accept DMs run to the 40-80 word default.
- **"Thanks for connecting"** is a sanctioned open (LinkedIn).
- **First-person product description is allowed in answer sentences** - still craft voice, still ONE concrete mechanic, never a feature list.

**Holds absolutely (no warm exception):**
- **NO credibility anchors in writing. Ever.** No Acme Packet, no 128 Technology, no exits. Anchors are for live spoken calls only (Cooper, 2026-06-12).
- **NO pricing in writing. Ever.** (Cooper, 2026-06-12. See the pricing sub-rule.)
- No em dashes, no colons, no dashes-as-punctuation (hyphenated compounds fine), and no move-announcing transitions ("another angle on this," "one more thought"). Just say the thing.
- ONE ask per message.
- Customer names stay anonymized ("one fiber operator," never the name).
- No "I'd love to" / "I'd be happy to" vendor language. ("Happy to set up time" / "happy to talk it through" remain sanctioned patterns.)
- No fabricated familiarity, no fake "great chatting" if no chat happened.
- Craft voice: reasoning connected with so/since/but, no stacked fragments, no announce-then-say.

**Competitor names:** still never introduced by us. ONE exception: when the prospect named the competitor first and the answer requires it ("how is this not Megaport?"), the answer may use their word once, then reverts to "the fabric" / "a third-party fabric." Refusing to say the word they used reads evasive.

## Channel Mechanics

Every reply class works on both channels; only formatting differs.

**Email:**
- Reply in-thread, same subject (`Re:`). Never a new subject on a reply.
- No re-greeting beyond the first name. Mirror their formality and length - a two-line reply gets a tight answer, not an essay.
- Signatures auto-append. Never write one.

**LinkedIn:**
- Post-accept DM default 40-80 words.
- One-pager attaches in the DM per branded-doc § Outbound One-Pager Variant.
- The post-accept flow hands the meeting ask to email (above); a verbal DM reply, though, gets worked in the DM - stay in the channel they chose.

**Cross-channel rule:** LinkedIn + email to the same contact is ONE conversation. The non-redundancy gate spans both channels. Reply on the channel they last engaged on unless the user directs otherwise.

## Meeting Mechanics

- **On any positive: propose three specific times.** Never a bare calendar link (validated house rule). Spread across 2-3 business days in the prospect's timezone; flag for the sender to adjust to their real calendar before sending.
- **Size the ask to what the reply earned.** INTEREST earned the direct scheduling ask. QUESTION earned an answer plus a soft offer. OBJECTION earned a soft ask only. ACCEPT earned a pressure-off DM with the ask deferred to email. Never grow the ask past what they gave you.
- The demo give ("I can show you the whole thing end to end") stays available for technical buyers and converts QUESTION replies especially well - curiosity wants to SEE it.

## Logging (Mandatory, via HubSpot MCP)

Same protocol as linkedin-outreach § Logging - the funnel is invisible without it:
1. **Their reply text** → note on the contact (LinkedIn replies live nowhere else; email replies may already sync, log if not).
2. **One-pager delivery** → note: `one-pager sent: [file] via [channel] YYYY-MM-DD`.
3. **Meeting proposed** → note with the three times offered.
4. **DEFERRAL** → HubSpot task on the contact, due at THEIR named window, assigned to the sender's owner ID.
5. **REDIRECT** → create/update the referred contact, note the referral source.

**NO signal push-back** (no new catalog research runs here) and **NO `last_enriched_date` bump** - this skill writes contact notes and tasks only, never enrichment or signal fields.

## Calibration Examples (authored - the house-validated set is voice-gold-standard §E)

**Email INTEREST - reply: "You've clearly done your research. I'm open to a call to discuss how we could pilot this."**

> Marc,
>
> Glad it landed, and a pilot is exactly the right frame, since this proves itself in a live path, not a deck.
>
> Three windows that work on my side: Tuesday 10am, Wednesday 2pm, Thursday 9am, all Eastern. If none fit, name one and I'll make it work.

*(48 words. Zero new pitch. One new thing: the pilot-frame affirmation. Three times, one ask.)*

**Email OBJECTION - reply: "We already have NNI partners for off-net. Not sure what this adds."**

> Dana,
>
> Fair, and keep them, since the partner relationships are the asset. The part I'd look at is what happens between your desk and theirs. The order goes out, and the wait on the far end is still quoted in weeks while your on-net side delivers in days. What I work on makes that partner leg provision at the same pace as your own, with the path and the customer staying yours.
>
> Worth 20 minutes to see whether it fits how your wholesale desk actually runs?

*(86 words. Concede-what's-true open, one mechanical distinction, soft ask. No competitor names, no feature list.)*

**LinkedIn DM QUESTION (mechanics) - reply: "Interesting. How does the partner on the far end get paid in this model?"**

> Ravi, good question and I want to get you the exact answer rather than the rough one, since the commercial side is the part everyone asks about second. Easiest is 20 minutes with the founder who designed it. I can set that up this week if you're open.

*(49 words. Do-not-improvise honored: no invented settlement mechanics. The precision of the question becomes the reason to meet.)*

**Email DEFERRAL - reply: "Timing's off - we're heads-down on the Charlotte build until Q3."**

> Sam,
>
> Makes sense, and honestly the conversation is better once Charlotte is lit anyway, since that's when the cross-carrier legs start to matter. I'll come back to you mid-Q3 unless you'd rather I didn't.

*(36 words. Their window anchored, permission asked, no sneaky pitch. Log the Q3 task.)*

## Quality Checklist

- [ ] Thread Receipt present and complete (channel, what we sent, what they did, class, activity scan, contact state, adds, must-not-repeat)
- [ ] Activity Scan ran (or "MCP unavailable" noted) - at most ONE found item leveraged, naturally
- [ ] Reply class identified and the matching move executed
- [ ] **NO pricing anywhere in the message** (numbers, ranges, comparisons - all banned in writing)
- [ ] **NO credibility anchors** (live spoken calls only)
- [ ] Non-redundancy gate passed: no reused angle/close/signal/phrase from ANY prior message, either channel
- [ ] Exactly ONE new thing added
- [ ] Federation-mechanics questions NOT improvised - verified facts or the escalation give only
- [ ] Competitor named only if the prospect named it first, once, then "the fabric"
- [ ] ONE ask, sized to what the reply earned
- [ ] Positive replies get three specific times (never a bare calendar link)
- [ ] Length fits the class (INTEREST ≤60 / QUESTION ≤120 email, ≤80 DM / WENT QUIET ≤40 / DM default 40-80 words)
- [ ] Email replies stay in-thread (Re: same subject); DM replies match the thread's register (lowercase if it runs lowercase)
- [ ] No em dashes/colons/dash-as-punctuation, no move-announcing transitions, no vendor language, customer names anonymized
- [ ] Reads like the same person kept thinking - passes the whole-thread read-through test
- [ ] Logging writes queued (reply note, one-pager note, meeting-proposed note, deferral task as applicable)

## Skill Chain

- **Preceded by:** cold-email or linkedin-outreach (this skill takes over on any reply or accept)
- **One-pager:** branded-doc § Outbound One-Pager Variant builds the asset; this skill writes the message it rides on
- **Objection substance:** context/core/differentiation-naas-aggregator.md (written register only)
- **QA:** copy-strategist
- **NOT for batches:** this skill is one-thread-at-a-time by design. sdr-pipeline is cold-only and never invokes it.
