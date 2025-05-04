import os
os.system("cls")
sum=0
n=int(input("Introduzca un numero: "))
m=n
while n>0:
    x=n%10
    sum=sum+x
    n=n//10
print("La suma de los digitos de: ",m," es de : ",sum)   