import os
os.system("cls")

x=int(input("Introduzca un numero: "))
y=int(input("Introduzca un numero: "))
if x>0 and y>0:
    print("El punto (",x,",",y,") esta en el plano I")
else:
   if x<0 and y>0:
        print("El punto (",x,",",y,") esta en el plano II")
   else:
       if x<0 and y<0:
            print("El punto (",x,",",y,") esta en el plano III")
       else:
           print("El punto (",x,",",y,") esta en el plano IV")
