import os
os.system("cls")
import random
a=random.randrange(1,10)
intentos=3
while (True):
    n=int(input("Introduzca un numero: "))
    if(n>a):
        print("El numero es menor")
    elif(n<a):
        print("El numero es mayor")
    else:
        print("Usted Gano!!! Adivino el numero!!!!")
        break   
    intentos=intentos-1
    if(intentos==0):
        print("Mejor suerte la proxima :)")
        break 