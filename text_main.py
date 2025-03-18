import pywhatkit as kit
import cv2

text = input("Saisir un texte : ")
kit.text_to_handwriting(text, save_to="C:/Users/tya/Desktop/t/script Python/Script CODE/saisir_main.png")
img = cv2.imread("C:/Users/tya/Desktop/t/script Python/Script CODE/saisir_main.png")
cv2.imshow("C:/Users/tya/Desktop/t/script Python/Script CODE/saisir_main.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()