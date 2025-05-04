import os
os.system("cls")
n=int(input("Introduzca un numero: "))
cnt=0
for i in range(n+1):
    n=(n-(n%10))/10
    cnt=cnt+1
    if(n==0):
        break
print("La cantidad de digitos es: ",cnt)    