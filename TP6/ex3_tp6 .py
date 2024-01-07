# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst
print(f"{ajouter_elt()} {id(ajouter_elt())}")
print(f"{ajouter_elt()} {id(ajouter_elt())}")
print(f"{ajouter_elt()} {id(ajouter_elt())}")

def  ajouter_carac (ch="abc", elt="d"):
    return ch+elt
print(f"{ajouter_carac()} {id(ajouter_carac())}")
print(f"{ajouter_carac()} {id(ajouter_carac())}")
print(f"{ajouter_carac()} {id(ajouter_carac())}")
#on deduit que l'id ne change pas ce qui signifie que c'est la même liste qui a été utilisée