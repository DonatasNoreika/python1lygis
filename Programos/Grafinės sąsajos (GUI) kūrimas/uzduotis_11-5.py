
# Perdaryti bet kurią ankstesnėse pamokose sukurtą programą, kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja

from tkinter import *
import calendar

pagrindinis_langas = Tk()

def tikrinti(event):
    ivesta = int(ivedimas1.get())
    print(type(ivesta))
    if calendar.isleap(ivesta):
        uzrasas2["text"] = (f"{ivesta} metai yra keliamieji!")
    else:
        uzrasas2["text"] = (f"{ivesta} metai yra nekeliamieji!")

def uzdaryti(event):
    pagrindinis_langas.withdraw()
    sys.exit()

# Laukų, mygtukų formavimas
uzrasas1 = Label(pagrindinis_langas, text="Įveskite metus")
ivedimas1 = Entry(pagrindinis_langas)
mygtukas1 = Button(pagrindinis_langas, text="Patvirtinti")
mygtukas1.bind("<Button-1>", tikrinti)
ivedimas1.bind("<Return>", tikrinti)
pagrindinis_langas.bind("<Escape>", uzdaryti)
uzrasas2 = Label(pagrindinis_langas, text="")

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)
pagrindinis_langas.mainloop()