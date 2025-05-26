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

veikianti alternatyva su papildoma biblioteka (pagaliau!!):
# pip install pendulum

import pendulum

dt1 = pendulum.datetime(2025, 5, 26, 15, 14, 29)
dt2 = pendulum.datetime(2000, 1, 1, 0, 0, 0)

diff = dt1.diff(dt2)

print("Years:", diff.in_years())
print("Months:", diff.in_months())   # total months
print("Weeks:", diff.in_weeks())     # total weeks
print("Days:", diff.in_days())       # total days
print("Hours:", diff.in_hours())       # total hours
print("Minutes:", diff.in_minutes())       # total minutes
print("Seconds:", diff.in_seconds())       # total seconds

# jeigu norime laiko intervalą atvaizduoti taip, pvz:
# praėjo 2 metai, 7 mėnesiai, 23 dienos ir t.t.
# konsolėje: pip install python-dateutil

# from dateutil.relativedelta import relativedelta
# delta = relativedelta(datetime.datetime.now(), kazkokia_data)
# print(f'metu: {res.years}, menesiu {res.months}, dienu {res.days}, valandu {res.hours}') ir t.t.
