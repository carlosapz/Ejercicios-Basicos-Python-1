import os
os.system("cls")
alum=int(input("Introduzca cuantos alumnos hay: "))
sillas=int(input("Introduzca cuantas sillas estan disponibles: "))
if alum>sillas:
    sf=alum-sillas
    print("Las sillas que faltan para los alumnos son: ",sf)
else:
    print("Todos los alumnos tienen sillas")    