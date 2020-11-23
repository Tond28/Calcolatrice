from tkinter import *
from tkinter import ttk

def calcolomassa(*args):
 try:
     Volume=float(V.get())
     risultato.set(Volume*D)


 except ValueError:
     risultato.set("ERRORE")
     pass

def reset(*args):
 clear = ""
 V.set(clear)
 list_help.current(0)
 risultato.set(clear)

root=Tk()
root.title("Calcolatrice Massa")
root.geometry("600x270")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

V=StringVar()
risultato=StringVar()

V_entry=Entry(root, width=3, textvariable=V, font=('verdana', 50))
V_entry.place(height=100, x=5, y=100)

D = 0

def callback(*args):
    global D
    programma=Umisura.get()
    if programma=="Acqua":
        D = 1000
    if programma=="Acqua Salata":
        D = 1030
    if programma=="Alluminio":
        D = 2750
    if programma=="Argento":
        D = 10500
    if programma=="Aria":
        D = 1.293
    if programma=="Carta":
        D = 970
    if programma=="Diamante":
        D = 3550
    if programma=="Ferro":
        D = 7880
    if programma=="Latte":
        D = 1034
    if programma=="Marmo":
        D = 2800
    if programma=="Mercurio":
        D = 13590
    if programma=="Oro":
        D = 19250
    if programma=="Piombo":
        D = 11340
    if programma=="Platino":
        D = 21400
    if programma=="Stagno":
        D = 7280
    if programma=="Sughero":
        D = 350
    if programma=="Vetro":
        D = 2700
    if programma=="Zinco":
        D = 7100


Umisura = StringVar()
help_=["", "Acqua", "Acqua Salata", "Alluminio", "Argento", "Aria", "Carta", "Diamante", "Ferro", "Latte", "Marmo", "Mercurio", "Oro", "Piombo", "Platino", "Stagno", "Sughero"]

list_help = ttk.Combobox(root, width = 27, value=help_, textvariable = Umisura) 

list_help.bind("<<ComboboxSelected>>", callback)

label = Label(root)
label.place(height=110, x=450, y=60)

list_help.place(height=30, x=200, y=100)
list_help.current(0) 

Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=5, y=210)
Label(root, text="Calcolo Massa", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Volume:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Densità del materiale:", font=('verdana', 20)).place(height=50, x=194, y=50)
Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=150, y=210)
Button(root, text="CALCOLA", command=calcolomassa, font=('verdana', 15)).place(height=25, x=5, y=240)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=240)

root.bind('<Return>', calcolomassa)
root.bind('<Return>', reset)

root.mainloop()