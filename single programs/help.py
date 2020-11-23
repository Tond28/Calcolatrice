from tkinter import *
from tkinter import ttk


def callback(*args):
    programma=Umisura.get()
    if programma=="Somma|Sottrazione":
        selected.set("Programma semplice compreso nella matematica base\nSvolge somma e sottrazione")
    elif programma=="Moltiplicazione|Divisione":
        selected.set("Programma semplice compreso nella matematica base\nSvolge Moltiplicazioni e divisioni")
    elif programma=="Potenza|Radice":
        selected.set("Programma semplice compreso nella matematica base\nSvolge Potenze e radici di qualsiasi grado")
    elif programma=="Percentuale":
        selected.set("Programma compreso nella matematica base\nCalcola la percentuale e l'inverso")
    elif programma=="Matrice2x2|Matrice3x3":
        selected.set("Programma compreso in Algebra\nEsegue il calcolo matrici delle matrici 2x2 e 3x3")
    elif programma=="Random":
        selected.set("Programma compreso in Algebra\nEsegue l'estrazione randomica di un numero")
    elif programma=="Equivalenze":
        selected.set("Programma compreso in Fisica\nCalcola la conversione tra diverse unità di misura\nAnche con valore al quadrato e al cubo")
    elif programma=="Forze":
        selected.set("Programma compreso in Fisica\nCalcola forza peso, forza d'attrito e forza elastica")
    elif programma=="Forze2":
        selected.set("Programma compreso in Fisica\nCalcola la forza d'equilibrio")
    elif programma=="Momenti Forze":
        selected.set("Programma compreso in Fisica\nCalcola i momenti in fisica")
    elif programma=="Dinamica":
        selected.set("Programma compreso in Fisica\nCalcola la velocità e l'accelerazione")
    elif programma=="Convertitore Velocità":
        selected.set("Programma compreso in Fisica\nConverte una velocità in diverse unità di misura")
    elif programma=="Area triangolo":
        selected.set("Programma compreso in Geometria\nCalcola l'area di un triangolo")
    elif programma=="Area poligono reg.":
        selected.set("Programma compreso in Fisica\nCalcola l'area di qualsiasi poligono regolare\nesclusivamente con più di 3 lati")
    elif programma=="Area e perimetro cerchio":
        selected.set("Programma compreso in Geometria\nCalcola l'area e il perimetro di un cerchio raggio")
    elif programma=="Pitagora":
        selected.set("Programma compreso in Geometria\nCalcola il teorema di pitagora\nCalcola il teorema di pitagora inverso")
    elif programma=="Coseno Seno Tangente":
        selected.set("Programma compreso in Geometria\nCalcola il Seno, Coseno e Tangente di un angolo")
    elif programma=="Cubo":
        selected.set("Programma compreso in Geometria Solida\nCalcola Volume e perimetro di un cubo")
    elif programma=="Parallelepipedo":
        selected.set("Programma compreso in Geometria Solida\nVol. e 2p di un parallelepipedo a base rettangolare")
    elif programma=="Sfera":
        selected.set("Programma compreso in Geometria Solida\nCalcola Volume e perimetro di una sfera")
    elif programma=="Piramide":
        selected.set("Programma compreso in Geometria Solida\nCalcola Vol. e 2p di una piramide a base quadrata")
    elif programma=="Cono":
        selected.set("Programma compreso in Geometria Solida\nCalcola Volume e perimetro di un cono")

root=Tk()

root.title("Help Index")
root.geometry("600x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

frames = [PhotoImage(file='images/spalla2.gif',format = 'gif -index %i' %(i)) for i in range(40)]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind>39:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


selected = StringVar()
Umisura = StringVar()
Label(root, textvariable=selected, font=('verdana', 16), fg="blue").place(height=200, x=10, y=100)
Label(root, text="Help\nSelezionare il programmma per avere la descrizione", font=('verdana', 16)).place(height=50, x=10, y=2)
help_=["", "Somma|Sottrazione", "Moltiplicazione|Divisione", "Potenza|Radice", "Percentuale", 
"Matrice2x2|Matrice3x3", "Random",
"Equivalenze", "Forze", "Forze2", "Momenti Forze", "Dinamica", "Convertitore Velocità",
"Area triangolo", "Area poligono reg.", "Area e perimetro cerchio", "Pitagora", "Coseno Seno Tangente", "Cubo", "Parallelepipedo", "Sfera", "Piramide", "Cono"]

list_help = ttk.Combobox(root, width = 27, value=help_, textvariable = Umisura) 

list_help.bind("<<ComboboxSelected>>", callback)

label = Label(root)
label.place(height=110, x=450, y=60)
root.after(0, update, 0)


list_help.place(height=30, x=200, y=70)
list_help.current(0)  

root.mainloop()
