#!/usr/bin/python3
import MySQLdb
import sys  # to  accept arguement from the command line
""" The script displayes all states by ID """


def list_states(username, password, database_name):
    """The function accepts username, password and name of the
    database make conection to the database and list states by ID"""
    # connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database_name)
    cursor = db.cursor()

    # Retrieve and display list of states from table state
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)
    # close the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password>\
              <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
