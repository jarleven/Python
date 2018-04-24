# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:08:42 2018

@author: jareng
"""

import rpyc

# Remote Python Call  RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely

ts1 = ev3.TouchSensor("in1")
ts2 = ev3.TouchSensor("in2")

ev3.Leds.set_color(ev3.Leds.LEFT,  ev3.Leds.YELLOW)
ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)

# Colors can be RED, GREEN, YELLOW, ORANGE or AMBER.


while True:

    if ts1.value():
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    else:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    
    if ts2.value():
        break
    
ev3.Sound.speak("Goodbye").wait()
