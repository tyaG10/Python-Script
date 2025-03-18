nombre_romain = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def Romain_to_decimal(NbreRomain):
    
    sum = 0
    for i in range(len(NbreRomain) - 1):
        left = NbreRomain[i]
        right = NbreRomain[i+1]
        
        if nombre_romain[left] < nombre_romain[right]:
            sum -= nombre_romain[left]
            
        else:
            sum += nombre_romain[right]
            
    sum += nombre_romain[NbreRomain[-1]]
    print("La valeur du nombre romain en decimal est : ",sum)
        
        
romain = input("Entrer un nombre romain : ")
Romain_to_decimal(romain)