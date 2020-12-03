import serial
import time

def readlineCR(port):
    rv = ""
    while True:
        ch = port.readlines()
 #       rv += ch
 #       if ch=='\r' or ch=='':
 #           return rv
        return ch

def run():
    ptn1 = [0x05, 0x30, 0x30, 0x46, 0x46, 0x57, 0x52, 0x30, 0x44, 0x30, 0x39, 0x30, 0x32, 0x30, 0x32]
    ptn2 = [0x06, 0x30, 0x30, 0x46, 0x46]
    # port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    port = serial.Serial(port='com5', baudrate=9600, parity='O', stopbits=1, bytesize=8, timeout=1.0)
    # print("baudrate:{}".format(Ubaudrate))
    ary1 = bytearray(ptn1)
    ary2 = bytearray(ptn2)
    while True:
        port.write(ary1)
        time.sleep(0.00)
        port.write(ary2)
        time.sleep(0.0)
        rcv = readlineCR(port)
        #    port.write('\r\nYou sent:'+repr(rcv))
        print(rcv)
        time.sleep(0)

if __name__ == '__main__':
    run()