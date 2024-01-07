x=float(input("Vous cherchez la table de multiplication de quel nombre ? :"))
produit=1
L=[]
for i in range(0, 10):
    L.append(x*float(i))

    print(x,"*",i,"=",round(L[i],2))
