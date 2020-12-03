import serial
import re

ser=serial.Serial(port="com5",baudrate=9600,parity='O',stopbits=1,bytesize=8,timeout=1.0)

def sendaway():
    sendout = (chr(5)+"01FFWRAD090002")
    ser.write(sendout.encode())
    receive()

def f(s):
    return "" if not s else f(s[4:]) + s[:4]

def receive():
    received = ser.read(29).decode()

    index1 = received.find('FF')
    str1 = received[index1 + 2:]
    index2 = str1.find('FF')
    if index2 == -1:
        received = str1[: 8]
    else:
        str2 = str1[index2 + 2: index2 + 10]
        received = str2

    hexa = str(f(received))
    toint = (int(hexa, 16))
    print("==========ActQty:" + str(toint))
    return toint

def _main_():
    while 1:
        sendaway()

_main_()
