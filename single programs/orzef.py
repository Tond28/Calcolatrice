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

def Felastica(*args):
 try:
     kost=float(k.get())
     fe=float(x.get())
     risultato3.set(kost*fe)
     
 except ValueError:
     risultato3.set("ERRORE")
     pass


def reset(*args):                                                                           
 clear = ""
 Fp_1.set(clear)
 µ.set(clear)
 Fp_2.set(clear)
 k.set(clear)
 x.set(clear)
 risultato.set(clear)
 risultato2.set(clear)
 risultato3.set(clear)


root=Tk()
root.title("Calcolatrice Forze")
root.geometry("700x670")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


Fp_1=StringVar()
Fp_2=StringVar()
µ=StringVar()
k=StringVar()
x=StringVar()
risultato=StringVar()
risultato2=StringVar()
risultato3=StringVar()


m1_entry=Entry(root, width=3, textvariable=Fp_1, font=('verdana', 50))
m1_entry.place(height=100, x=5, y=100)


µ1_entry=Entry(root, width=4, textvariable=µ, font=('verdana', 50))
µ1_entry.place(height=100, x=5, y=290)

Fp2_entry=Entry(root, width=3, textvariable=Fp_2, font=('verdana', 50))
Fp2_entry.place(height=100, x=225, y=290)

k_entry=Entry(root, width=3, textvariable=k, font=('verdana', 50))
k_entry.place(height=100, x=5, y=480)

x_entry=Entry(root, width=3, textvariable=x, font=('verdana', 50))
x_entry.place(height=100, x=285, y=480)

Label(root, text="Calcolatore Forze", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Forza Peso (N)", font=('verdana', 20)).place(height=30, x=5, y=55)
Label(root, text="Kg", font=('verdana', 20)).place(height=50, x=147, y=123)
Label(root, text="x", font=('verdana', 20)).place(height=50, x=200, y=123)
Label(root, text="g", font=('Times New Roman', 20)).place(height=50, x=235, y=123)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=260, y=140)

Label(root, text="Forza d'Attrito (N)", font=('verdana', 20)).place(height=30, x=5, y=245)
Label(root, text="x", font=('verdana', 20)).place(height=40, x=190, y=320)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=420, y=330)
Label(root, text="N", font=('verdana', 22)).place(height=40, x=375, y=323)

Label(root, text="Forza Elastica (N)", font=('verdana', 20)).place(height=30, x=5, y=435)
Label(root, text="N/m", font=('verdana', 22)).place(height=40, x=140, y=520)
Label(root, text="x", font=('verdana', 20)).place(height=40, x=230, y=510)
Label(root, text="m", font=('verdana', 20)).place(height=40, x=430, y=520)
Label(root, text="=", font=('verdana', 20)).place(height=40, x=470, y=510)

Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=280, y=134)
Label(root, textvariable=risultato2, font=('verdana', 20)).place(height=30, x=450, y=325)
Label(root, textvariable=risultato3, font=('verdana', 20)).place(height=30, x=500, y=515)

Button(root, text="CALCOLA FORZA PESO", command=Fpeso, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="CALCOLA FORZA D'ATTRITO", command=Fattrito, font=('verdana', 15)).place(height=25, x=5, y=400)
Button(root, text="CALCOLA FORZA ELASTICA", command=Felastica, font=('verdana', 15)).place(height=25, x=5, y=590)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=600, y=635)


root.bind('<Return>', Fpeso)
root.bind('<Return>', Fattrito)
root.bind('<Return>', Felastica)
root.bind('<Return>', reset)


root.mainloop()