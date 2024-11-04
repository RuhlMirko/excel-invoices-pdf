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
    date = Path(file).stem.split('-')[1]

    pdf.set_font(family="Helvetica", size=16, style='B')
    pdf.cell(w=50, h=8, text=f"Invoice nr.{filename}", new_x='LMARGIN', new_y='NEXT')

    pdf.set_font(family="Helvetica", size=12, style='I')
    pdf.cell(w=50, h=8, text=f"Date: {date}", new_x='LMARGIN', new_y='NEXT')




    pdf.output(f'PDFs/{filename}.pdf')
