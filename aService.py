#Create a Provider and a Facility

import psycopg2
import random
import datetime
from faker import Faker
from psycopg2 import Error
fake = Faker('en_CA')
print ("Create a Service ")
print ("----------------")
print ("This will delete the old table.")
try:
    connection = psycopg2.connect(user = "test", password = "test",  host = "127.0.0.1",  port = "5432", database = "test")
    cursor = connection.cursor()
    
# --------------------Service------------------------------------------------------------------
# --------------------Service------------------------------------------------------------------
    drop_table_service = '''DROP TABLE IF EXISTS service'''
    cursor.execute(drop_table_service)
        
    create_table_service = '''CREATE TABLE service
          (ID INT PRIMARY KEY    NOT NULL,
          NAME           TEXT    NOT NULL,
          CLIENT_ID      TEXT,  
          SERVICE_DATE   TEXT,  
          FACILITY_ID    TEXT,  
          SERVICE_AMOUNT TEXT,
          SERVICE_COST   TEXT,
          PROVIDER_ID    TEXT); '''
    
    cursor.execute(create_table_service)
    connection.commit()
    
    print("New table Service created successfully in PostgreSQL ")
    print("Insert data in table Service")
    print("-----------------------------")

    service_types={'Consult', 'CABG', 'Post op care', 'Eye Exam', 'Insulin', 'Cataract', 'Abortion', 'Consult'}
    postgres_insert_query = """ INSERT INTO service (ID, NAME, CLIENT_ID, SERVICE_DATE, FACILITY_ID, SERVICE_AMOUNT, SERVICE_COST, PROVIDER_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    for x in range(20):
      name         = random.choice(tuple(service_types))
      clientid     = x+1
      servicedate  = datetime.datetime(2018, random.randint(1,12), random.randint(1,28))
      facilityid   = x+1
      serviceamount= random.randint(1,10)
      servicecost  = random.randint(1,10)*random.randint(5,10)
      providerid   = x+1
      record_to_insert = (x+1, name, clientid, servicedate, facilityid, serviceamount, servicecost, providerid)
      cursor.execute(postgres_insert_query, record_to_insert)
      print("Table Service insert:{}".format(record_to_insert))
      connection.commit()

    print("Table Service populated with TEST data.")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table SERVICE. ", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")    