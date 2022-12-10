#!/usr/bin/python3


import MySQLdb
import sys


if _name_ == "_main_":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    query_rows = crs.fetchall()
    for row in querry_rows:
        if row[1][0] == 'N':
            print(row)
        crs.close()
        db.close()
