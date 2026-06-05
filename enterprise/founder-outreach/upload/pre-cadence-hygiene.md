# Pre-Cadence List Hygiene

**Status:** Mandatory pre-cadence gate alongside `persona-targeting-blocklist.md` for every Smartlead batch and every batch LinkedIn cadence.
**Source:** Deep Messaging Audit (2026-05-11) §7. Confirmed in Cross-Audit Decisions Sidecar §7.
**Owner:** Cooper (RevOps) - gate is enforced at the SDR pipeline stage before list export.

---

## Why this exists

11 of 34 replies in the 60-day Smartlead window were auto-OOO, address-change, autoresponder, unsubscribe-bot, "I retired," or sender-bounce. **That's 32% of all replies on no-content signal.** These are not content failures, but they consume cadence slots that should belong to real prospects. Removing them does not lift raw reply count, but it lifts **signal density** - every auto-OOO suppressed is a slot freed for a contact who can actually buy.

Expected impact: ~10-15% relative lift on reply-rate as a metric (raw reply count holds, denominator drops by ~5-8% as bounce/OOO contacts are removed before the second touch).

---

## Three filters

### Filter 1 - Auto-bounce / autoresponder detection

**What it does:** If an email address triggers an autoresponder, address-change reply, or unsubscribe-bot reply on the first send, suppress that lead from E2 and E3.

**Triggers to detect:**
- "This mailbox is no longer monitored, please contact [new address]" - Terranet address-change pattern
- Unsubscribe-bot replies (e.g., Truvista's automated unsubscribe handler)
- "I am no longer with [Company], please reach out to [name]"
- Standard SMTP soft-bounce followed by autoresponder body
- Out-of-office that is permanent (no return date)

**Action on detection:**
1. Suppress from E2 and E3 in the current cadence.
2. Surface in a Cooper-review queue with the autoresponder text excerpted.
3. If address-change is provided, log the suggested new contact for re-research (don't auto-add to a campaign - research the role first).
4. If the unsubscribe is real, add the domain to the global block list per Smartlead `add_domain_block_list`.

**Estimated savings:** ~50-80 wasted sends per 60-day window across all senders.

---

### Filter 2 - OOO detection at send-time

**What it does:** If a contact's most recent inbound from any source within 14 days indicates an active OOO, delay the cadence until after the OOO window.

**Triggers to detect:**
- Active "Out of office" / "Currently traveling" / "On parental leave" / "Returning [date]" in the contact's recent inbound replies
- Calendar status feed (when available) showing the contact is on declared leave
- LinkedIn status banner showing "Currently on leave" or similar

**Action on detection:**
1. Pause the cadence for that contact only.
2. Resume the cadence the calendar day after the stated return date (e.g., "Back Mon May 19" → resume sends Tue May 20).
3. If no return date is stated, hold for 10 business days and re-check.

**Anchor evidence:** Damian @ Exatel auto-OOO'd twice in the 60-day corpus. The framing was correct; the sends were just badly timed. A pre-send OOO check would have held both touches for a real conversation window.

---

### Filter 3 - LinkedIn-status check on lead pull

**What it does:** At list-pull time, verify the contact's current LinkedIn role matches the source list's role. Flag for re-research before sending if they differ.

**Triggers to detect:**
- Title change on LinkedIn vs source list (e.g., source says "VP Network Engineering," LinkedIn says "Retired" or "Open to work")
- Company change (contact has moved to a new company since the list was built)
- "Retired" / "Consulting" / "Advising multiple companies" - explicit retirement signals
- Tenure shorter than 90 days at the listed company (likely role is still being defined; outreach is mistimed)

**Action on detection:**
1. Flag the contact in the SDR pipeline queue with the LinkedIn-vs-source delta.
2. Block the cadence until Cooper or the rep clears the flag.
3. If retired or moved companies, archive the contact in HubSpot (per CRM hygiene routines) and remove from the cadence permanently.

**Anchor evidence:** Dave Furiness @ MCNC is retired but was still in the prospect list. Sending him a cold email surfaced him as a stale lead - costly because retiree replies are usually hostile and damage sender reputation.

---

## What this hygiene layer does NOT cover

- **Spam-trap / known-bad-email-pattern detection** is handled by Smartlead deliverability tooling and the company-enrichment skill. This file is about role and engagement-state hygiene, not technical deliverability.
- **Domain warm-up state:** Smartlead's own warm-up controls handle this. This file does not gate by sender domain heat.
- **Engagement-quality scoring** (was the contact opened-but-no-reply across 2+ campaigns?) is downstream of this hygiene layer and lives in pipeline-analytics, not here.

---

## Implementation - where these filters run

1. **At list pull (Apollo / ZoomInfo / saved search):**
   - Filter 3 runs synchronously. LinkedIn role check happens before the contact lands in the SDR queue.
2. **At Smartlead campaign export (pre-launch):**
   - Filter 1 - historical bounce/autoresponder check against the prior 90 days of sender activity.
3. **Between E1 and E2 (continuously, during the cadence):**
   - Filter 1 - autoresponder detection on the E1 send.
   - Filter 2 - OOO detection on any inbound during the gap.
4. **The persona-targeting blocklist** (`context/outreach/persona-targeting-blocklist.md`) runs alongside these filters at the same stage. Both must pass for a contact to enter Smartlead.

---

## Decision history

- **2026-05-11:** Hygiene filters specified from Deep Messaging Audit §7. Cross-Audit Decisions Sidecar §7 confirmed scope and ordering.
