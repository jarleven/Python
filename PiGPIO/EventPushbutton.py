# Eventdriven pushbutton

import RPi.GPIO as GPIO

def myCallback(channel):
    print("Button %s was pushed" % channel)

print("Connect button to GPIO17/PIN11 and GND")
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.add_event_detect(17, GPIO.FALLING, callback=myCallback, bouncetime=250)
while True:
    pass

