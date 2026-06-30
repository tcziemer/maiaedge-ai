# MSA — Detailed Specifications

Read this file when generating Master Subscription Agreements.

## Template

The template is `msa_template.docx` — a proper Word document with 11 numbered sections plus Exhibits A and B.

## Process

1. Load template: Copy `msa_template.docx` to working directory
2. Find and replace the three variable fields (see below)
3. Save as `[CustomerShortName]_MSA_[EffectiveDate].docx`
4. Convert to PDF: `libreoffice --headless --convert-to pdf [filename].docx`

## Variable Fields

There are only **3 variable fields** in the entire MSA. Everything else is fixed legal text.

| Variable | Pattern to Find | Replace With | Example |
|----------|----------------|--------------|---------|
| Effective Date | `______` after "dated as of" in the opening paragraph | Full date | "February 15, 2026" |
| Customer Legal Name | `_________________________` after "and" in the opening paragraph | Full legal entity name | "IENTC Telecom, S.A. de C.V." |
| Customer Address | `___________________________________` after "with offices at" | Full address | "Av. Insurgentes Sur 1602, Mexico City" |

The customer name also appears in the signature block at the bottom — search and replace there too.

## Content-Based Search Approach

Use python-docx to find paragraphs by content rather than by index:

```python
from docx import Document

doc = Document("msa_template.docx")

for para in doc.paragraphs:
    # Opening paragraph with all three blanks
    if "dated as of" in para.text and "______" in para.text:
        # Replace date blank
        for run in para.runs:
            if "______" in run.text and "dated" not in run.text:
                run.text = run.text.replace("______", effective_date, 1)
                break

    # Customer name blank (longer underscore pattern)
    if "_________________________" in para.text:
        for run in para.runs:
            if "_________________________" in run.text:
                run.text = run.text.replace("_________________________", customer_name, 1)

    # Customer address blank (longest underscore pattern)
    if "___________________________________" in para.text:
        for run in para.runs:
            if "___________________________________" in run.text:
                run.text = run.text.replace("___________________________________", customer_address, 1)
```

## Template Structure

```
Title:     "MAIAEDGE, INC." (bold, centered)
Subtitle:  "MASTER SUBSCRIPTION AGREEMENT" (bold, centered)

Opening:   "Master Subscription Agreement, dated as of ______, 202_ (the
           "Effective Date"), between MaiaEdge, Inc., with offices at 77 Bedford
           Street, Suite 150, Burlington, MA 01803 ("MaiaEdge"), and
           _________________________, with offices at
           ___________________________________ ("Customer")."

Sections:
  1.  SCOPE OF AGREEMENT, GRANT OF LICENSE, EQUIPMENT AND PERSONNEL
      1.1 Scope of Agreement
      1.2 Access to Solution
      1.3 Equipment
      1.4 Restrictions
      1.5 Authorized Users
      1.6 Responsibilities
  2.  TERM OF AGREEMENT, SUBSCRIPTION TERM AND TERMINATION
      2.1–2.4
  3.  SERVICES FEES AND PAYMENT TERMS
      3.1–3.5
  4.  CUSTOMER DATA
      4.1–4.3
  5.  INTELLECTUAL PROPERTY RIGHTS
  6.  CONFIDENTIAL INFORMATION
      6.1–6.4
  7.  LIMITED WARRANTY AND DISCLAIMERS
      7.1–7.3
  8.  SUPPORT SERVICES; SERVICE LEVEL AGREEMENT
  9.  LIMITATION OF LIABILITY
  10. INDEMNIFICATION
      10.1–10.4
  11. GENERAL
      11.1–11.11

Exhibit A: Support Terms
Exhibit B: Service Level Agreement
```

## DO NOT MODIFY

- Any section content (1-11) — this is a legal contract
- Exhibit A (Support Terms)
- Exhibit B (Service Level Agreement)
- Any defined terms or legal language
- MaiaEdge company information

## Verification Checklist

Before delivering:
- [ ] Effective date is populated (no leftover "______")
- [ ] Customer legal name is populated (no leftover underscores)
- [ ] Customer address is populated (no leftover underscores)
- [ ] Customer name also appears in the signature block section
- [ ] No other content was modified
- [ ] File saved with correct naming: [CustomerShortName]_MSA_[EffectiveDate].docx
- [ ] Converted to PDF as primary deliverable
