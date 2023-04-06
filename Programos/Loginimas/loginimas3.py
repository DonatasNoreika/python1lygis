import logging

# logging.basicConfig(filename="uzduotis3.log", encoding="UTF-8", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(filename="uzduotis3.log", encoding="UTF-8")
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)

def suma(*args):
    rezultatas = sum(args)
    logger.info(f"funkcijos {suma.__name__} su argumentais {args} rezultatas {rezultatas}")
    return rezultatas


def saknis(skaicius):
    rezultatas = 0
    try:
        rezultatas = skaicius ** 0.5
        logger.info(f"funkcijos {saknis.__name__} su argumentu {skaicius} rezultatas {rezultatas}")
    except TypeError:
        logger.exception("Paduotas ne skaičius")
    return rezultatas


def simboliu_kiekis(sakinys):
    rezultatas = len(sakinys)
    logger.info(f"funkcijos {simboliu_kiekis.__name__} su argumentu {sakinys} rezultatas {rezultatas}")
    return rezultatas


def dalyba(x, y):
    rezultatas = 0
    try:
        rezultatas = x / y
        logger.info(f"funkcijos {dalyba.__name__} su argumentais {x} ir {y} rezultatas {rezultatas}")
    except ZeroDivisionError:
        logger.exception("Dalyba iš nulio negalima")
    return rezultatas


suma(5, 5, 4)
saknis(9)
simboliu_kiekis("Code Academy")
dalyba(5, 0)
