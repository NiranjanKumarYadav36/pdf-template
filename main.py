from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='p', unit='mm', format='A4')

df = pd.read_csv("topics (1).csv")

for index, rows in df.iterrows():
    for i in range(rows['Pages']):
        pdf.add_page()
        pdf.set_font(family="Times", style='B', size=15)
        pdf.set_text_color(100, 0, 100)
        pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1)
        pdf.line(x1=10, y1=20, x2=200, y2=20)

    # for i in range(rows['Pages'] - 1):
    #     pdf.add_page()


pdf.output("output.pdf")

