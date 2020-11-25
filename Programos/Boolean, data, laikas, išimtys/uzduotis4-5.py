import datetime

while True:
    try:
        ivesta = input("Įveskite metus (YYYY-MM-DD) ")
        ivesta_data = datetime.datetime.strptime(ivesta, "%Y-%m-%d")
        break
    except:
        print("Įvestas ne sveikasis arba netinkamas datos skaičius")

now = datetime.datetime.now()
skirtumas = now - ivesta_data

print(f"Praėjo metų: ", skirtumas.days // 365)
print("Praėjo mėnesių: ", round(skirtumas.days / 365 * 12))
print("Praėjo savaičių: ", round(skirtumas.days / 7))
print("Praėjo dienų: ", skirtumas.days)
print("Praėjo valandų: ", round(skirtumas.total_seconds() / 3600))
print("Praėjo minučių: ", round(skirtumas.total_seconds() / 60))
print("Praėjo sekundžių: ", round(skirtumas.total_seconds()))
