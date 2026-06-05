# Apollo Weekly Budget Spec (shared by all Apollo-consuming routines)

**Effective 2026-05-06.** Replaces the prior 750-credit weekly hard cap (2026-05-03) with an **850-credit weekly hard cap** tracked across all routines via a single state file. The 100-credit increase funds R1 Fresh Enrichment's Path α expansion (sub-cap raised from 30/run to 50/run) so the redesigned 4-filter-group trigger query can drain its dynamic 100-150 record candidate pool without Apollo-budget starvation.

---

## Why this exists

Previous design (2026-05-03): each routine had its own per-run sub-cap with no real-time coordination. Sum at full daily/weekly draw was ~1,125 credits/week (R1 250 + R2 250 + R6 125 + Signal Scan 250 + R8 250). At 6,000 credits/month that left tiny headroom for ad-hoc work or surge weeks. The 2026-05-03 redesign introduced a 750-credit weekly hard cap with a single state file.

Cooper's directive (2026-05-06): bump weekly hard cap to **850 Apollo credits per ISO week** across ALL routines. At 6,000/month allocation that's ~3,650 credits/month from routines - still leaves ~2,350/month headroom for manual research, batch enrichment requests, and conference prep. The +100 credits/week buys R1 Fresh Enrichment 5 × 20-credit runs of additional Path α capacity, which is the throughput unlock the redesigned trigger query needs to converge the CRM toward "fully enriched and trustworthy" rather than churning the same 391 candidates daily.

---

## State file

**Path:** `weekly-reports/apollo-budget.json` (single rolling file, lives in maiaedge-ai repo `main` branch).

**Schema:**
```json
{
  "week_iso": "2026-W19",
  "week_start_et": "2026-05-04",
  "weekly_cap": 850,
  "consumed": 0,
  "by_routine": {
    "fresh-enrichment": 0,
    "stale-reenrichment": 0,
    "territory-hygiene": 0,
    "persona-fill": 0,
    "weekly-signal-scan": 0,
    "quarterly-job-changes": 0
  },
  "history": []
}
```

`history[]` entries:
```json
{
  "timestamp": "2026-05-04T15:23:11Z",
  "routine": "fresh-enrichment",
  "credits": 18,
  "consumed_after": 18,
  "run_id": "fresh-enrichment-2026-05-04"
}
```

---

## Per-routine sub-cap allocation (850/week budget - effective 2026-05-21)

| Routine | Cadence | Sub-cap (per run) | Weekly draw at full | % of 850 |
|---|---|---|---|---|
| Signal Scan | Mon | 250 | 250 | 29% |
| R1 Fresh Enrichment | M-F | 30 | 150 | 18% |
| R8 Persona Fill | Fri | 175 | 175 | 21% |
| R2 Stale Re-Enrichment | M-F | 50 | 250 | 29% |
| R6 Territory & Hygiene | M-F | 5 | 25 | 3% |
| **Steady-state weekly draw** |  |  | **850** | **100%** |
| R9 Quarterly Job Changes | Quarterly | spare-capacity | varies | n/a |

**Change history:**
- 2026-05-03: introduced 750/week cap with R1 sub-cap 30/run, R2 sub-cap 30/run.
- 2026-05-06: raised cap to 850/week, R1 sub-cap 30 → 50/run (R1 weekly draw 150 → 250) to support R1's redesigned 4-filter-group trigger query and three-path workflow. R1 Path α (full enrichment) is the only Apollo-consuming path; Path β (re-research) and Path γ (eviction) are Apollo-free.
- 2026-05-21: R1 sub-cap 50 → 30/run (frees 100 cr/wk; R1 daily peak was 22 on 2026-05-12, average 5-10/day, so 30/day stays 36% over peak). R2 sub-cap 30 → 50/run to consume R1's freed budget; supports 120-day rotation at 5,000 active records (~42 records/day FULL break-even; 50/day buys 67% headroom). Global weekly cap unchanged at 850; net Apollo impact zero.

R9 fires once per quarter - consumes whatever's available in the current week's spare capacity (typically 0-100 credits if other routines have run normally, up to 850 if it lands on a quiet week).

---

## Pre-flight check (every Apollo-consuming routine, every run)

At run start, BEFORE any Apollo call:

```python
import json, datetime, os
from pathlib import Path

BUDGET_PATH = "weekly-reports/apollo-budget.json"
WEEKLY_CAP = 850
ROUTINE_NAME = "stale-reenrichment"  # change per routine
ROUTINE_SUB_CAP = 50                  # change per routine (R1 = 30, R2 = 50, R6 = 5, R8 = 175, Signal Scan = 250) - updated 2026-05-21

# 1. Determine current ISO week
now_et = datetime.datetime.now(tz=ZoneInfo("America/New_York"))
iso_year, iso_week, _ = now_et.isocalendar()
current_week_iso = f"{iso_year}-W{iso_week:02d}"
current_monday = (now_et - datetime.timedelta(days=now_et.weekday())).date().isoformat()

# 2. Read tracker (or initialize)
if Path(BUDGET_PATH).exists():
    budget = json.loads(Path(BUDGET_PATH).read_text())
    if budget.get("week_iso") != current_week_iso:
        # New ISO week → reset
        budget = make_fresh_budget(current_week_iso, current_monday)
else:
    budget = make_fresh_budget(current_week_iso, current_monday)

# 3. Compute available
available = WEEKLY_CAP - budget["consumed"]

# 4. Decide
if available <= 0:
    log("Apollo weekly cap exhausted - skipping all Apollo for this run")
    apollo_budget_for_run = 0
else:
    apollo_budget_for_run = min(ROUTINE_SUB_CAP, available)
    if apollo_budget_for_run < ROUTINE_SUB_CAP:
        log(f"Apollo weekly cap tight - scaled from {ROUTINE_SUB_CAP} to {apollo_budget_for_run}")

# 5. Run routine with apollo_budget_for_run as the hard ceiling on Apollo calls
```

`make_fresh_budget()` initializer:
```python
def make_fresh_budget(week_iso, week_start_et):
    return {
        "week_iso": week_iso,
        "week_start_et": week_start_et,
        "weekly_cap": 850,
        "consumed": 0,
        "by_routine": {r: 0 for r in [
            "fresh-enrichment", "stale-reenrichment", "territory-hygiene",
            "persona-fill", "weekly-signal-scan", "quarterly-job-changes"
        ]},
        "history": []
    }
```

---

## Post-run update (every Apollo-consuming routine, every run)

After the routine completes (or aborts mid-run), update the tracker with ACTUAL credits consumed:

```python
# 1. Re-read budget (someone else may have run in the meantime - unlikely with staggered crons but defensive)
budget = json.loads(Path(BUDGET_PATH).read_text())

# 2. Append history entry
budget["consumed"] += actual_credits_used
budget["by_routine"][ROUTINE_NAME] += actual_credits_used
budget["history"].append({
    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "routine": ROUTINE_NAME,
    "credits": actual_credits_used,
    "consumed_after": budget["consumed"],
    "run_id": f"{ROUTINE_NAME}-{now_et.date().isoformat()}"
})

# 3. Trim history to last 14 days (keep file small)
cutoff = (now_et - datetime.timedelta(days=14)).isoformat() + "Z"
budget["history"] = [h for h in budget["history"] if h["timestamp"] >= cutoff]

# 4. Write + commit + push
Path(BUDGET_PATH).write_text(json.dumps(budget, indent=2))
subprocess.run(["git", "add", BUDGET_PATH])
subprocess.run(["git", "commit", "-m",
    f"apollo budget: {ROUTINE_NAME} +{actual_credits_used} consumed={budget['consumed']}/850 ({current_week_iso})"
])
subprocess.run(["git", "push"])
```

**Note (effective 2026-05-06):** R1 Fresh Enrichment downgraded the git commit/push to **best-effort** with a 10s timeout. If `.git/index.lock` is held by a concurrent routine OR git exits non-zero, R1 logs `Git commit deferred (concurrent routine); JSON updated locally` in its Slack DM and continues - the local JSON write is the source of truth, the next routine that successfully commits sweeps the deferred update into git history. Other routines may follow the same pattern at their authors' discretion. The Slack DM is the audit trail of record for Apollo consumption.

---

## Cooper run report inclusion (mandatory)

Every routine's run report MUST include an Apollo Budget line:

```
*Apollo budget:* [routine_used] credits this run · [weekly_consumed]/850 weekly · [available] remaining for week
```

If budget exhausted mid-run:
```
*Apollo budget:* WEEKLY CAP HIT - Apollo calls skipped after [N] credits. [Defer / hold detail]. Next reset: Monday [next_monday_et].
```

---

## Edge cases

- **File missing** → initialize fresh, log to run report.
- **File corrupted / malformed JSON** → reset to empty, log warning to run report and Cooper-only Slack DM.
- **Concurrent writes** (two routines running in same minute - should not happen given staggered crons but defensive): last writer wins. Drift acceptable.
- **Mid-week cap change** (e.g., Cooper raises cap to 1,000 mid-Wednesday): edit `weekly_cap` in the file directly, no routine code change needed.
- **Apollo monthly cap separately enforced** by `apollo_users_api_profile` pre-flight: still applies as the global ceiling. If monthly is depleted, weekly tracker becomes irrelevant - all routines defer Apollo regardless.

---

## Routines that consume Apollo (must implement this spec)

| Routine | Platform | File path |
|---|---|---|
| R1 Fresh Enrichment | Cowork | `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` |
| R2 Stale Re-Enrichment | Cowork | `cowork-scheduled-tasks/r2-stale-reenrichment/prompt.md` |
| R6 Territory & Hygiene | Claude Code | `routines/claude-code/r6-territory-hygiene/prompt.md` |
| R8 Persona Fill | Claude Code | `routines/claude-code/r8-persona-fill/prompt.md` |
| R9 Quarterly Job Changes | Claude Code | `routines/claude-code/r9-quarterly-job-changes/prompt.md` |
| Signal Scan: Colo | Cowork | `cowork-scheduled-tasks/signal-scan-colo/prompt.md` |
| Signal Scan: Fiber | Cowork | `cowork-scheduled-tasks/signal-scan-fiber/prompt.md` |
| Signal Scan: NeoCloud | Cowork | `cowork-scheduled-tasks/signal-scan-neocloud/prompt.md` |
| Signal Scan: Network Op | Cowork | `cowork-scheduled-tasks/signal-scan-networkop/prompt.md` |
| Signal Scan: MSP/Aggregator | Cowork | `cowork-scheduled-tasks/signal-scan-msp/prompt.md` |
| Signal Scan: Enterprise | Cowork | `cowork-scheduled-tasks/signal-scan-enterprise/prompt.md` |
| Signal Scan: Aggregator (Apollo budget 0) | Cowork | `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md` |

Routines that do NOT consume Apollo and are out of scope: R0 Import Validator, R3 Duplicate Accounts, R4 Flagged Consolidation, R5 Contact Dedup, Daily Sales Activity Brief (renamed from Daily Call Recap 2026-05-05), Weekly Market News, R-Tier-Audit (daily M-F 3pm CT HubSpot-only compute, added 2026-05-14; cadence: monthly → weekly 2026-05-14 → daily M-F 2026-05-21 per Cooper), D7 Edge Case Resolution (weekly web_fetch + web_search only, added 2026-05-14).
