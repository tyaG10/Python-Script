from forex_python.converter import CurrencyRates

c = CurrencyRates()


sum = int(input("Entrer la somme a convertir :"))
uniteSource = input("Donner la devise de la somme a convertir :").upper()
uniteDestination = input("Vous voulez convertir la monnaie en quoi ? :").upper()

print(f"Ainsi vous voulez convertir {sum} {uniteSource} en {uniteDestination}")
result = c.convert(uniteSource, uniteDestination, sum)

print(f"Le resultat est {result} {uniteDestination}")