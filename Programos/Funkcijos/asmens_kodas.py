def gauti_ak_kontrolini(asmens_kodas: str | int) -> int:
    a, b, c, d, e, f, g, h, i, j = map(int, list(str(asmens_kodas)[:10]))
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


def gauti_ak_kontrolini(asmens_kodas: str | int) -> int:
    a, b, c, d, e, f, g, h, i, j = map(int, list(str(asmens_kodas)[:10]))
    S = a * 1 + b * 2 + c * 3 + d * 4 + e * 5 + f * 6 + g * 7 + h * 8 + i * 9 + j * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = a * 3 + b * 4 + c * 5 + d * 6 + e * 7 + f * 8 + g * 9 + h * 1 + i * 2 + j * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def generuoti_ak(lytis, gimimo_data, eiles_nr):
    data_split = gimimo_data.split("-")
    metai1 = data_split[0][:2]

    if lytis == "vyras":
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 1)
    if lytis == "moteris":
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 2)

    metai2 = data_split[0][2:]
    menuo = data_split[1]
    diena = data_split[2]
    eile_str = str(eiles_nr).zfill(3)
    ak_be_kontrolinio = pirmas_skaicius + metai2 + menuo + diena + eile_str
    return ak_be_kontrolinio + str(gauti_ak_kontrolini(ak_be_kontrolinio))


print(generuoti_ak("moteris", "2000-01-05", 50))

# Alternatyva (papildytas variantas su datos patikrinimu ir eilės numerio konvertavimu į stringą (pvz. 1 į 001)):

import datetime


def gauti_ak_kontrolini(asmens_kodas: str | int) -> int:
    a, b, c, d, e, f, g, h, i, j = map(int, list(str(asmens_kodas)[:10]))
    S = a * 1 + b * 2 + c * 3 + d * 4 + e * 5 + f * 6 + g * 7 + h * 8 + i * 9 + j * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = a * 3 + b * 4 + c * 5 + d * 6 + e * 7 + f * 8 + g * 9 + h * 1 + i * 2 + j * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def generuoti_ak(lytis: str, gimimo_data: str, eiles_nr: int) -> str | int:
    """
    Generuoja LT asmens kodą pagal įvestus parametrus
    :param lytis: "vyras" arba "moteris"
    :param gimimo_data: formatas: "YYYY-MM-DD"
    :param eiles_nr: sveikas skaičius nuo 1 iki 999
    :return: sugeneruotas asmens kodas arba klaida
    """
    try:
        datetime.datetime.strptime(gimimo_data, "%Y-%m-%d")
    except:
        return "Neteisingai įvesta data. Formatas: YYYY-MM-DD"

    if int(eiles_nr) < 1 or int(eiles_nr) > 999:
        return "Neteisingai įvestas eilės nr. Ribos: 1 - 999"

    data_split = gimimo_data.split("-")
    metai1 = data_split[0][:2]
    if lytis == "vyras":
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 1)
    elif lytis == "moteris":
        pirmas_skaicius = str((int(metai1) - 18) * 2 + 2)
    else:
        return 'Neteisingai pasirinkta lytis. Variantai: "vyras", "moteris"'

    metai2 = data_split[0][2:]
    menuo = data_split[1].zfill(2)
    diena = data_split[2].zfill(2)
    eile_str = str(eiles_nr).zfill(3)
    ak_be_kontrolinio = pirmas_skaicius + metai2 + menuo + diena + eile_str
    return int(ak_be_kontrolinio + str(gauti_ak_kontrolini(ak_be_kontrolinio)))


print(generuoti_ak("vyras", "2000-02-05", 663))


