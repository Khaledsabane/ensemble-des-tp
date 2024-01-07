somme=int(input("Donner la somme :"))
b100= somme//100
somme%=100
b50=somme//50
somme%=50
b10=somme//10
somme%=10
b2=somme//2
somme%=2
b1=somme
print(f"cela équivaut à {b100} billets de 100, {b50}  billets de 50, {b10} billets de 10, {b2} billets de 2 et {b1} bollets de 1")
