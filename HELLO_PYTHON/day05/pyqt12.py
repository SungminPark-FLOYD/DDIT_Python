import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt12.ui")[0]


class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.isClick)
        self.com = self.randomNum()
        
    def randomNum(self):
        arr = [1,2,3,4,5,6,7,8,9]
        
        for i in range(1000):
            ran = int(random()*9)
            a = arr[0]
            arr[0] = arr[ran]
            arr[ran] = a
    
        return "{}{}{}".format(arr[0], arr[1], arr[2])
    
    def getS(self, ulist):
        a = 0
        carr = list(self.com)
        
        if carr[0] == ulist[0] : a += 1
        if carr[1] == ulist[1] : a += 1
        if carr[2] == ulist[2] : a += 1
        
        return a
    def getB(self, ulist):
        a = 0
        carr = list(self.com)
        
        if carr[0] == ulist[1] or carr[0] == ulist[2] : a += 1
        if carr[1] == ulist[0] or carr[1] == ulist[2] : a += 1
        if carr[2] == ulist[0] or carr[2] == ulist[1] : a += 1
        
        return a
       
    def isClick(self):
        user = self.le.text()
        res = ""
        ulist = list(user)
        
        s = self.getS(ulist)
        b = self.getB(ulist)
        
        res = "{}\t{}S{}B".format(user, s, b)
        
        if s == 3:
            QMessageBox.about(self,'정답입니다',"정답 : {}".format(self.com))
        
        self.te.append(res)
        self.le.setText("")
         
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
   
