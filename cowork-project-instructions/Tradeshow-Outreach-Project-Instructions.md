# Tradeshow Pre-Event Outreach — Processing Instructions

MaiaEdge is attending a tradeshow. These instructions govern how to process a contact list into send-ready, event-anchored outreach for **any** show (ITW, PTC, Metro Connect, Fiber Connect, NANOG, Capacity, etc.).

The motion: account-level research once per account, then a per-contact pass to flex the angle to the role. The work is in finding what's specific to each company AND each contact. Tradeshow attendance is the opener anchor; relevance from research is what earns the read.

These instructions inherit the writing rules from the MaiaEdge outreach skills — `skills/cold-email/SKILL.md`, `skills/linkedin-outreach/SKILL.md`, and the combined `skills/sdr-pipeline/SKILL.md`. Where this doc and those skills overlap, the skills are the source of truth.

---

## Event Configuration Block — Lock In Before Every Run

Fill this in at the start of each run. Everything downstream (CTAs, Email 3 timing language, hashtags, subject line) reads from these values. Do not start writing until every field is set.

| # | Variable | Value (fill per run) | Used in |
|---|----------|----------------------|---------|
| 1 | `EVENT_NAME` | e.g. ITW | Hooks, CTAs, Email 3, LinkedIn |
| 2 | `EVENT_FULL_NAME` | e.g. International Telecoms Week | HubSpot task search, shared-event matching |
| 3 | `EVENT_DATES` | e.g. May 18–21, 2026 | Email 3 timing nudge |
| 4 | `EVENT_VENUE` | e.g. Gaylord National Resort & Convention Center | QA location check |
| 5 | `EVENT_CITY` | e.g. National Harbor, Maryland | Email 3 CTA ("grab a few minutes in `[EVENT_CITY]`") |
| 6 | `SUBJECT_LINE` | e.g. `connect at itw?` — all lowercase, no variation | Configured in Smartlead, NOT stored in the output file |
| 7 | `EVENT_HASHTAGS` | e.g. #ITW26 (plus prior-event tags for warm matching: #PTC26, #MetroConnect26, #FiberConnect) | Shared-event matching on warm contacts |
| 8 | `SOURCE_FILE` + sheet name | e.g. `[Show]_R2_Final_v2.xlsx` / `Ready for Outreach` | Step 1 |
| 9 | `OUTPUT_FILE` | default `[Show]_[Round]_Written.xlsx` | Step 5 |
| 10 | `LINKEDIN_SCOPE` | **ASK at run start.** One of: `every-contact` (write a LinkedIn message for all contacts) OR `event-task-only` (LinkedIn only for contacts with an existing `EVENT_FULL_NAME` task in HubSpot, blank for the rest). | Step 3, Output Col 8 |
| 11 | `CREATE_HS_TASKS` | **ASK at run start.** yes/no — create a HubSpot LinkedIn task on each contact for the rep to send the message. See "LinkedIn Task Structure." | Post-write |

**Two run-start questions to confirm with the user before processing:**
1. LinkedIn scope — every contact, or event-task-only?
2. Create HubSpot LinkedIn tasks — yes or no?

---

## Source File

**Required columns (minimum):** First Name, Last Name, Title, Email, Account, Account Owner.

**Optional, used if present:** Domain, Customer Segment, Account Brief, Activity Status (blank = cold; `ACTIVE: ...` = warm).

If an optional column is missing, work with what's available — don't block.

---

## Output File

**Filename:** `OUTPUT_FILE` (default `[Show]_[Round]_Written.xlsx`).
**Build method:** create with headers on the first account batch, then append each account's contacts as they are processed and QA'd. **Save after every account.**

**Output columns (8):**

| Col | Header | Content |
|-----|--------|---------|
| 1 | First Name | From source |
| 2 | Last Name | From source |
| 3 | Title | From source |
| 4 | Account | From source |
| 5 | Email 1 | Full body text for Email 1 |
| 6 | Email 2 | Full body text for Email 2 |
| 7 | Email 3 | Full body text for Email 3 |
| 8 | LinkedIn Message | Target 35–50 words / max 280 chars (under LinkedIn's 300 hard limit). Per `LINKEDIN_SCOPE`: written for every contact, OR only for contacts with an existing `EVENT_FULL_NAME` task in HubSpot. Blank otherwise. |

**Subject line:** `SUBJECT_LINE`, configured in Smartlead, not stored in the output file.

**Skipped contacts** (exclusion list, active deal, research incomplete, etc.): include the row with First Name through Account populated. Put the skip reason in Email 1 (e.g. `SKIPPED: Active deal`). Leave Email 2, Email 3, and LinkedIn Message blank.

---

## Processing Model: Account-by-Account

Process the source file account by account (grouped by the Account column). All contacts at the same account share one round of account-level research. Each contact then gets a quick per-contact pass to adapt the angle to their role. The batch unit is the ACCOUNT, not an arbitrary group of N.

### Step 0: Pre-Read Reference Files

Before writing any emails, read these from the maiaedge-ai repo (paths relative to repo root):

**Voice + writing rules (mandatory every run):**
1. `context/copy-strategy/segment-language.md` — insider vocabulary, daily reality, conversational patterns per segment
2. `context/outreach/email-writing-rules.md` — core philosophy, angle-first, Research Receipt format, banned phrases, posture rules, Email 3 rotation, subject-line guidance
3. `context/outreach/fallback-messaging.md` — segment-specific fallback E1/E2/E3 templates when research is thin
4. `context/outreach/persona-targeting-blocklist.md` — **PRE-CADENCE GATE.** Title blocklist; blocked contacts route to Cooper-review queue
5. `context/outreach/pre-cadence-hygiene.md` — **PRE-CADENCE GATE.** Auto-bounce / OOO / LinkedIn-status filters before any contact enters the cadence
6. `context/outreach/sender-profiles.md` — Tim Lieto, Ken Cunningham, Tim Ziemer voice profiles
7. `context/copy-strategy/segment-messaging.md` — segment proof points, persona-pain mapping, anti-position framing
8. `context/copy-strategy/outbound-playbook.md` — multi-touch cadence and sequencing logic

**Skill rules (the writing contract this run follows):**
9. `skills/cold-email/SKILL.md` — angle-first cold email structure, Research Receipt hard gate, posture
10. `skills/linkedin-outreach/SKILL.md` — 35–50 word / 280-char LinkedIn format, no sender intro in body
11. `skills/sdr-pipeline/SKILL.md` — the combined 3-email + LinkedIn batch contract and QA bar

**Segment-specific (read for the segment of the account being processed):**
12. `context/segments/[segment].md` — colocation / fiber-operator / neocloud / network-operator / msp-aggregator / enterprise cheatsheet
13. `context/signals/signal-framework.md` + `context/signals/[segment]-signals.md` — universal + per-segment cataloged signals. Each Tier A signal's `Pattern:` field becomes a literal web search query in Step 2.

If a segment changes mid-run (research overrides source classification), reload the segment cheatsheet AND signals catalog before writing.

### Step 1: Load the Account

Pull all contacts for the next account. Identify: contact count, each contact's title / email / segment / account owner, whether an Account Brief exists, whether any contact has an Activity Status flag.

### Step 1.5: Activity Gate (Mandatory — Per Contact)

Before investing research time, run the activity gate per contact to prevent tone-deaf outreach to contacts already in conversation. When source data lacks these fields, pull from HubSpot.

| HubSpot field | Threshold | Action |
|---|---|---|
| `notes_last_contacted` within 14 days | **STOP** | `SKIPPED: Active conversation (last contacted YYYY-MM-DD)` |
| `notes_last_contacted` 15–30 days | **WARNING** | Flag for rep review before sending |
| `hs_sequences_is_enrolled` = true | **STOP** | `SKIPPED: Currently in HubSpot sequence [name]` |
| `hs_lead_status` = "Connected" or "Open Deal" | **STOP** | `SKIPPED: Lead status [status]` |
| `hs_lead_status` = "Attempted to Contact" | **CAUTION** | Don't repeat the prior angle |
| `num_contacted_notes` > 10 | **WARNING** | Email must be significantly differentiated |
| `linked_in_message` populated | **CAUTION** | LinkedIn already sent — don't duplicate |

**Active deal contacts:** review the deal carefully. May SKIP, or may need to complement (not conflict with) the existing sales conversation. Flag for rep review if unclear.

### Step 2: Account-Level Research (One Time Per Account)

**Start with the Account Brief.** If present, it's the baseline. Do NOT restate any of it in the emails. It exists to make the angle precise.

**The event is a public signal.** Registration / exhibitor list / speaker slot satisfies the Company-level finding line of the Research Receipt as a NON-CATALOG public signal. But event attendance ALONE is not a substitute for research — every attendee has the same event signal. What differentiates this email is the company-specific angle layered underneath.

**Catalog-grounded signal lookup (mandatory).** Ground web search in the segment's signals catalog, not generic "[company] news" queries.

1. Open `context/signals/[segment]-signals.md`. Read Tier A signals first.
2. Run each Tier A signal's `Pattern:` field as a literal web search query, substituting `[company name]`.
3. **Minimum 3 Tier A pattern searches.** If a HIGH-confidence Tier A hit lands, stop and layer it under the event opener.
4. **No Tier A hits → expand to Tier B patterns** from the same catalog.
5. **Cross-check `recent_news_or_trigger_event` in HubSpot** (populated weekly by weekly-signal-scan; web search wins where they disagree).
6. **Contact-level search:** `[Contact Name] [Company] LinkedIn` — role tenure, recent activity, what they own. Required even when company-level search found a signal.
7. **If web + HubSpot both come up empty across ≥5 query attempts:** signal code = NON-CATALOG (event-only), posture = ASKED, document the literal queries you ran.

**Signal Recency & Fact Validation (Research Quality gate — do this before any signal informs the angle):**

1. **Validate the Account Brief — don't trust it blind.** The brief is the baseline, not gospel. Confirm its core claims (segment, scale, ownership, product focus, footprint) against current web search. If the brief is older than ~30 days or research contradicts it, trust the fresh research and note the correction on the Receipt. A brief that has gone stale is a wrong-fact risk, not a shortcut.
2. **Only reference RECENT signals as the reason to meet.** Check each signal's EVENT date (`last_signal_date` = when the news/funding/hire actually happened, not when it was detected). Freshness windows from `context/signals/signal-framework.md`:
   - **≤60 days → full-strength, time-bound reason to meet.** This is the hook layered under the event opener: a fresh signal gives the conversation a reason to happen now.
   - **60–90 days → usable but softer.** Frame as context, not "just announced."
   - **>90 days → STALE. Do NOT reference as current.** Re-verify with a fresh search or drop it. Citing a >90-day event as if it's news is a wrong-fact failure.
   Longer-runway signals stay actionable past the raw window: exec hires (~90-day mandate), M&A (60–120d post-close), BEAD/grant builds (18–24mo ramp). A 50-day-old M&A is still hot; a 9-month-old "new hire" is not.
3. **Cross-check HubSpot `recent_news_or_trigger_event` against the live web.** This field is refreshed weekly and can be stale mid-week. Web search wins where they disagree. If HubSpot shows a signal the web can't confirm as still current, treat it as stale.
4. **No wrong facts.** Every fact that informs the angle must be verified against a dated primary source. Don't let dirty CRM data drive the angle — `infrastructure_profile` beats `annualrevenue` when they conflict (revenue data is wrong more often). If you can't verify a fact, don't build the angle on it. The fact never appears in the email anyway (research is invisible), but a wrong fact produces a wrong angle, and the recipient will catch it.

**For ACTIVE accounts (Activity Status flagged):** pull HubSpot call notes, email threads, meeting notes, deal status, task history. Look for shared event activity using `EVENT_HASHTAGS` and prior-event tags. If real history exists, use it: "We've connected with a few folks at `[Company]`" or "I think our teams were both at `[past event]` and didn't get a chance to connect." If activity is thin or ambiguous, don't force warmth — a slightly warmer cold email beats a fake warm one.

**For "Active deal(s)" contacts:** review the deal carefully. May SKIP, or complement (not conflict with) what's already happening. Flag for review if unclear.

**Check for an existing event task** (only required when `LINKEDIN_SCOPE = event-task-only`): search HubSpot tasks associated with each contact for any task mentioning `EVENT_NAME` or `EVENT_FULL_NAME`. A contact with such a task gets a LinkedIn message; otherwise leave Col 8 blank.

**State the account angle in one sentence:** "`[Company]` is `[doing X]`, which means `[specific problem]`." The angle must come from research, not the segment template. The event hook gets the door open; the angle earns the read. Fallback messaging is a last resort.

### Step 3: Per-Contact Email Writing

For each contact at this account:

1. **Quick role check** (no extra web research unless the title is unusual).
2. **Adapt the account angle to the role:**
   - C-level / VP Business → revenue, competitive positioning, market timing
   - CTO / VP Engineering → architecture, integration, operational overhead
   - VP Network / Network Ops → visibility, control, provisioning speed
   - Sales / Channel / Partnerships → ability to sell, speed to quote
   - Carrier Relations / Roaming → wholesale relationships, settlement, partner enablement
   - Other titles → infer from the title itself
3. **Segment Lock.** Confirm the segment from research (override source if mismatch). Re-read `segment-language.md` for that segment's vocabulary if it's been more than 5 accounts since the last load. Use ONLY that segment's vocabulary.
4. **Posture decision (DIRECT or ASKED).** Match the move to the research:
   - **DIRECT** = declarative problem statement. Use when a HIGH-confidence Tier A cataloged signal exists under the event hook AND the contact is a technical buyer.
   - **ASKED** = illumination question or premise hedge ("Probably already on your radar, but…"). Use when the only signal is the event itself, or the contact is a senior business buyer, or the pain is variable across the segment.
   - Not randomized to a quota.
5. **Emit a Research Receipt (HARD GATE).** Before writing any email body, emit a complete four-section Receipt. No Receipt = do not write. Format below.
6. **Write 3 emails** per the framework below. **Posture rotates across the sequence:** if E1 is DIRECT, E2 is ASKED. E3 takes a "show is coming up" close regardless.
7. **Write the LinkedIn message** per `LINKEDIN_SCOPE`. When written, LinkedIn posture should differ from E1. Same research and angle, compressed to 35–50 words / ≤280 chars.

### Research Receipt (Hard Gate Before Each Email Body)

Every email and LinkedIn message must be preceded by a Research Receipt — the SAME format used by `skills/cold-email/SKILL.md`, `skills/linkedin-outreach/SKILL.md`, and `skills/sdr-pipeline/SKILL.md`. An email without a Receipt is invalid output — restart that contact from research.

```
RESEARCH RECEIPT — [Contact First Last] @ [Company]

Segment: [segment / sub-segment]   Status: VERIFIED | CORRECTED from [X]
Catalog: context/signals/[segment]-signals.md

Searches run (literal query strings — not paraphrased):
1. `[exact query]` → [URL + date, OR "no Tier A hit"]
2. `[exact query]` → [URL + date, OR "no Tier A hit"]
3. `[exact query]` → [URL + date, OR "no Tier A hit"]
[min 3 if claiming a cataloged signal; min 5 if claiming NON-CATALOG (event-only)]

Company-level finding: [signal + source quote + date. Event registration/exhibitor list counts as NON-CATALOG signal — cite it. If a deeper Tier A/B signal was found, cite that too.]
Contact-level finding: [what THIS contact owns / recent role activity / why they care about THIS facet. REQUIRED on every Receipt.]
Brief validation: [VERIFIED against current research | CORRECTED: (what changed) | NO BRIEF]
Signal recency: [event date YYYY-MM-DD — FRESH ≤60d | AGING 60–90d | STALE >90d → re-verified or dropped. The deeper signal, not the event itself.]

Signal code: [F-A1 | NC-A2 | NO-B3 | NON-CATALOG | NONE]
Posture: [DIRECT | ASKED] — [one-line reason tied to the finding]

---

Subject: [SUBJECT_LINE per Smartlead config]

[email body]
```

**Refuse-to-write rule:** if you cannot honestly fill all four sections (≥3 literal queries with results, Company-level finding, Contact-level finding, Posture with reason), output `RESEARCH INCOMPLETE: [reason]` in place of the email body, mark the contact `SKIPPED: Research incomplete`, and move on. Do NOT fabricate a Receipt. The Receipt is review metadata above the body — it does not get sent.

### Step 4: Copy Strategist QA Pass

Before appending, review every email in the account batch:

- **Research Receipt present** above every email and LinkedIn body — ≥3 literal queries with results (≥5 if NON-CATALOG), Company-level finding, Contact-level finding, Posture with reason.
- **Recipient's-eye read:** would they read past the first sentence? Does it sound like someone who knows their world? Is the angle specific to THIS company, not a generic segment pain?
- **Research invisibility (most important rule):** no displayed company facts, facility counts, route miles, revenue, funding, project names, or "I noticed" observations. If a sentence reads like "I googled you," cut it.
- **Signal recency:** the angle leans only on a FRESH signal (event date ≤90 days, ideally ≤60). No stale signals referenced as current. Where a fresh signal exists, it is used as the time-bound reason to meet.
- **Fact accuracy:** Account Brief validated against current research; angle-driving facts verified against dated sources; no wrong facts. `infrastructure_profile` beats `annualrevenue` on conflict.
- **Pressure-off:** peer suggesting a conversation, not a salesperson pushing a meeting. No urgency tactics, no manufactured scarcity. CTAs optional and easy to decline.
- **Warm angle authenticity (ACTIVE contacts only):** any referenced past interaction must be HubSpot-backed. If warmth would be a stretch, soften or remove.
- **Value bridge** is 1 sentence max, embedded by contrast or standalone-but-punchy, in "I" voice. No brand-voice constructions ("We help operators…" / "We built infrastructure that…"). Multi-sentence value bridges are BANNED.
- **Mechanical:** no em dashes, no banned phrases, no competitor names, no customer names, no credibility anchors. Correct sender per Account Owner. Location is `EVENT_CITY` / `EVENT_VENUE`.
- **Word count:** Email 1 ~70–85 words; Email 2 under 55; Email 3 2–3 sentences. (Tighter than legacy per-segment targets — keep it under the ceiling, not at it.)
- **First name** before the email body.
- **Posture rotates** across E1/E2/E3 — not all the same.
- **Hedge variety:** "I'd guess" / "I'd imagine" in ≤30% of E1s per batch of 10+. Mix in direct assertions, illumination questions, premise hedges, peer observations.
- **LinkedIn check (where written):** 35–50 words / ≤280 chars, no sender intro in body, company-specific problem fused into the observation, soft CTA optional, Research Receipt above. LinkedIn posture differs from E1. Event is the opener OR the CTA anchor — not both.
- **Sequence:** 3 distinct angle categories (revenue / competitive / operational / market timing / cost-of-inaction / peer social proof), CTAs rotated, reads like a real person coming back with new thoughts. Standalone test: would E2 still make sense with E1 removed?

### Step 5: Append Account to Output File

Write all contacts for this account. Save after every account.

### Step 6: Report and Continue

Briefly: account name, contact count, any skips, whether warm angles were available, any segment corrections, any LinkedIn messages written. Then proceed immediately to the next account. Do NOT wait for user confirmation between accounts.

---

## The Pre-Event Email Framework

### Email 1 (~70–85 words): Event Opener + Problem + CTA

1. **Event hook (1 sentence):** natural reference. For confirmed attendees: "saw you in the app." For lists: "saw `[company]` on the exhibitor list." For ACTIVE contacts with HubSpot event history: "I think our teams were both at `[past event]` and didn't get a chance to connect." The event hook IS the public-signal observation — cite it in the Receipt's Company-level finding.
2. **Problem/angle pivot (1–2 sentences):** the company-specific angle from research. The recipient should think "this person understands what we're dealing with" without seeing a single fact about their company stated back.
3. **Value bridge (1 sentence MAX, embed-by-contrast preferred):** how MaiaEdge relates. Segment vocabulary only. "I" voice. No brand-voice constructions.
4. **CTA (1 sentence):** event-anchored, low-pressure. Optional when an illumination question carries the close.

**Default Email 1 CTA:** "Open to setting some time up at the show?"

### Email 2 (under 55 words): New Angle, No Re-Introduction

No re-introduction. No "following up." No meta-references like "the other angle on this." Lead straight into a different dimension of the problem.

1. **New thought (2–3 sentences):** a genuinely different angle on the same underlying problem — peer observation, market shift, or different facet.
2. **CTA (1 sentence):** rotated from Email 1, opens the door to a delegate.

**Default Email 2 CTA:** "Would be great to find time to sit down while we are all at the show, or happy to start with someone on your team. Either way works."

### Email 3 (2–3 sentences max): Show Is Coming Up

Not a graceful exit — a "the event is around the corner" nudge.

1. **Timing nudge (1–2 sentences):** `EVENT_NAME` is approaching (reference `EVENT_DATES` casually if natural). Human, low-key.
2. **Soft close (1 sentence):** door open. **Exactly ONE CTA** — never a conditional close plus a second close.

**Email 3 CTA options (rotate for variance, swap `EVENT_NAME`/`EVENT_CITY` per run):**
- "If this is worth a conversation, happy to find time at the show."
- "Either way, hope to cross paths at `EVENT_NAME`."
- "If the timing's right, let's grab a few minutes in `EVENT_CITY`."
- "Happy to pick this up at `EVENT_NAME` if it makes sense."

Do NOT reuse the same CTA phrasing across the 3 emails for a given contact.

### LinkedIn Message (per `LINKEDIN_SCOPE`)

**Length:** target 35–50 words, max 280 chars (under LinkedIn's 300 hard limit). This is NOT a miniature email — it's a connection request that proves you understand their world in one breath.

**Pattern:** `[First name], [observation/question with company-specific signal]. [Optional: one sentence of context]. [soft CTA or none].` The company-specific detail IS the problem statement — fused, not sequential. The contrast pattern does the heavy lifting: name what works, then name what doesn't; the gap is the MaiaEdge opportunity. Value bridge embedded by contrast, "I" voice.

**No sender intro in the body.** The recipient already sees the sender from LinkedIn's UI. "Tim from MaiaEdge" in the body is redundant and triggers the sales-pitch reflex — banned.

**Soft CTAs:** "Worth connecting?" / "Can we find time to connect at the show?" / "Worth connecting at the show?"

`EVENT_NAME` is the opener ("Saw you're heading to `EVENT_NAME`" / "Will you be at `EVENT_NAME`?") OR the CTA anchor ("at the show") — not both. Open with the recipient's first name, then directly into the observation.

**Research Receipt** required above every LinkedIn message — same four-section format. NONE valid only with ≥5 literal queries.

**Avoid:** generic "let's connect at `EVENT_NAME`," compressed-email format, flattery/congratulations, listing MaiaEdge features, more than one MaiaEdge sentence, brand-voice constructions, sender intro in body.

---

## LinkedIn Task Structure (If `CREATE_HS_TASKS = yes`)

Create a HubSpot task on each contact (assigned to the Account Owner):

- **Task type:** LinkedIn (or "To-Do" if LinkedIn type unavailable)
- **Title:** `Send LinkedIn message — [Contact First Name] [Last Name]`
- **Due date:** same day as Email 1 send, or per the rep's preference
- **Body format (CRITICAL):**

```
[LinkedIn profile URL]

[LinkedIn message body]
```

URL on its own top line, blank line, then the message. No labels ("URL:", "Message:"), no extra text. If the LinkedIn URL isn't in the source or HubSpot, leave the URL line blank but still create the task with the message body.

---

## Tone and Voice — Critical

**Diplomatic and pressure-off.** A peer suggesting a useful conversation, not a salesperson booking a meeting. Zero pressure. CTA always optional.

**Research is INVISIBLE.** The single most important rule. Research makes the angle precise and the vocabulary correct. It NEVER appears as displayed facts, stats, or "I noticed." If a sentence could read as "I googled you," cut it.

**No fake familiarity.** Warmth comes from real shared history (HubSpot-verified) only. A direct, respectful cold approach beats forced familiarity.

**Short and manual-feeling.** Looks like someone typed it in Gmail. 2–3 tight paragraphs max. Fragments OK. One idea per email. First name before the body.

**Write as the Account Owner.** Use the sender from the source file (Account Owner column). Match their voice from `sender-profiles.md`.

---

## Hard Bans (Non-Negotiable)

- **No em dashes.** Use periods or commas.
- No "Hope this finds you well" / "Just wanted to reach out" / "I noticed" / "Revolutionary" / "Game-changing" / "Reason I'm reaching out."
- **No customer names.** Anonymize: "one fiber operator," not the actual name.
- **No competitor names.** "Third-party fabric" only where the segment fits — works for fiber operators and aggregators, NOT for Tier 1 network operators or carrier relations/roaming roles.
- **For colos:** don't lean on "lose revenue to third-party fabrics" — find research-based angles instead.
- **No credibility anchors** (no Acme Packet, no 128 Technology) in cold or LinkedIn.
- **No specific NNI/provisioning timelines** (60-day, 90-day) — varies by operator.
- **No "describing them back"** openers ("For a `[role]` at a `[type of company doing X]`…") — salesy and lecturing.
- **No sign-offs** — signatures are auto-appended by the platform.
- **No restating company facts** (revenue, facility counts, route miles, funding, project names).
- **Category descriptor:** "Carrier infrastructure" only (never IaaS, NaaS, platform).
- **Neocloud:** OPERATOR sovereignty banned. DATA sovereignty allowed. No network jargon.

---

## Segment Handling

If the source has a Customer Segment, validate it against research and override if research shows otherwise. Use the overridden segment's vocabulary and angles.

For "Other" / "Enterprise" / any unclear segment: determine the best-fit MaiaEdge segment during account research. If genuinely enterprise-only (internal network, no wholesale) or on the exclusion list, SKIP.

**Enterprise (Multi-DC ICP):** `Enterprise-CustomerSegment` is an ICP segment. Evaluate against the four Enterprise sub-segments (`Financial Services`, `Healthcare Systems`, `Retail and Distribution`, `Outsourcing Services` — Enterprise) AND the hard scale gate ($1B+ revenue + 3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house net eng). Both gates pass → target via Enterprise lead-angle templates. Either gate fails → SKIP. Anchor account: Meijer.

### Exclusion List (SKIP and mark in output)

IXP, Tower REIT, IT MSP (helpdesk/break-fix), Retail ISP (no wholesale), Software vendor, Hyperscaler (AWS/Azure/GCP/Meta), Enterprise failing the scale or vertical gate (sub-$1B mid-market, single-DC, network outsourced to a single MSP, no direct carrier contracts, or Watch List verticals — Manufacturing / Energy-Utilities / Logistics / Government-Defense), Under 7 employees, Vendor/Contractor/Manufacturer, Consulting firm (Deloitte/McKinsey/BCG/Bain are project firms and excluded; Cognizant/Genpact/Concentrix/TaskUs with operational delivery centers ARE Outsourcing Services — Enterprise ICP), Trade organization, Defunct/Acquired.

---

## Active Contact Handling

For contacts with Activity Status flagged:

1. **Check HubSpot first.** Call notes, email threads, meeting notes, deal status, task history.
2. **Work the warm angle if it's real.** Reference genuine interaction history naturally.
3. **Check shared event history** using `EVENT_HASHTAGS` and prior-event tags. If found: "I think our teams were both at `[event]` and didn't get a chance to connect."
4. **Active deal(s) contacts** require extra care. Review the deal. May SKIP, or complement (not conflict with) the existing conversation. When in doubt, skip and flag.

**Activity types in the source file:**
- `ACTIVE: Logged interactions` — call/meeting notes exist. Use them.
- `ACTIVE: Recent email engagement; Logged interactions` — email threads exist. Check tone and recency.
- `ACTIVE: Active deal(s)` — deal in pipeline. Review before writing. May skip.

---

## Territory Model

| Territory | Owner | Coverage |
|-----------|-------|----------|
| East | Tim Lieto | AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV |
| West | Ken Cunningham | AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND, NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY |
| International | Tim Ziemer | All non-US |

The Account Owner column already has the correct sender. Use that value. If the source owner doesn't match the territory model for the company's HQ state, note it (informational, not a STOP — could be a deliberate cross-territory play).

---

## Proof Points (Anonymized — Use Sparingly)

| Use Case | Reference |
|----------|-----------|
| Speed | "One fiber operator went from 60–90 day provisioning to under 10 minutes." |
| Sovereignty | "A colo operator told us with third-party fabrics, 'you turn the customer over to them.' With MaiaEdge, they control their destiny." |
| Simplicity | "One operator called it 'fabric in a box. Drop it in, add water, it works.'" |
| Scale | "Deployed across 800+ cell towers and 20+ data centers for a network operator." |
| Reach extension | "A fiber operator in the Pacific extends reach to the mainland without new infrastructure." |
| Multi-carrier | "We're working with an aggregator that uses MaiaEdge to unify visibility across all upstream carrier partners." |

---

## Quality Checklist (Every Account Batch)

**Research Quality**
- [ ] Account Brief read, used as baseline (not displayed), AND validated against current research — corrections noted on the Receipt
- [ ] Catalog-grounded web search (≥3 Tier A patterns; ≥5 queries if NON-CATALOG)
- [ ] HubSpot checked for ACTIVE accounts (activity, deals, tasks, events)
- [ ] Segment validated against research
- [ ] Every referenced signal's event date ≤90 days (ideally ≤60); no stale signals cited as current
- [ ] A fresh signal, where one exists, is used as the time-bound reason to meet
- [ ] No wrong facts — angle-driving facts verified against dated sources; `infrastructure_profile` beats revenue on conflict
- [ ] HubSpot `recent_news_or_trigger_event` cross-checked against live web (web wins on conflict)
- [ ] Company-specific angle stated in one sentence, from research not template
- [ ] Event task checked (only when `LINKEDIN_SCOPE = event-task-only`)
- [ ] Research Receipt emitted above every email and LinkedIn body

**Email Quality**
- [ ] Research is INVISIBLE
- [ ] Diplomatic, pressure-off tone
- [ ] Within word count (E1 70–85 / E2 <55 / E3 2–3 sentences)
- [ ] No em dashes, banned phrases, competitor/customer names, credibility anchors
- [ ] Value bridge 1 sentence, "I" voice, no brand-voice constructions
- [ ] CTA event-anchored and low-pressure; rotated across all 3 emails
- [ ] Each email a genuinely different angle; E2 doesn't reference E1; E3 has "show is coming up" energy
- [ ] Posture rotates across the sequence; hedge variety respected
- [ ] Correct sender per Account Owner; location is `EVENT_CITY` / `EVENT_VENUE`
- [ ] Warm angle HubSpot-backed (ACTIVE only)

**LinkedIn Quality (where written)**
- [ ] 35–50 words / ≤280 chars; no sender intro in body
- [ ] Company-specific, fused into a problem statement
- [ ] `EVENT_NAME` as opener OR CTA anchor, not both
- [ ] Reads like a real connection request, not a compressed email
- [ ] Research Receipt above it

**Sequence Quality**
- [ ] 3 distinct angle categories across the sequence
- [ ] CTA phrasing rotated across all 3 emails
- [ ] Reads like a real person coming back with new thoughts
- [ ] Standalone test passes (E2 makes sense with E1 removed)

---

## End-of-Run Summary

After all accounts are processed, report:
- Total contacts processed / total in source file
- Total skipped (with reason breakdown)
- Total segment corrections
- Total LinkedIn messages written
- Active account handling summary (warm angles used, deals flagged)
- HubSpot tasks created (if `CREATE_HS_TASKS = yes`)
- Output file location
