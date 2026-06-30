# MaiaEdge SDR Pipeline - Changelog

## What's In This Folder

```
final finshed workflow/
├── SKILL.md                              ← NEW: Consolidated 8-step SDR pipeline skill
├── CHANGELOG.md                          ← This file
├── references/
│   ├── messaging-framework.md            ← NEW: Segment messaging, personas, tone, proof points
│   ├── email-writing-rules.md            ← NEW: Consolidated email rules reference
│   └── hubspot-values.md                 ← NEW: Exact HubSpot property value mappings
├── evals/
│   └── evals.json                        ← 3 test cases for validation
├── eval-results/                         ← Test outputs from all 3 evals
│   ├── eval_review.html                  ← Side-by-side quality review
│   ├── eval-1-flexential-h5/             ← Batch colo test
│   ├── eval-2-acquired-companies/        ← Exclusion handling test
│   └── eval-3-radiusdc/                  ← Named contacts test
└── updated-skills/                       ← UPDATED copies of existing plugin skills
    ├── maiaedge-outreach/
    │   ├── cold-email/SKILL.md           ← Updated
    │   ├── linkedin-outreach/SKILL.md    ← Updated
    │   ├── prospect-research/SKILL.md    ← Updated
    │   └── segment-classification/SKILL.md ← Updated
    └── maiaedge-sales/
        └── cold-outreach/SKILL.md        ← Updated
```

---

## Updated Skills - What Changed

### maiaedge-outreach / cold-email

| Change | Why |
|---|---|
| Added competitor name ban to "Never" list | Eval 1 (Flexential) email named Megaport and Equinix directly. Rule was implied but not explicit. |
| Added "No competitor names" to quality checklist | Enforcement mechanism for the ban |
| Added "ENFORCE THE FLOOR" to word count section | Eval 3 (RadiusDC) emails came in at 68 and 74 words vs 100-150 target. Now explicit: must hit minimum, add company-specific detail if short. |

### maiaedge-outreach / linkedin-outreach

| Change | Why |
|---|---|
| Changed "[Sender], MaiaEdge." to "[Sender] from MaiaEdge." in all templates | Eval 3 LinkedIn messages said "Tim, MaiaEdge." which reads as addressing Tim, not introducing Tim as the sender. |
| Added em dash scan instruction | Eval 3 Joseph's LinkedIn had an em dash. Rule existed in emails but wasn't explicit for LinkedIn. |
| Added "No competitor names" rule | Colo template referenced Megaport by name. Changed to "third-party." |
| Updated all 6 segment starter templates to "from MaiaEdge" format | Consistency with the format fix |

### maiaedge-outreach / prospect-research

| Change | Why |
|---|---|
| Expanded Step 0 to "HubSpot Deep Pull" with full property list | Original only said "review segment classification." New version pulls account_brief, recent_news, segment, sub_segment, activity, sequences, lead_status — everything the pipeline needs. |
| Added Step 0.5: Activity Gate (MANDATORY) with explicit thresholds | Original had no activity gate. Pipeline testing showed this is critical — prevents tone-deaf outreach to contacts in active conversations. |
| Added territory check instruction | Original had no territory awareness. Pipeline caught this in eval 3 (Denver CO = Ken's territory, Tim sending). |
| Added data source tagging ([HS], [Apollo], [Web], [User], [Missing]) | Original didn't tag sources. Pipeline needs to know where data came from for trust/verification. |
| Added segment verification, activity gate, and data source fields to research summary template | Research output now includes verification status, not just classification. |

### maiaedge-outreach / segment-classification

| Change | Why |
|---|---|
| Added "Post-Research Segment Verification (MANDATORY)" section | Original only classified. It never verified after research. Eval showed a company could be misclassified (e.g., standard colo with strong AI signals should be AI colo). Now explicit: verify after research, flag mismatches. |

### maiaedge-sales / cold-outreach

| Change | Why |
|---|---|
| Added "Pre-Write Checks (MANDATORY)" section with Activity Gate, Territory Check, Data Source Tagging | Original had zero pre-write safety checks. No activity awareness, no territory flagging, no source tracking. These are the 3 biggest pipeline improvements. |
| Strengthened competitor name ban | Changed from "No mention of specific NaaS competitors" to explicit "NEVER write Megaport or Equinix or Lumen." |
| Updated LinkedIn section with "from MaiaEdge" format, em dash scan, credibility anchor requirement | Original LinkedIn section was bare (4 lines). Now matches the detail level of the standalone linkedin-outreach skill. |
| Added 4 new quality checklist items | Activity gate passed, territory flagged, segment verified, LinkedIn format correct. |

---

## Skills NOT Changed (No Updates Needed)

These skills are separate workflows that the consolidated pipeline doesn't replace. They don't need the above fixes because they serve different purposes:

- **maiaedge-revops/contact-discovery** — Finds contacts at accounts. Separate from outreach writing.
- **maiaedge-revops/crm-hygiene** — CRM data quality auditing. Operational task.
- **maiaedge-revops/pipeline-analytics** — Deal pipeline analysis. Post-outreach.
- **maiaedge-revops/territory-manager** — Territory validation. Already has territory model.
- **maiaedge-enrichment-pipeline/** (all 4 skills) — Pre-pipeline enrichment. Different workflow.
- **maiaedge-events/event-intelligence** — Conference workflows. Different use case.
- **maiaedge-sales/account-research** — Strategic account briefs. Different depth.
- **maiaedge-sales/call-prep** — Discovery prep. Post-email.
- **maiaedge-sales/competitive-intel** — Competitive positioning reference.
- **maiaedge-sales/sales-enablement** — Marketing materials creation.
- **maiaedge-sales/segment-classification** — Duplicate of outreach version (already updated there).
- **maiaedge-sales-docs** — Order forms, MSAs. Post-deal.
- **maiaedge-account-brief** — Strategic account briefs. Different skill.
