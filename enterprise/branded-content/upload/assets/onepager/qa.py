# -*- coding: utf-8 -*-
"""
Auto-ship QA gate for the outbound one-pager. Run this on a content JSON BEFORE render.py.
It fails closed: any FAIL means the brief is not safe to ship unchecked. This is what replaces
a human eyeballing every brief at volume.

    python3 qa.py content.<account>.json

Checks:
  1.  Leak / internal-voice phrases            (FAIL)  pre-meeting brief, ahead of our conversation, founder names, etc.
  1b. Segment call-out in masthead eyebrow     (FAIL)  the top stays account-only
  2.  Announcing section headlines             (FAIL)  headers STATE the point, never narrate the move
  3.  Em / en dashes                           (FAIL)  none allowed; ranges use hyphens
  4.  Ungrounded numbers (stat strip + body)   (VERIFY) flagged as an assumption to confirm; does NOT block
  4b. Currency / percent signs in body         (VERIFY) flagged to confirm; does NOT block
  5.  Structure complete (3 stats/plays/pillars, all slots)  (FAIL)
  6.  Word caps exceeded (the one-page guarantee)            (FAIL)
  7.  Asserted current-state flaws             (WARN)  heuristic; reframe forward-state
  8.  Absolute / superlative claims            (VERIFY) verify defensible or soften
  9.  Claims about the account's business      (VERIFY) comparative/superlative claims to confirm vs research

Verifiability is the point: a brief may state only what is verified. Numbers are enforced mechanically here;
non-numeric claims about the account or market are the writer's responsibility (research them, don't assert).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
FACTS = HERE / "facts.md"

MIDDOT = "\u00b7"
EM_DASH = "\u2014"
EN_DASH = "\u2013"

LEAK_PHRASES = [
    "pre-meeting brief", "pre meeting brief", "opportunity brief", "ahead of our conversation",
    "ahead of any conversation", "built from the outside", "not a pitch", "working session",
    "clear view of fit", "in either direction", "the right room", "no deck", "no pitch",
    "we expect the call", "we hope to", "sharpen these", "sharpen or correct", "read these as",
    "co-founder", "cofounder", "tim ziemer", "abilash", "the goal is a clear view",
]

ANNOUNCE_HEADERS = [
    "structural truth", "why it matters", "where we fit", "where maiaedge fits", "the thesis",
    "the ask", "market context", "next step", "the conversation", "the opportunity",
    "three plays", "use cases", "the capability", "where it touches", "the overlap", "the read",
]

SEGMENT_WORDS = ["sovereign", "neocloud", "colocation", "fiber", "network operator", "msp",
                 "aggregator", "enterprise", "gpu cloud", "carrier infrastructure"]

CURRENT_STATE_FLAGS = [
    "today that means", "still rides", "you cannot see", "you can't see", "you cannot prove",
    "you can't prove", "nobody can show", "no hop-by-hop answer", "you have no visibility",
    "best-effort internet", "best effort internet", "you don't have", "you do not have",
]

ABSOLUTES = ["the only", "the first", "the best", "no one", "nobody", "guaranteed",
             "unmatched", " never ", " always ", "100%", "everyone"]

CLAIM_FLAGS = ["few clouds", "more than any", "as much as", "leading", "largest", "biggest",
               "first to", "pioneer", "one of the few", "unlike most", "ahead of the", "the only cloud"]

CAPS = {  # word caps (the one-page guarantee)
    "account_eyebrow": 6, "masthead_sub": 22,
    "hook.headline": 8, "hook.body": 62, "whynow.headline": 8, "whynow.body": 67,
    "plays_headline": 8, "product.headline": 10, "product.body": 57, "cta.body": 34,
    "play.cell": 34, "pillar.desc": 17, "stat.label": 13,
}

issues = []
def fail(m): issues.append(("FAIL", m))
def warn(m): issues.append(("WARN", m))
def wc(s): return len(str(s).split())


def approved_blob():
    """Approved numbers/tokens live between the QA-APPROVED-STAT-TOKENS markers in facts.md.
    Fall back to the whole file if the fence is missing."""
    if not FACTS.exists():
        return ""
    txt = FACTS.read_text(encoding="utf-8")
    m = re.search(r"QA-APPROVED-STAT-TOKENS(.*?)QA-APPROVED-STAT-TOKENS-END", txt, re.DOTALL)
    return (m.group(1) if m else txt).lower()


def body_fields(c):
    out = [c.get("masthead_sub", ""),
           c.get("hook", {}).get("headline", ""), c.get("hook", {}).get("body", ""),
           c.get("whynow", {}).get("headline", ""), c.get("whynow", {}).get("body", ""),
           c.get("plays_headline", ""),
           c.get("product", {}).get("headline", ""), c.get("product", {}).get("body", ""),
           c.get("cta", {}).get("lead", ""), c.get("cta", {}).get("body", "")]
    for p in c.get("plays", []):
        out += [p.get("play", ""), p.get("looks", ""), p.get("pays", "")]
    for p in c.get("pillars", []):
        out += [p.get("desc", "")]
    for s in c.get("stats", []):
        out += [s.get("label", "")]
    return out


def main():
    if len(sys.argv) < 2:
        print("usage: python3 qa.py content.<account>.json"); sys.exit(2)
    c = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    approved = approved_blob()
    blob = " \n ".join(body_fields(c) + [c.get("account_eyebrow", "")]).lower()

    # 1. leak phrases
    for p in LEAK_PHRASES:
        if p in blob:
            fail("leak/internal-voice phrase present: '%s'" % p)

    # 1b. segment call-out in masthead eyebrow (keep it account-only)
    eb = c.get("account_eyebrow", "").lower()
    if "&middot;" in eb or MIDDOT in eb:
        fail("segment call-out in masthead eyebrow: drop the separator + descriptor, keep it account-only (e.g. 'FOR NSCALE')")
    for w in SEGMENT_WORDS:
        if w in eb:
            fail("segment call-out in masthead eyebrow: '%s' (keep the top account-only)" % w)
    if "carrier infrastructure" in c.get("product", {}).get("headline", "").lower():
        warn("product header is a category self-claim; prefer a neutral safe label like 'What MaiaEdge is'")

    # 2. announcing headlines
    headers = [c.get("hook", {}).get("headline", ""), c.get("whynow", {}).get("headline", ""),
               c.get("plays_headline", ""), c.get("product", {}).get("headline", ""),
               c.get("title_line1", "") + " " + c.get("title_accent", "")]
    for h in headers:
        for a in ANNOUNCE_HEADERS:
            if a in h.lower():
                fail("announcing header (state the point, don't label the move): '%s' contains '%s'" % (h.strip(), a))

    # 3. dashes
    for t in body_fields(c):
        if EM_DASH in t or EN_DASH in t or " -- " in t:
            fail("em/en dash present (use hyphens): '%s...'" % t[:60])

    # 4. every number must be grounded in the approved fence (stat strip + body prose)
    for s in c.get("stats", []):
        tok = str(s.get("num", "")).strip().lower()
        if tok and tok not in approved:
            warn("VERIFY: stat '%s' is not pre-approved in facts.md - confirm it is true before sending (or add it to the fence)" % s.get("num"))
    for t in body_fields(c):
        for n in re.findall(r"\d[\d,]*", t):
            if n not in approved:
                warn("VERIFY: number '%s' in \"%s...\" is not pre-approved - confirm against research before sending" % (n, t[:50]))
    # 4b. currency / percent never improvised in body
    for t in body_fields(c):
        if "$" in t or "%" in t:
            warn("VERIFY: a figure ($ or %%) appears in \"%s...\" - confirm it is researched, or route it through facts.md" % t[:50])

    # 5. structure
    for key, n in (("stats", 3), ("plays", 3), ("pillars", 3)):
        if len(c.get(key, [])) != n:
            fail("structure: expected %d %s, got %d" % (n, key, len(c.get(key, []))))
    for slot in ["account_eyebrow", "title_line1", "title_accent", "masthead_sub", "hook",
                 "whynow", "plays_headline", "product", "cta"]:
        if slot not in c:
            fail("structure: missing slot '%s'" % slot)

    # 6. word caps
    def cap(path, val):
        if path in CAPS and wc(val) > CAPS[path]:
            fail("over word cap: %s = %d words (max %d)" % (path, wc(val), CAPS[path]))
    cap("account_eyebrow", c.get("account_eyebrow", ""))
    cap("masthead_sub", c.get("masthead_sub", ""))
    cap("hook.headline", c.get("hook", {}).get("headline", ""))
    cap("hook.body", c.get("hook", {}).get("body", ""))
    cap("whynow.headline", c.get("whynow", {}).get("headline", ""))
    cap("whynow.body", c.get("whynow", {}).get("body", ""))
    cap("plays_headline", c.get("plays_headline", ""))
    cap("product.headline", c.get("product", {}).get("headline", ""))
    cap("product.body", c.get("product", {}).get("body", ""))
    cap("cta.body", c.get("cta", {}).get("body", ""))
    for s in c.get("stats", []):
        cap("stat.label", s.get("label", ""))
    for p in c.get("plays", []):
        for k in ("play", "looks", "pays"):
            if wc(p.get(k, "")) > CAPS["play.cell"]:
                fail("over word cap: play '%s' %s = %d words (max %d)" % (p.get("play", "?")[:20], k, wc(p.get(k, "")), CAPS["play.cell"]))
    for p in c.get("pillars", []):
        if wc(p.get("desc", "")) > CAPS["pillar.desc"]:
            fail("over word cap: pillar '%s' desc = %d words (max %d)" % (p.get("name", "?"), wc(p.get("desc", "")), CAPS["pillar.desc"]))

    # 7. current-state flaw heuristic (warn)
    for f in CURRENT_STATE_FLAGS:
        if f in blob:
            warn("possible asserted current-state flaw (reframe forward-state): '%s'" % f)
    # 8. absolutes / superlatives (warn - verify defensible)
    for a in ABSOLUTES:
        if a in blob:
            warn("absolute/superlative claim (verify it is true + defensible, or soften): '%s'" % a.strip())
    # 9. claims about the account business (verify against research)
    for cl in CLAIM_FLAGS:
        if cl in blob:
            warn("VERIFY: claim about the account ('%s') - back it with research or soften; do not assert from outside the business" % cl.strip())

    fails = [m for lvl, m in issues if lvl == "FAIL"]
    warns = [m for lvl, m in issues if lvl == "WARN"]
    print("=" * 64)
    print("ONE-PAGER QA  -  " + Path(sys.argv[1]).name)
    print("=" * 64)
    if not fails and not warns:
        print("PASS  -  clean. Safe to render and ship.")
    else:
        if fails:
            print("MUST FIX (blocks - brand / voice / format):")
            for m in fails: print("  x   " + m)
        if warns:
            print("VERIFY BEFORE SEND (assumptions - does NOT block; you confirm + guide):")
            for m in warns: print("  ?   " + m)
        print("-" * 64)
        print("%d must-fix, %d to-verify" % (len(fails), len(warns)))
        print("RESULT:", "BLOCKED until must-fix cleared" if fails else "OK to render - review the verify list, then you guide it")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
