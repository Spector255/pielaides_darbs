from tkinter import *
from tkinter import messagebox
from info_multi import Multiizvelne
from info_single import Singleizvelne
# ================== FUNCTIONS ==================
def showMulti():
    msg = messagebox.showinfo(title="Multiplayer",
                              message="Ir izvēlēts daudzspēlētāju režims")
    rootmain.destroy()
    Multiizvelne()

def showSingle():
    msg = messagebox.showinfo(title="Singleplayer",
                              message="Ir izvēlēts vienspēlētāja režims")
    msg = messagebox.showwarning(title="Rules",
                              message="Tā kā šajā režīmā Jūs spēlējat ar datoru, nevis ar cilvēku, tad ir mainīti šādi noteikumi: \nJa uzvar dators, tad viņa pēdējais gājiens neliksies laukumā, lai tu meklētu viņa uzvārēs kombināciju un izdarītu darbu pie kļūdām! :) \nTāpat, ja gribēsi spēlēt negodīgi un spiest nevis uz brīvam ailem (pat tad, ja tā ir tava šūna), tad dators to uztvers kā gaitas caurlaidi un automātiski izdarīs nākamo gājienu! \nLabas spēles!")
    rootmain.destroy()
    Singleizvelne()
# ================== MAIN ==================

def izvelne():
    global rootmain
    rootmain = Tk()                 #Izveido pamatlogu 
    rootmain.geometry("350x300")    #Loga izmērs
    rootmain.title("Mode chooser")      #Loga nosaukums

    Single = Button(rootmain,               # Veidojam pogu konkrēta logā 
                    width=20, height=2,  # Pogas izmērs
                    text="Vienspēlētāja",          # Pogas teksts
                    command=showSingle,      # Darbība, kura izpildisies pēc nospiešanas
                    )

    Single.place(x=100, y=125)      # pogas vieta logā

    Multi = Button(rootmain,
                   width=20, height=2,
                   text="Daudzspēlētāju",
                   command=showMulti,
                   )

    Multi.place(x=100, y=175)

    Virsrakts = Label(rootmain,
                     text = "Izvēlieties režīmu, kurā vēlaties spēlēt:",
                     fg = "red")   #Teksta krāsa
    Virsrakts.place(x=70, y=75)

    rootmain.mainloop()
