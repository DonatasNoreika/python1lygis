import calendar
import datetime


def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3


def saraso_suma(sarasas):
    return sum(sarasas)


def didziausias_skaicius(*args):
    return max(args)


def stringas_atbulai(stringas):
    return stringas[::-1]


def info_apie_sakini(stringas):
    zodziai = len(stringas.split())
    print(f"Šiame sakinyje yra {zodziai} žodžių")
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    print(f"Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}")
    return zodziai, didziosios, mazosios, skaiciai


def unikalus_sarasas(sarasas):
    return list(set(sarasas))


def ar_pirminis(skaicius):
    if skaicius > 1:
        for num in range(2, skaicius):
            if skaicius % num == 0:
                return False
        return True
    return False


def isrikiuoti_nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    return " ".join(zodziai)


def ar_keliamieji(metai):
    return calendar.isleap(metai)


def patikrinti_data(sukaktis, dabar=datetime.datetime.now()):
    ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
    skirtumas = dabar - ivesta_data

    metai = skirtumas.days // 365
    menesiai = round(skirtumas.days / 365 * 12)
    savaites = round(skirtumas.days // 7)
    dienos = skirtumas.days
    valandos = round(skirtumas.total_seconds() / 3600)
    minutes = round(skirtumas.total_seconds() / 60)
    sekundes = round(skirtumas.total_seconds())

    print("Praėjo metų: ", metai)
    print("Praėjo mėnesių: ", menesiai)
    print("Praėjo savaičių: ", savaites)
    print("Praėjo dienų: ", dienos)
    print("Praėjo valandų: ", valandos)
    print("Praėjo minučių: ", minutes)
    print("Praėjo sekundžių: ", sekundes)
    return metai, menesiai, savaites, dienos, valandos, minutes, sekundes
