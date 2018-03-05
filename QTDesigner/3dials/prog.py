# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:21:45 2018

@author: Win10User


C:\python>pyuic5 -x firstgui.ui -o firstgui.py

"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dials import Ui_dials
import random

class MyFirstGuiProgram(Ui_dials):
    def __init__(self, dialog):
        Ui_dials.__init__(self)
        self.setupUi(dialog)


        self.pushButton_1.clicked.connect(self.luckyButton)
        self.pushButton_2.clicked.connect(self.mixButton)


    def mixButton(self, value):
        print("Lag saft")
        a = self.dial_1.value()
        print("  Verdi A %d" % a)

        a = self.dial_2.value()
        print("  Verdi B %d" % a)

        a = self.dial_3.value()
        print("  Verdi C %d" % a)







    def luckyButton(self, value):
        print("Heldiggrisen")

        a = random.randint(20,90)
        self.dial_1.setProperty("value", a) 
        
        b = random.randint(20,90)
        self.dial_2.setProperty("value", b) 

        c = random.randint(20,90)
        self.dial_3.setProperty("value", c) 


   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
