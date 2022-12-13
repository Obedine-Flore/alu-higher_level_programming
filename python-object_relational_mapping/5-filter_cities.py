#!/usr/bin/python3
"""this script matches states to cities in the
hbtn_0e_4_usa database"""


import MySQLdb
import sys


if __name__ == "_main_":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    crs = db.cursor()
    crs.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.stae_id = states.id\
                WHERE states.name = '{}'\
                ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = crs.fetchall()
    print(", ".join([row[0] for row in rows]))
    crs.close()
    db.close()
