def CantidadDig(n):
    c=0
    while n>0 :
        c=c+1
        n=n//10
    return (c)  
# Programa principal para hallar la cantidad de digitos de un numero
num= int (input("Introduzca un numero   "))
print ("La cantidad de digitos es ", CantidadDig(num))
num1= int (input("Introduzca un numero   "))
ca=CantidadDig(num1)
print (ca)