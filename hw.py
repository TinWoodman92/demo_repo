#!/usr/bin/python3

import os
from random import *
from sqlite3 import *
import getpass


if not os.path.isfile(os.path.join(os.getcwd(), 'sexy.db')):
	chk_1 = True
else:
	chk_1 = False

con = connect('sexy.db')
cur = con.cursor()

if chk_1:
	cur.execute("CREATE TABLE sexy_tbl (username TEXT, chk INTEGER);")

chk_2 = randint(0,1)
username = getpass.getuser()
param = {"username" : username, "chk" : chk_2}

cur.execute("INSERT INTO sexy_tbl (username, chk) VALUES(:username, :chk);", param)

k = []
res = cur.execute('''
	SELECT sum(chk) as sum_chk, count(chk) as count_chk 
	FROM sexy_tbl
	WHERE username = :username;''',
	param)

for desc in cur.description: k.append(desc[0])
row = res.fetchone()
rcd = dict(zip(k,row))

chk_3 = (rcd["sum_chk"]/rcd["count_chk"]) > 0.5

if chk_3:
	print("\033[95mheyy sexy!\033[0m")
else:
	print("Hello World!")

diag = input()	

if 'sexy' in diag.lower():
	print(f"Your sexy score is {rcd['sum_chk']} out of {rcd['count_chk']}.")
	input()

con.commit()
cur = None
con = None