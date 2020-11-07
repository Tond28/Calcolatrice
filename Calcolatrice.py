from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def open_program_somma():
    os.system('"%s"' %"single programs\somma-sottrazione.py")

def open_program_moltdiv():
    os.system('"%s"' %"single programs\moltdiv.py")

def open_program_potenza():
    os.system('"%s"' %"single programs\Potenza-Radice.py")

def open_program_areapol():
    os.system('"%s"' %"single programs\Area_Poligoni.py")

def open_program_areatriangolo():
    os.system('"%s"' %"single programs\Areatrriangolo.py")

def open_program_cerchio():
    os.system('"%s"' %"single programs\pigreco.py")

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
filemenu.add_command(label="Potenza|Radice", command=open_program_potenza)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Geometria", menu=editmenu)
editmenu.add_command(label="Area Triangolo", command=open_program_areatriangolo)
editmenu.add_command(label="Area Poligoni reg", command=open_program_areapol)
editmenu.add_command(label="Area & 2p Cerchio", command=open_program_cerchio)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=root.quit)


root.config(menu=menubar)

root.mainloop()
