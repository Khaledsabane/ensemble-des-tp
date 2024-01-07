nb=int(input("Donnez le nombre d'etudiants : "))
moyenne=0.0;
notes=[]
somme=0

for i in range(0,nb):
    etu = int(input(f"note etudiant  {i} : "))
    if etu<0 or etu>20:
        etu = int(input(f"note etudiant  {i} : "))
    notes.append(etu)
    somme+=etu
moyenne=somme/nb
print("la moyenne de classe est : ",moyenne)

print(f"Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(0,nb):
    print(f"{i}  |  {notes[i]}  | {notes[i]-moyenne}")


