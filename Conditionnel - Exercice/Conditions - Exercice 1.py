fir=float(input("Veuillez entrer un premier nombre "))
sec=float(input("Veuillez entrer un second nombre "))
thi=float(input("Veuillez entrer un second nombre "))

if fir == sec == thi:
    print("les nombres sont égaux")
    
elif fir > sec and fir > thi:
    print ("le plus grand nombre est" ,fir)

elif fir < sec and sec > thi:
    print ("le plus grand nombre est" ,sec)
    
else:
    print ("le plus grand nombre est" ,thi)
