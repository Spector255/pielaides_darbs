import tkinter as tk
import hashlib
import sqlite3
import random
import string
from tkinter import messagebox
from option import izvelne

# Pieslēdzamies datu bāzei SQLite
conn = sqlite3.connect('lietotaji.db')
c = conn.cursor()

# Izveidojam tabulu lietotāju datiem, ja tāda vēl nav
c.execute('''CREATE TABLE IF NOT EXISTS lietotaji
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              lietotajvards text,
              parole text,
              epasts text)''')
conn.commit()

# Funkcija, lai šifrētu paroli
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Funkcija, kas pārbauda, vai lietotājs ir datu bāzē
def check_user(username, password):
    c.execute("SELECT * FROM lietotaji WHERE (lietotajvards=:lietotajvards OR epasts=:lietotajvards) AND parole=:parole", {'lietotajvards': username, 'parole': hash_password(password)})
    if c.fetchone():
        return True
    else:
        return False

# Funkcija, kas pārbauda, vai e-pasts ir derīgs
def check_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

# Funkcija, kas izveido CAPTCHA kodu
def generate_captcha():
    captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return captcha

# Funkcija, kas apstrādā notikumu, kad tiek nospiesta pogas "Ienākt"
def login():
    global username_entry, password_entry
    if not username_entry or not password_entry:
        return
    username = username_entry.get()
    password = password_entry.get()
    if check_user(username, password):
        if 'register_window' in globals():
            register_window.destroy()
        messagebox.showinfo("Veiksmīga autentifikācija", "Veiksmīga autentifikācija!")
        root.destroy()  # Aizveram logu ar nosaukumu "Login"
        izvelne()  # Izsaukt funkciju "izvelne" no faila "option.py"
    else:
        messagebox.showerror("Neveiksmīga autentifikācija", "Šķiet, ka kaut kas, ko Jūs ievadījāt, izrādījās nepareizs!")

# Funkcija, kas apstrādā notikumu, kad tiek nospiesta pogas "Reģistrēties"

def register():
    global register_window, username_entry, password_entry, email_entry, captcha_code
    register_window = tk.Toplevel(root)
    register_window.title("Reģistrācija")
    register_window.geometry("350x300")
    username_label = tk.Label(register_window, text="Lietotājvārds:")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()
    password_label = tk.Label(register_window, text="Parole:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()
    email_label = tk.Label(register_window, text="E-pasts:")
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()
    captcha_code = generate_captcha()
    captcha_label = tk.Label(register_window, text="CAPTCHA: " + captcha_code)
    captcha_label.pack()
    captcha_entry = tk.Entry(register_window)
    captcha_entry.pack()

    #Izveidojam pogu "Reģistrēties" un marķieri, lai izvadītu paziņojumus par veiksmīgu vai neveiksmīgu reģistrāciju
    register_button = tk.Button(register_window, text="Reģistrēties", command=lambda: register_new_user(username_entry.get(), password_entry.get(), email_entry.get(), captcha_entry.get()))
    register_button.pack()
    register_label = tk.Label(register_window, text="")
    register_label.pack()

#Funkcija, kas apstrādā notikumu, kad tiek nospiesta pogas "Reģistrēties" jaunā logā

def register_new_user(username, password, email, captcha):
    if check_email(email) and captcha == captcha_code:
        c.execute("INSERT INTO lietotaji (lietotajvards, parole, epasts) VALUES (?, ?, ?)", (username, hash_password(password), email))
        conn.commit()
        messagebox.showinfo("Veiksmīga reģistrācija", "Reģistrācija veiksmīga!")
        register_window.destroy()
        root.destroy()
        izvelne()
    else:
        messagebox.showerror("Neveiksmīga reģistrācija", "Lūdzu, ievadiet derīgu e-pasta adresi un CAPTCHA kodu.")

#Izveidojam galveno logu
global root
root = tk.Tk()
root.title("Login")
root.geometry("350x300")

# Uzstādām paziņojuma par virsrakstu
root.withdraw()
title = messagebox.showinfo("Lietotāja autentifikācija", "Lūdzu, ievadiet lietotājvārdu vai e-pastu un paroli")

#Parādām atgriezto logu un uzliekam fokusu uz to
root.deiconify()
root.focus_force()

#Izveidojam apvienotu marķieri un ievades lauku lietotājvārdam vai e-pastam
username_label = tk.Label(root, text="Lietotājvārds vai e-pasts:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#Izveidojam marķieri un ievades lauku parolei
password_label = tk.Label(root, text="Parole:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

#Izveidojam pogu "Ienākt" un marķieri, lai izvadītu paziņojumus par veiksmīgu autentifikāciju vai neveiksmīgu ienākšanu
login_button = tk.Button(root, text="Ienākt", command=login)
login_button.pack()
login_label = tk.Label(root, text="")
login_label.pack()

#Izveidojam pogu "Reģistrēties"
register_button = tk.Button(root, text="Reģistrēties", command=register)
register_button.pack()

#Sākam galveno loga ciklu
root.mainloop()

#Aizveram savienojumu ar datu bāzi
conn.close()