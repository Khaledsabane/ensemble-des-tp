taille=0
compt=0
T=input("entre la chaine de  caractere:")
for i in T:
    taille+=1
print(taille)

for i in T:
    if i=='a' or i=='e' or i=='u' or i=='y' or i=='o' or i=='i':
          compt+=1
print(f"le pourcentage de voyelle est: {(compt/taille)*100} %")


occu=-1
i=0
T1="wagon"
taille1=0
for k in T1:
    taille1+=1

while i<taille-taille1+1 and occu==-1 :
    j=0

    while j < taille1 and T[i+j]==T1[j] :
        j+=1
    if j==taille1:
        occu=i

    else:
        i+=1
print(f"le debut de la premiere est : {occu}")


i=0
T1="wagon"
taille1=0
nbr=0
for k in T1:
    taille1+=1

while  i < taille - taille1 + 1:
    j = 0

    while j < taille1 and T[i + j] == T1[j]:
        j += 1

    if j == taille1:
        nbr += 1
        i += taille1
    else:
        i += 1


print(f"le nombre est: {nbr}")
