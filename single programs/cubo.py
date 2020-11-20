from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import tkinter as tk

def calcoloarea(*args):
 try:
     lato=float(l.get())
     risultato.set(6*(lato**2))


 except ValueError:
     risultato.set("ERRORE")
     pass

def calcolovol(*args):
 try: 
     lato=float(l.get())
     risultato2.set(lato**3)
     

 except ValueError:
     risultato2.set("ERRORE")
     pass

def reset(*args):
 clear = ""
 l.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=tk.Tk()
root.title("Calcolatrice A, V; Cubo")
root.geometry("600x520")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

immagine_tk = ImageTk.PhotoImage(Image.open("images\cubo.png"))
tk.Label(root, image=immagine_tk).place(height=400, x=5, y=220)

l=StringVar()
risultato=StringVar()
risultato2=StringVar()


r_entry=Entry(root, width=3, textvariable=l, font=('verdana', 50))
r_entry.place(height=100, x=5, y=100)


Label(root, text="RISULTATO VOLUME CUBO:", font=('verdana', 15)).place(height=20, x=5, y=300)
Label(root, text="RISULTATO AREA CUBO:", font=('verdana', 15)).place(height=20, x=5, y=240)
Label(root, text="Calcolo Area e Volume del Cubo", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Lato:", font=('verdana', 20)).place(height=50, x=5, y=50)

Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=290, y=300)
Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=260, y=240)
Button(root, text="CALCOLA AREA CUBO", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="CALCOLA VOLUME CUBO", command=calcolovol, font=('verdana', 15)).place(height=25, x=5, y=270)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=490)

root.bind('<Return>', calcoloarea)
root.bind('<Return>', calcolovol)
root.bind('<Return>', reset)

root.mainloop()