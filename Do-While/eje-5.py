import os
os.system ("cls")
digMayor=0
n= int (input("Introduzca un número:   "))
while n>0:
    dig=n % 10
    n= n//10
    if dig> digMayor:
        digMayor=dig
print ("El digito mayor es ", digMayor)
