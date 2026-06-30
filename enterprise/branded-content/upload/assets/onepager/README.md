# Outbound One-Pager (self-contained)

Everything needed to generate a MaiaEdge outbound account one-pager lives in THIS folder. It is the
post-engagement asset (rides a LinkedIn-accept thank-you DM or an email reply, never cold). The brief
makes the case; the follow-up email carries the meeting ask.

## Files
| File | Role |
|---|---|
| `render.py` | Renders a content JSON to ONE single-page branded PDF (Tomorrow embedded, gold/black, compact masthead). Structure is locked; personalization lives in the JSON slots. |
| `qa.py` | Pre-flight gate. Run BEFORE render. Blocks brand/voice/format problems; flags unverified numbers + claims as "VERIFY BEFORE SEND" notes (these do NOT block). |
| `facts.md` | Approved-numbers fence + credibility rules. RevOps-owned. Every number the gate auto-approves lives here. |
| `content-schema.md` | How to fill the content JSON: slots, word caps, voice rules, the headers-state-not-announce rule. Read before filling. |
| `content.example.json` | Worked example (Nscale). Copy per account. |
| `content.GMI.json` | Second worked example (GMI Cloud). |
| `fonts/` | Tomorrow weights, embedded in the PDF (vendored here so the folder is portable). |
| `logos/` | MaiaEdge logo (vendored). |
| `requirements.txt` | Python dependency. |

## Requirements
- Python 3.9+
- WeasyPrint: `pip install -r requirements.txt` (or `pip install weasyprint`). WeasyPrint needs system
  libraries pango + cairo + gdk-pixbuf (macOS: `brew install pango`; Debian/Ubuntu: `apt-get install
  libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0`). Standard library only otherwise.

## Run (per account)
```
# 1. copy the example and fill every slot from research (see content-schema.md)
cp content.example.json content.<account>.json

# 2. gate it  -  fix MUST-FIX items; review the VERIFY-BEFORE-SEND assumptions and confirm them
python3 qa.py content.<account>.json

# 3. render the single-page PDF (writes the file named in the JSON's out_pdf)
python3 render.py content.<account>.json
```

## Where the angle comes from
The best angle is research-driven. `content-schema.md` has a context router mapping each decision (segment, persona pains, why-now trigger, plays, proof) to the canonical `context/` files in this repo. Read those before filling a brief.

## How the gate treats claims (important)
The gate is intentionally easy on the front-end user. It **blocks** only objective brand/voice/format
problems (internal-voice leaks, em dashes, a segment call-out in the eyebrow, announcing headers, missing
slots, over-length). It does **not** block on facts: any number or comparative claim about the account is
surfaced as a "VERIFY BEFORE SEND" note so you confirm it against research before it reaches a prospect.
The rule is simple: do not make a big claim about the customer's business from the outside without verified
research. The gate flags the assumption; you guide it from there.
