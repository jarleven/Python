# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:18:02 2018

@author: jareng
"""

# https://sites.google.com/site/ev3python/learn_ev3_python/screen/bmp-image-collection

import rpyc
from time import sleep
#import image
from PIL import Image

"""
     conda install pillow
     conda install -c anaconda pillow 

"""

# Remote Python Call  RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely


lcd = ev3.Screen()

logo = image.open('mouth.bmp')
lcd.image.paste('mouth.bmp', (0,0))
lcd.update()
sleep(20)