print("saisir le nombre des minutes écoulées depuis le début de mois est :")
minutes=input()
minutes=int(minutes)
jourdumois=(minutes//60)//24
print("le jour est {}".format(jourdumois))
