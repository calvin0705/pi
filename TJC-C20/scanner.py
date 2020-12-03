import time
import serial
import RPi.GPIO as GPIO
import threading


PIN=18

def reset_gpio():
    print('reset gpio ...')
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup(PIN)
    GPIO.setup(PIN, GPIO.OUT, initial=1)

def trigger_gpio():
    print('trigger gpio ...')
    while True:
        print('[[ Trigger GPIO ... ]]')
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(2)
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(0.5)

def act_scanner():
    print('act scanner ....')
    reset_gpio()
    trigger_gpio()
    
ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        timeout=1
)

def read():
    print('reading...')
    counter = 1
    scanner_serial = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    while True:
        try:
            while True:
                print('------')
                #readline = scanner_serial.readline()
                readline = scanner_serial.readline()
                if readline:
                    print('{}: read:{}\n'.format(counter, readline.decode('utf-8')))
            counter += 1
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit()
        except Exception as err:
            print(err)

t = threading.Thread(target = act_scanner)
t.start()

read()

