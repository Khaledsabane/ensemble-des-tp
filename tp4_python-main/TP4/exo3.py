nMax=3
v1=[]
v2=[]
somme=0.0
n=int(input("entrez le nombre n : "))
while n<1 or n>nMax:
    n=int(input("entrez le nombre n : "))
print("Saisie du premier vecteur :")
for i in range(0, n):
    v1.append(int(input(f" V1[{i}] = ")))
print("Saisie du second vecteur :")
for i in range(0, n):
    v2.append(int(input(f" V2[{i}] = ")))
for i in range(0, n):
    produit=v1[i]*v2[i]
    somme+=produit
print("Le produit scalaire de v1 par v2 vaut", somme)