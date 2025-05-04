# operaciones con dos numeros
import os
while(True):
    os.system ("cls")
    print("Operaciones")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Division")
    op= int (input ("Digite una opcion....."))
    a= int (input ("Digite un valor....."))
    b= int (input ("Digite otro valor....."))
    if op==1:
       	res=a+b        
    if op==2:
    	res=a-b     
    if op==3:
        res=a*b
    if op==4:
        res=a/b
    print("El resultado es: ", res)
    continuar= input("Desea continuar S/N....");
    if continuar=='N'or continuar=='n':
        break
