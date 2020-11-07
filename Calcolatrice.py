from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def open_program_somma():
    os.system('"%s"' %"single programs\somma-sottrazione.py")

def open_program_moltdiv():
    os.system('"%s"' %"single programs\moltdiv.py")

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Lorem Ipsum")
   button.pack()
   
root = Tk()
root.geometry("250x100")
root.title("Calcolatrice")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Matematica base", menu=filemenu)
filemenu.add_command(label="Somma|Sottrazione", command=open_program_somma)
filemenu.add_command(label="Moltiplicazione|Divisione", command=open_program_moltdiv)

filemenu.add_separator()
filemenu.add_command(label="Potenza", command=donothing)
filemenu.add_command(label="Radice", command=donothing)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Geometria", menu=editmenu)
editmenu.add_command(label="Area Triangolo", command=donothing)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=root.quit)


root.config(menu=menubar)

root.bind('<Return>', open_program_somma)
root.mainloop()