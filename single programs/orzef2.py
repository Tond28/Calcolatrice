from tkinter import *
from tkinter import ttk


def calcolofeq(*args):
 try:
     fpeso=float(fp.get())
     altezza=float(h.get())
     lung=float(l.get())
     risultato.set(fpeso*(altezza/lung))


 except ValueError:
     risultato.set("ERRORE")
     pass


def reset(*args):
 clear = ""
 fp.set(clear)
 h.set(clear)
 l.set(clear)
 risultato.set(clear)


root=Tk()
root.title("Calcolatrice Forza d'Equilibrio")
root.geometry("600x700")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


fp=StringVar()
h=StringVar()
l=StringVar()
risultato=StringVar()


fp_entry=Entry(root, width=3, textvariable=fp, font=('verdana', 50))
fp_entry.place(height=100, x=5, y=100)


h_entry=Entry(root, width=3, textvariable=h, font=('verdana', 50))
h_entry.place(height=100, x=5, y=260)


l_entry=Entry(root, width=3, textvariable=l, font=('verdana', 50))
l_entry.place(height=100, x=5, y=420)



Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=630)
Label(root, text="Calcolo Forza d'Equilibrio", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Forza Peso :", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Altezza :", font=('verdana', 20)).place(height=50, x=5, y=210)
Label(root, text="Lunghezza :", font=('verdana', 20)).place(height=50, x=5, y=370)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=140, y=630)
Button(root, text="CALCOLA", command=calcolofeq, font=('verdana', 15)).place(height=25, x=5, y=660)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=660)


root.bind('<Return>', calcolofeq)
root.bind('<Return>', reset)

root.mainloop()