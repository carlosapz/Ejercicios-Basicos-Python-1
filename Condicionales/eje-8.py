import os
os.system("cls")
num1=int(input("Introduzca un numero: "))
num2=int(input("Introduzca un numero: "))
if num1 >num2:
    r=num1-num2
    print(num1," - ",num2," = ", r) 
else:
    r=num2-num1
    print(num2," - ",num1," = ", r)    