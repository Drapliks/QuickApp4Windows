import os
import webbrowser
print("Здарствуйте, Drapliks")
print("Список команд:")
print("1.clc - Запускает калькулятор.")
print("2.ff - Запускает браузер")
print("3.mnp - Запускает базовые программы.")
print("4.devp - Запускает программы для разаработки.")
print("5.alp - Запускает все программы.")
print("6.pof - Выключить компьютер.")
def clc():
    print(">>"+str(eval(input(">>"))))
def mainProgs():
    os.startfile(r'C:/Users/Drapliks/AppData/Roaming/Telegram Desktop/Telegram.exe')
    webbrowser.open("https://music.yandex.ru/")
def devProgs():
    os.startfile(r'C:/Program Files/Unity Hub/Unity Hub.exe')
    os.startfile(r"C:/Users/Drapliks/AppData/Local/Programs/Microsoft VS Code/Code.exe")
def allProg():
    os.startfile(r'C:/Users/Drapliks/AppData/Roaming/Telegram Desktop/Telegram.exe')
    webbrowser.open("https://music.yandex.ru/")
    os.startfile(r'C:/Program Files/Unity Hub/Unity Hub.exe')
    os.startfile(r"C:/Users/Drapliks/AppData/Local/Programs/Microsoft VS Code/Code.exe")
def poweroff():
    os.startfile("C:/Windows/System32/SlideToShutDown.exe")
def ff():
    os.startfile(r"C:/Program Files/Mozilla Firefox/firefox.exe")
while True:
    cmd = input(">")
    if cmd == "clc":
        print("Выполняю...")
        clc()
    if cmd == "mnp":
        print("Выполняю...")
        mainProgs()
    if cmd == "devp":
        print("Выполняю...")
        devProgs()
    if cmd == "alp":
        print("Выполняю...")
        allProg()
    if cmd == "pof":
        print("Выполняю...")
        poweroff()
    if cmd == "ff":
        print("Выполняю...")
        ff()