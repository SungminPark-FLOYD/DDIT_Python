import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt04.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        
    def isClick(self):
        dan = self.le.text()
        dan = int(dan)        
        res = ""
        for i in range(1, 9+1) :
            # res += str(dan) + " * " + str(i) + " = " + str(i * dan) + "\n"
            res += "{} * {} = {}\n".format(dan, i, dan*i)

        
        self.te.setText(res)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
