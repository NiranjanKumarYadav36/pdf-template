from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', unit='mm', format='A4')
pdf.set_auto_page_break(auto='False', margin=0)

df = pd.read_csv("topics (1).csv")

for index, rows in df.iterrows():
    # for i in range(rows['Pages']):

    # set the header
    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=15)
    pdf.set_text_color(100, 0, 100)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1)

    for i in range(20, 280, 10):
        pdf.line(10, i, 200, i)

    # set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style='B', size=9)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=5, txt=rows['Topic'], align='R')

    for i in range(rows['Pages'] - 1):
        pdf.add_page()

        for j in range(20, 280, 10):
            pdf.line(10, j, 200, j)

        # set the footer
        pdf.ln(262)
        pdf.set_font(family="Times", style='B', size=9)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=rows['Topic'], align='R')

pdf.output("output.pdf")
