import random

print("Bus sugeneruoti 3 skaičiai")
print("Jei vienas iš jų – 5, tu pralaimėjai!")

for x in range(3):
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Pralaimėjai...")
        break
else:
    print("Laimėjai!")
