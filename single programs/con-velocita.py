from tkinter import *
from tkinter import ttk

def calcolo(*args):
    valore_t1=tempo_t1.get()
    valore_t2=tempo_t2.get()
    valore_s1=spazio_t1.get()
    valore_s2=spazio_t2.get()
    valoreprimo=float(var_1.get())
    valoretempo=1
    if valore_t1=="y":
        valoretempo*=365*24
    elif valore_t1=="d":
        valoretempo*=24
    elif valore_t1=="h":
        valoretempo=1
    elif valore_t1=="min":
        valoretempo/=60
    elif valore_t1=="s":
        valoretempo/=60*60
    
    if valore_t2=="y":
        valoretempo/=(24*365)
    elif valore_t2=="d":
        valoretempo/=24
    elif valore_t2=="h":
        valoretempo=valoretempo
    elif valore_t2=="min":
        valoretempo*=60
    elif valore_t2=="s":
        valoretempo*=(60*60)

    

    if valore_s1=="Km":
        valorespazio=valoreprimo*(10**3)
    elif valore_s1=="Hm":
        valorespazio=valoreprimo*(10**2)
    elif valore_s1=="Dam":
        valorespazio=valoreprimo*(10**1)
    elif valore_s1=="m":
        valorespazio=valoreprimo*(10**0) 
    elif valore_s1=="dm":
        valorespazio=valoreprimo*(10**-1)
    elif valore_s1=="cm":
        valorespazio=valoreprimo*(10**-2) 
    elif valore_s1=="mm":
        valorespazio=valoreprimo*(10**-3) 

    if valore_s2=="Km":
        valorespazio*=(10**-3) 
    elif valore_s2=="Hm":
        valorespazio*=(10**-2) 
    elif valore_s2=="Dam":
        valorespazio*=(10**-1) 
    elif valore_s2=="m":
        valorespazio*=(10**0) 
    elif valore_s2=="dm":
        valorespazio*=(10**1) 
    elif valore_s2=="cm":
        valorespazio*=(10**2)
    elif valore_s2=="mm":
        valorespazio*=(10**3) 

    out=valorespazio/valoretempo
    risultato.set(out)
    



def reset(*args):                                                                           
    clear = ""
    var_1.set(clear)
    risultato.set(clear)
    tempo_t1.set(list_tempo[2])
    tempo_t2.set(list_tempo[2])
    spazio_t1.set(list_spazio[3])
    spazio_t2.set(list_spazio[3])



root=Tk()
root.title("Conversione Spazio/Tempo")
root.geometry("650x350")


var_1=StringVar()

Umisura = StringVar()

tempo_t1 = StringVar()
tempo_t2 = StringVar()
spazio_t1 = StringVar()
spazio_t2=StringVar()
risultato = StringVar()

var1_entry=Entry(root, width=3, textvariable=var_1, font=('verdana', 50))
var1_entry.place(height=100, x=5, y=80)



Label(root, text="Conversione Tempo", font=('verdana', 20)).pack(anchor=N)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=230, y=100)
Label(root, text="/", font=('verdana', 25)).place(height=70, x=213, y=130)
Label(root, text="/", font=('verdana', 25)).place(height=70, x=553, y=130)
Label(root, textvariable=risultato, font=('verdana', 20)).place(height=30, x=260, y=110)

Button(root, text="CALCOLA", command=calcolo, font=('verdana', 15)).place(height=25, x=5, y=190)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=550, y=300)

list_spazio=["Km", "Hm", "Dam", "m", "dm", "cm", "mm"]
list_tempo = ["y","d", "h", "min", "s"]


tempo_t1.set(list_tempo[2])
tempo_t2.set(list_tempo[2])
spazio_t1.set(list_spazio[3])
spazio_t2.set(list_spazio[3])

opt1 = OptionMenu(root, tempo_t1, *list_tempo)
opt1.config(width=2, font=('verdana', 12))
opt1.place(height=60, x=230, y=140)

opt2 = OptionMenu(root, tempo_t2, *list_tempo)
opt2.config(width=2, font=('verdana', 12))
opt2.place(height=60, x=570, y=140)

opt3 = OptionMenu(root, spazio_t1, *list_spazio)
opt3.config(width=2, font=('verdana', 12))
opt3.place(height=60, x=150, y=140)

opt3 = OptionMenu(root, spazio_t2, *list_spazio)
opt3.config(width=2, font=('verdana', 12))
opt3.place(height=60, x=490, y=140)


root.bind('<Return>', calcolo)
root.bind('<Return>', reset)

root.mainloop()

