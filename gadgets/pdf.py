from  fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="PDF by Dalibor written in Python.", ln=True, align='C')
pdf.output("./pdf.pdf")

print("✅PDF created successfully.")