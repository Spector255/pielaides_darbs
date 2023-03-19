from tkinter import *
from tkinter import messagebox
from multiplayer import pamatprogramma

# ================== FUNCTIONS ==================

def kopsavilkums(): #datu sanemsana
    global ranswer, epl1, epl2
    ranswer = option_R.get()
    epl1 = PL1Entry.get()
    epl2 = PL2Entry.get()
    root.destroy()
    pamatprogramma(ranswer, epl1, epl2)

# ==================== MAIN ====================

def Multiizvelne(): #izveidojam logu
    global root, option_R, PL1Entry, PL2Entry

    root = Tk()
    root.title("Information about players")
    root.geometry("350x300")

    Virsrakts = Label(root, text="Aizpildiet informāciju par spēlētājiem:", fg="red")
    Virsrakts.place(x=70, y=25)

    InfoPL1 = Label(root, text="Pirmā spēlētāja vārds:")
    InfoPL1.place(x=20, y=75)

    InfoPL2 = Label(root, text="Otrā spēlētāja vārds:")
    InfoPL2.place(x=20, y=100)

    PL1Entry = Entry(root)
    PL2Entry = Entry(root)

    PL1Entry.place(x=150, y=75)
    PL2Entry.place(x=145, y=100)

    Poga = Button(root, text="Turpināt", command=kopsavilkums)
    Poga.place(x=140, y=200)

    root.mainloop()