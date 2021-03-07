# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:36:46 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)

from PyQt5.QtGui import QColor


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        col = QColor (0,0,0)
        self.button = QPushButton('Dialogo', self)
        self.button.move(20,20)
        
        self.button.clicked.connect(self.showDialog)
        
        self.frame = QFrame(self)
        
        #Tengo que buscar el significado de esta ultima linea de código
        self.frame.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frame.setGeometry(130, 22, 200, 200)
        
        self.setGeometry(500, 500, 450, 350)
        
        self.setWindowTitle('Dialogo Color')
        self.show()
        
    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame.setStyleSheet('QWidget { background-color: %s }' % col.name())
            
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__== '__main__':
    main()
    

            