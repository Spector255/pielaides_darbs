from tkinter import *
from tkinter import messagebox
# ================== FUNCTIONS ==================
def cleaning():     #attiram laukumu
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
    uzruna.config(text = f"{player1}, tavs gājiens({element1})")

def statistika(): #izvadam statistiku
    msg = messagebox.showinfo(title="Statistika!",
                              message=f"Statistika kopš programmas palaišanas:\n - {player1} uzvārejis: {Xwin} reizes \n - {player2} uzvārejis: {Owin} reizes \n -Neviens neuzvārejis: {XO} reizes \n -Pavisām spēlēs: {Xwin+Owin+XO}")
def finalX():   #apsveicam lietotaju nr. 1
    msg = messagebox.showinfo(title="Apsveicam!",
                              message=f"Apsveicam! Uzvarēja {player1}!")
    statistika()
    cleaning()

def finalO(): #apsveicam lietotaju nr. 2
    msg = messagebox.showinfo(title="Apsveicam!",
                              message=f"Apsveicam! Uzvarēja {player2}!")
    statistika()
    cleaning()

def final(): #pazinojums par speles beigam
    msg = messagebox.showwarning(title="-_-",
                              message="Neviens nav uzvarējis!")
    statistika()
    cleaning()    

def parbaudeX(): #parbaudam speletaja nr. 1 uzvaru
    if (rutinas[0] == 1 and rutinas[1] == 1  and rutinas[2] == 1 )  or (rutinas[3] == 1 and rutinas[4] == 1  and rutinas[5] == 1 ) or (rutinas[6] == 1 and rutinas[7] == 1  and rutinas[8] == 1 )or (rutinas[0] == 1 and rutinas[3] == 1  and rutinas[6] == 1 ) or (rutinas[1] == 1 and rutinas[4] == 1  and rutinas[7] == 1 ) or (rutinas[2] == 1 and rutinas[5] == 1  and rutinas[8] == 1 )or (rutinas[2] == 1 and rutinas[4] == 1  and rutinas[6] == 1 )or (rutinas[0] == 1 and rutinas[4] == 1  and rutinas[8] == 1 ):
      global Xwin
      Xwin= Xwin + 1
      finalX()

def parbaudeO(): #parbaudam speletaja nr. 2 uzvaru
    if (rutinas[0] == 2 and rutinas[1] == 2  and rutinas[2] == 2 ) or (rutinas[3] == 2 and rutinas[4] == 2  and rutinas[5] == 2 ) or (rutinas[6] == 2 and rutinas[7] == 2  and rutinas[8] == 2 )or (rutinas[0] == 2 and rutinas[3] == 2  and rutinas[6] == 2 ) or (rutinas[1] == 2 and rutinas[4] == 2  and rutinas[7] == 2 ) or (rutinas[2] == 2 and rutinas[5] == 2  and rutinas[8] == 2 )or (rutinas[2] == 2 and rutinas[4] == 2  and rutinas[6] == 2 )or (rutinas[0] == 2 and rutinas[4] == 2  and rutinas[8] == 2 ):
      global Owin
      Owin= Owin + 1
      finalO()

def parbaude(): #parbaudam neizskirsto speli
    if not 0 in rutinas:
        global XO
        XO=XO+1
        final()
        

def printing(X): #uzraksta druka
    global solis, element_izdrukai
    vertiba=0
    if solis%2!=0:
        element_izdrukai = element2
        vertiba=2
        uzruna.config(text = f"{player1}, tavs gājiens({element1})")
    else:
        element_izdrukai = element1
        vertiba=1
        uzruna.config(text = f"{player2}, tavs gājiens({element2})")
    if rutinas[X-1] == 0:
        if X==1:
            one.config(text = element_izdrukai)
        elif X==2:
            two.config(text = element_izdrukai)
        elif X==3:
            three.config(text = element_izdrukai)
        elif X==4:
            four.config(text = element_izdrukai)
        elif X==5:
            five.config(text = element_izdrukai)
        elif X==6:
            six.config(text = element_izdrukai)
        elif X==7:
            seven.config(text = element_izdrukai)
        elif X==8:
            eight.config(text = element_izdrukai)
        else:
            nine.config(text = element_izdrukai)
        solis=solis+1
        rutinas[X-1] = vertiba
    parbaudeX()
    parbaudeO()
    parbaude()
    

def pamatprogramma(pl1elements, player1name, player2name): #veidojam laukumu
    global rutinas, solis, Xwin, Owin, XO, player1, player2, element1, element2
    global one,two,three,four,five,six,seven,eight,nine,uzruna
    rutinas=[0,0,0,0,0,0,0,0,0]
    solis=0
    Xwin=0
    Owin=0
    XO=0
    player1 = player1name
    player2 = player2name
    if pl1elements == 1:
        element1 = "X"
        element2 = "O"
    else:
        element1 = "O"
        element2 = "X"
    
    root = Tk()
    root.geometry("230x230")
    root.title("Game")

    one = Button(root,                
                   width=6, height=3,  
                   command = lambda: printing(1)
                   )

    one.place(x=40, y=30)

    two = Button(root,
                   width=6, height=3,  
                   command = lambda: printing(2)
                   )

    two.place(x=90, y=30)

    three = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(3)
                   )

    three.place(x=140, y=30)

    four = Button(root,                
                   width=6, height=3,           
                   command = lambda: printing(4)
                   )

    four.place(x=40, y=85)

    five = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(5)
                   )

    five.place(x=90, y=85)

    six = Button(root,                
                   width=6, height=3,           
                   command = lambda: printing(6)
                   )

    six.place(x=140, y=85)

    seven = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(7)
                   )

    seven.place(x=40, y=140)

    eight = Button(root,                
                   width=6, height=3,           
                   command = lambda: printing(8)
                   )

    eight.place(x=90, y=140)

    nine = Button(root,                
                   width=6, height=3,            
                   command = lambda: printing(9)
                   )

    nine.place(x=140, y=140)

    uzruna = Label(root,
                text = f"{player1name}, tavs gājiens({element1})",
                fg = "red")
    
    uzruna.place(x=55, y=5)

    root.mainloop()
