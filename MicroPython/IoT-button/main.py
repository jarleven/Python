# Set internal LED with the FLASH pushbutton. Interrupt controlled
from machine import Pin
from machine import Timer
from machine import reset
import socket
import boot
import ubinascii
import gc

#from uptime import uptime
import utime
import time


PRELLTIME=100
POLLTIME=100
IGNORETIME=100

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



button = [None] * 4
tim = [None] *4
SendState = [None] *4

# TODO make a class : https://docs.micropython.org/en/latest/reference/isr_rules.html

def isr_one(p):
    isr_common(0)

def isr_two(p):
    isr_common(1)

def isr_three(p):
    isr_common(2)

def isr_four(p):
    isr_common(3)


def timer_cb_one(t):
    timer_cb_common(0)

def timer_cb_two(t):
    timer_cb_common(1)

def timer_cb_three(t):
    timer_cb_common(2)

def timer_cb_four(t):
    timer_cb_common(3)


isr_func = [isr_one, isr_two, isr_three, isr_four]
timer_cb = [timer_cb_one,timer_cb_two,timer_cb_three, timer_cb_four]



for idx in range(4):
    SendState[idx] = 0 # 0 idle, 1 ISR, 2 Steadey
    button[idx] = Pin(pins[idx], Pin.IN, Pin.PULL_UP)
    tim[idx] = Timer(-1)



# For the ESP8266 there is some chaos regarding the pin interrupt handling
# Quote Mar 17, 2018 "p.irq(trigger=0,handler=callback) seems to properly disable the interruptions."
# https://github.com/micropython/micropython/issues/2847

def enable_btirq(idx):
    button[idx].irq(trigger=Pin.IRQ_FALLING, handler=isr_func[idx])
    button[idx] = Pin(pins[idx], Pin.IN, Pin.PULL_UP)

def disable_btirq(idx):
    button[idx].irq(trigger=0, handler=isr_func[idx])



def isr_common(idx):
    global SendState              # To modify a global variable we need to state it's name
    SendState[idx] = 1
    disable_btirq(idx)
      

def timer_cb_common(idx):

    if SendState[idx] == 2:
        if button[idx].value():
            SendState[idx] = 0
            enable_btirq(idx)
            print("Ignored glitch press %d, waiting for new user input" % idx)
        else:
            print("Captured button press %d" % idx)
            SendState[idx] = 3

    else:

        if not button[idx].value():
            tim[idx].init(period=PRELLTIME, mode=Timer.ONE_SHOT, callback=timer_cb[idx])
            print("Button %d not released" % idx)
        else:
            enable_btirq(idx)
            print("Ready button %d, waiting for new user input" % idx)


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




# Register interrup pin
for idx in range(4):
    enable_btirq(idx)
    print("Enabling button %d" % idx)

print("Free memory %d " % gc.mem_free()) 
print("Startring main")
gc.collect()

# Loop
while True:

    wdt.feed()


    if(boot.sta_if.isconnected()):
        onboardLED.off()
    else:
        onboardLED.on()
        

    for idx in range(4):
        if SendState[idx] == 1:
            # Clear the new event flag set in the interrupt
            print("Trigger, wait a bit")
            SendState[idx] = 2


            # We have an event and the interrupt was disabled. Enable the interruptagain with the timer
            # This is our debounce
            tim[idx].init(period=IGNORETIME, mode=Timer.ONE_SHOT, callback=timer_cb[idx])
            # Timer example from https://www.dfrobot.com/blog-606.html

        if SendState[idx] == 3:

            SendState[idx] = 0
            tim[idx].init(period=POLLTIME, mode=Timer.ONE_SHOT, callback=timer_cb[idx])

            if(idx==0):
                print("-------DEBUG-------")
                for a in range(1, 4):
                    print("  ID %d  state %d" % (a, SendState[a]))
                                
                    enable_btirq(a)
                print("  Free memory %d " % gc.mem_free()) 
                gc.collect()
                print("  Free memory %d " % gc.mem_free()) 

                print("  Uptime %d seconds" % (utime.ticks_ms()/1000))
                print("       DEBUG")
                    

            else:

                netValue = lamp[idx]
                netData = "binary LED%d toggle" % (netValue)

                sendData(netData)
                print("Action on LED%d" % lamp[idx])


