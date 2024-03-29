#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
