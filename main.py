from tkinter import PAGES, Variable
from fpdf import FPDF
import pandas as pd

# Create PDF object with specified settings
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Read data from CSV file
df = pd.read_csv("topics.csv")

# Iterate over rows in dataframe and create PDF pages
for index, row in df.iterrows():
    pdf.add_page()

    # Set font, color and print topic on the page
    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Add horizontal line after topic
    pdf.line(10, 22, 200, 22)

    # Add vertical lines with interval of 10mm
    for space in range(0, 260, 10):
        pdf.line(10, 32 + space, 200, 32 + space)

    # Set footer at bottom of the page
    pdf.ln(265)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(100, 180, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add additional pages for the topic if necessary
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set footer on additional pages
        pdf.ln(277)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(100, 180, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Add vertical lines with interval of 10mm on additional pages
        for space in range(0, 260, 10):
            pdf.line(10, 32 + space, 200, 32 + space)

# Output PDF file
pdf.output("output.pdf")