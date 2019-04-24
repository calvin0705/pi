import RPi.GPIO as GPIO
from time import sleep

"""PIN DEFINE"""
LED_O_1 = 3
LED_O_2 = 4
LED_O_3 = 24
LED_O_4 = 23

LED_I_1 = 17
LED_I_2 = 27
LED_I_3 = 22
LED_I_4 = 10

HIGH = 1
LOW = 0

"""BROADCOM IC PINOUT"""
GPIO.setmode(GPIO.BCM)

""" Setting GPIO I/O"""
GPIO.setup(LED_I_1, GPIO.IN)
GPIO.setup(LED_I_2, GPIO.IN)
GPIO.setup(LED_I_3, GPIO.IN)
GPIO.setup(LED_I_4, GPIO.IN)

GPIO.setup(LED_O_1, GPIO.OUT)
GPIO.setup(LED_O_2, GPIO.OUT)
GPIO.setup(LED_O_3, GPIO.OUT)
GPIO.setup(LED_O_4, GPIO.OUT)


def SET_LED(PIN1,PIN2,PIN3,PIN4,LED_OUT):
	GPIO.output(PIN1, LED_OUT)
	GPIO.output(PIN2, LED_OUT)
	GPIO.output(PIN3, LED_OUT)
	GPIO.output(PIN4, LED_OUT)
	sleep(2)
	
def READ_IO():
	if GPIO.input(LED_I_1):
		print(LED_I_1,'was HIGH++++++++')
	else:
		print(LED_I_1,'was LOW')
		
	if GPIO.input(LED_I_2):
		print(LED_I_2,'was HIGH++++++++')
	else:
		print(LED_I_2,'was LOW')
		
	if GPIO.input(LED_I_3):
		print(LED_I_3,'was HIGH++++++++')
	else:
		print(LED_I_3,'was LOW')
		
	if GPIO.input(LED_I_4):
		print(LED_I_4,'was HIGH++++++++')
	else:
		print(LED_I_4,'was LOW')

	
while True:

	SET_LED(LED_O_1,LED_O_2,LED_O_3,LED_O_4,HIGH)
	
	READ_IO()	
		
	SET_LED(LED_O_1,LED_O_2,LED_O_3,LED_O_4,LOW)
	
	READ_IO()