from tkinter import *
from tkinter import ttk


def calcolomom(*args):
 try:
     forza=float(f.get())
     braccio=float(b.get())
     risultato.set(braccio*forza)


 except ValueError:
     risultato.set("ERRORE")
     pass


def reset(*args):
 clear = ""
 f.set(clear)
 b.set(clear)
 risultato.set(clear)


root=Tk()
root.title("Calcolatrice Momento")
root.geometry("600x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


f=StringVar()
b=StringVar()
risultato=StringVar()


f_entry=Entry(root, width=3, textvariable=f, font=('verdana', 50))
f_entry.place(height=100, x=5, y=100)


b_entry=Entry(root, width=3, textvariable=b, font=('verdana', 50))
b_entry.place(height=100, x=5, y=260)


Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=430)
Label(root, text="Calcolo Momento", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Braccio (m):", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Forza (N):", font=('verdana', 20)).place(height=50, x=5, y=210)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=150, y=430)
Button(root, text="CALCOLA", command=calcolomom, font=('verdana', 15)).place(height=25, x=5, y=460)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=460)


root.bind('<Return>', calcolomom)
root.bind('<Return>', reset)


root.mainloop()