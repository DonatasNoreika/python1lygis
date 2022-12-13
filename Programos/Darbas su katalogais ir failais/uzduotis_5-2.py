while True:
    ivestas = input("Įveskite tekstą: ")
    tekstas += ivestas + "\n"
    if not ivestas:
        break

failo_pav = input("Įveskite failo pavadinimą")

with open(f"{failo_pav}.txt", 'w') as file:
    file.write(tekstas)
