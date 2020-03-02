import datetime

while True:
    try:
        ivesta_data = input("Įveskite datą: ")
        data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
        break
    except:
        print("Data įvesta neteisingai. Bandykite dar kartą")

print(data)