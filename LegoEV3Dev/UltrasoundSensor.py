# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:15:10 2018

@author: jareng
"""

import rpyc


# Remote Python Call  RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely

ultrasonic = ev3.UltrasonicSensor('in1')

print("Avstanden er %f" % ultrasonic.distance_centimeters)
    