import os.path
import datetime
path1=input("entrez le nom du premier fichier :")
path2=input("entrez le nom du deuxième fichier :")
print("la taille du du premier fichier :",os.path.getsize(path1),"octets")
print("la taille du deuxième fichier :",os.path.getsize(path2),"octets")

if os.path.isfile(path1) and os.path.isfile(path2):
   if datetime.datetime.fromtimestamp(os.path.getmtime(path1)) > datetime.datetime.fromtimestamp(os.path.getmtime(path2)):
       print(f"le fichier modifié le plus récemment est le fichier 1")
       print("sa date de creation est :", datetime.datetime.fromtimestamp(os.path.getmtime(path1)))
   else:
       print(f"le fichier modifié le plus récemment est le fichier 2")
       print("sa date de creation est :", datetime.datetime.fromtimestamp(os.path.getmtime(path2)))


