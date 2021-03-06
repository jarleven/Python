
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUItimer import Ui_timer
import random

class TimerExample(Ui_timer):
    def __init__(self, dialog):
        Ui_timer.__init__(self)
        self.setupUi(dialog)

        self.pushButton.clicked.connect(self.timerButton)


    def stopSingleShot(self):
        print("We got called by a timer event!")
        self.label.setText("Timer done !")

    def timerButton(self, value):

        a = 5000
        print("Fire the singleShot timer in %dms" % a)
        self.label.setText("Wait %dms" % a)

        QtCore.QTimer.singleShot(a, self.stopSingleShot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = TimerExample(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
