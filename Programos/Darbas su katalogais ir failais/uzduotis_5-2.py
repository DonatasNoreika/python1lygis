tekstas = ""

while True:
    pirmas = input("Įveskite eilutę: ")
    if pirmas != "":
        tekstas += pirmas + "\n"
    else:
        break

failo_pavadinimas = input("Įveskite failo pavadinimą: ")

with open(failo_pavadinimas + ".txt", "w", encoding="UTF-8") as failas:
    failas.write(tekstas)
