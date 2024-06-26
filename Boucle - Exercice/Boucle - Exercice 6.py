num=int(input("Veuillez entrer un nombre "))
resultat=float(1)
for count in range (1,num+1):
    resultat*=count

print(num, '! =',resultat)
