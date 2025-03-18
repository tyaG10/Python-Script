from pyzbar.pyzbar import decode
from PIL import Image



decoderQR = decode(Image.open("C:/Users/tya/Desktop/t/script Python/Script CODE/qrcode.png"))
print(decoderQR[0].data.decode("ascii"))
