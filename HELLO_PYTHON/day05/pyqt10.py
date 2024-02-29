import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt10.ui")[0]


class WindowClass(QMainWindow, form_class):
    global ran
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        self.ran = int(random()*100)+1
        print(self.ran)
        
    def isClick(self):
        mine = self.le.text()
        a = int(mine)
        
        res = ""
        if a > self.ran :
            res = "DOWN"
        if a < self.ran :
            res = "UP" 
        if a == self.ran :
            QMessageBox.about(self,'정답입니다',"정답 : {}".format(a))
            return
                 
        b = self.te.toPlainText()   
        self.te.setText("{}{}\t{}\n".format(b,a, res))
        self.le.setText("")
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
