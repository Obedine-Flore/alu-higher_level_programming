#!/usr/bin/python3
"""
This script lists all sates with a name starting with
N from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


if _name_ == "_main_":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in querry_rows:
        if row[1][0] == 'N':
            print(row)
        cur.close()
        db.close()
