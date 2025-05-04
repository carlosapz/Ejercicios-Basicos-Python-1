import os
os.system("cls")
ususario="diegorojas"
contraseña="13579"
intentos=3
while(intentos>0):
    u=input("Introduzca su usuario: ")
    c=input("Introduzca su contraseña: ")
    if((u==ususario)and(c==contraseña)):
        print("Ha iniciado sesion correctamente")
        break
    else:
        intentos=intentos-1
        print("Ha introducido los datos (Ususario/contraseña) de forma incorrecta")
        print("Le quedan ",intentos,"intentos")