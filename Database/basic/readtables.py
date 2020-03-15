import psycopg2
from Database.basic.postgresqldb import *


def read_hospital_table(hospital_Id):
    #Read data from Hospital table
    # Read data from Hospital table
    try:
        # Call getDbConnection method to get connection.
        # This method already provided in question 1
        connection = connectdb()
        cursor = connection.cursor()

        sql_select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(sql_select_query, (hospital_Id,))
        records = cursor.fetchall()

        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:   = ", row[0], )
            print("Hospital Name: = ", row[1])
            print("Bed Count:     = ", row[2], "\n")

        # Close db connection
        closedb(connection)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def read_doctor_table(doctor_Id):
    # Read data from Doctor table

    try:
        # Call getDbConnection method to get connection.
        # This method already provided in question 1
        connection = connectdb()
        cursor = connection.cursor()


        sql_select_query = """select * from Doctor where Doctor_Id = %s"""
        cursor.execute(sql_select_query, (doctor_Id,))
        records = cursor.fetchall()

        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:    = ", row[0])
            print("Doctor Name:  = ", row[1])
            print("Hospital Id:  = ", row[2])
            print("Joining Date: = ", row[3])
            print("Speciality:   = ", row[4])
            print("Salary:       = ", row[5])
            print("Experience:   = ", row[6], "\n")

        # Close db connection
        closedb(connection)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_specialist_doctors_list(speciality, salary):
    # Fetch doctor's details as per Speciality and Salary
    try:
        # Call getDbConnection method to get connection.
        # This method already provided in question 1
        connection = connectdb()
        cursor = connection.cursor()

        sql_select_query = """select * from Doctor where Speciality=%s and Salary > %s"""
        cursor.execute(sql_select_query, (speciality, salary))
        records = cursor.fetchall()

        print("Printing Doctors record as per given Speciality")
        for row in records:
            print("Doctor Id:       = ", row[0])
            print("Doctor Name:     = ", row[1])
            print("Hospital Id:     = ", row[2])
            print("Joining Date:    = ", row[3])
            print("Speciality:      = ", row[4])
            print("Salary:          = ", row[5])
            print("Experience:      = ", row[6], "\n")

        # Close db connection
        closedb(connection)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_hospital_name(HospitalId):
    #Fetch Hospital Name using Hospital Id
    # Fetch doctor's details as per Speciality and Salary
    try:
        # Call getDbConnection method to get connection.
        # This method already provided in question 1
        connection = connectdb()
        cursor = connection.cursor()

        sql_select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(sql_select_query, (HospitalId,))
        record = cursor.fetchone()

        # Close db connection
        closedb(connection)

        return record[1]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_doctord_within_hospital(hospitalId):
    #Fetch All doctors within given Hospital
    # Fetch doctor's details as per Speciality and Salary
    try:
        # Call getDbConnection method to get connection.
        # This method already provided in question 1
        connection = connectdb()
        cursor = connection.cursor()

        sql_select_query = """select * from Doctor where Hospital_Id = %s"""
        cursor.execute(sql_select_query, (hospitalId,))
        records = cursor.fetchall()

        print("Printing Doctors Within given Hospital")
        for row in records:
            print("Doctor Id:   = ", row[0])
            print("Doctor Name: = ", row[1])
            print("Hospital Id: = ", row[2])
            hospital_name = get_hospital_name(row[2])
            print("Hospital Name: = ", hospital_name)
            print("Joining Date:  = ", row[3])
            print("Speciality:  = ", row[4])
            print("Salary:      = ", row[5])
            print("Experience:  = ", row[6], "\n")

        # Close db connection
        closedb(connection)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




print("Start of a Python Database Programming Exercise\n\n")

read_hospital_table(2)
read_doctor_table(105)

print("End of a Python Database Programming Exercise\n\n")


print("Start of a Python Database Programming Exercise\n\n")

get_specialist_doctors_list("Garnacologist", 30000)

print("End of a Python Database Programming Exercise\n\n")