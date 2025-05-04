#Verificar si un numero es capicuo
#Funcion Invertir
def invertir(n):
    f=0
    while n>0:
        c=n%10
        n=n//10
        f=(f*10)+c
    return (f)
# Programa principal 
num=int(input("Introduzca un numero: ")) 
b=invertir(num)
if(b==num):
    print("El numero ",num," es capicua")
else:
    print("El numero ",num," no es capicua")      