import os
os.system("cls")
n = int(input("Ingresa un numero: "))
num = 0
while n>0:
	num = num+1
	x = 1
	contador = 0
	while x<=num:
		if num%x==0:
			contador = contador+1
		x = x+1
	if contador==2:
		print("El numero ",num," es primo")
		n = n-1