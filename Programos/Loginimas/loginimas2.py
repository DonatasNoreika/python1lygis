import logging

logging.basicConfig(filename="uzduotis2.log", encoding="UTF-8", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    rezultatas = sum(args)
    logging.info(f"funkcijos {suma.__name__} su argumentais {args} rezultatas {rezultatas}")
    return rezultatas


def saknis(skaicius):
    rezultatas = 0
    try:
        rezultatas = skaicius ** 0.5
        logging.info(f"funkcijos {saknis.__name__} su argumentu {skaicius} rezultatas {rezultatas}")
    except TypeError:
        logging.exception("Paduotas ne skaičius")
    return rezultatas


def simboliu_kiekis(sakinys):
    rezultatas = len(sakinys)
    logging.info(f"funkcijos {simboliu_kiekis.__name__} su argumentu {sakinys} rezultatas {rezultatas}")
    return rezultatas


def dalyba(x, y):
    rezultatas = 0
    try:
        rezultatas = x / y
        logging.info(f"funkcijos {dalyba.__name__} su argumentais {x} ir {y} rezultatas {rezultatas}")
    except ZeroDivisionError:
        logging.exception("Dalyba iš nulio negalima")
    return rezultatas


suma(5, 5, 4)
saknis(9)
simboliu_kiekis("Code Academy")
dalyba(5, 0)
