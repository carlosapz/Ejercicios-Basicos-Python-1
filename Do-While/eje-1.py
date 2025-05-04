import os
os.system ("cls")
c=0
n= int (input("Introduzca un número:   "))
while n>0:
    n=n//10
    c=c+1
print ("la cantidad de digitos es ", c)