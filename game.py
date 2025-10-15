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

def nblock():
    print("You're in North Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo2c).grid(row=1,column=1)

def neblock():
    print("You're in North Eastern Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo3c).grid(row=1,column=2)

def wblock():
    print("You're in Western Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo4c).grid(row=2,column=0)

def cblock():
    print("You're in Central Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo5c).grid(row=2,column=1)

def eblock():
    print("You're in East Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo6c).grid(row=2,column=2)

def swblock():
    print("You're in South Western Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo7c).grid(row=3,column=0)

def sblock():
    print("You're in South Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo8c).grid(row=3,column=1)

def seblock():
    print("You're in South Eastern Block.")
    resetmap()
    Button(frame1, text = 'button', image = photo9c).grid(row=3,column=2)

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

root = tk.Tk()

currentblock = "C"

root.bind("<Key>", blockstep)

root.title("Пиксельная Фаллаут РПГ")
root.minsize(920, 460)
root.maxsize(920, 460)
root.geometry("+100+50")

bg = PhotoImage(file = "background.png")

# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

frame1 = tk.Frame(root, borderwidth=1, relief='ridge')
frame1.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

frame2 = tk.Frame(root, borderwidth=1, relief='ridge')
frame2.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

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

#I gotta set a background for the whole window as a tiled image.