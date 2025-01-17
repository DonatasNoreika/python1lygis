def gauti_ak_kontrolini(asmens_kodas: str | int) -> int:
    a, b, c, d, e, f, g, h, i, j = map(int, list(str(asmens_kodas)[:-1]))
    S = a * 1 + b * 2 + c * 3 + d * 4 + e * 5 + f * 6 + g * 7 + h * 8 + i * 9 + j * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = a * 3 + b * 4 + c * 5 + d * 6 + e * 7 + f * 8 + g * 9 + h * 1 + i * 2 + j * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def ar_ak_validus(asmens_kodas: str | int) -> bool:
    return int(str(asmens_kodas)[-1]) == gauti_ak_kontrolini(asmens_kodas)


print(ar_ak_validus(45212265291))
print(ar_ak_validus(43311245363))


def ak_generavimas(lytis, data, eilesnr):
    data_split = data.split("-")
    metai1 = data_split[0][:2]

    if lytis == "vyras":
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 1)
    else:
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 2)

    metai2 = data_split[0][2:]
    menuo = data_split[1]
    diena = data_split[2]
    be_paskutinio = pirmas_skaicius + metai2 + menuo + diena + eilesnr
    return int(be_paskutinio + str(gauti_ak_kontrolini(be_paskutinio)))

print(ak_generavimas("vyras", "2000-12-12", "045"))
print(ak_generavimas("vyras", "2000-12-12", "512"))
print(ak_generavimas("moteris", "1995-12-12", "500"))

# Alternatyva (papildytas variantas su datos patikrinimu ir eilės numerio konvertavimu į stringą (pvz. 1 į 001)):

import datetime

def gauti_kontrolini(asmens_kodas: int):
    kodas_str = str(asmens_kodas)
    A = int(kodas_str[0])
    B = int(kodas_str[1])
    C = int(kodas_str[2])
    D = int(kodas_str[3])
    E = int(kodas_str[4])
    F = int(kodas_str[5])
    G = int(kodas_str[6])
    H = int(kodas_str[7])
    I = int(kodas_str[8])
    J = int(kodas_str[9])
    S = A * 1 + B * 2 + C * 3 + D * 4 + E * 5 + F * 6 + G * 7 + H * 8 + I * 9 + J * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = A * 3 + B * 4 + C * 5 + D * 6 + E * 7 + F * 8 + G * 9 + H * 1 + I * 2 + J * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def ar_validus(asmens_kodas: int):
    return int(str(asmens_kodas)[-1]) == gauti_kontrolini(asmens_kodas)

# print(ar_validus(60808119589))
# print(ar_validus(36609239182))
# print(ar_validus(45303278696))

def generuoti_ak(lytis: str, gimimo_data: str, eiles_nr: int) -> int:
    """

    :param lytis: "vyras" arba "moteris"
    :param gimimo_data: formatas: YYYY-MM-DD
    :param eiles_nr: sveikas skaičius iki 999
    :return:
    """
    try:
        datetime.datetime.strptime(gimimo_data, "%Y-%m-%d")
    except:
        return "Neteisingai įvesta data"
    data_split = gimimo_data.split("-")
    metai1 = data_split[0][:2]
    if lytis == "vyras":
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 1)
    else:
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 2)

    metai2 = data_split[0][2:]
    menuo = data_split[1]
    diena = data_split[2]
    eiles_nr = ((3 - len(str(eiles_nr))) * str(0)) + str(eiles_nr)
    be_kontrolinio = pirmas_skaicius + metai2 + menuo + diena + eiles_nr
    return int(be_kontrolinio + str(gauti_kontrolini(int(be_kontrolinio))))

print(generuoti_ak("vyras", "2000-12-31", 955))
print(generuoti_ak("moteris", "1992-02-28", 1))
print(generuoti_ak("vyras", "2010-02-28", 22))
