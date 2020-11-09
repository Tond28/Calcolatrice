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


def calcolo2(*args):
    valore3=Prumisura3.get()
    valore4=Prumisura4.get()
    valoreprimo2=float(var_2.get())
    if valore3=="E":
        valorebase2=valoreprimo2*(10**21)
    elif valore3=="P":
        valorebase2=valoreprimo2*(10**18)
    elif valore3=="T":
        valorebase2=valoreprimo2*(10**15)
    elif valore3=="G":
        valorebase2=valoreprimo2*(10**12)
    elif valore3=="M":
        valorebase2=valoreprimo2*(10**9)
    elif valore3=="k":
        valorebase2=valoreprimo2*(10**6)
    elif valore3=="h":
        valorebase2=valoreprimo2*(10**4)
    elif valore3=="da":
        valorebase2=valoreprimo2*(10**2)
    elif valore3=="u":
        valorebase2=valoreprimo2*(10**0) 
    elif valore3=="d":
        valorebase2=valoreprimo2*(10**-2)
    elif valore3=="c":
        valorebase2=valoreprimo2*(10**-4) 
    elif valore3=="m":
        valorebase2=valoreprimo2*(10**-6) 
    elif valore3=="µ":
        valorebase2=valoreprimo2*(10**-9) 
    elif valore3=="n":
        valorebase2=valoreprimo2*(10**-12) 
    elif valore3=="p":
        valorebase2=valoreprimo2*(10**-15)
    elif valore3=="f":
        valorebase2=valoreprimo2*(10**-18) 
    elif valore3=="a":
        valorebase2=valoreprimo2*(10**-21)

    if valore4=="E":
        valorebase2*=(10**-21) 
    elif valore4=="P":
        valorebase2*=(10**-18) 
    elif valore4=="T":
        valorebase2*=(10**-15) 
    elif valore4=="G":
        valorebase2*=(10**-12) 
    elif valore4=="M":
        valorebase2*=(10**-9) 
    elif valore4=="k":
        valorebase2*=(10**-6) 
    elif valore4=="h":
        valorebase2*=(10**-4) 
    elif valore4=="da":
        valorebase2*=(10**-2) 
    elif valore4=="u":
        valorebase2*=(10**0) 
    elif valore4=="d":
        valorebase2*=(10**2) 
    elif valore4=="c":
        valorebase2*=(10**4)
    elif valore4=="m":
        valorebase2*=(10**6) 
    elif valore4=="µ":
        valorebase2*=(10**9)
    elif valore4=="n":
        valorebase2*=(10**12)
    elif valore4=="p":
        valorebase2*=(10**15)
    elif valore4=="f":
        valorebase2*=(10**18) 
    elif valore4=="a":
        valorebase2*=(10**21)

    risultato2.set(valorebase2)

def calcolo3(*args):
    valore5=Prumisura5.get()
    valore6=Prumisura6.get()
    valoreprimo3=float(var_3.get())
    if valore5=="E":
        valorebase3=valoreprimo3*(10**24)
    elif valore5=="P":
        valorebase3=valoreprimo3*(10**21)
    elif valore5=="T":
        valorebase3=valoreprimo3*(10**18)
    elif valore5=="G":
        valorebase3=valoreprimo3*(10**15)
    elif valore5=="M":
        valorebase3=valoreprimo3*(10**12)
    elif valore5=="k":
        valorebase3=valoreprimo3*(10**9)
    elif valore5=="h":
        valorebase3=valoreprimo3*(10**6)
    elif valore5=="da":
        valorebase3=valoreprimo3*(10**3)
    elif valore5=="u":
        valorebase3=valoreprimo3*(10**0) 
    elif valore5=="d":
        valorebase3=valoreprimo3*(10**-3)
    elif valore5=="c":
        valorebase3=valoreprimo3*(10**-6) 
    elif valore5=="m":
        valorebase3=valoreprimo3*(10**-9) 
    elif valore5=="µ":
        valorebase3=valoreprimo3*(10**-12) 
    elif valore5=="n":
        valorebase3=valoreprimo3*(10**-15) 
    elif valore5=="p":
        valorebase3=valoreprimo3*(10**-18)
    elif valore5=="f":
        valorebase3=valoreprimo3*(10**-21) 
    elif valore5=="a":
        valorebase3=valoreprimo3*(10**-24)

    if valore6=="E":
        valorebase3*=(10**-24) 
    elif valore6=="P":
        valorebase3*=(10**-21) 
    elif valore6=="T":
        valorebase3*=(10**-18) 
    elif valore6=="G":
        valorebase3*=(10**-15) 
    elif valore6=="M":
        valorebase3*=(10**-12) 
    elif valore6=="k":
        valorebase3*=(10**-9) 
    elif valore6=="h":
        valorebase3*=(10**-6) 
    elif valore6=="da":
        valorebase3*=(10**-3) 
    elif valore6=="u":
        valorebase3*=(10**0) 
    elif valore6=="d":
        valorebase3*=(10**3) 
    elif valore6=="c":
        valorebase3*=(10**6)
    elif valore6=="m":
        valorebase3*=(10**9) 
    elif valore6=="µ":
        valorebase3*=(10**12)
    elif valore6=="n":
        valorebase3*=(10**15)
    elif valore6=="p":
        valorebase3*=(10**18)
    elif valore6=="f":
        valorebase3*=(10**21) 
    elif valore6=="a":
        valorebase3*=(10**24)

    risultato3.set(valorebase3)


def reset(*args):                                                                           
 clear = ""
 var_1.set(clear)
 var_2.set(clear)
 var_3.set(clear)
 risultato.set(clear)
 risultato2.set(clear)
 risultato3.set(clear)
 Umisura.set(OptionList[0])
 Prumisura.set(OptionList2[8])
 Prumisura2.set(OptionList2[8])
 Prumisura3.set(OptionList2[8])
 Prumisura4.set(OptionList2[8])
 Prumisura5.set(OptionList2[8])
 Prumisura6.set(OptionList2[8])


root=Tk()
root.title("Calcolatrice Equivalenze")
root.geometry("650x750")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


var_1=StringVar()
var_2=StringVar()
var_3=StringVar()
Umisura = StringVar()

Prumisura = StringVar()
Prumisura2 = StringVar()

Prumisura3 = StringVar()
Prumisura4 = StringVar()

Prumisura5 = StringVar()
Prumisura6 = StringVar()

risultato = StringVar()
risultato2 = StringVar()
risultato3 = StringVar()

var1_entry=Entry(root, width=3, textvariable=var_1, font=('verdana', 50))
var1_entry.place(height=100, x=5, y=80)

var2_entry=Entry(root, width=3, textvariable=var_2, font=('verdana', 50))
var2_entry.place(height=100, x=5, y=290)

var3_entry=Entry(root, width=3, textvariable=var_3, font=('verdana', 50))
var3_entry.place(height=100, x=5, y=500)


Label(root, text="Equivalenze", font=('verdana', 20)).pack(anchor=N)
Label(root, text="Spazio (m^2)", font=('verdana', 15)).place(height=30, x=5, y=250)
Label(root, text="Spazio (m^3)", font=('verdana', 15)).place(height=30, x=5, y=460)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=100)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=310)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=520)



Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=260, y=110)
Label(root, textvariable=risultato2, font=('verdana', 20)).place(height=30, x=260, y=320)
Label(root, textvariable=risultato3, font=('verdana', 20)).place(height=30, x=260, y=530)


Button(root, text="CALCOLA", command=calcolo, font=('verdana', 15)).place(height=25, x=5, y=190)
Button(root, text="CALCOLA", command=calcolo2, font=('verdana', 15)).place(height=25, x=5, y=400)
Button(root, text="CALCOLA", command=calcolo3, font=('verdana', 15)).place(height=25, x=5, y=610)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=710)


OptionList = ["Spazio (m)", "Massa (g)"]
OptionList2 = ["E", "P", "T", "G", "M", "k", "h", "da", "u", "d", "c", "m", "µ", "n", "p", "f", "a"]

Umisura.set(OptionList[0])
Prumisura.set(OptionList2[8])
Prumisura2.set(OptionList2[8])
Prumisura3.set(OptionList2[8])
Prumisura4.set(OptionList2[8])
Prumisura5.set(OptionList2[8])
Prumisura6.set(OptionList2[8])

opt = OptionMenu(root, Umisura, *OptionList)
opt.config(width=10, font=('verdana', 12))
opt.place(height=30, x=5, y=40)

opt2 = OptionMenu(root, Prumisura, *OptionList2)
opt2.config(width=2, font=('verdana', 12))
opt2.place(height=60, x=150, y=122)

opt3 = OptionMenu(root, Prumisura2, *OptionList2)
opt3.config(width=2, font=('verdana', 12))
opt3.place(height=60, x=580, y=137)

opt3 = OptionMenu(root, Prumisura3, *OptionList2)
opt3.config(width=2, font=('verdana', 12))
opt3.place(height=60, x=150, y=330)

opt4 = OptionMenu(root, Prumisura4, *OptionList2)
opt4.config(width=2, font=('verdana', 12))
opt4.place(height=60, x=580, y=350)

opt5 = OptionMenu(root, Prumisura5, *OptionList2)
opt5.config(width=2, font=('verdana', 12))
opt5.place(height=60, x=150, y=540)

opt6 = OptionMenu(root, Prumisura6, *OptionList2)
opt6.config(width=2, font=('verdana', 12))
opt6.place(height=60, x=580, y=560)

root.bind('<Return>', calcolo)
root.bind('<Return>', calcolo2)
root.bind('<Return>', calcolo3)
root.bind('<Return>', reset)

root.mainloop()