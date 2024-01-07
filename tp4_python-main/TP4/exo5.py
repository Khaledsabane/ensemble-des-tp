T=[3,0,0,3,0,0,0,0]
jour =T[0] * 10 + T[1]
mois = T[2] * 10 + T[3]
annee = T[4] * 1000 + T[5] * 100 + T[6]*10 + T[7]
Vrai=0
if 0 < annee and annee <= 9999:
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois==12:
        if 1 <= jour and jour <= 31:
            print("date correcte")
            Vrai=1
    else:
        if mois == 2:
            if ((annee%4 == 0 and annee%100 != 0) or annee%400 == 0):
                if 1 <= jour and jour <= 29:
                    print("date correcte")
                    Vrai = 1

            else:
                if 1 <= jour and jour <= 28:
                    print("date correcte")
                    Vrai==1
        else:
            if 1 <= jour and jour <= 30:
                print("date correcte")
                Vrai==1
if Vrai==0:
    print("date incorrecte")


