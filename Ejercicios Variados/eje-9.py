import os
os.system("cls")
cont = 0
a = int(input("Introduzca el primer numero: "))
b = int(input("Introduzca el segundo numero: "))
while (True):
	a = a-b
	cont = cont+1
	if a<b: 
		break
print(cont)