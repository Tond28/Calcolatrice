from tkinter import *
from tkinter import ttk


def calcoloip(*args):
 try:
     cateto1=float(h.get())
     cateto2=float(b.get())
     risultato.set(((cateto1**2)+(cateto2**2))**(1/2))


 except ValueError:
     risultato.set("ERRORE")
     pass

def calcolocat(*args):
 try:
     cateto3=float(c.get())
     ipotenusa=float(i.get())
     risultato2.set(((ipotenusa**2)-(cateto3**2))**(1/2))


 except ValueError:
     risultato2.set("ERRORE")
     pass

def reset(*args):
 clear = ""
 h.set(clear)
 b.set(clear)
 i.set(clear)
 c.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice Teorema di Pitagora")
root.geometry("600x525")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


h=StringVar()
b=StringVar()
i=StringVar()
c=StringVar()
risultato=StringVar()
risultato2=StringVar()


h_entry=Entry(root, width=3, textvariable=h, font=('verdana', 50))
h_entry.place(height=100, x=5, y=100)


b_entry=Entry(root, width=3, textvariable=b, font=('verdana', 50))
b_entry.place(height=100, x=205, y=100)

i_entry=Entry(root, width=3, textvariable=i, font=('verdana', 50))
i_entry.place(height=100, x=5, y=360)

c_entry=Entry(root, width=3, textvariable=c, font=('verdana', 50))
c_entry.place(height=100, x=205, y=360)


Label(root, text="IPOTENUSA RISULTANTE:", font=('verdana', 15)).place(height=20, x=5, y=240)
Label(root, text="Teorema di Pitagora", font=('verdana', 20)).place(height=40, x=115, y=5)
Label(root, text="Teorema di Pitagora Inverso", font=('verdana', 20)).place(height=40, x=100, y=270)

Label(root, text="Cateto 1:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Cateto 2:", font=('verdana', 20)).place(height=50, x=205, y=50)
Label(root, text="Ipotenusa:", font=('verdana', 20)).place(height=50, x=5, y=310)
Label(root, text="Cateto 3:", font=('verdana', 20)).place(height=50, x=205, y=310)
Label(root, text="CATETO RISULTANTE:", font=('verdana', 15)).place(height=40, x=5, y=490)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=270, y=240)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=235, y=500)
Button(root, text="CALCOLA", command=calcoloip, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="CALCOLA", command=calcolocat, font=('verdana', 15)).place(height=25, x=5, y=470)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=490)


root.bind('<Return>', calcoloip)
root.bind('<Return>', calcolocat)
root.bind('<Return>', reset)


root.mainloop()