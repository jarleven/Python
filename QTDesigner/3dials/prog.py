# -*- coding: utf-8 -*-
"""

pyuic5 -x dials.ui -o dials.py

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


    def stopPumpA(self):
        print("Pumpe A stop")

    def stopPumpB(self):
        print("Pumpe B stop")

    def stopPumpC(self):
        print("Pumpe C stop")
    
    # Read the dials and send out the values to the terminal
    def mixButton(self, value):
        print("Lag saft")
        a = self.dial_1.value()
        print("  Verdi A %d" % a)
        QtCore.QTimer.singleShot(a*100, self.stopPumpA)

        b = self.dial_2.value()
        print("  Verdi B %d" % b)
        QtCore.QTimer.singleShot(b*100, self.stopPumpB)

        c = self.dial_3.value()
        print("  Verdi C %d" % c)
        QtCore.QTimer.singleShot(c*100, self.stopPumpC)



    # Set the dials to random values
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
