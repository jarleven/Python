"""

https://www.tutorialspoint.com/python3/python_multithreading.htm

Stort spørsmål er om dette kan kjøre inne i flask 

rm -f setup.sh && wget https://raw.githubusercontent.com/jarleven/flaskapp/main/luma/setup.sh && chmod +x setup.sh && ./setup.sh

"""

from luma.core.interface.serial import pcf8574
from luma.lcd.device import hd44780

import _thread
import time

hallo = "Starting"
    
interface = pcf8574(address=0x27, backlight_enabled=True)
device = hd44780(interface, width=16, height=2)
#device.text = hallo

# Define a function for the thread
def print_time( threadName, delay, device):
   global hallo
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      device.text = hallo

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, device,))

   for i in range(10):
        time.sleep(5)
        hallo=str(i)
        print("Main is ", i)

except:
   print ("Error: unable to start thread")

while 1:
   pass

