# Sukurti programą su grafine sąsaja, kuri:
# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

from tkinter import *

langas = Tk()

def pasisveikinti():
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")

# Laukų, mygtukų formavimas
uzrasas1 = Label(langas, text="Įveskite vardą")
ivedimas1 = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti", command = pasisveikinti)
uzrasas2 = Label(langas, text="")

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
langas.mainloop()
