#!/usr/bin/env python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} name passwd database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query with user input (safe from injection)
    query = "SELECT cities.name FROM cities JOIN states ON\
        cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Extract city names from the rows
    city_names = [row[0] for row in rows]

    # Display the results
    print(', '.join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()
