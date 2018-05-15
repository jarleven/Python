# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:48:19 2018

@author: jareng
"""

import rpyc


# Remote Python Call   RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.1.135')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely

# In the simple form we can set the left LED with yellow color.
ev3.Leds.set_color(ev3.Leds.LEFT,  ev3.Leds.YELLOW)


# Code below will loop all the colors available on both LEDs of the EV3
# Colors can be RED, GREEN, YELLOW, ORANGE or AMBER.
colors=[ev3.Leds.RED, ev3.Leds.GREEN, ev3.Leds.YELLOW, ev3.Leds.ORANGE, ev3.Leds.AMBER]

while True:
    for color in colors:
        ev3.Leds.set_color(ev3.Leds.LEFT,  color)
        ev3.Leds.set_color(ev3.Leds.RIGHT, color)
