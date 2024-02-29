import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt11.ui")[0]


class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        
    def printStar(self, a):
        s = ""
    
        for i in range(a):
            s += "*"
    
        return "{}\n".format(s)
    

    def isClick(self):
        str_first = self.le_first.text()
        str_last = self.le_last.text()
        
        first = int(str_first)
        last = int(str_last)
        
        res = ""
        for i in range(first, last+1):
            res += self.printStar(i)
        
        self.pte.setPlainText(res)
        # self.pte.setText(res)
    
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
