from tkinter import *
from tkinter import ttk


def calcolo(*args):
 try:
     pass


 except ValueError:
     pass


def reset(*args):
 pass


root=Tk()
root.title("Help Index")
root.geometry("600x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

h = StringVar()
Umisura = StringVar()

h_entry=Entry(root, width=3, textvariable=h, font=('verdana', 50))
h_entry.place(height=100, x=5, y=100)


Label(root, text="Diamo sempre un titolo ai nostri lavori!", font=('verdana', 10)).place(height=20, x=260, y=50)
Label(root, text="Prende gli input richiesti e li elabora", font=('verdana', 10)).place(height=20, x=5, y=200)
Label(root, text="Calcola i dati secondo la funzione del programma", font=('verdana', 10)).place(height=20, x=5, y=310)
Label(root, text="Pulisce il programma riportandolo allo stadio iniziale pronto per un nuovo calcolo", font=('verdana', 10)).place(height=20, x=5, y=477)
Label(root, text="Classico menù a tendina", font=('verdana', 10)).place(height=20, x=405, y=400)
Label(root, text="Titolo", font=('verdana', 20)).place(height=50, x=260, y=0)


Label(root, text="Input:", font=('verdana', 20)).place(height=50, x=5, y=50)


Button(root, text="CALCOLA", command=calcolo, font=('verdana', 15)).place(height=25, x=5, y=280)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=5, y=450)

OptionList = ["1", "2", "3"]
Umisura.set(OptionList[0])
opt = OptionMenu(root, Umisura, *OptionList)
opt.config(width=10, font=('verdana', 12))
opt.place(height=30, x=405, y=370)


root.bind('<Return>', calcolo)
root.bind('<Return>', reset)


root.mainloop()