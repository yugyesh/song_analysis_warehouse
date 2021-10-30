from src.sql_queries import copy_queries
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
