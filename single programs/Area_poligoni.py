from tkinter import *
from tkinter import ttk


def calcoloarea(*args):
 try:
     numlati=float(nlat.get())
     lunglati=float(llat.get())
     lungdiag=float(ldiag.get())
     perimetro=numlati*lunglati
     apotema=(((lungdiag/2)**2-(lunglati/2)**2)**(1/2))
     risultato.set((apotema*perimetro)/2)


 except ValueError:
     risultato.set("ERRORE")
     pass


def reset(*args):
 clear = ""
 nlat.set(clear)
 llat.set(clear)
 ldiag.set(clear)
 risultato.set(clear)


root=Tk()
root.title("Calcolatrice Area Poligoni")
root.geometry("600x700")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


nlat=StringVar()
llat=StringVar()
ldiag=StringVar()
risultato=StringVar()


nlat_entry=Entry(root, width=3, textvariable=nlat, font=('verdana', 50))
nlat_entry.place(height=100, x=5, y=100)


llat_entry=Entry(root, width=3, textvariable=llat, font=('verdana', 50))
llat_entry.place(height=100, x=5, y=260)


ldiag_entry=Entry(root, width=3, textvariable=ldiag, font=('verdana', 50))
ldiag_entry.place(height=100, x=5, y=420)

Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=630)
Label(root, text="Calcolo area poligoni regolari", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Numero Lati :", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Lunghezza Lato :", font=('verdana', 20)).place(height=50, x=5, y=210)
Label(root, text="Lunghezza Diagonale :", font=('verdana', 20)).place(height=50, x=5, y=370)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=255, y=630)
Button(root, text="CALCOLA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=660)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=660)


root.bind('<Return>', calcoloarea)
root.bind('<Return>', reset)


root.mainloop()