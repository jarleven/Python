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

    conda uninstall pillow
        

The following packages will be REMOVED:

    anaconda-navigator: 1.6.9-py36hc720852_0  https://repo.continuum.io/pkgs/main
    imageio:            2.2.0-py36had6c2d2_0  https://repo.continuum.io/pkgs/main
    pillow:             5.1.0-py36h0738816_0  anaconda
    scikit-image:       0.13.0-py36h6dffa3f_1 https://repo.continuum.io/pkgs/main
    

    conda install pillow=4.0.0
    conda install anaconda-navigator
    conda install scikit-image

    https://sites.google.com/site/ev3python/learn_ev3_python/rpyc

"""

# Remote Python Call  RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')   # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']               # import ev3dev.ev3 remotely
PIL   = conn.modules['PIL']


lcd = ev3.Screen()
lcd.clear()



#logo = Image.open('mouth.bmp')

#logo.show(logo)
#lcd.image.paste(logo, (0,0))
#lcd.update()
sleep(20)