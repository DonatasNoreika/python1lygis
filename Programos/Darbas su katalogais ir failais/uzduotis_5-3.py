import os
from datetime import datetime

# 1 Ant darbalaukio sukurtų naują katalogą "Mano Katalogas"

try:
    os.chdir('C:\\Users\\Donoras\\Desktop')
    os.mkdir("Naujas katalogas")
except:
    "Toks katalogas jau yra"

os.chdir('C:\\Users\\Donoras\\Desktop\\Naujas katalogas')

# 2 Jame sukurtų failą "data.txt", kurios tektas - šiandienos data ir laikas

with open("data.txt", "w") as failas:
    failas.write(str(datetime.today()))

# 3 Atspaudintų, kada naujas failas buvo modifikuotas ir kiek jis užima baitų
os.chdir('C:\\Users\\Donoras\\Desktop\\Naujas katalogas')

print("Sukūrimo data:", datetime.fromtimestamp(os.stat("data.txt").st_ctime))
print("Failo dytis:", os.stat("data.txt").st_size)
