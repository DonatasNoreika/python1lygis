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

    
# Alternatyva:

# import random
# 
# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)
# 
# print(num1, num2, num3)
# 
# if num1 == 5 or num2 == 5 or num3 == 5:
#     print("Pralaimėjai")
# else:
#     print("Laimėjai")


# Arba:
# from random import randint

# skaiciai = [randint(1,6), randint(1,6), randint(1,6)]
# print(skaiciai)

# if 5 in skaiciai:
#     print("Pralaimėjai")
# else:
#     print("Laimėjai")
