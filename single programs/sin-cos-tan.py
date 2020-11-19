from tkinter import *
from tkinter import ttk
import math


def cos(*args):
 try:
        coseno=float(cos_1.get())
        risultato.set(math.cos(coseno))

 except ValueError:
        risultato.set("ERRORE")
        pass


def sin(*args):
 try:
        seno=float(sin_1.get())
        risultato2.set(math.sin(seno))
     
 except ValueError:
        risultato2.set("ERRORE")
        pass

def tan(*args):
 try:
        tangente=float(tan_1.get())
        risultato3.set(math.tan(tangente))
 except ValueError:
        risultato3.set("ERRORE")
        pass


def reset(*args):                                                                           
 clear = ""
 cos_1.set(clear)
 sin_1.set(clear)
 tan_1.set(clear)
 risultato.set(clear)
 risultato2.set(clear)
 risultato3.set(clear)


root=Tk()
root.title("Seno, Coseno, Tangente")
root.geometry("650x700")



cos_1=StringVar()
sin_1=StringVar()
tan_1=StringVar()
risultato=StringVar()
risultato2=StringVar()
risultato3=StringVar()


cosen_entry=Entry(root, width=3, textvariable=cos_1, font=('verdana', 50))
cosen_entry.place(height=100, x=20, y=50)


seno1_entry=Entry(root, width=3, textvariable=sin_1, font=('verdana', 50))
seno1_entry.place(height=100, x=20, y=240)


tang_entry=Entry(root, width=3, textvariable=tan_1, font=('verdana', 50))
tang_entry.place(height=100, x=20, y=430)


Label(root, text="°", font=('verdana', 30)).place(height=30, x=160, y=55)
Label(root, text="°", font=('verdana', 30)).place(height=30, x=160, y=245)
Label(root, text="°", font=('verdana', 30)).place(height=30, x=160, y=435)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=170, y=90)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=170, y=280)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=170, y=470)
Label(root, text="Coseno", font=('verdana', 20)).place(height=31, x=115, y=5)
Label(root, text="Seno", font=('verdana', 20)).place(height=31, x=103, y=200)
Label(root, text="Tangente", font=('verdana', 20)).place(height=32, x=103, y=385)

Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=190, y=87)
Label(root, textvariable=risultato2, font=('verdana', 20)).place(height=30, x=190, y=275)
Label(root, textvariable=risultato3, font=('verdana', 20)).place(height=30, x=190, y=466)

Button(root, text="CALCOLA COSENO", command=cos, font=('verdana', 15)).place(height=25, x=5, y=160)
Button(root, text="CALCOLA SENO", command=sin, font=('verdana', 15)).place(height=25, x=5, y=350)
Button(root, text="CALCOLA TANGENTE", command=tan, font=('verdana', 15)).place(height=25, x=5, y=540)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=595)

root.bind('<Return>', cos)
root.bind('<Return>', sin)
root.bind('<Return>', tan)
root.bind('<Return>', reset)

root.mainloop()
