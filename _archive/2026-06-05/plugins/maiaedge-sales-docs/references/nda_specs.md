# NDA — Detailed Specifications

Read this file when generating Mutual Non-Disclosure Agreements. It contains the template structure, variable field locations, and implementation guidance.

## Preferred Approach: Use the Helper Script

```bash
python build_nda.py --input data.json --template nda_template.docx
```

Prepare the input as JSON:

```json
{
  "effective_date": "March 6, 2026",
  "participant_name": "Datum, Inc.",
  "participant_address": "100 Main Street, Suite 400, Dallas, TX 75201",
  "signer_name": "Manish Singh",
  "signer_title": "CTO",
  "output_path": "Datum_NDA_March2026.docx"
}
```

If the script isn't available, follow the manual specifications below.

---

## Template Structure (8 Sections)

All section body text is fixed legal boilerplate — NEVER modify it.

```
TITLE (para 0):    "Mutual Non-Disclosure Agreement" (bold, centered, ~11.5pt / 146050 EMU)
BLANK (para 1):    empty
PREAMBLE (para 2): "Mutual Non-Disclosure Agreement, entered into on ________, 202_
                    (the "Effective Date"), is made by and between MaiaEdge, Inc. ..."
BLANK (para 3):    empty

SECTIONS (paras 4-18, alternating content and blank lines):
  1. Confidential Information  (List Paragraph style)
  2. Exceptions                (List Paragraph style)
  3. Non-Use and Non-Disclosure (List Paragraph style)
  4. No License or Warranties  (List Paragraph style)
  5. Irreparable Harm          (List Paragraph style)
  6. Return of Information     (List Paragraph style)
  7. Term and Termination      (List Paragraph style)
  8. General                   (List Paragraph style)

BLANK (para 19):   empty

SIGNATURE BLOCK (paras 20-26, tab-aligned two columns):
  Para 20 (Heading 1): "MaiaEdge, Inc.\t\t\t\t\t\tParticipant:\t___..."
  Para 21 (Heading 1): "77 Bedford Street, Suite 150\t\t\t\tAddress:\t___..."
  Para 22 (Body Text): "Burlington, MA 01803\t\t\t\t\t\t___..." (address continuation)
  Para 23 (Normal):    "\t" (spacer)
  Para 24 (Body Text): "Signed:\t\t___...\tSigned:\t\t___..."
  Para 25 (Body Text): "Printed Name:\t___...\tPrinted Name:\t___..."
  Para 26 (Body Text): "Title:\t\t___...\tTitle:\t\t___..."
```

The NDA has **NO tables** and **NO embedded images**.

## Variable Fields — Content-Based Search

**Do NOT use hardcoded paragraph indices.** Always search by content patterns.

| Variable | How to Find | What to Replace |
|----------|-------------|-----------------|
| Effective date | Search for paragraph containing `"________, 202_"` | Replace the underscore+year pattern with "Month Day, Year" |
| Participant name | Search for paragraph containing `"Participant:\t"` (Heading 1 style) | Replace `"_______________________________"` after the tab |
| Participant address | Search for paragraph containing `"Address:\t"` (Heading 1 style) | Replace `"_______________________________"` after the tab |
| Address continuation | The paragraph immediately after Address (Body Text style, contains `Burlington`) | Replace right-side `"_______________________________"` |
| Signer name | Search for paragraph containing `"Printed Name:\t"` | Replace the **SECOND** set of underscores (right-side column) |
| Signer title | Search for paragraph containing `"Title:\t"` (last such paragraph) | Replace the **SECOND** set of underscores (right-side column) |

## Run-Level Replacement Approach

The underscore blanks (`_______________________________`) may span multiple runs. The safe approach:

```python
def replace_blank_in_paragraph(para, search_text, new_value, occurrence=1):
    """
    Find a paragraph containing search_text, then replace the Nth
    occurrence of underscore blanks with new_value.
    """
    full_text = para.text
    if search_text not in full_text:
        return False

    # Find underscore patterns (3+ consecutive underscores)
    import re
    blanks = list(re.finditer(r'_{3,}', full_text))
    if occurrence > len(blanks):
        return False

    target = blanks[occurrence - 1]
    start, end = target.start(), target.end()

    # Map character positions to runs
    pos = 0
    for run in para.runs:
        run_start = pos
        run_end = pos + len(run.text)
        if run_start <= start < run_end:
            # This run contains (or starts) the blank
            prefix = run.text[:start - run_start]
            suffix = run.text[end - run_start:] if end <= run_end else ""
            run.text = prefix + new_value + suffix
            # Clear any remaining runs that were part of the blank
            ...
            return True
        pos = run_end
    return False
```

For the signature block, "second occurrence" means the right-side column (Printed Name, Title).

## Formatting Reference

- Title: Bold, centered, ~11.5pt (146050 EMU)
- Body text / Preamble: 9pt (114300 EMU), "Body Text" style
- Section items: 9pt (114300 EMU), "List Paragraph" style, numbered 1-8
- Section heading words: Bold within list item (e.g., **"Confidential Information."** then normal)
- Signature block: Mix of "Heading 1" and "Body Text" styles, tab-aligned

## DO NOT MODIFY

- Title text or formatting
- Any numbered section content (1-8) — legal boilerplate
- MaiaEdge company info (name, address: 77 Bedford Street, Suite 150, Burlington, MA 01803)
- Governing law: State of Delaware
- Term duration: 3 years
- Survival period: 3 years from disclosure date

## Verification Checklist

Before delivering:
- [ ] Effective date is populated (no leftover "________, 202_")
- [ ] Participant company name appears in signature block
- [ ] Participant address is filled in (both lines)
- [ ] Signer name appears under "Printed Name" on the right side
- [ ] Signer title appears under "Title" on the right side
- [ ] MaiaEdge side of signature block is unchanged
- [ ] No leftover underscore blanks in any variable field
- [ ] File saved with correct naming: [CustomerShortName]_NDA_[EffectiveDate].docx
- [ ] Converted to PDF as primary deliverable
