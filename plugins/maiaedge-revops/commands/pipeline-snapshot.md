---
description: Analyze deal pipeline health, velocity, and forecast
argument-hint: "[snapshot | velocity | forecast | stuck | win-loss | rep-performance]"
---

Analyze the MaiaEdge deal pipeline.

Arguments provided: $ARGUMENTS

Invoke the pipeline-analytics skill. If a specific mode is provided, run that analysis. If no mode specified, run a pipeline snapshot.

Modes:
- `snapshot` — Current pipeline value by stage, segment breakdown, projected close this quarter
- `velocity` — Average days in each stage, conversion rates stage-to-stage, bottleneck identification
- `forecast` — Three scenarios: best case, weighted, commit. Based on stage probability and deal age.
- `stuck` — Deals exceeding 2x average time in current stage. Ranked by value.
- `win-loss` — Win rate by segment, average deal size, common loss reasons
- `rep-performance` — Side-by-side comparison of rep metrics (pipeline value, velocity, win rate)
