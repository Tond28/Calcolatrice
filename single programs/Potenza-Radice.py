from tkinter import *
from tkinter import ttk


def potenza(*args):
 try:
     base_1=float(bas_1.get())
     esponente_1=float(esp_1.get())
     risultato.set(base_1**esponente_1)

 except ValueError:
     risultato.set("ERRORE")
     pass


def radice(*args):
 try:
     base_2=float(bas_2.get())
     esponente_2=float(esp_2.get())
     risultato2.set(base_2**(1/esponente_2))
     
 except ValueError:
     risultato2.set("ERRORE")
     pass


def reset(*args):                                                                           
 clear = ""
 bas_1.set(clear)
 esp_1.set(clear)
 bas_2.set(clear)
 esp_2.set(clear)
 risultato.set(clear)
 risultato2.set(clear)


root=Tk()
root.title("Radice|Potenza")
root.geometry("500x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


bas_1=StringVar()
bas_2=StringVar()
esp_1=StringVar()
esp_2=StringVar()
risultato=StringVar()
risultato2=StringVar()


pot1_entry=Entry(root, width=3, textvariable=bas_1, font=('verdana', 50))
pot1_entry.place(height=100, x=5, y=70)


pot2_entry=Entry(root, width=3, textvariable=esp_1, font=('verdana', 25))
pot2_entry.place(height=50, x=140, y=40)

Label(root, text="√", font=('verdana', 105)).place(height=210, x=15, y=230)

rad1_entry=Entry(root, width=3, textvariable=bas_2, font=('verdana', 50))
rad1_entry.place(height=100, x=125, y=300)


rad2_entry=Entry(root, width=3, textvariable=esp_2, font=('verdana', 25))
rad2_entry.place(height=50, x=10, y=270)


Label(root, text="Potenza", font=('verdana', 20)).pack(anchor=N)
Label(root, text="Radice", font=('verdana', 20)).place(height=30, x=120, y=230)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=140, y=100)
Label(root, text="=", font=('verdana', 20)).place(height=50, x=270, y=325)

Label(root, textvariable=risultato, font=('verdana', 18)).place(height=30, x=170, y=114)
Label(root, textvariable=risultato2, font=('verdana', 18)).place(height=30, x=300, y=335)

Button(root, text="CALCOLA POTENZA", command=potenza, font=('verdana', 15)).place(height=25, x=5, y=180)
Button(root, text="CALCOLA RADICE", command=radice, font=('verdana', 15)).place(height=25, x=5, y=420)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=255, y=465)


root.bind('<Return>', potenza)
root.bind('<Return>', radice)
root.bind('<Return>', reset)


root.mainloop()