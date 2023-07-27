import tkinter as tk
import pickle


class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"


def nuskaityti_pkl():
    try:
        with open("asmenys.pkl", 'rb') as file:
            asmenys = pickle.load(file)
    except:
        asmenys = []
    return asmenys


asmenys = nuskaityti_pkl()


def irasyti_pkl():
    with open("asmenys.pkl", 'wb') as file:
        pickle.dump(asmenys, file)


def ivesti():
    vardas = vardas_entry.get()
    pavarde = pavarde_entry.get()
    asmuo = Asmuo(vardas, pavarde)
    asmenys.append(asmuo)
    irasyti_pkl()
    asmenys_listbox.delete(0, tk.END)
    asmenys_listbox.insert(tk.END, *asmenys)


def istrinti():
    indeksas = asmenys_listbox.curselection()[0]
    del asmenys[indeksas]
    irasyti_pkl()
    asmenys_listbox.delete(0, tk.END)
    asmenys_listbox.insert(tk.END, *asmenys)


window = tk.Tk()
window.geometry("180x250")
vardas_label = tk.Label(window, text="Vardas")
vardas_entry = tk.Entry(window)
pavarde_label = tk.Label(window, text="Pavardė")
pavarde_entry = tk.Entry(window)
ivedimas_button = tk.Button(window, text="Įvesti", command=ivesti)
trinti_button = tk.Button(window, text="Ištrinti", command=istrinti)
asmenys_listbox = tk.Listbox(window)
asmenys_listbox.insert(tk.END, *asmenys)

vardas_label.grid(row=0, column=0)
vardas_entry.grid(row=0, column=1)
pavarde_label.grid(row=1, column=0)
pavarde_entry.grid(row=1, column=1)
ivedimas_button.grid(row=2, column=0)
trinti_button.grid(row=2, column=1)
asmenys_listbox.grid(row=3, columnspan=2)

window.mainloop()
