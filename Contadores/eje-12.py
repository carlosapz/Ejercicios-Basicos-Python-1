import os
os.system ("cls")
print ("Serie")
n= int (input("Introduzca un número  :   "))
for i in range(1,n+1, 1):
    for j in range (1,i+1 ,1):
        print (j,  "  " , end="")
    print ("\n")       
print ("\n\n\n")
