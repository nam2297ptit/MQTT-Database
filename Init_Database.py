import sqlite3
import json

# SQLite DB Name
DB_Name =  "sensor.db"
#Create Database
conn = sqlite3.connect(DB_Name)
print ("Create database successfully")
#Create table Temperature
conn.execute('''CREATE TABLE Temperature
        (id 				INT ,     
         SensorID           char(20)    NOT NULL,
         Date_and_Time      datetime    NOT NULL,
         Value         		real 		NOT NULL );''')
#Create table Humidity
conn.execute('''CREATE TABLE Humidity
        (id 				INT ,     
         SensorID           char(20)    NOT NULL,
         Date_and_Time      datetime    NOT NULL,
         Value      		real 		NOT NULL );''')

print ("Table created successfully")
conn.close()