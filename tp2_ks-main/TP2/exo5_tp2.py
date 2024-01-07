print('entrez un nombre:')
nombre=input()
nombre=int(nombre)
if nombre > 0:
    print('le nombre est postif', nombre)
elif nombre < 0:
    print('le nombre est négatif', nombre)
else:
    print('le nombre est égale à zéro')

if nombre %2==0 :
    print('le nombre est  pair')
else:
    print('le nombre est  impair')

