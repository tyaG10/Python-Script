from captcha.image import ImageCaptcha
from PIL import Image

image = ImageCaptcha(width=400, height=200)
text_captcha = input("Le texte captcha :")
donne = image.generate(text_captcha)
image.write(text_captcha, "C:/Users/tya/Desktop/t/script Python/Script CODE/captcha_image.png")
Image.open("C:/Users/tya/Desktop/t/script Python/Script CODE/captcha_image.png")