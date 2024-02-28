import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        
    def isClick(self):
        mine = self.le_mine.text()
        com = ""
        res = ""
        ran = random()
        if ran > 0.5 :
            com = "홀"
        else:
            com = "짝"
            
        if mine == com:
            res = "이김"
        else :
            res = "짐"
        
        self.le_com.setText(com)
        self.le_result.setText(res)
  
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
