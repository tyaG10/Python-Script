
def validateur(password):
    if len(password) < 6 or len(password) > 40:
        print("Le mot de passe doit etre compris entre 6 et 40 caracteres")
        return False
        
    minuscule = False
    majuscule = False
    chiffre = False
    special = False
    
    for i in range(len(password)):
        if password[i] >= "a" and password[i] <= "z":
            minuscule = True
            
        if password[i] >= "A" and password[i] <= "Z":
            majuscule = True
            
        if password[i] >= "0" and password[i] <= "9":
            chiffre = True
            
        if password[i]=="@" or password[i]=="#" or password[i]=="$" or password[i]=="%" or password[i]=="?" or password[i]=="&" or password[i]=="!":
            special = True
            
    if minuscule==False:
        print("Le mot de passe doit comporter au moins une lettre minuscule")
        
    if majuscule==False:
        print("Le mot de passe doit comporter au moins une lettre majuscule")
    
    if chiffre==False:
        print("Le mot de passe doit comporter au moins un chiffre")
        
    if special==False:
        print("Le mot de passe doit comporter au moins un caractere special")
        
    if minuscule and majuscule and chiffre and special:
        print("le mot de passe respecte tout les norme") 
        
    return True


mdp = input("Entrer un mot de passse : \n")
validateur(mdp)