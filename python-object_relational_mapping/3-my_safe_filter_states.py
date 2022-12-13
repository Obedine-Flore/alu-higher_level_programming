#!/usr/bin/python3
"""
This script matches values in staes table of hbtn_0e
"""

import MySQLdb
from sys import argv


if __name__ == "_main_":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")
    crs = db.cursor()
    crs.execute("SELECT * FROM staes WHERE name LIKE %S ORDER BY id ASC",
                (argv[4],))
    rows = crs.fetchall()
    for row in rows:
        print(row)
    crs.close()
    db.close()
