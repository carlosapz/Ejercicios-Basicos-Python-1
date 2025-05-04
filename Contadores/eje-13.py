import os
os.system ("cls")
print ("Serie")
n= int (input("Introduzca un número  :   "))
for i in range(1,n+1, 1):
    for k in range (1, n-i+1):
        print (end=" ")
    for j in range (1,i+1 ,1):
        print ( "  ",i , end="")
    print ("\n")       
print ("\n\n\n")
