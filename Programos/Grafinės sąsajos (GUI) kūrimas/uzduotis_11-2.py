
# Patobulinti 1 užduoties programą, kad ji:
# Įvedus vardą, atspausdintų "Labas, {vardas}!" ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"


from tkinter import *

import sys

pagrindinis_langas = Tk()
paskutinis = "Nebuvo įvesta"

def pasisveikinti(event):
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")
    global paskutinis
    paskutinis = uzrasas2["text"]

# Laukų, mygtukų formavimas
uzrasas1 = Label(pagrindinis_langas, text="Įveskite vardą")
ivedimas1 = Entry(pagrindinis_langas)
mygtukas1 = Button(pagrindinis_langas, text="Patvirtinti")
mygtukas1.bind("<Button-1>", pasisveikinti)
ivedimas1.bind("<Return>", pasisveikinti)
uzrasas2 = Label(pagrindinis_langas, text="")

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
pagrindinis_langas.mainloop()