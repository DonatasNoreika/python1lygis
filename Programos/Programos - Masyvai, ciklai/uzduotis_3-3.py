

zodziai = []

ivedimas = (input("Įveskite žodį: "))

while ivedimas != "":
    zodziai.append(ivedimas)
    ivedimas = (input("Įveskite žodį: "))

for zodis in zodziai:
    print(zodis, len(zodis), zodziai.index(zodis) + 1)
print(len(zodziai))


# paprasčiau:

# zodziai = []

# for i in range(5):
    # zodziai.append(input("Įveskite žodį: "))

# for zodis in zodziai:
    # print(zodis, len(zodis), zodziai.index(zodis))
