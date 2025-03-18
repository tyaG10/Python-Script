import matplotlib.pyplot as mp


ville = ("Yaounde", "Douala", "Bafoussam", "Bamenda", "Bertoua", "Ngaoundere", "Garoua","Maroua","Ebolowa", "Buea")
valeur = [50,36,56,87,563,415,45,12,98,256]

mp.pie(valeur, labels=ville, autopct='%1.f%%', counterclock=False, startangle=105)
mp.show()