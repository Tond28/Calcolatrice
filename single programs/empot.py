from tkinter import *
from tkinter import ttk

def calcolo(*args):
    valore1=tempo_el1.get()
    valore2=tempo_el2.get()
    valoreprimo=float(var_1.get())
    if valore1=="millenni":
        valorebase=valoreprimo*1000*365*24
    elif valore1=="secoli":
        valorebase=valoreprimo*100*365*24
    elif valore1=="decenni":
        valorebase=valoreprimo*10*365*24
    elif valore1=="lustri":
        valorebase=valoreprimo*5*365*24
    elif valore1=="anni bisestili":
        valorebase=valoreprimo*366*24
    elif valore1=="anni":
        valorebase=valoreprimo*365*24
    elif valore1=="settimane":
        valorebase=valoreprimo*7*24
    elif valore1=="giorni":
        valorebase=valoreprimo*24
    elif valore1=="ore":
        valorebase=valoreprimo
    elif valore1=="minuti":
        valorebase=valoreprimo/60
    elif valore1=="secondi":
        valorebase=(valoreprimo/60)/60
    
    if valore2=="millenni":
        valorebase/=(1000*365*24)
    elif valore2=="secoli":
        valorebase/=(100*365*24)
    elif valore2=="decenni":
        valorebase/=(10*365*24)
    elif valore2=="lustri":
        valorebase/=(5*365*24)
    elif valore2=="anni bisestili":
        valorebase/=(24*366)
    elif valore2=="anni":
        valorebase/=(24*365)
    elif valore2=="settimane":
        valorebase=valorebase/(7*24)
    elif valore2=="giorni":
        valorebase/=24
    elif valore2=="ore":
        valorebase=valorebase
    elif valore2=="minuti":
        valorebase*=60
    elif valore2=="secondi":
        valorebase*=(60*60)

    risultato.set(valorebase)

def reset(*args):                                                                           
    clear = ""
    var_1.set(clear)
    risultato.set(clear)
    tempo_el1.set(list_tempo[8])
    tempo_el2.set(list_tempo[8])



root=Tk()
root.title("Conversione Tempo")
root.geometry("650x350")


var_1=StringVar()

Umisura = StringVar()

tempo_el1 = StringVar()
tempo_el2 = StringVar()

risultato = StringVar()

var1_entry=Entry(root, width=3, textvariable=var_1, font=('verdana', 50))
var1_entry.place(height=100, x=5, y=80)



Label(root, text="Conversione Tempo", font=('verdana', 20)).pack(anchor=N)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=100)
Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=260, y=110)

Button(root, text="CALCOLA", command=calcolo, font=('verdana', 15)).place(height=25, x=5, y=190)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=300)

list_tempo = ["millenni", "secoli","decenni", "lustri", "anni bisestili", "anni","settimane", "giorni", "ore", "minuti", "secondi"]

tempo_el1.set(list_tempo[8])
tempo_el2.set(list_tempo[8])

opt1 = OptionMenu(root, tempo_el1, *list_tempo)
opt1.config(width=10, font=('verdana', 12))
opt1.place(height=60, x=150, y=140)

opt2 = OptionMenu(root, tempo_el2, *list_tempo)
opt2.config(width=10, font=('verdana', 12))
opt2.place(height=60, x=510, y=140)


root.bind('<Return>', calcolo)
root.bind('<Return>', reset)

root.mainloop()


