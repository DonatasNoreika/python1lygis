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


# jeigu norime laiko intervalą atvaizduoti taip, pvz:
# praėjo 2 metai, 7 mėnesiai, 23 dienos ir t.t.
# konsolėje: pip install python-dateutil

# from dateutil.relativedelta import relativedelta
# delta = relativedelta(datetime.datetime.now(), kazkokia_data)
# print(f'metu: {res.years}, menesiu {res.months}, dienu {res.days}, valandu {res.hours}') ir t.t.
