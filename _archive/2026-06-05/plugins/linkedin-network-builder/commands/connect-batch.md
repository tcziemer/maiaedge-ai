---
description: Send LinkedIn connection requests from an existing target list, then enrich and push to HubSpot
allowed-tools: Read, Write, Bash, TodoWrite
argument-hint: "[target-list-file]"
---

Standalone connection sender. Use this to send connections from a previously generated target list without re-sourcing companies from HubSpot.

After sending connections, enriches each contact via Apollo and pushes to HubSpot (same as Step 5 of `/build-targets`).

Read the `icp-networking` skill for the full connection protocol, enrichment flow, and rate limiting rules.

## Inputs

- **Target list file:** $1 (path to XLSX, or most recent `linkedin-results-*.xlsx` / `enrichment-candidates-*.xlsx` in workspace)

## Pre-Flight

1. **Confirm LinkedIn is open.** Check Chrome tabs for LinkedIn. If not found, navigate to linkedin.com and confirm Cooper is logged in.
2. **Read the target list.** Required columns: First Name, Last Name, Company, LinkedIn URL. Title, Segment, HubSpot Company ID optional but preferred.
3. **Filter processed rows.** If Status column exists, skip "Sent", "Already Connected", "Pending".
4. **Confirm with Cooper.** Show count: "Ready to send [N] connection requests?"

## Connection Loop

For each target:

1. Navigate directly to LinkedIn profile URL
2. Wait 2-3 seconds for page load
3. `find` the "Connect" button
4. Click Connect ref. If modal, `find` "Send without a note", click it.
5. If "More" dropdown: click More, find Connect, click, then Send without a note
6. If already connected/pending/follow-only: skip, log status
7. Wait 4-5 seconds before next

**Stop conditions:** Weekly limit -> STOP. CAPTCHA -> STOP, alert Cooper. Chrome issue -> pause, alert.

Log each: name, company, title, LinkedIn URL, status.

## Post-Connection: Apollo Enrichment

For each contact with status "Sent":

1. `apollo_people_match` with LinkedIn URL. Keep email only if `email_status = "verified"`.
2. `apollo_contacts_create` with `run_dedupe: true`.
3. Apollo-HubSpot sync handles contact creation in HubSpot automatically.

If Apollo fails for a contact, log error and continue.

## Output

Save `linkedin-results-{date}.xlsx` with columns:
| # | First Name | Last Name | Title | Company | Segment | LinkedIn URL | Connection Status | Email | Email Status | Apollo Status |

Summary: X sent, X skipped, X errors. X with verified email, X without.

## Notes

- Max 20 connections per session. If list has more than 20 unprocessed rows, process first 20 only.
- This does NOT source companies or flag misclassifications. For the full workflow, use `/build-targets`.
