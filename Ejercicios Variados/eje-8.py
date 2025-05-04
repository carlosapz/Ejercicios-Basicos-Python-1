import os
os.system("cls")
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))
if a>0 and b>0:
	maximo = 1
	x = 1
	while x<=a:
		if a%x==0 and b%x==0:
			if x>maximo:
				maximo = x
		x = x+1
	print("El maximo comun divisor es: ",maximo)
else:
	print("Debes ingresar numeros mayores a cero")