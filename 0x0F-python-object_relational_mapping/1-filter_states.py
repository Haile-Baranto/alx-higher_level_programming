#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N' from the hbtn_0e_0_usa database.

Usage: python script.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database_name
    )
    cursor = db.cursor()

    # Retrieve and display sorted list of states starting with 'N'
    query = (
        "SELECT * FROM states WHERE name LIKE 'N%' "
        "ORDER BY states.id ASC"
    )
    cursor.execute(query)
    states = cursor.fetchall()

    # Display the retrieved states
    print("States with names starting with 'N':")
    for state in states:
        print(state)

    # Close the database connection
    cursor.close()
    db.close()
