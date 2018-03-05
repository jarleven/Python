# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dials.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dials(object):
    def setupUi(self, dials):
        dials.setObjectName("dials")
        dials.resize(673, 371)
        self.buttonBox = QtWidgets.QDialogButtonBox(dials)
        self.buttonBox.setGeometry(QtCore.QRect(570, 330, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.dial_1 = QtWidgets.QDial(dials)
        self.dial_1.setGeometry(QtCore.QRect(10, 80, 211, 181))
        self.dial_1.setNotchesVisible(True)
        self.dial_1.setObjectName("dial_1")
        self.dial_2 = QtWidgets.QDial(dials)
        self.dial_2.setGeometry(QtCore.QRect(230, 80, 211, 181))
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName("dial_2")
        self.dial_3 = QtWidgets.QDial(dials)
        self.dial_3.setGeometry(QtCore.QRect(450, 80, 211, 181))
        self.dial_3.setNotchesVisible(True)
        self.dial_3.setObjectName("dial_3")
        self.pushButton_1 = QtWidgets.QPushButton(dials)
        self.pushButton_1.setGeometry(QtCore.QRect(170, 330, 191, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(dials)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 330, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dials)
        self.buttonBox.accepted.connect(dials.accept)
        self.buttonBox.rejected.connect(dials.reject)
        QtCore.QMetaObject.connectSlotsByName(dials)

    def retranslateUi(self, dials):
        _translate = QtCore.QCoreApplication.translate
        dials.setWindowTitle(_translate("dials", "Saft"))
        self.pushButton_1.setText(_translate("dials", "Eg føler meg heldig"))
        self.pushButton_2.setText(_translate("dials", "Miks saft"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dials = QtWidgets.QDialog()
    ui = Ui_dials()
    ui.setupUi(dials)
    dials.show()
    sys.exit(app.exec_())

