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

class TekstasIFaila:
    def __init__(self, ivestas_tekstas):
        self.ivestas_tekstas = ivestas_tekstas

    def sukurti_faila(self):
        with open('tekstas.txt', 'w') as failas:
            failas.write(self.ivestas_tekstas)

    def nuskaityti_faila(self):
        with open('tekstas.txt', 'r') as failas:
            print(failas.read())

    def prideti_data(self):
        with open('tekstas.txt', 'a') as failas:
            failas.write(str(datetime.today()))

    def sunumeruoti(self):
        naujas = ""
        skaicius = 1
        with open('tekstas.txt', 'r') as failas:
            for eilute in failas:
                naujas += str(skaicius) + " " + eilute
                skaicius += 1

        with open('tekstas.txt', 'w') as failas:
            failas.write(naujas)

    def prideti_data(self):
        with open('tekstas.txt', 'a') as failas:
            failas.write(str(datetime.today()))

    def pakeisti_teksta(self, originalus, pakeistas):
        pakeitimas = ""
        with open('tekstas.txt', 'r') as failas:
            pakeitimas = failas.read()

        pakeitimas = pakeitimas.replace(originalus, pakeistas)

        with open('tekstas.txt', 'w', encoding="UTF-8") as failas:
            failas.write(pakeitimas)

    def atspausdinti_atbulai(self):
        with open('tekstas.txt', 'r') as failas:
            print(failas.read()[::-1])

    def informacija(self):
        print("Žodžių kiekis:", len(self.ivestas_tekstas.split()))
        print("Skaičių kiekis:", sum(c.isdigit() for c in self.ivestas_tekstas))
        print("Didžiųjų raidžių:", sum(c.isupper() for c in self.ivestas_tekstas))
        print("Mažųjų raidžių:", sum(c.islower() for c in self.ivestas_tekstas))

    def kopijuoti_didziosiomis(self):
        with open('tekstas.txt', 'r', encoding="UTF-8") as nuskaitomas_failas:
            with open('tekstas_didziosiomis.txt', "w", encoding="UTF-8") as irasomas_failas:
                irasomas_failas.write(nuskaitomas_failas.read().upper())

zen_tekstas = TekstasIFaila(zen)

# 1. Sukurti failą tekstas.txt su tekstu:

zen_tekstas.sukurti_faila()

# 2. Nuskaityti sukurtą failą:

zen_tekstas.nuskaityti_faila()

# 3. Paskutinėje sukurto failo eilutėje pridėtų šiandien datą:

zen_tekstas.prideti_data()

# 4. Sunumeruoti visas failo teksto eilutes (kiekvienos pradžioje pridėti skaičių):

zen_tekstas.sunumeruoti()

# 5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeisti į "Gražu yra geriau nei bjauru.":

zen_tekstas.pakeisti_teksta("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

# 6. Atspausdintų visą failo tekstą atbulai:

zen_tekstas.atspausdinti_atbulai()

# 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

zen_tekstas.informacija()

# 8. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

zen_tekstas.kopijuoti_didziosiomis()



