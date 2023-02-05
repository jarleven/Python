# https://hackspace.raspberrypi.com/books/micropython-pico/pdf
# https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf

# For more details and step by step guide visit: Microcontrollerslab.com
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import time
import ntptime
import network

# Garbage collector
import gc
gc.collect()

ssid = '3DATA'
password = 'Vinter2022'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass 

print('Connection successful')
print(station.ifconfig())

# If the code is to run for a long time you need to refresh the ntp time regularly
ntptime.settime()

while True:
    # This is UTC
    utc = time.localtime() 
    # (year, month, mday, hour, minute, second, weekday, yearday)
    print(utc)
    # Format and add 1 hour, dirty hack !
    lokaltid = ("Klokka er %s:%s:%s"%(utc[3]+1,utc[4],utc[5]))
    print(lokaltid)
    print("")
    time.sleep(1)


