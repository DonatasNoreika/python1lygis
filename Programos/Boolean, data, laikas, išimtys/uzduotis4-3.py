import datetime

ivesta = input("Įveskite metus (YYYY-MM-DD HH:MM:SS) ")

ivesta_data = datetime.datetime.strptime(ivesta, "%Y-%m-%d %X")
now = datetime.datetime.now()
skirtumas = now - ivesta_data

print("Praėjo metų: ", skirtumas.days // 365)
print("Praėjo mėnesių: ", round(skirtumas.days / 365 * 12))
print("Praėjo savaičių: ", skirtumas.days // 7)
print("Praėjo dienų: ", skirtumas.days)
print("Praėjo valandų: ", round(skirtumas.total_seconds() / 3600))
print("Praėjo minučių: ", round(skirtumas.total_seconds() / 60))
print("Praėjo sekundžių: ", round(skirtumas.total_seconds()))
