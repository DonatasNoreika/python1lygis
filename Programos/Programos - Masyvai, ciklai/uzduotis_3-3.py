zodziai = []

while True:
    ivedimas = (input("Įveskite žodį: "))
    if ivedimas == "":
        break
    zodziai.append(ivedimas)

for numeris, zodis in enumerate(zodziai):
    print(f"{numeris + 1}: {zodis}, simbolių kiekis: {len(zodis)}")
print("Žodžių kiekis:", len(zodziai))


# paprasčiau:

# zodziai = []

# for i in range(5):
    # zodziai.append(input("Įveskite žodį: "))

# for zodis in zodziai:
    # print(zodis, len(zodis), zodziai.index(zodis))
