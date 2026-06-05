# Cold List Outreach — Processing Instructions

These instructions govern how to process a cold contact list into send-ready outreach. No event anchor — relevance comes entirely from research. Same account-by-account motion as tradeshow runs, but the work is harder because there's no shared moment to lean on.

---

## Per-Run Variables (Lock in Before Starting)

Confirm these at the start of every run:

1. **Source file path and sheet name**
2. **Output file name** (default: `[ListName]_Written.xlsx`)
3. **Subject line(s)** — varies per run, lock in here. Configured in Smartlead, not stored in the output file.
4. **LinkedIn messages: yes or no?** — ASK before the run starts. If yes, every contact gets a LinkedIn message in addition to the 3 emails. If no, leave the LinkedIn column blank.
5. **Create HubSpot LinkedIn tasks: yes or no?** — ASK before the run starts (only relevant if LinkedIn messages are enabled). If yes, create a HubSpot task on each contact for the rep to send the LinkedIn message. See "LinkedIn Task Structure" below.

---

## Source File

**Required columns (minimum):** First Name, Last Name, Title, Email, Account, Account Owner

**Optional, used if present:** Domain, Customer Segment, Account Brief, Activity Status

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
| 8 | LinkedIn Message | Target 35-50 words / max 280 chars (under LinkedIn's 300 hard limit). NO sender intro in body. Research Receipt above (see skills/cold-email/SKILL.md and skills/linkedin-outreach/SKILL.md for the four-section format). Only if confirmed at run start, otherwise blank. |

**Build method:** Create with headers on first account batch, then append each account's contacts as they are processed and QA'd. Save after every account.

**Skipped contacts:** include row with First Name through Account populated. Put skip reason in Email 1 (e.g., `SKIPPED: Active deal`). Leave other columns blank.

---

## Processing Model: Account-by-Account

Group contacts by Account. All contacts at the same account share one round of account-level research. Each contact then gets a per-contact pass to flex the angle to their role. The batch unit is the ACCOUNT.

### Step 0: Pre-Read Reference Files

Before writing, read from the maiaedge-ai repo:

1. `segment-language.md` — insider vocabulary per segment
2. `Email-Writing-Rules.md` — core philosophy, angle-first, banned phrases
3. `fallback-messaging.md` — segment-specific fallback hooks
4. `sender-profiles.md` — Tim Lieto, Ken Cunningham, Tim Ziemer voice profiles
5. Relevant segment cheatsheet (`colocation.md`, `fiber-operator.md`, `neocloud.md`, `network-operator.md`, `msp-aggregator.md`)

### Step 1: Load the Account

Pull all contacts for the next account. Identify count, titles, segment, owner, whether an Account Brief exists, whether any contact has Activity Status flagged.

### Step 2: Account-Level Research (One Time Per Account)

**Start with the Account Brief.** If present, it's the baseline. Do NOT restate any of it in emails. It exists to make the angle precise.

**Layer in 2-3 web searches:** recent news, expansions, partnerships, hiring, funding, route launches, facility announcements. Find what's TIMELY for this account — that's the angle. Without an event anchor, the relevance MUST come from this research.

**For Active accounts** (Activity Status flagged): pull HubSpot call notes, email threads, meeting notes, deal status, task history. Use real history if it exists ("We've connected with a few folks at [Company]"). If activity is thin, don't force warmth.

**For "Active deal(s)" contacts:** review the deal carefully. May SKIP. May need to complement (not conflict with) the existing sales conversation. Flag for review if unclear.

**State the angle in one sentence:** "[Company] is [doing X], which means [specific problem]." The angle must come from research, not from the segment template.

### Step 3: Per-Contact Email Writing

For each contact:

1. Quick role check (no extra research unless title is unusual)
2. Adapt the account angle to the role:
   - C-level / VP Business → revenue, competitive positioning, market timing
   - CTO / VP Engineering → architecture, integration, operational overhead
   - VP Network / Network Ops → visibility, control, provisioning speed
   - Sales / Channel / Partnerships → ability to sell, speed to quote
   - Carrier Relations / Roaming → wholesale relationships, settlement, partner enablement
3. Write 3 emails (framework below)
4. Write LinkedIn message **only if confirmed at run start**

### Step 4: QA Pass

Before appending:

- **Recipient's-eye read:** would they read past the first sentence? Does it sound like someone who knows their world?
- **Research invisibility:** no displayed company facts, stats, route miles, revenue, funding, project names, "I noticed"
- **Pressure-off:** peer suggesting a conversation, not salesperson pushing a meeting
- **Mechanical:** no em dashes, no banned phrases, no competitor/customer names, no credibility anchors, correct sender per Account Owner
- **Word count:** Email 1 ~70-85 words; Email 2 under 55; Email 3 short
- **First name** before email body
- **LinkedIn (if applicable):** Target 35-50 words / max 280 chars (under LinkedIn's 300 hard limit), NO sender intro in body, company-specific problem, soft CTA optional, Research Receipt above (see skills/cold-email/SKILL.md and skills/linkedin-outreach/SKILL.md for the four-section format)
- **Sequence:** 3 distinct angles, CTAs rotated, reads like a real person coming back with new thoughts

### Step 5: Append Account to Output

Write all contacts for the account. Save.

### Step 6: Report and Continue

Briefly: account name, contact count, skips, warm angles available, segment corrections. Proceed immediately to next account — do NOT wait for confirmation.

---

## Email Framework

### Email 1 (~70-85 words)

No event hook. The opener IS the relevance — lead with the angle that came from research. Done well, it should feel like a peer who knows their world reaching out, not a stranger.

1. **Relevance opener (1-2 sentences):** the company-specific problem or observation, written naturally. NOT "I noticed [fact]" (that PHRASE is banned), but a public-signal observation IS allowed and encouraged ("Saw the Q3 release notes mentioned…" / "Caught your panel at MetroConnect" / "Noticed the BEAD subgrant award post"). Research stays INVISIBLE except for the cited public signal.
2. **Value bridge (1 sentence MAX, embed-by-contrast preferred):** how MaiaEdge relates. Segment vocabulary only. Preferably embed as a contrast clause inside the problem paragraph ("the fix is…" / "the version that works is…"). Standalone allowed only as a 1-sentence "I" voice line. NO brand-voice constructions ("We help operators…" / "We built infrastructure that…" — BANNED). Multi-sentence value bridge paragraphs BANNED.
3. **CTA (1 sentence):** low-pressure, timing-flexible. Optional when an illumination question carries the close.

**Posture (DIRECT or ASKED):** Match to signal strength. Cataloged Tier A signal → DIRECT. Inferred angle → ASKED.

**Research Receipt** required above the email body — four sections: Searches Run (≥3 literal queries paired with results, ≥5 if NONE), Company-level finding, Contact-level finding, Posture with reason. See `context/outreach/email-writing-rules.md` for the canonical Receipt format.

**CTA:** Some version of "Hope to get a chance to connect when the timing works for you?"

### Email 2 (under 55 words)

No re-introduction. No "following up." No meta-references like "the other angle on this." Lead straight into a different dimension of the problem.

1. **New thought (2-3 sentences):** different angle on the same underlying problem.
2. **CTA (1 sentence):** rotated, opens the door to a delegate.

**CTA:** "Open to setting some time up? Happy to connect with somebody on your team first if that's preferred."

### Email 3 (2-3 sentences max)

No timing hook. No "show is coming up." Just a soft, pressure-off final touch — is this relevant, or wrong moment.

1. **Soft check-in (1-2 sentences):** is this relevant to what they have going on, or wrong moment.
2. **Soft close.** ONE CTA only. Never conditional close + a second close.

**CTA options (rotate for variance — pressure-off):**
- "Is this relevant to what you have going on?"
- "Better time for me to reach out?"
- "Worth a conversation, or wrong moment?"
- "Happy to circle back if the timing's off."
- "Door's open if this becomes useful."

### LinkedIn Message (Only If Confirmed at Run Start)

**Length:** Target 35-50 words, max 280 characters (under LinkedIn's 300 hard limit). NOT a miniature email.

**Pattern:** `[Recipient first name], [observation/question with company-specific signal]. [Optional: one sentence of context]. [CTA or no CTA].` Embed-by-contrast preferred for the value bridge (woven into the problem paragraph as a contrast clause). NO standalone "We built carrier infrastructure that…" or "We help operators…" — those brand-voice constructions are BANNED. Use "I" voice or product-as-outcome framing if a value bridge is needed.

**NO sender intro in body.** Recipient sees who sent the connection request from LinkedIn's UI. "Tim from MaiaEdge." / "Ken from MaiaEdge." in the message body is BANNED — it's redundant and triggers the sales-pitch reflex before the recipient reads the actual message.

**Research Receipt** required above the LinkedIn message — same four-section format as the email Receipt (Searches Run with literal queries, Company-level finding, Contact-level finding, Posture). NONE only valid with ≥5 literal queries above it. See `skills/linkedin-outreach/SKILL.md`.

**Soft CTAs (no event anchor):**
- "Worth connecting?"
- "Open to a quick conversation?"
- "Worth a few minutes?"

CTA OPTIONAL when a strong illumination question carries the close.

**Open with the recipient's first name** followed by a comma, then directly into the observation/question.

**Avoid:** generic connect requests, compressed-email format, flattery, listing MaiaEdge features, more than one MaiaEdge sentence, brand-voice constructions ("We help…" / "Most operators…"), sender intro in body.

---

## LinkedIn Task Structure (If Confirmed at Run Start)

If LinkedIn tasks are enabled, create a HubSpot task on each contact assigned to the Account Owner. Task structure:

- **Task type:** LinkedIn (or "To-Do" if LinkedIn type unavailable)
- **Title:** `Send LinkedIn message — [Contact First Name] [Last Name]`
- **Due date:** Same day as Email 1 send, or per the rep's preference
- **Body format (CRITICAL):**

```
[LinkedIn profile URL]

[LinkedIn message body]
```

The URL goes on its own line at the top. Then a blank line. Then the message. This lets the rep click the URL to open the profile, then copy/paste the message below it. No labels ("URL:", "Message:"), no extra text — just the link, blank line, message.

If a contact's LinkedIn URL is not in the source file or HubSpot, leave the URL line blank but still create the task with the message body so the rep can find the profile manually.

---

## Tone — Critical

**Diplomatic and pressure-off.** Peer suggesting a useful conversation, not salesperson pushing a meeting. Zero pressure. CTA always optional.

**Research is INVISIBLE.** The single most important rule. Research exists to make the angle precise and the vocabulary correct. It NEVER appears as displayed facts, stats, or "I noticed" observations. If a sentence could be interpreted as "I googled you," cut it.

**No fake familiarity.** This is cold — don't pretend otherwise. A direct cold approach beats forced familiarity.

**Short and manual-feeling.** Looks like someone typed it in Gmail. 2-3 paragraphs max with tight spacing. Fragments OK. One idea per email. First name before the body.

**Write as the Account Owner.** Use the sender from the source file. Match voice from `sender-profiles.md`.

---

## Hard Bans

- **No em dashes.** Use periods or commas.
- No "Hope this finds you well" / "Just wanted to reach out" / "I noticed" / "Revolutionary" / "Game-changing" / "Reason I'm reaching out"
- **No customer names.** Anonymize: "one fiber operator" not the actual name.
- **No competitor names.** "Third-party fabric" only when the segment fits — works for fiber operators and aggregators, NOT for Tier 1 network operators or carrier relations/roaming roles.
- **For colos:** don't lean on "lose revenue to third-party fabrics" — find research-based angles instead.
- **No credibility anchors** (no Acme Packet, no 128 Technology) in cold or LinkedIn.
- **No specific NNI/provisioning timelines** (60-day, 90-day) — varies by operator.
- **No "describing them back"** openers like "For a [role] at a [type of company doing X]..." — sounds salesy and lectures the reader.
- **No sign-offs** (auto-appended by platform).
- **No restating company facts** (revenue, facility counts, route miles, funding, project names).
- **Category descriptor:** "Carrier infrastructure" only (never IaaS, NaaS, platform).
- **Neocloud:** OPERATOR sovereignty banned, DATA sovereignty allowed, no network jargon.

---

## Segments

If source has Customer Segment, validate against research. Override if research shows otherwise.

For "Enterprise" or "Other": determine best-fit MaiaEdge segment during account research. If genuinely enterprise-only (internal network, no wholesale) or on the exclusion list, SKIP.

### Exclusion List (SKIP and mark)

IXP, Tower REIT, IT MSP (helpdesk/break-fix), Retail ISP (no wholesale), Software vendor, Hyperscaler (AWS/Azure/GCP/Meta), Enterprise (internal-only network), Under 7 employees, Vendor/Contractor/Manufacturer, Consulting firm, Trade organization, Defunct/Acquired.

---

## Active Contact Handling

For contacts with Activity Status flagged:

1. **Check HubSpot first.** Call notes, email threads, meeting notes, deal status, task history.
2. **Work the warm angle if real.** Reference it naturally if it exists.
3. **Active deal(s) contacts:** review the deal. May SKIP. May need to complement existing sales conversation.

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
| Speed | "One fiber operator went from 60-90 day provisioning to under 10 minutes." |
| Sovereignty | "A colo operator told us with third-party fabrics, 'you turn the customer over to them.' With MaiaEdge, they control their destiny." |
| Simplicity | "One operator called it 'fabric in a box. Drop it in, add water, it works.'" |
| Scale | "Deployed across 800+ cell towers and 20+ data centers for a network operator." |
| Federation | "A fiber operator in the Pacific uses federation to extend to the mainland." |
| Multi-carrier | "We're working with an aggregator that uses MaiaEdge to unify visibility across all upstream carrier partners." |

---

## End-of-Run Summary

After all accounts processed, report:
- Total contacts processed / total in source
- Total skipped (with reason breakdown)
- Total segment corrections
- LinkedIn messages written (if applicable)
- Active accounts handled (warm angles used, deals flagged)
- Output file location
