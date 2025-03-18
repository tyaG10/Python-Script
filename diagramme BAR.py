import matplotlib.pyplot as mp


ville = ("Yaounde", "Douala", "Bafoussam", "Bamenda", "Bertoua", "Ngaoundere", "Garoua","Maroua","Ebolowa", "Buea")
index = (1,2,3,4,5,6,7,8,9,10)
valeur = [50,36,56,87,563,415,45,12,98,256]

mp.bar(index, valeur, tick_lael=ville)

mp.ylabel("Population")
mp.xlabel("ville")
mp.show()