import sqlite3

conn = sqlite3.connect("paskaitos.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS paskaitos (
            pavadinimas text,
            destytojas text,
            trukme integer
            )""")

with conn:
    c.execute("INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40)")
    c.execute("INSERT INTO paskaitos VALUES ('Python', 'Donatas', 80)")
    c.execute("INSERT INTO paskaitos VALUES ('Java', 'Tomas', 80)")

with conn:
    c.execute("SELECT * From paskaitos Where trukme > 50")
    print(c.fetchall())

with conn:
    c.execute("UPDATE paskaitos SET pavadinimas='Python programavimas' WHERE pavadinimas='Python'")

with conn:
    c.execute("DELETE from paskaitos WHERE destytojas='Tomas'")

with conn:
    c.execute("SELECT * From paskaitos")
    print(c.fetchall())
