import logging

logging.basicConfig(filename="uzduotis1.log", encoding="UTF-8", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    rezultatas = sum(args)
    logging.info(f"funkcijos {suma.__name__} su argumentais {args} rezultatas {rezultatas}")
    return rezultatas


def saknis(skaicius):
    rezultatas = skaicius ** 0.5
    logging.info(f"funkcijos {saknis.__name__} su argumentu {skaicius} rezultatas {rezultatas}")
    return rezultatas


def simboliu_kiekis(sakinys):
    rezultatas = len(sakinys)
    logging.info(f"funkcijos {simboliu_kiekis.__name__} su argumentu {sakinys} rezultatas {rezultatas}")
    return rezultatas


def daugyba(x, y):
    rezultatas = x * y
    logging.info(f"funkcijos {daugyba.__name__} su argumentais {x} ir {y} rezultatas {rezultatas}")
    return rezultatas


suma(5, 5, 4)
saknis(9)
simboliu_kiekis("Code Academy")
daugyba(5, 4)
