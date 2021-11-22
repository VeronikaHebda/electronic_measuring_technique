from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import numpy as np

window = Tk()
window.geometry("1000x600")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text = "Zadanie 1")
notebook.add(tab2, text = "Zadanie 2")
notebook.pack(expand = True, fill = "both")


############### zakladka 1
def obliczNg0 (lamb):
    lamb = lamb/1000
    Ng0 = 287.6155 + (4.8866 / (lamb ** 2)) + (0.0680 / (lamb ** 4))
    return Ng0
def obliczlol (obl_Ng0):
    ng0 = obl_Ng0/10**6 + 1
    return ng0

#wykres1
fala = np.arange(400, 1601, 10)
fig = Figure(figsize=(6, 4), dpi=100)  # matplotlib Figure
fig,ax = plt.subplots()
ax.plot(fala, obliczNg0(fala))
ax.set_title("Wykres zależności współczynnika Ng0 od długości fali")
ax.grid()
plt.close()
canvas = FigureCanvasTkAgg(fig, master=tab1)  # master = jakastam_frame
canvas.get_tk_widget().place(x=30,y=50)
canvas.draw()  # w funkcji rysowania


###scroll i tabelka
sc = Scrollbar(tab1)
sc.pack(side = RIGHT, fill = Y)
my_game = ttk.Treeview(tab1,height = 20, yscrollcommand = sc.set)
my_game['columns'] = ('fala', 'Ng0')
my_game.column("#0", width=0,  stretch=NO)
my_game.column("fala",anchor=CENTER, width=80)
my_game.column("Ng0",anchor=W,width=150)
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("fala",text="Długość fali",anchor=CENTER)
my_game.heading("Ng0",text="Ng0",anchor=CENTER)

for i in range (0,121):
    my_game.insert(parent='',index='end',iid=i,text='',
    values=(str(fala[i]),str(obliczNg0(fala)[i])))

my_game.place(x = 700, y = 50)
sc.config( command = my_game.yview )

y = obliczlol(obliczNg0(fala))
def wstaw1():
    ax.clear()
    ax.plot(fala, obliczNg0(fala))  #rysowanie
    ax.grid()
    ax.set_title("Wykres zależności współczynnika Ng0 od długości fali")
    canvas.draw()
    for i in range(0, 121):
        my_game.delete(i)
        my_game.insert(parent='', index='end', iid=i, text='',
        values=(str(fala[i]), str(obliczNg0(fala)[i])))
def wstaw2():
    ax.clear()
    ax.plot(fala, y)  # rysowanie
    ax.ticklabel_format(useOffset=False)
    ax.grid()
    ax.set_title("Wykres zależności współczynnika ng0 od długości fali")
    canvas.draw()
    for i in range(0, 121):
        my_game.delete(i)
        my_game.insert(parent='', index='end', iid=i, text='',
        values=(str(fala[i]), str(y[i])))


button_Ng0 = Button(tab1,text = "Ng0",font = ("Ariel",13), command= wstaw1)
button_Ng0.place(x = 30, y = 10)
button_ng0 = Button(tab1,text = "ng0",font = ("Ariel",13), command= wstaw2)
button_ng0.place(x = 80, y = 10)


####zakladka2




tkinter.mainloop()
