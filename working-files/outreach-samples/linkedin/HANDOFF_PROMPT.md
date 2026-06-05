# LinkedIn Outreach Handoff — ITW 2026

## What You're Doing

Create LinkedIn connection messages for 225 high-leverage contacts across 3 sender files. Each message is derived from the Email 1 that was already written for that contact — you're condensing the angle into ≤300 characters (punctuation and spaces count).

## Input Files

### LinkedIn Target Lists (who to write for)
These are in `/mnt/ITW/final contact lists/cold contacts/emails processed/final smartlead imports/linkedin targets/`:

| File | Sender | Contacts |
|------|--------|----------|
| `Tim_Lieto_LinkedIn_Targets.csv` | Tim Lieto | 75 |
| `Ken_Cunningham_LinkedIn_Targets.csv` | Ken Cunningham | 75 |
| `Timothy_Ziemer_LinkedIn_Targets.csv` | Timothy Ziemer | 75 |

Columns: `First Name, Last Name, Title, Company, Email, LinkedIn, Score, Tier`

### Processed Outreach Files (source of Email 1)
These are in `/mnt/ITW/final contact lists/cold contacts/emails processed/`:

- `ITW_2026_Colocation_Outreach.xlsx`
- `ITW_2026_Fiber_Operator_Outreach.xlsx`
- `ITW_2026_MSP_Aggregator_Outreach.xlsx`
- `ITW_2026_Neocloud_Outreach.xlsx`
- `ITW_2026_Network_Operator_Outreach.xlsx`
- `ITW_2026_Unknown_Segment_Outreach.xlsx`
- `itwwarmlist_v2.xlsx`

Columns: `First Name, Last Name, Title, Company, Email, Subject, Email 1, Email 2, Email 3`

**Match contacts from the LinkedIn target CSVs to the outreach files by email address** to pull their Email 1 content.

## Output File

One XLSX file per sender, saved to the `linkedin targets` folder:

| Column | Source |
|--------|--------|
| First Name | From LinkedIn target CSV |
| Last Name | From LinkedIn target CSV |
| Title | From LinkedIn target CSV |
| Company | From LinkedIn target CSV |
| LinkedIn URL | From LinkedIn target CSV (LinkedIn column) |
| HubSpot Contact Link | Look up each contact by email in HubSpot via MCP, build link as `https://app.hubspot.com/contacts/PORTALID/contact/CONTACTID` |
| Connection Message | NEW — condensed from Email 1, ≤300 characters |

Output filenames:
- `Tim_Lieto_LinkedIn_Outreach.xlsx`
- `Ken_Cunningham_LinkedIn_Outreach.xlsx`
- `Timothy_Ziemer_LinkedIn_Outreach.xlsx`

## How to Write the Connection Messages

### The Core Rule
Each contact already has an Email 1 in the outreach files. That email contains:
1. An ITW hook (opening reference to the show)
2. A company-specific angle/problem
3. A value bridge to MaiaEdge
4. An event-anchored CTA

Your job is to **distill the angle from Email 1 into ≤300 characters**. The LinkedIn message should carry the same angle and tone — just compressed. Do NOT write a generic message. Do NOT lose the company-specific detail that makes Email 1 work.

### What to Keep from Email 1
- The company-specific problem/angle (this is the core — never lose this)
- The ITW connection (shared event context)
- Peer tone (not salesy)

### What to Cut from Email 1
- The greeting (Hi Name, is handled by LinkedIn)
- The value bridge / MaiaEdge explanation
- The detailed CTA (LinkedIn connection IS the ask)
- Any proof points or anonymized references

### Structure (≤300 characters)
1. ITW reference + company-specific problem in 1-2 sentences
2. Soft ask: "connecting ahead of ITW" or "worth a conversation at the show?"

### Character Counting
- 300 characters HARD LIMIT. Count every character including spaces and punctuation.
- Aim for 250-290 to leave breathing room
- If over 300, cut words, don't compress meaning

### Voice Rules (inherited from email)
- No em dashes. Ever.
- No "I noticed" / "I saw that" / flattery / congratulations
- No competitor names, no customer names, no credibility anchors
- No "revolutionary" / "game-changing" / marketing speak
- Write like a peer, not a salesperson
- "I'd guess" and "I'd imagine" are fine for inferences
- Short sentences. Fragments OK.

### Example Transformation

**Email 1 (full):**
> Hi Kurt,
>
> I saw Summit Broadband on the ITW attendance list. With the expansion into enterprise and wholesale across Florida, I'd imagine provisioning speed is the bottleneck between signing deals and actually recognizing revenue. We help fiber operators close that gap. Your team provisions circuits in minutes instead of weeks. Open to connecting at ITW?

**LinkedIn message (≤300 chars):**
> Heading to ITW and saw Summit Broadband on the list. With the Florida expansion, I'd guess provisioning speed is the gap between signed deals and revenue. Worth a conversation at the show?

(That's 189 characters — well under 300, carries the same angle.)

## HubSpot Lookups

Use the HubSpot MCP to search for each contact by email address. Extract the contact ID and build the link. If a contact is not found in HubSpot, leave the HubSpot link column blank.

The HubSpot portal ID can be found from any successful contact lookup — it's in the URL pattern.

## Processing Approach

Process in batches of 10-15 contacts at a time:
1. Read 10-15 contacts from the LinkedIn target CSV
2. Match each to their Email 1 from the outreach files (by email address)
3. Look up each in HubSpot (batch if possible)
4. Write the ≤300 char connection message based on Email 1's angle
5. Append to the output file
6. Repeat

Save after every batch. Report progress.

## Skills to Read Before Writing

Read the `linkedin-outreach` skill FIRST — it has the 300-character philosophy, angle selection rules, and format requirements. Also read `segment-language.md` from the maiaedge-ai repo for insider vocabulary.

## Quality Checks (Every Message)

- [ ] ≤300 characters (count them)
- [ ] Carries the same company-specific angle as Email 1
- [ ] ITW reference present
- [ ] No em dashes
- [ ] No banned phrases
- [ ] No competitor/customer names
- [ ] Tone matches Email 1 (peer, not salesperson)
- [ ] Would make sense as a LinkedIn connection request from the assigned sender
