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

def open_program_pytagora():
    os.system('"%s"' %"single programs\pytagora.py")

def open_program_matrici3x3():
    os.system('"%s"' %"single programs\matrice3x3.py")

def open_program_matrici2x2():
    os.system('"%s"' %"single programs\matrici2x2.py")

def open_program_sistema2x2():
    os.system('"%s"' %"single programs\Sistema2x2.py")

def open_program_sistema3x3():
    os.system('"%s"' %"single programs\Sistema3x3.py")

def open_program_equivalenze():
    os.system('"%s"' %"single programs\equivalenze.py")

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Lorem Ipsum")
   button.pack()
   
root = Tk()
root.geometry("500x500")
root.title("Calcolatrice")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Matematica base", menu=filemenu)
filemenu.add_command(label="Somma|Sottrazione", command=open_program_somma)
filemenu.add_command(label="Moltiplicazione|Divisione", command=open_program_moltdiv)
filemenu.add_command(label="Potenza|Radice", command=open_program_potenza)


filemenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Algebra", menu=filemenu2)
filemenu2.add_command(label="Matrice2x2", command=open_program_matrici2x2)
filemenu2.add_command(label="Matrice3x3", command=open_program_matrici3x3)
filemenu2.add_command(label="Cramer2x2", command=open_program_sistema2x2)
filemenu2.add_command(label="Cramer3x3", command=open_program_sistema3x3)


filemenu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fisica", menu=filemenu3)
filemenu3.add_command(label="Equivalenze", command=open_program_equivalenze)


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Geometria", menu=editmenu)
editmenu.add_command(label="Area Triangolo", command=open_program_areatriangolo)
editmenu.add_command(label="Area Poligoni reg", command=open_program_areapol)
editmenu.add_command(label="Area & 2p Cerchio", command=open_program_cerchio)
editmenu.add_command(label="Pitagora", command=open_program_pytagora)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=root.quit)


root.config(menu=menubar)

root.bind('<Return>', open_program_somma)
root.mainloop()