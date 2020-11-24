sarasas = [6, 98, 159, "zodziai", 5.55, True]

print(sarasas[2])

sarasas.append(888)
print(sarasas)

sarasas.insert(2, "Naujas")
print(sarasas)

sarasas.remove("Naujas")
print(sarasas)

sarasas.clear()
print(sarasas)

amzius = {"Rokas": 20, "Andrius": 34, "Laura": 25}

print(amzius["Laura"])

amzius["Donatas"] = 100
print(amzius)

del amzius["Laura"]
print(amzius)

amzius["Andrius"] = 35
print(amzius)
