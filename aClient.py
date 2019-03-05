#Create a cient

import psycopg2
import random
from faker import Faker
from psycopg2 import Error
fake = Faker('en_CA')

print ("Create a Client")
print ("---------------------------------")
print ("This will delete the old tables.")
try:
    connection = psycopg2.connect(user = "test", password = "test",  host = "127.0.0.1",  port = "5432", database = "test")
    cursor = connection.cursor()
    
    # --------------------Clinet------------------------------------------------------------------
    # --------------------Clinet------------------------------------------------------------------
    drop_table_client = '''DROP TABLE IF EXISTS client'''
    cursor.execute(drop_table_client)
        
    create_table_client = '''CREATE TABLE client
          (ID INT PRIMARY KEY     NOT NULL,
          FIRSTNAME          TEXT NOT NULL,
          MIDDLENAME         TEXT         ,
          LASTNAME           TEXT NOT NULL,
          GENDER             TEXT NOT NULL,
          SIN                TEXT,
          ADDRESS            TEXT,  
          POSTALCODE         TEXT,
          BIRTHDATE          TEXT); '''

    cursor.execute(create_table_client)
    connection.commit()

    print("New table Client created successfully in PostgreSQL ")
    print("Insert data in table Client")
    print("---------------------------")

    postgres_insert_query = """ INSERT INTO client (ID, FIRSTNAME, MIDDLENAME, LASTNAME, GENDER ,SIN, ADDRESS, POSTALCODE, BIRTHDATE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    for x in range(20):
        gender=random.choice(['M','F'])
        if gender == 'M':
            fname=fake.first_name_male()
            mname=fake.first_name_male()
        else:
            fname=fake.first_name_female()
            mname=fake.first_name_female()

        lname=fake.last_name()
        sin=fake.ssn()
        address=fake.street_address()
        postcode=fake.postcode()
        birthdate=fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=99)
        record_to_insert = (x+1, fname, mname, lname, gender, sin, address, postcode, birthdate)
        cursor.execute(postgres_insert_query, record_to_insert)
        print("Table Client insert:{}".format(record_to_insert))

    connection.commit()
    print("Table Client populated with TEST data.")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table Client. ", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")