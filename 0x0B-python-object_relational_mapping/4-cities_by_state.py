#!/usr/bin/python3
"""Task 4"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]


def print_cities_states():
    """
    Method to list all cities
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name\
            FROM cities, states\
            WHERE cities.state_id = states.id\
            ORDER BY cities.id"
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
