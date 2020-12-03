import serial
import time
#serial連線
#ser=serial.Serial(port="/dev/ttyUSB0",baudrate=9600,parity='O',stopbits=1,bytesize=8,timeout=1.0)
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
		time.sleep(1)

def f(s):
	return "" if not s else f(s[4:]) + s[:4]


def receive():

	received = ser.read(29).decode()

	print(">>>> received: " + (received))

	###格式化收到的東西
	index1 = received.find('FF')
	print('index1=', index1)
	str1 = received[index1 + 2:]
	print('str1=', str1)
	index2 = str1.find('FF')
	print('index2=', index2)
	if index2 == -1:
		received = str1[: 8]
	else:
		str2 = str1[index2 + 2: index2 + 10]
		received = str2
	print(received)

	#數值轉換->str->int(hex)->int(dec)
	hexa = str(f(received))
	toint = (int(hexa, 16))
	print("==========PLC Value:" + str(toint))



def _main_():
#	#選單
	sendaway()


_main_()
