from sql_queries import drop_table_queries, create_table_queries
import psycopg2
import os

# connect to the database
def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """

    # extract db username and password
    try:
        user = os.environ["USER"]
        password = os.environ["PASSWORD"]
        host = os.environ["HOST"]
        dbname = os.environ["DB_NAME"]
    except KeyError as error:
        print("Error: username and password not defined")
        print(error)

    # connect to default database
    try:
        conn = psycopg2.connect(
            f"host={host} dbname={dbname} user={user} password={password}"
        )
    except psycopg2.Error as error:
        print("Unable to connect to the default database")
        print(error)

    # ? Why to set autocommit = true
    conn.set_session(autocommit=True)

    # get cursor
    try:
        cur = conn.cursor()
    except psycopg2.Error as error:
        print("Unable to get cursor")
        print(error)

    # create sparkify database with utf8 encoding
    # ? Why to use the encoding while creating the database
    try:
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        cur.execute(
            "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0"
        )
        dbname = "sparkifydb"
    except psycopg2.Error as error:
        print("Error while creating sparkifydb")
        print(error)

    # connecting to sparkifydb
    try:
        conn = psycopg2.connect(
            f"host={host} dbname={dbname} user={user} password={password}"
        )
    except psycopg2.Error as error:
        print(f"Error while connecting to {dbname}")
        print(error)

    # conn.set_session(autocommit=True)

    # get cursor
    # ? What is cursor
    try:
        cur = conn.cursor()
    except psycopg2.Error as error:
        print(f"Unable to retrieve cursor for {dbname}")
        print(error)

    return cur, conn


# create tables
def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    try:
        for query in create_table_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as error:
        print("Error: Unable to create table")
        print(error)


# drop all tables
def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    try:
        for query in drop_table_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as error:
        print("Error while droping table")
        print(error)


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    cur, conn = create_database()

    drop_tables(cur, conn)

    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
