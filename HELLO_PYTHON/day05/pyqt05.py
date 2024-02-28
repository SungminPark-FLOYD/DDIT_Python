import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        
    def isClick(self):
        aa = [1,2,3,4,5, 6,7,8,9,10,
                11,12,13,14,15, 16,17,18,19,20,
                21,22,23,24,25, 26,27,28,29,30,
                31,32,33,34,35, 36,37,38,39,40,
                41,42,43,44,45]
        
        for i in range(1000):
            ran = int(random()*45)
            a = aa[0]
            aa[0] = aa[ran]
            aa[ran] = a
            
        
        self.ln1.display(aa[0]) 
        self.ln2.display(aa[1]) 
        self.ln3.display(aa[2]) 
        self.ln4.display(aa[3]) 
        self.ln5.display(aa[4]) 
        self.ln6.display(aa[5]) 
            
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
