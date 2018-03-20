
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUItimer import Ui_timer
import random

class TimerExample(Ui_timer):
    def __init__(self, dialog):
        Ui_timer.__init__(self)
        self.setupUi(dialog)

        self.pushButton.clicked.connect(self.mixButton)


    def stopSingleShot(self):
        print("We got called by a timer event!")
        self.label.setText("Timer done !")

    def mixButton(self, value):

        a = 5000
        print("Throw the timer callback in %dms" % a)
        
        QtCore.QTimer.singleShot(a, self.stopSingleShot)
        self.label.setText("Wait %dms" % a)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = TimerExample(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
