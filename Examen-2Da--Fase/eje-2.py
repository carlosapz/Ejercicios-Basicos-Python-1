import os
os.system("cls")
n = int(input("Ingrese un numero: "))
a = n
while (True):
	m = int(input("Ingrese un segundo numero de un solo digito: "))
	if m<10: 
		break
cn = 0
while n>0:
	x = n%10
	if x==m:
		cn = cn+1
	n = (n//10)
print("El numero ",m," esta en ",a," ",cn," veces")