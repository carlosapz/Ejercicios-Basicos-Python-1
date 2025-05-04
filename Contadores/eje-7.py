import os
os.system("cls")
n=int(input("Introduzca la cantidad de la serie: "))
Aux=n
for i in range(0,n,1 ):
    i=i+1
    print(i, end=" ")
for i in range(n-1):
    print (Aux, end=" ")
    Aux=Aux-1