# Patobulinti 3 užduoties programą, kad ji:
# Turėtų statuso juostą apačioje, kurioje:
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas
# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą

from tkinter import *

langas = Tk()
issaugotas = StringVar()


def pasisveikinti():
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")
    status["text"] = "Pasisveikinta"


def iseiti():
    langas.destroy()


def isvalyti():
    ivesta = ivedimas1.get()
    issaugotas.set(ivesta)
    uzrasas2["text"] = ""
    ivedimas1.delete(0, END)
    ivedimas1.focus()
    status["text"] = "Išvalyta"

def atkurti():
    ivedimas1.delete(0, END)
    ivedimas1.insert(0, issaugotas.get())
    pasisveikinti()
    status["text"] = "Atkurta"

# Laukų, mygtukų formavimas
uzrasas1 = Label(langas, text="Įveskite vardą")
ivedimas1 = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti", command=pasisveikinti)
langas.bind("<Return>", lambda e: pasisveikinti())
langas.bind("<Escape>", lambda e: iseiti())
uzrasas2 = Label(langas, text="")
status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)

# Meniu
meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)

submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)
langas.mainloop()
