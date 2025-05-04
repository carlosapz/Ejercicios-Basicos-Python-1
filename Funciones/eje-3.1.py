import os
os.system("cls")
# procedomentos y funciones
def primerdig(n):
    while n>10 :
        n=n//10
    return (n)  
def cantidaddig(n):
    c=0
    while n>0 :
        n=n//10
        c=c+1
    return (c) 
def EliminaPrimerDig(n):
    i=0
    c=0
    while n>10 :
        d=n % 10
        n=n//10
        i=i+(d * (10**c))
        c=c+1
    return (i) 

# Programa principal 
num1 = int (input("Introduzca el primer numero: "))
num2 = int (input("Introduzca el segundo numero: "))
pdn1=primerdig(num1)
pdn2=primerdig(num2)
cdn1=cantidaddig(num1)-1
cdn2=cantidaddig(num2)-1
edn1=EliminaPrimerDig(num1)
edn2=EliminaPrimerDig(num2)
nnum1=pdn2*(10**edn1)
nnum2=pdn1*(10**edn2)
print("El primer numero con digito cambiado es: ",nnum1)    
print("El segundo numero con digito cambiado es: ",nnum2)     