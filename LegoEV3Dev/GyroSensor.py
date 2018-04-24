# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:04:19 2018

@author: jareng
"""

import rpyc

# Remote Python Call  RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely

gs = ev3.GyroSensor("in1")

print(gs.angle)


"""

    print(gs.angle)
 
    print(gs.rate)

    Note to reset the angle call the rate one time

"""