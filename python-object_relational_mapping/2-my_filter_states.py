#!/usr/bin/python3
"""This script takes an argument and displays the argument"""

import MySQLdb
import sys


if _name_ == "_main_":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    crs = db.cursor()
    crs.execute("SELECT * FROM staes WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".FORMAT(SYS.ARGV[4]))
    rows = crs.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    crs.close()
    db.close()
