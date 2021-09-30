from src.sql_queries import drop_table_queries, create_table_queries
import psycopg2
import os
from configparser import ConfigParser

# connect to the database
def connect_aws():
    """
    - Creates and connects to the aws redshift
    - Returns the connection and cursor of the database
    """
    config = ConfigParser()

    config.read_file(open("./dwh.cfg"))

    KEY = config.get("AWS", "KEY")
    SECRET = config.get("AWS", "SECRET")

    DWH_DB = config.get("DWH", "DWH_DB")
    DWH_DB_USER = config.get("DWH", "DWH_DB_USER")
    DWH_DB_PASSWORD = config.get("DWH", "DWH_DB_PASSWORD")
    DWH_PORT = config.get("DWH", "DWH_PORT")

    DWH_ENDPOINT = config.get("DWH", "DWH_ENDPOINT")
    DWH_ROLE_ARN = config.get("DWH", "DWH_ROLE")

    conn_string = "postgresql://{}:{}@{}:{}/{}".format(
        DWH_DB_USER, DWH_DB_PASSWORD, DWH_ENDPOINT, DWH_PORT, DWH_DB
    )
    try:
        conn = psycopg2.connect(
            conn_string,
        )
    except psycopg2.Error as error:
        print(error)
        return None

    try:
        cur = conn.cursor()
    except psycopg2.Error as error:
        print("Unable to retrieve cursor for")
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
    cur, conn = connect_aws()

    drop_tables(cur, conn)

    create_tables(cur, conn)

    conn.close()
