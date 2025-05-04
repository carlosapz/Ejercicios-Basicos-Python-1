import os
os.system("cls")
digmenor=0
n=int(input("Introduzca un numero: "))
while n>0:
    dig=n%10
    n=n//10
    if dig<digmenor:
        Digmen=dig
print("El digito menor es ",digmenor)        
