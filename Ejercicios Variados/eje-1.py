import os
os.system("cls")
n=int(input("introduzca un numero: "))
suma=0
m=n
while n>0:
    suma=suma+(n%10)
    n=(n-(n%10))/10
print("La suma de los dijitos de ",m, " es: ",suma)