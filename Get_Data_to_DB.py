#!/usr/bin/python

import sqlite3
import json

# SQLite DB Name
DB_Name =  "sensor.db"

#json_Dict = json.loads(jsonData)
# SensorID = 1
# Data_and_Time = "31-Jan-2019 23:23:52:610629"
# Value = 23.4

# #Push into DB Table
# conn = sqlite3.connect(DB_Name)
# print ("Opened database successfully")
# conn.execute("INSERT INTO Temperature (SensorID,Date_and_Time, Value) \
#       VALUES (?,?,?)",[SensorID,Data_and_Time, Value])
# conn.commit()
# print ("Records created successfully")
# conn.close()

def Temperature(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Value = json_Dict['Temperature']
	
	#Push into DB Table
	conn = sqlite3.connect(DB_Name)
	conn.execute("INSERT INTO Temperature (SensorID,Date_and_Time, Value) \
	      VALUES (?,?,?)",[SensorID,Data_and_Time, Value])
	conn.commit()
	print ("Temperature created new value")
	print("")
	conn.close()


def Humidity(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Value = json_Dict['Humidity']
	
	#Push into DB Table
	conn = sqlite3.connect(DB_Name)
	conn.execute("INSERT INTO Humidity (SensorID,Date_and_Time, Value) \
	      VALUES (?,?,?)",[SensorID,Data_and_Time, Value])
	conn.commit()
	print ("Humidity created new value")
	print("")
	conn.close()

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "Home/BedRoom/DHT22/Temperature":
		Temperature(jsonData)
	elif Topic == "Home/BedRoom/DHT22/Humidity":
		Humidity(jsonData)	