import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for file in filepaths:
    df = pd.read_excel(file, sheet_name='Sheet 1')
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(file).stem.split('-')[0]

    print(filename)
    pdf.set_font(family="Helvetica", size=16, style='B')
    pdf.cell(w=50, h=8, text=f"Invoice nr.{filename}")

    pdf.output(f'PDFs/{filename}.pdf')
