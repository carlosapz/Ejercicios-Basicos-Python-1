import os
os.system("cls")
n=int(input("Introduzca un numero: "))
m=n
while n>9:
    SegDig=n%10
    n=(n-(n%10))//10
print("El segundo digito de ",m," es: ",SegDig)    