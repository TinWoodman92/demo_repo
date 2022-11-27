import os
from random import *
from sqlite3 import *


if not os.path.isfile(os.path.join(os.getcwd(), 'sexy.db')):
	chk_1 = True
else:
	chk_1 = False

con = connect('sexy.db')
cur = con.cursor()

if chk_1:
	cur.execute("CREATE TABLE sexy_tbl (chk INTEGER);")

chk_2 = randint(0,1)

cur.execute("INSERT INTO sexy_tbl (chk) VALUES(:chk);", {"chk" : chk_2})

rst = []
k = []
res = cur.execute("SELECT sum(chk) as sum_chk, count(chk) as count_chk FROM sexy_tbl;")
for desc in cur.description: k.append(desc[0])
for row in res.fetchall(): rst.append(dict(zip(k,row)))

rcd = rst[0]
chk_3 = (rcd["sum_chk"]/rcd["count_chk"]) > 0.5

if chk_3:
	print("\033[95mheyy sexy!\033[0m")
else:
	print("Hello World!")

diag = input()	

if 'sexy' in diag.lower():
	print(f"Your sexy score is {rcd['sum_chk']} out of {rcd['count_chk']}.")

con.commit()
cur = None
con = None