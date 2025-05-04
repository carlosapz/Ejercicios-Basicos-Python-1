import os
os.system("cls")
def cantidad(n):
	cantn = 0
	while n>=1:
		n = (n/10)
		cantn = cantn+1
	return cantn
    
n = int(input("Ingrese un numero: "))
b = int(input("Ingrese un segundo numero: "))
m = cantidad(n)
a = cantidad(b)
print("El numero ",n," tiene ",m," digitos")
print("El numero ",b," tiene ",a," digitos")