from tkinter import *
from tkinter import ttk


def calcoloarea(*args):
 try:
     numlati=float(nlat.get())
     lunglati=float(llat.get())
     lungdiag=float(ldiag.get())
     risultato.set(2*(numlati*lunglati)+4*(lunglati*lungdiag))


 except ValueError:
     risultato.set("ERRORE")
     pass

def calcoloarea2(*args):
 try:
     numlati=float(nlat.get())
     lunglati=float(llat.get())
     lungdiag=float(ldiag.get())
     risultato2.set(numlati*lunglati*lungdiag)


 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):
 clear = ""
 nlat.set(clear)
 llat.set(clear)
 ldiag.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice A, V; Parallelepipedo")
root.geometry("600x700")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


nlat=StringVar()
llat=StringVar()
ldiag=StringVar()
risultato=StringVar()
risultato2=StringVar()


nlat_entry=Entry(root, width=3, textvariable=nlat, font=('verdana', 50))
nlat_entry.place(height=100, x=5, y=100)


llat_entry=Entry(root, width=3, textvariable=llat, font=('verdana', 50))
llat_entry.place(height=100, x=5, y=260)


ldiag_entry=Entry(root, width=3, textvariable=ldiag, font=('verdana', 50))
ldiag_entry.place(height=100, x=5, y=420)


Label(root, text="AREA:", font=('verdana', 15)).place(height=20, x=5, y=565)
Label(root, text="VOLUME:", font=('verdana', 15)).place(height=20, x=5, y=625)
Label(root, text="Calcolo Area e Volume Parallelepipedo", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Lato:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Altezza:", font=('verdana', 20)).place(height=50, x=5, y=210)
Label(root, text="Base:", font=('verdana', 20)).place(height=50, x=5, y=370)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=80, y=565)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=103, y=625)

Button(root, text="CALCOLA AREA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=530)
Button(root, text="CALCOLA VOLUME", command=calcoloarea2, font=('verdana', 15)).place(height=25, x=5, y=590)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=660)


root.bind('<Return>', calcoloarea)
root.bind('<Return>', calcoloarea2)
root.bind('<Return>', reset)


root.mainloop()