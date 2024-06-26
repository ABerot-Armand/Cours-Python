#num=int(input("Veuillez entrer un nombre "))
#truc=num
#resultat=float(1)
#for count in range (1,num+1):
#    resultat*=count
#
#print(truc, '! =',resultat)

#Écrire un algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts
#volontaires. On demande à l’utilisateur le nombre de chevaux partants, et le nombre de chevaux joués. Les deux
#messages affichés devront être :
#Dans l’ordre : une chance sur X de gagner
#Dans le désordre : une chance sur Y de gagner
#X et Y nous sont donnés par la formule suivante, si n est le nombre de chevaux partants et p le nombre de chevaux joués
#(on rappelle que le signe ! signifie "factorielle", comme dans l'exercice 6 ci-dessus)
#X = n ! / (n - p) !
#Y = n ! / (p ! * (n – p) !)

cheveauxpartant=int(input("Veuillez entrer le nombre de cheveaux partant "))
cheveauxjoue=int(input("Veuillez entrer le nombre de cheveaux joué(s) "))
cheveauxultime = cheveauxpartant - cheveauxjoue

factocheveauxpartant=float(1)
for count in range (1,cheveauxpartant+1):
    factocheveauxpartant*=count

factocheveauxjoue=float(1)
for count in range (1,cheveauxjoue+1):
    factocheveauxjoue*=count

factocheveauxultime=float(1)
for count in range (1,cheveauxultime+1):
    factocheveauxultime*=count

X = (factocheveauxpartant / factocheveauxultime)
Y = (factocheveauxpartant / (factocheveauxjoue * factocheveauxultime))

print("Dans l’ordre : une chance sur ",X," de gagner")
print("Dans le désordre : une chance sur ",Y," de gagner")
