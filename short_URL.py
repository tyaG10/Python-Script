import pyshorteners

lien = input("Entrer votre lien : ")
type_lien = pyshorteners.Shortener()
short_lien = type_lien.tinyurl.short(lien)

print("Le lien reduit est : "+short_lien)