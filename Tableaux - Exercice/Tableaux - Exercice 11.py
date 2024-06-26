nombreValeur = int(input("entre le nombre de valeur que vous souhaitez saisir "))
nTab = nombreValeur*[0]
for i in range (nombreValeur):
    nTab[i] = float(input("saississez une valeur : "))
print(nTab)
max=nTab[1]
maxcase=1
min=nTab[1]
mincase=1
for i in range (len(nTab)):
    if max < nTab[i]:
        max = nTab[i]
        maxcase = i+1
    if nTab[i] < min:
        min = nTab[i]
        mincase = i+1

print("La valeur la plus grande est",max,"dans la cellule numero",maxcase)
print("la valeur la plus petite est",min,"dans la cellule numero",mincase)
