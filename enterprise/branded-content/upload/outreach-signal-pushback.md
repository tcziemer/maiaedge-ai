# Outreach Signal Push-Back to HubSpot

The single canonical procedure for writing a freshly-discovered signal back to HubSpot at outreach time. Referenced by `cold-email`, `linkedin-outreach`, `sdr-pipeline`, `account-brief`, and `prospect-research`. Each skill carries a one-line pointer to this file plus any skill-specific delta (see the sdr-pipeline batch note at the end).

## Inviolable rule

This step runs AFTER the primary output (the drafted email, LinkedIn DM, or brief) has been delivered to the rep. It must never gate, delay, or alter the primary output. If anything here fails, the rep already has what they need; signal-engine staleness is a routine-recovery problem, not a rep-blocker. Skip silently on any failure. The next R-Tier-Audit run reconciles the signal fields.

## When to write back

During your outreach research (the company-level and contact-level lookups) you ran web search and optionally web fetch. If that research surfaced a **signal-grade event** (funding round, exec hire, M&A, facility/market launch, public outage / RCA, earnings-language shift, or any U1-U6 / AP / FR class in [`signal-framework.md`](./signal-framework.md)), score it against the Signal Scan rubric (Tier × Freshness × Confidence). **Only events scoring ≥8 trigger the push-back.** Sub-8 noise stays silent. When more than one event qualifies, pick the single highest-scored event ≥8.

## Comparison gate (write only if fresher)

Read current `last_signal_date` for this company via `mcp__claude_ai_HubSpot__get_crm_objects`. If your discovered **event date** is strictly newer than HubSpot's value (or HubSpot's value is null), proceed. Otherwise no write: Signal Scan or a more recent push-back already has equal-or-fresher data. Idempotent no-op.

## The write block

One `mcp__claude_ai_HubSpot__manage_crm_objects` call with `updateRequest.objects[]`, `objectType: "companies"`, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`. Fields:

- `recent_news_or_trigger_event` — pure narrative, no date prefix. Format: `"[Signal Type] - [one-line summary]"`. 2-4 sentences, ≤250 char hard cap.
- `last_signal_date` — the **event date** (YYYY-MM-DD) extracted from the source article: when the event actually happened, NOT today's run date. If the body doesn't state it, use the article publication date as a ±few-day approximation.
- `last_signal_score` — your rubric score (number, typically 0-60).
- `signal_count_last_30d` — read current value. If current `last_signal_date` is within 30d of your new event date, increment by 1. If current is null or >30d old, write 1.
- `signal_heat` — recompute per `compute_signal_heat` below. **Title Case enum:** `Hot` / `Warm` / `Cool` / `Cold`. Lowercase is silently rejected.
- `account_tier` — recompute per [`tier-compute-spec.md`](../account-tiering/tier-compute-spec.md) §4. **Only write if `hs_is_target_account != true`** (the flag freezes tier; heat continues regardless).

## `compute_signal_heat` (canonical: tier-compute-spec.md §11.5)

```
signal_heat is computed top-down, first match wins:

Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
       OR signal_count_last_30d >= 2
       OR account has any associated open deal past `appointmentscheduled`

Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

Inputs: last_signal_score, last_signal_date (event date), signal_count_last_30d, open-deal state.
Output: enum Hot | Warm | Cool | Cold (Title Case per HubSpot).
hs_is_target_account = true does NOT freeze signal_heat. Tier is rep-locked; heat always reports the truth.
```

Heat writes are idempotent: skip if `computed_heat == current_heat`.

## Stamping policy

**Do NOT bump `last_enriched_date`.** Outreach-time signal push-backs are partial writes, not full enrichment passes. R2's 120-day rotation owns the freshness guarantee.

## Audit log

Add a HubSpot company note alongside the field writes:

```
Signal push-back from [skill name] on YYYY-MM-DD: discovered <signal type> event YYYY-MM-DD, score <N>. Heat <prior> -> <new>. Tier <prior> -> <new>.
```

(Title Case heat values in the note.)

## Failure handling

If any MCP call fails: log to the run report under "Signal push-back deferred" and continue. The rep already has their output. R-Tier-Audit reconciles next run. **Never surface push-back failures as a blocker.**

## sdr-pipeline batch specifics

`sdr-pipeline` runs this **per-company at the end of each company's processing loop** (not end-of-batch), so each company's research is freshest and the comparison gate isn't re-reading HubSpot twice. Batch rate-limiting: loop ≤10 writes per `manage_crm_objects` call (HubSpot MCP cap), 250ms minimum between batches, exponential backoff (1s → 2s → 4s) on HTTP 429. Surface in the run summary: push-backs fired (N), skipped-idempotent (N), deferred-failure (N, reconciled by R-Tier-Audit next run).
