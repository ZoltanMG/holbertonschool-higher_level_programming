#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!.
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
    cur.execute("""SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s""", (arguments[4], ))
    states = cur.fetchall()
    for num in range(len(states)):
        for citie in states[num]:
            if num < len(states) - 1:
                print(citie, end=', ')
            else:
                print(citie)
    cur.close()
    db.close()
