from tkinter import *
from tkinter import ttk


root=Tk()
root.title("About")
root.geometry("600x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

Label(root, text="Calcolatrice creata da: Gaetano Citarella, Filippo Tondelli", font=('verdana', 15)).place(height=25, x=0, y=0)
Label(root, text="Questo programma è stato ideato per fare calcoli di: \nMatematica di Base, Algebra, Fisica, Geometria, Geometria Solida.", font=('verdana', 10)).place(height=40, x=70, y=30)
Label(root, text="RILASCIATA VERSIONE 1.0", font=('verdana', 20), fg='#ff0000').place(height=40, x=115, y=70)

frames = [PhotoImage(file='images/spalla2.gif',format = 'gif -index %i' %(i)) for i in range(40)]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind>39:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

label = Label(root)
label.place(height=200, x=230, y=240)
root.after(0, update, 0)

root.mainloop()
