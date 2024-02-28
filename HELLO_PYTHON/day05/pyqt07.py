import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt07.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.isClick)
        self.pb2.clicked.connect(self.isClick)
        self.pb3.clicked.connect(self.isClick)
        self.pb4.clicked.connect(self.isClick)
        self.pb5.clicked.connect(self.isClick)
        self.pb6.clicked.connect(self.isClick)
        self.pb7.clicked.connect(self.isClick)
        self.pb8.clicked.connect(self.isClick)
        self.pb9.clicked.connect(self.isClick)
        self.pb0.clicked.connect(self.isClick)
        self.pbCall.clicked.connect(self.call)
        
    def isClick(self):
        phone = self.le.text();
        btn = self.sender()
        btn_text = btn.text()        
        phone += btn_text
        
        self.le.setText(phone)
        
    def call(self):
        phone = self.le.text(); 
        QMessageBox.about(self,'Calling~~',phone)
        
  
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
