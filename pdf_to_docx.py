from pdf2docx import Converter

chemin_document_pdf = "C:/Users/tya/Desktop/t/script Python/Script CODE/Group 1.pdf"
chemin_document_word = "C:/Users/tya/Desktop/t/script Python/Script CODE/Group 1.pdf.docx"

cv = Converter(chemin_document_pdf)
cv.convert(chemin_document_word)

cv.close()