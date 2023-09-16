#!/usr/bin/python3
"""
This script connects to a MySQL database
and lists states from a specified database
matching the last argument
It takes three arguments: MySQL username,
MySQL password, and database name.
Results are sorted in ascending order by states.id.

Usage:
    python script.py <username> <password> <database_name>
"""


import MySQLdb
import sys


def list_states(username, password, database_name, searched):
    """
    List all states from the specified MySQL database.
    that matches the argument searched

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database to connect to.

    Returns:
        None
    """

    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        # Execute the SQL query to fetch all states sorted by states.id
        cursor.execute("SELECT cities.name FROM "
                       "cities INNER JOIN states "
                       "ON cities.state_id = states.id "
                       "WHERE states.name LIKE BINARY %s "
                       "ORDER BY cities.id ASC ", (searched, ))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            city_names = [row[0] for row in rows]
            print(', '.join(city_names))
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username>"
              "<password> <database_name> <searched>")
        sys.exit(1)

    username, password, database_name, searched = sys.argv[1:5]
    list_states(username, password, database_name, searched)
