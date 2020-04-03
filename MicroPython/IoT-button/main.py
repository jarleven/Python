# Set internal LED with the FLASH pushbutton. Interrupt controlled
from machine import Pin
from machine import Timer
from machine import reset
import boot
import ubinascii
import gc

from machine import I2C
import sh1106
import framebuf

#from uptime import uptime
import utime
import time

import socket

PRELLTIME=100
POLLTIME=100
IGNORETIME=100


# Send the data over the network
def sendData(netData):
    print("Sending data: ")
    print(netData)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(netData + "\n\n")
    received = sock.recv(1024)
    sock.close()

    print("Got data echo: ")
    print(received)


def system_debug():

    print("-------DEBUG-------")

    print("  Free memory before gc.collect() %d " % gc.mem_free())
    gc.collect()
    print("  Free memory after gc.collect()  %d " % gc.mem_free())

    # MorganTimney  from https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days/37194105
    print("  Uptime %d seconds" % (utime.ticks_ms()/1000))
    days = divmod(utime.ticks_ms()/1000, 86400)
    # days[0] = whole days and
    # days[1] = seconds remaining after those days
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    print("  %i days, %i hours, %i minutes, %i seconds" % (days[0], hours[0], minutes[0], minutes[1]))
    print("-------DEBUG-------")


class Pushbutton(object):

    def __init__(self, idx, pin):
        self.idx=idx
        self.pin=pin
        self.state = 0


        self.button = Pin(self.pin, Pin.IN, Pin.PULL_UP)        
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.isr_cb)
        

        self.enirq()
        self.timer = Timer(-1)


    def get_state(self):
        return(self.state)

    
    def timer_cb(self, tim):

        if self.state == 1:
            if self.button.value():
                self.state = 0
                self.enirq()
                print("Ignored glitch press %d, waiting for new user input" % self.idx)
            else:
                self.timer.init(period=IGNORETIME, mode=Timer.ONE_SHOT, callback=self.timer_cb)
                self.state = 2

        if self.state == 2:
             if self.button.value():
                print("Captured button press %d" % self.idx)
                self.state = 3

             else:
                self.timer.init(period=IGNORETIME, mode=Timer.ONE_SHOT, callback=self.timer_cb)
                print("Button not released %d" % self.idx)


    def isr_cb(self, isr):
        print("cb")
        self.disirq()
        self.state=1
        self.timer.init(period=IGNORETIME, mode=Timer.ONE_SHOT, callback=self.timer_cb)

 
    def enirq(self):
        self.state=0
        print("Enable IRQ %d" % self.idx)
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.isr_cb)
        self.button = Pin(self.pin, Pin.IN, Pin.PULL_UP)

    # For the ESP8266 there is some chaos regarding the pin interrupt handling
    # Quote Mar 17, 2018 "p.irq(trigger=0,handler=callback) seems to properly disable the interruptions."
    # https://github.com/micropython/micropython/issues/2847
    def disirq(self):
        print("Disable IRQ %d" % self.idx)
        self.button.irq(trigger=0, handler=self.isr_cb)

    # TODO is this needed ??
    def __iter__(self):
        pass






print("Free memory %d " % gc.mem_free()) 

pins=myConfig.pins
led=myConfig.LEDPIN
HOST, PORT=(myConfig.HOST, myConfig.PORT)
module=myConfig.module

# The MAC address of the module, human readable
espmac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()   

# Define the value of the pushbuttons from the physical MAC address
if espmac in module:
    print("Found MAC %s" % espmac)
    lamp = module[espmac]
else:
    print("Unknown device MAC %s" % espmac)
    lamp = [10, 6, 7, 8]

print("IO pins are : ", pins)
print("LAMPS are   : ", lamp)


onboardLED = Pin(led, Pin.OUT)
onboardLED.off()


buttons = []
 
for i in range(4):
    buttons.append(Pushbutton(i, pins[i]))


# Orange SDA  D5   GPIO14  BUTTON4 on v1 (remove capacitors)
# Gul    SCL  D0   GPIO16  TP2 on v1
i2c = I2C(scl=Pin(16), sda=Pin(14))


print('Scan i2c bus...')
devices = i2c.scan()

lcdpresent=False

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    if device == 0x3c:
        print("LCD found")
        lcdpresent=True        

if lcdpresent:
    display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
    display.sleep(False)
    display.fill(0)
    #display.text('Testing 2', 0, 0, 1)
    display.text(sta_if.ifconfig()[0], 0, 0, 1)

    display.show()

    time.sleep(1)
    wdt.feed()
    time.sleep(1)
    wdt.feed()


    #with open('scatman.pbm', 'rb') as f:
    #    f.readline() # Magic number
    #    f.readline() # Creator comment
    #    f.readline() # Dimensions
    #    data = bytearray(f.read())
    #fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
    #
    #display.invert(1)
    #display.blit(fbuf, 0, 0)
    #display.show()






print("Free memory %d " % gc.mem_free()) 
print("Startring main")
gc.collect()


ServSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_addr = ("",21567)
ServSock.setblocking(0)
ServSock.bind(listen_addr)


# Loop
counter=0
beat=0
while True:

    try:
        data,addr = ServSock.recvfrom(1024)
        if data:
            #print(data.strip(),addr)
            #
            # The images here : https://www.twobitarcade.net/article/displaying-images-oled-displays/
            # Can now be transferred with netcat
            # cat scatman.1.bin | nc -u 192.168.2.228 21567 -w 0 
            #
            image = bytearray(data.strip()) 

            fbuf = framebuf.FrameBuffer(image, 128, 64, framebuf.MONO_HLSB)

            display.fill(0)
            display.blit(fbuf, 0, 0)
            display.show()




#        print(data.strip(),addr)
#        display.fill(0)
#        display.text(data.strip(), 0, 0, 1)
#        display.show()

    except:
        pass

    wdt.feed()
    if(counter>10000):
        counter=0
        beat=beat+1
        print("It's alive %05d" % beat)
        #display.text("It's alive %05d" % beat, 0, 10, 1)
        #display.show()

    counter = counter + 1

    #line, _ = sock.recvfrom(180)

    #if len(line) > 0:
    #    print("UDP data %s" % line)


    if(boot.sta_if.isconnected()):
        onboardLED.off()
    else:
        onboardLED.on()

    for button in buttons:
        if button.get_state() == 3:
            button.enirq()
            print("Button %d say hello" % button.idx)

            if button.idx == 0:
                system_debug()
            else:

                lampID=lamp[button.idx]
                netData = "binary LED%d toggle" % lampID

                sendData(netData)
                print("Action on LED%d" % lampID)


