import serial
import time
import re
import os
import pymongo
import logging
from random_object_id import generate

#===========================================================
# Define "TJC LCD control"
end = [0xff,0xff,0xff]
port_lcd = serial.Serial(port='com4', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=3.0)
ary_end = bytearray(end)

#===========================================================
# Define "Misubishi PLC reader"
port_plc=serial.Serial(port='com5',baudrate=9600,parity='O',stopbits=1,bytesize=8,timeout=1.0)

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
    logging.error('PLC read fail ~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!~~~~~~~~!!!!!!!!')
    port_plc.close()
    time.sleep(0.5)
    port_plc.open()

def receive():
    received = port_plc.read(14).decode(errors='ignore')
    print(received)

    isPlcNone = re.search(r'01FF(.{8})', received)
    if (isPlcNone == None):
        plc_serial_reset()
        return 0

    val = {}
    val[0] = (isPlcNone.group(0))
    val[1] = (isPlcNone.group(1))
    hexa = str(f(val[1]))
    toint = (int(hexa, 16))
    print(toint)

    # ---------------------------------------
    # Show output in TJC LCD
    # ---------------------------------------
    output3 = "n0.val=" + str(toint)
    port_lcd.write(output3.encode())
    port_lcd.write(ary_end)

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
#	Main Loop
#===========================================================
def main():
	tangle_io = 0
	while True:
		tangle_io = tangle_io ^ 1
		lcd_comd(tangle_io)
		Read_PLC()
		time.sleep(0)

if __name__ == '__main__':
    main()