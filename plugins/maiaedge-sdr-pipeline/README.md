# MaiaEdge SDR Pipeline Plugin

End-to-end batch outreach pipeline. Takes a list of companies + contact titles and produces send-ready 3-email sequences + LinkedIn messages with Smartlead-ready import files.

## When to Use This vs. maiaedge-outreach

| Use Case | Plugin |
|----------|--------|
| "Write me an email to Sarah at Flexential" | **maiaedge-outreach** (one-off) |
| "Here's 10 companies, build full sequences for Smartlead" | **maiaedge-sdr-pipeline** (batch) |
| "Quick LinkedIn message for this CTO" | **maiaedge-outreach** (one-off) |
| "Process this list into a Smartlead import" | **maiaedge-sdr-pipeline** (batch) |

## Pipeline Steps

1. **HubSpot Deep Pull** — Account briefs, contacts, activity, segment
2. **Activity Gate** — Check for active conversations (mandatory)
3. **Account Brief Review** — Read existing research
4. **Web Research** — Verify + supplement with current intel
5. **Apollo Enrichment** — Fill email/phone gaps
6. **Segment Verification** — Confirm segment matches reality
7. **Email Writing** — 3-email sequence + LinkedIn per contact
8. **Quality Check** — Automated checklist per contact
9. **Output** — Smartlead import XLSX + review XLSX

## Skills

- `sdr-pipeline` — The full pipeline skill

## References

- `email-writing-rules.md` — Tone, structure, banned phrases, CTAs
- `messaging-framework.md` — Segment-specific messaging and persona mapping
- `hubspot-values.md` — HubSpot property values for segments

## Commands

- `/run-pipeline` — Run the full pipeline on a list of companies + contacts

## Evals

Test cases and results in `evals/` and `eval-results/`.
