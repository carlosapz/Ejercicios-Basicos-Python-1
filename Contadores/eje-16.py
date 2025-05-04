import os
os.system("cls")
m = int(input("Introduzca un digito entre el 10 al 99: "))
n = int(input("Introduzca un digito entre el 10 al 99: "))
m1 = int(m/10)
n1 = int(n/10)
if m1>n1:
	print("El primer digito mayor es ",m1)
else:
	print("El primer digito mayor es ",n1)