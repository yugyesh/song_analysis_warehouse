from src.sql_queries import (
    copy_queries,
    insert_queries,
)
import psycopg2


def copy_to_staging(cur, conn):
    """copy the song data and log data from the s3 to staging tables"""
    try:
        for query in copy_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as error:
        print("Unable to copy data to staging area")
        print(error)


def transform_staging(cur, conn):
    """This method takes all the insert queries and stores
    the data into the fact and dimension table using staging tables

    Args:
        cur ([object]): [database cursor]
        conn ([object]): [database connection]
    """
    try:
        for query in insert_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as error:
        print("Error while transforming song to dimensional table")
        print(error)
