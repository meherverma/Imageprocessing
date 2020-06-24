import PyPDF2

with open('invoice.pdf', 'rb') as file:
    reader=PyPDF2.PdfFileReader(file)
    print(reader.numPages)