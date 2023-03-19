from tkinter import *
from tkinter import messagebox
from singleplayer import single_pamatprogramma

# ================== FUNCTIONS ==================

def kopsavilkums(): #sanemam datus
    global rdefic, epl1
    rdefic = raddif.get()
    epl1 = PLEntry.get()
    
    root.destroy()
    single_pamatprogramma(epl1, rdefic)

# ==================== MAIN ====================

def Singleizvelne(): #izveidojam logu

    global root, raddif, PLEntry

    root = Tk()
    root.title("Information about player")
    root.geometry("350x300")

    Virsrakts = Label(root, text="Aizpildiet informāciju par spēlētāju:", fg="red")
    Virsrakts.place(x=70, y=25)

    InfoPL = Label(root, text="Spēlētāja vārds:")
    InfoPL.place(x=20, y=75)

    PLEntry = Entry(root)
    PLEntry.place(x=130, y=75)

    Teksts_sare = Label(root, text="Izvēlies sarežģītību: ")
    Teksts_sare.place(x=20, y=105)

    raddif = IntVar()

    RadioEAS = Radiobutton(root, text="Easy", variable=raddif, value=1)
    RadioMED = Radiobutton(root, text="Medium", variable=raddif, value=2)
    RadioEAS.place(x=170, y=95)
    RadioMED.place(x=170, y=115)

    Poga = Button(root, text="Turpināt", command=kopsavilkums)
    Poga.place(x=140, y=150)

    root.mainloop()