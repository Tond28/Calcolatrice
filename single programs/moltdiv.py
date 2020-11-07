from tkinter import *
from tkinter import ttk


def moltiplicazione(*args):
 try:
     fattore_1=float(molt_1.get())
     fattore_2=float(molt_2.get())
     risultato.set(fattore_1 * fattore_2)

 except ValueError:
     risultato.set("ERRORE")
     pass


def divisione(*args):
 try:
     dividendo_1=float(div_1.get())
     divisore_2=float(div_2.get())
     risultato2.set(dividendo_1 / divisore_2)
     
 except ValueError:
     risultato2.set("ERRORE")
     pass
 except ZeroDivisionError:
     risultato2.set("ERRORE")
     pass


def reset(*args):                                                                           
 clear = ""
 molt_1.set(clear)
 molt_2.set(clear)
 div_1.set(clear)
 div_2.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Moltiplicazione|Divisione")
root.geometry("650x400")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


molt_1=StringVar()
molt_2=StringVar()
div_1=StringVar()
div_2=StringVar()
risultato=StringVar()
risultato2=StringVar()


molt1_entry=Entry(root, width=3, textvariable=molt_1, font=('verdana', 50))
molt1_entry.place(height=100, x=5, y=50)


molt2_entry=Entry(root, width=3, textvariable=molt_2, font=('verdana', 50))
molt2_entry.place(height=100, x=205, y=50)


div1_entry=Entry(root, width=3, textvariable=div_1, font=('verdana', 50))
div1_entry.place(height=100, x=5, y=240)


div2_entry=Entry(root, width=3, textvariable=div_2, font=('verdana', 50))
div2_entry.place(height=100, x=205, y=240)


Label(root, text="=", font=('verdana', 15)).place(height=20, x=360, y=90)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=360, y=280)
Label(root, text="Prodotto", font=('verdana', 20)).place(height=30, x=115, y=5)
Label(root, text="Divisione", font=('verdana', 20)).place(height=30, x=103, y=200)
Label(root, text="x", font=('verdana', 20)).place(height=50, x=157, y=73)
Label(root, text=":", font=('verdana', 20)).place(height=40, x=160, y=270)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=390, y=87)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=390, y=275)

Button(root, text="CALCOLA PRODOTTO", command=moltiplicazione, font=('verdana', 15)).place(height=25, x=5, y=160)
Button(root, text="CALCOLA DIVISIONE", command=divisione, font=('verdana', 15)).place(height=25, x=5, y=350)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=365)


root.bind('<Return>', moltiplicazione)
root.bind('<Return>', divisione)
root.bind('<Return>', reset)


root.mainloop()