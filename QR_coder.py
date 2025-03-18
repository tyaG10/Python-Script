import pyqrcode
import png

text = input("Entrer un text :")
qrcode = pyqrcode.create(text)

qrcode.png("C:/Users/tya/Desktop/t/script Python/Script CODE/qrcode.png", scale=5)

