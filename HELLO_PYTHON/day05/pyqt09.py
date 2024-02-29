import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt09.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        self.le_mine.returnPressed.connect(self.isClick)
        
    def isClick(self):
        mine = self.le_mine.text()
        com = ""
        res = ""
        ran = random()
        if ran > 0.66 :
            com = "가위"
        elif ran > 0.33:
            com = "바위"
        else :
            com = "보"
            
        if mine == "보" and  com == "가위":
            res = "짐"
        if mine == "가위" and  com == "바위":
            res = "짐"
        if mine == "바위" and  com == "보":
            res = "짐"
            
        if mine == "보" and  com == "바위":
            res = "이김"
        if mine == "가위" and  com == "보":
            res = "이김"
        if mine == "바위" and  com == "가위":
            res = "이김"    
            
        if mine == com:
            res = "비김"
        
        self.le_com.setText(com)
        self.le_result.setText(res)
  
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
