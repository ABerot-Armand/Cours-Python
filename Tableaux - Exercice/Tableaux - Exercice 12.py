nombreValeur = int(input("entre le nombre de valeur que vous souhaitez saisir "))
nTab = nombreValeur*[0]
for i in range (nombreValeur):
    nTab[i] = float(input("saississez une valeur : "))
print(nTab)

moyenne=(sum(nTab)/len(nTab))
supmoy=0
for i in range (len(nTab)):
    if (nTab[i] >= moyenne):
        supmoy+=1

print(supmoy)
