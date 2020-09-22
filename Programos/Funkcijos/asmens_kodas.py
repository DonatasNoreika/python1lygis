def grazinti_asmens_kodo_kontrolinį(asmens_kodas):
    kodas = str(asmens_kodas)
    A = int(kodas[0])
    B = int(kodas[1])
    C = int(kodas[2])
    D = int(kodas[3])
    E = int(kodas[4])
    F = int(kodas[5])
    G = int(kodas[6])
    H = int(kodas[7])
    I = int(kodas[8])
    J = int(kodas[9])
    S = A * 1 + B * 2 + C * 3 + D * 4 + E * 5 + F * 6 + G * 7 + H * 8 + I * 9 + J * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = A * 3 + B * 4 + C * 5 + D * 6 + E * 7 + F * 8 + G * 9 + H * 1 + I * 2 + J * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def asmens_kodo_validacija(asmens_kodas):
    paskutinis_sk = int(str(asmens_kodas)[-1])
    return paskutinis_sk == grazinti_asmens_kodo_kontrolinį(asmens_kodas)


def asmens_kodo_generavimas(lytis, gimimo_data, eiles_numeris):
    pirmas_skaicius = ""

    data_split = gimimo_data.split("-")
    metai = int(data_split[0][:2])

    if lytis == "vyras":
        pirmas_skaicius = str((int(metai) - 18) * 2 + 1)
    else:
        pirmas_skaicius = str((int(metai) - 18) * 2 + 2)

    metai = data_split[0][2:]
    menuo = data_split[1]
    diena = data_split[2]

    be_paskutinio = pirmas_skaicius + metai + menuo + diena + eiles_numeris

    return int(be_paskutinio + str(grazinti_asmens_kodo_kontrolinį(be_paskutinio)))


print(asmens_kodo_validacija(45102129987))
print(asmens_kodo_validacija(61907108400))

print(asmens_kodo_generavimas("vyras", "2000-12-12", "512"))
