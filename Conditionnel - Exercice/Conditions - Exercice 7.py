copies=float(input("Veuillez entrer le nombre de copies voulu "))

if copies < 20:
    copies = copies / 100
    print("vous devez payer", copies * 10,"euros")

if copies > 20:
    copies = copies - 20
    copies = copies / 100
    print("vous devez payer", copies * 8 + 2,"euros")
