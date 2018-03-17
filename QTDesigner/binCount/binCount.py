
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUIbinCount import Ui_binCount



class MyFirstGuiProgram(Ui_binCount):
    def __init__(self, dialog):
        Ui_binCount.__init__(self)
        self.setupUi(dialog)


        self.lcdNumber.setSegmentStyle(2) # Flat segment
    
        self.dial.valueChanged.connect(self.onDialValueChanged)


    def onDialValueChanged(self, value):

	        
        self.lcdNumber.setProperty("value", value)
 

	# Loop through the label_1 , label_2 , label_3 and label_4 objects
	# Set the labels to represent the bits in the values we get from the dial
        for i in range(0,4):

            # Mask out each bit in the value we get from the dial.
            # Bitwise operation https://wiki.python.org/moin/BitwiseOperators
            thisBit = value >> i            
            thisBit = thisBit & 1 

            # This will replace the ordinary way of writing the string TRUE
            # self.label_1.setText("TRUE")
 
            xlabel = getattr(self, "label_"+str(i))
            if thisBit == True:     
                xlabel.setText("TRUE")
            else:
                xlabel.setText("FALSE")

        # Just print some debug text for the decimal and binary value we get from the dial
        text = "Dial value: %02d  - Binary %s" % (value, format(value, '04b'))
        print(text)
        
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
