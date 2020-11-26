import pickle

while True:
    try:
        with open("biudzetas.pkl", "rb") as pickle_in:
            biudzetas = pickle.load(pickle_in)
            suma = 0
            for skaicius, irasas in enumerate(biudzetas):
                suma += irasas
                print(skaicius, irasas)
            print("Biudžeto balansas", suma)
    except:
        print("Nepavyko nuskaityti failo")
        biudzetas = []

    irasas = float(input("Įveskite pajamas arba išlaidas"))
    biudzetas.append(irasas)

    try:
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(biudzetas, pickle_out)
    except:
        print("Nepavyko įrašyti failo")
    uzklausimas = input("Norite dar įvesti duomenų? taip/ne")
    if uzklausimas == "taip":
        continue
    else:
        break
