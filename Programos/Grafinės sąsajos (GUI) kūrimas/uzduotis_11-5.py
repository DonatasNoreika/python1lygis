# Perdaryti bet kurią ankstesnėse pamokose sukurtą programą, kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja

from tkinter import *
import calendar

langas = Tk()

def tikrinti():
    ivesta = int(ivedimas1.get())
    if calendar.isleap(ivesta):
        uzrasas2["text"] = (f"{ivesta} metai yra keliamieji!")
    else:
        uzrasas2["text"] = (f"{ivesta} metai yra nekeliamieji!")

def uzdaryti():
    langas.destroy()

# Laukų, mygtukų formavimas
uzrasas1 = Label(langas, text="Įveskite metus")
ivedimas1 = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti", command=tikrinti)
ivedimas1.bind("<Return>", lambda event: tikrinti())
langas.bind("<Escape>", lambda event: uzdaryti())
uzrasas2 = Label(langas, text="")

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
langas.mainloop()
