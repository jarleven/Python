# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUItimer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_timer(object):
    def setupUi(self, timer):
        timer.setObjectName("timer")
        timer.resize(303, 113)
        self.buttonBox = QtWidgets.QDialogButtonBox(timer)
        self.buttonBox.setGeometry(QtCore.QRect(0, 50, 101, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(timer)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(timer)
        self.label.setGeometry(QtCore.QRect(130, 20, 111, 21))
        self.label.setObjectName("label")

        self.retranslateUi(timer)
        self.buttonBox.rejected.connect(timer.reject)
        self.buttonBox.accepted.connect(timer.accept)
        QtCore.QMetaObject.connectSlotsByName(timer)

    def retranslateUi(self, timer):
        _translate = QtCore.QCoreApplication.translate
        timer.setWindowTitle(_translate("timer", "Timer"))
        self.pushButton.setText(_translate("timer", "Timer"))
        self.label.setText(_translate("timer", "Idle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    timer = QtWidgets.QDialog()
    ui = Ui_timer()
    ui.setupUi(timer)
    timer.show()
    sys.exit(app.exec_())

