for count in range (4):
    num=int(input("Veuillez entrer un nombre "))
    if count == 0:
        Base = num
        truc = count + 1
    elif (num > Base):
        Base = num
        truc = count + 1
print(Base,"est le plus grand nombre rentré (c'était le nombre numero",truc,")")
