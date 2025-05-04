#Funcion Primer Digito
def PrimDig(n):
 while n>0:
    Aux=n%10
    n=n//10
 return (Aux)

def CantidadDig(n):
    c=0
    while n>0 :
        c=c+1
        n=n//10
    return (c)

# Proceso 
a=int(input("Introduzca el primer numero: "))
a1=PrimDig(a)
b=int(input("Introduzca el segundo numero: "))
b1=PrimDig(b)
res1=a1-b1
print("la resultante es",res1)