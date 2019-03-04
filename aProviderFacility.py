#Create a Provider and a Facility

import psycopg2
import random
from faker import Faker
from psycopg2 import Error
print ("Create a Provider and a Facility.")
print ("---------------------------------")
print ("This will delete the old tables.")
try:
    connection = psycopg2.connect(user = "test", password = "test",  host = "127.0.0.1",  port = "5432", database = "test")
    cursor = connection.cursor()
    
# --------------------Provider------------------------------------------------------------------
# --------------------Provider------------------------------------------------------------------
    drop_table_provider = '''DROP TABLE IF EXISTS provider'''
    cursor.execute(drop_table_provider)
        
    create_table_provider = '''CREATE TABLE provider
          (ID INT PRIMARY KEY    NOT NULL,
          NAME           TEXT    NOT NULL,
          ADDRESS        TEXT,  
          POSTALCODE     TEXT,
          TYPE           TEXT); '''
    
    cursor.execute(create_table_provider)
    connection.commit()
    print("New table Provider created successfully in PostgreSQL ")

    print("Insert data in table Provider")
    print("-----------------------------")
    fake = Faker('en_CA')
    provider_types={ 'Physician', 'Nurse', 'Pharmacist' }
    postgres_insert_query = """ INSERT INTO provider (ID, NAME, ADDRESS, POSTALCODE, TYPE) VALUES (%s,%s,%s,%s,%s)"""
    for x in range(20):
      name=fake.last_name()
      address=fake.street_address()
      postcode=fake.postcode()
      providertype=random.choice(tuple(provider_types))
      record_to_insert = (x+1, name, address, postcode, providertype)
      cursor.execute(postgres_insert_query, record_to_insert)
      count = cursor.rowcount
      print("Table Provider insert:{}".format(record_to_insert))
      connection.commit()
    print("Table Provider populated with TEST data.")


# --------------------Facility------------------------------------------------------------------
# --------------------Facility------------------------------------------------------------------
    drop_table_provider = '''DROP TABLE IF EXISTS facility'''
    cursor.execute(drop_table_provider)
        
    create_table_facility = '''CREATE TABLE facility
          (ID INT PRIMARY KEY    NOT NULL,
          NAME           TEXT    NOT NULL,
          ADDRESS        TEXT,  
          POSTALCODE     TEXT,
          TYPE           TEXT); '''
    
    cursor.execute(create_table_facility)
    connection.commit()
    print("New table Facility created successfully in PostgreSQL ")

    print("Insert data in table Facility")
    print("----------------------------")
    fake = Faker('en_CA')
    facility = { 'Vancouver General', 'Victoria General', 'Jubilee Hospital', 'Shelborne Clinic', 'UVic Clinic', 'Bay Street', 'Elizabeth Bradshaw', 'Fort Street', 'McKenzie'}
    facility_types = { 'Hospital',  'Clinic',  'Ambulance Station', 'Abortion Clinic', 'Laboratory', 'Pharmacy'}

    postgres_insert_query = """ INSERT INTO facility (ID, NAME, ADDRESS, POSTALCODE, TYPE) VALUES (%s,%s,%s,%s,%s)"""
    for x in range(20):
      name=random.choice(tuple(facility))
      address=fake.street_address()
      postcode=fake.postcode()
      facilitytype=random.choice(tuple(facility_types))
      record_to_insert = (x+1, name, address, postcode, facilitytype)
      cursor.execute(postgres_insert_query, record_to_insert)
      count = cursor.rowcount
      print("Table Facility insert:{}".format(record_to_insert))
      connection.commit()
    print("Table Facility populated with TEST data.")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL tables. ", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

