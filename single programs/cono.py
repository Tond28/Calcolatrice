from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import tkinter as tk

def calcoloareaT(*args):
 try:
        lato=float(lat.get())
        raggio=float(r.get())
        areab = 3.141592653589793*(raggio**2)
        areal = 3.141592653589793*lato*raggio
        risultato.set(areal + areab)


 except ValueError:
        risultato.set("ERRORE")
        pass

def calcolovolume(*args):
 try:
        altezza=float(alt.get())
        raggio=float(r.get())
        risultato2.set((3.141592653589793*(raggio**2)*altezza)/3)


 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):
    clear = ""
    lat.set(clear)
    alt.set(clear)
    r.set(clear)
    risultato.set(clear)
    risultato2.set(clear)


root=tk.Tk()
root.title("Cono")
root.geometry("600x700")

immagine_tk = ImageTk.PhotoImage(Image.open("images\cono.png"))
tk.Label(root, image=immagine_tk).place(height=400, x=300, y=100)


lat=StringVar()
alt=StringVar()
r=StringVar()
risultato=StringVar()
risultato2=StringVar()


lat_entry=Entry(root, width=3, textvariable=lat, font=('verdana', 50))
lat_entry.place(height=100, x=5, y=100)


r_entry=Entry(root, width=3, textvariable=r, font=('verdana', 50))
r_entry.place(height=100, x=5, y=260)


alt_entry=Entry(root, width=3, textvariable=alt, font=('verdana', 50))
alt_entry.place(height=100, x=5, y=420)


Label(root, text="AREA:", font=('verdana', 15)).place(height=20, x=5, y=565)
Label(root, text="VOLUME:", font=('verdana', 15)).place(height=20, x=5, y=625)
Label(root, text="Calcolo Area e Volume Cono", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Apotema:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Raggio di base:", font=('verdana', 20)).place(height=50, x=5, y=210)
Label(root, text="Altezza:", font=('verdana', 20)).place(height=50, x=5, y=370)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=80, y=565)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=103, y=625)

Button(root, text="CALCOLA AREA TOTALE", command=calcoloareaT, font=('verdana', 15)).place(height=25, x=5, y=530)
Button(root, text="CALCOLA VOLUME", command=calcolovolume, font=('verdana', 15)).place(height=25, x=5, y=590)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=660)


root.bind('<Return>', calcoloareaT)
root.bind('<Return>', calcolovolume)
root.bind('<Return>', reset)


root.mainloop()