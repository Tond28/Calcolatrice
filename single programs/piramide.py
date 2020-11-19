from tkinter import *
from tkinter import ttk


def calcoloareaT(*args):
 try:
        lato1=float(lat1.get())
        apotema=float(apo.get())
        areab = lato1**2
        p = 4*lato1
        areal = ((p*apotema)/2)
        risultato.set(areal + areab)


 except ValueError:
        risultato.set("ERRORE")
        pass

def calcolovolume(*args):
 try:
        altezza=float(alt.get())
        lato1=float(lat1.get())
        apotema=float(apo.get())
        p = 4*lato1
        areal = ((p*apotema)/2)
        risultato2.set((areal*altezza)/3)


 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):
    clear = ""
    lat1.set(clear)
    alt.set(clear)
    apo.set(clear)
    risultato.set(clear)
    risultato2.set(clear)


root=Tk()
root.title("Parallelepipedo")
root.geometry("600x700")


lat1=StringVar()
alt=StringVar()
apo=StringVar()
risultato=StringVar()
risultato2=StringVar()


lat1_entry=Entry(root, width=3, textvariable=lat1, font=('verdana', 50))
lat1_entry.place(height=100, x=5, y=100)


apo_entry=Entry(root, width=3, textvariable=apo, font=('verdana', 50))
apo_entry.place(height=100, x=5, y=260)


alt_entry=Entry(root, width=3, textvariable=alt, font=('verdana', 50))
alt_entry.place(height=100, x=5, y=420)


Label(root, text="AREA:", font=('verdana', 15)).place(height=20, x=5, y=565)
Label(root, text="VOLUME:", font=('verdana', 15)).place(height=20, x=5, y=625)
Label(root, text="Calcolo Area e Volume Piramide", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Lato di base:", font=('verdana', 20)).place(height=50, x=5, y=50)
Label(root, text="Apotema:", font=('verdana', 20)).place(height=50, x=5, y=210)
Label(root, text="Altezza:", font=('verdana', 20)).place(height=50, x=5, y=370)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=80, y=565)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=20, x=103, y=625)

Button(root, text="CALCOLA AREA TOTALE", command=calcoloareaT, font=('verdana', 15)).place(height=25, x=5, y=530)
Button(root, text="CALCOLA VOLUME", command=calcolovolume, font=('verdana', 15)).place(height=25, x=5, y=590)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=660)


root.bind('<Return>', calcoloareaT)
root.bind('<Return>', calcolovolume)
root.bind('<Return>', reset)


root.mainloop()