from tkinter import *
from tkinter import ttk


def perc1(*args):
 try:
     p1=float(p_1.get())
     p2=float(p_2.get())
     risultato.set((p1*p2)/100)

 except ValueError:
     risultato.set("ERRORE")
     pass


def perc2(*args):
 try:
     p3=float(p_3.get())
     p4=float(p_4.get())
     risultato2.set((p3*100)/p4)
     
 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):                                                                           
 clear = ""
 p_1.set(clear)
 p_2.set(clear)
 p_3.set(clear)
 p_4.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice Percentuale")
root.geometry("804x480")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


p_1=StringVar()
p_2=StringVar()
p_3=StringVar()
p_4=StringVar()
risultato=StringVar()
risultato2=StringVar()


p1_entry=Entry(root, width=3, textvariable=p_1, font=('verdana', 50))
p1_entry.place(height=100, x=50, y=100)

p2_entry=Entry(root, width=3, textvariable=p_2, font=('verdana', 50))
p2_entry.place(height=100, x=300, y=100)

p3_entry=Entry(root, width=3, textvariable=p_3, font=('verdana', 50))
p3_entry.place(height=100, x=50, y=290)

p4_entry=Entry(root, width=3, textvariable=p_4, font=('verdana', 50))
p4_entry.place(height=100, x=255, y=290)


Label(root, text="Calcolatore Percentuale", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Esempio: il 30% di 10 é 3", font=('verdana', 20)).place(height=30, x=5, y=55)
Label(root, text="Il", font=('verdana', 20)).place(height=50, x=5, y=123)
Label(root, text="%", font=('verdana', 20)).place(height=50, x=200, y=123)
Label(root, text="di", font=('verdana', 20)).place(height=50, x=245, y=123)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=450, y=140)

Label(root, text="Esempio: se 7 é il 70% del totale, questo totale é 10.", font=('verdana', 20)).place(height=30, x=5, y=245)
Label(root, text="Se", font=('verdana', 20)).place(height=40, x=5, y=320)
Label(root, text="è", font=('verdana', 20)).place(height=40, x=200, y=320)
Label(root, text="il", font=('verdana', 20)).place(height=40, x=225, y=320)
Label(root, text="% del totale;", font=('verdana', 20)).place(height=40, x=390, y=320)
Label(root, text="totale =", font=('verdana', 20)).place(height=40, x=5, y=400)



Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=470, y=134)
Label(root, textvariable=risultato2, font=('verdana', 20)).place(height=30, x=120, y=410)

Button(root, text="CALCOLA", command=perc1, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="CALCOLA", command=perc2, font=('verdana', 15)).place(height=25, x=5, y=450)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=700, y=450)


root.bind('<Return>', perc1)
root.bind('<Return>', perc2)
root.bind('<Return>', reset)

root.mainloop()
