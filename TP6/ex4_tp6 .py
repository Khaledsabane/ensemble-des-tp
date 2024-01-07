import random
tab=[]
def generer (nbr,vmin,vmax):
    for i in range(nbr):
        tab.append(random.randint(vmin,vmax))
    return tab
def combienInferieur(table, vseuil=30):
    cpt=0
    for i in table:
        if i<vseuil:
            cpt+=1
    return cpt

nb = int(input(f"preciser le nombre de valeur à générer :"))
val_min = int(input(f"preciser la valeur min :"))
val_max = int(input(f"preciser la valeur max :"))
bool=input("vous voulez préciser le seuil ?")





tab = generer(nb,val_min, val_max)
total=0

if bool=="Oui" or bool=="O" or bool=="o":
    seuil=int(input(f"preciser le seuil :"))
    total = combienInferieur(tab, seuil)
elif bool=="Non" or bool=="N" or bool=="n":
    total = combienInferieur(tab)
    seuil=30
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab.sort()
print(tab)


print(f"Il y en a {total} inférieurs à {seuil}")