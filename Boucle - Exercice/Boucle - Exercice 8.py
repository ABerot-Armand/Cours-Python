num=int
count=int(0)
while (num != 0):
    count = count + 1
    num=int(input("Veuillez entrer un nombre "))
    if count == 1:
        Base = num
        truc = count    
    elif (num > Base):
        Base = num
        truc = count
print(Base,"est le plus grand nombre rentré (c'était le nombre numero",truc,")")
