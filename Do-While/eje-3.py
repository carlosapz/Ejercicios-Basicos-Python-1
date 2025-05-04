import os
os.system("cls")
n=int(input("Introduzca un numero: "))
m=n
while n>0:
    Aux=n%10
    n=n//10
print("El primer digito de ",m," es de: ",Aux)    