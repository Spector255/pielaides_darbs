from tkinter import *
from tkinter import messagebox
from random import randint

# ================== FUNCTIONS ==================
def kluda():  #Uzrakstam, ka šūna ir aizņemta
    msg = messagebox.showerror(title="Nav godīgi -_-",
                              message="Šī šūna jau ir aizņemta!")

def cleaning():  #Notīram spēlēs laukumu
    one.config(text = "")
    two.config(text = "")
    three.config(text = "")
    four.config(text = "")
    five.config(text = "")
    six.config(text = "")
    seven.config(text = "")
    eight.config(text = "")
    nine.config(text = "")
    global rutinas
    rutinas=[0,0,0,0,0,0,0,0,0]
    global solis
    solis=0

def statistika():   #izvadam statistiku
    msg = messagebox.showinfo(title="Statistika!",
                              message=f"Statistika kopš programmas palaišanas:\n - {player1} uzvārejis: {Xwin} reizes \n - Dators uzvārejis: {Owin} reizes \n - Neviens neuzvārejis: {XO} reizes \n - Pavisām spēlēs: {Xwin+Owin+XO}")
    
    cleaning()
def finalX():   #Apsveicam spēlētāju
    msg = messagebox.showinfo(title="Apsveicam!",
                              message=f"Apsveicam! Uzvarēja {player1}!")
    statistika()
 
def finalO(): #Paziņojam, ka uzvarēja datoru
    msg = messagebox.showinfo(title=":(",
                              message=f"Uzvarēja dators!")
    statistika()

def final(): #paziņojums par spēlēs beigam
    msg = messagebox.showwarning(title="-_-",
                              message="Neviens nav uzvarējis!")
    statistika()  

def parbaudeX(): #parbaudam, vai ir uzvārējis spēlētājs
    if (rutinas[0] == 1 and rutinas[1] == 1  and rutinas[2] == 1 )  or (rutinas[3] == 1 and rutinas[4] == 1  and rutinas[5] == 1 ) or (rutinas[6] == 1 and rutinas[7] == 1  and rutinas[8] == 1 )or (rutinas[0] == 1 and rutinas[3] == 1  and rutinas[6] == 1 ) or (rutinas[1] == 1 and rutinas[4] == 1  and rutinas[7] == 1 ) or (rutinas[2] == 1 and rutinas[5] == 1  and rutinas[8] == 1 )or (rutinas[2] == 1 and rutinas[4] == 1  and rutinas[6] == 1 )or (rutinas[0] == 1 and rutinas[4] == 1  and rutinas[8] == 1 ):
      global Xwin
      Xwin= Xwin + 1
      finalX()

def parbaudeO(): #parbaudam, vai ir uzvārējis dators
    if (rutinas[0] == 2 and rutinas[1] == 2  and rutinas[2] == 2 ) or (rutinas[3] == 2 and rutinas[4] == 2  and rutinas[5] == 2 ) or (rutinas[6] == 2 and rutinas[7] == 2  and rutinas[8] == 2 )or (rutinas[0] == 2 and rutinas[3] == 2  and rutinas[6] == 2 ) or (rutinas[1] == 2 and rutinas[4] == 2  and rutinas[7] == 2 ) or (rutinas[2] == 2 and rutinas[5] == 2  and rutinas[8] == 2 )or (rutinas[2] == 2 and rutinas[4] == 2  and rutinas[6] == 2 )or (rutinas[0] == 2 and rutinas[4] == 2  and rutinas[8] == 2 ):
      global Owin
      Owin= Owin + 1
      finalO()

def parbaude(): #parbaudam neizškirsto spēli
    if not 0 in rutinas:
        global XO
        XO=XO+1
        final()

def dator(): #datora gājieni
    if 0 in rutinas:
        global rutnumurs
        rutnumurs = 0 
        if dific == 1 or solis<3:
            rutnumurs = randint(0,8)
            while rutinas[rutnumurs] != 0:
                rutnumurs = randint(0,8)
        else:
            if (rutinas[1] and rutinas[2] == 1) or (rutinas[3] and rutinas[6] == 1) or (rutinas[4] and rutinas[8] == 1) or (rutinas[1] and rutinas[2] == 2) or (rutinas[3] and rutinas[6] == 2) or (rutinas[4] and rutinas[8] == 2):
                rutnumurs = 0
            elif (rutinas[0] and rutinas[2] == 1) or (rutinas[4] and rutinas[7] == 1) or (rutinas[0] and rutinas[2] == 2) or (rutinas[4] and rutinas[7] == 2):
                rutnumurs = 1
            elif (rutinas[0] and rutinas[1] == 1) or (rutinas[5] and rutinas[8] == 1) or (rutinas[4] and rutinas[6] == 1) or (rutinas[0] and rutinas[1] == 2) or (rutinas[5] and rutinas[8] == 2) or (rutinas[4] and rutinas[6] == 2):
                rutnumurs = 2
            elif (rutinas[0] and rutinas[6] == 1) or (rutinas[4] and rutinas[5] == 1) or (rutinas[0] and rutinas[6] == 2) or (rutinas[4] and rutinas[5] == 2):
                rutnumurs = 3
            elif (rutinas[3] and rutinas[5] == 1) or (rutinas[1] and rutinas[7] == 1) or (rutinas[2] and rutinas[6] == 1) or (rutinas[0] and rutinas[8] == 1) or (rutinas[3] and rutinas[5] == 2) or (rutinas[1] and rutinas[7] == 2) or (rutinas[2] and rutinas[6] == 2) or (rutinas[0] and rutinas[8] == 2):
                rutnumurs = 4
            elif (rutinas[3] and rutinas[4] == 1) or (rutinas[2] and rutinas[8] == 1) or (rutinas[3] and rutinas[4] == 2) or (rutinas[2] and rutinas[8] == 2):
                rutnumurs = 5
            elif (rutinas[0] and rutinas[3] == 1) or (rutinas[7] and rutinas[8] == 1) or (rutinas[4] and rutinas[2] == 1) or (rutinas[0] and rutinas[3] == 2) or (rutinas[7] and rutinas[8] == 2) or (rutinas[4] and rutinas[2] == 2):
                rutnumurs = 6
            elif (rutinas[8] and rutinas[6] == 1) or (rutinas[4] and rutinas[1] == 1) or (rutinas[8] and rutinas[6] == 2) or (rutinas[4] and rutinas[1] == 2):
                rutnumurs = 7
            elif (rutinas[6] and rutinas[7] == 1) or (rutinas[2] and rutinas[5] == 1) or (rutinas[4] and rutinas[0] == 1) or (rutinas[6] and rutinas[7] == 2) or (rutinas[2] and rutinas[5] == 2) or (rutinas[4] and rutinas[0] == 2):
                rutnumurs = 8
            else:
                while rutinas[rutnumurs] != 0:
                    rutnumurs = randint(0,8)
        if rutinas[rutnumurs] == 0:
            rutinas[rutnumurs] = 2
        else:
            try:
                dator()
            except:
                rutnumurs = rutinas.index(0)
                rutinas[rutnumurs] = 2
        parbaudeX()
        parbaudeO()
        parbaude()   

        if rutnumurs==0:
            one.config(text = "O")
        elif rutnumurs==1:
            two.config(text = "O")
        elif rutnumurs==2:
            three.config(text = "O")
        elif rutnumurs==3:
            four.config(text = "O")
        elif rutnumurs==4:
            five.config(text = "O")
        elif rutnumurs==5:
            six.config(text = "O")
        elif rutnumurs==6:
            seven.config(text = "O")
        elif rutnumurs==7:
            eight.config(text = "O")
        elif rutnumurs==8:
            nine.config(text = "O")
        rutinas[rutnumurs] = 2
    else:
        kluda()
        

def printing(X): #spēlētāja gājieni
    global solis
    if rutinas[X] == 0:
        if X==0:
            one.config(text = "X")
        elif X==1:
            two.config(text = "X")
        elif X==2:
            three.config(text = "X")
        elif X==3:
            four.config(text = "X")
        elif X==4:
            five.config(text = "X")
        elif X==5:
            six.config(text = "X")
        elif X==6:
            seven.config(text = "X")
        elif X==7:
            eight.config(text = "X")
        else:
            nine.config(text = "X")
        rutinas[X] = 1
    else:
        kluda()
    solis=solis+1
    dator()
    solis=solis+1
    parbaudeX()
    parbaudeO()
    parbaude()
    

def single_pamatprogramma(player1name, rdefic): #izveidojam laukumu
    global rutinas, Xwin, Owin, XO, solis, player1, dific
    global one,two,three,four,five,six,seven,eight,nine
    rutinas=[0,0,0,0,0,0,0,0,0]
    solis=0
    Xwin=0
    Owin=0
    XO=0
    player1 = player1name
    dific = rdefic

    root = Tk()
    root.geometry("230x230")
    root.title("Game")

    one = Button(root,                
                   width=6, height=3,  
                   command = lambda: printing(0)
                   )

    one.place(x=40, y=30)

    two = Button(root,
                   width=6, height=3,  
                   command = lambda: printing(1)
                   )

    two.place(x=90, y=30)

    three = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(2)
                   )

    three.place(x=140, y=30)

    four = Button(root,                
                   width=6, height=3,           
                   command = lambda: printing(3)
                   )

    four.place(x=40, y=85)

    five = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(4)
                   )

    five.place(x=90, y=85)

    six = Button(root,                
                   width=6, height=3,           
                   command = lambda: printing(5)
                   )

    six.place(x=140, y=85)

    seven = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(6)
                   )

    seven.place(x=40, y=140)

    eight = Button(root,                
                   width=6, height=3,           
                   command = lambda: printing(7)
                   )

    eight.place(x=90, y=140)

    nine = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(8)
                   )

    nine.place(x=140, y=140)

    root.mainloop()
