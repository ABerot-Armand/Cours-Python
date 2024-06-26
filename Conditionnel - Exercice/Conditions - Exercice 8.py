heure=int(input("Veuillez entrer l'heure qu'il est. (Sans les minutes) "))
minute=int(input("Veuillez entrer les minutes "))

if minute + 1 < 59:
    print("Dans une minute il sera ",heure,"h",minute +1)

elif heure +1 == 24:
    print("Dans une minute il sera 00 h 00")
    
else: 
    print("Dans une minute il sera ",heure+1,"h 00")
