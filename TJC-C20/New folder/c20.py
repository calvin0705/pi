#!/usr/bin/python3

import serial
import time
import re
import pymongo
from pymongo import MongoClient
from random_object_id import generate
from datetime import datetime

#===========================================================
# Define "TJC LCD control"
end = [0xff,0xff,0xff]
port_lcd = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)

#===========================================================
# Define "Misubishi PLC reader"
port_plc = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity='O',stopbits=1,bytesize=8,timeout=0.5)

#===========================================================
#	Misubishi PLC reader
#===========================================================
def Read_PLC():
    sendout = (chr(5)+"01FFWRAD090002")
    port_plc.write(sendout.encode())
    receive()

def f(s):
    return "" if not s else f(s[4:]) + s[:4]

def plc_serial_reset():
    print("fail~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!")
    print("fail~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!")
    print("fail~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!")
    port_plc.close()
    time.sleep(0.5)
    port_plc.open()

def receive():
    received = port_plc.read(14).decode(errors='ignore')
    print(received)

    isPlcNone = re.search(r'01FF(.{8})', received)
    if(isPlcNone == None):
        plc_serial_reset()
        return 0

    val = {}
    val[0] = (isPlcNone.group(0))
    val[1] = (isPlcNone.group(1))
    hexa = str(f(val[1]))
    toint = (int(hexa, 16))
    print(toint)

    output3 = "n0.val=" + str(toint)
    port_lcd.write(output3.encode())
    port_lcd.write(ary_end)


    bson_id = generate()
    tfa20_time = time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    record = { "_id": bson_id,
            "Time": tfa20_time,
            "name": "Calvin",
            "Output": toint}

    collection.insert_one(record)

    return toint


#===========================================================
#	TJC LCD control
#===========================================================
def lcd_comd(tangle_io):
	output1 = "pio1=" + str(tangle_io)
	port_lcd.write(output1.encode())
	port_lcd.write(ary_end)

	output2 = "b1.pic=" + str(tangle_io)
	port_lcd.write(output2.encode())
	port_lcd.write(ary_end)


#===========================================================
#	MongoDB
#===========================================================
# importing Mongoclient from pymongo
#from pymongo import MongoClient

host = "10.0.105.158"
port = "27018"
user = "c20admin"
password = "c20pwd"
db_name = "c20"
auth_mechanism = "SCRAM-SHA-1"
uri = "mongodb://"+user+":"+password+"@"+host+":"+port+"/"+db_name+"?"+"authMechanism="+auth_mechanism
client = pymongo.MongoClient(uri) #client object to connect

# database
db = client["c20"]

# Created or Switched to collection
# names: GeeksForGeeks
collection = db["tfa20"]

#def mongo_test():
#    bson_id = generate()
#    tfa20_time = time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
#
#    record = { "_id": bson_id,
#            "Time": tfa20_time,
#            "name": "Calvin",
#            "Output": "1005"}
#
#    collection.insert_one(record)


#===========================================================
#	Main Loop
#===========================================================
def main():
    tangle_io = 0
    while True:
        tangle_io = tangle_io ^ 1
        lcd_comd(tangle_io)
        Read_PLC()
        #mongo_test()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
