# procedimentos y funciones
def OrdenaMM(x,y,z):
    if x<y:
        if y<z:
            return(x,y,z)
        else:
            if x<z:
                return(x,z,y)
            else:
                return(z,x,y)
    else:
        if y>z:
            return(z,y,x)
        else:
            if x<z:
                return(y,x,z)
            else:
                return(y,z,x)

# Programa principal para ordenar tres  numeros
numA= int (input("Introduzca el primer numero   "))
numB= int (input("Introduzca el segundo numero   "))
numC= int (input("Introduzca el tercer numero   "))
a,b,c= OrdenaMM(numA, numB, numC)
print ("Los numeros en forma acsendente son:", a,b,c)
d= int (input("Introduzca el primer numero   "))
f= int (input("Introduzca el segundo numero   "))
g= int (input("Introduzca el tercer numero   "))
a,b,c= OrdenaMM(d, f, g)
print ("Los numeros en forma acsendente son:", a,b,c)
