lst1=[0, 1, 2]
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
lst2= ajouter_elt(lst1,len(lst1))
print(f"la liste 1: {lst1} {type(lst1)} {id(lst1)}")
print(f"la liste 2 : {lst2} {type(lst2)} {id(lst2)}")

