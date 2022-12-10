#!/usr/bin/python3


import sys
import MySQLdb


if _name_ == "_main_":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306
        )

    crs = db.cursor()
    crs.execute("SELECT cities.id, cities.name, states.name \
            FROM cities, states WHERE cities.state_id = states.id \
            ORDER BY id ASC")

    rows = crs.fetchall()

    for i in rows:
        print(i)
    db.close()
