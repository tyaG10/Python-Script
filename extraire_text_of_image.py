from PIL import Image
from pytesseract import pytesseract

chemin_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

chemin_image = "C:/Users/tya/Desktop/t/script Python/Script CODE/image.PNG"

pytesseract.tesseract_cmd = chemin_tesseract

img = Image.open(chemin_image)

text = pytesseract.image_to_string(img)

print(text)