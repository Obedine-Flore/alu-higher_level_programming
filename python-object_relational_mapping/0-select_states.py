#!/usr/bin/python3
"""This script lists all the states from the hbtn_0e_0_usa database"""

import MySQLdb
import sys


def main():
    """This function lists all the states from the
    hbtn_0e_usa database"""
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
