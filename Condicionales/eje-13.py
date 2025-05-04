import os
os.system("cls")
a = int(input("Introduzca el 1er digito: "))
b = int(input("Introduzca el 2do digito: "))
c = int(input("Introduzca el 3er digito: "))
if a<=b and b<=c:
	print("De menor a mayor es",a,", ",b,", ",c)
else:
	if a<=c and c<=b:
		print("De menor a mayor es ",a,", ",c,", ",b)
	else:
		if b<=a and a<=c:
			print("De menor a mayor es ",b,", ",c,", ",a)
		else:
			if c<=a and a<=b:
				print("De menor a mayor es ",c,", ",a,", ",b)
			else:
				print("De menor a mayor es ",c,", ",b,", ",a)
