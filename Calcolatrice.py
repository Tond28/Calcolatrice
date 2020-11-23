from tkinter import *
from tkinter import ttk, Canvas
from tkinter import filedialog
import os
import time

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

def open_program_helpindex():
    os.system('"%s"' %"single programs\help.py")

def open_program_about():
    os.system('"%s"' %"single programs\info.py")

def open_program_forze():
    os.system('"%s"' %"single programs\orzef.py")

def open_program_forze2():
    os.system('"%s"' %"single programs\orzef2.py")

def open_program_Momento():
    os.system('"%s"' %"single programs\Momento.py")

def open_program_Dinamica():
    os.system('"%s"' %"single programs\elfillov.py")

def open_program_coseno():
    os.system('"%s"' %"single programs\sin-cos-tan.py")

def open_program_cubo():
    os.system('"%s"' %"single programs\cubo.py")

def open_program_tilt():
    os.system('"%s"' %"single programs\parallelepipedo.py")

def open_program_velocita():
    os.system('"%s"' %"single programs\con-velocita.py")

def open_program_sfera():
    os.system('"%s"' %"single programs\sfera.py")

def open_program_randomico():
    os.system('"%s"' %"single programs\domclasseran.py")

def open_program_piramide():
    os.system('"%s"' %"single programs\piramide.py")

def open_program_cono():
    os.system('"%s"' %"single programs\cono.py")

def open_program_percentuale():
    os.system('"%s"' %"single programs\percentuale.py")

def open_program_massa():
    os.system('"%s"' %"single programs\massa.py")

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Lorem Ipsum")
   button.pack()
   
root=Tk()

primo=StringVar()
secondo=StringVar()
operatore=StringVar()
risultatoout=StringVar()
root.title("Calcolatrice")
root.geometry("500x500")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Matematica base", menu=filemenu)
filemenu.add_command(label="Somma|Sottrazione", command=open_program_somma)
filemenu.add_command(label="Moltiplicazione|Divisione", command=open_program_moltdiv)
filemenu.add_command(label="Potenza|Radice", command=open_program_potenza)
filemenu.add_command(label="Percentuale", command=open_program_percentuale)

filemenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Algebra", menu=filemenu2)
filemenu2.add_command(label="Matrice2x2", command=open_program_matrici2x2)
filemenu2.add_command(label="Matrice3x3", command=open_program_matrici3x3)
filemenu2.add_command(label="Cramer2x2", command=open_program_sistema2x2)
filemenu2.add_command(label="Cramer3x3", command=open_program_sistema3x3)
filemenu2.add_command(label="Random", command=open_program_randomico)

filemenu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fisica", menu=filemenu3)
filemenu3.add_command(label="Equivalenze", command=open_program_equivalenze)
filemenu3.add_command(label="Forze", command=open_program_forze)
filemenu3.add_command(label="Forze 2", command=open_program_forze2)
filemenu3.add_command(label="Momenti Forze", command=open_program_Momento)
filemenu3.add_command(label="Dinamica", command=open_program_Dinamica)
filemenu3.add_command(label="Converititore velocità", command=open_program_velocita)
filemenu3.add_command(label="Massa", command=open_program_massa)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Geometria", menu=editmenu)
editmenu.add_command(label="Area Triangolo", command=open_program_areatriangolo)
editmenu.add_command(label="Area Poligoni reg", command=open_program_areapol)
editmenu.add_command(label="Area & 2p Cerchio", command=open_program_cerchio)
editmenu.add_command(label="Pitagora", command=open_program_pytagora)
editmenu.add_command(label="Coseno, Seno, Tangente", command=open_program_coseno)

editmenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Geometria Solida", menu=editmenu2)
editmenu2.add_command(label="Cubo", command=open_program_cubo)
editmenu2.add_command(label="Parallelepipedo", command=open_program_tilt)
editmenu2.add_command(label="Sfera", command=open_program_sfera)
editmenu2.add_command(label="Piramide", command=open_program_piramide)
editmenu2.add_command(label="Cono", command=open_program_cono)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=open_program_helpindex)
helpmenu.add_command(label="About...", command=open_program_about)
helpmenu.add_command(label="Lorem Ipsum", command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)



frames = [PhotoImage(file='images/spalla2.gif',format = 'gif -index %i' %(i)) for i in range(40)]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind>39:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)





ans_out=0
uno=""
due=""

controllo=0
controllo_op=0
punto_uno=0
punto_due=0
def num_1(*args):
    global uno, due
    if controllo==0:
        uno=uno+"1"
        primo.set(uno)
    elif controllo==1:
        due=due+"1"
        secondo.set(due)

def num_0(*args):
    global uno, due
    if controllo==0:
        uno=uno+"0"
        primo.set(uno)
    elif controllo==1:
        due=due+"0"
        secondo.set(due)

def num_2(*args):
    global uno, due
    if controllo==0:
        uno=uno+"2"
        primo.set(uno)
    elif controllo==1:
        due=due+"2"
        secondo.set(due)

def num_3(*args):
    global uno, due
    if controllo==0:
        uno=uno+"3"
        primo.set(uno)
    elif controllo==1:
        due=due+"3"
        secondo.set(due)

def num_4(*args):
    global uno, due
    if controllo==0:
        uno=uno+"4"
        primo.set(uno)
    elif controllo==1:
        due=due+"4"
        secondo.set(due)

def num_5(*args):
    global uno, due
    if controllo==0:
        uno=uno+"5"
        primo.set(uno)
    elif controllo==1:
        due=due+"5"
        secondo.set(due)

def num_6(*args):
    global uno, due
    if controllo==0:
        uno=uno+"6"
        primo.set(uno)
    elif controllo==1:
        due=due+"6"
        secondo.set(due)

def num_7(*args):
    global uno, due
    if controllo==0:
        uno=uno+"7"
        primo.set(uno)
    elif controllo==1:
        due=due+"7"
        secondo.set(due)

def num_8(*args):
    global uno, due
    if controllo==0:
        uno=uno+"8"
        primo.set(uno)
    elif controllo==1:
        due=due+"8"
        secondo.set(due) 

def num_9(*args):
    global uno, due
    if controllo==0:
        uno=uno+"9"
        primo.set(uno)
    elif controllo==1:
        due=due+"9"
        secondo.set(due) 

def punto(*args):
    global uno, due, punto_uno, punto_due
    if controllo==0 and not "."in uno:
        if uno=="":
            uno=uno+"0."
        else:
            uno=uno+"."
        punto_uno=1
        primo.set(uno)
    elif controllo==1 and not "."in due:
        if due=="":
            due=due+"0."
        else:
            due=due+"."
        punto_due=1
        secondo.set(due)
    
def somma(*args):
    global controllo, controllo_op, uno
    if uno=="":
        uno=uno+"0"
        primo.set(uno)
        controllo=1
        operatore.set("+")
        controllo_op=1
    else:
        controllo=1
        operatore.set("+")
        controllo_op=1

def sottrazione(*args):
    global controllo, controllo_op, uno
    if uno=="":
        uno=uno+"0"
        primo.set(uno)
        controllo=1
        operatore.set("-")
        controllo_op=2
    else:
        controllo=1
        operatore.set("-")
        controllo_op=2

def moltiplicazione(*args):
    global controllo, controllo_op, uno
    if uno=="":
        uno=uno+"0"
        primo.set(uno)
        controllo=1
        operatore.set("x")
        controllo_op=3
    else:
        controllo=1
        operatore.set("x")
        controllo_op=3

def divisione(*args):
    global controllo, controllo_op, uno
    if uno=="":
        uno=uno+"0"
        primo.set(uno)
        controllo=1
        operatore.set("÷")
        controllo_op=4
    else:
        controllo=1
        operatore.set("÷")
        controllo_op=4  

def percentuale(*args):
    global controllo, controllo_op, uno
    if uno=="":
        uno=uno+"0"
        primo.set(uno)
        controllo=1
        operatore.set("%")
        controllo_op=5
    else:
        controllo=1
        operatore.set("%")
        controllo_op=5

def risultato(*args):
    global ans_out
    if controllo_op==1:
        risultato1=float(uno)+float(due)
        risultatoout.set(risultato1)
    elif controllo_op==2:
        risultato1=float(uno)-float(due)
        risultatoout.set(risultato1)
    elif controllo_op==3:
        risultato1=float(uno)*float(due)
        risultatoout.set(risultato1)
    elif controllo_op==4:
        risultato1=float(uno)/float(due)
        risultatoout.set(risultato1)
    elif controllo_op==5:
        if due=="":
            risultato1=(float(uno)*1)/100
            risultatoout.set(risultato1)
        else:
            risultato1=(float(uno)*float(due))/100
            risultatoout.set(risultato1)
    ans_out=risultato1

def cancel(*args):
    global uno, due, controllo, controllo_op
    if controllo==0:
        uno=uno[:-1]
        primo.set(uno)
    elif controllo_op>0 and due=="":
        controllo=0
        operatore.set("")
        controllo_op=0
        risultatoout.set("")
    elif controllo==1:
        if risultato!=0:
            due=due[:-1]
            secondo.set(due)
            risultatoout.set("")
        else:
            due=due[:-1]
            secondo.set(due)

def segno(*args):
    global uno, due
    if controllo==0:
        if "-" in uno:
            uno=uno.replace("-", "")
            primo.set(uno)
        else:
            uno="-"+uno
            primo.set(uno)
    elif controllo==1:
        if "-" in due:
            due=due.replace("-", "")
            secondo.set(due)
        else:
            due="-"+due
            secondo.set(due)
   
def reset():
    global uno, due, controllo_op, controllo
    clear=""
    primo.set(clear)
    secondo.set(clear)
    operatore.set(clear)
    risultatoout.set(clear)
    uno=""
    due=""
    controllo_op=0
    controllo=0

def ans_ris():
    global uno, ans_out
    reset()
    ans_out=str(ans_out)
    uno=uno+str(ans_out)
    primo.set(ans_out)

linea=Canvas(root, width=700, height=300)
linea.pack()

linea.create_line(600, 0, 0, 0, width=(10))
linea.create_line(0, 135, 0, 0, width=(10))
linea.create_line(500, 135, 500, 0, width=(10))
linea.create_line(600, 90, 0, 90, width=(4))
linea.create_line(600, 135, 0, 135, width=(4))

Label(root, textvariable=primo, font=('verdana', 19)).place(height=24, x=5, y=10)
Label(root, textvariable=operatore, font=('verdana', 19)).place(height=24, x=5, y=34)
Label(root, textvariable=secondo, font=('verdana', 19)).place(height=24, x=5, y=61)
Label(root, textvariable=risultatoout, font=('verdana', 19)).place(height=24, x=5, y=100)

Button(root, text=".", command=punto, font=('verdana', 32)).place(height=62, x=65, y=410)
Button(root, text="0", command=num_0, font=('verdana', 30)).place(height=62, x=5, y=410)
Button(root, text="±", command=segno, font=('verdana', 30)).place(height=62, x=121, y=410)

Button(root, text="1", command=num_1, font=('verdana', 30)).place(height=62, x=5, y=350)
Button(root, text="2", command=num_2, font=('verdana', 30)).place(height=62, x=67, y=350)
Button(root, text="3", command=num_3, font=('verdana', 30)).place(height=62, x=129, y=350)

Button(root, text="4", command=num_4, font=('verdana', 30)).place(height=62, x=5, y=290)
Button(root, text="5", command=num_5, font=('verdana', 30)).place(height=62, x=67, y=290)
Button(root, text="6", command=num_6, font=('verdana', 30)).place(height=62, x=129, y=290)

Button(root, text="7", command=num_7, font=('verdana', 30)).place(height=62, x=5, y=230)
Button(root, text="8", command=num_8, font=('verdana', 30)).place(height=62, x=67, y=230)
Button(root, text="9", command=num_9, font=('verdana', 30)).place(height=62, x=129, y=230)

Button(root, text="+", command=somma, font=('verdana', 30)).place(height=62, x=225, y=350)
Button(root, text="-", command=sottrazione, font=('verdana', 31)).place(height=62, x=295, y=350)
Button(root, text="%", command=percentuale, font=('verdana', 32)).place(height=62, x=353, y=350)
Button(root, text="X", command=moltiplicazione, font=('verdana', 32)).place(height=62, x=225, y=290)
Button(root, text="÷", command=divisione, font=('verdana', 25)).place(height=62, x=294, y=290)
Button(root, text="  =  ", command=risultato, font=('verdana', 30)).place(height=62, x=225, y=411)
Button(root, text="DEL", command=reset, font=('verdana', 22)).place(height=62, x=225, y=230)
Button(root, text="C", command=cancel, font=('verdana', 22)).place(height=62, x=306, y=230)
Button(root, text="ANS", command=ans_ris, font=('verdana', 22)).place(height=62, x=351, y=411)

label = Label(root)
label.place(height=110, x=353, y=230)
root.after(0, update, 0)


root.bind('<Return>', risultato)

root.mainloop()

