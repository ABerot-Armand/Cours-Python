print("Veuillez entrer les trois longueurs d'un triangle")
fir=float(input("Premiere longueur "))
sec=float(input("Seconde longueur "))
thi=float(input("Troisème longueur "))

fircube=fir**2
seccube=sec**2
thicube=thi**2

if (fircube == (seccube + thicube)) or (seccube == (fircube + thicube)) or (thicube == (fircube + seccube)):
        print ("le triangle est rectangle")

else:
        print ("le triangle n'est pas rectangle")
