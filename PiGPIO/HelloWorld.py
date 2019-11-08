# As simple as it gets

#
# Import Libraries
#

import time
import RPi.GPIO as GPIO # import our GPIO library

#
# Define our stuff
#

# The pin we blink on the Raspberry Pi, and the delay in seconds
GPIOPIN = 4
# Time in seconds for LED states
BLINKTIME = 1


#
# Code 
#

GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM

GPIO.setup(GPIOPIN,GPIO.OUT)
#GPIO.setup(pin,GPIO.IN)



# Blink the pin
print("Pi light'em up!")

# Just go roundabout here blinking the LEDs
while True:
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(BLINKTIME)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(BLINKTIME)
