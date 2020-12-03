import urllib
import time

def main():
    while True:
        wifi_ip = check_output(['hostname', '-I'])
        if wifi_ip is not None:
            time.sleep(0.5)


if __name__ == '__main__':
    main()
    
==========================================================

https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679

import threading
import time

def task():
  print("Timer object is getting executed...")
  threading.Timer(1, task).start()

if __name__=='__main__':
  task()