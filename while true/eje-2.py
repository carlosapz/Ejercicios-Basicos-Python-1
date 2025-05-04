# leer la edad de una persona
import os
os.system ("cls")
while(True):
    edad= int (input("Introduzca su edad:   "))
    if( edad>0 and edad<100):
        break
    else:
        print ("La edad es incorrecta, introduzca un dato entre 0 y 100 ")
print ("Edad Correcta !!")