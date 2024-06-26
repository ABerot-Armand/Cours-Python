fir=float(input("Veuillez entrer un premier nombre "))
sec=float(input("Veuillez entrer un second nombre "))
thi=float(input("Veuillez entrer un troisième nombre "))

if fir > sec and sec > thi : 

        X = thi
        Y = sec
        Z = fir

elif fir > sec and thi > sec :
        X = sec
        Y = thi
        Z = fir

elif sec > fir and fir > sec :
        X = thi
        Y = fir
        Z = sec

elif sec > fir and sec > fir :
        X = fir
        Y = thi
        Z = sec

elif thi > fir and fir > sec :
        X = sec
        Y = fir
        Z = thi

else :
        X = fir
        Y = sec
        Z = thi


print("X = ",X,"Y = ",Y,"Z = ",Z)
