# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:21:45 2018

@author: Win10User


C:\python>pyuic5 -x firstgui.ui -o firstgui.py

"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from firstgui import Ui_myfirstgui

class MyFirstGuiProgram(Ui_myfirstgui):
    def __init__(self, dialog):
        Ui_myfirstgui.__init__(self)
        self.setupUi(dialog)

        # Connect "dial" dialog with a custom function (onDialValueChanged)
    
        self.dial.valueChanged.connect(self.onDialValueChanged)


    def onDialValueChanged(self, value):

        text = "Dial value: {v}".format(v=value)
        print(text)
        text = "Dial value: %d" % value
        print(text)
        
        self.progressBar.setProperty("value", value)
        self.lcdNumber.setProperty("value", value)

        self.lcdNumber.setSegmentStyle(2) # Flat segment
        palette = self.lcdNumber.palette()

        # foreground color
        if value > 50:
            palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
            self.label.setText("Warning")
            image = QtGui.QImage(QtGui.QImageReader("image.png").read())
            self.label_2.setPixmap(QtGui.QPixmap(image))
            #label.show()


        else:
             palette.setColor(palette.WindowText, QtGui.QColor(0, 255, 50))
             self.label.setText("Normal")   

        # set the palette
        self.lcdNumber.setPalette(palette)


   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
