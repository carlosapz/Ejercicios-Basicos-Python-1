import os
os.system("cls")
n=int(input("Introduzca un numero: "))
cnt=0
while (True):
    n=(n-(n%10))/10
    cnt=cnt+1
    if(n==0):
        break
print("La cantidad de digitos es: ",cnt)    