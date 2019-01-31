# **Guide**

--------------------
### __Requirements__
- Python3+
- SQLite – included with Python, no need to install
- Python pip – for installing packages
- Paho MQTT Client – Install it with pip command “pip install paho–mqtt"
- MQTT Broker – If you don’t have your own, use “iot.eclipse.org“

### __Usage__
Run the files in turn below :
1. __Init_Database.py__ : Creat “sensor.db” sqlite database file with Tables Temperature and Humidity.
2. __Publish.py__ : Publishing random values to Broker.
3. __Subscribe.py__ : Subscribe to topics on Broker.
4. __Get_Data_to_DB.py__ : Get values to “sensor.db” sqlite database
___

### __Having problems?__
Please contact for me __nam2297ptit@gmail.com_