import os
os.system("cls")
n = int(input("Ingresa cuantos numeros deseas generar"))
x = 1
a = 0
b = 1
for i in range(1,n+1):
	if x%2==1:
		print(a)
		a = a+b
	else:
		print(b)
		b = b+a
	x = x+1