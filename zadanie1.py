from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import numpy as np
from math import e


window = Tk()
window.geometry("990x590")
window.title("Etp 1")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1, text = "Zadanie 1")
notebook.add(tab2, text = "Zadanie 2")
notebook.add(tab3, text = "Zadanie 3")
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
ax = fig.add_subplot(xlabel = "Długość fali w nm", ylabel = "Współczynnik")
ax.plot(fala, obliczNg0(fala))
ax.set_title("Wykres zależności współczynnika Ng0 od długości fali")
ax.grid()
canvas = FigureCanvasTkAgg(fig, master=tab1)  # master = jakastam_frame
canvas.get_tk_widget().place(x=30,y=50)
canvas.draw()  # w funkcji rysowania

toolbar = NavigationToolbar2Tk(canvas,tab1)
toolbar.place(x = 220, y = 460)


###scroll i tabelka
sc = Scrollbar(tab1)
sc.pack(side = RIGHT, fill = Y)
my_game = ttk.Treeview(tab1,height = 19, yscrollcommand = sc.set)
my_game['columns'] = ('fala', 'Ng0')
my_game.column("#0", width=0,  stretch=NO)
my_game.column("fala",anchor=CENTER, width=80)
my_game.column("Ng0",anchor=W,width=150)
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("fala",text="Długość fali w nm",anchor=CENTER)
my_game.heading("Ng0",text="Ng0",anchor=CENTER)

a = obliczNg0(fala)
y = obliczlol(obliczNg0(fala))
for i in range (0,121):
    a[i] = "{:.12f}".format(a[i])
    y[i] = "{:.12f}".format(y[i])

for i in range (0,121):
    my_game.insert(parent='',index='end',iid=i,text='',
    values=(str(fala[i]),str(a[i])))

my_game.place(x = 670, y = 50)
sc.config( command = my_game.yview )


def wstaw1():
    ax.clear()
    ax.plot(fala, obliczNg0(fala))  #rysowanie
    ax.grid()
    ax.set_title("Wykres zależności współczynnika Ng0 od długości fali")
    canvas.draw()
    for i in range(0, 121):
        my_game.delete(i)
        my_game.insert(parent='', index='end', iid=i, text='',
        values=(str(fala[i]), str(a[i])))
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

label1 = Label(tab2,text = "Długość fali [nm]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label2 = Label(tab2,text = "Temperatura sucha [C]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label3 = Label(tab2,text = "Temperatura mokra [C]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label4= Label(tab2,text = "Ciśnienie [hPa]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label5 = Label(tab2,text = "Poprawka na km [mm]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label6 = Label(tab2,text = "Poprawka od mierz. dł. [mm]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label7 = Label(tab2,text = "Długość poprawiona [m]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)
label8= Label(tab2,text = "Długość pomierzona [m]: ", font=("Ariel",13,'bold'), fg='black', bd=10, padx=5, pady=5)

label1.place(x = 20, y = 50)
label2.place(x = 20, y = 100)
label3.place(x = 20, y = 150)
label4.place(x = 20, y = 200)
label5.place(x = 540, y = 50)
label6.place(x = 540, y = 100)
label7.place(x = 540, y = 150)
label8.place(x = 20, y = 250)

entry1 = Entry(tab2, font = ("Ariel",15), width = 12)
entry2 = Entry(tab2, font = ("Ariel",15), width = 12)
entry3 = Entry(tab2, font = ("Ariel",15), width = 12)
entry4 = Entry(tab2, font = ("Ariel",15), width = 12)
entry5 = Entry(tab2, font = ("Ariel",15), width = 15)
entry6 = Entry(tab2, font = ("Ariel",15), width = 15)
entry7 = Entry(tab2, font = ("Ariel",15), width = 15)
entry8 = Entry(tab2, font = ("Ariel",15), width = 12)

entry1.place(x = 240, y = 60)
entry2.place(x = 240, y = 110)
entry3.place(x = 240, y = 160)
entry4.place(x = 240, y = 210)
entry5.place(x = 790, y = 60)
entry6.place(x = 790, y = 110)
entry7.place(x = 790, y = 160)
entry8.place(x = 240, y = 260)




def oblicz():
    lam = float(entry1.get())
    temp_sucha = float(entry2.get())
    T = temp_sucha + 273.15
    temp_mokra = float(entry3.get())
    cis = float(entry4.get())
    m = float(entry8.get())
    Ng02 = obliczNg0(lam)
    Ew = 6.1078 * e **((17.269*temp_mokra)/(237.30+temp_mokra))
    e2 = Ew - 0.000662*cis*(temp_sucha-temp_mokra)
    Nrz = Ng02 * 0.269578 * (cis/T) - 11.27*(e2/T)
    Ngs = Ng02 * 0.269578 * (1013.25/288.15) - 11.27*(10.87/288.15)
    D = Ngs - Nrz
    print(D)
    P = D*(m/1000)
    P = "{:.15f}".format(P)[:15]
    P = float(P)
    print(P)
    Pp = m + P
    print(Pp)
    D = "{:.15f}".format(D)[:15]
    Pp = "{:.15f}".format(Pp)[:15]
    entry5.insert(0,D)
    entry6.insert(0, P)
    entry7.insert(0, Pp)

button_oblicz = Button(tab2,text = "Oblicz",font = ("Ariel",15), command= oblicz)
button_oblicz.place(x = 430, y = 120)

####zakladka3
odl = np.arange(1, 101, 1)
r = 6371
roznica = -(odl**3/(24*(8*r)**2)) * 1000000
#wykres1
fig1 = Figure(figsize=(6, 4), dpi=100)  # matplotlib Figure
ax1 = fig1.add_subplot(xlabel = "Długość w km", ylabel = "Różnica w mm")
ax1.plot(odl, roznica)
ax1.set_title("Wykres różnicy długości między łukiem a cięciwą")
ax1.grid()
canvas1 = FigureCanvasTkAgg(fig1, master=tab3)  # master = jakastam_frame
canvas1.get_tk_widget().place(x=30,y=50)
canvas1.draw()  # w funkcji rysowania
ax1.ticklabel_format(useOffset=False)

toolbar1 = NavigationToolbar2Tk(canvas1,tab3)
toolbar1.place(x = 220, y = 460)


###scroll i tabelka
sc1 = Scrollbar(tab3)
sc1.pack(side = RIGHT, fill = Y)
zad3 = ttk.Treeview(tab3,height = 19, yscrollcommand = sc1.set)
zad3['columns'] = ('fala', 'Ng0')
zad3.column("#0", width=0,  stretch=NO)
zad3.column("fala",anchor=CENTER, width=80)
zad3.column("Ng0",anchor=W,width=150)
zad3.heading("#0",text="",anchor=CENTER)
zad3.heading("fala",text="Dystans w km",anchor=CENTER)
zad3.heading("Ng0",text="Różnica w mm",anchor=CENTER)

for i in range (0,100):
    roznica[i] = "{:.15f}".format(roznica[i])
for i in range (0,100):
    zad3.insert(parent='',index='end',iid=i,text='',
    values=(odl[i],str(roznica[i])))

zad3.place(x = 670, y = 50)
sc1.config( command = zad3.yview )

tkinter.mainloop()
