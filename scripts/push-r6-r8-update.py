"""Build update bodies for R6 and R8 triggers from the updated spec files.

The trigger inlines the full spec content. We assemble a wrapper that matches
the trigger's existing structure (`message.role: user`, the same allowed_tools
and mcp_connections — those are auto-preserved by the partial update API as
long as we send job_config.ccr.events with the new content)."""

import json

R6_PATH = r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\Claude routine prompts\crm-guardian-routine-6-territory-hygiene.md"
R8_PATH = r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\Claude routine prompts\crm-guardian-routine-8-weekly-persona-fill.md"

with open(R6_PATH, "r", encoding="utf-8") as f:
    r6_content = f.read()
with open(R8_PATH, "r", encoding="utf-8") as f:
    r8_content = f.read()

# Sanity: confirm the no-git policy actually landed
for label, content in [("R6", r6_content), ("R8", r8_content)]:
    must_have = [
        "Step 0",
        "early-checkpoint",
        "monthly_consumed",
        "NO `git pull`",
    ] if label == "R6" else [
        "0. **Preflight",
        "early-checkpoint",
        "monthly_consumed",
        "NO `git pull`",
    ]
    # Patterns that indicate stale INSTRUCTIONS to use git/tracker (not "NO ..." prohibitions)
    must_not_have = [
        "via Bash + git pull",
        "Pre-flight: read tracker file",
        "Post-run: update `weekly-reports/apollo-budget.json` per the spec",
        "750/week global cap",
        "available = 750",
    ]
    for needle in must_have:
        assert needle in content, f"{label}: missing required string: {needle!r}"
    for needle in must_not_have:
        assert needle not in content, f"{label}: still contains stale instruction: {needle!r}"
    print(f"{label}: OK ({len(content)} chars)")

R6_ENV = "env_018AmYCxSHNPrHk4q3ofk9hm"  # from earlier RemoteTrigger.get
R8_ENV = R6_ENV  # same env for both
SOURCES = [{"git_repository": {"url": "https://github.com/Cooperfkennedy/maiaedge-ai"}}]


def build_body(content: str, env_id: str, allowed_tools: list[str]) -> dict:
    return {
        "job_config": {
            "ccr": {
                "environment_id": env_id,
                "events": [
                    {
                        "data": {
                            "message": {"content": content, "role": "user"},
                            "type": "user",
                        }
                    }
                ],
                "session_context": {
                    "allowed_tools": allowed_tools,
                    "model": "claude-opus-4-7[1m]",
                    "sources": SOURCES,
                },
            }
        }
    }

# R6 allowed_tools per the prior get response
R6_TOOLS = ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch"]
R8_TOOLS = R6_TOOLS  # mirror

r6_body = build_body(r6_content, R6_ENV, R6_TOOLS)
r8_body = build_body(r8_content, R8_ENV, R8_TOOLS)

with open(r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r6-update-body-v2.json", "w", encoding="utf-8") as f:
    json.dump(r6_body, f, ensure_ascii=False)
with open(r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r8-update-body-v2.json", "w", encoding="utf-8") as f:
    json.dump(r8_body, f, ensure_ascii=False)

print(f"R6 body: {len(json.dumps(r6_body))} bytes")
print(f"R8 body: {len(json.dumps(r8_body))} bytes")
