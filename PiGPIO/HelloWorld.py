# As simple as it gets

# Log in to your Pi
# Download this file and execute it with the following commands.
#
# wget https://raw.githubusercontent.com/jarleven/Python/master/PiGPIO/HelloWorld.py
# python3 HelloWorld.py
#
#

#
# Import Libraries
#

import time
import RPi.GPIO as GPIO # import our GPIO library

#
# Define our stuff
#

MYLEDPIN = 4   # The pin we blink on the Raspberry Pi GPIO4 / Pin7
BLINKTIME = 1  # Time in seconds for LED states

#            https://github.com/tvierb/raspberry-ascii
#
#                            J8
#                           .___.              
#                  +3V3---1-|O O|--2--+5V
#          (SDA)  GPIO2---3-|O O|--4--+5V
#         (SCL1)  GPIO3---5-|O O|--6--GND
#    (GPIO_GLCK)  GPIO4---7-|O O|--8-----GPIO14 (TXD0)
#                   GND---9-|O.O|-10-----GPIO15 (RXD0)
#    (GPIO_GEN0) GPIO17--11-|O O|-12-----GPIO18 (GPIO_GEN1)
#    (GPIO_GEN2) GPIO27--13-|O O|-14--GND 
#    (GPIO_GEN3) GPIO22--15-|O O|-16-----GPIO23 (GPIO_GEN4)
#                  +3V3--17-|O O|-18-----GPIO24 (GPIO_GEN5)
#     (SPI_MOSI) GPIO10--19-|O.O|-20--GND 
#     (SPI_MOSO) GPIO9 --21-|O O|-22-----GPIO25 (GPIO_GEN6)
#     (SPI_SCLK) GPIO11--23-|O O|-24-----GPIO8  (SPI_C0_N)
#                   GND--25-|O O|-26-----GPIO7  (SPI_C1_N)
#       (EEPROM) ID_SD---27-|O O|-28-----ID_SC Reserved for ID EEPROM
#                GPIO5---29-|O.O|-30--GND
#                GPIO6---31-|O O|-32-----GPIO12
#                GPIO13--33-|O O|-34--GND
#                GPIO19--35-|O O|-36-----GPIO16
#                GPIO26--37-|O O|-38-----GPIO20
#                  GND--39-|O O|-40-----GPIO21
#                           '---'
#                       40W 0.1" PIN HDR


#
# Code 
#

GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM That is GPIOxx as in the figure above

GPIO.setup(MYLEDPIN,GPIO.OUT)

print("Pi light'em up! Press Ctrl+C to exit")
try:
    # Forever go roundabout here blinking the LED
    while True:
        print("Blink ---___")
        GPIO.output(MYLEDPIN,GPIO.HIGH)
        time.sleep(BLINKTIME)
        GPIO.output(MYLEDPIN,GPIO.LOW)
        time.sleep(BLINKTIME)
          
except KeyboardInterrupt:
    print("Someone pressed Ctrl+C, goodbye!")
    GPIO.cleanup()
