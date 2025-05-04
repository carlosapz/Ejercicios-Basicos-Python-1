import os
os.system("cls")
def Preg1 (n):
    while True:
        n>100
        break
    may=0
    men=9
    while (n>0):
        x=n%10
        if x>may:
            may=x
        if x<men:
            men=x
        n=n//10
    nf=(may*10)+men
    return(nf)

def Preg2 (n):
    
    while (True):
        m=int(input())
        m<10
        break
    cn=0
    while n>0:
        x=n%10
        if(x==m):
            cn=cn+1
        n=(n//10)
        return(cn)

def Preg3 (n):
    may=0
    n=int(input())
    a=n
    while(n>0):
        x=n%10
        if(x>may):
            may=x
        n=n//10
    n2=0
    i=0
    while(a!=0):
        d=a%10
        a=a//10
        if (d!=may):
            n2=n2+d*int(10**i)
            i=i+1
            return(n2)

while(True):            
 print("-------------------------------------------------")
 print("               ¿Que opcion quiere?               ")
 print("-------------------------------------------------")
 print("1.-Nuevo numero segun el mayor y menor           ")
 print("2.-Cuantas veces se repite un numero             ")
 print("3.-Dado un numero N eliminar el dígito más grande")
 print("4.-Salir                                         ")
 print("-------------------------------------------------")
 op=int(input("opcion: "))
 if(op==1):
     Preg1()
     print("Desea Volver al Menu (digite 1) o desea terminar el programa (digite 2)")
     p1=int(input("opcion: "))
     if(p1==2):
        print("Hasta luego")
        break
 if(op==2):
     Preg2()
     print("Desea Volver al Menu (digite 1) o desea terminar el programa (digite 2)")
     p1=int(input("opcion: "))
     if(p1==2):
        print("Hasta luego")
        break   
 if(op==3):
     Preg3()
     print("Desea Volver al Menu (digite 1) o desea terminar el programa (digite 2)")
     p1=int(input("opcion: "))
     if(p1==2):
        print("Hasta luego")
        break   
 if(op==4):
     print("Hasta Pronto")
     break