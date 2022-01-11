
from statistics import mean, median

# Atliktų veiksmus su skaičiais iki 50:

skaiciai = list(range(51))

# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų:

# naujas = map(lambda x: x * 10, skaiciai)
# print(list(naujas))

# arba

naujas = [x * 10 for x in skaiciai]
print(naujas)

# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų

# is_7 = filter(lambda x: x % 7 == 0, skaiciai)
# print(list(is_7))

# arba

is_7 = [x for x in skaiciai if x % 7 == 0]
print(is_7)

# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų

# kvadratu = list(map(lambda x: x ** 2, skaiciai))
# print(list(kvadratu))

# arba

kvadratu = [x ** 2 for x in skaiciai]
print(kvadratu)

# Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą,
# mažiausią ir didžiausią skaičių, vidurkį, medianą

print(sum(kvadratu))
print(min(kvadratu))
print(max(kvadratu))
print(mean(kvadratu))
print(median(kvadratu))

# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai

atbulai = sorted(kvadratu, reverse=True)
print(atbulai)
