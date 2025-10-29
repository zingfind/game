import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def blockstep(key):
    global currentblock
    #print(currentblock)
    #print(key.keysym)
    if currentblock == "NW":
        if key.keysym == "s":
            currentblock = "W"
            print(currentblock)
            wblock()
        elif key.keysym == "d":
            currentblock = "N"
            print(currentblock)
            nblock()
        else:
            pass
    elif currentblock == "N":
        if key.keysym == "a":
            currentblock = "NW"
            print(currentblock)
            nwblock()
        elif key.keysym == "s":
            currentblock = "C"
            print(currentblock)
            cblock()
        elif key.keysym == "d":
            currentblock = "NE"
            print(currentblock)
            neblock()
        else:
            pass
    elif currentblock == "NE":
        if key.keysym == "a":
            currentblock = "N"
            print(currentblock)
            nblock()
        elif key.keysym == "s":
            currentblock = "E"
            print(currentblock)
            eblock()
        else:
            pass
    elif currentblock == "W":
        if key.keysym == "w":
            currentblock = "NW"
            print(currentblock)
            nwblock()
        elif key.keysym == "s":
            currentblock = "SW"
            print(currentblock)
            swblock()
        elif key.keysym == "d":
            currentblock = "C"
            print(currentblock)
            cblock()
        else:
            pass
    elif currentblock == "C":
        if key.keysym == "w":
            currentblock = "N"
            print(currentblock)
            nblock()
        elif key.keysym == "a":
            currentblock = "W"
            print(currentblock)
            wblock()
        elif key.keysym == "s":
            currentblock = "S"
            print(currentblock)
            sblock()
        elif key.keysym == "d":
            currentblock = "E"
            print(currentblock)
            eblock()
        else:
            pass
    elif currentblock == "E":
        if key.keysym == "w":
            currentblock = "NE"
            print(currentblock)
            neblock()
        elif key.keysym == "a":
            currentblock = "C"
            print(currentblock)
            cblock()
        elif key.keysym == "s":
            currentblock = "SE"
            print(currentblock)
            seblock()
        else:
            pass
    elif currentblock == "SW":
        if key.keysym == "w":
            currentblock = "W"
            print(currentblock)
            wblock()
        elif key.keysym == "d":
            currentblock = "S"
            print(currentblock)
            sblock()
        else:
            pass
    elif currentblock == "S":
        if key.keysym == "w":
            currentblock = "C"
            print(currentblock)
            cblock()
        elif key.keysym == "a":
            currentblock = "SW"
            print(currentblock)
            swblock()
        elif key.keysym == "d":
            currentblock = "SE"
            print(currentblock)
            seblock()
        else:
            pass
    elif currentblock == "SE":
        if key.keysym == "w":
            currentblock = "E"
            print(currentblock)
            eblock()
        elif key.keysym == "a":
            currentblock = "S"
            print(currentblock)
            sblock()
        else:
            pass
    else:
        pass

def nwblock():
    print("You're in Northwest Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo1c).grid(row=1,column=0)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Нажать на первую кнопку пульта", width=33, command=remotekey1).grid(row=1,column=0)
    Button(frame2, text="Нажать на вторую кнопку пульта", width=33, command=remotekey2).grid(row=2,column=0)

def remotekey1():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Что-то произошло.").grid(row=0, column=0)

def remotekey2():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Что-то произошло.").grid(row=0, column=0)

def nblock():
    print("You're in North Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo2c).grid(row=1,column=1)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Войти в систему компьютера", width=33, command=computerlogin).grid(row=1,column=0)
    Button(frame2, text="Ударить по компьютеру", width=33, command=hitcomputer).grid(row=2,column=0)

def computerlogin():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Вы успешно зашли в систему").grid(row=0, column=0)

def hitcomputer():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Вы ударили по компьютеру.").grid(row=0, column=0)

def neblock():
    print("You're in North Eastern Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo3c).grid(row=1,column=2)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Открыть дверь бункера", width=33, command=openbunker).grid(row=1,column=0)

def openbunker():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Дверь не открывается.").grid(row=0, column=0)

def wblock():
    print("You're in Western Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo4c).grid(row=2,column=0)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Разобраться в мусоре на полу", width=33, command=picktrash).grid(row=1,column=0)

def picktrash():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Вы нашли пароль от компьютера").grid(row=0, column=0)

def cblock():
    print("You're in Central Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo5c).grid(row=2,column=1)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Поспать", width=33, command=sleepnow).grid(row=1,column=0)

def sleepnow():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Вы проснулись отдохнувшим").grid(row=0, column=0)

def eblock():
    print("You're in East Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo6c).grid(row=2,column=2)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Открыть шкафчики", width=33, command=openlocker).grid(row=1,column=0)
    Button(frame2, text="Потрясти шкафчики", width=33, command=shakelocker).grid(row=2,column=0)

def shakelocker():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Шкафчики сильно шатаются").grid(row=0, column=0)

def openlocker():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Внутри ничего").grid(row=0, column=0)

def swblock():
    print("You're in South Western Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo7c).grid(row=3,column=0)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Заглянуть в цветочный горшок", width=33, command=flowerpot).grid(row=1,column=0)

def flowerpot():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="Вы нашли пистолет").grid(row=0, column=0)

def sblock():
    print("You're in South Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo8c).grid(row=3,column=1)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Choose action").grid(row=0,column=0)
    Button(frame2, text="Look under the carpet", width=33, command=checkcarpet).grid(row=1,column=0)

def checkcarpet():
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text="You got dust all over yourself").grid(row=0, column=0)

def seblock():
    print("You're in South Eastern Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo9c).grid(row=3,column=2)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Заглянуть в цветочный горшок", width=33, command=flowerpot).grid(row=1,column=0)

def resetmap():
    Button(frame1, text = 'button', image = photo1).grid(row=1,column=0)
    Button(frame1, text = 'button', image = photo2).grid(row=1,column=1)
    Button(frame1, text = 'button', image = photo3).grid(row=1,column=2)
    Button(frame1, text = 'button', image = photo4).grid(row=2,column=0)
    Button(frame1, text = 'button', image = photo5).grid(row=2,column=1)
    Button(frame1, text = 'button', image = photo6).grid(row=2,column=2)
    Button(frame1, text = 'button', image = photo7).grid(row=3,column=0)
    Button(frame1, text = 'button', image = photo8).grid(row=3,column=1)
    Button(frame1, text = 'button', image = photo9).grid(row=3,column=2)

def startmap():
    Button(frame1, text = 'button', image = photo1).grid(row=1,column=0)
    Button(frame1, text = 'button', image = photo2).grid(row=1,column=1)
    Button(frame1, text = 'button', image = photo3).grid(row=1,column=2)
    Button(frame1, text = 'button', image = photo4).grid(row=2,column=0)
    Button(frame1, text = 'button', image = photo5c).grid(row=2,column=1)
    Button(frame1, text = 'button', image = photo6).grid(row=2,column=2)
    Button(frame1, text = 'button', image = photo7).grid(row=3,column=0)
    Button(frame1, text = 'button', image = photo8).grid(row=3,column=1)
    Button(frame1, text = 'button', image = photo9).grid(row=3,column=2)
    Label(frame2, text="Выбор действия").grid(row=0,column=0)
    Button(frame2, text="Поспать", width=33, command=sleepnow).grid(row=1,column=0)

root = tk.Tk()

currentblock = "C"

root.bind("<Key>", blockstep)

root.title("Game")
root.minsize(920, 460)
root.maxsize(920, 460)
root.geometry("+100+50")

bg = PhotoImage(file = "background.png")

label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

frame1 = tk.Frame(root, borderwidth=1, relief='ridge')
frame1.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

frame2 = tk.Frame(root, borderwidth=1, relief='ridge')
frame2.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

frame3 = tk.Frame(root, borderwidth=1, relief='ridge')
frame3.grid(row=0, column=2, padx=(20, 20), pady=(20, 20))

#Label(frame3, text="Инвентарь").grid(row=0,column=0)

photo1 = PhotoImage(file = r"nwtile.png")
photo2 = PhotoImage(file = r"ntile.png")
photo3 = PhotoImage(file = r"netile.png")
photo4 = PhotoImage(file = r"wtile.png")
photo5 = PhotoImage(file = r"ctile.png")
photo6 = PhotoImage(file = r"etile.png")
photo7 = PhotoImage(file = r"swtile.png")
photo8 = PhotoImage(file = r"stile.png")
photo9 = PhotoImage(file = r"setile.png")

photo1c = PhotoImage(file = r"nwtilecharacter.png")
photo2c = PhotoImage(file = r"ntilecharacter.png")
photo3c = PhotoImage(file = r"netilecharacter.png")
photo4c = PhotoImage(file = r"wtilecharacter.png")
photo5c = PhotoImage(file = r"ctilecharacter.png")
photo6c = PhotoImage(file = r"etilecharacter.png")
photo7c = PhotoImage(file = r"swtilecharacter.png")
photo8c = PhotoImage(file = r"stilecharacter.png")
photo9c = PhotoImage(file = r"setilecharacter.png")

startmap()

root.mainloop()