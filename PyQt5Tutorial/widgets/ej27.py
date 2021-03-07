# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:37:27 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

import sys

class Example (QWidget):
    
    def __init__ (self):  
        super().__init__()
              
        self.initUI()

    def initUI(self):
        
        checkBox = QCheckBox ('Mostrar Titulo', self)
        checkBox.move(20,20)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(300,300,350,250)
        self.setWindowTitle('QCheckBox')
        self.show()
        
    def changeTitle (self, state):
        
        if state == Qt.Checked:
            self.setWindowTitle ('QCheckBox')
        else:
            self.setWindowTitle ('Titulo Oculto')
        
def main():
    app = QApplication (sys.argv)
    ex = Example()
    sys.exit (app.exec_())
    
if __name__== '__main__':
    main()
    

