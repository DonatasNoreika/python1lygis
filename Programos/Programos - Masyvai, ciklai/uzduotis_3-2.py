suma = 0

while True:
    skaicius = int(input("Įveskite skaičių: "))
    if skaicius < 0:
        break
    suma += skaicius

print(suma)
