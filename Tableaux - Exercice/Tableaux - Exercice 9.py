tab1 = [1,2,8,4,5]
tab2 = [6,7,3,9,10]

print(tab1)
print (tab2)
tab3 = len(tab1)*[0]
for i in range (len(tab1)):
    tab3[i]= tab1[i] + tab2[i]

print(tab3)
