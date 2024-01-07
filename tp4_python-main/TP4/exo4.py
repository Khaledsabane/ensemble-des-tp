L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
L2=[]
element=0
freq=0
for i in range(0, len(L1)):
    compteur = 1
    for j in range(i+1, len(L1)):
        if L1[i]==L1[j]:
            compteur+=1
    L2.append(compteur)
    if compteur>freq:
        freq=compteur
        element=L1[i]

print("l’élément apparaissant le plus fréquemment dans une listeest :", element)
print("avec une frequence de:x", freq)

#Partie 2:
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
element=0
freq=0
for i in range(0, len(L1)):
    compteur=L1.count(L1[i])
    if compteur>freq:
        freq=compteur
        element=L1[i]

print("l’élément apparaissant le plus fréquemment dans une listeest :", element)
print("avec une frequence de:x", freq)
























""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /








"** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
