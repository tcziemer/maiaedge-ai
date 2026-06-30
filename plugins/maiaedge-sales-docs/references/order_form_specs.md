# Order Form — Detailed Specifications

Read this file when generating Order Form documents. It contains the exact cell layout matching the template.

## Build Process (Exact Order)

LibreOffice recalc **strips rich text formatting**, so the order matters:

```
1. Copy order_form_template_1.xlsx → working file
2. CLEAR all variable cells (buyer info, product rows, totals, signatures, MSA ref)
3. Populate all variable fields (header, buyer, products, totals, MSA ref, signatures)
4. Apply all structural formatting (borders, merges, column widths, row heights, page setup)
5. Run recalc.py to calculate formulas and cache values
   → Path: .skills/skills/xlsx/scripts/recalc.py
6. AFTER recalc: Apply rich text formatting to section body cells (A31, A35, A39, A43, A47, A50)
7. Save final .xlsx
8. Convert to PDF: libreoffice --headless --calc --convert-to pdf (do NOT run recalc again)
```

## CRITICAL: Clear Old Template Data

The template ships with sample data (Rocnet Supply / IENTC). You MUST clear ALL variable cells before populating. Specifically clear:

```python
# Buyer info (D column, rows 6-11)
for row in range(6, 12):
    ws.cell(row=row, column=4).value = None  # D6:D11

# Product rows (A-G, row 15+) — clear the sample product
for col in range(1, 8):
    ws.cell(row=15, column=col).value = None

# Signature block (B column — old customer side)
for row in range(53, 58):
    ws.cell(row=row, column=2).value = None  # B53:B57

# Subscription date
ws['B27'].value = None

# MSA reference paragraph (A50, merged A:G)
ws['A50'].value = None
```

## Page Setup

- Orientation: Portrait (letter size)
- Fit to page: fitToWidth=1, fitToHeight=1
- Margins: left=0.4, right=0.4, top=0.35, bottom=0.35, header=0.15, footer=0.15
- Print area: A1:G57

## Logo

- **File**: `MaiaEdge_Logo_Horizontal_RGB.png` (dark/color logo)
- Position: Top LEFT at cell A1
- Size: width=220, height=63
- The template already has the logo. Do NOT re-insert unless it's missing.

## Actual Template Cell Layout

This is the EXACT cell-by-cell layout of the template. All cell references are verified.

```
Row 1:      [MaiaEdge Logo at A1]  (row height: 77)
Row 2:      E2: "Quote #" (bold)   F2: [value]             (row height: 25)
Row 3:      E3: "Date" (bold)      F3: [value]             (row height: 25)
Row 4:      [gap]                                           (row height: 20)
Row 5:      A5: "Sold By (Seller)" (bold)  D5: "Bill To (Buyer)" (bold)  (row height: 25)
Row 6:      A6: "MaiaEdge Inc."            D6: [Customer Name]           (row height: 25)
Row 7:      A7: "77 S. Bedford St., Suite 150"   D7: [Customer Address]  (row height: 25)
Row 8:      A8: "Burlington, MA 01803"     D8: [Customer Website URL]    (row height: 25)
Row 9:      A9: "Contact: Tim Ziemer"      D9: "Contact: [Name]"         (row height: 25)
Row 10:     A10: "Email: timziemer@maiaedge.io"  D10: "Email: [email]"   (row height: 25)
Row 11:     A11: "Terms: Net 30"           D11: "Phone: [phone]"         (row height: 25)
Row 12:     [gap]                                           (row height: 20)
Row 13:     C13: "MaiaEdge Confidential"                    (row height: 20)
Row 14:     [TABLE HEADERS: A=SKU, B=Product Name, C=Description, D=Subscription Term, E=Qty, F=Unit Price, G=Extended Price]
Row 15+:    [PRODUCT ROWS — one per SKU]
Row 16:     A16:E16 merged "Subtotal List Price"   G16: =SUM(G15:G15)
Row 17:     A17:E17 merged [blank]   F17: label   G17: formula
Row 18:     A18:E18 merged [blank]   F18: label   G18: formula  (discount row - hide if no discount)
Row 19:     F19: label               (final annual price - hide if no discount)
Row 20:     A20: "Quote Terms (summary)" (bold)
Row 21-25:  A21-A25: Quote term bullet points
Row 26:     A26: "MaiaEdge, Inc. – International Delivery..." (bold, Aptos 12pt)
Row 27:     A27: "Subscription start date"   B27: [date value]
Row 28:     A28:G28 merged — Subscription Term paragraph (Calibri 11pt)
Row 29:     A29: "1. Delivery and Risk of Loss" (bold, Aptos 12pt)
Row 31:     A31:G31 merged — Section 1 body text
Row 33:     A33: "2. Importer of Record and Compliance" (bold, Aptos 12pt)
Row 35:     A35:G35 merged — Section 2 body text
Row 37:     A37: "3. Taxes, Duties, and Governmental Charges" (bold, Aptos 12pt)
Row 39:     A39:G39 merged — Section 3 body text
Row 41:     A41: "4. Indemnification" (bold, Aptos 12pt)
Row 43:     A43:G43 merged — Section 4 body text
Row 45:     A45: "5. Survival" (bold, Aptos 12pt)
Row 47:     A47:G47 merged — Section 5 body text
Row 49:     A49: "Relationship to Master Service Agreement" (Helvetica Neue 16pt)
Row 50:     A50:G50 merged — MSA reference paragraph [VARIABLE — replace customer name + date]
Row 53:     A53: "For: MaiaEdge Inc. (Seller)"   B53: "For: [Customer] (Customer)"
Row 54:     A54: "Authorized Signature: ___..."   B54: "Authorized Signature: ___..."
Row 55:     A55: "Printed Name: ___..."           B55: "Printed Name: ___..."
Row 56:     A56: "Title: ___..."                  B56: "Title: ___..."
Row 57:     A57: "Date: ___..."                   B57: "Date: ___..."
```

**Key column facts:**
- Quote # and Date labels are in column E, values in column F (NOT F/G)
- Seller info is in column A, rows 5-11 (NOT merged A:C)
- Buyer info is in column D, rows 5-11 (NOT merged D:G)
- Signature block: seller in column A, customer in column B (NOT A:C / D:G)
- No cell merges in the header/buyer/seller section — only in totals rows (A16:E16, A17:E17, A18:E18), section body rows, and A28:G28

## Quote # and Date (Rows 2-3)

```
E2: "Quote #"   (right-aligned, bold, Tomorrow Regular 14pt) — DO NOT CHANGE
F2: [value]      (Tomorrow Regular 14pt) — REPLACE with quote number
E3: "Date"       (right-aligned, bold, Tomorrow Regular 14pt) — DO NOT CHANGE
F3: [value]      (Tomorrow Regular 14pt) — REPLACE with date string (e.g., "03_10_26")
```

## Seller Info (Column A, Rows 5-11) — STATIC, DO NOT CHANGE

The seller section is pre-populated in the template. Do NOT modify these cells:

```
A5:  "Sold By (Seller)"           (bold, Tomorrow Regular 14pt)
A6:  "MaiaEdge Inc."              (Tomorrow Regular 14pt)
A7:  "77 S. Bedford St., Suite 150"  (Tomorrow Regular 14pt)
A8:  "Burlington, MA 01803"       (Tomorrow Regular 14pt)
A9:  "Contact: Tim Ziemer"        (Tomorrow Regular 14pt)
A10: "Email: timziemer@maiaedge.io"  (Tomorrow Regular 14pt)
A11: "Terms: Net 30"              (Tomorrow Regular 14pt)
```

## Buyer Info (Column D, Rows 5-11) — VARIABLE, REPLACE ALL

Clear D6:D11 first, then populate:

```
D5:  "Bill To (Buyer)"            — DO NOT CHANGE (bold label)
D6:  "[Customer Company Name]"    (Tomorrow Regular 14pt)
D7:  "[Full Address]"             (Tomorrow Regular 14pt)
D8:  "[Website URL]"              (Tomorrow Regular 14pt — was Calibri 11 in template, match Tomorrow 14)
D9:  "Contact: [Name]"            (Tomorrow Regular 14pt)
D10: "Email: [email]"             (Tomorrow Regular 14pt)
D11: "Phone: [phone]"             (Tomorrow Regular 14pt)
```

## Product Table (Row 14 = Headers, Row 15+ = Data)

**Header row (14):** Gray fill (#F2F2F2), bold, centered, Tomorrow Regular 11pt, thin gray borders. DO NOT CHANGE.

**Product rows (15+):** Clear the sample row first. Then add one row per SKU:

```
A15: SKU                          (Tomorrow 11pt)
B15: Product Name                 (Tomorrow 11pt)
C15: Description                  (Tomorrow 11pt, wrap text)
D15: "[X] months"                 (Tomorrow 11pt)
E15: Qty                          (Tomorrow Regular 12pt, right-aligned)
F15: Unit Price (Annual)          (Tomorrow 11pt, number — NOT currency formatted in cell)
G15: =E15*F15                     (Tomorrow Regular 12pt, right-aligned, formula)
```

If multiple SKUs, add rows 16, 17, etc. and push totals rows down accordingly. For a single-SKU order, row 15 holds the product and row 16+ hold totals.

**Column widths:** A=26.7, B=27.1, C=32.7, D=15.1, E=8.0, F=14.0, G=22.0

**Row height for product rows:** ~115 (to fit the full description text)

## Totals Area

The totals area starts immediately after the last product row. The template has rows 16-19 for totals.

### No Discount (standard case)

When there is NO discount, use only two total rows and HIDE/CLEAR the discount rows:

```
Row 16: A16:E16 merged — clear text     F16: "Total Contract Value"    G16: =SUM(G15:G15)*[years]
Row 17: A17:E17 merged — clear text     F17: "Annual Price"            G17: =SUM(G15:G15)
Row 18: F18: [clear]                    G18: [clear]                   — HIDE this row
Row 19: F19: [clear]                                                   — HIDE this row
```

Set F16 and F17 font: bold, right-aligned.
Set G16 and G17 font: Tomorrow Regular 12pt, bold.
Add a medium black bottom border to G17.

### With Discount

```
Row 16: A16:E16 merged    F16: "Total Contract Value"      G16: =SUM(G15:G15)*[years]
Row 17: A17:E17 merged    F17: "Annual Price"              G17: =SUM(G15:G15)
Row 18: A18:E18 merged    F18: "Discount ([X]%)"           G18: =G17*[discount_pct]
Row 19:                    F19: "Discounted TCV"            G19: =(G17-G18)*[years]
                           (add F20/G20 if needed for "Discounted Annual Price")
```

**Important:** The `[years]` multiplier for TCV = term months ÷ 12 (e.g., 36 months = 3).

## Subscription Start Date (Row 27)

The template has a SPLIT layout:

```
A27: "Subscription start date"     (Tomorrow Regular 11pt — label, keep as-is)
B27: [date value]                  (Tomorrow Regular 11pt — REPLACE with date, e.g., "4/1/2026")
```

Do NOT combine into a single cell. Keep A27 as the label and put the date in B27.

## Subscription Term Paragraph (Row 28)

A28:G28 is merged. This is boilerplate text about the subscription term. **Leave as-is in the template** — do NOT modify.

## Sections 1-5 (Rows 29-47)

The template has a TWO-ROW structure for each section:
- **Heading row** (A29, A33, A37, A41, A45): Bold, Aptos 12pt — leave as-is
- **Body row** (A31, A35, A39, A43, A47): Merged A:G — leave as-is

**These are all boilerplate legal text. Do NOT modify any section content.**

However, after recalc.py runs, the body cells (A31, A35, etc.) may need rich text reapplied since recalc can strip it. Apply rich text AFTER recalc:

```python
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont

bold_font = InlineFont(b=True, sz=12, rFont='Aptos')
normal_font = InlineFont(b=False, sz=12, rFont='Aptos')

# Example for A31 — combine heading + body into the merged cell
rich = CellRichText(
    TextBlock(bold_font, "1. Delivery and Risk of Loss\n"),
    TextBlock(normal_font, "Delivery of the Equipment shall be made...")
)
ws['A31'].value = rich
ws['A31'].font = Font(name='Aptos', size=12, bold=False)
```

**Note:** The heading rows (A29, A33, etc.) are SEPARATE from the body rows. The rich text in the body cells should include the heading text as a bold first line followed by the body paragraph. This means:
- After applying rich text to A31, A35, etc., the separate heading rows (A29, A33, etc.) can be hidden or their content cleared to avoid duplication.
- OR keep the heading rows visible and don't include the heading in the rich text body cell.

**Recommended approach:** Leave the template's heading rows (A29, A33, A37, A41, A45) and body rows (A31, A35, A39, A43, A47) exactly as they are. Do NOT apply rich text unless recalc has actually stripped the formatting. Check after recalc — if the body cells still look correct, skip rich text entirely.

## MSA Reference (Row 49-50)

Row 49 is the heading: "Relationship to Master Service Agreement" — leave as-is.

Row 50 (A50:G50 merged) is the MSA reference paragraph — this is **VARIABLE**. Replace the full text with:

```
"This Service Order is issued under and governed by the Master Subscription Agreement between MaiaEdge Inc. and [CUSTOMER NAME] dated [MSA_DATE] (the "MSA"). Capitalized terms used but not defined in this Service Order have the meanings given in the MSA. In the event of any conflict between this Service Order and the MSA, the MSA shall control unless this Service Order expressly states otherwise."
```

Set font: Calibri 11pt, wrap text.

## Signature Block (Rows 53-57)

The signature block uses columns **A (seller)** and **B (customer)**. NOT merged A:C / D:G.

Font: Helvetica Neue 9.6pt. Row heights: ~16pt each.

**Seller side (column A) — DO NOT CHANGE:**
```
A53: "For: MaiaEdge Inc. (Seller)"
A54: "Authorized Signature: ____________________________"
A55: "Printed Name: ____________________________________"
A56: "Title: ___________________________________________"
A57: "Date: ____________________________________________"
```

**Customer side (column B) — CLEAR old data, then populate:**
```
B53: "For: [Customer Name] (Customer)"
B54: "Authorized Signature: ____________________________"
B55: "Printed Name: ____________________________________"
B56: "Title: ___________________________________________"
B57: "Date: ____________________________________________"
```

## Hidden Rows

The template does NOT have hidden rows. All rows are visible. The section heading rows (29, 33, 37, 41, 45) have a height of ~16. The gap between sections is achieved through the body row heights. Do NOT hide any rows unless you are hiding unused discount rows (18-19).

## Row Heights Reference (From Template)

```
Row 1:  77    (logo)
Row 2-3: 25   (quote info)
Row 4:  20    (gap)
Row 5-11: 25  (seller/buyer)
Row 12: 20    (gap)
Row 13: 20    (confidential)
Row 14: 30    (table headers)
Row 15: 115   (product row — tall for description)
Row 16: 20    (subtotal)
Row 17: 24    (annual price)
Row 18: 29    (discount — hide if not used)
Row 19: 20    (total — hide if not used)
Row 20-25: 20 (quote terms)
Row 26: 20    (delivery terms heading)
Row 27: 20    (subscription start date)
Row 28: 85    (subscription paragraph)
Row 29: 16    (section 1 heading)
Row 31: 16    (section 1 body — auto-height if needed)
Row 33: 16    (section 2 heading)
Row 35: 16    (section 2 body)
Row 37: 16    (section 3 heading)
Row 39: 16    (section 3 body)
Row 41: 16    (section 4 heading)
Row 43: 16    (section 4 body)
Row 45: 16    (section 5 heading)
Row 47: 16    (section 5 body)
Row 49: 20    (MSA heading)
Row 50: (auto) (MSA body)
Row 53-57: 16 (signatures)
```

## Calculation Verification

Before finalizing:
- [ ] Extended Price = Unit Price × Qty (each product row)
- [ ] TCV = Sum of Extended Prices × Term Years
- [ ] Annual Price = Sum of Extended Prices
- [ ] If discount: Discount Amount = Annual Price × Discount %
- [ ] If discount: Discounted TCV = (Annual - Discount) × Years
- [ ] If discount: Discounted Annual = Annual - Discount
- [ ] Unit prices match `price_list.md` Annual Price column for the term length
- [ ] HA units are 30% off primary (verify against price_list.md)
- [ ] Quote # and Date populated in F2 and F3 (not G2/G3)
- [ ] All old template buyer data cleared (D6:D11)
- [ ] All old template signature data cleared (B53:B57)
- [ ] MSA reference paragraph updated with correct customer name and date
- [ ] B27 has the subscription start date
