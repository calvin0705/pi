import serial
import re
import time
#serial連線
ser=serial.Serial(port='com5',baudrate=9600,parity='O',stopbits=1,bytesize=8,timeout=1.0)
#發出
def sendaway():

	while 1:
		#合拼成發出的格式
		sendout = (chr(5)+"00FFWRAD090002")
		print("發出: " + sendout)
		#送出
		ser.write(sendout.encode())
		time.sleep(1)
		receive()

#解碼每2個字倒轉
def f(s):
    return "" if not s else f(s[4:]) + s[:4]

#接收
def receive():
	val = {}
	#接收
	received = ser.read(29).decode()
	print("收到: "+(received))

	#格式化收到的東西
	m =re.search(r'FF(.*)FF(.{8})', received)
	val[0] = (m.group(0))
#	print('v0:', val[0])
	val[1] = (m.group(1))
#	print('v1:', val[1])
	val[2] = (m.group(2))
#	print('v2:', val[2])

	# 數值轉換->str->int(hex)->int(dec)
	hexa = str(f(val[2]))
#	print('hexa=', hexa)
	toint = (int(hexa, 16))
#	print('toint=', toint)
	print("==========\n機台:" + str(val[1]) + "\n數值:" + str(toint) + "\n==========")


def _main_():
	#選單
	sendaway()


_main_()
