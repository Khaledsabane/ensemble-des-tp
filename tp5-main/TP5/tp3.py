bool=0
chaine=input("entrez une chaine de caractere :")
phrase_alpha=''


for k in chaine:
    if k.isalpha():
        phrase_alpha+=k.lower()

for i in range(len(phrase_alpha)//2):
    if phrase_alpha[i]!=phrase_alpha[-i-1]:
        bool=1

if bool==1:
    print("programme non palindrome")
else:
    print("programme palindrome")


