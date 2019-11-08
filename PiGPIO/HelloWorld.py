# As simple as it gets

#
# Import Libraries
#

import time
import RPi.GPIO as GPIO # import our GPIO library

#
# Define our stuff
#

GPIOPIN = 4   # The pin we blink on the Raspberry Pi
BLINKTIME = 1 # Time in seconds for LED states


#
# Code 
#

GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM

GPIO.setup(GPIOPIN,GPIO.OUT)
#GPIO.setup(pin,GPIO.IN)


print("Pi light'em up!")

# Forever go roundabout here blinking the LED
while True:
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(BLINKTIME)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(BLINKTIME)
