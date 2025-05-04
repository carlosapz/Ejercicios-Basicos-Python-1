import os, pyautogui, webbrowser
from types import new_class
os.system("cls")
from time import sleep

lista=[59167333782,59160030845,59176509431]

def envia(telefono,archivo):
    webbrowser.open(f'https://web.whatsapp.com/send?phone={telefono}')
    sleep(10)    
    with open(archivo,'r') as Texto:
         for Txt in Texto:
            pyautogui.typewrite(Txt)
            pyautogui.press("enter")
    sleep(10)    

def enviarMensajeAunContacto(telefono,archivo):
    telefono=int(input("Introduzca un telefono [con prefijo 591 sin espacio]"))
    archivo=input("Introduzca el nombre del archivo: ")
    webbrowser.open(f'https://web.whatsapp.com/send?phone={telefono}')
    sleep(10)    
    with open(archivo,'r') as Texto:
         for Txt in Texto:
            pyautogui.typewrite(Txt)
            pyautogui.press("enter")
    sleep(10)    

def enviarMensajeALista(archivo):
    archivo=input("Introduzca el nombre del archivo: ")
    for telefonos in lista:
        envia(telefonos,archivo)

def adicionTelefono():
    fono=int(input("Introduzca un telefono [con prefijo 591 sin espacio]"))
    archivo=input("Introduzca el nombre del archivo: ")
    lista.append(fono)
    for telefonos in lista:
        envia(telefonos,archivo)

def MenuPrincipal():
    while(True):
     print("|------------------------------------------------------------|")
     print("|                     DIGITE UNA OPCION:                     |")
     print("|------------------------------------------------------------|")
     print("|    1.- Enviar los mensajes a toda la lista                 |")
     print("|    2.- Enviar el mensaje a un solo contacto                |")
     print("|    3.- Adicionar un numero a la lista y enviar los mensajes|")
     print("|    4.- Salir del programa                                  |")
     print("|------------------------------------------------------------|")
     opcion=int(input("Digite su opcion:  "))
     if(opcion==1):
         enviarMensajeALista(archivo=int)
         print("Desea Volver al Menu (digite 1) o desea terminar el programa (digite 2)")
         p1=int(input("opcion: "))
         if(p1==2):
           print("Hasta luego")
           break
     if(opcion==2):
         enviarMensajeAunContacto(telefono=int,archivo=int)
         print("Desea Volver al Menu (digite 1) o desea terminar el programa (digite 2)")
         p1=int(input("opcion: "))
         if(p1==2):
            print("Hasta luego")
            break
     if(opcion==3):
         adicionTelefono()
         print("Desea Volver al Menu (digite 1) o desea terminar el programa (digite 2)")
         p1=int(input("opcion: "))
         if(p1==2):
            print("Hasta luego")
            break
     if(opcion==4):
        print("Hasta Pronto")
        break

MenuPrincipal()