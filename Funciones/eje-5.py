import os
os.system("cls")
#Procedimiento 
def Validacion(n1,n2):
    valid=0
    if (n1==n2):
        valid=1
    else:
        valid=0
    return(valid)        
#Programa Principal
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))    
a=Validacion(a,b)
b=Validacion(b,c)
c=Validacion(c,a)
a1=Validacion(b,a)
b1=Validacion(c,b)
c1=Validacion(a,c)
if((a==0)&(b==0)&(c==0)&(a1==0)&(b1==0)&(c1==0)):
    print("Son numeros diferentes")
else:
    print("Deben ser 3 numeros diferentes")
