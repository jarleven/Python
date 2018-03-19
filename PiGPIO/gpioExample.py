
import os    
import time

rpi = False

if os.uname()[1] == 'raspberrypi':
    rpi = True

    # This is because : 
    # uname -a
    # Linux raspberrypi 4.4.50-v7+ #970 SMP Mon Feb 20 19:18:29 GMT 2017 armv7l GNU/Linux


    import RPi.GPIO as GPIO # import our GPIO library
    GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM
    print("Running on Raspberry Pi target!")


    
def gpio_setup(pin,direction):
    print("Setting pin %d direction as %s" % (pin, direction))

    if rpi:
        if directio == "Out":
            GPIO.setup(pin,GPIO.OUT)
        else:
            GPIO.setup(pin,GPIO.IN)


def gpio_output(pin, level):
    print("Setting pin %d level as %d" % (pin, level))

    if rpi:
        if level == True:
            GPIO.output(pin,GPIO.HIGH)
        else:
            GPIO.output(pin,GPIO.LOW)


# Setup pin direction
gpio_setup(17, "Out")

# Blink the pin
while True:
    gpio_output(17,True)
    time.sleep(1)
    gpio_output(17,False)
    time.sleep(1)
