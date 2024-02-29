import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt08.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        
        
    def isClick(self):
        le1 = self.le1.text()
        le2 = self.le2.text() 
        lee1 = int(le1)
        lee2 = int(le2)
        res = 0
        for i in range(lee1, lee2 + 1):
            res += i
        
        self.le3.setText("{}".format(res))
               
  
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
