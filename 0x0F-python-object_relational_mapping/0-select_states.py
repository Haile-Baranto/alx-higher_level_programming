#!/usr/bin/python3

""" The script displayes all states by ID using
mysql username, mysql password and database name as arguement
from the command line"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password>\
              <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name)
    cursor = db.cursor()

    # Retrieve and display sorted list of states
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    # Close the database connection
    cursor.close()
    db.close()
