import pickle
from tkinter import *

langas = Tk()
virsus = Frame(langas)
apacia = Frame(langas)


def gauti_biudzeta():
    try:
        with open("biudzetas.pkl", "rb") as pickle_in:
            biudzetas = pickle.load(pickle_in)
    except:
        biudzetas = []
    return biudzetas


def irasyti_biudzeta(biudzetas):
    try:
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(biudzetas, pickle_out)
    except:
        print("Nepavyko įrašyti failo")


def ivesti_irasa(event):
    suma = int(suma_laukas.get())
    biudzetas = gauti_biudzeta()
    biudzetas.append(suma)
    irasyti_biudzeta(biudzetas)
    boksas.delete(0, END)
    boksas.insert(END, *gauti_biudzeta())
    balansas_uzrasas["text"] = str(sum(gauti_biudzeta()))
    suma_laukas.delete(0, 'end')

def isvalyti():
    biudzetas = []
    irasyti_biudzeta(biudzetas)
    boksas.delete(0, END)

langas.geometry("250x200")
uzrasas1 = Label(virsus, text="Įrašykite sumą")
suma_laukas = Entry(virsus)
mygtukas = Button(virsus, text="Įvesti")
mygtukas.bind("<Button-1>", ivesti_irasa)
langas.bind("<Return>", ivesti_irasa)
mygtukas2 = Button(virsus, text="Išvalyti", command=isvalyti)
balansas_uzrasas_labas = Label(virsus, text="Balansas:")
balansas_uzrasas = Label(virsus, text=str(sum(gauti_biudzeta())))

scrollbaras = Scrollbar(apacia)
boksas = Listbox(apacia, yscrollcommand=scrollbaras.set)
scrollbaras.config(command=boksas.yview)
boksas.insert(END, *gauti_biudzeta())

virsus.pack()
apacia.pack()
uzrasas1.grid(row=0, column=0)
suma_laukas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
scrollbaras.pack(side=RIGHT, fill=Y)
boksas.pack(side=LEFT)
mygtukas2.grid(row=2, column=2)
balansas_uzrasas_labas.grid(row=1, column=1)
balansas_uzrasas.grid(row=1, column=2)
langas.mainloop()
