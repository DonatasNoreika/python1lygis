from tkinter import *

window = Tk()
window.geometry("270x65")
window.title("Pasisveikinimas")

name = StringVar()


# functions
def greet():
    user_name = entry1.get()
    name.set(user_name)
    label_result['text'] = f"Labas, {user_name}"
    status_label['text'] = "sukurta"


def clear_ui():
    entry1.delete(0, END)
    label_result["text"] = ""
    status_label['text'] = "išvalyta"


def revert():
    entry1.insert(0, name.get())
    greet()
    status_label['text'] = "atkurta"


def exit():
    window.quit()


# objects
label1 = Label(window, text="Įveskite vardą: ")
entry1 = Entry(window)
button1 = Button(window, text="Patvirtinti", command=greet)
window.bind("<Return>", lambda e: greet())
window.bind("<Escape>", lambda e: exit())
label_result = Label(window, text="")
status_label = Label(window, text="", bd=1, relief=SUNKEN, anchor=W)

# menus
my_menu = Menu(window)
window.config(menu=my_menu)
submeniu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Menu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=clear_ui)
submeniu.add_command(label="Atkurti", command=revert)
submeniu.add_command(label="Išeiti", command=exit)

# packing
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=0, column=2)
label_result.grid(row=1, columnspan=3)
status_label.grid(row=2, columnspan=3, sticky=W + E)
window.mainloop()
