year=int(input("Veuillez entrer une année "))

if year % 400 == 0 :
    print(year, "est bissextile")

elif year % 4 == 0 and year % 100 != 0 :
    print(year, "est bissextile")

else : print(year, "n'est pas bissextile")
