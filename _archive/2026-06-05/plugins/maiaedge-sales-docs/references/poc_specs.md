# POC Agreement — Detailed Specifications

Read this file when generating Proof of Concept Agreements. It contains formatting details, template structure, and implementation guidance.

## Preferred Approach: Use the Helper Script

The fastest and most reliable way to generate a POC Agreement is to use the bundled script:

```bash
python build_poc.py --input data.json --template poc_agreement_template.docx
```

The script handles all variable replacement, logo swapping, table population, and signature updates. Prepare the input as JSON:

```json
{
  "date": "March 6, 2026",
  "customer_name": "Datum, Inc.",
  "customer_contact": "Manish Singh",
  "poc_duration": "90 days from date of first hardware delivery",
  "equipment": [
    {"sku": "ME-PBC-PCE-100G", "description": "Path Border Controller + PCE License, 100G, 90-Day POC", "qty": 3, "fee": "Complimentary"}
  ],
  "delivery_locations": [
    {"number": 1, "contact": "Manish Singh", "address": "Dallas, TX", "notes": "PBC Unit 1"}
  ],
  "fees_description": "at no charge",
  "maiaedge_signer_name": "Tim Ziemer",
  "maiaedge_signer_title": "CRO & Co-Founder",
  "customer_signer_name": "Manish Singh",
  "customer_signer_title": "CTO",
  "white_logo_path": "MaiaEdge_Logo_Horizontal_RevWhite.png",
  "output_path": "output.docx"
}
```

If the script isn't available or you need manual control, follow the specifications below.

---

## Template Structure (11 Sections)

All section body text is fixed legal boilerplate — NEVER modify it.

```
HEADER BLOCK (paragraphs 0-7):
  Para 0:  (empty)
  Para 1:  "PROOF OF CONCEPT AGREEMENT" (bold, ~20pt / 254000 EMU)
  Para 2:  "Confidential  |  MaiaEdge, Inc." (~10pt / 127000 EMU)
  Para 3:  "Date:  [VARIABLE]"         — bold label, normal value
  Para 4:  "Provider:  MaiaEdge, Inc.  —  Burlington, MA" (FIXED)
  Para 5:  "Customer:  [VARIABLE]"     — bold label, normal value
  Para 6:  "Customer Contact:  [VARIABLE]" — bold label, normal value
  Para 7:  "POC Duration:  [VARIABLE]" — bold label, normal value

TABLE 0: Logo table (1 col) — contains embedded image in Row 0
TABLE 1: Equipment table (4 cols: SKU, Description, Qty, POC Fee)
TABLE 2: Delivery Locations table (4 cols: #, Contact, Address, Notes)
TABLE 3: Signature table (3 cols: MaiaEdge | spacer | Customer)

SECTIONS (in paragraph body):
  1.  Purpose
  2.  POC Equipment          ← TABLE 1
  3.  Delivery Locations     ← TABLE 2
  4.  POC Period & Extension
  5.  Access and Support     ← bullet list
  6.  Fees
  7.  Confidentiality
  8.  Intellectual Property
  9.  Disclaimer of Warranties
  10. General
  11. Signatures             ← TABLE 3
```

## Variable Fields

| Variable | Where | How to Find |
|----------|-------|-------------|
| Date | Para starting with "Date:" | Content search for paragraph text starting with "Date:" |
| Customer name | Para starting with "Customer:" + Section 1 body + Signature table | Search by paragraph text prefix; also search-replace "Datum, Inc." in body |
| Customer contact | Para starting with "Customer Contact:" + Delivery table + Signature table | Search by paragraph text prefix |
| POC Duration | Para starting with "POC Duration:" | Search by paragraph text prefix |
| Equipment | TABLE 1 (doc.tables[1]) | Clear data rows (keep header), add new rows |
| Delivery locations | TABLE 2 (doc.tables[2]) | Clear data rows (keep header), add new rows |
| Fees description | Section 6 body | Search for "no charge" or "complimentary" in paragraph text |
| MaiaEdge signer | TABLE 3, Column 0 | Search for "Tim Ziemer" and "CRO & Co-Founder" in cell text |
| Customer signer | TABLE 3, Column 2 | Search for example customer name in cell text |

## Logo Replacement

The POC Agreement uses the **white logo** (`MaiaEdge_Logo_Horizontal_RevWhite.png`).

The logo is in Table 0, Row 0, Cell 0 as an embedded `<w:drawing>` element. To replace:

```python
from docx.shared import Inches

cell = doc.tables[0].rows[0].cells[0]

# Remove existing drawings
ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
for para in cell.paragraphs:
    for drawing in para._element.findall(f'.//{ns}drawing'):
        drawing.getparent().remove(drawing)
    for run in para.runs:
        run.text = ""

# Insert new logo
run = cell.paragraphs[0].add_run()
run.add_picture("MaiaEdge_Logo_Horizontal_RevWhite.png", width=Inches(2.5))
```

## Header Field Replacement

Labels in the template are bold and split across runs. For example, "POC Duration:" might be:
- Run 0: "POC Duration" (bold)
- Run 1: ":  " (bold)
- Run 2: "90" (normal)
- Run 3: " days from..." (normal)

To replace reliably, use content-based paragraph searching, then work with runs:
1. Find the paragraph whose `.text` starts with the label
2. Walk runs to find where the label ends and the value begins
3. Clear value runs and set the new value, preserving label formatting

## Equipment Table Format

| SKU | Description | Qty | POC Fee |
|-----|-------------|-----|---------|
| ME-PBC-PCE-100G | Path Border Controller + PCE License, 100G, 90-Day POC | 3 | Complimentary |

- SKU: Base product SKU from the price list
- Description: "[Product name] + PCE License, [capacity], [duration]-Day POC"
- Qty: Number of units
- POC Fee: "Complimentary" or dollar amount (always ask — NEVER assume)

## Delivery Locations Table Format

| # | Attention / Contact | Facility / Address | Notes |
|---|--------------------|--------------------|-------|
| 1 | Manish Singh | Dallas, TX | PBC Unit 1 |

- Row count should match total equipment quantity
- Use "TBD" for unconfirmed locations (at least 1 must be provided)

## Formatting Reference

- Title: Bold, ~20pt (254000 EMU)
- Section headings: Bold, ~12pt (152400 EMU), numbered
- Body text: Normal weight, ~11pt
- Subtitle: ~10pt (127000 EMU)
- Bullet list (Section 5): "List Paragraph" style
- Tables: 4-column with header row
- Signature table: 3-column, no visible borders

## DO NOT MODIFY

- Section body text (Sections 1-10) — legal boilerplate
- "Confidential | MaiaEdge, Inc." subtitle
- "Provider: MaiaEdge, Inc. — Burlington, MA" line
- Section numbering or ordering
- Table column headers

## Verification Checklist

Before delivering:
- [ ] All header fields populated (Date, Customer, Contact, Duration)
- [ ] Logo replaced with white version
- [ ] Equipment table has correct SKUs, descriptions, quantities, and fees
- [ ] Delivery locations table matches equipment quantity
- [ ] Section 1 body references correct customer name
- [ ] Fees section matches what's in the equipment table
- [ ] Signature block has correct names and titles on both sides
- [ ] No leftover example data (no "Datum, Inc.", "Manish Singh" unless that's the actual customer)
- [ ] File saved with correct naming: [CustomerShortName]_POC_Agreement_[Date].docx
- [ ] Converted to PDF as primary deliverable
