import os
print("Здарствуйте, Drapliks")
print("Список команд:")
print("1.clc - Запускает калькулятор.")
print("2.ff - Запускает браузер.")
print("3.mnp - Запускает базовые программы.")
print("4.pof - Выключить компьютер.")
def clc():
    print(">>"+str(eval(input(">>"))))
def mainProgs():
    os.startfile(r'C:/Users/Drapliks/AppData/Roaming/Telegram Desktop/Telegram.exe')
    os.startfile(r'C:/Users/Drapliks/AppData/Local/Programs/YandexMusic/Яндекс Музыка.exe')
    os.startfile(r"C:/Users/Drapliks/qa.exe")
def poweroff():
    os.startfile(r"C:/Windows/System32/SlideToShutDown.exe")
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
    if cmd == "pof":
        print("Выполняю...")
        poweroff()
    if cmd == "ff":
        print("Выполняю...")
        ff()
