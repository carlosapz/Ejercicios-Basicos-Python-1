import os
os.system("cls")
n = int(input("Ingrese un numero:  "))
while (True):
	if n%2==0:
		n = n/2
	else:
		n = (n*3)+1
	print(n)
	if n==1: break