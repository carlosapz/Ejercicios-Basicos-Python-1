import os
os.system("cls")
n=int(input("Introduzca la cantidad de elemnetos para la serie :   "))
s=1
for i in range(1,n, 1):
    print(s, "  ", end='')  
    s=s+i
print ("\n\n\n")
