# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myfirstgui(object):
    def setupUi(self, myfirstgui):
        myfirstgui.setObjectName("myfirstgui")
        myfirstgui.resize(378, 297)
        self.buttonBox = QtWidgets.QDialogButtonBox(myfirstgui)
        self.buttonBox.setGeometry(QtCore.QRect(-230, 190, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.dial = QtWidgets.QDial(myfirstgui)
        self.dial.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.progressBar = QtWidgets.QProgressBar(myfirstgui)
        self.progressBar.setGeometry(QtCore.QRect(20, 150, 141, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(myfirstgui)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 120, 31, 23))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(myfirstgui)
        self.label.setGeometry(QtCore.QRect(30, 120, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(myfirstgui)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 181, 271))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(myfirstgui)
        self.buttonBox.accepted.connect(myfirstgui.accept)
        self.buttonBox.rejected.connect(myfirstgui.reject)
        QtCore.QMetaObject.connectSlotsByName(myfirstgui)

    def retranslateUi(self, myfirstgui):
        _translate = QtCore.QCoreApplication.translate
        myfirstgui.setWindowTitle(_translate("myfirstgui", "My First Gui!"))
        self.label.setText(_translate("myfirstgui", "Normal"))
        self.label_2.setText(_translate("myfirstgui", "Bilde"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myfirstgui = QtWidgets.QDialog()
    ui = Ui_myfirstgui()
    ui.setupUi(myfirstgui)
    myfirstgui.show()
    sys.exit(app.exec_())

