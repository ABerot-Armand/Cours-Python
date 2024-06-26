num=int
total=int(0)
while (num != 0):
    num=int(input("Veuillez entrer un nombre "))
    total = total + num
print(total)

paiement=int(input("Veuillez entrer la somme payé "))
paiement = paiement - total
while (paiement > 9):
    print ("10 euros")
    paiement = paiement - 10
while (paiement > 4):
    print("5 euros")
    paiement = paiement - 5
while (paiement > 0):
     print("1 euro")
     paiement = paiement - 1


