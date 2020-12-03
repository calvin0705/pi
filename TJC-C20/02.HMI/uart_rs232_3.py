import serial
import time


end = [0xff,0xff,0xff]
porta = serial.Serial(port='com4',baudrate=9600,parity='N',stopbits=1,bytesize=8,timeout=3.0)
ary_end = bytearray(end)
n=1
b=1
c=0
while True:
	print(n)

	output="z0.val=" + str(n)
	porta.write(output.encode())
	porta.write(ary_end)
	n=n+9
	if (n > 180):
		n = 0

	output2 = "n0.val=" + str(b)
	porta.write(output2.encode())
	porta.write(ary_end)
	b = b +98

	output3 = "pio1=" + str(c)
	porta.write(output3.encode())
	porta.write(ary_end)
	c = ~c

	time.sleep(0.2)