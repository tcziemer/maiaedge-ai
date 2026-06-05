# Cold List Outreach — Processing Instructions

These instructions govern how to process a cold contact list into send-ready outreach. No event anchor — relevance comes entirely from research. Same account-by-account motion as tradeshow runs, but the work is harder because there's no shared moment to lean on. A fresh, verified signal IS the reason to reach out now.

These instructions inherit the writing rules from the MaiaEdge outreach skills — `skills/cold-email/SKILL.md`, `skills/linkedin-outreach/SKILL.md`, and the combined `skills/sdr-pipeline/SKILL.md`. Where this doc and those skills overlap, the skills are the source of truth.

---

## Per-Run Variables (Lock In Before Starting)

Confirm these at the start of every run:

1. **Source file path and sheet name**
2. **Output file name** (default: `[ListName]_Written.xlsx`)
3. **Subject line(s)** — varies per run, lock in here. Configured in Smartlead, not stored in the output file.
4. **LinkedIn messages: yes or no?** — ASK before the run starts. If yes, every contact gets a LinkedIn message in addition to the 3 emails. If no, leave the LinkedIn column blank.
5. **Create HubSpot LinkedIn tasks: yes or no?** — ASK before the run starts (only relevant if LinkedIn messages are enabled). If yes, create a HubSpot task on each contact for the rep to send the LinkedIn message. See "LinkedIn Task Structure" below.

---

## Source File

**Required columns (minimum):** First Name, Last Name, Title, Email, Account, Account Owner.

**Optional, used if present:** Domain, Customer Segment, Account Brief, Activity Status.

If an optional column is missing, work with what's available — don't block.

---

## Output File

**Output columns (8):**

| Col | Header | Content |
|-----|--------|---------|
| 1 | First Name | From source |
| 2 | Last Name | From source |
| 3 | Title | From source |
| 4 | Account | From source |
| 5 | Email 1 | Full body text |
| 6 | Email 2 | Full body text |
| 7 | Email 3 | Full body text |
| 8 | LinkedIn Message | Target 35–50 words / max 280 chars (under LinkedIn's 300 hard limit). NO sender intro in body. Research Receipt above (see `skills/cold-email/SKILL.md` and `skills/linkedin-outreach/SKILL.md` for the four-section format). Only if confirmed at run start, otherwise blank. |

**Build method:** create with headers on the first account batch, then append each account's contacts as they are processed and QA'd. **Save after every account.**

**Skipped contacts:** include the row with First Name through Account populated. Put the skip reason in Email 1 (e.g. `SKIPPED: Active deal`). Leave the other columns blank.

---

## Processing Model: Account-by-Account

Group contacts by Account. All contacts at the same account share one round of account-level research. Each contact then gets a per-contact pass to flex the angle to their role. The batch unit is the ACCOUNT.

### Step 0: Pre-Read Reference Files

Before writing, read these from the maiaedge-ai repo (paths relative to repo root):

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

Pull all contacts for the next account. Identify: contact count, each contact's title / email / segment / owner, whether an Account Brief exists, whether any contact has an Activity Status flag.

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

**Territory check:** if the source's Account Owner doesn't match the territory model below for the company's HQ state, note it (informational, not a STOP — user may be running a cross-territory play).

### Step 2: Account-Level Research (One Time Per Account)

**Start with the Account Brief.** If present, it's the baseline. Do NOT restate any of it in emails. It exists to make the angle precise.

**Catalog-grounded signal lookup (mandatory).** This is the primary research mode. Ground web search in the segment's signals catalog (`context/signals/[segment]-signals.md`), NOT generic "[company] news" queries. The catalog patterns enforce the signal taxonomy and prevent grabbing whatever press release looks shiny.

1. Open `context/signals/[segment]-signals.md` for the account's segment. Read Tier A signals first.
2. Run each Tier A signal's `Pattern:` field as a literal web search query, substituting `[company name]`. Examples (fiber):
   - F-A1: `"BEAD subgrant awarded" [Company] route miles`
   - F-A2: `[Company] ("definitive agreement" OR "to acquire" OR "completes acquisition") fiber`
   - F-A5: `[Company] ("named" OR "appointed") (VP OR Chief) (Network OR Wholesale OR Service Delivery)`
3. **Minimum 3 Tier A pattern searches.** If a HIGH-confidence Tier A hit lands, stop — that's the signal.
4. **No Tier A hits → expand to Tier B patterns** from the same catalog.
5. **Cross-check `recent_news_or_trigger_event` in HubSpot** for confirmation. This field is populated weekly by `weekly-signal-scan` and can be stale mid-week — web search wins where they disagree.
6. **Contact-level search:** `[Contact Name] [Company] LinkedIn` — role tenure, recent activity, what they own. NOT optional, even when company-level search found a signal.
7. **If web + HubSpot both come up empty across ≥5 query attempts:** mark Signal code = NONE, posture = ASKED, document the literal queries you ran.

**Signal Recency & Fact Validation (Research Quality gate — do this before any signal informs the angle):**

1. **Validate the Account Brief — don't trust it blind.** The brief is the baseline, not gospel. Confirm its core claims (segment, scale, ownership, product focus, footprint) against current web search. If the brief is older than ~30 days or research contradicts it, trust the fresh research and note the correction on the Receipt. A brief that has gone stale is a wrong-fact risk, not a shortcut.
2. **Only build on a RECENT signal — and use it as the reason to reach out now.** With no event to lean on, the signal carries the entire reason for the email. Check each signal's EVENT date (`last_signal_date` = when the news/funding/hire actually happened, not when it was detected). Freshness windows from `context/signals/signal-framework.md`:
   - **≤60 days → full-strength, time-bound reason to reach out.** A fresh signal is why this email lands now instead of any other week.
   - **60–90 days → usable but softer.** Frame as context, not "just announced."
   - **>90 days → STALE. Do NOT reference as current.** Re-verify with a fresh search or drop it and fall back to the segment's inferred-pain angle (posture = ASKED). Citing a >90-day event as if it's news is a wrong-fact failure.
   Longer-runway signals stay actionable past the raw window: exec hires (~90-day mandate), M&A (60–120d post-close), BEAD/grant builds (18–24mo ramp). A 50-day-old M&A is still hot; a 9-month-old "new hire" is not.
3. **Cross-check HubSpot `recent_news_or_trigger_event` against the live web.** This field is refreshed weekly and can be stale mid-week. Web search wins where they disagree. If HubSpot shows a signal the web can't confirm as still current, treat it as stale.
4. **No wrong facts.** Every fact that informs the angle must be verified against a dated primary source. Don't let dirty CRM data drive the angle — `infrastructure_profile` beats `annualrevenue` when they conflict (revenue data is wrong more often). If you can't verify a fact, don't build the angle on it. The fact never appears in the email anyway (research is invisible), but a wrong fact produces a wrong angle, and the recipient will catch it.

**For Active accounts** (Activity Status flagged): pull HubSpot call notes, email threads, meeting notes, deal status, task history. Use real history if it exists ("We've connected with a few folks at `[Company]`"). If activity is thin, don't force warmth.

**For "Active deal(s)" contacts:** review the deal carefully. May SKIP. May need to complement (not conflict with) the existing sales conversation. Flag for review if unclear.

**State the account angle in one sentence:** "`[Company]` is `[doing X]`, which means `[specific problem]`." The angle must come from research, not the segment template.

### Step 3: Per-Contact Email Writing

For each contact:

1. **Quick role check** (no extra research unless the title is unusual).
2. **Adapt the account angle to the role:**
   - C-level / VP Business → revenue, competitive positioning, market timing
   - CTO / VP Engineering → architecture, integration, operational overhead
   - VP Network / Network Ops → visibility, control, provisioning speed
   - Sales / Channel / Partnerships → ability to sell, speed to quote
   - Carrier Relations / Roaming → wholesale relationships, settlement, partner enablement
3. **Segment Lock.** Confirm the segment from research (override source if mismatch). Re-read `segment-language.md` for that segment's vocabulary if it's been more than 5 accounts since the last load. Use ONLY that segment's vocabulary.
4. **Posture decision (DIRECT or ASKED).** Match the move to what the research actually surfaced:
   - **DIRECT** = declarative problem statement. Use when a HIGH-confidence, FRESH (≤90d) Tier A cataloged signal exists AND the contact is a technical buyer (CTO / VP Engineering / VP Network).
   - **ASKED** = illumination question or premise hedge ("Probably already on your radar, but…"). Use when the angle is inferred (NONE in the Receipt) or the signal is stale, or the contact is a senior business buyer (CEO / CFO), or the pain is variable across the segment.
   - NOT randomized to a quota. Match the move to what you have.
5. **Emit a Research Receipt (HARD GATE).** Before writing any email body for this contact, emit a complete Receipt block. No Receipt = do not write. Format below.
6. **Write 3 emails** (framework below). **Posture rotates across the sequence:** if E1 is DIRECT, E2 is ASKED. E3 takes a detached or take-away close regardless. Three declarative pain statements in a row read as one writer pushing one angle three times.
7. **Write the LinkedIn message only if confirmed at run start.** LinkedIn posture should differ from E1.

### Research Receipt (Hard Gate Before Each Email Body)

Every email this run produces must be preceded by a Research Receipt above the email body — the SAME format used by `skills/cold-email/SKILL.md`, `skills/linkedin-outreach/SKILL.md`, and `skills/sdr-pipeline/SKILL.md`. An email without a Receipt is invalid output — restart that contact from research.

```
RESEARCH RECEIPT — [Contact First Last] @ [Company]

Segment: [segment / sub-segment]   Status: VERIFIED | CORRECTED from [X]
Catalog: context/signals/[segment]-signals.md

Searches run (literal query strings — not paraphrased):
1. `[exact query]` → [URL + date, OR "no Tier A hit"]
2. `[exact query]` → [URL + date, OR "no Tier A hit"]
3. `[exact query]` → [URL + date, OR "no Tier A hit"]
[min 3 if claiming a cataloged signal; min 5 if claiming NONE]

Company-level finding: [signal description with source quote + date, OR "NONE — no Tier A or Tier B hits across [N] searches"]
Contact-level finding: [what THIS contact owns / recent role activity / why they care about THIS facet. REQUIRED on every Receipt, including when the company finding is NONE.]
Brief validation: [VERIFIED against current research | CORRECTED: (what changed) | NO BRIEF]
Signal recency: [event date YYYY-MM-DD — FRESH ≤60d | AGING 60–90d | STALE >90d → re-verified or dropped | NONE]

Signal code: [F-A1 | NC-A2 | NO-B3 | NONE]
Posture: [DIRECT | ASKED] — [one-line reason tied to the finding above]

---

Subject: [subject line per Smartlead config]

[email body]
```

**Refuse-to-write rule:** if you cannot honestly fill all four sections (≥3 literal queries with results, Company-level finding, Contact-level finding, Posture with reason), output `RESEARCH INCOMPLETE: [reason]` in place of the email body, mark the contact `SKIPPED: Research incomplete`, and move on. Do NOT fabricate a Receipt. The Receipt is review metadata above the body — it does not get sent.

**Why each section enforces what it does:**
- Literal queries make faking research more expensive than running it.
- NONE costs more than success (5 queries vs 3) — inverts the path-of-least-resistance incentive.
- Contact-level finding is its own required line — forces the company+contact two-stage research to actually happen.
- Brief validation + Signal recency lines force a freshness/accuracy check before a stale fact ever reaches the angle.

### Step 4: QA Pass

Before appending:

- **Research Receipt present** above every email body — Searches Run (≥3 literal queries with results, ≥5 if NONE), Company-level finding, Contact-level finding, Brief validation, Signal recency, Posture with reason. NONE without ≥5 queries above it is research-skipping and fails this check.
- **Signal recency:** the angle leans only on a FRESH signal (event date ≤90 days, ideally ≤60), used as the reason to reach out now. No stale signals referenced as current. If the only signal is stale, the email runs on inferred-pain (posture = ASKED), not a dressed-up old headline.
- **Fact accuracy:** Account Brief validated against current research; angle-driving facts verified against dated sources; no wrong facts. `infrastructure_profile` beats `annualrevenue` on conflict.
- **Recipient's-eye read:** would they read past the first sentence? Does it sound like someone who knows their world?
- **Research invisibility:** no displayed company facts, stats, route miles, revenue, funding, project names, "I noticed."
- **Pressure-off:** peer suggesting a conversation, not a salesperson pushing a meeting.
- **Mechanical:** no em dashes, no banned phrases, no competitor/customer names, no credibility anchors, correct sender per Account Owner.
- **Value bridge** is 1 sentence max, embedded by contrast or standalone-but-punchy, "I" voice. Multi-sentence value bridge paragraphs BANNED. No brand-voice constructions ("We help operators…" / "We work with…").
- **Word count:** Email 1 70–85 words; Email 2 under 55; Email 3 2–3 sentences.
- **First name** before the email body.
- **Posture rotates across the sequence.** If E1 was DIRECT, E2 should be ASKED. E3 takes a detached or take-away close.
- **Hedge variety:** "I'd guess" / "I'd imagine" in ≤30% of E1s per batch of 10+. Mix in direct assertions, illumination questions, premise hedges, peer observations.
- **LinkedIn (if applicable):** 35–50 words / ≤280 chars, no sender intro in body, company-specific problem, soft CTA optional, Research Receipt above (same four-section format). LinkedIn posture differs from E1.
- **Sequence:** 3 distinct angle categories (revenue / competitive / operational / market timing / cost-of-inaction / peer social proof), CTAs rotated, reads like a real person coming back with new thoughts. Standalone test: would E2 still make sense with E1 removed?

### Step 5: Append Account to Output

Write all contacts for the account. Save.

### Step 6: Report and Continue

Briefly: account name, contact count, skips, warm angles available, segment corrections, stale-signal fallbacks used. Proceed immediately to the next account — do NOT wait for confirmation.

---

## Email Framework

### Email 1 (~70–85 words)

No event hook. The opener IS the relevance — lead with the angle that came from research. Done well, it should feel like a peer who knows their world reaching out, not a stranger.

1. **Relevance opener (1–2 sentences):** the company-specific problem or observation, written naturally. NOT "I noticed [fact]" (that PHRASE is banned), but a public-signal observation IS allowed and encouraged ("Saw the Q3 release notes mentioned…" / "Caught your panel at MetroConnect" / "Noticed the BEAD subgrant award post"). The observation must be FRESH (≤90d) — an old signal is not an opener. Research stays INVISIBLE except for the cited public signal.
2. **Value bridge (1 sentence MAX, embed-by-contrast preferred):** how MaiaEdge relates. Segment vocabulary only. "I" voice. No brand-voice constructions ("We help operators…" / "We built infrastructure that…" — BANNED). Multi-sentence value bridge paragraphs BANNED.
3. **CTA (1 sentence):** low-pressure, timing-flexible. Optional when an illumination question carries the close.

**Posture (DIRECT or ASKED):** decided in Step 3.4. DIRECT for HIGH-confidence, FRESH Tier A cataloged signals + technical buyers. ASKED otherwise.

**Default Email 1 CTA:** some version of "Hope to get a chance to connect when the timing works for you?"

### Email 2 (under 55 words)

No re-introduction. No "following up." No meta-references like "the other angle on this." Lead straight into a different dimension of the problem.

1. **New thought (2–3 sentences):** a different angle on the same underlying problem.
2. **CTA (1 sentence):** rotated, opens the door to a delegate.

**Default Email 2 CTA:** "Open to setting some time up? Happy to connect with somebody on your team first if that's preferred."

### Email 3 (2–3 sentences max)

No timing hook. No "show is coming up." Just a soft, pressure-off final touch — is this relevant, or wrong moment.

1. **Soft check-in (1–2 sentences):** is this relevant to what they have going on, or wrong moment.
2. **Soft close.** ONE CTA only. Never a conditional close plus a second close.

**CTA options (rotate for variance — pressure-off):**
- "Is this relevant to what you have going on?"
- "Better time for me to reach out?"
- "Worth a conversation, or wrong moment?"
- "Happy to circle back if the timing's off."
- "Door's open if this becomes useful."

### LinkedIn Message (Only If Confirmed at Run Start)

**Length:** target 35–50 words, max 280 chars (under LinkedIn's 300 hard limit). NOT a miniature email.

**Pattern:** `[First name], [observation/question with company-specific signal]. [Optional: one sentence of context]. [CTA or no CTA].` Embed-by-contrast preferred for the value bridge. NO standalone "We built carrier infrastructure that…" or "We help operators…" — brand-voice constructions BANNED. Use "I" voice or product-as-outcome framing if a value bridge is needed.

**No sender intro in the body.** The recipient already sees the sender from LinkedIn's UI. "Tim from MaiaEdge" in the body is redundant and triggers the sales-pitch reflex — banned.

**Soft CTAs (no event anchor):** "Worth connecting?" / "Open to a quick conversation?" / "Worth a few minutes?" — CTA OPTIONAL when a strong illumination question carries the close.

**Research Receipt** required above every LinkedIn message — same four-section format. NONE valid only with ≥5 literal queries.

**Open with the recipient's first name** followed by a comma, then directly into the observation/question.

**Avoid:** generic connect requests, compressed-email format, flattery, listing MaiaEdge features, more than one MaiaEdge sentence, brand-voice constructions, sender intro in body.

---

## LinkedIn Task Structure (If Confirmed at Run Start)

If LinkedIn tasks are enabled, create a HubSpot task on each contact (assigned to the Account Owner):

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

## Tone — Critical

**Diplomatic and pressure-off.** A peer suggesting a useful conversation, not a salesperson pushing a meeting. Zero pressure. CTA always optional.

**Research is INVISIBLE.** The single most important rule. Research makes the angle precise and the vocabulary correct. It NEVER appears as displayed facts, stats, or "I noticed." If a sentence could read as "I googled you," cut it.

**No fake familiarity.** This is cold — don't pretend otherwise. A direct cold approach beats forced familiarity.

**Short and manual-feeling.** Looks like someone typed it in Gmail. 2–3 tight paragraphs max. Fragments OK. One idea per email. First name before the body.

**Write as the Account Owner.** Use the sender from the source file (Account Owner column). Match their voice from `sender-profiles.md`.

---

## Hard Bans

- **No em dashes.** Use periods or commas.
- No "Hope this finds you well" / "Just wanted to reach out" / "I noticed" / "Revolutionary" / "Game-changing" / "Reason I'm reaching out."
- **No customer names.** Anonymize: "one fiber operator," not the actual name.
- **No competitor names.** "Third-party fabric" only where the segment fits — works for fiber operators and aggregators, NOT for Tier 1 network operators or carrier relations/roaming roles.
- **For colos:** don't lean on "lose revenue to third-party fabrics" — find research-based angles instead.
- **No credibility anchors** (no Acme Packet, no 128 Technology) in cold or LinkedIn.
- **No specific NNI/provisioning timelines** (60-day, 90-day) — varies by operator.
- **No "describing them back"** openers ("For a `[role]` at a `[type of company doing X]`…") — salesy and lecturing.
- **No sign-offs** — auto-appended by the platform.
- **No restating company facts** (revenue, facility counts, route miles, funding, project names).
- **Category descriptor:** "Carrier infrastructure" only (never IaaS, NaaS, platform).
- **Neocloud:** OPERATOR sovereignty banned. DATA sovereignty allowed. No network jargon.

---

## Segments

If the source has a Customer Segment, validate it against research and override if research shows otherwise.

For "Other" or any unclear segment: determine the best-fit MaiaEdge segment during account research. If on the exclusion list, SKIP.

**Enterprise (Multi-DC ICP):** `Enterprise-CustomerSegment` is an ICP segment. Evaluate against the four Enterprise sub-segments (`Financial Services`, `Healthcare Systems`, `Retail and Distribution`, `Outsourcing Services` — Enterprise) AND the hard scale gate ($1B+ revenue + 3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house net eng). Both gates pass → eligible for outreach via Enterprise lead-angle templates. Either gate fails → SKIP and route to R2 RE_ENRICH for re-classification to `Other`. Anchor account: Meijer.

### Exclusion List (SKIP and mark)

IXP, Tower REIT, IT MSP (helpdesk/break-fix), Retail ISP (no wholesale), Software vendor, Hyperscaler (AWS/Azure/GCP/Meta), Enterprise failing the scale or vertical gate (sub-$1B mid-market, single-DC, network outsourced to a single MSP, no direct carrier contracts, or Watch List verticals — Manufacturing / Energy-Utilities / Logistics / Government-Defense), Under 7 employees, Vendor/Contractor/Manufacturer, Consulting firm (Deloitte/McKinsey/BCG/Bain are project firms and excluded; Cognizant/Genpact/Concentrix/TaskUs with operational delivery centers ARE Outsourcing Services — Enterprise ICP), Trade organization, Defunct/Acquired.

---

## Active Contact Handling

For contacts with Activity Status flagged:

1. **Check HubSpot first.** Call notes, email threads, meeting notes, deal status, task history.
2. **Work the warm angle if real.** Reference it naturally if it exists.
3. **Active deal(s) contacts:** review the deal. May SKIP. May need to complement the existing sales conversation.

---

## Territory Model

| Territory | Owner | Coverage |
|-----------|-------|----------|
| East | Tim Lieto | AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV |
| West | Ken Cunningham | AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND, NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY |
| International | Tim Ziemer | All non-US |

The Account Owner column already has the correct sender. Use that value.

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
- [ ] Catalog-grounded web search (≥3 Tier A patterns; ≥5 queries if NONE)
- [ ] Every referenced signal's event date ≤90 days (ideally ≤60); no stale signals cited as current
- [ ] A fresh signal, where one exists, is used as the reason to reach out now; if the only signal is stale, the email runs on inferred-pain (ASKED)
- [ ] No wrong facts — angle-driving facts verified against dated sources; `infrastructure_profile` beats revenue on conflict
- [ ] HubSpot `recent_news_or_trigger_event` cross-checked against live web (web wins on conflict)
- [ ] Segment validated against research
- [ ] Company-specific angle stated in one sentence, from research not template
- [ ] Research Receipt emitted above every email and LinkedIn body

**Email Quality**
- [ ] Research is INVISIBLE
- [ ] Diplomatic, pressure-off tone
- [ ] Within word count (E1 70–85 / E2 <55 / E3 2–3 sentences)
- [ ] No em dashes, banned phrases, competitor/customer names, credibility anchors
- [ ] Value bridge 1 sentence, "I" voice, no brand-voice constructions
- [ ] CTA low-pressure; rotated across all 3 emails
- [ ] Each email a genuinely different angle; E2 doesn't reference E1
- [ ] Posture rotates across the sequence; hedge variety respected
- [ ] Correct sender per Account Owner

**LinkedIn Quality (where written)**
- [ ] 35–50 words / ≤280 chars; no sender intro in body
- [ ] Company-specific, fused into a problem statement
- [ ] Reads like a real connection request, not a compressed email
- [ ] Research Receipt above it

**Sequence Quality**
- [ ] 3 distinct angle categories across the sequence
- [ ] CTA phrasing rotated across all 3 emails
- [ ] Standalone test passes (E2 makes sense with E1 removed)

---

## End-of-Run Summary

After all accounts are processed, report:
- Total contacts processed / total in source file
- Total skipped (with reason breakdown)
- Total segment corrections
- LinkedIn messages written (if applicable)
- Stale-signal fallbacks used (signal found but >90d, ran on inferred-pain)
- Active accounts handled (warm angles used, deals flagged)
- Output file location
