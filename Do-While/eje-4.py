import os
os.system("cls")
cnp=0
cni=0
n=int(input("introduzca un numero: "))
m=n
while n>0:
    x=n%10
    n=n//10
    if x%2==0:
        cnp=cnp+1
    else:
        cni=cni+1

print("La cantidad de digitos pares de ",m," es de: ",cnp)
print("La cantidad de digitos impares de ",m," es de: ",cni)