import serial
import time

#===========================================================
# Define "TJC LCD control"
end = [0xff,0xff,0xff]
port_lcd = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=3.0)
ary_end = bytearray(end)

#===========================================================
# Define "Misubishi PLC reader"
port_plc=serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity='O',stopbits=1,bytesize=8,timeout=1.0)

#===========================================================
#	Misubishi PLC reader
#===========================================================
def Read_PLC():
    sendout = (chr(5)+"01FFWRAD090002")
    port_plc.write(sendout.encode())
    receive()

def f(s):
    return "" if not s else f(s[4:]) + s[:4]

def receive():
    received = port_plc.read(29).decode()

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

    #output3 = "n0.val=" + str(toint)
    #port_lcd.write(output3.encode())
    #port_lcd.write(ary_end)

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
#	Main Loop
#===========================================================
def main():
	#tangle_io = 0
	while True:
		#tangle_io = tangle_io ^ 1
		#lcd_comd(tangle_io)
		Read_PLC()
		time.sleep(0.5)

if __name__ == '__main__':
    main()
