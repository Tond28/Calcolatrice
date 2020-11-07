from tkinter import *
from tkinter import ttk


def addizione(*args):
 try:
     addendo_1=float(add_1.get())
     addendo_2=float(add_2.get())
     risultato.set(addendo_1 + addendo_2)

 except ValueError:
     risultato.set("ERRORE")
     pass


def sottrazione(*args):
 try:
     sottraendo_1=float(sottr_1.get())
     sottraendo_2=float(sottr_2.get())
     risultato2.set(sottraendo_1 - sottraendo_2)
     
 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):                                                                           
 clear = ""
 add_1.set(clear)
 add_2.set(clear)
 sottr_1.set(clear)
 sottr_2.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice (+ , -)")
root.geometry("650x400")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


add_1=StringVar()
add_2=StringVar()
sottr_1=StringVar()
sottr_2=StringVar()
risultato=StringVar()
risultato2=StringVar()


add1_entry=Entry(root, width=3, textvariable=add_1, font=('verdana', 50))
add1_entry.place(height=100, x=5, y=50)


add2_entry=Entry(root, width=3, textvariable=add_2, font=('verdana', 50))
add2_entry.place(height=100, x=205, y=50)


sottr1_entry=Entry(root, width=3, textvariable=sottr_1, font=('verdana', 50))
sottr1_entry.place(height=100, x=5, y=240)


sottr2_entry=Entry(root, width=3, textvariable=sottr_2, font=('verdana', 50))
sottr2_entry.place(height=100, x=205, y=240)


Label(root, text="=", font=('verdana', 15)).place(height=20, x=360, y=90)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=360, y=280)
Label(root, text="Somma", font=('verdana', 20)).place(height=30, x=115, y=5)
Label(root, text="Sottrazione", font=('verdana', 20)).place(height=30, x=103, y=200)
Label(root, text="+", font=('verdana', 20)).place(height=50, x=157, y=73)
Label(root, text="-", font=('verdana', 20)).place(height=40, x=160, y=270)

Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=390, y=87)
Label(root, textvariable=risultato2, font=('verdana', 20)).place(height=30, x=390, y=275)

Button(root, text="CALCOLA ADDIZIONE", command=addizione, font=('verdana', 15)).place(height=25, x=5, y=160)
Button(root, text="CALCOLA SOTTRAZIONE", command=sottrazione, font=('verdana', 15)).place(height=25, x=5, y=350)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=365)


root.bind('<Return>', addizione)
root.bind('<Return>', sottrazione)
root.bind('<Return>', reset)


root.mainloop()