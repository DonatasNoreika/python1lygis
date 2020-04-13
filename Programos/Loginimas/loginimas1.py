import math

import logging
logging.basicConfig(filename="uzduotis_15_1.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(x):
    logging.info(f"Skaiciaus {x} saknis lygi {math.sqrt(x)}")
    return math.sqrt(x)

def simboliai(sakinys):
    logging.info(f"Sakinio {sakinys} ilgis lygus {len(sakinys)} simboliu")
    return len(sakinys)

def dalyba(x, y):
    logging.info(f"{x} padalinta is {y} lygu {x / y}")
    return x / y

print(suma(4, 5, 7, 8, 9, 9))
print(saknis(49))
print(simboliai("Labas vakaras"))
print(dalyba(10, 5))
