
metai = int(input("Iveskite metus: "))
if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
    print("Keliamieji metai")
else:
    print("Nekeliamieji metai")
	
	
# alternatyva:
	
# metai = int(input("Iveskite metus: "))

# if metai % 400 == 0:
    # print("Keliamieji metai")
	
# elif metai % 100 == 0:
    # print("Nekeliamieji metai")
# elif metai % 4 == 0:
    # print("Keliamieji metai")
	
# else:
    # print("Nekeliamieji metai")
	
	

	
	
