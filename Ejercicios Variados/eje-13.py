import os
os.system("cls")
n=int(input("Introduzca la hora inicial: "))
m=int(input("Introduzca los minutos iniciales: "))
c=0
for x in range(n,n+1):
    for y in range (m,60,):
        for z in range (0,60,):
            if c<100:
                print(x,":",y,":",z)
                c=c+1
        m=0        
