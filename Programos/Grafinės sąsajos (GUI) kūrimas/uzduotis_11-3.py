
# Patobulinti 2 užduoties programą, kad ji:
# Turėtų meniu, kuriame:
# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys


from tkinter import *

import sys

pagrindinis_langas = Tk()
paskutinis = "Nebuvo įvesta"

def pasisveikinti(event):
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")
    global paskutinis
    paskutinis = uzrasas2["text"]

def isvalyti():
    uzrasas2["text"] = ""

def atkurti():
    uzrasas2["text"] = paskutinis

def uzdaryti(event):
    pagrindinis_langas.withdraw()
    sys.exit()

def uzdaryti2():
    pagrindinis_langas.withdraw()
    sys.exit()

# Laukų, mygtukų formavimas
uzrasas1 = Label(pagrindinis_langas, text="Įveskite vardą")
ivedimas1 = Entry(pagrindinis_langas)
mygtukas1 = Button(pagrindinis_langas, text="Patvirtinti")
mygtukas1.bind("<Button-1>", pasisveikinti)
ivedimas1.bind("<Return>", pasisveikinti)
uzrasas2 = Label(pagrindinis_langas, text="")

# Meniu:
meniu = Menu(pagrindinis_langas)
pagrindinis_langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)

submeniu.add_command(label="Išvalyti", command = isvalyti)
submeniu.add_command(label="Atkurti paskutinį", command = atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command = uzdaryti2)

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
pagrindinis_langas.mainloop()