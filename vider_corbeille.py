import winshell
try:
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
    print("On vient de vider la corbeile")
except:
    print("La corbeille est deja vide")