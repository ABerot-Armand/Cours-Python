nombreValeur = int(input("entre le nombre de valeur que vous souhaitez saisir "))
nTab = nombreValeur*[0]
for i in range (nombreValeur):
    nTab[i] = float(input("saississez une valeur : "))
print(nTab)

for i in range (len(nTab)):
    nTab[i] = nTab [i] +1
print(nTab)
