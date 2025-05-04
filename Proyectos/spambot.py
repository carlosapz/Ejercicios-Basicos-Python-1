import os,pyautogui,time
os.system("cls")

time.sleep(10)

himno=open("aviso.txt","r")

for line in himno:
    pyautogui.typewrite(line)
    pyautogui.press("enter")