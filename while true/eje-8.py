import os
os.system ("cls")
while(True):
    print("Menu:")
    print ("1. Mostrar la cantidad de digitos que tiene")
    print ("2. Mostrar el ultimo digito")
    print ("3. Mostrar el primer digito")
    op=int (input ("Digite una opcion....."))
    n=int (input ("Digite un valor....."))
    c=0
    m=n
    if op==1:
       while n>0:
        n=n//10
        c=c+1
        print ("la cantidad de digitos que tiene son: ", c)	     
    if op==3:
        Aux=n%10
         n=n//10
         print("El primer digito de ",m," es de: ",Aux)  
         continuar= input("Desea continuar S/N....");
    if continuar=='N'or continuar=='n':
     break