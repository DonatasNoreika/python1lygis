
sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą

# suma = sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
# print(suma)

# arba

stringai = sum(x for x in sarasas if type(x) is int or type(x) is float)
print(stringai)

# Sudėtų ir atspausdintų visus sąrašo žodžius
#
# sakinys = filter(lambda x: type(x) is str, sarasas)
# print(" ".join(sakinys))

# arba

sakinys = [x for x in sarasas if type(x) is str]
print(" ".join(sakinys))

# Suskaičiuotų ir atspausdintų, kiek sąrašę yra loginių (boolean)
# kintamųjų su True reikšme

# rezultatas = len(list(filter(lambda x: x == True, sarasas)))
# print(rezultatas)

# arba

rezultatas = sum(x for x in sarasas if x == True)
print(rezultatas)
