from tkinter import *
from tkinter import ttk


def calcoloarea(*args):
 try:
        profondita=float(prof.get())
        altezza=float(alt.get())
        base=float(bas.get())
        risultato.set(2*(base*profondita)+2*(base*altezza)+2*(profondita*altezza))


 except ValueError:
        risultato.set("ERRORE")
        pass

def calcolovolume(*args):
 try:
        profondita=float(prof.get())
        altezza=float(alt.get())
        base=float(bas.get())
        risultato2.set(profondita*base*altezza)


 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):
    clear = ""
    prof.set(clear)
    alt.set(clear)
    bas.set(clear)
    risultato.set(clear)
    risultato2.set(clear)


root=Tk()
root.title("Parallelepipedo")
root.geometry("600x700")



prof=StringVar()
alt=StringVar()
bas=StringVar()
risultato=StringVar()
risultato2=StringVar()


bas_entry=Entry(root, width=3, textvariable=bas, font=('verdana', 50))
bas_entry.place(height=100, x=5, y=100)


prof_entry=Entry(root, width=3, textvariable=prof, font=('verdana', 50))
prof_entry.place(height=100, x=5, y=260)


alt_entry=Entry(root, width=3, textvariable=alt, font=('verdana', 50))
alt_entry.place(height=100, x=5, y=420)


Label(root, text="AREA:", font=('verdana', 15)).place(height=20, x=5, y=565)
Label(root, text="VOLUME:", font=('verdana', 15)).place(height=20, x=5, y=625)
Label(root, text="Calcolo Area e Volume Parallelepipedo", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Base:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Profondità:", font=('verdana', 20)).place(height=50, x=5, y=210)
Label(root, text="Altezza:", font=('verdana', 20)).place(height=50, x=5, y=370)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=80, y=565)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=103, y=625)

Button(root, text="CALCOLA AREA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=530)
Button(root, text="CALCOLA VOLUME", command=calcolovolume, font=('verdana', 15)).place(height=25, x=5, y=590)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=660)


root.bind('<Return>', calcoloarea)
root.bind('<Return>', calcolovolume)
root.bind('<Return>', reset)


root.mainloop