import psycopg2
from psycopg2 import Error
from Database.basic.config import config

# https://pynative.com/python-database-programming-exercise-with-solution/

def create_tables():
    conn = None

    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        create_table_query = '''CREATE TABLE mobile
              (ID INT PRIMARY KEY     NOT NULL,
              MODEL           TEXT    NOT NULL,
              PRICE         REAL); '''

        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)

    finally:
        # closing database connection.
        if conn is not None:
            conn.close()
            print('Database connection closed.')