from src.create_tables import connect_aws
from src.sql_queries import copy_queries
import psycopg2

cur, conn = connect_aws()


def copy_staging(cur, conn):
    """copy the song data and log data from the s3 to staging tables"""
    try:
        for query in copy_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as error:
        print("Unable to copy data to staging area")
        print(error)


copy_staging(cur, conn)
