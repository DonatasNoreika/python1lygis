
# 1 Importuoti modulį datetime. Atsispausdinti (atskirai) šiandienos datą (date.today()), tik laiką bei datą ir laiką kartu.

# import datetime
#
# print(datetime.date.today())
# print(datetime.datetime.today())
# print(datetime.datetime.now().time())

# 2 Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą

# from datetime import date
#
# print(date.today())

# 3 Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.

from datetime import date as data

print(data.today())
