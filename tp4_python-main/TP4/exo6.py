tab=[5, 2, 4, 8, 1, 3]
for i in range(len(tab)):
   for j in range(i+1,len(tab)):
       if tab[i]>tab[j]:
           print(tab)
           temp=tab[j]
           tab[j]=tab[i]
           tab[i]=temp
#------------------------------
print("question 2 :")
tab=[5, 2, 4, 8, 1, 3]
print(sorted(tab))
#------------------------------
print("question 3 :")
tab=[5, 2, 4, 8, 1, 3]
tab.sort()
print(tab)
