nom1=input("nom 1:")
prenom1=input("prenom 1:")
nom2=input("nom 2:")
prenom2=input("prenom 2:")

if nom1 < nom2:
    print(str.upper(nom1),str.capitalize(prenom1))
    print(str.upper(nom2), str.capitalize(prenom2))
elif nom1 > nom2:
    print(str.upper(nom2), str.capitalize(prenom2))
    print(str.upper(nom1), str.capitalize(prenom1))
elif nom1 ==nom2:
    if prenom1 < prenom2:
        print(str.upper(nom1), str.capitalize(prenom1))
        print(str.upper(nom2), str.capitalize(prenom2))
    else :
        print(str.upper(nom2), str.capitalize(prenom2))
        print(str.upper(nom1), str.capitalize(prenom1))


