from tkinter import *
from tkinter import ttk


def calcoloarea(*args):
 try:
     altezza=float(h.get())
     base=float(b.get())
     risultato.set(altezza/base)


 except ValueError:
     risultato.set("ERRORE")
     pass

def calcoloarea2(*args):
 try:
     altezza2=float(h2.get())
     base2=float(b2.get())
     risultato2.set(altezza2/base2)


 except ValueError:
     risultato2.set("ERRORE")
     pass

def reset(*args):
 clear = ""
 h.set(clear)
 b.set(clear)
 h2.set(clear)
 b2.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice Dinamica")
root.geometry("700x580")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


h=StringVar()
b=StringVar()
h2=StringVar()
b2=StringVar()
risultato=StringVar()
risultato2=StringVar()


h_entry=Entry(root, width=3, textvariable=h, font=('verdana', 50))
h_entry.place(height=100, x=70, y=47)


b_entry=Entry(root, width=3, textvariable=b, font=('verdana', 50))
b_entry.place(height=100, x=70, y=160)

h2_entry=Entry(root, width=3, textvariable=h2, font=('verdana', 50))
h2_entry.place(height=100, x=70, y=327)


b2_entry=Entry(root, width=3, textvariable=b2, font=('verdana', 50))
b2_entry.place(height=100, x=70, y=440)

Label(root, text="Calcolo Velocità", font=('verdana', 20)).pack(anchor=N)
Label(root, text="Calcolo Accelerazione", font=('verdana', 20)).place(height=25, x=200, y=300)

Label(root, text="ΔS", font=('verdana', 20)).place(height=50, x=5, y=70)
Label(root, text="Δt", font=('verdana', 20)).place(height=50, x=5, y=180)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=126)
Label(root, text="ΔV", font=('verdana', 20)).place(height=50, x=5, y=355)
Label(root, text="Δt", font=('verdana', 20)).place(height=50, x=5, y=465)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=406)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=270, y=140)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=270, y=421)

Button(root, text="CALCOLA VELOCITA'", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=270)
Button(root, text="CALCOLA ACCELERAZIONE", command=calcoloarea2, font=('verdana', 15)).place(height=25, x=5, y=550)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=600, y=550)

linea=Canvas(root, width=170, height=3)
linea.place(height=10, x=60, y=150)
linea.create_line(150, 0, 0, 0, width=(10))

linea2=Canvas(root, width=170, height=3)
linea2.place(height=10, x=60, y=430)
linea2.create_line(150, 0, 0, 0, width=(10))

root.bind('<Return>', calcoloarea)
root.bind('<Return>', calcoloarea2)
root.bind('<Return>', reset)


root.mainloop()