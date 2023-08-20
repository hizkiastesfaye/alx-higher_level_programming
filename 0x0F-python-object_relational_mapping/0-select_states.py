#!/usr/bin/python3
import MySQLdb
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()

