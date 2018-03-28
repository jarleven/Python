# -*- coding: utf-8 -*-
"""

Inspiration from :  http://shazsterblog.blogspot.no/2013/12/raspberry-pi-led-blinker.html

"""


import time 
import threading


class Blinker(threading.Thread):
    def __init__(self, speed, times):    
        threading.Thread.__init__(self);
        self.speed = speed;    
        self.times = times;

    def run(self):
        for i in range(0,self.times):
            print("  Time : %d" % ((i+1)))
            print("    High")
            time.sleep(self.speed)
            print("    Low")
            time.sleep(self.speed)
        print("  Blinking Complete!")


print("Main loop Start")

blinker = Blinker(1, 5)
blinker.start()

print("Main loop done")
