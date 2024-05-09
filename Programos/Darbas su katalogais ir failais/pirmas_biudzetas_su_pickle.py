import pickle

try:
    with open("journal.pkl", 'rb') as file:
        journal = pickle.load(file)
except FileNotFoundError as err:
    journal = []

while True:
    action = int(input("1 - add income/expences\n2 - view income/expences\n3 - show balance\n4 - exit\n"))
    match action:
        case 1:
            number = float(input("Enter income/expence: "))
            journal.append(number)
            with open("journal.pkl", 'wb') as file:
                pickle.dump(journal, file)
        case 2:
            print(journal)
        case 3:
            print("Balance:", sum(journal))
        case 4:
            print("Good bye")
            break
