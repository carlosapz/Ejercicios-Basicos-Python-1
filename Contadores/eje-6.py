import os
os.system("cls")
n = int(input("¿De que numero quieres la tabla?:  "))
m = int(input("¿Cuantos resultados quiere?:  "))
for i in range(1,m+1):
	r = i*n
	print(n,"*",i,"=",r)