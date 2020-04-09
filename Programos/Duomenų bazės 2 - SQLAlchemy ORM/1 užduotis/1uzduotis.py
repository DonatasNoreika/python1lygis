from darbuotojas import engine, Darbuotojas, Base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirinkite: 1 - darbuotojo įvedimas, 2 - trynimas, 3 - atnaujinimas, 8 - peržiūra, 9 - išeiti"))
    if pasirinkimas == 1:
        while True:
            try:
                name = input("Įveskite vardą")
                last_name = input("Įveskite pavardę")
                birthdate = datetime.strptime(input("Įveskite gimimo datą (YYYY-MM-DD)"), "%Y-%m-%d")
                position = input("Įveskite pareigas")
                salary = float(input("Įveskite atlyginimą"))
                darbuotojas = Darbuotojas(name, last_name, birthdate, position, salary)
                session.add(darbuotojas)
                session.commit()
                break
            except:
                print("Klaida. Bandykite dar kartą")
    if pasirinkimas == 2:
        visi = session.query(Darbuotojas).all()
        for darbuotojas in visi:
            print(darbuotojas)
        numeris = int(input("Pasirinkite norimo ištrinti įrašo ID"))
        trinamas_darbuotojas = session.query(Darbuotojas).get(numeris)
        session.delete(trinamas_darbuotojas)
        session.commit()
    if pasirinkimas == 3:
        visi = session.query(Darbuotojas).all()
        for darbuotojas in visi:
            print(darbuotojas)
        numeris = int(input("Pasirinkite norimo redaguoti įrašo ID"))
        darbuotojas = session.query(Darbuotojas).get(numeris)
        while True:
            try:
                darbuotojas.name = input("Įveskite vardą")
                darbuotojas.last_name = input("Įveskite pavardę")
                darbuotojas.birthdate = datetime.strptime(input("Įveskite gimimo datą (YYYY-MM-DD)"), "%Y-%m-%d")
                darbuotojas.position = input("Įveskite pareigas")
                darbuotojas.salary = float(input("Įveskite atlyginimą"))
                session.commit()
                break
            except:
                print("Klaida. Bandykite dar kartą")
    if pasirinkimas == 8:
        visi = session.query(Darbuotojas).all()
        for darbuotojas in visi:
            print(darbuotojas)
    if pasirinkimas == 9:
        print("Viso gero")
        break

