from PyPDF2 import PdfFileWriter, PdfFileReader

filename = "/home/pmoracho/Descargas/04YA6001.pdf"

pdf = PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print(page.extractText())

