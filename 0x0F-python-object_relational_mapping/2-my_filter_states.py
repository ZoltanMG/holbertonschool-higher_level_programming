#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    arguments = sys.argv
    db = MySQLdb.connect(host="localhost",
                         user=arguments[1],
                         passwd=arguments[2],
                         db=arguments[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = '{}' ORDER BY
    states.id ASC""".format(arguments[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
