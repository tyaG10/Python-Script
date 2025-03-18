import PyPDF2

pdf = open("C:/Users/tya/Desktop/t/script Python/Script CODE/soutenance-GRP1.pdf", "rb")
lire = PyPDF2.PdfFileReader(pdf)
page = lire.getPage(0)
print(page.extract_text())