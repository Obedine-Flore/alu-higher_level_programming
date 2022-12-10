#!/usr/bin/python3
""" this script  lists all states from the database
hbtn_0e_0_usa"""


import MySQLdb
import sys


def main():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    crs = db.cursor()

    crs.execute("SELECT * FROM states ORDER BY id ASC")

    rows = crs.fetchall()
    for row in rows:
        print(row)

    crs.close()
    db.close()


if _name_ == "_main_":
    main()
