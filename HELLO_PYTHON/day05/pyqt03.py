import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt03.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        
    def isClick(self):
        num1 = self.pte01.toPlainText()
        num2 = self.pte02.toPlainText()
        
        num1 = int(num1)
        num2 = int(num2)
        
        mul = num1 * num2
        
        self.pte03.setPlainText(str(mul))
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
