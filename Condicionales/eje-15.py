import math
a = int(input("Ingrese el valor de a:"))
b = int(input("Ingrese el valor de b:"))
c = int(input("Ingrese el valor de c:"))
if a==0:
	print("Error no se puede dividir por cero")
else:
	rp1 = (4*a*c)
	rp = (b**2)
	if rp<rp1:
		print("No existe raiz negativa")
	else:
		rp2 = math.sqrt(rp-rp1)
		if a==0:
			print("Error no se puede dividir por cero")
		else:
			xuno = (-b+rp2)/(2*a)
			xdos = (-b-rp2)/(2*a)
			print("El valor de x1 es ",xuno)
			print("El valor de x2 es ",xdos)