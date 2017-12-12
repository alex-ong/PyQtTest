import sys
import datetime
from PyQt5 import *
#import PyQt5.QtGui  as QtG
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import time
import random

TIMER = 0.0
def update_label():    
    global TIMER
    print (time.time() - TIMER)
    TIMER = time.time()    
    ui.update()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        
        self.labels = []
        rows = 20
        cols = 30
        self.interval = 0
        font = QtGui.QFont("Arial", 16)
        for row in range(rows):
            for col in range(cols):
                label = QtWidgets.QLabel(Form)
                label.setGeometry(QtCore.QRect(col*40, row*20, 40, 16))
                label.setFont(font)
                label.privateVar1 = int(random.random() * 99)
                label.privateVar2 = int(random.random() * 5) + 1
                self.labels.append(label)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def update(self):
        for (i,label) in enumerate(self.labels):
            label.privateVar1 += label.privateVar2
            label.privateVar1 %= 100            
            string = str(label.privateVar1).zfill(2)
            label.setText(string)
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.label.setText(_translate("Form", plsupdatethis))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(0)  # every 10,000 milliseconds

    sys.exit(app.exec_())