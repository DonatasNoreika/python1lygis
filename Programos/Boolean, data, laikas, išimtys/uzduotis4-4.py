while True:
    try:
        print(int(input("Įveskite skaičių: ")) > 0)
        break
    except ValueError:
        print("Įvestas neteisingas skaičius (turi būti sveikasis)")
