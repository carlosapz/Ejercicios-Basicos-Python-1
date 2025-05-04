import os
os.system("cls")
# procedomentos y funciones
def primerdig(n):
    c=0
    i=0
    while n>10 :
        d=n % 10
        n=n//10
        i=i+(d * (10**c))
        c=c+1
    return (n, c, i)  
# Programa principal 
num1= int (input("Introduzca un numero   "))
num2= int (input("Introduzca un numero   "))
pdn1, cdn1, edn1=primerdig (num1)
pdn2, cdn2, edn2=primerdig (num2)
nnum1=(pdn2*(10**cdn1))+edn1
print ("El primer dígito es ", nnum1)
nnum2=(pdn1*(10**cdn2))+edn2
print ("El primer dígito es ", nnum2)
