from PIL import Image

img = Image.open("C:/Users/tya/Desktop/t/script Python/Script CODE/qrcode.png")
rgb_image = img.convert("RGB")

rgb_image.save("C:/Users/tya/Desktop/t/script Python/Script CODE/qrcode.jpg")