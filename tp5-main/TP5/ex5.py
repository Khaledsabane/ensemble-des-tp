nbr=int(input("entrer le nombre d'heures :"))
sh=int(input("entrer le salaire horaire :"))
if nbr < 160 :
    s=nbr*160
elif nbr>200:
    nbr=nbr-200
    s=160*sh+sh*1.5*nbr+sh*1.25*40
elif nbr>160 and nbr<=200 :
    nbr-=160
    s=160*sh+sh*1.25*nbr
print(f"le salaire est: {s}")
