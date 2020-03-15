import psycopg2
from Database.basic.config import config

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Hospital (
            Hospital_Id INT PRIMARY KEY,
            Hospital_Name TEXT NOT NULL,
            Bed_Count INT
        )
        """,
        """
        CREATE TABLE Doctor ( Doctor_Id INT PRIMARY KEY, 
            `Doctor_Name` TEXT NOT NULL , 
            `Hospital_Id` INT NOT NULL , 
            `Joining_Date` DATE NOT NULL , 
            `Speciality` TEXT NULL , 
            `Salary` INT NULL , 
            `Experience` INT NULL
        )
        """)

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_hospitals():
    # Insert data into table hospital
    sql = """INSERT INTO hospital(Hospital_Id, Hospital_Name, Bed_Count) VALUES
            ('1', 'Mayo Clinic', '200'),
            ('2', 'Cleveland Clinic', '400'),
            ('3', 'Johns Hopkins', '1000'),
            ('4', 'UCLA Medical Center', '1500')"""

    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_doctors():
    # Insert data into table hospital
    sql = """INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) VALUES 
                ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
                ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
                ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
                ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
                ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
                ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
                ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
                ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL)"""

    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    create_tables()



