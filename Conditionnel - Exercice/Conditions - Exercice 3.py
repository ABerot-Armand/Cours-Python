#ax²+bx+c=0
#delta = b²-4ac
#Delta>0 : 2 solution
            #x1= -b-sqrt(delta) //2a ; x2= -b+sqrt(delta) //2a

#Delta=0 1 solution
            #x1 = -b//2a

#Delta<0 pas de Solution réelle possible
import math
print("Veuillez entrer a, b et c")
a=float(input("a=? "))
b=float(input("b=? "))
c=float(input("c=? "))

delta=float(b**2-4*a*c)

#x1(float((-b - math.sqrt(delta))/(2*a)))
#x2(float((-b + math.sqrt(delta))/(2*a)))

if delta > 0:
    print("Il y a deux solutions: x1=",-b - math.sqrt(delta)/(2*a),"et x2=",-b + math.sqrt(delta)/(2*a),)

elif delta < 0:
    print("Il n'y a pas de solution")

else:
    print("Il n'y a qu'une solution: x1=", -b / (2*a),)
