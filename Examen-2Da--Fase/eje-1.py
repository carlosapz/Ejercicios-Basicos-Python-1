import os
os.system("cls")
while (True):
	n = int(input("Introduzca un numero mayor a 100: "))
	if n>=100: 
		break
may = 0
men = 9
while n>0:
	x = n%10
	if x>may:
		may = x
	if x<men:
		men = x
	n = (n//10)
nf = (may*10)+men
print("El numero conformado por el mayor y el manor es de ",nf)