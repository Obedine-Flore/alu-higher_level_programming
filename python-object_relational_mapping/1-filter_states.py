#!/usr/bin/python3
"""This script that lists all states with a name starting with N"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    query_rows = crs.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    crs.close()
    db.close()
