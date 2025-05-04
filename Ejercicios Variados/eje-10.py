import os
os.system("cls")
cn=0
i=1
n=int(input("Introduzca un numero: "))
if(n>1):
  while (i<n):
    i=i+1
    if (n%i==0):
       cn=cn+1
if(cn>2):
  print("El numero no es primo")
else:
  print("El numero es primo")        