from tkinter import *
from tkinter import ttk


root=Tk()
root.title("About")
root.geometry("600x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

Label(root, text="Calcolatrice creata da: Gaetano Citarella, Filippo Tondelli", font=('verdana', 10)).place(height=20, x=0, y=0)
Label(root, text="Versione programma: 0.2.9", font=('verdana', 10)).place(height=20, x=0, y=25)
Label(root, text="Questo programma è stato ideato per fare calcoli di: \nMatematica di Base, Algebra, Fisica, Geometria, Geometria Solida.", font=('verdana', 10)).place(height=40, x=1, y=45)
Label(root, text="^ATTUALMENTE IN AGGIORNAMENTO^", font=('verdana', 10)).place(height=20, x=165, y=90)

root.mainloop()
