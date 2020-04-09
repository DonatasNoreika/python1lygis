
from dbcon import *
from tkinter import Tk, Frame, Label, Entry, Button, Listbox, SINGLE, END

asmuo_edit = False
get_all_records_list()

def update_fields():
    boksas.delete(0, END)
    boksas.insert(END, *get_all_records_list())
    laukas1.delete(0, 'end')
    laukas2.delete(0, 'end')
    laukas3.delete(0, 'end')
    laukas1.focus()

def ui_add(event):
    global asmuo_edit
    if asmuo_edit:
        update_record(asmuo_edit.id, laukas1.get(), laukas2.get(), laukas3.get())
        asmuo_edit = False
    else:
        add_record(laukas1.get(), laukas2.get(), laukas3.get())
    update_fields()

def ui_delete():
    aktyvus = get_all_records_list()[boksas.curselection()[0]]
    delete_record(aktyvus.id)
    update_fields()

def ui_edit():
    global asmuo_edit
    asmuo_edit = get_all_records_list()[boksas.curselection()[0]]
    update_fields()
    laukas1.insert(0, asmuo_edit.name)
    laukas2.insert(0, asmuo_edit.surname)
    laukas3.insert(0, asmuo_edit.age)

# Graphic Objects initialization
main_window = Tk()
main_window.title("Asmenų katalogas")
# main_window.iconbitmap(r'asmenys.ico')
top_frame = Frame(main_window)
button_frame = Frame(main_window)
boksas = Listbox(button_frame, selectmode=SINGLE)
boksas.insert(END, *get_all_records_list())
uzrasas1 = Label(top_frame, text="Įveskite asmenį", width=40)
laukas1 = Entry(top_frame)
laukas1_uzr = Label(top_frame, text="Vardas")
laukas2 = Entry(top_frame)
laukas2_uzr = Label(top_frame, text="Pavardė")
laukas3 = Entry(top_frame)
laukas3_uzr = Label(top_frame, text="Amžius")
mygtukas1 = Button(top_frame, text="Įvesti")
mygtukas1.bind("<Button-1>", ui_add)
laukas1.bind("<Return>", ui_add)
laukas2.bind("<Return>", ui_add)
laukas3.bind("<Return>", ui_add)
mygtukas2 = Button(top_frame, text="Redaguoti", command=ui_edit)
mygtukas3 = Button(top_frame, text="Ištrinti", command=ui_delete)

# Graphic Objects visualization
uzrasas1.grid(row=0, columnspan=2)
laukas1_uzr.grid(row=1, column=0)
laukas1.grid(row=1, column=1)
laukas2_uzr.grid(row=2, column=0)
laukas2.grid(row=2, column=1)
laukas3_uzr.grid(row=3, column=0)
laukas3.grid(row=3, column=1)
mygtukas1.grid(row=4, columnspan=2, sticky="E")
mygtukas2.grid(row=4, columnspan=2)
mygtukas3.grid(row=4, columnspan=2, sticky="W")
boksas.pack()
top_frame.pack()
button_frame.pack()
main_window.mainloop()
