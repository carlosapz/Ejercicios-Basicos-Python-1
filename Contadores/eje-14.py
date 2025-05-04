import os 
os.system("cls")
n=int(input("Introduzca la cantidad de digitos que quiere:  "))
for i in range (1,n+1,1):
    if i%3==0:
        print(0)
    else:
        if i%3==2:
           print("1")
        else:
            print("0")    
