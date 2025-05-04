import os
os.system("cls")
edad = int(input("Introduzque su edad: "))
if edad>0:
	if edad>=11:
		if edad>=17:
			if edad>=18:
				print("Usted es mayor de edad")
			else:
				print("Usted es un adolecente")
		else:
			print("Usted es un adolecente")
	else:
		print("Usted todavia es un niño")
else:
	print("Error")