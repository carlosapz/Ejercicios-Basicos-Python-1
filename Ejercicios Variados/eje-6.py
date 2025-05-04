import os
os.system("cls")
aux = 0
a = int(input("Introduzca el primer numero: "))
b = int(input("Introduzca el segundo numero: "))
if a>b:
	while (True):
		a = a-b
		if a<b: 
			break
	print("El modulo es: ",a)
else:
	while (True):
		b = b-a
		if b<a: 
			break
	print("El modulo es: ",b)