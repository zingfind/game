import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def block1event():
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="Welcome.").grid(row=10, column=10, padx=(20, 20), pady=(20, 20))
    Button(frame2, text="Open the door.", command=opendoor).grid(row=1,column=0)

def opendoor():
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="You can't open this door, it's locked.").grid(row=10, column=10, padx=(20, 20), pady=(20, 20))

def block4event():
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text="You walked into a corner").grid(row=10, column=10, padx=(20, 20), pady=(20, 20))

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

def nblock():
    print("You're in North Block.")

def neblock():
    print("You're in North Eastern Block.")

def wblock():
    print("You're in Western Block.")

def cblock():
    print("You're in Central Block.")

def eblock():
    print("You're in East Block.")

def swblock():
    print("You're in South Western Block.")

def sblock():
    print("You're in South Block.")

def seblock():
    print("You're in South Eastern Block.")

root = tk.Tk()

currentblock = "C"

root.bind("<Key>", blockstep)

root.title("Fallout Text RPG")
root.minsize(1200, 600)
root.maxsize(1200, 600)
root.geometry("+100+50")


frame1 = tk.Frame(root, borderwidth=1, relief='ridge')
frame1.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

frame2 = tk.Frame(root, borderwidth=1, relief='ridge')
frame2.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

photo1 = PhotoImage(file = r"block1.png") 
Button(frame1, text = 'button', image = photo1, command=block1event).grid(row=1,column=0)

photo2 = PhotoImage(file = r"block2.png") 
Button(frame1, text = 'button', image = photo2).grid(row=1,column=1)
photo3 = PhotoImage(file = r"block3.png") 
Button(frame1, text = 'button', image = photo3).grid(row=1,column=2)
photo4 = PhotoImage(file = r"block4.png") 
Button(frame1, text = 'button', image = photo4, command=block4event).grid(row=1,column=3)
photo5 = PhotoImage(file = r"block5.png")
Button(frame1, text = 'button', image = photo5, command=block4event).grid(row=2,column=0)
photo6 = PhotoImage(file = r"block6.png")
Button(frame1, text = 'button', image = photo6).grid(row=2,column=1)
photo7 = PhotoImage(file = r"block7.png")
Button(frame1, text = 'button', image = photo7).grid(row=2,column=2)
photo8 = PhotoImage(file = r"block8.png")
Button(frame1, text = 'button', image = photo8).grid(row=2,column=3)

root.mainloop()