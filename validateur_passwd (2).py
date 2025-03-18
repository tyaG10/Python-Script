
def validateur(password):
    if len(password) < 6 or len(password) > 40:
        print("Le mot de passe doit etre compris entre 6 et 40 caracteres")
        return False
        
    minuscule = False
    majuscule = False
    chiffre = False
    special = False
    
    for caractere in password:
        if caractere.islower():
            minuscule = True
            
        if caractere.isupper():
            majuscule = True
            
        if caractere.isdigit():
            chiffre = True
            
        if not caractere.isalnum():
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