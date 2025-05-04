import os
os.system("cls")
may=0
n = int(input("Ingrese un numero: "))
a = n
while n>0:
	x = n%10
	if x>may:
		may = x
	n = (n//10)
n2 = 0
i = 0
while a!=0:
	d = a%10
	a = (a//10)
	if d!=may:
		n2 = n2+d*int(10**i)
		i = i+1
print("El numero sin el digito mayor es ",n2)