import os
os.system("cls")
while(True):
    n=int(input("Introduzca un numero: "))
    if((n>99)&(n<1000)):
        print("El numero ",n, " tiene 3 cifras")
        break
    elif((n>-99)&(n<-1000)):
         print("El numero ",n, " tiene 3 cifras")