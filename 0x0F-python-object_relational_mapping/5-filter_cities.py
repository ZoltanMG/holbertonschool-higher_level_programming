#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s""", (argv[4], ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(', '.join(cities))
    cur.close()
    db.close()
