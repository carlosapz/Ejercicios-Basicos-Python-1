import os
os.system("cls")
edad = int(input("Introduzca su edad: "))
genero = int(input("Introduzca su genero:(F=1/M=0): "))
if genero==1:
	if edad>=60:
		print ("Usted se puede jubilar")
	else:
		print ("Aun no puede jubilarse")
else:
	if edad>=65:
		print ("Usted puede jubilarse")
	else:
		print ("aun le falta edad para jubilarse")
