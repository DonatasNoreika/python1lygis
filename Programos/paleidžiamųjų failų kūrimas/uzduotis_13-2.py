
# Patobulinti 3 užduoties programą, kad ji:
# Turėtų statuso juostą apačioje, kurioje:
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas
# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą

from tkinter import *

import sys

pagrindinis_langas = Tk()
paskutinis = "Nebuvo įvesta"
pagrindinis_langas.title("Sveikinimas")
pagrindinis_langas.iconbitmap(r'sveikinimas.ico')

def pasisveikinti(event):
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")
    global paskutinis
    paskutinis = uzrasas2["text"]
    status["text"] = "Sukurta"

def isvalyti():
    uzrasas2["text"] = ""
    status["text"] = "Išvalyta"

def atkurti():
    uzrasas2["text"] = paskutinis
    status["text"] = "Atkurta"

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
pagrindinis_langas.bind("<Escape>", uzdaryti)
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

# Status juosta
status = Label(pagrindinis_langas, text="", bd=1, relief=SUNKEN, anchor=W)

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)
pagrindinis_langas.mainloop()