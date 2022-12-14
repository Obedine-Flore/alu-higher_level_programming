#!/usr/bin/python3
"""This script that takes in an argument and displays all values in the states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    rows = crs.fetchall()
    for i in rows:
        print(i)
    crs.close()
    db.close()
