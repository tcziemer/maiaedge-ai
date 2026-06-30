# Modern Outbound Playbook  -  2024-2026 Best Practices

What's actually working in B2B enterprise outbound right now, based on benchmarks and data. Reference this when critiquing sequences or recommending strategy.

---

## Reply Rate Benchmarks (2025-2026)

Know what "good" looks like so you can calibrate advice:

| Metric | Average | Good | Excellent | Best-in-Class |
|---|---|---|---|---|
| Cold email reply rate | 3-5% | 5-8% | 8-12% | 12%+ |
| Open rate | 25-35% | 35-50% | 50-65% | 65%+ |
| Meeting booked rate (from replies) | 25-35% | 35-50% | 50%+ |  -  |
| LinkedIn connection accept rate | 20-30% | 30-45% | 45%+ |  -  |
| LinkedIn InMail response rate | 10-15% | 15-25% | 25%+ |  -  |

**For MaiaEdge specifically** (enterprise infrastructure, C-level targets):
- Expect lower volume but higher quality. A 5-8% reply rate to C-suite at fiber operators is strong.
- Anything above 10% reply on a well-targeted, well-researched sequence is exceptional.
- Meeting-to-reply conversion should be 30-40% with proper follow-up.

**House baseline (2026-06-11 retro, 4,614 sends / 1,934 contacts, Mar-Jun 2026):** 1.2% human-reply, 0.93% positive, 44% positive→held-meeting. Event-anchored waves ran 1.0-4.4% positive; anchor-less June waves ran 0.0%. **Targets:** event/anchored 4-6% human reply (2-3% positive); craft-structure cold 2-3% human reply (1-1.5% positive); hold reply→meeting ≥40%. Track HUMAN-reply rate, not raw replies (51% of raw replies in the corpus were OOO/auto).

---

## Sequence Architecture  -  What's Working Now

### Optimal Sequence Length
The data is clear: **3-5 emails over 10-17 days** is the sweet spot for enterprise B2B.

- Industry data says 58% of replies come on Email 1 — **the house data disagrees: E2 is our workhorse** (8 of 18 all-time positives on E2, 6 on E1, 4 on E3; the short E3 nudge booked 2 meetings). Keep all three touches.
- Email 2 can boost reply rates by up to 49% (this is the highest-leverage follow-up)
- Email 3 still adds ~20% incremental replies
- By Email 4-5, returns drop off sharply (55% decline from earlier emails)
- Beyond 5 emails in a single thread: diminishing or negative returns

**For MaiaEdge's 3-email Smartlead sequences, this is well-calibrated.** The architecture is:
- Email 1: Full research-driven opening (Day 1)
- Email 2: Follow-up with new angle (Day 4-5) -- must come from a DIFFERENT angle category than Email 1
- Email 3: Breakup with final value hook (Day 10-12)

**Email 2 Angle Diversity (Mandatory):** Email 2 must come from a different angle CATEGORY than Email 1. Six categories: Revenue, Competitive, Operational, Market Timing, Cost-of-Inaction, Peer Social Proof. Standalone test: if you removed Email 1 from the sequence, would Email 2 still make sense as a standalone thought? If it depends on Email 1 for context, it's not differentiated enough. Cap "one operator told us..." at 1 per 3-email sequence.

### The 3-7-7 Cadence
Recent data shows the **3-7-7 follow-up cadence** captures 93% of total replies by Day 10:
- Day 0: Email 1
- Day 3: Email 2
- Day 10: Email 3

After Day 10, additional follow-ups produce marginal or negative returns for cold outreach. Save further touches for LinkedIn or phone.

### Multi-Channel Sequencing
The best campaigns in 2025-2026 layer multiple channels:

**Recommended MaiaEdge cadence (updated 2026-06-12 — LinkedIn leads, email carries the ask):**
```
Day -3: LinkedIn connection request (craft voice, ≤280 chars, from the rep/founder)
        → on ACCEPT (+24-48h): thank-you DM + account one-pager (branded-doc outbound
          variant), pressure-off, no CTA push. LOG accept + delivery per linkedin-outreach.
Day 0:  Email 1 (craft structure: structural truth → craft line → show-me give → call-ask)
        Same-account contacts staggered ≥48h; never the same morning; ≤3/account per wave.
Day 4:  Email 2 (new angle; for accepted contacts, name ONE claim from the one-pager and
        carry the meeting ask here)
Day 9:  Email 3 (one actionable ask; timing nudge if a real window exists, else take-away)
Any reply → propose three specific times (never a bare calendar link).
Any unsub/negative at an account → stop ALL contacts at that account.
```

**Anchor inventory, ranked by observed yield (retro 2026-06-11):** live event presence (4.4% positive) > event 2-3 weeks out (1.0-1.8%) > market catalyst calibrated to seat (Campaign A pattern, unproven) > rep travel (weak) > anchor-less diagnosis copy (0.0% — banned shape; the craft structure manufactures the why-now instead).

**The show-me give is a standing cold asset:** live demo is ready (confirmed 2026-06-12). "Fifteen minutes and I can show you the whole thing end to end" — demo pull was the strongest cold behavior in the corpus (a CEO replied asking for "a real demo"; another went to the website and asked to see it end to end).

**Channel strengths:**
- **Email**: Detail, research demonstration, specific value props
- **LinkedIn**: Warmth, peer connection, thought leadership credibility
- **Phone**: Urgency, rapport, handling objections in real-time
- **Video (Loom)**: Category education, technical deep-dives (use sparingly, later in sequence)

---

## Email Copy  -  What's Driving Replies in 2026

### Length: Shorter is Winning

The data is dramatic:
- Companies that trimmed emails by 40% saw: open rates +86%, reply rates +181%, meetings +78%
- One point. One CTA. One reason to reply.

**For MaiaEdge:** Sequence length is governed by hard caps in `context/outreach/email-writing-rules.md` - Email 1 at 85-110 words, Email 2 under 55 words, Email 3 at 2-3 sentences max. These caps apply across every segment. A tight email under the cap beats a padded one that hits any number.

### Hook Types  -  What's Working

Recent data on hook effectiveness:

| Hook Type | Reply Rate | Notes |
|---|---|---|
| **Timeline hook** (compressed achievement) | 9.9-10.7% | Best performer. "In 10 minutes instead of 90 days." |
| **Peer proof hook** | 7-9% | "One operator we work with..." Social proof opening. |
| **Market shift hook** | 6-8% | "The infrastructure landscape is shifting..." Works for C-suite. |
| **Problem-statement hook** | 3.9-4.8% | Generic problem naming. Underperforms because everyone does it. |
| **"I noticed" hook** | 2-4% | Dead. Instantly signals automation. Avoid. |

**For MaiaEdge:** Timeline hooks and peer proof hooks are natural fits. "One fiber operator went from 60-90 day provisioning to under 10 minutes" is a timeline hook with peer proof. That's the sweet spot.

### Personalization Depth

The science is settled: deep personalization crushes generic:
- Personalized subject lines: +50% open rates
- Tailored content: +32.7% response rates
- Highly-targeted small campaigns outperform broad blasts by 2.76x
- 73% of decision-makers say personalization matters

**What "deep" means for MaiaEdge:**
- NOT: "I saw your LinkedIn post about..." (surveillance)
- NOT: Merge tags alone ({first_name}, {company})
- YES: Company-specific problem hypothesis based on research
- YES: Research that SHAPES which problem you name (the expansion informs the angle -- it doesn't appear in the email as "your recent expansion into...")
- YES: Understanding of their specific infrastructure challenges, expressed as problems they live with
- YES: Role-appropriate framing of the problem (but never "At the [role] level" or "From a [function] standpoint" -- just state the problem directly)

**The research investment:** 10-15 minutes per enterprise prospect. This is what separates 3% reply rates from 10%+ reply rates.

### Subject Lines

**What's working:**
- 4-7 words
- Company name or specific topic
- No clickbait, no hype. **Genuine, substantive questions are allowed for cold** ("how do you handle paths beyond Jamaica?" earned the only pure-cold E2 positive in the house corpus); empty "Quick question" stays banned.
- Good: "[Company] provisioning" / "[Company] interconnection" / "Cross-carrier paths at [Company]"
- Bad: "Quick question" / "Unlock new revenue" / "The future of connectivity"

**2026 trend:** Subject lines that read like internal email subjects (simple, specific) outperform marketing-style subjects by 2-3x.

---

## Deliverability  -  The Foundation

None of this matters if emails don't reach the inbox.

**Non-negotiable checklist:**
- SPF/DKIM/DMARC authenticated
- Spam complaint rate under 0.3%
- Bounce rate under 2%
- Domain warmed up (gradual volume increase over 2-4 weeks)
- Max 50-100 sends per mailbox per day for cold outreach
- Engagement quality matters: ESPs increasingly weight time-spent-reading and reply depth

**MaiaEdge-specific:** Because we're targeting C-suite at infrastructure companies, inbox placement is critical. These are corporate email systems with sophisticated filtering. Every email must look like genuine human correspondence, not bulk outreach.

---

## 2026 Trends Shaping Strategy

### Precision Over Volume
The winners are running intelligence-led outbound: hitting prospects at the right moments using intent signals, not blasting lists. For MaiaEdge, this means:
- Timing signals (expansion, funding, leadership change, competitive threat) are the single biggest predictor of reply rates
- A well-timed email to one person beats 100 untargeted emails

### AI-Augmented, Human-Finished
Elite teams use AI for 80% of research and sequencing, then apply human judgment for the final 20%. The skill-builder pipeline (research → draft → human review → send) is the right model.

### Engagement-First Metrics
Reply rate alone is outdated. Leading indicators now include:
- Reply quality (positive/neutral/negative sentiment)
- Conversation depth (multi-reply threads)
- Meeting conversion rate
- Pipeline generated per sequence

### Multi-Threading by Default
For enterprise accounts ($100M+ target companies), sequence to 3-5 stakeholders simultaneously with coordinated messaging. Each stakeholder gets role-specific framing of the same core message.

### The 12-Month Nurture Reality
Enterprise deals take 9-18 months. The cold sequence is just the opening move. Build toward:
- Educational check-ins quarterly
- Trigger-event re-engagement
- Content-based touchpoints (research, case studies)
- Conference/event-based reconnection

---

## Persona Targeting Discipline (pre-cadence gate, 2026-05-11)

The replied-thread audit isolated persona-mistargeting as the single largest non-content driver of the depressed reply rate in the 60-day Smartlead corpus. ~15% of replies were wrong-persona redirects ("not my purview," forward-to-engineer, hostile unsubscribe). Fixing the title-targeting model lifts reply rate by ~0.5-1.0 points before any copy work compounds.

The full blocklist lives in `context/outreach/persona-targeting-blocklist.md`. The gate runs at the SDR pipeline stage before any contact enters Smartlead or a LinkedIn batch cadence. High-level summary:

- **Universal blocks:** Account Executive, Account Manager, Customer Success Manager.
- **Aggregator / NaaS / TSD blocks:** Director - Carrier Wholesale, Wholesale Manager, Director - Sales (Wholesale).
- **Fiber / ISP blocks:** Director - Field Operations, GM / Regional Operations Manager.
- **International carrier blocks:** Country Manager / GM - [Country] at carriers with HQ product orgs, Finance Director / Treasurer.

Blocked contacts route to a Cooper-review queue, not silently dropped. The Wholesale-Director partner-recruitment cadence (Sidecar Decision 11) is deferred - if a Konnexx-pattern engagement materializes, that motion gets a separate cadence outside the standard SDR pipeline.

## Pre-Cadence List Hygiene (pre-cadence gate, 2026-05-11)

11 of 34 replies in the 60-day corpus were auto-OOO, address-change, autoresponder, unsubscribe-bot, "I retired," or sender-bounce - 32% of all replies on no-content signal. These don't lift raw reply count but lift signal density: every auto-OOO suppressed is a slot freed for a contact who can actually buy.

The three filters live in `context/outreach/pre-cadence-hygiene.md`. Expected impact: ~10-15% relative lift on reply-rate as a metric (raw reply count holds, denominator drops as bounce/OOO contacts are removed before the second touch).

- **Filter 1 - Auto-bounce / autoresponder detection:** suppress from E2/E3 after a first-send autoresponder.
- **Filter 2 - OOO detection at send-time:** delay the cadence until after declared return.
- **Filter 3 - LinkedIn-status check on lead pull:** flag for re-research if current role differs from source list.

## A/B Testing Framework

When recommending or designing A/B tests:

### Variables Worth Testing (High Impact)
1. **Subject line**  -  Easiest to test, significant impact on open rates
2. **Opening hook type**  -  Timeline vs. peer proof vs. market shift
3. **CTA phrasing**  -  "Open to a conversation?" vs. "Dealing with something similar?"
4. **Email length**  -  Full version vs. stripped-down version
5. **Angle**  -  Competitive threat vs. operational efficiency vs. revenue opportunity

### Variables Not Worth Testing (Low Impact)
- Sender name formatting (first name vs full name)
- Minor word choice within body
- Signature format
- Send time (within the 7-11am window)

### Testing Protocol
- Minimum sample: 50 sends per variant (100+ preferred)
- Run for full sequence cycle (10-14 days) before evaluating
- Primary metric: reply rate (not open rate)
- Secondary: positive reply rate, meeting booked rate
- Statistical significance: 95% confidence before declaring a winner

---

## Critique Calibration

When scoring MaiaEdge copy, use these benchmarks:

**A 7/10 email should:**
- Get a 5-8% reply rate on a well-targeted list
- Make the recipient think "this person actually knows my industry"
- Have a clear, specific problem hypothesis
- Be within the sequence caps with no filler

**A 9/10 email should:**
- Get a 10%+ reply rate
- Make the recipient think "I need to talk to this person"
- Feel like it could ONLY have been written for them
- Have a surprising insight or observation they haven't considered

**A 5/10 email should:**
- Get a 2-3% reply rate (below average but not spam)
- Feel competent but forgettable
- Have the right general angle but lack specificity
- Be "good enough to send" but "not good enough to stand out"
