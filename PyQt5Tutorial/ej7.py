# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:08:28 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        self.statusBar().showMessage('Lista')
        self.setGeometry(450, 450, 350, 250)
        self.setWindowTitle('Barra de Estados')
        self.show()
    

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__== '__main__':
    main()