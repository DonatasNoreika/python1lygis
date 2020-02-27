

for metai in range(2000, 2100):
    if metai % 400 == 0:
        print(metai)
    elif metai % 100 == 0:
        continue
    elif metai % 4 == 0:
        print(metai)
    else:
        continue