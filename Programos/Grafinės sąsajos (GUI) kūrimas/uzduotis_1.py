from tkinter import Tk, Label, Entry, Button, Menu, StringVar, W, E, SUNKEN

langas = Tk()

atkurimui = StringVar()


def pasisveikinti():
    rezultatas1["text"] = f"Labas, {laukas1.get()}!"
    status["text"] = "Sukurta"


def isvalyti():
    atkurimui.set(laukas1.get())
    laukas1.delete(0, 'end')
    rezultatas1["text"] = ""
    status["text"] = "Išvalyta"


def atkurti():
    laukas1.insert(0, atkurimui.get())
    pasisveikinti()
    status["text"] = "Atkurta"


def iseiti():
    langas.destroy()


uzrasas1 = Label(langas, text="Įveskite vardą")
laukas1 = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti", command=pasisveikinti)
laukas1.bind("<Return>", lambda e: pasisveikinti())
rezultatas1 = Label(langas, text="")
status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)

# Meniu:
meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
rezultatas1.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W + E)

langas.mainloop()
