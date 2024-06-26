nombreValeur = int(input("entre le nombre de valeur que vous souhaitez saisir "))
nTab = nombreValeur*[0]
nombresPositifs = 0
nombresNegatifs = 0
for osef in range (nombreValeur):
    nTab[osef] = float(input("saississez une valeur : "))
    if nTab[osef]>0:
        nombresPositifs = nombresPositifs + 1
    else:
        nombresNegatifs = nombresNegatifs + 1

print("Vous avez rentrez",nombresPositifs," nombres positifs")
print("Vous avez rentrez",nombresNegatifs," nombres négatifs")
