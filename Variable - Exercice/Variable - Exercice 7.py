fir=float(input("Veuillez entrer un premier nombre "))
sec=float(input("Veuillez entrer un second nombre "))
thi=float(input("Veuillez entrer un second nombre "))

if fir == sec == thi:
    print("les nombres sont égaux")
    

if fir > sec:
    if fir > thi:
        print ("le plus grand nombre est" ,fir)

if fir < sec:
    if sec > thi:
        print ("le plus grand nombre est" ,sec)
    else:
        print ("le plus grand nombre est" ,thi)
