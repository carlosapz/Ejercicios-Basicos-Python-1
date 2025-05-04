import os
os.system("cls")
n= int (input("Introduzca la dimencion de la lista  "))
lista=[None]*(n)
for i in range(n):
    dato= int (input(" lista ="))
    lista[i]= dato
for x in lista:
    print(x)
