import math

import logging
logging.basicConfig(filename="uzduotis_15_2.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(x):
    try:
        rezultatas = math.sqrt(x)
    except TypeError:
        logging.exception("Saknis gali buti traukiama tik is skaiciaus")
    else:
        logging.info(f"Skaiciaus {x} saknis lygi {rezultatas}")
        return rezultatas

def simboliai(sakinys):
    logging.info(f"Sakinio {sakinys} ilgis lygus {len(sakinys)} simboliu")
    return len(sakinys)

def dalyba(x, y):
    try:
        rezultatas = x / y
    except ZeroDivisionError:
        logging.exception("Dalyba is nulio")
    else:
        logging.info(f"{x} padalinta is {y} lygu {rezultatas}")
        return rezultatas


print(suma(4, 5, 7, 8, 9, 9))
print(saknis("Donatas"))
print(simboliai("Labas vakaras"))
print(dalyba(10, 0))

