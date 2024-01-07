somme =0
moyenne=0
coeff=0
bool=0
for i in range(1,6):
    S1=input(f"Veuillez entrer la note du module {i} et le coefficient correspondant :" )
    S2=S1.split(" ")
    S3=S2[0]
    S4=S2[1]
    if float(S2[0]) < 8:
        bool=1
    coeff+=float(S2[1])
    somme+=(float(S2[0])*float(S2[1]))
moyenne=somme/coeff
if moyenne>10 :
    if bool==0:
        print(f"admis avec une moyenne de : {moyenne}")
    else:
        print(f"etudiant n'est pas admis ")
else:
    print(f"etudiqnt n'est pas admis ")





