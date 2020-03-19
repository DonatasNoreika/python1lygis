from datetime import datetime

zen = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def atbulai(sakinys):
    return sakinys[::-1]

def patikrinti_sakini(sakinys):
    print("Žodžių kiekis:", len(sakinys.split()))
    print("Skaičių kiekis:", sum(c.isdigit() for c in sakinys))
    print("Didžiųjų raidžių:", sum(c.isupper() for c in sakinys))
    print("Mažųjų raidžių:", sum(c.islower() for c in sakinys))

def didziosiomis(sakinys):
    return sakinys.upper()

# 1. Sukurti failą tekstas.txt su tekstu:

with open('tekstas.txt', 'w') as failas:
    failas.write(zen)

# 2. Atspausdintų tekstą iš sukurto failą:

with open('tekstas.txt', 'r') as failas:
    print(failas.read())

# 3. Paskutinėje sukurto failo eilutėje pridėtų šiandien datą:

with open('tekstas.txt', 'a') as failas:
    failas.write(str(datetime.today()))

# 4. Sunumeruoti visas failo teksto eilutes (kiekvienos pradžioje pridėti skaičių):

naujas = ""
skaicius = 1
with open('tekstas.txt', 'r') as failas:
    for eilute in failas:
        naujas += str(skaicius) + " " + eilute
        skaicius += 1

with open('tekstas.txt', 'w') as failas:
    failas.write(naujas)


# 5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeisti į "Gražu yra geriau nei bjauru.":

pakeitimas = ""

with open('tekstas.txt', 'r') as failas:
    pakeitimas = failas.read()

pakeitimas = pakeitimas.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

with open('tekstas.txt', 'w', encoding="UTF-8") as failas:
    failas.write(pakeitimas)

# 6. Atspausdintų visą failo tekstą atbulai:

with open('tekstas.txt', 'r') as failas:
    print(atbulai(failas.read()))

# 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

with open('tekstas.txt', 'r') as failas:
    print(patikrinti_sakini(failas.read()))

# 8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS:

with open('tekstas.txt', 'r', encoding="UTF-8") as nuskaitomas_failas:
    with open('tekstas_didziosiomis.txt', "w", encoding="UTF-8") as irasomas_failas:
        irasomas_failas.write(didziosiomis(nuskaitomas_failas.read()))