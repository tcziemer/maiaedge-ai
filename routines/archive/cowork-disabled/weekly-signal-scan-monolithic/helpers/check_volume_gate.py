#!/usr/bin/env python3
"""
Volume-per-rep gate. Pass = each rep's final pool >= 25 OR carryover_pool documented as exhausted.

Usage:
    python3 check_volume_gate.py <scored.json>

Input file format (scored.json):
{
  "run_date": "YYYY-MM-DD",
  "scored": [
    {"owner": "lieto"|"cunningham"|"ziemer", "score": int, ...},
    ...
  ],
  "carryover_pool_meta": {
    "lieto":      {"pool_size": int, "exhausted": bool},
    "cunningham": {"pool_size": int, "exhausted": bool},
    "ziemer":     {"pool_size": int, "exhausted": bool}
  }
}

Decision logic per rep:
    - pool >= 25                  -> pass (action: post)
    - pool < 25, carryover_exhausted -> pass with YELLOW tag (action: post_with_yellow_tag)
    - pool < 25, NOT exhausted    -> FAIL (action: hold_dm_post_under_coverage_alert)

Output (stdout): JSON pass/fail report.

Exit codes: 0 always (the runtime decides what to do based on the report).
"""
import sys
import json
from collections import defaultdict

if len(sys.argv) != 2:
    sys.stderr.write("Usage: check_volume_gate.py <scored.json>\n")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        d = json.load(f)
except (OSError, IOError, json.JSONDecodeError) as e:
    sys.stderr.write(f"Cannot read {sys.argv[1]}: {e}\n")
    sys.exit(1)

FLOOR = 25
scored = d.get("scored", [])
carryover_meta = d.get("carryover_pool_meta", {})

report = {
    "floor": FLOOR,
    "per_rep": {},
    "overall_pass": True,
    "holds": [],
}

counts = defaultdict(int)
for r in scored:
    counts[r["owner"]] += 1

for rep in ("lieto", "cunningham", "ziemer"):
    pool = counts.get(rep, 0)
    co_meta = carryover_meta.get(rep, {})
    co_pool_size = co_meta.get("pool_size", 0)
    co_exhausted = co_meta.get("exhausted", False)

    if pool >= FLOOR:
        rep_pass, action = True, "post"
    elif co_exhausted:
        rep_pass, action = True, "post_with_yellow_tag"
    else:
        rep_pass, action = False, "hold_dm_post_under_coverage_alert"
        report["holds"].append(rep)
        report["overall_pass"] = False

    report["per_rep"][rep] = {
        "pool_size": pool,
        "carryover_pool_size": co_pool_size,
        "carryover_exhausted": co_exhausted,
        "pass": rep_pass,
        "action": action,
    }

print(json.dumps(report, indent=2))
