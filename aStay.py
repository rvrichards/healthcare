#Create a Stay
#
import constant
import psycopg2
import random
import datetime
from faker import Faker
from psycopg2 import Error

print ("Create a Stay ")
print ("-------------")
print ("This will delete the old table.")
try:
    connection = psycopg2.connect(user = "test", password = "test",  host = "127.0.0.1",  port = "5432", database = "test")
    cursor = connection.cursor()
    
# --------------------Stay------------------------------------------------------------------
# --------------------Stay------------------------------------------------------------------
    drop_table_stay = '''DROP TABLE IF EXISTS stay'''
    cursor.execute(drop_table_stay)
        
    create_table_stay = '''CREATE TABLE stay
          (ID INT PRIMARY KEY    NOT NULL,
          SERVICE_ID      TEXT   NOT NULL,
          CLIENT_ID       TEXT,  
          STAY_DATE_START TEXT,  
          STAY_DATE_END   TEXT,  
          FACILITY_ID     TEXT,  
          PROVIDER_ID     TEXT); '''
    
    cursor.execute(create_table_stay)
    connection.commit()
    
    print("New table Stay created successfully in PostgreSQL ")
    print("Insert data in table Stay")
    print("-------------------------")


    postgres_insert_query = """ INSERT INTO stay (ID, SERVICE_ID, CLIENT_ID, STAY_DATE_START, STAY_DATE_END, FACILITY_ID, PROVIDER_ID) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    for x in range(constant.NUMBER_OF_STAYS):
      serviceid   = random.randint(1,constant.NUMBER_OF_SERVICES)
      clientid    = random.randint(1,constant.NUMBER_OF_CLIENTS)
      staydate    = datetime.datetime.now() - datetime.timedelta(days=random.randint(10,666))
      enddate     = staydate + datetime.timedelta(days=random.randint(1,9))
      facilityid  = random.randint(1,constant.NUMBER_OF_FACILITIES)
      providerid  = random.randint(1,constant.NUMBER_OF_PROVIDERS)
      record_to_insert = (x+1, serviceid, clientid, staydate, enddate, facilityid, providerid)
      cursor.execute(postgres_insert_query, record_to_insert)
      print("Table Stay insert:{}".format(record_to_insert))
      connection.commit()

    print("Table Stay populated with TEST data.")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table STAY. ", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")    