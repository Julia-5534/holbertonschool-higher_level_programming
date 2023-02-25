#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for state in cur.fetchall():
        print(state)
