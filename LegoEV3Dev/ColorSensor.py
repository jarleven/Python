# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:50:49 2018

@author: jareng
"""

import rpyc

# Remote Python Call  RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely

cs = ev3.ColorSensor("in1")

# The color properties
while True:
    #print(cs.ambient_light_intensity)
    #print(cs.blue)
    #print(cs.green)
    #print(cs.red)
    #print(cs.color)
    print(cs.reflected_light_intensity)
   
"""
 For cs.color we get the following values back 
    
    0: No color
    1: Black
    2: Blue
    3: Green
    4: Yellow
    5: Red
    6: White
    7: Brown
"""