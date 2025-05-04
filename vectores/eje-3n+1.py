import os
os.system("cls")
x=int(input("Introduzca un numero: "))
while (x>1):
    print(x)
    if(x % 2 == 0):
        x=x/2
    else:
        x=(x*3)+1
print (x)             
