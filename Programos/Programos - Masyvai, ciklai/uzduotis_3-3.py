
zodziai = []
ivedimas = (input("Įveskite žodį: "))

while ivedimas != "":
    zodziai.append(ivedimas)
    ivedimas = (input("Įveskite žodį: "))

for zodis in zodziai:
    print(f"{zodziai.index(zodis) + 1}: {zodis}, simbolių kiekis: {len(zodis)}")
print("Žodžių kiekis:", len(zodziai))


# paprasčiau:

# zodziai = []

# for i in range(5):
    # zodziai.append(input("Įveskite žodį: "))

# for zodis in zodziai:
    # print(zodis, len(zodis), zodziai.index(zodis))
