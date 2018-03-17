# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIbinCount.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_binCount(object):
    def setupUi(self, binCount):
        binCount.setObjectName("binCount")
        binCount.resize(483, 163)
        self.buttonBox = QtWidgets.QDialogButtonBox(binCount)
        self.buttonBox.setGeometry(QtCore.QRect(60, 130, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.dial = QtWidgets.QDial(binCount)
        self.dial.setGeometry(QtCore.QRect(40, 0, 121, 131))
        self.dial.setMaximum(15)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(binCount)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 90, 31, 23))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_1 = QtWidgets.QLabel(binCount)
        self.label_1.setGeometry(QtCore.QRect(340, 30, 71, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(binCount)
        self.label_2.setGeometry(QtCore.QRect(270, 30, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(binCount)
        self.label_3.setGeometry(QtCore.QRect(200, 30, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_0 = QtWidgets.QLabel(binCount)
        self.label_0.setGeometry(QtCore.QRect(410, 30, 71, 21))
        self.label_0.setObjectName("label_0")

        self.retranslateUi(binCount)
        self.buttonBox.accepted.connect(binCount.accept)
        self.buttonBox.rejected.connect(binCount.reject)
        QtCore.QMetaObject.connectSlotsByName(binCount)

    def retranslateUi(self, binCount):
        _translate = QtCore.QCoreApplication.translate
        binCount.setWindowTitle(_translate("binCount", "Binary Counter"))
        self.label_1.setText(_translate("binCount", "Normal"))
        self.label_2.setText(_translate("binCount", "Normal"))
        self.label_3.setText(_translate("binCount", "Normal"))
        self.label_0.setText(_translate("binCount", "Normal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    binCount = QtWidgets.QDialog()
    ui = Ui_binCount()
    ui.setupUi(binCount)
    binCount.show()
    sys.exit(app.exec_())

