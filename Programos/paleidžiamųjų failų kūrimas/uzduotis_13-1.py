
import calendar

ivesti_metai_nuo = int(input("Įveskite datą nuo.. "))
ivesti_metai_iki = int(input("Įveskite datą iki.. "))

def keliamieji_metai(metai_nuo, metai_iki):
    for metai in range(metai_nuo, metai_iki):
        if calendar.isleap(metai):
            print(metai)

keliamieji_metai(ivesti_metai_nuo, ivesti_metai_iki)

input("Norėdami uždaryti spauskite ENTER")