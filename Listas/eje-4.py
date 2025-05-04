import os
os.system("cls")
n=int(input("Cual es el tamaño del vector: "))
vec=[None]*(n)
for i in range(n):
    x=int(input("Introduzca un numero para el vector: "))
    vec[i]=x
Aux=vec[0]
vec[0]=vec[n-1]
vec[n-1]=Aux 
for i in range(0,n):
    print(vec[i],end=" ") 
print(" ")      