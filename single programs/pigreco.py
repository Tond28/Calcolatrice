from tkinter import *
from tkinter import ttk


def calcoloarea(*args):
 try:
     raggio=float(r.get())
     risultato.set(3.141592653589793*(raggio**2))


 except ValueError:
     risultato.set("ERRORE")
     pass

def calcolocirc(*args):
 try: 
     raggio=float(r.get())
     risultato2.set(3.141592653589793*raggio*2)
     

 except ValueError:
     risultato2.set("ERRORE")
     pass

def reset(*args):
 clear = ""
 r.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice A, 2p del cerchio")
root.geometry("600x350")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


r=StringVar()
risultato=StringVar()
risultato2=StringVar()


r_entry=Entry(root, width=3, textvariable=r, font=('verdana', 50))
r_entry.place(height=100, x=5, y=100)


Label(root, text="RISULTATO AREA:", font=('verdana', 15)).place(height=20, x=5, y=300)
Label(root, text="RISULTATO CIRCONFERENZA:", font=('verdana', 15)).place(height=20, x=5, y=240)
Label(root, text="Calcolo Area e Perimetro del cerchio", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Raggio:", font=('verdana', 20)).place(height=50, x=5, y=50)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=200, y=300)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=320, y=240)
Button(root, text="CALCOLA AREA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=270)
Button(root, text="CALCOLA CIRCONFERENZA", command=calcolocirc, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=300)

root.bind('<Return>', calcoloarea)
root.bind('<Return>', calcolocirc)
root.bind('<Return>', reset)

root.mainloop()
