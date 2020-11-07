from tkinter import *
from tkinter import ttk
uno=""
due=""
controllo=0
controllo_op=0
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
    
def somma():
    global controllo, controllo_op
    controllo=1
    operatore.set("+")
    controllo_op=1
    



root=Tk()
primo=StringVar()
secondo=StringVar()
operatore=StringVar()
root.title("Radice|Potenza")
root.geometry("500x500")
Label(root, textvariable=operatore, font=('verdana', 15)).place(height=20, x=470, y=30)
Label(root, textvariable=primo, font=('verdana', 15)).place(height=20, x=5, y=10)
Button(root, text="0", command=num_0, font=('verdana', 15)).place(height=25, x=5, y=390)
Button(root, text="1", command=num_1, font=('verdana', 15)).place(height=25, x=5, y=360)
Button(root, text="2", command=num_2, font=('verdana', 15)).place(height=25, x=35, y=360)
Button(root, text="3", command=num_3, font=('verdana', 15)).place(height=25, x=65, y=360)
Button(root, text="4", command=num_4, font=('verdana', 15)).place(height=25, x=5, y=330)
Button(root, text="5", command=num_5, font=('verdana', 15)).place(height=25, x=35, y=330)
Button(root, text="6", command=num_6, font=('verdana', 15)).place(height=25, x=65, y=330)
Button(root, text="7", command=num_7, font=('verdana', 15)).place(height=25, x=5, y=300)
Button(root, text="8", command=num_8, font=('verdana', 15)).place(height=25, x=35, y=300)
Button(root, text="9", command=num_9, font=('verdana', 15)).place(height=25, x=65, y=300)
Button(root, text="+", command=somma, font=('verdana', 15)).place(height=25, x=165, y=300)




root.bind('<Return>', num_1)

root.mainloop()

print("ciao")