import sqlite3


con = sqlite3.connect("exchange rate")
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT Name FROM currency""").fetchall()
for elem in result:
    print(elem)
con.close()