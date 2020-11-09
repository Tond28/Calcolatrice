from tkinter import *
from tkinter import ttk


def Fpeso(*args):
 try:
     m1=float(Fp_1.get())
     risultato.set(m1*9.81)

 except ValueError:
     risultato.set("ERRORE")
     pass


def Fattrito(*args):
 try:
     µ2=float(µ.get())
     fp2=float(Fp_2.get())
     risultato2.set(µ2*fp2)
     
 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):                                                                           
 clear = ""
 Fp_1.set(clear)
 µ.set(clear)
 Fp_2.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice Forze")
root.geometry("700x800")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


Fp_1=StringVar()
Fp_2=StringVar()
µ=StringVar()
risultato=StringVar()
risultato2=StringVar()


m1_entry=Entry(root, width=3, textvariable=Fp_1, font=('verdana', 50))
m1_entry.place(height=100, x=5, y=100)


µ1_entry=Entry(root, width=4, textvariable=µ, font=('verdana', 50))
µ1_entry.place(height=100, x=5, y=290)

Fp2_entry=Entry(root, width=3, textvariable=Fp_2, font=('verdana', 50))
Fp2_entry.place(height=100, x=225, y=290)

Label(root, text="Calcolatore Forze", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Forza Peso (N)", font=('verdana', 20)).place(height=30, x=5, y=55)
Label(root, text="x", font=('verdana', 20)).place(height=50, x=157, y=123)
Label(root, text="g", font=('verdana', 20)).place(height=50, x=190, y=123)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=220, y=140)

Label(root, text="Forza d'Attrito (N)", font=('verdana', 20)).place(height=30, x=5, y=245)
Label(root, text="x", font=('verdana', 20)).place(height=40, x=190, y=320)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=420, y=330)
Label(root, text="N", font=('verdana', 22)).place(height=40, x=375, y=323)

Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=250, y=134)
Label(root, textvariable=risultato2, font=('verdana', 20)).place(height=30, x=450, y=325)

Button(root, text="CALCOLA FORZA PESO", command=Fpeso, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="CALCOLA FORZA D'ATTRITO", command=Fattrito, font=('verdana', 15)).place(height=25, x=5, y=400)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=600, y=755)


root.bind('<Return>', Fpeso)
root.bind('<Return>', Fattrito)
root.bind('<Return>', reset)


root.mainloop()