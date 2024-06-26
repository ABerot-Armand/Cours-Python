num=float(input("Veuillez entrer un nombre entre 10 et 20 "))
while (num<10) or (num>20) :
    if num<10 :
        num=float(input("Plus grand ! "))
    if num>20 :
        num=float(input("Plus petit ! "))

print ("c'est bon")
