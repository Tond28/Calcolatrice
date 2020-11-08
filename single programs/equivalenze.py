from tkinter import *
from tkinter import ttk

def calcolo(*args):
    Valore1=Prumisura.get()
    Valore2=Prumisura2.get()
    valoreprimo=float(var_1.get())
    if Valore1=="E":
        valorebase=valoreprimo*(10**18)
    elif Valore1=="P":
        valorebase=valoreprimo*(10**15)
    elif Valore1=="T":
        valorebase=valoreprimo*(10**12)
    elif Valore1=="G":
        valorebase=valoreprimo*(10**9)
    elif Valore1=="M":
        valorebase=valoreprimo*(10**6)
    elif Valore1=="k":
        valorebase=valoreprimo*(10**3)
    elif Valore1=="h":
        valorebase=valoreprimo*(10**2)
    elif Valore1=="da":
        valorebase=valoreprimo*(10**1)
    elif Valore1=="u":
        valorebase=valoreprimo*(10**0) 
    elif Valore1=="d":
        valorebase=valoreprimo*(10**-1)
    elif Valore1=="c":
        valorebase=valoreprimo*(10**-2) 
    elif Valore1=="m":
        valorebase=valoreprimo*(10**-3) 
    elif Valore1=="µ":
        valorebase=valoreprimo*(10**-6) 
    elif Valore1=="n":
        valorebase=valoreprimo*(10**-9) 
    elif Valore1=="p":
        valorebase=valoreprimo*(10**-12)
    elif Valore1=="f":
        valorebase=valoreprimo*(10**-15) 
    elif Valore1=="a":
        valorebase=valoreprimo*(10**-18)

    if Valore2=="E":
        valorebase*=(10**-18) 
    elif Valore2=="P":
        valorebase*=(10**-15) 
    elif Valore2=="T":
        valorebase*=(10**-12) 
    elif Valore2=="G":
        valorebase*=(10**-9) 
    elif Valore2=="M":
        valorebase*=(10**-6) 
    elif Valore2=="k":
        valorebase*=(10**-3) 
    elif Valore2=="h":
        valorebase*=(10**-2) 
    elif Valore2=="da":
        valorebase*=(10**-1) 
    elif Valore2=="u":
        valorebase*=(10**0) 
    elif Valore2=="d":
        valorebase*=(10**1) 
    elif Valore2=="c":
        valorebase*=(10**2)
    elif Valore2=="m":
        valorebase*=(10**3) 
    elif Valore2=="µ":
        valorebase*=(10**6)
    elif Valore2=="n":
        valorebase*=(10**9)
    elif Valore2=="p":
        valorebase*=(10**12)
    elif Valore2=="f":
        valorebase*=(10**15) 
    elif Valore2=="a":
        valorebase*=(10**18)

    risultato.set(valorebase)


def reset(*args):                                                                           
 clear = ""
 var_1.set(clear)
 risultato.set(clear)
 Prumisura.set(OptionList2[8])
 Prumisura2.set(OptionList2[8])


root=Tk()
root.title("Calcolatrice Equivalenze")
root.geometry("650x250")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


var_1=StringVar()
Umisura = StringVar()
Prumisura = StringVar()
Prumisura2 = StringVar()
risultato=StringVar()

add1_entry=Entry(root, width=3, textvariable=var_1, font=('verdana', 50))
add1_entry.place(height=100, x=5, y=80)


Label(root, text="Equivalenze", font=('verdana', 20)).pack(anchor=N)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=100)


Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=260, y=110)


Button(root, text="CALCOLA", command=calcolo, font=('verdana', 15)).place(height=25, x=5, y=190)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=5, y=220)


OptionList = ["Spazio (m)", "Massa (g)"]
OptionList2 = ["E", "P", "T", "G", "M", "k", "h", "da", "u", "d", "c", "m", "µ", "n", "p", "f", "a"] 

Umisura.set(OptionList[0])
Prumisura.set(OptionList2[8])
Prumisura2.set(OptionList2[8])

opt = OptionMenu(root, Umisura, *OptionList)
opt.config(width=10, font=('verdana', 12))
opt.place(height=30, x=0, y=40)

opt2 = OptionMenu(root, Prumisura, *OptionList2)
opt2.config(width=2, font=('verdana', 12))
opt2.place(height=60, x=150, y=122)

opt3 = OptionMenu(root, Prumisura2, *OptionList2)
opt3.config(width=2, font=('verdana', 12))
opt3.place(height=60, x=580, y=122)

root.bind('<Return>', calcolo)
root.bind('<Return>', reset)

root.mainloop()