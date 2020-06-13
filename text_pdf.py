import pdfplumber
pdf = pdfplumber.open('pdf-sample.pdf')
page = pdf.pages[1]
text = page.extract_text()
print(text)
pdf.close()