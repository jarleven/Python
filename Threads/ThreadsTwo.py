"""

Inspiration from :  http://shazsterblog.blogspot.no/2013/12/raspberry-pi-led-blinker.html

"""


import time 
import threading


class Blinker(threading.Thread):
    def __init__(self, speed, times, inst):    
        threading.Thread.__init__(self);
        self.speed = speed;    
        self.times = times;
        self.inst = inst;    

    def run(self):
        for i in range(0,self.times):
            print("  Time : %d  inst: %d" % ((i+1), self.inst ))
            print("    High")
            time.sleep(self.speed)
            print("    Low")
            time.sleep(self.speed)
        print("  Blinking Complete!")


print("Main loop start")

blinker = Blinker(0, 0, 0)

for x in range(0,10):
    time.sleep(2)
    if not blinker.is_alive():
        blinker = Blinker(1, 5, x)
        blinker.start()        
        print("  Restart")
    else:
        print("  Blinker is running, wait a bit")
        
print("Main loop done")
