from tkinter import *
from tkinter import ttk
from random import randint

def randomnum(*args):
 try:
     finale=float(x.get())
     risultato.set(randint(1, finale))

 except ValueError:
     risultato.set("ERRORE")
     pass


def reset(*args):
 clear = ""
 x.set(clear)
 risultato.set(clear)


root=Tk()
root.title("Generatore Interrogazioni")
root.geometry("600x270")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


x=StringVar()
risultato=StringVar()


x_entry=Entry(root, width=3, textvariable=x, font=('verdana', 50))
x_entry.place(height=100, x=5, y=100)

Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=210)
Label(root, text="Generatore Interrogazioni", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Numero studenti:", font=('verdana', 20)).place(height=50, x=5, y=50)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=150, y=210)
Button(root, text="CALCOLA", command=randomnum, font=('verdana', 15)).place(height=25, x=5, y=240)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=240)

root.bind('<Return>', randomnum)
root.bind('<Return>', reset)

root.mainloop()