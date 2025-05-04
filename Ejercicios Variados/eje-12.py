import os
os.system("cls")
dp=0
cd=-1
x=0
i=0
k=0
y=0
cni=0
l=0
p=0
n=int(input("Introduzca un numero: "))
i=n
while (0<n):
    x=n%10
    n=n//10
    cd=cd+1
    if (x%2==0):
      k=x*(10**(cd))
      y=y+k
    else:
        cni=cni+1 
        p=x*(10**(cni-1))
        l=l+p
print("El nuevo numero es : ",l)