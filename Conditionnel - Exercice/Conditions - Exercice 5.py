print("Veuillez entrer les trois longueurs d'un triangle")
fir=float(input("Premiere longueur "))
sec=float(input("Seconde longueur "))
thi=float(input("Troisème longueur "))


if (fir > (sec + thi)) or (sec > (fir + thi)) or (thi > (fir + sec)):
        print ("le triangle n'est pas constructible")

else:
        print ("le triangle est constructible")
