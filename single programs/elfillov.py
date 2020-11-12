from tkinter import *
from tkinter import ttk


def calcolovel(*args):
 try:
     difspazio=float(s.get())
     diftempo=float(t.get())
     risultato.set(difspazio/diftempo)


 except ValueError:
     risultato.set("ERRORE")
     pass

def calcolovel2(*args):
 try:
     difspazio2=float(s2.get())
     diftempo2=float(t2.get())
     risultato2.set(difspazio2/diftempo2)


 except ValueError:
     risultato2.set("ERRORE")
     pass

def reset(*args):
 clear = ""
 s.set(clear)
 t.set(clear)
 s2.set(clear)
 t2.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Calcolatrice Dinamica")
root.geometry("700x580")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


s=StringVar()
t=StringVar()
s2=StringVar()
t2=StringVar()
risultato=StringVar()
risultato2=StringVar()


s_entry=Entry(root, width=3, textvariable=s, font=('verdana', 50))
s_entry.place(height=100, x=70, y=47)


t_entry=Entry(root, width=3, textvariable=t, font=('verdana', 50))
t_entry.place(height=100, x=70, y=160)

s2_entry=Entry(root, width=3, textvariable=s2, font=('verdana', 50))
s2_entry.place(height=100, x=70, y=327)


t2_entry=Entry(root, width=3, textvariable=t2, font=('verdana', 50))
t2_entry.place(height=100, x=70, y=440)

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

Button(root, text="CALCOLA VELOCITA'", command=calcolovel, font=('verdana', 15)).place(height=25, x=5, y=270)
Button(root, text="CALCOLA ACCELERAZIONE", command=calcolovel2, font=('verdana', 15)).place(height=25, x=5, y=550)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=600, y=550)

linea=Canvas(root, width=170, height=3)
linea.place(height=10, x=60, y=150)
linea.create_line(150, 0, 0, 0, width=(10))

linea2=Canvas(root, width=170, height=3)
linea2.place(height=10, x=60, y=430)
linea2.create_line(150, 0, 0, 0, width=(10))

root.bind('<Return>', calcolovel)
root.bind('<Return>', calcolovel2)
root.bind('<Return>', reset)


root.mainloop()